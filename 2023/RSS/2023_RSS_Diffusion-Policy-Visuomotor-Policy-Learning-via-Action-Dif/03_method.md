# Method - Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.04137; PDF retrieval source: https://arxiv.org/pdf/2303.04137. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 16 (A.4 Hyperparameters), p. 16 (A.4 Hyperparameters)): On simulation benchmarks, we used the iDDPM algorithm Nichol and Dhariwal (2021) with the same 100 denoising diffusion iterations for both training and inference.

## Method Body Digest

- **p. 16 / A.4 Hyperparameters - extractive body cue:** On simulation benchmarks, we used the iDDPM algorithm Nichol and Dhariwal (2021) with the same 100 denoising diffusion iterations for both training and inference.
- **p. 16 / A.4 Hyperparameters - extractive body cue:** For CNN-based Diffusion Policy, We found using FiLM conditioning to pass-in observations is better than impainting on all tasks 1 2 3 4 5 6 ...
- **p. 16 / A.1 Normalization - extractive body cue:** Scaling the min and max of each action dimension independently to [-1,1] works well for most tasks.
- **p. 3 / 1 Introduction - extractive body cue:** Diffusion Policy 3 b) CNN-based c) Transformer-based Conv1D Conv1D Conv1D Conv1D Conv1D Input: Image Observation Sequence Output: Action Sequence … Cross Attention Cross Attention ×K ...
- **p. 3 / 1 Introduction - extractive body cue:** At time step t, the policy takes the latest To steps of observation data Ot as input and outputs Ta steps of actions At. b) ...
- **p. 1 / 1 Introduction - extractive body cue:** In this formulation, instead of directly outputting an action, the policy infers the action-score gradient, conditioned on visual observations, for K denoising iterations (Fig.
- **p. 1 / 1 Introduction - extractive body cue:** Policy learning from demonstration, in its simplest form, can be formulated as the supervised regression task of learning to map observations to actions.
- **p. 5 / 1 Introduction - extractive body cue:** 4.3 Benefits of Action-Sequence Prediction Sequence prediction is often avoided in most policy learning methods due to the difficulties in effectively sampling from high-dimensional output ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its ...
- **p. 4 / 1 Introduction - extractive body cue:** (2020), we introduce a novel transformer-based DDPM which adopts the transformer architecture from minGPT Shafiullah et al.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a visionconditioned diffusion policy, where the visual observations are treated as conditioning instead of a part of the joint data distribution.

## Source Evidence Cues

- **p. 16 / A.4 Hyperparameters - extractive body cue:** On simulation benchmarks, we used the iDDPM algorithm Nichol and Dhariwal (2021) with the same 100 denoising diffusion iterations for both training and inference.
- **p. 16 / A.4 Hyperparameters - extractive body cue:** For CNN-based Diffusion Policy, We found using FiLM conditioning to pass-in observations is better than impainting on all tasks 1 2 3 4 5 6 ...
- **Detected method headings:** A Diffusion Policy Implementation Details (p. 16); C.2.2 Evaluation Both Diffusion Policy and LSTM-GMM (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | On simulation benchmarks, we used the iDDPM algorithm Nichol and Dhariwal (2021) with the same 100 denoising diffusion iterations for both training ... | p. 16 (A.4 Hyperparameters), p. 16 (A.4 Hyperparameters) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | For CNN-based Diffusion Policy, We found using FiLM conditioning to pass-in observations is better than impainting on all tasks 1 2 3 ... | p. 16 (A.4 Hyperparameters) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | On simulation benchmarks, we used the iDDPM algorithm Nichol and Dhariwal (2021) with the same 100 denoising diffusion iterations for both training ... | p. 16 (A.4 Hyperparameters) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 16 / A.1 Normalization - extractive body cue:** Scaling the min and max of each action dimension independently to [-1,1] works well for most tasks.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 16 (A.1 Normalization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Diffusion, Policy, CNN-based, Transformer-based, Conv1D, Input, Image, Observation, Sequence, Output, Action, Cross, Attention, Obs | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | Diffusion, Policy, CNN-based, Transformer-based, Conv1D, Input, Image, Observation, Sequence, Output | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | successfully, employ, diffusion, models, visuomotor, policy, learning, present, following, technical | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Scaling, action, dimension, independently, works, well, most, tasks | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive body cue:** Diffusion Policy 3 b) CNN-based c) Transformer-based Conv1D Conv1D Conv1D Conv1D Conv1D Input: Image Observation Sequence Output: Action Sequence … Cross Attention Cross Attention ×K ...
- **p. 3 / 1 Introduction - extractive body cue:** At time step t, the policy takes the latest To steps of observation data Ot as input and outputs Ta steps of actions At. b) ...
- **p. 1 / 1 Introduction - extractive body cue:** In this formulation, instead of directly outputting an action, the policy infers the action-score gradient, conditioned on visual observations, for K denoising iterations (Fig.
- **p. 1 / 1 Introduction - extractive body cue:** Policy learning from demonstration, in its simplest form, can be formulated as the supervised regression task of learning to map observations to actions.
- **p. 5 / 1 Introduction - extractive body cue:** 4.3 Benefits of Action-Sequence Prediction Sequence prediction is often avoided in most policy learning methods due to the difficulties in effectively sampling from high-dimensional output ...
- **p. 6 / 1 Introduction - extractive body cue:** 0 500 1000 Epoch 0.0 0.001 0.002 0.003 0.004 Train Action Pred MSE Real PushT Img 0 500 1000 Epoch 0.0 0.2 0.4 0.6 0.8 ...
- **p. 16 / A.4 Hyperparameters - extractive body cue:** State-based Diffusion Policy is not sensitive to observation horizon.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value was not selected from the PDF body. | Diffusion Policy employs receding horizon position control to predict a sequence of actions into the future. | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | In particular, when the prediction horizon is one time step, Tp = 1, it can be seen that the optimal denoiser which ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | 5 left) and found the action horizon of 8 steps to be optimal for most tasks that we tested. | hardware, batch and throughput |

## Training vs Inference

- **p. 16 / A.4 Hyperparameters - extractive body cue:** On simulation benchmarks, we used the iDDPM algorithm Nichol and Dhariwal (2021) with the same 100 denoising diffusion iterations for both training and inference.
- **p. 7 / 5 Evaluation - extractive body cue:** We report results from the average of the last 10 checkpoints (saved every 50 epochs) across 3 training seeds and 50 environment initializations * (an ...
- **p. 8 / 5 Evaluation - extractive body cue:** However, we found finetuning the pretrained vision encoder with a small learning rate (10x smaller vs diffusion policy network) gives the best performance overall.
- **p. 8 / 5 Evaluation - extractive body cue:** For each architecture, we evaluated 3 different training strategies: training end-to-end from scratch, using frozen pre-trained vision encoder, and finetuning pre-trained vision encoders (with 10x ...
- **p. 7 / 5 Evaluation - extractive body cue:** Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of last 10 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** simulation, benchmarks, iDDPM, algorithm, Nichol, Dhariwal, same, denoising, diffusion, iterations, training, inference, CNN-based, Policy, found, FiLM, conditioning, pass-in, observations, better.
- **Relevant PDF headings:** A Diffusion Policy Implementation Details (p. 16); C.2.2 Evaluation Both Diffusion Policy and LSTM-GMM (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | The benchmark consists of 5 tasks with a proficient human (PH) teleoperated demonstration dataset for each and mixed proficient/non-proficient human (MH) demonstration ... | p. 6 (5 Evaluation), p. 7 (5 Evaluation) |
| Policy fitting | We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of ... | p. 6 (5 Evaluation), p. 8 (5 Evaluation) |
| Closed-loop rollout | Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) ... | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 5 Evaluation - extractive body cue:** There are two variants: one with RGB image observations and another with 9 2D keypoints obtained from the groundtruth pose of the T block, both ...
- **p. 8 / 5 Evaluation - extractive body cue:** Each method is evaluated with its best-performing action space: position control for Diffusion Policy and velocity control for baselines (the effect of action space will ...
- **p. 6 / 5 Evaluation - extractive body cue:** For each variant, we report results for both stateand image-based observations.
- **p. 8 / 5 Evaluation - extractive body cue:** 5.4 Ablation Study We explore alternative vision encoder design decisions on the simulated robomimic square task.
- **p. 9 / 5 Evaluation - extractive body cue:** 0.84 average IoU, compared with the 0% and 20% success rate of best-performing IBC and LSTM-GMM variants.
- **p. 9 / 5 Evaluation - extractive body cue:** On all tasks, Diffusion Policy variants with both CNN backbones and end-to-end-trained visual encoders yielded the best performance.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Diffusion Policy Ablation Study. Change (difference) in success rate relative to the maximum for each task is shown on the Y-axis. Left: trade-off ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 16 (A.4 Hyperparameters), p. 16 (A.4 Hyperparameters), objective p. 16 (A.1 Normalization), temporal p. 8 (5 Evaluation), p. 6 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 7 (5 Evaluation), p. 8 (5 Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** At time step t, the policy takes the latest To steps of observation data Ot as input and outputs Ta steps of actions At. b) In the CNN-based Diffusion Policy, ... (p. 3, 1 Introduction).
- **Objective/update evidence:** Scaling the min and max of each action dimension independently to [-1,1] works well for most tasks. (p. 16, A.1 Normalization).
- **Temporal/runtime evidence:** 5 left) and found the action horizon of 8 steps to be optimal for most tasks that we tested. (p. 8, 5 Evaluation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
