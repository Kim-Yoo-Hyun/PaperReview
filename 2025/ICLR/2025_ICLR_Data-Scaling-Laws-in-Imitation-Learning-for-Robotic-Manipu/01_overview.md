# Data Scaling Laws in Imitation Learning for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=pISLZG7ktL.
> PDF retrieval source: https://arxiv.org/pdf/2410.18647. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning, scaling laws, data collection
- Official paper: https://openreview.net/forum?id=pISLZG7ktL
- Full-text retrieval: https://arxiv.org/pdf/2410.18647
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 il 문제를 이해하기 위해 읽는다. 본문은 (2023), most of today's robotic policies still lack comparable zero-shot generalization (Xie et al., 2024).를 문제로 두고, To answer this, we present a comprehensive empirical study on data scaling in imitation learning, which is a predominant method for learning real-world manipulation skills (Shafiullah et al., 2024).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Data scaling has revolutionized fields like natural language processing and computer vision, providing models with remarkable generalization capabilities.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we investigate whether similar data scaling laws exist in robotics, particularly in robotic manipulation, and whether appropriate data scaling can yield single-task ...
- **p. 1 / ABSTRACT - extractive body cue:** To this end, we conduct a comprehensive empirical study on data scaling in imitation learning.
- **p. 1 / ABSTRACT - extractive body cue:** By collecting data across numerous environments and objects, we study how a policy's generalization performance changes with the number of training environments, objects, and demonstrations.
- **p. 1 / ABSTRACT - extractive body cue:** Throughout our research, we collect over 40,000 demonstrations and execute more than 15,000 real-world robot rollouts under a rigorous evaluation protocol.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** (2023), most of today's robotic policies still lack comparable zero-shot generalization (Xie et al., 2024).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While data scaling has endowed models in NLP and CV with exceptional generalization capabilities Achiam et al.

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To answer this, we present a comprehensive empirical study on data scaling in imitation learning, which is a predominant method for learning real-world manipulation skills ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, based on these data scaling laws, we propose an efficient data collection strategy to achieve the desired level of generalization (Sec.
- **p. 4 / 3 APPROACH - extractive body cue:** It enables highly efficient data collection and allows for seamless switching between different in-the-wild environments with minimal setup time.
- **p. 3 / 3 APPROACH - extractive body cue:** Finally, we introduce our rigorous evaluation protocol.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our extensive investigation reveals surprising results and contributions: • Simple power laws.
- **p. 5 / 3 APPROACH - extractive body cue:** There are several key observations: (1) As the number of training objects increases, the policy's performance on unseen objects consistently improves across all fractions of ...
- **p. 4 / 3 APPROACH - extractive body cue:** (2) Temporal ensemble: Diffusion Policy predicts a sequence of actions every T1 steps, with each sequence having a length of T2 (T2 > T1), and ...
- **p. 5 / 3 APPROACH - extractive body cue:** To explore the effect of the number of training environments on generalization, we use the same manipulation object across 32 distinct environments, collecting 120 demonstrations ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | There are several key observations: (1) As the number of training objects increases, the policy's performance on unseen objects consistently improves across all fractions of demonstrations. | observation history와 expert trajectory/action | p. 5 (3 APPROACH), p. 4 (3 APPROACH) |
| State/latent | There, several, observations, number, training, objects, increases, policy, performance, unseen, consistently, improves | behavior policy와 temporal action context | p. 5 (3 APPROACH), p. 4 (3 APPROACH), p. 4 (3 APPROACH) |
| Output/action | Specifically, the policy predicts at each timestep, resulting in overlapping action sequences. | predicted action 또는 action chunk | p. 4 (3 APPROACH), p. 4 (3 APPROACH), p. 5 (3 APPROACH) |
| Objective/outcome | UMI's portability, intuitive design, and low cost make it an ideal tool for our data collection needs. | imitation error, task success, robustness와 compounding error | p. 4 (3 APPROACH), p. 5 (3 APPROACH), p. 7 (3 APPROACH) |

## Main Claims and Actual Contribution

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To answer this, we present a comprehensive empirical study on data scaling in imitation learning, which is a predominant method for learning real-world manipulation skills ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, based on these data scaling laws, we propose an efficient data collection strategy to achieve the desired level of generalization (Sec.
- **p. 4 / 3 APPROACH - extractive body cue:** It enables highly efficient data collection and allows for seamless switching between different in-the-wild environments with minimal setup time.
- **p. 3 / 3 APPROACH - extractive body cue:** Finally, we introduce our rigorous evaluation protocol.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our extensive investigation reveals surprising results and contributions: • Simple power laws.
- **p. 4 / 3 APPROACH - extractive body cue:** To further enhance performance, we make two improvements: (1) DINOv2 visual encoder: In our experiments, fine-tuning the DINOv2 ViT (Oquab et al., 2023) outperforms both ...
- **p. 1 / ABSTRACT - extractive body cue:** With four data collectors working for one afternoon, we collect sufficient data to enable the policies for two tasks to achieve approximately 90% success rates ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We apply this strategy to two new tasks (Fold Towels and Unplug Charger), and within a single afternoon using four data collectors, we collect sufficient ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (3 APPROACH), p. 1 (ABSTRACT) |
| Embodiment/environment | Existing robotic manipulation datasets do not provide enough environments and objects for a single task to meet our requirements. | hardware/simulator version and reset protocol | p. 4 (3 APPROACH), p. 4 (3 APPROACH) |
| Dataset/benchmark | Throughout our research, we collect over 40,000 demonstrations and execute more than 15,000 real-world robot rollouts under a rigorous evaluation protocol. | role, split, size and leakage | p. 4 (3 APPROACH), p. 4 (3 APPROACH), p. 1 (ABSTRACT), p. 5 (3 APPROACH) |
| Metric | The results, shown in Table 1, report both the policy's normalized score and the corresponding success rate (for the definition of success criteria, see Appendix D). | definition, denominator, direction and uncertainty | p. 9 (32 Env-Object Pairs), p. 9 (32 Env-Object Pairs), p. 30 (Figure/Table caption) |
| Baseline/ablation | To further enhance performance, we make two improvements: (1) DINOv2 visual encoder: In our experiments, fine-tuning the DINOv2 ViT (Oquab et al., 2023) outperforms both ImageNet pre-trained ResNet (He et al., 2016; ... | fair input/data/compute/action matching | p. 4 (3 APPROACH), p. 6 (3 APPROACH), p. 6 (3 APPROACH) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 32 Env-Object Pairs - extractive body cue:** 7 DISCUSSION, LIMITATIONS, & FUTURE WORKS Data scaling is an exciting and ongoing event in robotics.
- **p. 3 / 3 APPROACH - extractive body cue:** While this approach allows precise control over individual factors, it cannot account for all possible variation factors.
- **p. 10 / 32 Env-Object Pairs - extractive body cue:** Our work has several limitations that future research can address.
- **p. 4 / 3 APPROACH - extractive body cue:** To ensure model capacity does not become a bottleneck when scaling data, we utilize a sufficiently large model, ViT-Large/14 (Dosovitskiy et al., 2020).
- **p. 7 / 3 APPROACH - extractive body cue:** Based on all the results, we summarize the following data scaling laws: 1Although we recognize the irreducible errors Y∞associated with scaling the data alone, fitting ...
- **p. 8 / 3 APPROACH - extractive body cue:** We leave the verification of this prediction for future work.
- **p. 8 / 3 APPROACH - extractive body cue:** For large-scale data collection, where the number of environments typically exceeds 16, adding multiple objects within the same environment does not further enhance policy performance, ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 il 문제를 이해하기 위해 읽는다. 본문은 (2023), most of today's robotic policies still lack comparable zero-shot generalization (Xie et al., 2024).를 문제로 두고, To answer this, we present a comprehensive empirical study on data scaling in imitation learning, which is a predominant method for learning real-world manipulation skills (Shafiullah et al., 2024).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 APPROACH), p. 4 (3 APPROACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
