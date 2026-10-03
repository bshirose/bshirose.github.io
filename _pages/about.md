---
layout: research-home
title: about
permalink: /
body_class: rh-page
description: Burhanuddin Shirose, PhD researcher in robotics at Carnegie Mellon University (AirLab). Motion planning for constrained and multi-agent robots.

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
hero:
  photo: /assets/img/newme.jpg
  eyebrow: PhD Researcher, Robotics Institute, Carnegie Mellon University
  lab: AirLab
  lab_url: https://theairlab.org/
  advisor: Prof. Sebastian Scherer
  advisor_url: https://www.ri.cmu.edu/ri-faculty/sebastian-scherer/
  name: Burhanuddin Shirose
  headline: Motion planning for constrained and multi-agent robots.
  lede: "I build planners that hold up on real hardware: coverage of unknown spaces, ergodic search in clutter, snake-robot reaching, and heterogeneous field teams."
  education:
    - label: M.S. Mechanical Engineering
      school: Carnegie Mellon University
      detail: GPA 3.90 / 4.0
    - label: B.Tech Mechanical Engineering
      school: NIT Tiruchirappalli
      detail: GPA 8.41 / 10

news:
  - date: "2026"
    text: <strong>Scalable MOES</strong> manuscript in preparation for IEEE RA-L, with up to 97.2× faster multi-agent allocation.
  - date: "2026"
    text: <strong>BINSAT</strong> reaching planner deployed on a physical 16-DoF snake robot.
  - date: Oct 2025
    text: <strong>CAP</strong> presented at IROS 2025. Journal extension (TAP) adds multi-robot coverage.
  - date: Aug 2025
    text: Convoy communication-relay behaviors presented at <strong>GVSETS 2025</strong>, Novi, MI.
  - date: May 2025
    text: Staircase estimation and ground segmentation published in <strong>IEEE RA-L</strong>.
  - date: Oct 2024
    text: <strong>GESCE</strong> (first author) presented at IROS 2024.

# ---------------------------------------------------------------------------
# Selected research (bento grid). span = columns out of 12 on desktop.
# media types: video | image. The first item is shown first; extra items become tabs.
# ---------------------------------------------------------------------------
projects:
  - id: cap
    span: 7
    pills:
      - { label: IROS 2025, kind: conf }
      - { label: IEEE Trans. (TAP), kind: journal }
    title: Connectivity-aware coverage path planning in unknown environments
    summary: CAP builds a coverage guidance graph online from LiDAR that records how explored and unexplored subareas connect. A hierarchical planner orders subareas with a global tour and covers each one locally, which removes the revisits that greedy frontier planners make. Tested in simulation and on Spot and wheeled robots in 60 m × 24 m warehouses.
    metrics:
      - { value: "−20%", label: total coverage time }
      - { value: "−15%", label: traversal in unknown space }
      - { value: "5", label: baselines compared }
    media:
      - { type: video, src: /assets/video/research/cap_realworld.mp4, poster: /assets/img/research/cap_realworld_poster.jpg, label: Real world, caption: "Warehouse experiment, 60 m × 24 m, 50× speed" }
      - { type: image, src: /assets/img/research/cap_method.png, label: Method, caption: "Coverage guidance graph and global tour", alt: "Four-panel CAP methodology figure: target cell, subareas, coverage guidance graph, local coverage path" }
      - { type: image, src: /assets/img/research/cap_realworld_rviz.jpg, label: Baselines, caption: "Coverage paths vs. 5 baselines, real-world scene 1", alt: "Real-world coverage paths of CAP compared with IBINN, BA*, BSA, e* and PPCPP" }
      - { type: image, src: /assets/img/research/cap_multi_results.png, label: Multi-robot, caption: "Multi-robot path length, overlap, coverage time", alt: "Bar charts comparing path length, overlap ratio and coverage time for multi-robot coverage planners" }
    links:
      - { label: Paper, url: "https://doi.org/10.1109/IROS60139.2025.11247648" }
      - { label: BibTeX, url: "/publications/#shen2025cap" }

  - id: gesce
    span: 5
    pills:
      - { label: IROS 2024, kind: conf }
      - { label: First author, kind: first }
    title: Graph-based ergodic search in cluttered environments
    summary: Ergodic planners spend time where targets are likely, but treat obstacles as soft costs and can still collide. GESCE builds a graph of the free space and searches it with ergodicity as the heuristic, so paths are collision-free by construction.
    metrics:
      - { value: "125", label: benchmark scenarios }
      - { value: "100%", label: collision-free paths }
      - { value: "5", label: MAPF clutter maps }
    media:
      - { type: image, src: /assets/img/research/gesce_fig1.png, label: Fig. 1, caption: "Ergodic path through a cluttered maze", alt: "GESCE Figure 1: 3D maze with an information peak and the planned ergodic trajectory" }
      - { type: image, src: /assets/img/research/gesce_baselines.png, label: Baselines, caption: "GESCE vs. optimization-based ergodic planners", alt: "Trajectories of GESCE and three baseline ergodic planners around circular obstacles" }
      - { type: image, src: /assets/img/research/gesce_benchmark_maps.png, label: Benchmarks, caption: "Information maps and MAPF benchmark maps", alt: "Five information distributions and five MAPF benchmark obstacle maps" }
    links:
      - { label: Paper, url: "https://doi.org/10.1109/IROS58592.2024.10802461" }
      - { label: Full results, url: "/projects/GESCE/" }

  - id: snake
    span: 5
    pills:
      - { label: IEEE RA-L, kind: prep }
      - { label: In preparation, kind: field }
    title: Hierarchical motion planning for high-DoF snake robots
    summary: Reaching lets a snake robot anchor its tail and extend across gaps, turning it into a 16-DoF serial manipulator. BINSAT searches over Bézier-curve backbones in 6-D, then lifts each candidate to joint space with a trajectory optimizer that enforces whole-body collision and torque limits.
    metrics:
      - { value: "16→6", label: planning dimensions }
      - { value: "98%", label: simulation success }
      - { value: "16-DoF", label: hardware deployment }
    media:
      - { type: video, src: /assets/video/research/snake_reaching.mp4, poster: /assets/img/research/snake_reaching_poster.jpg, label: Hardware, caption: "Reaching between tight spaces, 3× speed" }
      - { type: image, src: /assets/img/research/snake_binsat_pipeline.png, label: Method, caption: "BINSAT planning loop over Bézier backbones", alt: "BINSAT pipeline: initial state, low-dimensional Bezier search and high-dimensional trajectory optimization, final trajectory" }
      - { type: image, src: /assets/img/research/snake_hardware.jpg, label: Setup, fit: cover, caption: "Anchored tail, head reaching for inspection", alt: "Snake robot anchored in a tube with its head reaching into a second tight space" }
    links: []

  - id: convoy
    span: 7
    pills:
      - { label: GVSETS 2025, kind: symposium }
      - { label: Field deployment, kind: field }
    title: Decentralized heterogeneous convoys and high-speed autonomy
    summary: A decentralized planning stack lets mixed teams of wheeled UGVs and Spot quadrupeds form, resize, and hold convoys without a central planner. Compact footprint geometry keeps collision checks fast enough for 20 Hz replanning at 6 m/s, and robots peel off as communication relays to keep the team linked to base.
    metrics:
      - { value: "6 m/s", label: autonomous ground speed }
      - { value: "20 Hz", label: online replanning }
      - { value: "UGV+Spot", label: mixed fleet }
    media:
      - { type: video, src: /assets/video/research/convoy_decentralized.mp4, poster: /assets/img/research/convoy_decentralized_poster.jpg, label: Convoy, caption: "Decentralized convoy, aerial view" }
      - { type: video, src: /assets/video/research/highspeed_autonomy.mp4, poster: /assets/img/research/highspeed_autonomy_poster.jpg, label: High speed, caption: "Obstacle avoidance at speed, operator and vehicle views" }
      - { type: image, src: /assets/img/research/convoy_fleet.jpg, label: Fleet, fit: cover, caption: "Wheeled UGVs and Spot quadrupeds", alt: "Fleet of three wheeled UGVs and two Spot quadrupeds used in convoy experiments" }
      - { type: image, src: /assets/img/research/convoy_network_aerial.jpg, label: Relay network, fit: cover, caption: "Relay topology with link quality, field trial", alt: "Aerial view of robots acting as communication relays with link-quality labels" }
    links:
      - { label: MMPUG, url: "https://www.ri.cmu.edu/project/mmpug-multi-model-perception-uber-good/" }
      - { label: Project, url: "/projects/1_project/" }

  - id: moes
    span: 4
    pills:
      - { label: IEEE RA-L, kind: prep }
      - { label: AAAI MAPF-W, kind: workshop }
    title: Scalable multi-agent multi-objective ergodic search
    summary: Assigning agents to competing search objectives is combinatorial in team size. I cast allocation as clustering in Fourier space, warm-start it with an infinite-horizon approximation, and solve a lazy ILP that exploits the resulting structure.
    metrics:
      - { value: "97.2×", label: faster allocation }
      - { value: "min-max", label: optimality kept }
      - { value: "ILP", label: lazy constraints }
    figure_slot: /assets/img/research/moes.png
    figure_pending:
      value: "97.2×"
      label: Speedup of the lazy ILP allocator, with min-max optimality preserved.
    media: []
    links: []

  - id: hil
    span: 8
    pills:
      - { label: Hardware-in-the-loop, kind: field }
      - { label: Space robotics, kind: field }
    title: Microgravity docking emulator
    summary: Four synchronized UR10e arms reproduce spacecraft proximity operations on the ground. A MuJoCo model computes free-floating and contact dynamics, velocity control on the arms tracks the simulated client and tool-tip states with sub-millimeter, sub-millisecond accuracy, and measured contact forces feed back into the simulation.
    metrics:
      - { value: "4× UR10e", label: synchronized arms }
      - { value: "<1 mm", label: tracking accuracy }
      - { value: "<1 ms", label: synchronization }
    media:
      - { type: video, src: /assets/video/research/hil_docking.mp4, poster: /assets/img/research/hil_docking_poster.jpg, label: Emulator, caption: "MuJoCo simulation (top) driving the hardware emulator (bottom)" }
    links: []

# ---------------------------------------------------------------------------
# Video wall
# ---------------------------------------------------------------------------
videos:
  - { src: /assets/video/research/global_planner_sim.mp4, poster: /assets/img/research/global_planner_sim_poster.jpg, title: Local-minima escape, caption: "Local only vs. global + local planner, simulation" }
  - { src: /assets/video/research/global_planner_wheeled.mp4, poster: /assets/img/research/global_planner_wheeled_poster.jpg, title: Global navigation, caption: "Wheeled UGV, waypoint to waypoint, 4×" }
  - { src: /assets/video/research/legged_local_planner.mp4, poster: /assets/img/research/legged_local_planner_poster.jpg, title: Quadruped local planner, caption: "Spot through doors and clutter" }
  - { src: /assets/video/research/voxel_perception.mp4, poster: /assets/img/research/voxel_perception_poster.jpg, title: 3D voxel perception, caption: "Voxel grid to traversability map" }
  - { src: /assets/video/research/convoy_heterogeneous.mp4, poster: /assets/img/research/convoy_heterogeneous_poster.jpg, title: Heterogeneous convoy, caption: "Spot decoupled, tracking a wheeled convoy" }
  - { src: /assets/video/research/hil_docking.mp4, poster: /assets/img/research/hil_docking_poster.jpg, title: Microgravity docking HIL, caption: "4× UR10e + MuJoCo" }
---

I am a PhD researcher at the Carnegie Mellon University Robotics Institute, working in the AirLab with Prof. Sebastian Scherer. As a Robotics Engineer at CMU (2023 to 2025) I built real-time planners for ground vehicles, decentralized multi-robot teams, and a multi-arm hardware-in-the-loop testbed. I hold an M.S. in Mechanical Engineering from CMU and a B.Tech in Mechanical Engineering from NIT Tiruchirappalli.
