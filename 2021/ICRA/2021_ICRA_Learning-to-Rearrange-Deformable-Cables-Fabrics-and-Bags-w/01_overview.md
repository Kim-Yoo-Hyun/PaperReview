# Learning to Rearrange Deformable Cables, Fabrics, and Bags with Goal-Conditioned Transporter Networks

- Year/Venue: 2021 / ICRA
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, deformable object, cable manipulation, cloth manipulation, goal-conditioned learning, vision-based control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/berkeley-deformable/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- — Rearranging and manipulating deformable objects such as cables, fabrics, and bags is a long-standing challenge in robotic manipulation.
- I NTRODUCTION Manipulating deformable objects is a long-standing challenge in robotics with a wide range of real-world applications.
- In contrast to rigid object manipulation, deformable object manipulation presents additional challenges due to more complex configuration spaces, dynamics, and sensing.

## Core Idea
- We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can represent pick and ...
- In this work, we propose a new suite of benchmark tasks, called DeformableRavens, to test manipulation of cables, fabrics, and bags spanning 1D, 2D, and 3D deformables.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In simulation and in physical experiments, we demonstrate that goal-conditioned Transporter Networks enable agents to manipulate deformable structures into flexibly specified configurations without test-time visual anchors for target ...
- We also significantly extend prior results using Transporter Networks for manipulating deformable objects by testing on tasks with 2D and 3D deformables.
- Goals cannot be as easily specified as rigid object poses, and may involve complex relative spatial relations such as “place the item inside the bag.” In this work, ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can represent pick and ...
- In this work, we propose a new suite of benchmark tasks, called DeformableRavens, to test manipulation of cables, fabrics, and bags spanning 1D, 2D, and 3D deformables.
- For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned va

## Abstract Cue
- — Rearranging and manipulating deformable objects such as cables, fabrics, and bags is a long-standing challenge in robotic manipulation.
