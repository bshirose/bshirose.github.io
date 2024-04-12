---
layout: page
title: Local Planner
description: Fast efficient local planning for high speed robots
img: assets/img/rob.png
importance: 3
category: Research Projects
# related_publications: einstein1956investigations, einstein1950meaning
---
I designed and implementated a cutting-edge local planner algorithm tailored specifically for autonomous driving robots. This demanded a meticulous approach, balancing robustness and efficiency to ensure navigation in challenging environments. I engineered a solution that not only navigates through complex terrains but also operates optimally even at high speeds of up to 6m/s. Central to the success of this project was the integration of sophisticated obstacle avoidance mechanisms, meticulously crafted to detect and circumvent potential hazards while adhering to the robot's footprint constraints.

In the development process, I harnessed the power of modern C++ features to optimize code efficiency, facilitating swift processing of up to 6000 trajectories within an impressive timeframe of less than 20 milliseconds. This achievement stands as a testament to the meticulous attention to detail and innovative problem-solving skills employed throughout the project. By harnessing the latest advancements in programming techniques, I ensured that our solution not only met but exceeded performance expectations, setting a new standard for local planner algorithms in autonomous driving robotics.

To checkout the videos click on these links [Obstacle avoidance](https://drive.google.com/file/d/1DkYyZdJxwPBmrqujZMxvJZlshtpgPzLt/view?usp=sharing) or [High speed turning](https://drive.google.com/file/d/1xP1nwycBWJbe0KgVWpyzriNKHQRNJTVj/view?usp=sharing)

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/localPlanner.png"   class="img-fluid rounded z-depth-1" %}
    </div>
</div> 
<div class="caption">
    Path cancellation based of grid projection
</div>