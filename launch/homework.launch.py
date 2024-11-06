#!usr/bin/python3

import os
import sys
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackagePrefix

def generate_launch_description():
    ld = LaunchDescription()    
    return ld

def main(args=None):
    try:
        generate_launch_description()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()    