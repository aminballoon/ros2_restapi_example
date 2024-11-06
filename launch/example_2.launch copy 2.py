#!usr/bin/python3

import os
import sys
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackagePrefix

def generate_launch_description():
    ld = LaunchDescription()

    rest_server_path = os.path.join(FindPackagePrefix("ros2_restapi_example").find(package_name="ros2_restapi_example"), 
                               "lib", 
                               "ros2_restapi_example", 
                               "rest_server.py")

    run_server = ExecuteProcess(           
            name="REST Server",
            cmd=['python3', 
                str(rest_server_path), 
                "6699"],
            output='screen'        
    )

    ros2_rest_client_put = Node(
        package = 'ros2_restapi_example',
        executable = 'ros2_rest_client_put.py',
        output = 'screen',
        emulate_tty=True, 
        parameters=[{
            "host": "127.0.0.1",
            "port": 6699,
            "timer_frequency": 10
        }],
    )

    ros2_rest_client_post = Node(
        package = 'ros2_restapi_example',
        executable = 'ros2_rest_client_post.py',
        output = 'screen',
        emulate_tty=True, 
        parameters=[{
            "port": 6699
        }],
    )
    
    ld.add_action(run_server)
    ld.add_action(ros2_rest_client_put)
    ld.add_action(ros2_rest_client_post)
    

    return ld

def main(args=None):
    try:
        generate_launch_description()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()