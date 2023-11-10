---
layout: page
title: Robust Bi-Copter Control
description: Applied robust control methods, achieving a remarkable stability margin on the Quanser Bi-copter system
img: assets/img/qqq.jpeg
# redirect: https://unsplash.com
importance: 3
category: Robotics
---
Introducing a solution to the intricate task of designing controllers for multi-input output systems, our project focuses on the Quanser Aero system—a dual-input, dual-output system with pitch and yaw angles as outputs, and motor voltages as inputs. Recognizing the substantial coupling between these variables, our endeavor aimed at addressing this challenge through four distinct controller design techniques: H ∞ loop shaping, H 2 optimal control, H ∞ optimal control, and µ synthesis. Leveraging MATLAB for controller development and Simulink for simulation, I meticulously tuned parameters to ensure optimal performance in the face of uncertainties introduced into the plant. The culmination involved the implementation of controllers on the hardware setup, subjecting them to a square wave reference for both Yaw and Pitch axes. Rigorous analysis of the results ensued, with additional parameter fine-tuning applied to controllers exhibiting suboptimal performance. Notably, the H ∞ loop shaping controller emerged as the most effective performer in reference tracking. This comprehensive project not only navigated the intricacies of multi-input output systems but also showcased a meticulous approach to design, simulation, and implementation, contributing significantly to the field of robust bi-copter control.
