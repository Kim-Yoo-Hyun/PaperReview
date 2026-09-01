# RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=yAzN4tz7oI.
> PDF retrieval source: https://openreview.net/pdf/29d56379d000b8c0e05906c5958e67e2e870ab0c.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Diffusion
- Official paper: https://openreview.net/forum?id=yAzN4tz7oI
- Full-text retrieval: https://openreview.net/pdf/29d56379d000b8c0e05906c5958e67e2e870ab0c.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.를 문제로 두고, In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** RDT builds on diffusion models to effectively represent multi-modality, with innovative designs of a scalable Transformer to deal with the heterogeneity of multi-modal inputs and ...
- **p. 1 / ABSTRACT - extractive body cue:** To address data scarcity, we further introduce a Physically Interpretable Unified Action Space, which can unify the action representations of various robots while preserving the ...
- **p. 1 / ABSTRACT - extractive body cue:** With these designs, we managed to pre-train RDT on the largest collection of multi-robot datasets to date and scaled it up to 1.2B parameters, which ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, current approaches either depend on task-specific primitives (Mirrazavi Salehian et al., 2017; Rakita et al., 2019; Grannen et al., 2023a) or are limited to ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Following the success in natural language processing (Achiam et al., 2023; Touvron et al., 2023) and computer vision (Radford et al., 2021; Kirillov et al., ...
- **p. 1 / ABSTRACT - extractive body cue:** Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** First, the doubled action space induces multi-modal action distributions (Li, 2006; Jia et al., 2024) (see Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Compared with unimanual manipulation, bimanual manipulation has more possible action modes, leading to stronger multi-modality.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Published as a conference paper at ICLR 2025 Right-Wrist Camera Left-Wrist Camera Exterior Camera Right Gripper Left Gripper (a) Target dual-arm robot target right gripper ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It exhibits zeroshot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1∼5 demonstrations, and effectively handles complex, dexterous tasks. | image/video, language instruction, proprioception과 history | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| State/latent | exhibits, zeroshot, generalization, unseen, objects, scenes, understands, follows, language, instructions, learns, skills | language-grounded task state와 action-policy context | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/action | To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper arms. | continuous action, pose 또는 action chunk | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | The prohibitive costs of dual-arm systems create severe data scarcity (Sharma et al., 2018; Collaboration et al., 2023), fundamentally conflicting with the datahungry nature of foundation models. | instruction following, task success, generalization과 latency | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Following the success in natural language processing (Achiam et al., 2023; Touvron et al., 2023) and computer vision (Radford et al., 2021; Kirillov et al., ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different from ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3: Quantitative results. We report success rates (%) of ACT, OpenVLA, RDT (from scratch, no pre-trained), and RDT (ours, pre-trained) for 7 tasks. Sub-columns ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Besides, the large number of parameters after large-scale pre-training provides a lot of prior knowledge, which significantly improves the generalizability.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In Handover and Fold Shorts, RDT has learned new and complex skills of handover and folding through few-shot learning, whose action patterns are very different ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 10 (Figure/Table caption) |
| Embodiment/environment | We aim to answer the following questions through real-robot experiments: Q1: Can RDT zero-shot generalize to unseen objects and scenes? | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Dataset/benchmark | We select 7 challenging tasks to evaluate the generalizability and capabilities of RDT from different dimensions, including complex scenarios that the model may encounter in real-world tasks, such as various unseen elements ... | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Metric | In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different from that on seen ones. | definition, denominator, direction and uncertainty | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Baseline/ablation | 5.2 RESULTS ANALYSIS From the results in Table 3, we can see that RDT consistently outperforms other baselines. | fair input/data/compute/action matching | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 EXPERIMENTS - extractive body cue:** It probably makes ACT prone to failure.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Unstable loss curve during training without QKNorm & RMSNorm. (b) Success rates of RDT (w/o MLP Decoder or w/o ACI) in tasks ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The robot needs to Pick Up Pen (#1), Switch Hand (#2), Drop Pen (#3), and ensure it can Fall into Box (#4).
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The robot needs to Pick Up Cup (#1), Turn On Faucet (#2), Get Water (#3, to ensure that the water falls into the cup), Pour ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In contrast, the other baselines cannot even complete the entire task.
- **p. 10 / 6 CONCLUSION - extractive body cue:** We further introduce a Physically Interpretable Unified Action Space to unify action representations across different robots, enhancing robustness and transferability.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: RDT framework. Heterogeneous action spaces of various robots are embedded into a unified action space for multi-robot training. Inputs: proprioception zt, noisy action ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.를 문제로 두고, In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
