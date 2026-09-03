# OpenVLA: An Open-Source Vision-Language-Action Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v270/kim25c.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: VLA, Robotics, Imitation Learning
- Official paper: https://proceedings.mlr.press/v270/kim25c.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf
- Code/Project: https://github.com/openvla/openvla
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 While reproducing this scale of pretraining for robotics is still an open challenge - even the largest robot manipulation datasets [1, 11] only have 100K to 1M examples - this imbalance suggests ...를 문제로 두고, To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** A key weakness of learned policies for robotic manipulation is their inability to generalize beyond their training data: while existing policies trained for individual skills ...
- **p. 2 / 1 Introduction - extractive body cue:** Yet beyond robotics, existing foundation models for vision and language such as CLIP [8], SigLIP [9], and Llama 2 [10] are capable of these types ...
- **p. 2 / 1 Introduction - extractive body cue:** While reproducing this scale of pretraining for robotics is still an open challenge - even the largest robot manipulation datasets [1, 11] only have 100K ...
- **p. 2 / 1 Introduction - extractive body cue:** Towards this goal, existing work has explored integrating pretrained language and vision-language models for robotic representation learning [12-14] and as a component in modular systems ...
- **p. 2 / 1 Introduction - extractive body cue:** More recently, they have been used for directly learning visionlanguage-action models [VLAs; 1, 7, 17, 18] for control.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.
- **p. 2 / 1 Introduction - extractive body cue:** OpenVLA consists of a pretrained visuallyconditioned language model backbone that captures visual features at multiple granularities, fine-tuned on a large, diverse dataset of 970k robot ...
- **p. 3 / 1 Introduction - extractive body cue:** As a final contribution, we open-source all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale, with the hope that ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA: [ x, , Grip] = … Δ Δθ Δ Multi-Robot Control & Efficient Fine-Tuning Large-Scale Robot Training Data Fully Data Weights Code Open-Source Figure ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.
- **p. 3 / 1 Introduction - extractive body cue:** of compute efficient fine-tuning methods leveraging low-rank adaptation [LoRA; 25] and model quantization [26] to facilitate adapting OpenVLA models on consumer-grade GPUs instead of large ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | OpenVLA: [ x, , Grip] = … Δ Δθ Δ Multi-Robot Control & Efficient Fine-Tuning Large-Scale Robot Training Data Fully Data Weights Code Open-Source Figure 1: We present OpenVLA, a 7B-parameter open-source ... | image/video, language instruction, proprioception과 history | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |
| State/latent | OpenVLA, Grip, Multi-Robot, Control, Efficient, Fine-Tuning, Large-Scale, Robot, Training, Data, Fully, Weights | language-grounded task state와 action-policy context | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 Introduction) |
| Output/action | Abstract: Large policies pretrained on a combination of Internet-scale visionlanguage data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new behaviors from ... | continuous action, pose 또는 action chunk | p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | instruction following, task success, generalization과 latency | instruction following, task success, generalization과 latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.
- **p. 2 / 1 Introduction - extractive body cue:** OpenVLA consists of a pretrained visuallyconditioned language model backbone that captures visual features at multiple granularities, fine-tuned on a large, diverse dataset of 970k robot ...
- **p. 3 / 1 Introduction - extractive body cue:** As a final contribution, we open-source all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale, with the hope that ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA: [ x, , Grip] = … Δ Δθ Δ Multi-Robot Control & Efficient Fine-Tuning Large-Scale Robot Training Data Fully Data Weights Code Open-Source Figure ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Bridge V2 WidowX evaluation task categories and results. We evaluate OpenVLA and prior state-of- the-art generalist robot policies on a comprehensive suite of ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 6: Detailed Google robot evaluation results. We report full evaluation results for Google robot evaluations discussed in Section 4.1. Each generalist policy is evaluated ...
- **p. 7 / 4 Experiments - extractive body cue:** Notably, prior works achieve strong performance only in either precise or diverse tasks, resulting in widely varying success rates.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Embodiment/environment | Qualitatively, both RT-2-X and OpenVLA exhibit markedly more robust behaviors than the other tested models, such as approaching the correct object when distractor objects are present, properly orienting the robot's end-effector to ... | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | 2In Section 4.3, we experiment with a version of the OpenVLA model that is pretrained with a smaller robot data mixture (the same OpenX dataset mixture as Octo) and has a slightly ... | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (7.0 GB), p. 6 (4 Experiments) |
| Metric | Table 11: Quantized inference experiment results with blocking control. We report the success rate and standard error of OpenVLA on various BridgeData V2 WidowX tasks with bfloat16 precision (the default approach), 8-bit ... | definition, denominator, direction and uncertainty | p. 33 (Figure/Table caption), p. 25 (Figure/Table caption), p. 35 (Figure/Table caption) |
| Baseline/ablation | (2) Can OpenVLA be effectively fine-tuned on a new robot setup and task, and how does it compare to state-of-the-art data-efficient imitation learning approaches? | fair input/data/compute/action matching | p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7.0 GB - extractive body cue:** The current OpenVLA model has several limitations.
- **p. 8 / 7.0 GB - extractive body cue:** 5 Conclusion and Limitations In this work, we presented OpenVLA, a state-of-the-art, open-source vision-language-action model that obtains strong performance for cross-embodiment robot control out-of-the-box.
- **p. 32 / Figure/Table caption - extractive body cue:** Table 10: Fine-tuned vs. frozen vision encoder experiment results. We evaluate the performance of fine-tuning ("Fine-Tuned") vs. freezing the vision encoder ("Frozen Vision") in two ...
- **p. 7 / 4 Experiments - extractive body cue:** Additionally, we evaluate Octo [5] fine-tuned on the target dataset (RT-2-X does not support fine-tuning).
- **p. 6 / 4 Experiments - extractive body cue:** We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when distractors are present.
- **p. 7 / 4 Experiments - extractive body cue:** Franka-Tabletop Franka-DROID 66.7 53.5 33.3 93.3 80.0 0.0 83.3 63.3 26.7 Narrow Single-Instruction Tasks 19.4 27.8 30.6 27.8 22.2 66.7 16.7 25.0 91.7 Diverse Multi-Instruction ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 6: BridgeData V2 WidowX robot evaluation tasks. We evaluate every generalist robot policy on 4 types out-of-distribution (OOD) generalization tasks: visual, motion, physical, and ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 While reproducing this scale of pretraining for robotics is still an open challenge - even the largest robot manipulation datasets [1, 11] only have 100K to 1M examples - this imbalance suggests ...를 문제로 두고, To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** While reproducing this scale of pretraining for robotics is still an open challenge - even the largest robot manipulation datasets [1, 11] only have 100K to 1M examples - this ... (p. 2, 1 Introduction).
- **Actual contribution:** To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies. (p. 2, 1 Introduction).
- **Evaluation boundary:** Figure 4: Google robot evaluation results. We evaluate generalist robot policies on in-distribution and out-of- distribution (OOD) tasks on the mobile manipulator used in RT-1 and RT-2 evaluations [2, 7]. ... (p. 6, Figure/Table caption).
- **Explicit failure boundary:** We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when distractors are present. (p. 6, 4 Experiments).
