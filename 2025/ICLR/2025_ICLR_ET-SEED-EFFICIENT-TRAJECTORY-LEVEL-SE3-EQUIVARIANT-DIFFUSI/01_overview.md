# ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/969a11f489c59c50c2cfe8c407c68a9b-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114743. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Chenrui Tie, Yue Chen, Ruihai Wu, Boxuan Dong, Zeyi Li, Chongkai Gao, Hao Dong
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Diffusion, equivariant
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/969a11f489c59c50c2cfe8c407c68a9b-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/969a11f489c59c50c2cfe8c407c68a9b-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 7. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

ET-SEED는 물체와 장면에 같은 강체 변환을 가했을 때 로봇 행동 궤적도 그에 따라 변하도록 설계한 확산 모방 정책이다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/969a11f489c59c50c2cfe8c407c68a9b-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Imitation learning, e.g., diffusion policy, has been proven effective in various robotic manipulation tasks.
- **p. 1 / ABSTRACT - extractive body cue:** However, extensive demonstrations are required for policy robustness and generalization.
- **p. 1 / ABSTRACT - extractive body cue:** To reduce the demonstration reliance, we leverage spatial symmetry and propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion model for generating action sequences in complex ...
- **p. 1 / ABSTRACT - extractive body cue:** Further, previous equivariant diffusion models require the per-step equivariance in the Markov process, making it difficult to learn policy under such strong constraints.
- **p. 1 / ABSTRACT - extractive body cue:** We theoretically extend equivariant Markov kernels and simplify the condition of equivariant diffusion process, thereby significantly improving training efficiency for trajectory-level SE(3) equivariant diffusion policy.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, previous trajectory-level diffusion models for robotic manipulation have two key limitations.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** ET-SEED improves the sample efficiency and decreases the training difficulty by restricting the equivariant operations during the diffusion denoising process.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are mainly as followed: • We propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion policy defined on SE(3) manifold, which achieves ...
- **p. 7 / 4 METHOD - extractive body cue:** Formally, we have ˆAk→0 = sθ(O, Ak; k) (8) To ensure the overall SE(3) equivariance of our pipeline, we propose a novel design of denoising ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Further, in real-world experiments, with only 20 demonstration trajectories, our method is able to generalize to unseen scenarios.
- **p. 4 / 4 METHOD - extractive body cue:** In this paper, we propose ET-SEED, a trajectorylevel end-to-end SE(3) equivariant diffusion model for robotic manipulation.
- **p. 5 / 4 METHOD - extractive body cue:** This key design choice significantly reduces the training complexity, thereby enhancing the overall performance of our method.
- **p. 7 / 4 METHOD - extractive body cue:** In each denoising step, the input of our denoising network sθ consists of observation O, noisy action sequence Ak, and scalar condition k, outputs the ...
- **p. 4 / 4 METHOD - extractive body cue:** 2 is a general example to show how it works, given an observation and a noisy action sequence, our model first implement K -1 invariant ...
- **PDF p. 7, §4 / Eq. (9) (DOC-QA2 원문 대조):** Denoising network는 k>1에서 SE(3)-invariant backbone E_inv, 마지막 k=1에서 SE(3)-equivariant backbone E_equiv를 사용한다. 이는 diffusion iteration별 backbone 선택이다.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | ET-SEED can theoretically guarantee the output actions are equivariant to any SE(3) transformation applied on the input observation, while only involving one equivariant denoising step. | image/video, language instruction, proprioception과 history | p. 4 (4 METHOD), p. 7 (4 METHOD) |
| State/latent | ET-SEED, theoretically, guarantee, output, actions, equivariant, transformation, applied, input, observation, while, only | language-grounded task state와 action-policy context | p. 4 (4 METHOD), p. 7 (4 METHOD), p. 7 (4 METHOD) |
| Output/action | When the input observation O is transformed by any SE(3) element T, the output denoised action sequence A0 will be equivariantly transformed. | continuous action, pose 또는 action chunk | p. 7 (4 METHOD), p. 7 (4 METHOD), p. 4 (4 METHOD) |
| Objective/outcome | In practice, we observe that training neural networks to approximate the properties of p2 and p3 is much more challenging compared to p1, both in terms of performance and training cost. | instruction following, task success, generalization과 latency | p. 5 (4 METHOD), p. 7 (4 METHOD), p. 7 (4 METHOD) |

## Main Claims and Actual Contribution

- 마르코프 전이의 대칭 조건을 분석해 모든 잡음 제거 단계에 같은 등변성 제약을 부과하지 않아도 궤적 분포의 등변성을 얻는 구조를 도출했다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/969a11f489c59c50c2cfe8c407c68a9b-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/969a11f489c59c50c2cfe8c407c68a9b-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/969a11f489c59c50c2cfe8c407c68a9b-Paper-Conference.pdf#page=6)
- 강체·관절 물체·변형 물체 조작에서 시연 수와 초기 배치 변화에 따른 성공률을 비교하고 실물에서 생성 궤적을 시험했다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/969a11f489c59c50c2cfe8c407c68a9b-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/969a11f489c59c50c2cfe8c407c68a9b-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/969a11f489c59c50c2cfe8c407c68a9b-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Embodiment/environment | (3) Is our method applicable to real-world robotic manipulation tasks? | hardware/simulator version and reset protocol | p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Dataset/benchmark | We design six representative robot manipulation tasks: Open Bottle Cap, Open Door, Rotate Triangle, Calligraphy, Cloth Folding, and Cloth Fling. | role, split, size and leakage | p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (0.6 Results) |
| Metric | Table 1: Success rates (↑) and standard deviation of different tasks in simulation. Open Bottle Cap Open Door Rotate Triangle T NP T NP | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Baseline/ablation | DP3 and DP3+Aug are used to compare ET-SEED with baseline methods that utilize data augmentation to achieve spatial generalization, while EquiBot allows for a comparison between different architectures of equivariant diffusion process. | fair input/data/compute/action matching | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6 CONCLUSION - extractive body cue:** However, the proposed method has certain limitations.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Overview of our pipeline. A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant denoising ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** The standard deviation of the Gaussian noise is set to 10% of the workspace size.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In this variant, we use a standard PointNet++ to predict noise at each step. • Ours w/o Eqv-Diff: Our method without the SE(3) equivariant denoising ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 7 (4 METHOD), p. 4 (4 METHOD)이다.
