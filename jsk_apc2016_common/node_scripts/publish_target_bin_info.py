#!/usr/bin/env python

import rospy
from jsk_apc2016_common.msg import BinInfo, BinInfoArray


class PublishTargetBinInfo(object):
    def __init__(self):
        self.bin_info_dict = {}
        self.bin_info_array_sub = rospy.Subscriber('~input/bin_info_array', BinInfoArray, self.callback)
        self.target_bin_info_pub = rospy.Publisher('~target_bin_info', BinInfo, queue_size=5)

        rate = rospy.Rate(rospy.get_param('rate', 10))
        while not rospy.is_shutdown():
            if self.bin_info_dict == {}:
                rate.sleep()
            target_bin_name = rospy.get_param('~target_bin_name')
            if target_bin_name not in 'abcdefghijkl' or target_bin_name == '':
                rate.sleep()
                continue
            self.bin_info_dict[target_bin_name].header.seq = (
                    self.bin_info_dict[target_bin_name].header.seq + 1)
            target_bin_info = self.bin_info_dict[target_bin_name]
            target_bin_info.header.stamp = rospy.Time.now()
            self.target_bin_info_pub.publish(target_bin_info)
            rate.sleep()

    def bin_info_array_to_dict(self, bin_info_array):
        bin_info_dict = {}
        for bin_ in bin_info_array.array:
            bin_info_dict[bin_.name] = bin_
        return bin_info_dict

    def callback(self, bin_info_array):
        self.bin_info_dict = self.bin_info_array_to_dict(bin_info_array)


if __name__ == '__main__':
    rospy.init_node('publish_target_bin_info')
    publish_target_bin_info = PublishTargetBinInfo()



