# ROS-Localization-and-Navigation

## 1. Environment and Start

1. **OS**: Ubuntu 20.04 LTS

2. **ROS**: 1.0 Noetic LTS (Desktop-Full suggested)

3. Dependencies Installation:

``` bash
$ sudo apt install python-is-python3
$ sudo apt install ros-noetic-amcl
$ sudo apt install ros-noetic-base-local-planner
$ sudo apt install ros-noetic-map-server
$ sudo apt install ros-noetic-move-base
$ sudo apt install ros-noetic-navfn
```

4. Compile the project and Run (rename the root folder as `ros_motion_planning` first)

``` bash
$ cd ros_motion_planning/
$ catkin_make
$ cd ./src/sim_env/scripts/
$ sudo ./main.sh
```

5. Use **2D Nav Goal** to select the goal. Succeed!

## 2. File Tree

``` bash
ros_motion_planner
└── src
    ├── planner
    │   ├── global_planner
    │   ├── local_planner
    │   └── utils
    ├── sim_env             # simulation environment
    │   ├── config
    │   ├── launch
    │   ├── maps
    │   ├── meshes
    │   ├── models
    │   ├── rviz
    │   ├── scripts
    │   ├── urdf
    │   └── worlds
    ├── third_party
    │   ├── dynamic_rviz_config
    │   ├── dynamic_xml_config
    │   ├── gazebo_plugins
    │   └── rviz_plugins
    └── user_config         # user configuration file
```

## 3. Dynamic Configuration

Change configs through modifing the `./src/user_config/user_config.yaml`. For example, you can change the global_planner and local_planner as you want.

## 4. Application on a Real Robot

to be conducted.
