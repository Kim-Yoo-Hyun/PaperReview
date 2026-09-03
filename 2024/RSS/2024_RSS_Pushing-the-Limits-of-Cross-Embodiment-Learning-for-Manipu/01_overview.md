# Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p093.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p093.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, cross-embodiment, goal-conditioned policy, manipulation, Navigation, robot data
- Official paper: https://www.roboticsproceedings.org/rss20/p093.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p093.html
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 However, these prior works typically restrict their investigations to sets of similar embodiments - e.g., arms with parallel jaw grippers.를 문제로 두고, While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating for the first time that navigation data can ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent years in robotics and imitation learning have shown remarkable progress in training large-scale foundation models by leveraging data across a multitude of embodiments.
- **p. 1 / Abstract - extractive body cue:** The success of such policies might lead us to wonder: just how diverse can the robots in the training set be while still facilitating positive ...
- **p. 1 / Abstract - extractive body cue:** In this work, we study this question in the context of heterogeneous embodiments, examining how even seemingly very different domains, such as robotic navigation and ...
- **p. 1 / Abstract - extractive body cue:** We train a single goalconditioned policy that is capable of controlling robotic arms, quadcopters, quadrupeds, and mobile bases.
- **p. 1 / Abstract - extractive body cue:** We then investigate the extent to which transfer can occur across navigation and manipulation on these embodiments by framing them as a single goal-reaching task.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these prior works typically restrict their investigations to sets of similar embodiments - e.g., arms with parallel jaw grippers.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The advent of large-scale foundation models in machine learning has enabled harnessing diverse datasets to enhance sample efficiency, improve generalization, and facilitate transfer to novel ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating for ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present, to our knowledge, the first results demonstrating a large-scale policy trained jointly on navigation and manipulation data from many different robots, showing that ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** Each trajectory τ ∈Dem consists of a sequence of observations (images) and actions.
- **p. 3 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** While we could simply train a single policy across all of the navigation and manipulation datasets to output action labels that match each specific dataset ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The advent of large-scale foundation models in machine learning has enabled harnessing diverse datasets to enhance sample efficiency, improve generalization, and facilitate transfer to novel ...
- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Our heterogeneous cross-embodiment model consists of five different components: two observation encoders, a transformer, a diffusion policy action head [81], and an MLP distance prediction ...
- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** At a high level, we want our model to process its observations using some encoder, feed its embeddings into a transformer, and then output both ...
- **p. 4 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** We use separate observation and goal convolutional encoders to tokenize visual observations, which are passed through a Transformer block.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The objective of goal-conditioned imitation learning is to train a policy π(a/o, og) to output actions that control a particular embodiment given the current and goal observations. | egocentric RGB-D, language/task goal, base-arm proprioception | p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| State/latent | objective, goal-conditioned, imitation, learning, train, policy, output, actions, control, particular, embodiment, given | map/object/contact state와 base-arm coordination decision | p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| Output/action | To solve this problem, we train a goal-conditioned policy π(a/o, og) that outputs k actions into the future given a context of c observations. | base motion plus arm/gripper action | p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 7 (VI. ANALYSIS) |
| Objective/outcome | Our overall objective is the weighted combination of these two losses: L(θ, ϕ, ψ) = Ldiffusion(θ, ψ) + λLdistance(θ, ψ). | long-horizon task success, reachability, collision과 recovery | p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 1 (Body text (section boundary not confidently recovered)) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating for ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present, to our knowledge, the first results demonstrating a large-scale policy trained jointly on navigation and manipulation data from many different robots, showing that ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** Each trajectory τ ∈Dem consists of a sequence of observations (images) and actions.
- **p. 3 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** While we could simply train a single policy across all of the navigation and manipulation datasets to output action labels that match each specific dataset ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The advent of large-scale foundation models in machine learning has enabled harnessing diverse datasets to enhance sample efficiency, improve generalization, and facilitate transfer to novel ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Does manipulation help navigation? Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement in ...
- **p. 9 / VI. ANALYSIS - extractive body cue:** Despite the fact that neither the table nor the egg was seen in the training data of the policy, the robot achieves a 50% success ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Does navigation help manipulation? By aligning action coordinate frames, training on navigation and driving datasets results in a 20% improvement across five challenging ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 9 (VI. ANALYSIS) |
| Embodiment/environment | Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement in navigation performance (success % on y-axis). | hardware/simulator version and reset protocol | p. 8 (VI. ANALYSIS), p. 7 (VI. ANALYSIS) |
| Dataset/benchmark | Three of these robots-the LoCoBot, Jackal, and Unitree Go1-were present in the training dataset, while the DJI Tello is a novel embodiment. | role, split, size and leakage | p. 8 (VI. ANALYSIS), p. 7 (VI. ANALYSIS), p. 7 (VI. ANALYSIS), p. 9 (VI. ANALYSIS) |
| Metric | Fig. 6: Does manipulation help navigation? Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement in navigation performance (success % on y-axis). 17% ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 7 (VI. ANALYSIS), p. 7 (VI. ANALYSIS) |
| Baseline/ablation | Training our policy on a manipulation and navigation data split had a 20% greater success rate over 5 tasks compared to training only on manipulation data. | fair input/data/compute/action matching | p. 7 (VI. ANALYSIS), p. 9 (VI. ANALYSIS), p. 8 (VI. ANALYSIS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / VI. ANALYSIS - extractive body cue:** Gauging object distance is analogous to testing the robustness to a change in table height in tabletop manipulation, which previous works have identified as a ...
- **p. 7 / VI. ANALYSIS - extractive body cue:** This requires the robot to avoid colliding with the shelf as well as gauge its distance to the object, which is fundamentally similar to the ...
- **p. 8 / VI. ANALYSIS - extractive body cue:** While we qualitatively observed that these policies had better estimates for the closest node and had less collision with the environment, we acknowledge that the ...
- **p. 9 / VI. ANALYSIS - extractive body cue:** However, small changes in the mobile base can elicit large changes in position of the robot arm with respect to the scene, and the robot ...

## Why Read It

VLA and generalist robot policies의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 However, these prior works typically restrict their investigations to sets of similar embodiments - e.g., arms with parallel jaw grippers.를 문제로 두고, While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating for the first time that navigation data can ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, these prior works typically restrict their investigations to sets of similar embodiments - e.g., arms with parallel jaw grippers. (p. 1, I. INTRODUCTION).
- **Actual contribution:** The advent of large-scale foundation models in machine learning has enabled harnessing diverse datasets to enhance sample efficiency, improve generalization, and facilitate transfer to novel domains [1]. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 5: Does navigation help manipulation? By aligning action coordinate frames, training on navigation and driving datasets results in a 20% improvement across five challenging tabletop manipulation tasks (success % ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** Gauging object distance is analogous to testing the robustness to a change in table height in tabletop manipulation, which previous works have identified as a common distribution shift artifact leading ... (p. 7, VI. ANALYSIS).
