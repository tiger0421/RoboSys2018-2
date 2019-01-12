#!/usr/bin/env python

import rospy
import numpy as np
import cv2
import os.path
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class color_extract(object):
    def __init__(self):
        self.sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.callback)
        self.pub = rospy.Publisher("masked_image", Image, queue_size = 10)

        self._bridge = CvBridge()

    def callback(self, data):
        try:
            cv_image = self._bridge.imgmsg_to_cv2(data, "bgr8")
            hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
            masked_image = cv2.inRange(hsv, np.array([0, 0, 0]), np.array([60, 255, 60]))
            self.pub.publish(self._bridge.cv2_to_imgmsg(masked_image, "mono8"))

        except CvBridgeError, e:
            print e

if __name__ == "__main__":
    rospy.init_node("color_extract")
    color = color_extract()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
