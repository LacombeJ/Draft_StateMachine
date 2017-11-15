#!/usr/bin/env python


import roslib
import rospy
import smach
import smach_ros

# Sub-state machines
import gate
import navigate


# Main
# Creates state machine
def main():

    rospy.init_node('state_machine')

    sm = smach.StateMachine(outcomes=['completed'])
    
    with sm:
    
        smach.StateMachine.add('Start', Start(),
                            transitions={'done':'Navigate'})
                                        
        smach.StateMachine.add('Navigate', navigate.Navigate(),
                            transitions={'to_gate':'Gate',
                                        'to_buoy':'Buoy',
                                        'to_channel':'Channel'})
                                        
        smach.StateMachine.add('Gate', gate.Gate(),
                            transitions={'done':'Navigate'})
                            
        smach.StateMachine.add('Buoy', Buoy(),
                            transitions={'done':'Navigate'})
                            
        smach.StateMachine.add('Channel', Channel(),
                            transitions={'done':'Navigate'})
        
    outcome = sm.execute()



if __name__ == '__main__':
    main()
    
    
# Start Mission State
class Start(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])
        
    def execute(self, userdata):
        return 'done'
        
# Touch Buoy Task
class Buoy(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])
 
    def execute(self, userdata):
        return 'done'

# Go through Channel task
class Channel(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])
        
    def execute(self, userdata):
        return 'done'

