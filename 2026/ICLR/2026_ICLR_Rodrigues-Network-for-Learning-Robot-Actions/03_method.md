# Method - Rodrigues Network for Learning Robot Actions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/eb9b18ccb76a1156af5779ffdca1d91f-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2506.02618. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 3 (1 INTRODUCTION), p. 6 (3.1 BACKGROUND), p. 2 (1 INTRODUCTION), p. 6 (3.1 BACKGROUND), p. 1 (ABSTRACT), p. 1 (ABSTRACT)): Other methods apply Cartesian-space loss functions after computing forward kinematics on network outputs (Pavllo et al., 2020; Jiang et al., 2021; Liu et al., 2020), but these approaches do not ...

## Method Body Digest

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Other methods apply Cartesian-space loss functions after computing forward kinematics on network outputs (Pavllo et al., 2020; Jiang et al., 2021; Liu et al., 2020), ...
- **p. 6 / 3.1 BACKGROUND - extractive body cue:** Refer to Section B of the supplementary for details on computing the first-layer features and task-specific outputs.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We then convert it into a neural operator by treating the state-dependent parameters as input features, and relaxing the state-independent coefficients into optimizable weights.
- **p. 6 / 3.1 BACKGROUND - extractive body cue:** These tokens then interact through multi-head self-attention, allowing the model to aggregate information from all links regardless of their spatial distance.
- **p. 1 / ABSTRACT - extractive body cue:** Building on this operator, we design the Rodrigues Network (RodriNet), a novel neural architecture specialized for processing actions.
- **p. 1 / ABSTRACT - extractive body cue:** Our results suggest that integrating structured kinematic priors into the network architecture improves action learning in various domains.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This motivates us to design a neural network that leverages this structure as an inductive bias for better understanding and inference of actions.
- **p. 3 / 3.1 BACKGROUND - extractive body cue:** Therefore, we can abbreviate Equation 2 as Pcj = Ppj(Tj ˜R(ˆωj, θj)), where ˜R(ˆωj, θj) ∈R4×4 is the homogeneous matrix of the rotation.

## Design Rationale

- **p. 1 / ABSTRACT - extractive body cue:** To this end, we propose the Neural Rodrigues Operator, a learnable generalization of the classical forward kinematics operation, designed to inject kinematics-aware inductive bias into ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, our method derive a learnable operator from forward kinematics, thereby making the network kinematics-aware while maintaining the flexibility to learn high-level features.
- **p. 5 / 3.1 BACKGROUND - extractive body cue:** To achieve that, we propose a basic building block called Rodrigues Block (Figure 2), which comprises the following three components: (1) a Rodrigues Layer for ...

## Source Evidence Cues

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Other methods apply Cartesian-space loss functions after computing forward kinematics on network outputs (Pavllo et al., 2020; Jiang et al., 2021; Liu et al., 2020), ...
- **p. 6 / 3.1 BACKGROUND - extractive body cue:** Refer to Section B of the supplementary for details on computing the first-layer features and task-specific outputs.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We then convert it into a neural operator by treating the state-dependent parameters as input features, and relaxing the state-independent coefficients into optimizable weights.
- **p. 6 / 3.1 BACKGROUND - extractive body cue:** These tokens then interact through multi-head self-attention, allowing the model to aggregate information from all links regardless of their spatial distance.
- **p. 1 / ABSTRACT - extractive body cue:** Building on this operator, we design the Rodrigues Network (RodriNet), a novel neural architecture specialized for processing actions.
- **p. 1 / ABSTRACT - extractive body cue:** Our results suggest that integrating structured kinematic priors into the network architecture improves action learning in various domains.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This motivates us to design a neural network that leverages this structure as an inductive bias for better understanding and inference of actions.
- **Detected method headings:** B ADDITIONAL DETAILS ON NETWORK ARCHITECTURE (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | Other methods apply Cartesian-space loss functions after computing forward kinematics on network outputs (Pavllo et al., 2020; Jiang et al., 2021; Liu ... | p. 3 (1 INTRODUCTION), p. 6 (3.1 BACKGROUND) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | Refer to Section B of the supplementary for details on computing the first-layer features and task-specific outputs. | p. 6 (3.1 BACKGROUND), p. 2 (1 INTRODUCTION) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | We then convert it into a neural operator by treating the state-dependent parameters as input features, and relaxing the state-independent coefficients into ... | p. 2 (1 INTRODUCTION), p. 6 (3.1 BACKGROUND) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1 BACKGROUND - extractive body cue:** Therefore, we can abbreviate Equation 2 as Pcj = Ppj(Tj ˜R(ˆωj, θj)), where ˜R(ˆωj, θj) ∈R4×4 is the homogeneous matrix of the rotation.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Other methods apply Cartesian-space loss functions after computing forward kinematics on network outputs (Pavllo et al., 2020; Jiang et al., 2021; Liu et al., 2020), ...
- **p. 4 / 3.1 BACKGROUND - extractive body cue:** This operator generalizes the classical transformation in Equation 2.
- **원문 대조:** Multi-channel neural Rodrigues operator를 F_out=Rodrigues(F_in,W*,Θ)로 줄여 쓴다. W*는 좌·우 곱에 쓰는 학습 가능한 bias/sine/cosine coefficient이며 Θ는 joint feature다. ([PDF p. 4](https://arxiv.org/pdf/2506.02618#page=4), §3.3 Multi-Channel Neural Rodrigues Operator, Eq. (8)).
- **원문 대조:** 각 joint에서 parent-link feature, joint별 Rodrigues kernel, joint feature로 transformed feature를 계산한다. 이를 child-link의 입력 feature에 더하고 LayerNorm을 적용해 link feature를 갱신한다. ([PDF p. 5](https://arxiv.org/pdf/2506.02618#page=5), §4.1 Rodrigues Layer, Eqs. (9)–(10)).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We then convert it into a neural operator by treating the state-dependent parameters as input features, and relaxing the state-independent coefficients into optimizable weights.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 3 (3.1 BACKGROUND), p. 3 (1 INTRODUCTION), p. 4 (3.1 BACKGROUND), p. 4 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | then, convert, neural, operator, treating, state-dependent, parameters, input, features, relaxing, state-independent, coefficients, optimizable, weights | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | then, convert, neural, operator, treating, state-dependent, parameters, input, features, relaxing | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | Neural, Rodrigues, Operator, learnable, generalization, classical, forward, kinematics, operation, designed | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Therefore, abbreviate, Equation, Pcj, Ppj, where, homogeneous, matrix, rotation, Other | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We then convert it into a neural operator by treating the state-dependent parameters as input features, and relaxing the state-independent coefficients into optimizable weights.
- **p. 4 / 3.1 BACKGROUND - extractive body cue:** Based on this, we construct our Neural Rodrigues Operator for one single joint by replacing these fixed coefficients with learnable weights W bias, W cos, ...
- **p. 5 / 3.1 BACKGROUND - extractive body cue:** The Joint Layer computes its output joint features {Θout j } from its own input joint features {Θin j } and link features {F in ...
- **원문 대조:** 각 joint에서 parent-link feature, joint별 Rodrigues kernel, joint feature로 transformed feature를 계산한다. 이를 child-link의 입력 feature에 더하고 LayerNorm을 적용해 link feature를 갱신한다. ([PDF p. 5](https://arxiv.org/pdf/2506.02618#page=5), §4.1 Rodrigues Layer, Eqs. (9)–(10)).
- **p. 6 / 3.1 BACKGROUND - extractive body cue:** It sequentially applies the Rodrigues Layer, Joint Layer, and Self-attention Layer to produce updated link features, joint features, and a global token, where each layer's ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Their actions, including poses, motions, or control commands, are usually represented as values associated with all joints.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additionally, we show our network achieving state-of-the-art results in human hand pose estimation from images, where the articulated actor is no longer a robot, highlighting ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Methods We adopt Diffusion Policy (Chi et al., 2023) as our learning framework, using a 2-frame observation history and predicting 16 future ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Our method replaces these with the Rodrigues Network, which takes the current observation, denoising timestep, and a noisy action as inputs and ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | Methods We adopt Diffusion Policy (Chi et al., 2023) as our learning framework, using a 2-frame observation history and predicting 16 future ... | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | The network is given the first 8 frames of joint angles and tasked with predicting the remaining 8, also in joint space. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 INTRODUCTION - extractive body cue:** This motivates us to design a neural network that leverages this structure as an inductive bias for better understanding and inference of actions.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** For model hyperparameters and training settings, please refer to Sections C.1 and D.1 of the supplementary material.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Refer to Sections C.2 and D.2 of the supplementary for details on training, model parameter count control, and runtime comparisons.

## Method-Specific Formal Details

- **Body-defined terms:** Other, methods, apply, Cartesian-space, loss, functions, after, computing, forward, kinematics, network, outputs, Pavllo, Jiang, Liu, approaches, alter, architecture, thus, orthogonal.
- **Relevant PDF headings:** B ADDITIONAL DETAILS ON NETWORK ARCHITECTURE (p. 15).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | In real-world robot learning scenarios, neural backbones typically process observations in 3D Cartesian space (e.g., point clouds) and output control commands as ... | p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Policy fitting | Compared to the strongest baseline, HaMeR, our approach outperforms both the results reported in the original paper and our reproduced implementation. | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Closed-loop rollout | Our network achieves a notable performance improvement while significantly reducing the number of parameters (39.5M vs. ours: 10.7M). | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Additional studies on ablations and hyperparameter sensitivity are provided in the supplementary material.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Notably, its test MSE is lower than the train MSE of all baseline models, indicating that the Rodrigues Network not only fits the data more ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 11: Ablation studies for motion prediction in Cartesian space with trainset size = 105. We remove the Rodrigues Layer (R Layer), Joint Layer (J ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** These synthetic tasks provide a clean environment to directly evaluate network expressivity without other factors.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** To isolate the impact of the neural backbone, we keep the outer framework and all other components fixed, modifying only the denoising network.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Our method replaces these with the Rodrigues Network, which takes the current observation, denoising timestep, and a noisy action as inputs and predicts the corresponding ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** With this neural operator as a key component, we build the Rodrigues Network with additional layer designs, resulting in a powerful and embodiment-aware network architecture ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (1 INTRODUCTION), p. 6 (3.1 BACKGROUND), p. 2 (1 INTRODUCTION), p. 6 (3.1 BACKGROUND), p. 1 (ABSTRACT), p. 1 (ABSTRACT), objective p. 3 (3.1 BACKGROUND), p. 3 (1 INTRODUCTION), p. 4 (3.1 BACKGROUND), p. 4 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND), p. 2 (1 INTRODUCTION), temporal p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
