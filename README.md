# ROS-Localization-and-Navigation

## Running the Project

After cloning this repo, you can rename the root folder as follows:

``` bash
├─catkin_ws
│  ├─build
│  ├─devel
│  └─src
```

After completing the project, you can launch it by running the following commands first -

``` bash
$ cd ~/catkin_ws
$ catkin_make
```

Then run the following commands before running `$ source ~catkin_ws/devel/setup.bash` first in **separate** terminals:

``` bash
$ roslaunch udacity_bot udacity_world.launch
$ roslaunch udacity_bot amcl.launch
```

If you want to send a goal to navigate the robot, run folowing commands:

``` bash
$ source ~catkin_ws/devel/setup.bash
$ rosrun udacity_bot navigation_goal.cpp
```

Then you will see the robot reaching the navigational goal.
