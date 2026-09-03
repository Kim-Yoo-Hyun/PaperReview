# Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=cb0xbZ3APM.
> PDF retrieval source: https://arxiv.org/pdf/2505.23705. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=cb0xbZ3APM
- Full-text retrieval: https://arxiv.org/pdf/2505.23705
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, adapting LLMs and VLMs to real-world control requires addressing a number of new challenges.를 문제로 두고, To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-language-action (VLA) models provide a powerful approach to training control policies for physical systems, such as robots, by combining end-to-end learning with transfer of semantic ...
- **p. 1 / Abstract - extractive body cue:** However, the constraints of real-time control are often at odds with the design of VLMs: the most powerful VLMs have tens or hundreds of billions ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, recent VLA models have used specialized modules for efficient continuous control, such as action experts or continuous output heads, which typically ...
- **p. 1 / Abstract - extractive body cue:** While these modules improve real-time and control capabilities, it remains an open question whether they preserve or degrade the semantic knowledge contained in the pretrained ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we study this question in the context of VLAs that include a continuous diffusion or flow matching action expert, showing that naively ...
- **p. 1 / 1 Introduction - extractive body cue:** However, adapting LLMs and VLMs to real-world control requires addressing a number of new challenges.
- **p. 1 / 1 Introduction - extractive body cue:** Autoregressive decoding of discrete tokens is poorly suited to this kind of high-frequency continuous control, both because of the limited resolution of discretized actions and ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.
- **p. 2 / 1 Introduction - extractive body cue:** Second, using an action expert still enables fast inference.
- **p. 2 / 1 Introduction - extractive body cue:** While a number of different designs have been successful, a common theme is that models adapted for effective dexterous control typically augment a transformer or ...
- **p. 1 / 1 Introduction - extractive body cue:** The success of large language models (LLMs) can be attributed to the availability of large-scale datasets combined with powerful model architectures such as transformers that ...
- **p. 2 / 1 Introduction - extractive body cue:** At inference time, generating continuous actions with the smaller action expert is desirable for fast and precise control, while representation learning with discrete actions and ...
- **p. 1 / Abstract - extractive body cue:** While these modules improve real-time and control capabilities, it remains an open question whether they preserve or degrade the semantic knowledge contained in the pretrained ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | While a number of different designs have been successful, a common theme is that models adapted for effective dexterous control typically augment a transformer or VLM backbone with some sort of adapter ... | image/video, language instruction, proprioception과 history | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | While, number, different, designs, have, been, successful, common, theme, models, adapted, effective | language-grounded task state와 action-policy context | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/action | Furthermore, physical systems typically produce more complex observations than VLMs are trained for, such as multi-view images and proprioceptive states. | continuous action, pose 또는 action chunk | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction) |
| Objective/outcome | 1.7 1.25 3.14 1.42 NOISE ACTION EXPERT (300M) continuous actions -17 12 34 142 autoregressive loss flow matching loss bidirectional w/o loss stop gradient pick up the sleeve high-level prompt fold the ... | instruction following, task success, generalization과 latency | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.
- **p. 2 / 1 Introduction - extractive body cue:** Second, using an action expert still enables fast inference.
- **p. 8 / 6 Experiments - extractive body cue:** 6a shows that for the "table bussing" task our recipe achieves comparable performance to the embodiment specific results from above.
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Success rates (%) on the LIBERO [30] benchmark. Our method achieves a state-of-the-art in LIBERO-90 and LIBERO-Spatial, but is worse on LIBERO-10. inference ...
- **p. 7 / 6 Experiments - extractive body cue:** Our method consistently achieves the highest performance in the real world evaluations.
- **p. 8 / 6 Experiments - extractive body cue:** Our method received a score of 0.55 ± 0.09, π0 received 0.49±0.09, and π0-FAST achieved 0.45±0.09.
- **p. 7 / 6 Experiments - extractive body cue:** This seems to hurt performance on this task significantly.
- **p. 9 / 6 Experiments - extractive body cue:** 7, then joint-training without stop-gradient can also achieve good language following.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 8 (6 Experiments), p. 10 (Figure/Table caption) |
| Embodiment/environment | The robot is tasked with moving objects from a kitchen counter into an (already open) drawer. | hardware/simulator version and reset protocol | p. 9 (6 Experiments), p. 9 (6 Experiments) |
| Dataset/benchmark | A, B for details on tasks, datasets, and model training. | role, split, size and leakage | p. 9 (6 Experiments), p. 9 (6 Experiments), p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Metric | Table 1: Success rates (%) on the LIBERO [30] benchmark. Our method achieves a state-of-the-art in LIBERO-90 and LIBERO-Spatial, but is worse on LIBERO-10. inference (due to fewer tokens). Since here we ... | definition, denominator, direction and uncertainty | p. 10 (Figure/Table caption), p. 8 (6 Experiments), p. 9 (6 Experiments) |
| Baseline/ablation | Our method outperforms all other baselines both in terms of performance and the ability of the model to follow language instructions. | fair input/data/compute/action matching | p. 8 (6 Experiments), p. 7 (6 Experiments), p. 7 (6 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 6 Experiments - extractive body cue:** 4a) with a common failure mode of being unable to open the drawer.
- **p. 7 / 6 Experiments - extractive body cue:** A common limitation of many robot policies is that they pay much more attention to images than the language input [25].
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 10: Comparison of different state representations on "table bussing" task. Our method works well with both text and continuous state, while π0 works worse ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Problems with standard VLA recipes. The robot is instructed to bus the spoon into the bin. π0 [7] (left) ignores the command and ...
- **p. 8 / 6 Experiments - extractive body cue:** In comparison joint-training degrades in task completion.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, adapting LLMs and VLMs to real-world control requires addressing a number of new challenges.를 문제로 두고, To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
