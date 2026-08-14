# Problem

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, humanoid, whole-body teleoperation, loco-manipulation, Imitation Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://omni.human2humanoid.com/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- However, whole-body control of a full-sized humanoid robot is challenging , with many existing works focusing only on the lower body or decoupled lower and upper body control ...
- The input history could replace the global linear velocity, an essential input in previous work that requires Motion Capture (MoCap) to obtain.
- For the humanoid teleoperation interface , the need for expensive setups such as motion captures and exoskeletons also hinders large-scale humanoid data collection.

## 해결하려는 문제
- We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a ...
- : We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.
- OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans, as ...

## 선행 연구 / 배경 단서
- However, whole-body control of a full-sized humanoid robot is challenging , with many existing works focusing only on the lower body or decoupled lower and upper body control ...
- The input history could replace the global linear velocity, an essential input in previous work that requires Motion Capture (MoCap) to obtain.
- For the humanoid teleoperation interface , the need for expensive setups such as motion captures and exoskeletons also hinders large-scale humanoid data collection.
