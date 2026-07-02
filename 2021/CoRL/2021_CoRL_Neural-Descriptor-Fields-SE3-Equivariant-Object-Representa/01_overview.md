# Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation

- Year/Venue: 2021 / CoRL
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Robotics, equivariant, 3D geometry, manipulation
- Paper link: ./2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/paper.pdf
- Code/Project: https://github.com/anthonysimeonov/ndf_robot
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- — We present Neural Descriptor Fields (NDFs), an object representation that encodes both points and relative poses between an object and a target (such as a robot gripper ...
- We employ this representation for object manipulation, where given a task demonstration, we want to repeat the same task on a new object instance from the same category.
- We propose to achieve this objective by searching (via optimization) for the pose whose descriptor matches that observed in the demonstration.

## Core Idea
- We propose to achieve this objective by searching (via optimization) for the pose whose descriptor matches that observed in the demonstration.
- — We present Neural Descriptor Fields (NDFs), an object representation that encodes both points and relative poses between an object and a target (such as a robot gripper ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We propose to achieve this objective by searching (via optimization) for the pose whose descriptor matches that observed in the demonstration.
- Our performance generalizes across both object instances and 6-DoF object poses, and significantly outperforms a recent baseline that relies on 2D descriptors.
- We demonstrate learning of manipulation tasks from few (∼5-10) demonstrations both in simulation and on a real robot.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose to achieve this objective by searching (via optimization) for the pose whose descriptor matches that observed in the demonstration.
- — We present Neural Descriptor Fields (NDFs), an object representation that encodes both points and relative poses between an object and a target (such as a robot gripper ...
- In particular, we desire to construct a system which can manipulate objects from the same category into target configurations, irrespective of the object’s 3D location and orientation (see ...

## Abstract Cue
- — We present Neural Descriptor Fields (NDFs), an object representation that encodes both points and relative poses between an object and a target (such as a robot gripper or a rack used for hanging) via category-level descriptors.
