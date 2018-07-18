# #!/usr/bin/env python
# import rospy
# from std_msgs.msg import Float64
# import sys
# import copy
# import rospy
# import moveit_commander
# import moveit_msgs.msg
# import geometry_msgs.msg
# import json




# from itertools import izip_longest

# def grouper(n, iterable, fillvalue=None):
#     "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
#     args = [iter(iterable)] * n
#     return izip_longest(fillvalue=fillvalue, *args)



# moveit_commander.roscpp_initialize(sys.argv)
# robot = moveit_commander.RobotCommander()
# scene = moveit_commander.PlanningSceneInterface()
# group = moveit_commander.MoveGroupCommander("manipulator")
# ip_waypoints = []
# op_waypoints = []
# zvals = []
# target_z = 0.300
# first = 0
# tolerance = 0.008

# firstTime = True

# FILE_PATH = "/home/jrv/Research/RoboticArcitecture/abb_experimental_ws/Pattern/GFT.txt"

# # def callback(data):
# #     wpose = group.get_current_pose().pose
# #     global first
# #     #print ("x,y:" , wpose.position.x," ", wpose.position.y)
# #     print ( "I heard ", data.data )
# #     if(first <len(ip_waypoints)):     
# #       coordinates = ip_waypoints[first]
# #       if  ( ( wpose.position.x <= (float(coordinates[0])/1000 + tolerance )) and (wpose.position.x >= (float(coordinates[0])/1000 - tolerance )) and
# #             ( wpose.position.y <= (float(coordinates[1])/1000 + tolerance )) and (wpose.position.y >= (float(coordinates[1])/1000 - tolerance )) ):
# #         print first,":x,y,z,data:" , wpose.position.x," ", wpose.position.y," ", wpose.position.z, " reading:", data.data,"correction :", target_z - data.data
# #         zvals.append(data.data)
# #         corrected_coordinate = []
# #         corrected_coordinate.append(coordinates[0])
# #         corrected_coordinate.append(coordinates[1])
# #         zdiff = target_z - data.data
# #         corrected_coordinate.append((wpose.position.z - zdiff)*1000)
# #         op_waypoints.append(corrected_coordinate)

# #         first +=1

# #     if(len(ip_waypoints)==len(op_waypoints)):
# #       for point in op_waypoints:
# #         print point
# #       print zvals
# #       opfile = open('/home/jrv/Research/RoboticArcitecture/abb_experimental_ws/Pattern/Corrected/GFT_op.txt', 'w')
# #       for item in zvals:
# #         opfile.write("%s\n" % item)


# #       #mover()
# #       print "============ Stopping the system..."
# #       rospy.sleep(5)
# #       rospy.signal_shutdown("We are done")

    
# def listener():

#     # In ROS, nodes are uniquely named. If two nodes with the same
#     # node are launched, the previous one is kicked off. The
#     # anonymous=True flag means that rospy will choose a unique
#     # name for our 'listener' node so that multiple listeners can
#     # run simultaneously.

#     rospy.init_node('trackgort_node', anonymous=True)

#     # spin() simply keeps python from exiting until this node is stopped
#     if(len(ip_waypoints)!=len(op_waypoints)):
#      rospy.spin()

# def mover():
#   global firstTime
#   if(len(op_waypoints)==len(ip_waypoints) and firstTime == True):
#     move_group_output()
#     firstTime = False



# def move_group_output():

#   print "============ Starting Printing setup"
#   moveit_commander.roscpp_initialize(sys.argv)
#   robot = moveit_commander.RobotCommander()
#   scene = moveit_commander.PlanningSceneInterface()
#   group = moveit_commander.MoveGroupCommander("manipulator")
#   display_trajectory_publisher = rospy.Publisher(
#                                       '/move_group/display_planned_path',
#                                       moveit_msgs.msg.DisplayTrajectory,
#                                       queue_size=20)

#   print "============ Waiting for RVIZ..."
#   rospy.sleep(10)

#   wpose = geometry_msgs.msg.Pose()  
#   wpose = group.get_current_pose().pose
#   print wpose
#   waypoints = []
#   for coordinates in op_waypoints:
#     wpose.position.x = float(coordinates[0])/1000
#     wpose.position.y = float(coordinates[1])/1000
#     wpose.position.z = float(coordinates[2])/1000
#     waypoints.append(copy.deepcopy(wpose))

#   (plan3, fraction) = group.compute_cartesian_path(
#                                waypoints,   # waypoints to follow
#                                0.01,        # eef_step
#                                0.0)         # jump_threshold
  
#   print "============ Waiting while RVIZ displays plan3..."
#   rospy.sleep(5)

#   is_safe = raw_input("Plan ok to exexute? : y/n ")
#   slow_move = raw_input("Move slow to checkpoints? : y/n ")

#   if(slow_move == 'y' and is_safe=='y'):
#     for coordinates1, coordinates2 in grouper(2, op_waypoints):
#       waypoints=[]
#       wpose.position.x = float(coordinates1[0])/1000
#       wpose.position.y = float(coordinates1[1])/1000
#       wpose.position.z = float(coordinates1[2])/1000
#       waypoints.append(copy.deepcopy(wpose))
#       wpose.position.x = float(coordinates2[0])/1000
#       wpose.position.y = float(coordinates2[1])/1000
#       wpose.position.z = float(coordinates2[2])/1000
#       waypoints.append(copy.deepcopy(wpose))
#       (plan, fraction) = group.compute_cartesian_path(
#                                  waypoints,   # waypoints to follow
#                                  0.01,        # eef_step
#                                  0.0)         # jump_threshold
#       #path_plan.append(plan)
#       if(is_safe=='y'):
#         print("Executing trajectory")
#         group.execute(plan)
#   else:
#     if(is_safe=='y'):
#       print("Executing trajectory")
#       group.execute(plan3)
                              
#   print "============ Waiting while RVIZ displays plan3..."
#   rospy.sleep(5)
#   collision_object = moveit_msgs.msg.CollisionObject()
#   moveit_commander.roscpp_shutdown()

#   print "============ STOPPING"



# if __name__ == '__main__':
#   lines = [line.rstrip('\n') for line in open(FILE_PATH) if line.startswith(("MoveL")) ]
#   ip_waypoints = []

#   print "TrackGort"

#   for line in lines:
#     line = line.split(']', 1)[0]
#     line = line[8:]
#     coordinates  = line.split(',')
#     ip_waypoints.append(coordinates)
    
#   rate = rospy.Rate(400) # 10hz

#   print(ser.name)
#   ser.write('/000R4D.')
#   time.sleep(0.5)
#   ser.write('/020D0059.')
#   seq = []
#   count = 1
#   listener()
