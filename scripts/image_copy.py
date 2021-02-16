#!/usr/bin/env python3
import sys
import time
import math
import rclpy
import numpy
import cv2
import sensor_msgs.msg

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from rclpy.node import Node

class MinimalStreamer(Node):

    def __init__(self):
        super().__init__('minimal_streamer')
        self.bridge = CvBridge()
        self.cv_image = None

        self.subscription = self.create_subscription(
            Image, "image", self.draw_callback, 10)
        self.publisherCompress_ = self.create_publisher(sensor_msgs.msg.CompressedImage, "compressed", 10)
        self.publisher_ = self.create_publisher(Image, "drawed", 10)
        self.subscription

    def draw_callback(self, img):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(img, "bgr8")
        except CvBridgeError as e:
            self.get_logger().info('cv_bridge error "%s"' % str(e))
        hei, wei = self.cv_image.shape[0:2]
        self.get_logger().info(str(self.cv_image.shape))
        cv2.line(self.cv_image, (0, 0), (wei, hei), (0, 255, 255), 1)
        cv2.line(self.cv_image, (0, hei), (wei, 0), (0, 255, 255), 1)
        self.publisher_.publish(self.bridge.cv2_to_imgmsg(self.cv_image, "bgr8"))
        time.sleep(0.03)
#        self.publisherCompress_.publish(self.bridge.cv2_to_compressed_imgmsg(self.cv_image))

def main(args=None):
    rclpy.init(args=args)
    
    minimal_streamer = MinimalStreamer()
    rclpy.spin(minimal_streamer)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main(sys.argv)
