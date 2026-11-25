# Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p052.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p052.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Han Xue, Jieji Ren, Wendi Chen, Gu Zhang, Yuan Fang, Guoying Gu, Huazhe Xu, Cewu Lu
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, Diffusion, tactile sensing, contact-rich manipulation, slow-fast control, Imitation Learning
- Official paper: https://www.roboticsproceedings.org/rss21/p052.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p052.pdf
- Code/Project: https://reactive-diffusion-policy.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Reactive Diffusion Policy는 장기 동작을 느리게 예측하면서도 실행 중 들어오는 촉각에 맞춰 접촉 행동을 빠르게 바꾼다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p052.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans can accomplish complex contact-rich tasks using vision and touch, with highly rea r fast response (o external changes and adaptive control of contact forces: ...
- **p. 1 / Abstract - extractive body cue:** Ex ‘visual imitation learning (IL) approaches rly on aetion chunking ‘model complex behaviors, which lacks the ability to respond instantly to real-time tactile feedback during ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, most teleoperation systems. sirugsle to provide fine-grained tactile / force feedback, which limits the range of tasks that can be performed.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce TactAR, a low-cost teleoperation system that provides real-time tactile feedback through Augmented Reality (AR), along with Reactive Diffusion Policy ...
- **p. 1 / Abstract - extractive body cue:** RDP employs a two-level hierarchy: (1) a slow latent diffusion policy for predicting high-level ation chunks in latent space at low frequency, (2) a fast ...
- **p. 2 / I. Ivrropucrion - extractive body cue:** In order to compensate for the limitations of purely visual input, numerous approaches [40 27, 45, 64, 31] have explored the integration of tactile input ...
- **p. 3 / B. Robot Data Collection System - extractive body cue:** By integrating both tactile and visual modalities, our approach overcomes the limitations of prior works and achieves greater versatility in robotic manipulation,

## Core Idea

- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce TactAR, a low-cost teleoperation system that provides real-time tactile feedback through Augmented Reality (AR), along with Reactive Diffusion Policy ...
- **p. 2 / I. Ivrropucrion - extractive body cue:** In this work, we propose two critical components to solve the above issues of visual-tactile imitation learning:
- **p. 2 / I. Ivrropucrion - extractive body cue:** To leverage the high-quality visual tactile data collected by the TactAR system, we propose an imitation learning algorithm called Reactive Diffusion Policy (RDP) (Fig. / ...
- **p. 3 / B. Robot Data Collection System - extractive body cue:** ‘In contrast, our method combines normal force, shear force, and visual RGB inputs into a unified visual-tactile policy, enabling deployment across a broader range of ...
- **p. 3 / B. Robot Data Collection System - extractive body cue:** Our method ‘combines the advantages of low-cost VR controller and tactile sensing, getting tactile feedback via Augmented Reality, while preserving the accuracy needed for precise ...
- **p. 5 / B. Slow-Fast Policy Learning - extractive body cue:** 1 policy learning, a slow Latent Diffusion Policy (LDP) is trained to predict the latent action chuck according to the observation in a way similar ...
- **p. 7 / architecture - extractive body cue:** We calculate the latency caused by policy inference and action execution, and discard the first few action steps predicted by the model to send the ...
- **p. 7 / architecture - extractive body cue:** We use relative end-effector (EE) trajectory for action representation, which has been proven to be effective even in complex tasks by UMI [//].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | ForceMimiec [1] adds a force sensor on a handheld device [11] to get force feedback, but suffers from the inaccuracy of pose estimation, and thus cannot directly train an end2end policy. | tactile image/force, vision과 proprioceptive history | p. 3 (B. Robot Data Collection System), p. 1 (Body text (section boundary not confidently recovered)) |
| State/latent | ForceMimiec, adds, force, sensor, handheld, device, feedback, suffers, inaccuracy, pose, estimation, thus | contact geometry, force state 또는 latent dynamics | p. 3 (B. Robot Data Collection System), p. 1 (Body text (section boundary not confidently recovered)), p. 6 (B. Slow-Fast Policy Learning) |
| Output/action | action trajectories with a slow policy network and achieve closed-loop control based on high-frequency tactile / force feedback | grasp/contact action, force command 또는 object motion | p. 1 (Body text (section boundary not confidently recovered)), p. 6 (B. Slow-Fast Policy Learning), p. 2 (I. Ivrropucrion) |
| Objective/outcome | During training, given the observation (including image, tactlity and propri- ‘oception), the gradient field is leamed by ep and the DDPM training objective can be rewritten as | slip/contact success, force/pose error와 robustness | p. 6 (B. Slow-Fast Policy Learning), p. 5 (A. 3D Deformation Field Extraction), p. 4 (A. 3D Deformation Field Extraction) |

## Main Claims and Actual Contribution

- 잠재 확산 정책이 저주파 행동 묶음을 만들고 빠른 비대칭 토크나이저가 현재 촉각을 사용해 세부 동작을 복원한다. [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p052.pdf#page=5) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p052.pdf#page=6)
- 작업자에게 촉각을 시각적으로 돌려주는 TactAR로 시연을 수집하고 여러 실물 접촉 과제와 센서에서 정책을 평가했다. [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p052.pdf#page=4) · [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p052.pdf#page=8) · [PDF 9쪽](https://www.roboticsproceedings.org/rss21/p052.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Embodiment/environment | 1) Hardware: ‘The experimental platform consists of two Flexiv Rizon 4 [19] robotic arms with joint torque sensors and two Flexiv Grav [17] grippers. | hardware/simulator version and reset protocol | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Dataset/benchmark | 7, in the expert data, there are two upward lift trajectories, indicating the presence of multi-mosalty 4) Evaluation Protocols: We use similar initial states across all methods for both the robots and ... | role, split, size and leakage | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Metric | Although the performance of both methods is similar, low-dimensional tactile embedding demonstrates greater robustness to texture ‘changes resulting from gel damage or gel replacements during the evaluation process. | definition, denominator, direction and uncertainty | p. 9 (B. Results), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Baseline/ablation | All devices are connected to a workstation with an Intel Core i9-14900K CPU and an NVIDIA RTX 4090 GPU for both data collection and evaluation 2) Baselines: We use the following baselines ... | fair input/data/compute/action matching | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / B. Results - extractive body cue:** It may get stuck when making contact with the object (e.2., failure case 2 in Fig.
- **p. 9 / B. Results - extractive body cue:** However, despite similar performance, these two DP baselines exhibit different failure modes.
- **p. 10 / 056 O58 om - extractive body cue:** 8: Evaluation results and failure cases of baselines.
- **p. 10 / 056 O58 om - extractive body cue:** V that when the action chunk size is reduced from 8 to 2, the DP baseline tends to get stuck before grasping (failure case 4 ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** It is crucial to avoid exerting excessive force that could squeeze the cup while also ensuring that the force is sufficient to prevent the cup ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Note that the estimated TCP force / torque Signals have relatively larger noise compared tothe force sensor mounted on the robot end effector (e.g.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (I. Ivrropucrion), p. 3 (B. Robot Data Collection System), p. 4 (A. 3D Deformation Field Extraction), p. 1 (Abstract), p. 5 (B. Slow-Fast Policy Learning)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** In order to compensate for the limitations of purely visual input, numerous approaches [40 27, 45, 64, 31] have explored the integration of tactile input into imitation learning policies However, ... (p. 2, I. Ivrropucrion).
- **Actual contribution:** To address these challenges, we introduce TactAR, a low-cost teleoperation system that provides real-time tactile feedback through Augmented Reality (AR), along with Reactive Diffusion Policy (RDP), a novel slow-fast visuale ... (p. 1, Abstract).
- **Evaluation boundary:** All devices are connected to a workstation with an Intel Core i9-14900K CPU and an NVIDIA RTX 4090 GPU for both data collection and evaluation 2) Baselines: We use the ... (p. 7, V. EXPERIMENTS).
- **Explicit failure boundary:** We ‘observe that DP with pure visual input frequently predicts inaccurate trajectories and results in large contact forces (e.g. failure case 2 in Fig. (p. 9, B. Results).

## 원문과 공개 자료

- 게재본 표제면에 따라 Fang Yuan → Yuan Fang로 반영했다. [표제면](https://www.roboticsproceedings.org/rss21/p052.pdf#page=1)
- 코드 · 실제 팔에서 시각·촉각 정책을 실행하는 코드 · eval_real_robot_flexiv.py [배포 파일](https://raw.githubusercontent.com/xiaoxiaoxh/reactive_diffusion_policy/824c5e8de1fd1811106907a04b5f0186e0138c0b/eval_real_robot_flexiv.py)
- 가중치 · 들어 올리기 과제의 시각·촉각 잠재 확산 정책 · real_lift_image_tactile_emb_ldp_absolute_24fps/checkpoints/latest.ckpt [배포 파일](https://huggingface.co/WendiChen/reactive_diffusion_policy_model/blob/8e6364950d1e0aaa175a50e12262f70c3a9f1316/real_lift_image_tactile_emb_ldp_absolute_24fps/checkpoints/latest.ckpt)
- 데이터 · 실제 물체 들어 올리기 작업의 시연 아카이브 · dataset_full/lift_v2.zip [배포 파일](https://huggingface.co/datasets/WendiChen/reactive_diffusion_policy_dataset/blob/821a9faa144158425f93c26e75d862c7e5994933/dataset_full/lift_v2.zip)
