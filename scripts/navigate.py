
import roslib
import rospy
import smach
import smach_ros


# Navigate to next task sub-state-machine
def Navigate():

    sm = smach.StateMachine(outcomes=['done'])
    
    with sm:
    
        smach.StateMachine.add('DetectionMode', DetectionMode(),
                            transitions={'next':'DetectionStatus'})
                                        
        smach.StateMachine.add('DetectionStatus', DetectionStatus(),
                            transitions={'not_found':'BeginSearch',
                                        'not_aligned':'Align',
                                        'aligned':'SampleBarHeading'})
                             
                                    
        smach.StateMachine.add('BeginSearch', BeginSearch(),
                            transitions={'next':'DetectionStatus'})
                            
        smach.StateMachine.add('Align', Align(),
                            transitions={'next':'DetectionStatus'})
                            
        smach.StateMachine.add('SampleBar', SampleBar(),
                            transitions={'next':'MoveAlongBar'})
                            
        smach.StateMachine.add('MoveAlongBar', MoveAlongBar(),
                            transitions={'next':'NextTask'})
                            
        smach.StateMachine.add('NextTask', NextTask(),
                            transitions={'next':'done'})
    
    return sm
    
    
# Set object detector to navigation bar mode
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


# Begin nav bar search pattern
class BeginSearch(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        
        
# Align to above bar
class Align(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        

# Sample bar heading
class SampleBar(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        
# Move along bar heading
class MoveAlongBar(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        
        
# Start next task
class NextTask(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['next'])
        
    def execute(self, userdata):
        return 'next'
        



