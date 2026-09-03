# GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v305/deng25a.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, grasping, synthetic data
- Official paper: https://proceedings.mlr.press/v305/deng25a.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, unlike vision and language modalities, action data is absent from existing Internet datasets, demanding a new paradigm for data collection.를 문제로 두고, In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data acquisition burden, b) we ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** The fields of Natural Language Processing (NLP) and Computer Vision (CV) have undergone a paradigm shift with the advent of foundation models.
- **p. 2 / 1 Introduction - extractive body cue:** Large-scale models pretrained on vast amounts of Internet data exhibit zero-shot generalization to unseen scenarios [1, 2, 3] and few-shot adaptation for aligning with human ...
- **p. 2 / 1 Introduction - extractive body cue:** Inspired by this success, the foundation model for actions in the physical world has recently been introduced in Vision-Language-Action (VLA) models [5, 6, 7, 8].
- **p. 2 / 1 Introduction - extractive body cue:** These models process robotic visual observations and human instructions to directly generate robot actions.
- **p. 2 / 1 Introduction - extractive body cue:** However, unlike vision and language modalities, action data is absent from existing Internet datasets, demanding a new paradigm for data collection.
- **p. 2 / 1 Introduction - extractive body cue:** In addition, GraspVLA shows excellent generalization to long-tail object categories absent from synthetic action data, such as chargers, towels, and swimming goggles.
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real ...
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 2 / 1 Introduction - extractive body cue:** To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks.
- **p. 8 / 5 Hz - extractive body cue:** GraspVLA shows superior adaptability to novel tasks, surpassing the model without pretraining and all baselines.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** To bridge this gap, we explore the feasibility of training Vision-Language-Action (VLA) models entirely with large-scale synthetic action data.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Abstract: Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training.
- **p. 7 / 5 Hz - extractive body cue:** We benchmark GraspVLA against AnyGrasp [14], a state-of-the-art grasp detection model specialized in grasping.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Compared to AnyGrasp [14], the state-of-the-art in traditional grasping detection algorithms, GraspVLA supports natural language instructions and delivers a robust closed-loop grasping policy. | image/video, language instruction, proprioception과 history | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | Compared, AnyGrasp, state-of-the-art, traditional, grasping, detection, algorithms, GraspVLA, supports, natural, language, instructions | language-grounded task state와 action-policy context | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)) |
| Output/action | These models process robotic visual observations and human instructions to directly generate robot actions. | continuous action, pose 또는 action chunk | p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (1 Introduction) |
| Objective/outcome | Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. | instruction following, task success, generalization과 latency | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real ...
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 2 / 1 Introduction - extractive body cue:** To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks.
- **p. 8 / 5 Hz - extractive body cue:** GraspVLA shows superior adaptability to novel tasks, surpassing the model without pretraining and all baselines.
- **p. 24 / Figure/Table caption - extractive body cue:** Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while multiple views significantly ...
- **p. 6 / 5 Experiments - extractive body cue:** As illustrated in Table 1, GraspVLA achieves around 90% on all test sets and significantly outperforms all baselines, demonstrating strong zero-shot generalizability.
- **p. 6 / 5 Experiments - extractive body cue:** Our approach achieves the highest grasping success rate on items from both synthetic and web categories using short trajectories.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 24 (Figure/Table caption), p. 6 (5 Experiments) |
| Embodiment/environment | We define synthetic categories as those present in our SynGrasp-1B dataset, while web categories refer to those exclusively present in Internet grounding dataset. b) Synthetic categories c) Web categories 0.2m a) Robot ... | hardware/simulator version and reset protocol | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Dataset/benchmark | For generalists, we use π0 [7], OpenVLA [6], and Octo [26], three transformer-based policies pre-trained on large-scale real-world datasets. | role, split, size and leakage | p. 6 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Metric | For each object group, we also report the average Success weighted by Path Length (SPL) [76], a widely used metric that weights success rate with motion efficiency by penalizing unnecessarily long paths. | definition, denominator, direction and uncertainty | p. 6 (5 Experiments), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption) |
| Baseline/ablation | Additionally, the SPL metric reveals that GraspVLA grasps objects with shorter path lengths compared to π0 baselines which often exhibit hesitation. | fair input/data/compute/action matching | p. 6 (5 Experiments), p. 6 (5 Experiments), p. 24 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6 Conclusion - extractive body cue:** 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the Franka Panda arm with front and side views.
- **p. 9 / 6 Conclusion - extractive body cue:** Like most grasping policies, we synthesize grasp labels using force-closure, which do not account for deformability-a limitation common to all such methods.
- **p. 7 / 5 Experiments - extractive body cue:** We provide failure analysis in the supplementary.
- **p. 7 / 5 Experiments - extractive body cue:** We evaluate on three LIBERO suites (Long, Goal, Object), excluding Spatial, as its focus on spatial reasoning falls outside our scope.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 11: Examples of LIBERO Benchmark. We visualize both front and side views side by side. is considered a success. Similarly, if the target is ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, unlike vision and language modalities, action data is absent from existing Internet datasets, demanding a new paradigm for data collection.를 문제로 두고, In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data acquisition burden, b) we ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, unlike vision and language modalities, action data is absent from existing Internet datasets, demanding a new paradigm for data collection. (p. 2, 1 Introduction).
- **Actual contribution:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data acquisition burden, ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while multiple views significantly improve performance, our single-view implementation ... (p. 24, Figure/Table caption).
- **Explicit failure boundary:** Finally, the remaining failures (7%) include minor errors such as early gripper closure or collisions with the environment, which reinforcement learning could potentially address. (p. 26, C Details about Data Generation).
