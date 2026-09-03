# Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://papers.nips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html.
> PDF retrieval source: https://arxiv.org/pdf/2409.20537. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, cross-embodiment, proprioception, visual representation, heterogeneous data, Transformer
- Official paper: https://papers.nips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html
- Full-text retrieval: https://arxiv.org/pdf/2409.20537
- Code/Project: https://liruiw.github.io/hpt/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Recent progress in open-source large-scale data collection [14, 75] has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data has posed ...를 문제로 두고, We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** One of the roadblocks for training generalist robotic models today is heterogeneity.
- **p. 1 / Abstract - extractive body cue:** Previous robot learning methods often collect data to train with one specific embodiment for one task, which is expensive and prone to overfitting.
- **p. 1 / Abstract - extractive body cue:** This work studies the problem of learning policy representations through heterogeneous pretraining on robot data across different embodiments and tasks at scale.
- **p. 1 / Abstract - extractive body cue:** We propose Heterogeneous Pre-trained Transformers (HPT), which pre-train a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared ...
- **p. 1 / Abstract - extractive body cue:** This general architecture aligns the specific proprioception and vision inputs from distinct embodiments to a short sequence of tokens and then processes such tokens to ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent progress in open-source large-scale data collection [14, 75] has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) ...
- **p. 2 / 1 Introduction - extractive body cue:** The heterogeneity in robotics presents a distinct challenge: different robots are physically different embodiments1 of hardware acting in different environments.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose to address this issue by aligning the proprioception and vision information from different embodiments to a shared "language" of policies ...
- **p. 5 / 1 Introduction - extractive body cue:** This is used as the input sequence to the trunk that we introduce below.
- **p. 4 / 1 Introduction - extractive body cue:** These tokenizers map heterogeneous inputs from different embodiments to a fixed number of tokens with fixed dimensions, which enables the trunk to treat them in ...
- **p. 5 / 1 Introduction - extractive body cue:** We show illustrations of dataset mixtures (each color is a distinct embodiment) from different domains including real robot teleop [14], deployed robots [38], simulations, and ...
- **p. 17 / A Implementation Details - extractive body cue:** Different from previous work [55, 86], we use minimal amounts of processing and cleaning of the observation and actions in the raw trajectories.
- **p. 17 / A.1 Dataset Details - extractive body cue:** Since the human datasets do not contain proprioception and action information, we use hand poses and 2D positions in the image space as surrogates for ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We reinitialize the head and stem parameters with embodiment-specific input and output dimensions (such as different proprioception and action dimensions), and freeze the weights of the trunk. | multi-view observation, language/task label과 action trajectory | p. 6 (1 Introduction), p. 4 (1 Introduction) |
| State/latent | reinitialize, head, stem, parameters, embodiment-specific, input, output, dimensions, different, proprioception, action, freeze | shared representation, embodiment/task identity와 data distribution | p. 6 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Output/action | 3 Heterogenoues Pre-trained Transformers (HPT) In heterogeneous robot learning with cross embodiments, the data are generated from different domains such as simulation and real robots, across sensory modalities such as RGB images, ... | dataset sample 또는 learned policy action | p. 4 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction) |
| Objective/outcome | Since the human datasets do not contain proprioception and action information, we use hand poses and 2D positions in the image space as surrogates for the supervised learning objectives. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 17 (A.1 Dataset Details) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose to address this issue by aligning the proprioception and vision information from different embodiments to a shared "language" of policies ...
- **p. 5 / 1 Introduction - extractive body cue:** This is used as the input sequence to the trunk that we introduce below.
- **p. 4 / 1 Introduction - extractive body cue:** These tokenizers map heterogeneous inputs from different embodiments to a fixed number of tokens with fixed dimensions, which enables the trunk to treat them in ...
- **p. 5 / 1 Introduction - extractive body cue:** We show illustrations of dataset mixtures (each color is a distinct embodiment) from different domains including real robot teleop [14], deployed robots [38], simulations, and ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different simulator ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 12: Transfer Learning in the Real World. We evaluate the pre-trained HPTs on four tasks / two embodiments. The average success rate with standard ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 22 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Embodiment/environment | For the additional 7 simulation dataset, we use the simulator benchmarks across all popular simulators Drake [81], Mujoco [89, 49], Isaac Sim [20], and PyBullet [80], as well as Sapien [52] and ... | hardware/simulator version and reset protocol | p. 17 (A.1 Dataset Details), p. 17 (A.1 Dataset Details) |
| Dataset/benchmark | For the additional 7 simulation dataset, we use the simulator benchmarks across all popular simulators Drake [81], Mujoco [89, 49], Isaac Sim [20], and PyBullet [80], as well as Sapien [52] and ... | role, split, size and leakage | p. 17 (A.1 Dataset Details), p. 17 (A.1 Dataset Details) |
| Metric | Figure 12: Transfer Learning in the Real World. We evaluate the pre-trained HPTs on four tasks / two embodiments. The average success rate with standard deviations is computed for 45 trials per ... | definition, denominator, direction and uncertainty | p. 10 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Baseline/ablation | Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we show that an improvement in performance can ... | fair input/data/compute/action matching | p. 22 (Figure/Table caption), p. 8 (Figure/Table caption), p. 10 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6 Conclusion - extractive body cue:** See Appendix §C for some failure modes.
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 18: Ablation Study on HPT Stem. We ablate the pre-training performance for (a) proprioception, (b) vision stems, and (c) vision encoders. Setting: HPT-S, batch ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 19: (a) Initial Condition Overlay. We visualize different rollout initial conditions during test times. (b) Failure Cases of the Learned Policy in the Real ...
- **p. 10 / 6 Conclusion - extractive body cue:** We hope this perspective will inspire future work in handling the heterogeneous nature of robotic data for robotic foundation models.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different simulator ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 13: Large-scale Dataset Heterogeneity in Robotics. We show different dataset mixtures at increasing scales (top row) across trajectory counts, dataset sample counts, and sampling ...

## Why Read It

VLA and generalist robot policies의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Recent progress in open-source large-scale data collection [14, 75] has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data has posed ...를 문제로 두고, We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction), p. 8 (1 Introduction), p. 17 (A Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Recent progress in open-source large-scale data collection [14, 75] has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data ... (p. 1, 1 Introduction).
- **Actual contribution:** We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments. (p. 2, 1 Introduction).
- **Evaluation boundary:** Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we show that an improvement in ... (p. 22, Figure/Table caption).
- **Explicit failure boundary:** In Figure 19, we show some failure cases of the learned HPT policies in the real world. (p. 24, C Failure Cases).
