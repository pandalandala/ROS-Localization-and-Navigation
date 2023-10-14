#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../")))

from plugins import ObstacleGenerator

if __name__ == "__main__":
    obstacles = ObstacleGenerator()

    rospy.init_node("spawn_obstacles")
    obstacles.spawn()