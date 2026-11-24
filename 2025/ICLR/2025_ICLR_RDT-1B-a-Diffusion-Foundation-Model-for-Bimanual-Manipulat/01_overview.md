# RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html.
> PDF retrieval source: https://openreview.net/pdf/29d56379d000b8c0e05906c5958e67e2e870ab0c.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Songming Liu, Lingxuan Wu, Bangguo Li, Hengkai Tan, Huayu Chen, Zhengyi Wang, Ke Xu, Hang Su, Jun Zhu
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Diffusion
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html
- Full-text retrieval: https://arxiv.org/pdf/2410.07864
- Code/Project: https://rdt-robotics.github.io/rdt-robotics/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RDT는 여러 로봇의 데이터를 사전학습한 확산 트랜스포머를 양팔 조작에 미세조정한다. [PDF 1쪽](https://arxiv.org/pdf/2410.07864#page=1)

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

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It exhibits zeroshot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1∼5 demonstrations, and effectively handles complex, dexterous tasks. | image/video, language instruction, proprioception과 history | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| State/latent | exhibits, zeroshot, generalization, unseen, objects, scenes, understands, follows, language, instructions, learns, skills | language-grounded task state와 action-policy context | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/action | To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper arms. | continuous action, pose 또는 action chunk | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | The prohibitive costs of dual-arm systems create severe data scarcity (Sharma et al., 2018; Collaboration et al., 2023), fundamentally conflicting with the datahungry nature of foundation models. | instruction following, task success, generalization과 latency | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- 관절·말단장치 등 제어량의 물리적 의미를 보존하는 공통 행동 공간을 정의해 기구가 다른 로봇의 기록을 학습에 사용한다. [PDF 4쪽](https://arxiv.org/pdf/2410.07864#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2410.07864#page=5)
- 양팔 시연으로 미세조정한 뒤 실제 로봇에서 지시 수행과 새로운 물체·장면으로의 일반화를 평가했다. [PDF 7쪽](https://arxiv.org/pdf/2410.07864#page=7) · [PDF 9쪽](https://arxiv.org/pdf/2410.07864#page=9)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations. (p. 1, 1 INTRODUCTION).
- **Actual contribution:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability. (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** 5.2 RESULTS ANALYSIS From the results in Table 3, we can see that RDT consistently outperforms other baselines. (p. 9, 5 EXPERIMENTS).
- **Explicit failure boundary:** It probably makes ACT prone to failure. (p. 10, 5 EXPERIMENTS).

## 공개 자료 대조

- **코드** · RDT 행동 확산 Transformer 정의와 학습·추론 코드. [배포 파일](https://raw.githubusercontent.com/thu-ml/RoboticsDiffusionTransformer/cd79363a1387e8f81c7724d070ef7e45fd23150f/models/rdt/model.py) · [저자 배포 안내](https://raw.githubusercontent.com/thu-ml/RoboticsDiffusionTransformer/cd79363a1387e8f81c7724d070ef7e45fd23150f/README.md)
- **가중치** · RDT-1B 사전학습 모델의 파라미터 파일. [배포 파일](https://huggingface.co/robotics-diffusion-transformer/rdt-1b/blob/eb09036cc64ca4945051acbd1bd581d30a1d7711/pytorch_model.bin) · [저자 배포 안내](https://raw.githubusercontent.com/thu-ml/RoboticsDiffusionTransformer/cd79363a1387e8f81c7724d070ef7e45fd23150f/README.md)
- **데이터** · 저자의 양팔 미세조정 시연 배포본 중 첫 분할 아카이브. 다기종 사전학습 전체 자료의 배포와 구별한다. [배포 파일](https://huggingface.co/datasets/robotics-diffusion-transformer/rdt-ft-data/blob/a3f4b6624d4fc3a09b538f65081b37401fd8bd84/rdt_data.tar.gz.00) · [저자 배포 안내](https://raw.githubusercontent.com/thu-ml/RoboticsDiffusionTransformer/cd79363a1387e8f81c7724d070ef7e45fd23150f/README.md)
