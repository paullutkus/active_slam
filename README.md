## STEP 1: Place robot within the Gazebo environment

Setting up environment variable to the robot model.

```
export TURTLEBOT3_MODEL=waffle_pi

source ~/.bashrc
```

 Launching Gazebo and placing the robot Turtlebot3 Waffle pi model in it.
 
 ```
 roslaunch ros_autonomous_slam turtlebot3_maze1.launch
 ```
 
 We need to keep this process running always and execute other commands in a different terminal.
 
 
 ## STEP 2 : Performing Autonomous exploration of the environment and generating the Map
 
 Starting the SLAM node in the Navigation stack with a custom modified RVIZ file to monitor the mapping of the environment.
 
 ```
 roslaunch ros_autonomous_slam autonomous_explorer.launch 
 ```
 
 We then set up Exploration region for RRT in RVIZ Window using the RVIZ **Publish Points** option.
 
 For saving the generated map which is a occupancy grid
 
 ```
 rosrun map_server map_saver -f my_map
 ```
 
 ## STEP 3: Perform pathplanning
 
We perform pathplanning using the Navigation stack of the ROS. To open up a RVIZ window showing the Robot location within the previously constructed map.

```
roslaunch ros_autonomous_slam turtlebot3_navigation.launch
```


 
