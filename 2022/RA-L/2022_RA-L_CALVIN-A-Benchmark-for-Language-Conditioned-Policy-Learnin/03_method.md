# Method - CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.03227; PDF retrieval source: https://arxiv.org/pdf/2112.03227. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS)): The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for how to get from xt to xg.

## Method Body Digest

- **p. 6 / IV. BASELINE MODELS - extractive body cue:** The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for how to get ...
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** The encoder for the gripper camera takes an image of 84 × 84 as input and consists of 3 convolutional layers with 32, 64, and ...
- LfP 기준선은 놀이 궤적의 관측과 목표 영상을 조건으로 시연 행동의 우도를 높인다. [§IV 식 1 · PDF 6쪽](https://arxiv.org/pdf/2112.03227v4#page=6)
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** We set the weight controlling the influence of the KL divergence to the total loss to β = 0.001.
- **p. 3 / III. CALVIN - extractive body cue:** 2: Observation and action spaces supported by CALVIN. only allow feasible sequences that can be achieved from a predefined initial environment state.
- **p. 3 / 3) CALVIN Challenge - extractive body cue:** 1) Observation and Action Space: Unlike prior work which relies on RGB images from an egocentric camera to perceive its surroundings [1], [6], CALVIN offers ...
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** However, when learning language-conditioned policies πθ (at / xt, l) it is not possible to relabel any visited state x to a natural language goal ...
- **p. 2 / 1. CALVIN includes ∼24 hours teleoperated unstructured play - extractive body cue:** This is the first public benchmark of instruction following, to our knowledge, that combines: natural language conditioning, multimodal highdimensional inputs, 7-DOF continuous control, and longhorizon ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.
- **p. 2 / A LONG-STANDING goal for robotics and embodied - extractive body cue:** To address this problem we present CALVIN, a new opensource simulated benchmark that links human language to robot motor skills, behaviors, and objects in interactive ...
- **p. 3 / III. CALVIN - extractive body cue:** The CALVIN benchmark consists of three key components, which are:

## Source Evidence Cues

- **p. 6 / IV. BASELINE MODELS - extractive body cue:** The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for how to get ...
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** The encoder for the gripper camera takes an image of 84 × 84 as input and consists of 3 convolutional layers with 32, 64, and ...
- **Detected method headings:** IV. BASELINE MODELS (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for ... | p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | The encoder for the gripper camera takes an image of 84 × 84 as input and consists of 3 convolutional layers with ... | p. 6 (IV. BASELINE MODELS) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for ... | p. 6 (IV. BASELINE MODELS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- 놀이 데이터에서 목표 영상 $x_g$와 짧은 궤적 $\tau$를 뽑고, 행동의 조건부 로그우도 $\mathcal L_{\mathrm{LfP}}=\mathbb E_{(\tau,x_g)\sim D_{\mathrm{play}}}\!\left[\sum_{t=0}^{\lvert\tau\rvert}\log\pi_\theta(a_t\mid x_t,x_g)\right]$를 최대화한다. [§IV 식 1 · PDF 6쪽](https://arxiv.org/pdf/2112.03227v4#page=6)
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** We set the weight controlling the influence of the KL divergence to the total loss to β = 0.001.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | decoder, policy, trained, reconstruct, input, actions, conditioned, state, goal, inferred, plan, Observation, action, spaces | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | decoder, policy, trained, reconstruct, input, actions, conditioned, state, goal, inferred | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | present, CALVIN, Composing, Actions, Language, Vision, open-source, simulated, benchmark, learn | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | short, horizon, goal, image, conditioned, demonstrations, simple, maximum, likelihood, imitation | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / IV. BASELINE MODELS - extractive body cue:** The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for how to get ...
- **p. 3 / III. CALVIN - extractive body cue:** 2: Observation and action spaces supported by CALVIN. only allow feasible sequences that can be achieved from a predefined initial environment state.
- **p. 3 / 3) CALVIN Challenge - extractive body cue:** 1) Observation and Action Space: Unlike prior work which relies on RGB images from an egocentric camera to perceive its surroundings [1], [6], CALVIN offers ...
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** However, when learning language-conditioned policies πθ (at / xt, l) it is not possible to relabel any visited state x to a natural language goal ...
- **p. 2 / 1. CALVIN includes ∼24 hours teleoperated unstructured play - extractive body cue:** This is the first public benchmark of instruction following, to our knowledge, that combines: natural language conditioning, multimodal highdimensional inputs, 7-DOF continuous control, and longhorizon ...
- **p. 4 / 3) CALVIN Challenge - extractive body cue:** 2) Language Instructions: Approaches that learn languageconditioned continuous control policies typically require posthoc crowd-sourced natural language labels aligned with its corresponding robot interaction data [6], ...
- **p. 4 / 3) CALVIN Challenge - extractive body cue:** This poses an additional challenge since the policy has to generalize to multiple textures 1Simulator states consisting of object positions and orientations are also provided, ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | In contrast to their work, CALVIN contains more subtasks (34 vs 18), longer longhorizon evaluation sequences (5 vs 4), provides a range ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | For the Long-Horizon MTLC evaluation we observe that the agents perform poorly on CALVIN's long-horizon tasks with high-dimensional state spaces. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / IV. BASELINE MODELS - extractive body cue:** The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for how to get ...
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** We train the agent with the Adam optimizer and a learning rate of 10-4.
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** We note that the same training hyperparameters are used for all splits.

## Method-Specific Formal Details

- **Body-defined terms:** decoder, policy, trained, reconstruct, input, actions, conditioned, state, goal, inferred, plan, encoder, gripper, camera, takes, image, consists, convolutional, layers, channels.
- 식 1에서 시연 행동은 현재 관측과 목표 영상에 조건부다. [§IV 식 1 · PDF 6쪽](https://arxiv.org/pdf/2112.03227v4#page=6)

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | MEES et al.: CALVIN: A BENCHMARK FOR LANGUAGE-CONDITIONED POLICY LEARNING FOR LONG-HORIZON ROBOT MANIPULATION TASKS 7 Input Train →Test MTLC LH-MTLC Static ... | p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Baseline harness | We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, ... | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Metric / failure reporting | We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, ... | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** Additionally, more elaborate sensor fusion approaches such as mixture of experts [33], [34] or view-invariant contrastive learning [35], [36] might be necessary to learn better ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** In order to achieve better zero-shot generalization capabilities, additional techniques from the domain adaptation literature [36], better data augmentation and a stronger focus on depth ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Observation and action spaces supported by CALVIN. only allow feasible sequences that can be achieved from a predefined initial environment state. The CALVIN ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS), objective p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS), temporal p. 2 (II. RELATED WORK), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 3 (3) CALVIN Challenge), p. 3 (3) CALVIN Challenge), p. 4 (3) CALVIN Challenge).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for how to get from xt to xg. (p. 6, IV. BASELINE MODELS).
- **Objective/update evidence:** We set the weight controlling the influence of the KL divergence to the total loss to β = 0.001. (p. 6, IV. BASELINE MODELS).
- **Temporal/runtime evidence:** For the Long-Horizon MTLC evaluation we observe that the agents perform poorly on CALVIN's long-horizon tasks with high-dimensional state spaces. (p. 7, V. EXPERIMENTAL RESULTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
