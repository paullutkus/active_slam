#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
from nav_msgs.msg import OccupancyGrid

mapData=OccupancyGrid()

def mapCallBack(data):
    global mapData
    mapData=data

#Assign endpoint marker
def node():
    global mapData

    rospy.init_node('rviz_marker')
    rateHz = rospy.get_param('~rate',100)	
    namespace = rospy.get_param('~namespace','')

    rate = rospy.Rate(rateHz)


    map_topic= rospy.get_param('~map_topic','map')
    rospy.Subscriber(map_topic, OccupancyGrid, mapCallBack)

    marker = Marker()
    marker_pub = rospy.Publisher('end_point', Marker, queue_size=10)


    marker.header.stamp = rospy.Time.now()
    marker.header.frame_id = mapData.header.frame_id

    #marker.header.stamp = rospy.Time.now()
    marker.ns = namespace
    marker.id = 3195

    marker.type = 3

    marker.action = Marker.ADD

    marker.scale.x = 1.0
    marker.scale.y = 1.0
    marker.scale.z = 1.0

    marker.color.r = 0.79
    marker.color.g = 0.83
    marker.color.b = 0.15
    marker.color.a = 1.0

    marker.pose.position.x = -3.25
    marker.pose.position.y = 2.0
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0

    marker.lifetime = rospy.Duration()

    #marker_pub.publish(marker)

    while not rospy.is_shutdown():
        marker_pub.publish(marker)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass
 

