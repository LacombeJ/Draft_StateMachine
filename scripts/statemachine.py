#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros

import random

# Example state machine that attempts to complete all tasks

# Init state
# Returns whether initialization completed or failed
class Init(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['completed','failed'])
        
    def execute(self, userdata):
        print 'Initializing...'
        return 'completed'


# Next state
# Determines the where the 'robot' should move next
# Returns found if determined where the robot should move
# Returns completed if there is nowhere else to move (all tasks completed)
class Next(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['completed','found'],
                                    input_keys=['task','success','completed'],
                                    output_keys=['next'])
        
    def execute(self, userdata):
        print 'Determining next state...'
        
        task = userdata.task
        success = userdata.success
        completed = userdata.completed
        
        # A task has just exited
        if (task != None):
            completed[task] = success
            index = nextIndex(completed)
            if index != -1:
                userdata.next = index
                return 'found' # A task was found
            else:
                return 'completed' # All tasks are completed
            
        # Init has just taken place
        else:
            userdata.next = 0
            return 'found'


# Move state
# Returns task to transition to
class Move(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['to_task0','to_task1','to_task2','failed'],
                                    input_keys=['next'])
        
    def execute(self, userdata):
        next = userdata.next
        print 'Moving to task {}'.format(next)
        
        if next == 0:
            return 'to_task0'
        elif next == 1:
            return 'to_task1'
        elif next == 2:
            return 'to_task2'
        
        return 'failed'

# --------------------------------------------------------------------------------- #

# Generic Task
class Task(smach.State):

    def __init__(self, index):
        smach.State.__init__(self, outcomes=['exit'],
                                    output_keys=['task','success'])
        self._index = index
        
    def execute(self, userdata):
        print 'Attempting task {}'.format(self._index)
        success = randomBool()
        if success:
            print "Task {} succeeded".format(self._index)
        else:
            print "Task {} failed".format(self._index)
        userdata.task = self._index
        userdata.success = success
        return 'exit'

# --------------------------------------------------------------------------------- #

# Initializes user data
def initializeData(userdata):
    userdata.next = None
    userdata.task = -1
    userdata.success = None
    userdata.completed = {
        0:False,
        1:False,
        2:False
    }
    
# Return first index of incomplete task or -1 if all tasks are completed
def nextIndex(completed):
    for c in completed:
        if not completed[c]:
            return c
    return -1

# Returns a random bool
def randomBool():
    return random.random() > 0.5

# Main
# Creates state machine
def main():

    rospy.init_node('state_machine')

    sm = smach.StateMachine(outcomes=['completed','failed'])
    
    initializeData(sm.userdata)
    
    with sm:
    
        # Primary States
    
        smach.StateMachine.add('INIT', Init(),
                            transitions={'completed':'NEXT',
                                        'failed':'failed'})
                                        
        smach.StateMachine.add('NEXT', Next(),
                            transitions={'completed':'completed',
                                        'found':'MOVE'})
                        
        smach.StateMachine.add('MOVE', Move(),
                            transitions={'to_task0':'TASK0',
                                        'to_task1':'TASK1',
                                        'to_task2':'TASK2',
                                        'failed':'NEXT'})
                                        
        # Task States
        
        smach.StateMachine.add('TASK0', Task(0), transitions={'exit':'NEXT'})
        
        smach.StateMachine.add('TASK1', Task(1), transitions={'exit':'NEXT'})
        
        smach.StateMachine.add('TASK2', Task(2), transitions={'exit':'NEXT'})
        
        
    outcome = sm.execute()



if __name__ == '__main__':
    main()
