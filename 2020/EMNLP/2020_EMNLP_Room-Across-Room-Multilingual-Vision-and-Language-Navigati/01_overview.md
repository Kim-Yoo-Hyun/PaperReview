# Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://aclanthology.org/2020.emnlp-main.356/.
> PDF retrieval source: https://aclanthology.org/2020.emnlp-main.356.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / EMNLP
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Navigation, Navigation, grounding, Benchmark
- Official paper: https://aclanthology.org/2020.emnlp-main.356/
- Full-text retrieval: https://aclanthology.org/2020.emnlp-main.356.pdf
- Code/Project: https://github.com/google-research-datasets/RxR
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 High variance in path length, such that agents cannot simply exploit a strong length prior.를 문제로 두고, We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce Room-Across-Room (RxR), a new Vision-and-Language Navigation (VLN) dataset.
- **p. 1 / Abstract - extractive body cue:** RxR is multilingual (English, Hindi, and Telugu) and larger (more paths and instructions) than other VLN datasets.
- **p. 1 / Abstract - extractive body cue:** It emphasizes the role of language in VLN by addressing known biases in paths and eliciting more references to visible entities.
- **p. 1 / Abstract - extractive body cue:** Furthermore, each word in an instruction is time-aligned to the virtual poses of instruction creators and validators.
- **p. 1 / Abstract - extractive body cue:** We establish baseline scores for monolingual and multilingual settings and multitask learning when including Room-to-Room annotations (Anderson et al., 2018b).
- **p. 3 / 1 Introduction - extractive body cue:** High variance in path length, such that agents cannot simply exploit a strong length prior.
- **p. 3 / 1 Introduction - extractive body cue:** Paths may approach their goal indirectly, so agents cannot simply go straight to the goal.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.
- **p. 1 / Abstract - extractive body cue:** We introduce Room-Across-Room (RxR), a new Vision-and-Language Navigation (VLN) dataset.
- **p. 2 / 1 Introduction - extractive body cue:** In addition to verifying instruction quality, this allows us to collect a play-by-play account of how a human interpreted the instructions, represented as a pose ...
- **p. 2 / 1 Introduction - extractive body cue:** Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for agent training.
- **p. 1 / 1 Introduction - extractive body cue:** We provide monolingual and multilingual baseline experiments using a variant of the Reinforced Cross-Modal Matching agent (Wang et al., 2019).
- **p. 1 / Abstract - extractive body cue:** We also provide results for a model that learns from synchronized pose traces by focusing only on portions of the panorama attended to in human ...
- **p. 2 / 1 Introduction - extractive body cue:** This especially matters for VLN, as different languages encode spatial and temporal information in idiosyncratic ways-e.g., how contact/support relationships are expressed (Munnich et al., 2001), ...
- **p. 3 / 1 Introduction - extractive body cue:** Preliminaries Movement in the simulator is based on a navigation graph.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for agent training. | standardized observation, action, task state와 evaluation split | p. 2 (1 Introduction), p. 5 (1 Introduction) |
| State/latent | Guide, Follower, pose, traces, provide, dense, spatiotemporal, alignments, between, instructions, visual, percepts | benchmark state/goal와 method decision | p. 2 (1 Introduction), p. 5 (1 Introduction), p. 6 (29. US English instructions are the longest on av) |
| Output/action | The output of the Guide task is an audio file, a tokenized, timestamped, manually-transcribed instruction, and a pose trace (a series of timestamped 6-DOF camera poses). | policy/controller trajectory 또는 measured result | p. 5 (1 Introduction), p. 6 (29. US English instructions are the longest on av), p. 5 (29. US English instructions are the longest on av) |
| Objective/outcome | Datasets have been collected for both indoor (Anderson et al., 2018b; Thomason et al., 2019b; Qi et al., 2020) and outdoor (Chen et al., 2019; Mehta et al., 2020) environments; success in ... | success metric, robustness, generalization과 reproducibility | p. 1 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.
- **p. 1 / Abstract - extractive body cue:** We introduce Room-Across-Room (RxR), a new Vision-and-Language Navigation (VLN) dataset.
- **p. 2 / 1 Introduction - extractive body cue:** In addition to verifying instruction quality, this allows us to collect a play-by-play account of how a human interpreted the instructions, represented as a pose ...
- **p. 8 / 5 Experiments - extractive body cue:** Applying the same approach to textual attention did not improve performance.
- **p. 9 / 5 Experiments - extractive body cue:** The multimodal agent (4) outperforms both the languageonly agent (9) and the vision-only agent (10), indicating that both modalities contribute to performance.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5: RxR val-unseen: Monolingual vs. multilingual results. Training with both Guide and Follower paths benefits all languages (exp. 3 vs. 1 and 2), monolingual ...
- **p. 7 / 5 Experiments - extractive body cue:** In preliminary experiments, we found that pretraining the CNN in this way gave noticeable improvements over the same CNN pretrained for image classification on ImageNet ...
- **p. 7 / 5 Experiments - extractive body cue:** Monolingual Results Table 5 provides results on the val-unseen split for several training settings, as well as human performance from Follower annotations.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (5 Experiments), p. 9 (5 Experiments) |
| Embodiment/environment | Monolingual Results Table 5 provides results on the val-unseen split for several training settings, as well as human performance from Follower annotations. | hardware/simulator version and reset protocol | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Dataset/benchmark | Test Set RxR includes a heldout test set, which we divide into two splits: test-standard and testchallenge. | role, split, size and leakage | p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments) |
| Metric | Table 4: Simple baselines on val-unseen paths. RxR proves more difficult than R2R overall, and less amenable to agents that tend to go straight (baselines 2 and 3). Note: Baseline 3 partly ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 7 (5 Experiments), p. 7 (5 Experiments) |
| Baseline/ablation | 1 and 2), monolingual outperforms multilingual (exp. | fair input/data/compute/action matching | p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Experiments - extractive body cue:** Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's
- **p. 8 / 5 Experiments - extractive body cue:** This is consistent with results in multilingual machine translation (MT) and automatic speech recognition (ASR) where adding more languages can also lead to degradation for ...

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 High variance in path length, such that agents cannot simply exploit a strong length prior.를 문제로 두고, We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.
