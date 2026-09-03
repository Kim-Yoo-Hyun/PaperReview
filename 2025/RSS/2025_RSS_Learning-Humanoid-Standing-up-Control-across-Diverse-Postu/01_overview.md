# Learning Humanoid Standing-up Control across Diverse Postures

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p064.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p064.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, humanoid, standing up, fall recovery, sim-to-real
- Official paper: https://www.roboticsproceedings.org/rss21/p064.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p064.pdf
- Code/Project: https://taohuang13.github.io/humanoid-standingup.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Our proposed RL. framework addresses these limitations by achieving posture adaptivity and real-world deployability without predefined motions, enabling smooth, stable, and robust standing-up across a wide range of laboratory and outdoo ...를 문제로 두고, To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate exploration, Given the multiple stages of the task, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / I. INTRODUCTION - extractive body cue:** To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate exploration, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We overview the real-world performance of our controllers in Fg. / and summarize our core contributions as follows:
- **p. 12 / B. More Implementation Details - extractive body cue:** Our PPO implementation follows the framework outlined in [39]. ‘The actor network consists of 4 3-layer MLP with hidden dimensions [512, 256, 128], while each ...
- **p. 12 / B. More Implementation Details - extractive body cue:** We present the complete set of ward functions and their detailed descriptions in Tulble V1 Several regularization reward terms are adapted from prior work [21, ...
- **p. 13 / B. More Implementation Details - extractive body cue:** During the hardware deployment, the stiffness of hip and knee joints are amplified to 1.5 times than the simulation ones, similar to G1, We present ...
- **p. 6 / B. Main Results - extractive body cue:** key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same reward functions, the performance of the single ...
- **p. 6 / B. Main Results - extractive body cue:** HOST with short history length underperforms in contact-rich scenarios, such as the Wall terrain, In contrast, a longer history length improves performance, though it slightly ...
- **p. 8 / A. Main Results - extractive body cue:** this conclusion, with our approach achieving a 100% success rate and high motion smoothness across all scenes.' Generalization to outdoor environments (Viz.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

World models, safety, uncertainty, and recovery의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Our proposed RL. framework addresses these limitations by achieving posture adaptivity and real-world deployability without predefined motions, enabling smooth, stable, and robust standing-up across a wide range of laboratory and outdoo ...를 문제로 두고, To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate exploration, Given the multiple stages of the task, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
