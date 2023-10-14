# ROS-Localization-and-Navigation

## 1. Environment and Start

1. **OS**: Ubuntu 20.04 LTS

2. **ROS**: 1.0 Noetic LTS (Desktop-Full suggested)

3. Dependencies Installation:

   Update your software package first. Make sure to choose the appropriate server from `Software & Updates` on your Ubuntu.

   ```bash
   $ sudo apt-get update
   $ sudo apt-get upgrade
   ```

   **Note**: Make sure you are installing ROS and its dependencies with the appropriate versions when you type following commands, which now actually fits ROS Noetic only.

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
   ```

5. Execute the project.

   ```bash
   $ cd ./src/sim_env/scripts/
   $ sudo ./main.sh
   ```

   **Note**: If you meet some errors that are hard to solve when you run `sudo ./main.sh`, try running commands of `main.sh` step by step in your terminal, like:

   ```bash
   $ cd ./src/sim_env/scripts/
   $ source ../../../devel/setup.bash
   $ python ../../third_party/dynamic_xml_config/main_generate.py user_config.yaml
   $ roslaunch sim_env main.launch
   ```

6. Use **2D Nav Goal** to select the goal. Succeed!

7. Automatically send a goal to your robot if you want to.

   ```bash
   to be conducted ...
   ```

<img src="D:\Desktop\ROS-Localization-and-Navigation\assets\rrt.gif" alt="rrt" style="zoom:67%;" />

## 2. File Tree

``` bash
ros_motion_planner
└── src
    ├── planner             # algorithms mainly
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

Change configs through modifying the `./src/user_config/user_config.yaml`. For example, you can change the global_planner and local_planner as you want. When you run commands in `main.sh`, the python script will regenerate `.launch`, `.world` and so on, according to your configs in that file.

Below is an example of `user_config.yaml`:

```yaml
map: "warehouse"
world: "warehouse"
rviz_file: "sim_env.rviz"

robots_config:
  - robot1_type: "turtlebot3_waffle"
    robot1_global_planner: "rrt"
    # Graph Planner Options: a_star, jps, gbfs, dijkstra, d_star, lpa_star, d_star_lite, theta_star, lazy_theta_star, voronoi
    # Sample Planner Options: rrt, rrt_star, informed_rrt, rrt_connect
    # Intelligent Planner Options: aco
    robot1_local_planner: "dwa"
    # pid dwa static apf
    robot1_x_pos: "0.0"
    robot1_y_pos: "0.0"
    robot1_z_pos: "0.0"
    robot1_yaw: "0.0"

# plugins:
  # pedestrians: "pedestrian_config.yaml"
  # obstacles: "obstacles_config.yaml"
  # map_layers: "maps_config.yaml"
```

Explanation:

- `map`: static map，located in `src/sim_env/map/`, if `map: ""`, map_server will not publish map message which often used in SLAM.
- `world`: gazebo world，located in `src/sim_env/worlds/`.
- `rviz_file`: RVIZ configuration.
- `robots_config`: robotic configuration.
  - `type`: robotic type，such as *`turtlebot3_burger`, `turtlebot3_waffle` and `turtlebot3_waffle_pi`*.
  - `global_planner`: global algorithm.
  - `local_planner`: local algorithm.
  - `xyz_pos and yaw`: initial pose.
- `plugins`: other applications using in simulation.
  - `pedestrians`: configure file to add dynamic pedestrians.
  - `obstacles`: configure file to add static obstacles.

Except for the above mentioned, you can use *pedestrians* and *obstacles* by cancelling code annotation in `user_config.yaml` and modifying configuration files although there is no need to do so to run this project successfully.

## 4. Application on a Real Robot

To be conducted. FYI, following is some information which may be useful.

We use another [gazebo simulation](https://github.com/ZhanyuGuo/ackermann_ws) as an example, like we have a robot which has the capacity of localization, mapping and navigation (*using move_base*).

1. Download and compile this repository.

   ```bash
   $ cd <your_workspace>/
   $ git clone https://github.com/ai-winter/ros_motion_planning.git
   
   $ cd ros_motion_planning/
   $ catkin_make
   ```

2. Download and compile the 'real robot' software.

   ```bash
   $ cd <your_workspace>/
   $ git clone https://github.com/ZhanyuGuo/ackermann_ws.git
   
   $ cd ackermann_ws/
   $ # ---- IMPORTANT HERE, reasons in NOTE ----
   $ source <your_workspace>/ros_motion_planning/devel/setup.bash
   
   $ catkin_make
   ```

   **Note: Sourcing other workspaces before `catkin_make` will make the current `setup.bash` contain former sourced workspaces, i.e. they are also included when you only source this current workspace later.**

   **Remember: Remove the old `build/` and `devel/` of current workspace before doing this, otherwise it will not work.**

3. Change the **base_global_planner** and **base_local_planner** in real robot's `move_base` as you need.

   ```xml
   <?xml version="1.0"?>
   <launch>
       <!-- something else ... -->
       <node pkg="move_base" type="move_base" respawn="false" name="move_base" output="screen">
           <!-- something else ... -->
   
           <!-- Params -->
           <!-- for graph_planner -->
           <rosparam file="$(find sim_env)/config/planner/graph_planner_params.yaml" command="load" />
           <!-- for sample_planner -->
           <rosparam file="$(find sim_env)/config/planner/sample_planner_params.yaml" command="load" />
           <!-- for dwa_planner -->
           <rosparam file="$(find sim_env)/config/planner/dwa_planner_params.yaml" command="load" />
           <!-- for pid_planner -->
           <rosparam file="$(find sim_env)/config/planner/pid_planner_params.yaml" command="load" />
   
           <!-- Default Global Planner -->
           <!-- <param name="base_global_planner" value="global_planner/GlobalPlanner" /> -->
           <!-- GraphPlanner -->
           <param name="base_global_planner" value="graph_planner/GraphPlanner" />
           <!-- options: a_star, jps, gbfs, dijkstra, d_star, lpa_star, d_star_lite -->
           <param name="GraphPlanner/planner_name" value="a_star" />
           <!-- SamplePlanner -->
           <!-- <param name="base_global_planner" value="sample_planner/SamplePlanner" /> -->
           <!-- options: rrt, rrt_star, informed_rrt, rrt_connect -->
           <!-- <param name="SamplePlanner/planner_name" value="rrt_star" /> -->
   
           <!-- Default Local Planner -->
           <!-- <param name="base_local_planner" value="teb_local_planner/TebLocalPlannerROS" /> -->
           <param name="base_local_planner" value="pid_planner/PIDPlanner" />
           <!-- <param name="base_local_planner" value="dwa_planner/DWAPlanner" /> -->
   
           <!-- something else ... -->
       </node>
       <!-- something else ... -->
   </launch>
   ```

4. Run! But maybe there are still some details that you have to deal with...

## 5. Acknowledgements

- Our algorithms, robot and world models are mainly from [ros_motion_planning](https://github.com/ai-winter/ros_motion_planning), [Dataset-of-Gazebo-Worlds-Models-and-Maps](https://github.com/mlherd/Dataset-of-Gazebo-Worlds-Models-and-Maps) and [aws-robomaker-small-warehouse-world](https://github.com/aws-robotics/aws-robomaker-small-warehouse-world). Thanks for these open source repos sincerely.

## 6. License

The source code is released under [GPLv3](https://www.gnu.org/licenses/) license.

## 7. Maintenance

Feel free to contact us if you have any question.

### 一些注意事项：

1. 在`user_config.yaml`中，global_planner可以使用voronoi，但在使用前需要先将下方的map_layers的注释取消（未被完全测试）。
2. ACO算法未被完全测试。
