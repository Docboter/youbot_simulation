# YouBot Simulation
This repository provides a simulation environment for the KUKA YouBot in Gazebo using ROS 2. The simulation includes a Gazebo world setup, the YouBot robot model, and a launch file for easy execution.

## Prerequisites
First update your system by running the following command in a terminal
``` 
sudo apt update
sudo apt upgrade
```
### ROS2 
Install the latest version of ROS 2 Humble by following the instructions [here](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) 

### Gazebo Classic
Install Gazebo Classic with the following command
```
sudo apt install gazebo
```

 ### Create your workspace
Create a workspace for ROS. 
Run the following code to create your workspace with the _src_ subdirectory.
 
```bash
mkdir -p your_workspace/src
```
>[!NOTE]
> You can use any name you like for your workspace. For the rest of this file we will assume you name it _your_workspace_

## Installing
In this section you will find the necessary packages for your Ros2 workspace, run the following command to get into the _your_workspace/src_ folder

```
cd your_workspace/src
```
Now you need to install the necessary packages with the following command:
```
git clone https://github.com/hsk-mobile-robotics/youbot_simulation.git

git clone -b ros2 https://github.com/ros-simulation/gazebo_ros_pkgs.git
```

### Build your ROS 2 workspace
After you have installed the necessary packages, go back to _your_workspace_ and build the workspace by using this command:
>[!IMPORTANT] 
>Make sure you are in the _your_workspace_ folder. 
```
colcon build 
```
If you do not want to build the workspace every time you change a file, you can use:
```
colcon build --symlink-install
```

### Source your workspace
Now you need to source the workspace by running:
```
source install/setup.bash
```

## Start the simulation
To start the simulation use the following command:
```
ros2 launch youbot_gazebo youxacro.launch.py
```

## Moving the Youbotmodel
Once the simulation is running, you can move the robot by sending a command to the ROS2 topic /cmd_vel.

##  Move in a circle
In this example we want the robot to move in a circle
In a new terminal, use 
```
ros2 topic pub --rate 1 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```

To stop the robot, use the following command 
```
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

## Drive the Youbot
You can move the robot manually with your keyboard using this command:
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
You should now be able to move the robot with your keybord.
>[!IMPORTANT] 
>Note that the terminal with the keybord must be the selected/active terminal.
