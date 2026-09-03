# SUGAR: Pre-training 3D Visual Representations for Robotics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: 3D representation, Robotics, pretraining
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 vla 문제를 이해하기 위해 읽는다. 본문은 Pretraining in existing work, however, is typically limited to single objects and complete point clouds, hence, ignoring This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.를 문제로 두고, In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation learning on cluttered scenes. • We pre-train ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learning generalizable visual representations from Internet data has yielded promising results for robotics.
- **p. 1 / Abstract - extractive body cue:** Yet, prevailing approaches focus on pre-training 2D representations, being sub-optimal to deal with occlusions and accurately localize objects in complex 3D scenes.
- **p. 1 / Abstract - extractive body cue:** Meanwhile, 3D representation learning has been limited to single-object understanding.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce a novel 3D pre-training framework for robotics named SUGAR that captures semantic, geometric and affordance properties of objects through ...
- **p. 1 / Abstract - extractive body cue:** We underscore the importance of cluttered scenes in 3D representation learning, and automatically construct a multi-object dataset benefiting from cost-free supervision in simulation.
- **p. 1 / 1. Introduction - extractive body cue:** Pretraining in existing work, however, is typically limited to single objects and complete point clouds, hence, ignoring This CVPR paper is the Open Access version, ...
- **p. 1 / 1. Introduction - extractive body cue:** To alleviate the burden of data collection, recent endeavors [36, 37, 48, 49, 51, 62] have sought to leverage largescale internet data to pre-train 2D ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation ...
- **p. 2 / 1. Introduction - extractive body cue:** To enhance the capability of 3D representation in robotics, we propose SUGAR - a novel pre-training framework that learns semantics, geometry and affordance properties of ...
- **p. 1 / 1. Introduction - extractive body cue:** We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affordance on both single- and multi-object scenes. robotics.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce a novel 3D pre-training framework for robotics named SUGAR that captures semantic, geometric and affordance properties of objects through ...
- **p. 6 / 4.2. Referring Expression Grounding - extractive body cue:** OCID-Ref is collected in clean lab environments and consists of 58 object categories, 2,298 RGB-D images and 259,839 referring expressions for training.
- **p. 2 / 1. Introduction - extractive body cue:** To jointly train multiple properties, we propose a versatile transformer-based model comprising a point cloud encoder and a prompt-based decoder.
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** First, we only use a small transformer model which may not have sufficient capacity to jointly solve the five pre-training tasks when the pre-training data ...
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** As in the CML pretraining task, we use [img] and [txt] prompt tokens to extract point cloud features that are in the same space of ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation learning on cluttered scenes. • We pre-train ... | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 7 (4.3. Language-guided Robotic Manipulation) |
| State/latent | summary, contributions, three-fold, present, SUGAR, framework, versatile, transformer, architecture, point, cloud, representation | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 7 (4.3. Language-guided Robotic Manipulation), p. 2 (1. Introduction) |
| Output/action | This task aims to train a policy that can follow natural language instruction to perform manipulation tasks. | continuous action, pose 또는 action chunk | p. 7 (4.3. Language-guided Robotic Manipulation), p. 2 (1. Introduction), p. 7 (4.2. Referring Expression Grounding) |
| Objective/outcome | We underscore the importance of cluttered scenes in 3D representation learning, and automatically construct a multi-object dataset benefiting from cost-free supervision in simulation. | instruction following, task success, generalization과 latency | p. 1 (Abstract), p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation ...
- **p. 2 / 1. Introduction - extractive body cue:** To enhance the capability of 3D representation in robotics, we propose SUGAR - a novel pre-training framework that learns semantics, geometry and affordance properties of ...
- **p. 1 / 1. Introduction - extractive body cue:** We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affordance on both single- and multi-object scenes. robotics.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce a novel 3D pre-training framework for robotics named SUGAR that captures semantic, geometric and affordance properties of objects through ...
- **p. 6 / 4.2. Referring Expression Grounding - extractive body cue:** OCID-Ref is collected in clean lab environments and consists of 58 object categories, 2,298 RGB-D images and 259,839 referring expressions for training.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Performance of training with 10 demonstrations. (Ens m) significantly boosts the performance of the model trained from scratch with over 30% improvement. We ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Success rates of multi-task policies on 10 tasks of RLBench simulator.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot object recognition performance on three benchmarks. The Top1 accuracy is reported if not specified otherwise. The blue colored results in brackets on ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | ScanObjectNN is one of the most challenging 3D datasets, consisting of 15 common categories and 587 real-world 3D scans in the test split. | hardware/simulator version and reset protocol | p. 5 (4.1. Zero-shot Object Recognition), p. 5 (4. Evaluation on Robotic-related Tasks) |
| Dataset/benchmark | ScanObjectNN is one of the most challenging 3D datasets, consisting of 15 common categories and 587 real-world 3D scans in the test split. | role, split, size and leakage | p. 5 (4.1. Zero-shot Object Recognition), p. 5 (4. Evaluation on Robotic-related Tasks) |
| Metric | Table 4. Success rates of multi-task policies on 10 tasks of RLBench simulator. | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Baseline/ablation | The objects are synthetic 3D models without colors. | fair input/data/compute/action matching | p. 5 (4.1. Zero-shot Object Recognition), p. 5 (4.1. Zero-shot Object Recognition), p. 5 (4.1. Zero-shot Object Recognition) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** This work presents SUGAR, a novel 3D pre-training framework for robotics.
- **p. 8 / 5. Conclusion - extractive body cue:** It employs a versatile transformer-based architecture that jointly supports five pre-training tasks to learn semantic, geometric and affordances properties of objects in cluttered scenes.
- **p. 8 / 5. Conclusion - extractive body cue:** Experimental results demonstrate the excellent performance when using SUGAR for three robotic-related tasks, namely, zero-shot 3D object recognition, referring expression grounding, and language-driven robotic manipulation.

## Why Read It

Robotics-enabling 3D perception의 vla 문제를 이해하기 위해 읽는다. 본문은 Pretraining in existing work, however, is typically limited to single objects and complete point clouds, hence, ignoring This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.를 문제로 두고, In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation learning on cluttered scenes. • We pre-train ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (1) OBJ ONLY which only includes ground truth segmented), p. 6 (1) OBJ ONLY which only includes ground truth segmented) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Pretraining in existing work, however, is typically limited to single objects and complete point clouds, hence, ignoring This CVPR paper is the Open Access version, provided by the Computer Vision ... (p. 1, 1. Introduction).
- **Actual contribution:** In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation learning on cluttered scenes. • ... (p. 2, 1. Introduction).
- **Evaluation boundary:** Table 1. Zero-shot object recognition performance on three benchmarks. The Top1 accuracy is reported if not specified otherwise. The blue colored results in brackets on the ScanObjectNN dataset are obtained ... (p. 6, Figure/Table caption).
- **Explicit failure boundary:** While these 2D representations have demonstrated promising performance, they still fall short in addressing occlusions in complex cluttered scenes [79] and accurately predicting robotic actions [7] in the 3D world. (p. 1, 1. Introduction).
