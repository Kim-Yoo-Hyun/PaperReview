# Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p155.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p155.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, mid-level representation, 3D perception, bimanual manipulation, diffusion policy, generalization
- Official paper: https://www.roboticsproceedings.org/rss21/p155.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p155.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Large pre-trained robotics models have made significant progress in recent years towards improving robotic generalization capabilities by leveraging large-scale pre-training datasets, However, these models still face challenges in adapt ...를 문제로 두고, We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on a wide range of environments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this work, we investigate how spatially-grounded auxiliary representations can provide both broad, high-level grounding, as well as direct, actionable information to help policy learning ...
- **p. 1 / Abstract - extractive body cue:** We study these mid-level representations across three ‘critical dimensions: object-centricity, pose-awareness, and depthawareness.
- **p. 1 / Abstract - extractive body cue:** We use these interpretable mid-level representations to train specialist encoders via supervised learning, then use these representations as inputs to a diffusion policy to solve ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization ...
- **p. 1 / Abstract - extractive body cue:** This method achieves an average of 11% hi rate on average over a language-grounded baseline and a 21% higher success rate over a standard diffusion ...
- **p. 1 / 1. Ivrropuction - extractive body cue:** Large pre-trained robotics models have made significant progress in recent years towards improving robotic generalization capabilities by leveraging large-scale pre-training datasets, However, these models still ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** A key challenge with the multi-task policy learning regime is in obtaining policies that generalize to new objects, task variants, environmental factors and so on, ...

## Core Idea

- **p. 2 / 1. Ivrropuction - extractive body cue:** We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on a ...
- **p. 6 / B. Training - extractive body cue:** Similarly, our approach integrates mid-level expert outputs as implicit guidance in scenarios where no explicit reward signal is available, Instead of an advantage function, we ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** We find that reliance on structured signals presents a trade-off: policies that depend heavily on these representations can become more susceptible to overfiting and reduced ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** While one can hope to learn these relationships directly from end-to-end data, current large-scale robot policies that try to scale up imitation learning still struggle ...
- **p. 4 / V. ARCHITECTURE - extractive body cue:** We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints ...
- **p. 5 / B. Training - extractive body cue:** Once the expert modules are trained independently, their parameters are frozen. ‘Then, the policy network trained endto-end with a noise prediction loss.
- **p. 4 / V. ARCHITECTURE - extractive body cue:** At each state, we denoise the decoder predicts ¢ = 10 action chunks simultaneously with a transformer.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | By iteratively refining the training data and adjusting the weighting of consistent samples, our method creates a feedback loop that promotes tighter self-consistency between policy actions and mid-level ‘expert outputs. | multi-view observation, language/task label과 action trajectory | p. 6 (B. Training), p. 4 (V. ARCHITECTURE) |
| State/latent | iteratively, refining, training, data, adjusting, weighting, consistent, samples, creates, feedback, loop, promotes | shared representation, embodiment/task identity와 data distribution | p. 6 (B. Training), p. 4 (V. ARCHITECTURE), p. 3 (1. Ivrropuction) |
| Output/action | We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints (2 third-person images and 2 wrist images) ... | dataset sample 또는 learned policy action | p. 4 (V. ARCHITECTURE), p. 3 (1. Ivrropuction), p. 4 (1. Ivrropuction) |
| Objective/outcome | where A(s,a) represents the advantage function, which modulates the policy gradient loss Cyc based on the estimated benefit of selecting action « in states. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 6 (B. Training), p. 6 (B. Training), p. 5 (B. Training) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Ivrropuction - extractive body cue:** We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on a ...
- **p. 6 / B. Training - extractive body cue:** Similarly, our approach integrates mid-level expert outputs as implicit guidance in scenarios where no explicit reward signal is available, Instead of an advantage function, we ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** We find that reliance on structured signals presents a trade-off: policies that depend heavily on these representations can become more susceptible to overfiting and reduced ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** While one can hope to learn these relationships directly from end-to-end data, current large-scale robot policies that try to scale up imitation learning still struggle ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations lead ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Self-Consistency. On the left image, the robot's achieved trajectory doesn't match it's mid-level representation, which leads to a lower weight. In the right, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Real-World Results. There are clear differences in the benefits that different representations provide for tasks in the real world.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | For RT-H, ‘we relabel robot demonstrations with the language "move the arm leftright/up/down." For each environment in simulation and the real-world, we vary the object locations, add distractor objects, and change the ... | hardware/simulator version and reset protocol | p. 7 (C. Experiment Setup) |
| Dataset/benchmark | For RT-H, ‘we relabel robot demonstrations with the language "move the arm leftright/up/down." For each environment in simulation and the real-world, we vary the object locations, add distractor objects, and change the ... | role, split, size and leakage | p. 7 (C. Experiment Setup) |
| Metric | not stated or recoverable in the selected PDF body | definition, denominator, direction and uncertainty | 본문 anchor 없음 |
| Baseline/ablation | In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language baseline based on RE-H [2]. | fair input/data/compute/action matching | p. 7 (C. Experiment Setup), p. 7 (C. Experiment Setup), p. 7 (C. Experiment Setup) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4) Which policy architecture offers the best tradeoff be - extractive body cue:** tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs?
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Meanwhile, Table I! records the sensitivity scores for each of our mid-level experts as well as the robustness index. ‘The robustness index is computed by ...
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** This suggests that the benefits of more targeted feature utilization outweigh the slight decrease in robustness.

## Why Read It

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Large pre-trained robotics models have made significant progress in recent years towards improving robotic generalization capabilities by leveraging large-scale pre-training datasets, However, these models still face challenges in adapt ...를 문제로 두고, We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on a wide range of environments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Ivrropuction), p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 1 (1. Ivrropuction), p. 2 (1. Ivrropuction), p. 4 (V. ARCHITECTURE) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Large pre-trained robotics models have made significant progress in recent years towards improving robotic generalization capabilities by leveraging large-scale pre-training datasets, However, these models still face challenges in adapt ... (p. 1, 1. Ivrropuction).
- **Actual contribution:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization of the policy. (p. 1, Abstract).
- **Evaluation boundary:** In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language baseline based on RE-H [2]. (p. 7, C. Experiment Setup).
- **Explicit failure boundary:** This sensitivity-robusness tradeoff' underscores the necessity of developing robot policies that balance adherence 10 mid-level representations with the ability to remain adaptable and resilient in the face of environmental variations. ... (p. 4, 1. Ivrropuction).
