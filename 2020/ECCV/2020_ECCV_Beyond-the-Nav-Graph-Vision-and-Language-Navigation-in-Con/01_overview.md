# Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2004.02857.
> PDF retrieval source: https://arxiv.org/pdf/2004.02857. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Navigation, Robotics, Navigation, Benchmark
- Official paper: https://arxiv.org/abs/2004.02857
- Full-text retrieval: https://arxiv.org/pdf/2004.02857
- Code/Project: https://jacobkrantz.github.io/vlnce/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, these techniques are each independently far from perfect and such an agent would need to learn the limitations of these lowerlevel control systems - facing consequences when proposed waypoints cannot be ...를 문제로 두고, In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control via low-level actions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Springing forth from the pages of science fiction and capturing the daydreams of weary chore-doers everywhere, the promise and potential of general-purpose robotic assistants that ...
- **p. 1 / 1 Introduction - extractive body cue:** Taking a small step towards this goal, recent work has begun developing artificial agents that follow natural language navigation instructions in perceptually-rich, simulated environments [4,6].
- **p. 1 / 1 Introduction - extractive body cue:** An example instruction might be "Go down the hall and turn left at the wooden desk.
- **p. 1 / 1 Introduction - extractive body cue:** Continue until you reach the kitchen and then stop by the kettle." and agents are evaluated by their ability to follow the described path in ...
- **p. 1 / 1 Introduction - extractive body cue:** Many of these tasks have been developed from datasets of panoramic images captured in real scenes - e.g.
- **p. 3 / 1 Introduction - extractive body cue:** However, these techniques are each independently far from perfect and such an agent would need to learn the limitations of these lowerlevel control systems - ...
- **p. 2 / 1 Introduction - extractive body cue:** Taken together, these assumptions make current settings poor reflections of the real world both in terms of control (ignoring actuation, navigation, and localization error) and ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control ...
- **p. 1 / 1 Introduction - extractive body cue:** This paradigm enables efficient data collection and high visual fidelity compared to 3D scanning or creating synthetic environments; however, scenes are only observed from a ...
- **p. 4 / 1 Introduction - extractive body cue:** To summarize our contributions, we: - Lift the VLN task to continuous 3D environments - removing many unrealistic assumptions imposed by the nav-graph-based representation.
- **p. 1 / 1 Introduction - extractive body cue:** Many of these tasks have been developed from datasets of panoramic images captured in real scenes - e.g.
- **p. 3 / 1 Introduction - extractive body cue:** We develop agent architectures for this task and explore how popular mechanisms for VLN transfer to the VLN-CE setting.
- **p. 3 / 1 Introduction - extractive body cue:** Specifically, we develop a simple sequence-to-sequence baseline architecture as well as a cross-modal attentionbased model.
- **p. 2 / 1 Introduction - extractive body cue:** Our VLN-CE setting (b) lifts these assumptions by instantiating the task in continuous environments with low-level actions - providing a more realistic testbed for robot ...
- **p. 1 / 3 Facebook AI Research - extractive body cue:** To contextualize this new task, we develop models that mirror many of the advances made in prior settings as well as single-modality baselines.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our VLN-CE setting (b) lifts these assumptions by instantiating the task in continuous environments with low-level actions - providing a more realistic testbed for robot instruction following. - a static topological representation ... | standardized observation, action, task state와 evaluation split | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | VLN-CE, setting, lifts, assumptions, instantiating, task, continuous, environments, low-level, actions, providing, more | benchmark state/goal와 method decision | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | We perform a number of input-modality ablations to assess the biases and baselines in this new setting (including models without perception or instructions as suggested in [27]). | policy/controller trajectory 또는 measured result | p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | How an actual agent might acquire and update such a topology in new environments is an open question. - Oracle navigation. | success metric, robustness, generalization과 reproducibility | p. 2 (1 Introduction), p. 4 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control ...
- **p. 1 / 1 Introduction - extractive body cue:** This paradigm enables efficient data collection and high visual fidelity compared to 3D scanning or creating synthetic environments; however, scenes are only observed from a ...
- **p. 4 / 1 Introduction - extractive body cue:** To summarize our contributions, we: - Lift the VLN task to continuous 3D environments - removing many unrealistic assumptions imposed by the nav-graph-based representation.
- **p. 1 / 1 Introduction - extractive body cue:** Many of these tasks have been developed from datasets of panoramic images captured in real scenes - e.g.
- **p. 3 / 1 Introduction - extractive body cue:** We develop agent architectures for this task and explore how popular mechanisms for VLN transfer to the VLN-CE setting.
- **p. 12 / 5 Experiments - extractive body cue:** Despite having no learned components nor processing any input, both these agents achieve approximately 3% success rates in val-unseen.
- **p. 12 / 5 Experiments - extractive body cue:** We find that depth is a very strong signal for learning, with models lacking it (No Depth and No Vision) failing to outperform chance (≤1% ...
- **p. 11 / 5 Experiments - extractive body cue:** For our discussion, we will examine success rate and SPL as the primary metrics for performance and use NDTW to describe how paths differ in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 12 (5 Experiments), p. 12 (5 Experiments) |
| Embodiment/environment | This Cross-Modal Attention PM+DA*+Aug model achieves an SPL of 0.35 on val-seen and 0.30 on val-unseen - succeeding on 32% of episodes in new environments. | hardware/simulator version and reset protocol | p. 13 (5 Experiments), p. 11 (5 Experiments) |
| Dataset/benchmark | Our baseline Seq2Seq model significantly outperforms the random and hand-crafted baselines, successfully reaching the goal in 20% of val-unseen episodes. | role, split, size and leakage | p. 13 (5 Experiments), p. 11 (5 Experiments), p. 12 (5 Experiments), p. 14 (5 Experiments) |
| Metric | We report standard metrics for visual navigation tasks defined in [2,4,18] - trajectory length in meters (TL), navigation error in meters from goal at termination (NE), oracle success rate (OS), success rate ... | definition, denominator, direction and uncertainty | p. 11 (5 Experiments), p. 11 (5 Experiments), p. 12 (5 Experiments) |
| Baseline/ablation | Our baseline Seq2Seq model significantly outperforms the random and hand-crafted baselines, successfully reaching the goal in 20% of val-unseen episodes. | fair input/data/compute/action matching | p. 12 (5 Experiments), p. 13 (5 Experiments), p. 12 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Experiments - extractive body cue:** The second example shows a failure of the agent - it navigates towards the wrong windows and fails to first "pass the kitchen" - stopping ...
- **p. 14 / 5 Experiments - extractive body cue:** We also observe failures when the agent never sees the object(s) referred to by the instruction in the scene - with a limited egocentric field-of-view, ...
- **p. 15 / 6 Discussion - extractive body cue:** In models presented here, we took an approach where observations were mapped directly to low-level control in an end-to-end manner; however, exploring modular approaches is ...
- **p. 12 / 5 Experiments - extractive body cue:** We believe that depth enable agents to quickly begin traversing environments effectively (e.g. without collisions) and without this it is very difficult to bootstrap to ...
- **p. 15 / 5 Experiments - extractive body cue:** By default, our models cannot succeed on these.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 2. We transfer nav-graph trajectories over panoramas (blue dots) from the Room-to- Room (R2R) dataset to locations in reconstructed Matterport3D (MP3D) environments. Some map ...
- **p. 12 / 5 Experiments - extractive body cue:** The No Image model also achieves 17% success, similarly failing to reason about instructions.

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, these techniques are each independently far from perfect and such an agent would need to learn the limitations of these lowerlevel control systems - facing consequences when proposed waypoints cannot be ...를 문제로 두고, In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control via low-level actions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
