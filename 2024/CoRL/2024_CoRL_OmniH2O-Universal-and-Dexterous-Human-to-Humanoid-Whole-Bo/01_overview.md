# OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, humanoid, whole-body teleoperation, loco-manipulation, Imitation Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://omni.human2humanoid.com/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- However, whole-body control of a full-sized humanoid robot is challenging , with many existing works focusing only on the lower body or decoupled lower and upper body control ...
- The input history could replace the global linear velocity, an essential input in previous work that requires Motion Capture (MoCap) to obtain.
- For the humanoid teleoperation interface , the need for expensive setups such as motion captures and exoskeletons also hinders large-scale humanoid data collection.

## Core Idea
- : We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.
- We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 4.1.1 Simulation Motion-Tracking Results In Table 1’s first three rows, we can see that our deployable student policy significantly improves upon prior art on motion imitation and achieves ...
- In Table 1(a) we can see that DAgger improves performance overall, especially for policy with history input.
- OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans, as ...

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a ...
- : We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.
- OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans, as ...

## Abstract Cue
- : We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.
