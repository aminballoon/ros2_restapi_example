#!/usr/bin/python3

import sys
import rclpy
import requests
from rclpy.node import Node
import time

class ExampleROS2(Node):
    """ Example ROS node for ROS101 session in ARV about call REST_API """
    def __init__(self, node_name:str, timeout=3) -> None:
        super().__init__(node_name)
         
        self.declare_parameter('host', "127.0.0.1")        
        self.declare_parameter('port', 5000)

        _host = str(self.get_parameter('host').value)
        _port = int(self.get_parameter('port').value)

        self.url = f"http://{_host}:{str(_port)}/arv"
        print("URL:", self.url)
        
        response = requests.get(f"{self.url}/get")
        print(response.status_code)
        if response.status_code == 200:
            self.get_logger().info('Get Respone %r' % (response.json(),))
        else:
            self.get_logger().warn('Get Respone %r' % (response.json(),))
        sys.exit()
        
def main(args=None):
    rclpy.init(args=args)
    node = ExampleROS2("Client_GET")
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print(' repeater stopped cleanly')
    except BaseException:
        print(' exception in repeater:', file=sys.stderr)
        raise
    finally:
        node.destroy_node()
        rclpy.shutdown() 

if __name__ == "__main__":
    main()
