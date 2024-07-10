---
layout: page
title: Robust Bi-Copter Control
description: Applied robust control methods, achieving a remarkable stability margin on the Quanser Bi-copter system
# img: assets/img/qqq.jpeg
img: assets/img/stablecon.gif
# redirect: https://unsplash.com
importance: 3
category: Robotics
---
<!-- Introducing a solution to the intricate task of designing controllers for multi-input output systems, our project focuses on the Quanser Aero system—a dual-input, dual-output system with pitch and yaw angles as outputs, and motor voltages as inputs. Recognizing the substantial coupling between these variables, our endeavor aimed at addressing this challenge through four distinct controller design techniques: H ∞ loop shaping, H 2 optimal control, H ∞ optimal control, and µ synthesis. Leveraging MATLAB for controller development and Simulink for simulation, I meticulously tuned parameters to ensure optimal performance in the face of uncertainties introduced into the plant. The culmination involved the implementation of controllers on the hardware setup, subjecting them to a square wave reference for both Yaw and Pitch axes. Rigorous analysis of the results ensued, with additional parameter fine-tuning applied to controllers exhibiting suboptimal performance. Notably, the H ∞ loop shaping controller emerged as the most effective performer in reference tracking. This comprehensive project not only navigated the intricacies of multi-input output systems but also showcased a meticulous approach to design, simulation, and implementation, contributing significantly to the field of robust bi-copter control. -->


Presenting a groundbreaking solution to the intricate challenge of designing controllers for multi-input output systems, our project is centered around the Quanser Aero system. This system is a dual-input, dual-output configuration with pitch and yaw angles as outputs and motor voltages as inputs. Acknowledging the inherent coupling between these variables, our project set out to tackle this complexity through the implementation of four distinct controller design techniques: H ∞ loop shaping, H 2 optimal control, H ∞ optimal control, and µ synthesis.

The development process utilized MATLAB for controller design and Simulink for simulation, where meticulous parameter tuning was performed to ensure optimal performance in the presence of uncertainties introduced into the plant. The culmination of our efforts involved the practical implementation of these controllers on the hardware setup, subjecting them to a square wave reference for both Yaw and Pitch axes. Rigorous analysis of the results ensued, accompanied by additional parameter fine-tuning for controllers exhibiting suboptimal performance.

Notably, the H ∞ loop shaping controller emerged as the most effective performer in reference tracking. This comprehensive project not only successfully navigated the complexities of multi-input output systems but also demonstrated a meticulous approach to design, simulation, and implementation. As a result, our work significantly contributes to the field of robust bi-copter control, showcasing a groundbreaking advancement in controller design methodologies.

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/controls1.gif"  class="img-fluid rounded z-depth-1" %}
    </div>
</div> 
<div class="caption">
    Stabilizing control
</div>