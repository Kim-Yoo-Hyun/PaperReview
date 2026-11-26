# Learning Humanoid Standing-up Control across Diverse Postures

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p064.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p064.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Tao Huang, Junli Ren, Huayi Wang, Zirui Wang, Qingwei Ben, Muning Wen, Xiao Chen, Jianan Li, Jiangmiao Pang
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, humanoid, standing up, fall recovery, sim-to-real, Reinforcement Learning
- Official paper: https://www.roboticsproceedings.org/rss21/p064.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p064.pdf
- Code/Project: https://github.com/InternRobotics/HoST
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

HoST는 다양한 초기 자세에서 휴머노이드가 일어서도록 참조 동작 없이 강화학습하고, 실제 G1에 제어 정책을 옮긴다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p064.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Standing with the potential for Toco-maniputation systems, such as fall recovery.
- **p. 1 / Abstract - extractive body cue:** Existing approaches are cither limited to simulations that overlook hardware constraints or rely on predefined ground-specific motion trajectories, failing to ‘up across postures in real~ ...
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we present HOST (Humanoid Standing-up Control), a reinforcement learning framework that learns standing-up control from scratch, enabling robust sim= to-real transfer ...
- **p. 1 / Abstract - extractive body cue:** raining on diverse simulated ter ensure successful real-world deployment, we constrain the motion with smoothness regularization and implicit motion speed bound to alleviate oscillatory and ...
- **p. 1 / Abstract - extractive body cue:** After simulation-based training, the learned control
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our proposed RL. framework addresses these limitations by achieving posture adaptivity and real-world deployability without predefined motions, enabling smooth, stable, and robust standing-up across a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** ‘TABLE I: Comparison with existing methods on standing-up contol

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate exploration, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We overview the real-world performance of our controllers in Fg. / and summarize our core contributions as follows:
- **p. 12 / B. More Implementation Details - extractive body cue:** Our PPO implementation follows the framework outlined in [39]. ‘The actor network consists of 4 3-layer MLP with hidden dimensions [512, 256, 128], while each ...
- **p. 12 / B. More Implementation Details - extractive body cue:** We present the complete set of ward functions and their detailed descriptions in Tulble V1 Several regularization reward terms are adapted from prior work [21, ...
- **p. 13 / B. More Implementation Details - extractive body cue:** During the hardware deployment, the stiffness of hip and knee joints are amplified to 1.5 times than the simulation ones, similar to G1, We present ...
- **p. 13 / B. More Implementation Details - extractive body cue:** postures, PD controllers, observation and action spaces.
- **p. 12 / B. More Implementation Details - extractive body cue:** The lower bounds for the vertical force and action bound are ON and 0.25, respectively.
- **p. 13 / B. More Implementation Details - extractive body cue:** We make the following adjustment to work the algorithm: scale of pulling force, height for curriculum, height for stage

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | postures, PD controllers, observation and action spaces. | proprioception, reference pose/motion, visual or language command | p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details) |
| State/latent | postures, controllers, observation, action, spaces, lower, bounds, vertical, force, bound, respectively, Curriculum | whole-body pose, balance/contact state와 skill/mode | p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details) |
| Output/action | The lower bounds for the vertical force and action bound are ON and 0.25, respectively. | joint/whole-body action, motion target 또는 task trajectory | p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details) |
| Objective/outcome | We make the following adjustment to work the algorithm: more strict constraints on hip joint deviation rewards, weights for reward groups, and additional thigh orientation reward functions as a replacement for shank ... | tracking, balance, skill/task success와 recovery | p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details) |

## Main Claims and Actual Contribution

- 여러 가치 추정기와 지형 난도 교육과정을 사용해 자세별 일어서기 행동을 학습한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p064.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p064.pdf#page=4)
- 동작의 급격한 변화와 관절 속도를 억제하는 설계를 검토하고 실제 실내·외 표면에서 기립 동작을 평가한다. [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p064.pdf#page=5) · [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p064.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (B. Main Results), p. 6 (B. Main Results) |
| Embodiment/environment | this conclusion, with our approach achieving a 100% success rate and high motion smoothness across all scenes.' Generalization to outdoor environments (Viz. | hardware/simulator version and reset protocol | p. 8 (A. Main Results), p. 9 (B. Sim-to-real Analysis) |
| Dataset/benchmark | During real-world deployment, we observe a significant torque gap between simulation and reality (see Fig. | role, split, size and leakage | p. 8 (A. Main Results), p. 9 (B. Sim-to-real Analysis), p. 13 (B. More Implementation Details), p. 13 (B. More Implementation Details) |
| Metric | key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same reward functions, the performance of the single critic version of HOST deteriorates significantly across ... | definition, denominator, direction and uncertainty | p. 6 (B. Main Results), p. 6 (B. Main Results), p. 8 (A. Main Results) |
| Baseline/ablation | HOST with short history length underperforms in contact-rich scenarios, such as the Wall terrain, In contrast, a longer history length improves performance, though it slightly reduces motion smoothness and increases energy consumption ... | fair input/data/compute/action matching | p. 6 (B. Main Results), p. 8 (A. Main Results), p. 12 (B. More Implementation Details) |

## Explicit Limitations and Failure Boundary

- **p. 6 / B. Main Results - extractive body cue:** Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a ...
- **p. 9 / C. Emergent Properties - extractive body cue:** We further tested our controllers on a 15° slippery slope, simulating challenging real-world conditions such as unstable surfaces.
- **p. 8 / A. Main Results - extractive body cue:** Motion oscillations are observed in all scenes without smoothness regularization, often leading to standing-up failures, In contrast, our method produces smooth and stable motions, especially ...
- **p. 9 / VII. CoxcLusion - extractive body cue:** Our proposed framework, HOST, advances humanoid standing-up control by addressing the limitations of existing methods, which either neglect hardware constraints or rely on predefined motion ...
- **p. 12 / B. More Implementation Details - extractive body cue:** are handcrafted without collision models.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Robustness analysis in simulation. Evaluation of contol policies under four environmental disturbances demonstrates the robustness of our contol
- **p. 13 / B. More Implementation Details - extractive body cue:** Observation noises are without curriculum, set as below:

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (I. INTRODUCTION), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details)이다.
