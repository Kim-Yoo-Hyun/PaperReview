# Method - FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.2. Cascaded Action Denoising), p. 7 (5.3. Efficiency Improvement), p. 3 (4.1. Value-Guided Test-Time Sampling), p. 3 (4. Methodology), p. 7 (5.3. Efficiency Improvement)): During training, we use the calibrated Q-learning [49] to optimize the intermediate flow verifier φ.

## Method Body Digest

- **p. 4 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** During training, we use the calibrated Q-learning [49] to optimize the intermediate flow verifier φ.
- **p. 4 / 4.2. Cascaded Action Denoising - extractive body cue:** For the k-th sub-action chunk Aτ ∗ t,k, it contains the noisy action from time step t + kh to t + (k + 1)h ...
- **p. 7 / 5.3. Efficiency Improvement - extractive body cue:** In other words, when FM-Steer enters an erroneous state, it can evaluate multiple candidate actions and select a better forward trajectory.
- **p. 3 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** First, we enforce varying noise levels across all N candidate flow points by adjusting the flow-matching integration endpoint.
- **p. 3 / 4. Methodology - extractive body cue:** 2, we take a flow-based VLA as the base model and augment it with two modules: an intermediate flow verifier φ and a Lite-Flow denoiser ...
- **p. 7 / 5.3. Efficiency Improvement - extractive body cue:** Optimal Noisy Candidate Sampled Noisy Candidates a) Value Map of Candidate Actions PCA1 PCA2 state-action values b) Cascaded Action Denoising Visualization Refined Action Figure 5.
- **p. 5 / 5.1. Implementation Details - extractive body cue:** During deployment, we use a single RTX 4090 GPU for inference.
- **p. 3 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** Due to the multiple Euler forward iterations required by flow-based VLA during inference, repeated action sampling leads to a significant increase in computational cost.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the main contributions of this work are: • We propose FM-Steer, a test-time computing framework that enhances flow-based Vision-Language-Action models while improving the ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this issue, we propose a cascaded action denoising mechanism that distributes the denoising computation across the original VLA and a separate Lite-Flow denoiser, ...
- **p. 3 / 3. Preliminaries - extractive body cue:** The model typically consists of a VLM backbone and a flow matching expert.

## Source Evidence Cues

- **p. 4 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** During training, we use the calibrated Q-learning [49] to optimize the intermediate flow verifier φ.
- **p. 4 / 4.2. Cascaded Action Denoising - extractive body cue:** For the k-th sub-action chunk Aτ ∗ t,k, it contains the noisy action from time step t + kh to t + (k + 1)h ...
- **p. 7 / 5.3. Efficiency Improvement - extractive body cue:** In other words, when FM-Steer enters an erroneous state, it can evaluate multiple candidate actions and select a better forward trajectory.
- **p. 3 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** First, we enforce varying noise levels across all N candidate flow points by adjusting the flow-matching integration endpoint.
- **p. 3 / 4. Methodology - extractive body cue:** 2, we take a flow-based VLA as the base model and augment it with two modules: an intermediate flow verifier φ and a Lite-Flow denoiser ...
- **p. 7 / 5.3. Efficiency Improvement - extractive body cue:** Optimal Noisy Candidate Sampled Noisy Candidates a) Value Map of Candidate Actions PCA1 PCA2 state-action values b) Cascaded Action Denoising Visualization Refined Action Figure 5.
- **p. 5 / 5.1. Implementation Details - extractive body cue:** During deployment, we use a single RTX 4090 GPU for inference.
- **Detected method headings:** 4. Methodology (p. 3); Model (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | During training, we use the calibrated Q-learning [49] to optimize the intermediate flow verifier φ. | p. 4 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.2. Cascaded Action Denoising) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | For the k-th sub-action chunk Aτ ∗ t,k, it contains the noisy action from time step t + kh to t + ... | p. 4 (4.2. Cascaded Action Denoising), p. 7 (5.3. Efficiency Improvement) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | In other words, when FM-Steer enters an erroneous state, it can evaluate multiple candidate actions and select a better forward trajectory. | p. 7 (5.3. Efficiency Improvement), p. 3 (4.1. Value-Guided Test-Time Sampling) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** Due to the multiple Euler forward iterations required by flow-based VLA during inference, repeated action sampling leads to a significant increase in computational cost.
- **p. 4 / 4.2. Cascaded Action Denoising - extractive body cue:** 4.1 partially denoises the noisy action to reduce computational cost of repeated sampling.
- **p. 4 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** As for the reward, we construct D using the sparse binary reward function following [32], where the rewards of the last 3 transitions in each ...
- **p. 5 / 4.3. Training and Deployment Strategy - extractive body cue:** The dataset for the intermediate flow verifier is constructed using the reward function described in Sec.
- **p. 7 / 5.3. Efficiency Improvement - extractive body cue:** 1, previous methods such as V-GPS and RoboMonkey do improve VLA performance to some extent, but they do so at a significant cost in control ...
- **원문 대조:** 후보 다양성을 위해 deterministic Euler integration에 stochasticity를 추가하고 각 forward step을 isotropic Gaussian으로 모델링한다. Σ_τ는 후보 다양성을 조절하는 hyperparameter이며 기존 cue는 이 sampling 단계의 설명이다. ([PDF p. 3](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf#page=3), §4.1 Value-Guided Test-Time Sampling).
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 3 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.1. Value-Guided Test-Time Sampling).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | flow-based, VLA, aims, model, data, distribution, At/ot, mapping, observation, consists, images, language, instructions, robot | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | flow-based, VLA, aims, model, data, distribution, At/ot, mapping, observation, consists | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | summary, main, contributions, FM-Steer, test-time, computing, framework, enhances, flow-based, Vision-Language-Action | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | Due, multiple, Euler, forward, iterations, required, flow-based, VLA, during, inference | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Preliminaries - extractive body cue:** A flow-based VLA aims to model the data distribution p(At/ot), mapping the observation ot, which consists of images it, language instructions ℓt, and robot state ...
- **p. 4 / 4.2. Cascaded Action Denoising - extractive body cue:** For the k-th sub-action chunk Aτ ∗ t,k, it contains the noisy action from time step t + kh to t + (k + 1)h ...
- **p. 4 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** In this way, the intermediate flow verifier estimates the state-action value Qφ(qt, Aτn t ) of the candidate flow point Aτn t conditioned on the ...
- **p. 2 / 1. Introduction - extractive body cue:** The intermediate flow verifier is trained with offline reinforcement learning and serves as a state-action value estimator, which is used to select the candidates with ...
- **p. 7 / 5.3. Efficiency Improvement - extractive body cue:** Optimal Noisy Candidate Sampled Noisy Candidates a) Value Map of Candidate Actions PCA1 PCA2 state-action values b) Cascaded Action Denoising Visualization Refined Action Figure 5.
- **p. 2 / 1. Introduction - extractive body cue:** By iteratively sampling intermediate noisy actions rather than fully denoised actions, part of the flowmatching computation in the original action expert is asynchronously offloaded to ...
- **p. 5 / 4.3. Training and Deployment Strategy - extractive body cue:** The action of the dataset used to train the LiteFlow denoiser is obtained by sampling from the frozen original VLA, and the observation is obtained ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Specifically, at timestep t, the optimal flow point selected by the intermediate flow verifier is a noisy action chunk Aτ ∗ t ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | For example, at the initial timestep t, the original VLA generates N = 5 candidate action chunks {Aτ1 t , Aτ2 t ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | For example, at the initial timestep t, the original VLA generates N = 5 candidate action chunks {Aτ1 t , Aτ2 t ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** During training, we use the calibrated Q-learning [49] to optimize the intermediate flow verifier φ.
- **p. 5 / 5.1. Implementation Details - extractive body cue:** During deployment, we use a single RTX 4090 GPU for inference.
- **p. 5 / 5.1. Implementation Details - extractive body cue:** FM-Steer is trained on 8 A100 GPUs with a batch size ranging from 8 to 32 across different datasets.

## Method-Specific Formal Details

- **Body-defined terms:** During, training, calibrated, Q-learning, optimize, intermediate, flow, verifier, k-th, sub-action, chunk, contains, noisy, action, time, step, corresponding, observation, including, image.
- **Relevant PDF headings:** 4. Methodology (p. 3); Model (p. 6).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including ... | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Filtering / recovery | We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including ... | p. 5 (5. Experiments), p. 1 (Figure/Table caption) |
| Monitoring / re-entry | Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer ... | p. 6 (Figure/Table caption), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablations on LIBERO and SimplerEnv. We conduct ablation studies across LIBERO [44] and SimplerEnv [39] on Wid- owX and Google Robot tasks. In ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Real-world ablations on WidowX, Franka, and Agi- Bot G-1. We conduct ablation studies of FM-Steer across 3 differ- ent real-world robotic platforms, covering ...
- **p. 8 / 6. Conclusion - extractive body cue:** The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies.
- **p. 8 / 6. Conclusion - extractive body cue:** FM-Steer combines valueguided test-time sampling with effective best-of-N selection and cascaded action denoising, integrating the original VLA with a lightweight denoiser to achieve rapid and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of FM-Steer. FM-Steer augments a flow-based VLA with two modules: the intermediate flow verifier and the Lite- Flow denoiser. Given an observation, ...
- **p. 5 / 5.1. Implementation Details - extractive body cue:** FMSteer sets the noise-level bound T in the range of 0.7 to 0.9 and selects N = 5 candidates from the original VLA at each ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Experimental setups on WidowX, AgiBot G-1, and Franka. We evaluate FM-Steer across 3 simulation environments and 3 different real-world robotic platforms, covering 15 ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.2. Cascaded Action Denoising), p. 7 (5.3. Efficiency Improvement), p. 3 (4.1. Value-Guided Test-Time Sampling), p. 3 (4. Methodology), p. 7 (5.3. Efficiency Improvement), objective p. 3 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.2. Cascaded Action Denoising), p. 4 (4.1. Value-Guided Test-Time Sampling), p. 5 (4.3. Training and Deployment Strategy), p. 7 (5.3. Efficiency Improvement), p. 3 (4.1. Value-Guided Test-Time Sampling), temporal p. 4 (4.2. Cascaded Action Denoising), p. 5 (4.3. Training and Deployment Strategy), p. 4 (4.2. Cascaded Action Denoising), p. 5 (4.3. Training and Deployment Strategy), p. 3 (3. Preliminaries), p. 1 (Body text (section not recovered)).
