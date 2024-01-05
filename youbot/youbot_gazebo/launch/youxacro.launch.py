import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node

import xacro

def generate_launch_description():

    use_sim_time = LaunchConfiguration("use_sim_time")
    pkg_youbot_model_description = get_package_share_directory('youbot_model_description')
    
    # Get paths
    xacro_file =  os.path.join(pkg_youbot_model_description, 'urdf', 'youbot.urdf.xacro')
    #Gazebo
    pkg_youbot_gazebo = get_package_share_directory('youbot_gazebo')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')


    #Get xacro file and transform it into xml
    robot_description_config = xacro.process_file(xacro_file)
    robot_description = robot_description_config.toxml()
    params = {"robot_description": robot_description "use_sim_time": use_sim_time}



    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[params]
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        arguments=robot_description
    )

     # Visualize in RViz
    rviz = Node(
       package='rviz2',
       executable='rviz2',
      #arguments=['-d', os.path.join(pkg_youbot_rviz, 'config', 'config.rviz')],
       condition=IfCondition(LaunchConfiguration('rviz'))
    )

     # Setup to launch the simulator and Gazebo world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),       
       # launch_arguments={'gz_args': PathJoinSubstitution([
       #     pkg_youbot_model_description, 'sdf', 'youbotworld.sdf'
       # ])}.items(),
   )

    return LaunchDescription([
            
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='use sim time if true'),
        DeclareLaunchArgument(
            'rviz', 
            default_value='true',
            description='Open RViz.'),
            
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz,
        gazebo,
      
        ])
