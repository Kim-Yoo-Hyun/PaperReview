# EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/0dadf17389895a1d660a178d1140e07c-Abstract-Conference.html.
> PDF retrieval source: https://openreview.net/pdf/7d1ac63392c225113c314e6263f1d18dfbff895e.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Xupeng Zhu, Yu Qi, Yizhe Zhu, Robin Walters, Robert Platt
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, 3D Vision, equivariant
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/0dadf17389895a1d660a178d1140e07c-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/0dadf17389895a1d660a178d1140e07c-Paper-Conference.pdf
- Code/Project: https://github.com/ZXP-S-works/EquAct
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

EquAct는 장면의 회전·이동에 맞춰 조작 자세 예측도 변하도록 언어 조건부 3차원 정책을 설계했다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0dadf17389895a1d660a178d1140e07c-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Transformer architectures can effectively learn language-conditioned, multi-task 3D open-loop manipulation policies from demonstrations by jointly processing natural language instructions and 3D observations.
- **p. 1 / Abstract - extractive body cue:** However, although both the robot policy and language instructions inherently encode rich 3D geometric structures, standard transformers lack built-in guarantees of geometric consistency, often resulting ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we leverage SE(3) equivariance as a key structural property shared by both policy and language, and propose EquAct-a novel SE(3)-equivariant multi-task transformer.
- **p. 1 / Abstract - extractive body cue:** EquAct is theoretically guaranteed to be SE(3) equivariant and consists of two key components: (1) an efficient SE(3)-equivariant point cloud-based U-net with spherical Fourier features ...
- **p. 1 / Abstract - extractive body cue:** To evaluate its spatial generalization ability, we benchmark EquAct on 18 RLBench simulation tasks with both SE(3) and SE(2) scene perturbations, and on 4 physical ...
- **p. 2 / 1 Introduction - extractive body cue:** To fill in this gap, EquAct proposes 18 RLBench with SE(3) initialization to mimic physical world settings.
- **p. 2 / 1 Introduction - extractive body cue:** Nevertheless, EquAct is limited to keyframe actions that cannot solve fine-grained closed-loop tasks and do not leverage pre-trained vision models.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose a continuous SE(3)-equivariant keyframe policy that includes a novel equivariant U-net architecture, a novel invariant FiLM layer, and a novel equivariant field network.
- **p. 6 / 4 Method - extractive body cue:** To extend this operation to the spherical Fourier domain, we propose a novel spherical Fourier upsampling method (Figure 3 (b) right).
- **p. 2 / 1 Introduction - extractive body cue:** While achieving state-of-the-art performance on 18 RLBench SE(2) and SE(3) benchmarks, our method leverages a spherical Fourier representation to achieve computational efficiency during both training ...
- **p. 6 / 4 Method - extractive body cue:** 4.3 Invariant Feature-wise Linear Modulation Layers (iFiLM) We propose invariant Feature-wise Linear Modulation (iFiLM) layers (Figure 3 (b) left) to enforce the geometric invariance of ...
- **p. 3 / 2 Background - extractive body cue:** The first class consists of multi-viewbased methods [14, 15, 66, 73, 8], where the 3D scene is projected into three orthogonal image planes.
- **p. 7 / 4 Method - extractive body cue:** For translational action value evaluation, given the query translational action at and the latent point cloud h, the field network qt builds a graph with ...
- **p. 7 / 4 Method - extractive body cue:** For rotational action value evaluation, given the query trans-rotal action at, ar and the latent point cloud h, the field network qr first aggregates features ...
- **p. 6 / 4 Method - extractive body cue:** Specifically, the iFiLM layer takes as input a spherical Fourier feature c and a type-0 (invariant) condition feature k, and outputs a semantically modulated feature ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | EquAct is a multi-task keyframe action policy that takes an observation o and a natural language instruction n as input and predicts the next best keyframe action of the gripper a, denoted ... | image/video, language instruction, proprioception과 history | p. 4 (4 Method), p. 2 (2 Background) |
| State/latent | EquAct, multi-task, keyframe, action, policy, takes, observation, natural, language, instruction, input, predicts | language-grounded task state와 action-policy context | p. 4 (4 Method), p. 2 (2 Background), p. 5 (4 Method) |
| Output/action | The keyframe action formulation [24, 26] defines an open-loop policy setting, where the policy predicts the next goal pose of the gripper based on the current observation. | continuous action, pose 또는 action chunk | p. 2 (2 Background), p. 5 (4 Method), p. 5 (4 Method) |
| Training objective | 원문 대조: 학습은 expert action을 후보 action 중 선택하는 classification으로 다루고 translation, rotation, gripper-open 예측에 cross-entropy를 사용한다. 식의 H는 cross-entropy이며 일반적인 RL return objective가 아니다. ([PDF p. 5](https://arxiv.org/pdf/2505.21351#page=5), §4 Method, training-loss equation) | Expert-action classification; RL return과 구분 | [PDF p. 5](https://arxiv.org/pdf/2505.21351#page=5), §4 Method, training-loss equation |

## Main Claims and Actual Contribution

- 구면 푸리에 특징을 쓰는 점군 U-Net과 변환에 불변인 언어 조건화 층 iFiLM을 결합한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0dadf17389895a1d660a178d1140e07c-Paper-Conference.pdf#page=4) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0dadf17389895a1d660a178d1140e07c-Paper-Conference.pdf#page=6)
- 변환한 RLBench 장면과 실물 조작에서 물체의 자세가 훈련 분포와 달라질 때의 일반화를 시험했다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0dadf17389895a1d660a178d1140e07c-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0dadf17389895a1d660a178d1140e07c-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5 Experiments), p. 9 (5 Experiments) |
| Embodiment/environment | In the 10 SE(3) setting, the training set contains 10 demo per task and both the training and testing scenes have randomly SE(3) initialized objects. | hardware/simulator version and reset protocol | p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Dataset/benchmark | 5.2 Physical experiments Table 2: Physical experiments. avg. disass. pluck pick install SR ↑ pipe flower fruit toilet roll Var × Demo 3 × 10 3 × 15 3 × 10 2 ... | role, split, size and leakage | p. 8 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments) |
| Metric | Performance is measured by a binary reward, where 0% and 100% correspond to failure and successful completion of the task according to the natural language instruction, respectively. | definition, denominator, direction and uncertainty | p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Baseline/ablation | In the end, EquAct outperforms SOTA baselines by 2.6% and 6.2% when trained with 100 or 10 demos in SE(2) setting, and by 15.4% when trained with 10 demos in SE(3) setting. | fair input/data/compute/action matching | p. 9 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5 Experiments - extractive body cue:** Performance is measured by a binary reward, where 0% and 100% correspond to failure and successful completion of the task according to the natural language ...
- **p. 9 / 5 Experiments - extractive body cue:** In comparison, 3DDA struggles in these experiments, often skipping keyframe actions and resulting in failure.
- **p. 9 / 5 Experiments - extractive body cue:** 6 Conclusion and limitations Conclusion.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (2 Background), p. 7 (4 Method)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Nevertheless, EquAct is limited to keyframe actions that cannot solve fine-grained closed-loop tasks and do not leverage pre-trained vision models. (p. 2, 1 Introduction).
- **Actual contribution:** We propose a continuous SE(3)-equivariant keyframe policy that includes a novel equivariant U-net architecture, a novel invariant FiLM layer, and a novel equivariant field network. (p. 2, 1 Introduction).
- **Evaluation boundary:** 5.2 Physical experiments Table 2: Physical experiments. avg. disass. pluck pick install SR ↑ pipe flower fruit toilet roll Var × Demo 3 × 10 3 × 15 3 × ... (p. 9, 5 Experiments).
- **Explicit failure boundary:** In comparison, 3DDA struggles in these experiments, often skipping keyframe actions and resulting in failure. (p. 9, 5 Experiments).

## 공개 자료 대조

- **코드** · EquAct의 등변 행동 모델 및 학습 코드. [배포 파일](https://raw.githubusercontent.com/ZXP-S-works/EquAct/b0a5433e09ef10aa8195812269664d62dcd7209a/diffuser_actor/equ_act_optimization/equ_act.py) · [저자 배포 안내](https://raw.githubusercontent.com/ZXP-S-works/EquAct/b0a5433e09ef10aa8195812269664d62dcd7209a/README.md)
