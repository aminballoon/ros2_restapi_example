cmake_minimum_required(VERSION 3.8)
project(ros2_restapi_example)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

################ BUILD DEPENDENCIES #################
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)

################ Install Python Module ################ 
ament_python_install_package(${PROJECT_NAME})

################ Install Python executables ################ 
install(PROGRAMS
  scripts/rest_server.py
  scripts/ros2_rest_client_get.py
  scripts/ros2_rest_client_post.py
  scripts/ros2_rest_client_put.py
  DESTINATION lib/${PROJECT_NAME}
)

################ INSTALL LAUNCH, ETC #################
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME})

ament_package()
