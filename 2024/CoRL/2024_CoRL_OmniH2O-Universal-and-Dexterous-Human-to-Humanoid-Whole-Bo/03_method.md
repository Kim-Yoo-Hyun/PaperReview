# Method

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, humanoid, whole-body teleoperation, loco-manipulation, Imitation Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://omni.human2humanoid.com/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- : We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.
- We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a ...
- Our ablation study (Table 2(a)) also (b) Ablation on History steps/Architecture shows that policies without velocity input has OmniH2O-History0 S ⊂ R90 83.26 46.00 4.86 4.45 OmniH2O-History5 S ...

## 원리적 동기
- However, whole-body control of a full-sized humanoid robot is challenging , with many existing works focusing only on the lower body or decoupled lower and upper body control ...
- The input history could replace the global linear velocity, an essential input in previous work that requires Motion Capture (MoCap) to obtain.
- : We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.

## 핵심 방법론
- Our ablation study (Table 2(a)) also (b) Ablation on History steps/Architecture shows that policies without velocity input has OmniH2O-History0 S ⊂ R90 83.26 46.00 4.86 4.45 OmniH2O-History5 S ...
- Additionally, we evaluate different neural network architectures for history utilization: MLP, LSTM, GRU and determine that MLP-based OmniH2O performs the best.
- All sequences Successful sequences State Dimension Sim2Real Succ ↑ Eg-mpjpe ↓ Empjpe ↓ Eacc ↓ Evel ↓ Eg-mpjpe ↓ Empjpe ↓ Eacc ↓ Evel ↓ Privileged policy S ...
- Ablation on History Steps/Architecture.
