
import roslib
import rospy
import smach
import smach_ros


# Go through gate sub-state-machine
def Gate():

    sm = smach.StateMachine(outcomes=['done'])
    
    with sm:
    
        smach.StateMachine.add('DetectionMode', DetectionMode(),
                            transitions={'next':'DetectionStatus'})
                                        
        smach.StateMachine.add('DetectionStatus', DetectionStatus(),
                            transitions={'timeout':'Recovery',
                                        'not_found':'DetectionStatus',
                                        'not_aligned':'Align',
                                        'aligned':'DVL'})
                        
        smach.StateMachine.add('Recovery', Recovery(),
                            transitions={'next':'DetectionStatus'})
                            
        smach.StateMachine.add('Align', Align(),
                            transitions={'next':'DetectionStatus'})
                            
        smach.StateMachine.add('DVL', DVL(),
                            transitions={'next':'BarrelRoll'})
                            
        smach.StateMachine.add('BarrelRoll', BarrelRoll(),
                            transitions={'next':'NextTask'})
                            
        smach.StateMachine.add('NextTask', NextTask(),
                            transitions={'next':'done'})
    
    return sm
    
    
# Set object detector to gate mode
class DetectionMode(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        

# Check object detection status
class DetectionStatus(smach.State):

    def __init__(self):
        smach.State.__init__(self,outcomes=['timeout,not_found,
                                            'not_aligned','aligned'])
        
    def execute(self, userdata):
        return 'aligned'


# Perform recovery behaviors
class Recovery(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        
        
# Local move to alignment
class Align(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        

# Disengage DVL
class DVL(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        
        
# Peform a barrel roll
class BarrelRoll(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        
        
# Move to next task
class NextTask(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        



