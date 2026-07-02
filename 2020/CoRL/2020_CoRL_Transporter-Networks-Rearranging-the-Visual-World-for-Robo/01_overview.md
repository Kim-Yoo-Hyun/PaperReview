# Transporter Networks: Rearranging the Visual World for Robotic Manipulation

- Year/Venue: 2020 / CoRL
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Robotics, Vision-Language Action, equivariance, Imitation Learning
- Paper link: ./2020/CoRL/2020_CoRL_Transporter-Networks-Rearranging-the-Visual-World-for-Robo/paper.pdf
- Code/Project: https://github.com/google-research/ravens
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- It is sample efficient in learning complex vision-based manipulation tasks: inserting blocks into fixtures (a), sequential pick-and-place in Towers of Hanoi (c), assembling kits with unseen objects (d), ...
- Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place.

## Core Idea
- In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input – which can parameterize robot ...
- We validate our methods with hardware in the real world.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our goals are threefold: 1) investigate whether preserving visuo-spatial structure within Transporter Networks improves their sample efficiency and generalization, 2) compare them to common baselines for end-to-end vision-based ...
- Experiment videos and code will be made available at https://transporternets.github.io We execute experiments in both simulated and real settings to evaluate Transporter Networks across various tasks.
- Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses.

## Limitation
- In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to integrate torque/force actions with spatial action spaces.

## Contribution
- In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input – which can parameterize robot ...
- Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place.
- Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses.

## Abstract Cue
- Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector.
