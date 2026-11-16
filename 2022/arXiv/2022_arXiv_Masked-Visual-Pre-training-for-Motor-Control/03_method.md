# Method - Masked Visual Pre-training for Motor Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.06173; PDF retrieval source: https://arxiv.org/abs/2203.06173. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2.2. Learning Motor Control from Pixels), p. 3 (2.1. Masked Visual Pre-training), p. 2 (2) Our self-supervised approach consistently outperforms), p. 2 (2) Our self-supervised approach consistently outperforms), p. 4 (2.2. Learning Motor Control from Pixels), p. 4 (3.6. Distributed Training)): Specifically, we use the proximal policy optimization (PPO) algorithm (Schulman et al., 2017).

## Method Body Digest

- **p. 3 / 2.2. Learning Motor Control from Pixels - extractive body cue:** Specifically, we use the proximal policy optimization (PPO) algorithm (Schulman et al., 2017).
- **p. 3 / 2.1. Masked Visual Pre-training - extractive body cue:** We adopt masked modeling as our self-supervision objective-specifically, we use masked autoencoder (MAE) (He et al., 2021).
- **p. 2 / 2) Our self-supervised approach consistently outperforms - extractive body cue:** We believe that our work is a promising step in this direction and release the benchmark suite, pre-trained models, and the training code on the ...
- **p. 2 / 2) Our self-supervised approach consistently outperforms - extractive body cue:** supervised representations (up to 80% absolute success rate), and even matches the oracle performance in some cases. - 3) We find that pre-training on images ...
- **p. 4 / 2.2. Learning Motor Control from Pixels - extractive body cue:** Crucially, it leverages a fast simulator and provides distributed training for scaling learning-based motor control from pixel observations.
- **p. 4 / 3.6. Distributed Training - extractive body cue:** Similar to data parallel training, we create a model replica per-GPU, collect rollouts on each GPU, and synchronize gradients across GPUs.
- **p. 5 / 3.6. Distributed Training - extractive body cue:** The result shows that self-supervised pre-training markedly improves representation quality for motor control tasks.
- **p. 3 / 2.2. Learning Motor Control from Pixels - extractive body cue:** PPO is a state-of-theart policy gradient method that has shown excellent performance on complex motor control tasks and successful transfer to real hardware (OpenAI et ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We also compare our method to visual encoders trained by supervised learning on ImageNet (Deng et al., 2009), the choice of encoder in most vision ...
- **p. 4 / 3.1. Motivation - extractive body cue:** To this end, we introduce a new benchmark suite for Pixel Motor Control, which we call PixMC.
- **p. 1 / 1. Introduction - extractive body cue:** We show that we are able to solve a range of motor control tasks with variations in robots, scenes, and objects.

## Source Evidence Cues

- **p. 3 / 2.2. Learning Motor Control from Pixels - extractive body cue:** Specifically, we use the proximal policy optimization (PPO) algorithm (Schulman et al., 2017).
- **p. 3 / 2.1. Masked Visual Pre-training - extractive body cue:** We adopt masked modeling as our self-supervision objective-specifically, we use masked autoencoder (MAE) (He et al., 2021).
- **p. 2 / 2) Our self-supervised approach consistently outperforms - extractive body cue:** We believe that our work is a promising step in this direction and release the benchmark suite, pre-trained models, and the training code on the ...
- **p. 2 / 2) Our self-supervised approach consistently outperforms - extractive body cue:** supervised representations (up to 80% absolute success rate), and even matches the oracle performance in some cases. - 3) We find that pre-training on images ...
- **p. 4 / 2.2. Learning Motor Control from Pixels - extractive body cue:** Crucially, it leverages a fast simulator and provides distributed training for scaling learning-based motor control from pixel observations.
- **p. 4 / 3.6. Distributed Training - extractive body cue:** Similar to data parallel training, we create a model replica per-GPU, collect rollouts on each GPU, and synchronize gradients across GPUs.
- **p. 5 / 3.6. Distributed Training - extractive body cue:** The result shows that self-supervised pre-training markedly improves representation quality for motor control tasks.
- **Detected method headings:** 2) Our self-supervised approach consistently outperforms (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | Specifically, we use the proximal policy optimization (PPO) algorithm (Schulman et al., 2017). | p. 3 (2.2. Learning Motor Control from Pixels), p. 3 (2.1. Masked Visual Pre-training) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | We adopt masked modeling as our self-supervision objective-specifically, we use masked autoencoder (MAE) (He et al., 2021). | p. 3 (2.1. Masked Visual Pre-training), p. 2 (2) Our self-supervised approach consistently outperforms) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | We believe that our work is a promising step in this direction and release the benchmark suite, pre-trained models, and the training ... | p. 2 (2) Our self-supervised approach consistently outperforms), p. 2 (2) Our self-supervised approach consistently outperforms) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2.1. Masked Visual Pre-training - extractive body cue:** We adopt masked modeling as our self-supervision objective-specifically, we use masked autoencoder (MAE) (He et al., 2021).
- **p. 3 / 2.2. Learning Motor Control from Pixels - extractive body cue:** PPO is a state-of-theart policy gradient method that has shown excellent performance on complex motor control tasks and successful transfer to real hardware (OpenAI et ...
- **p. 4 / 3.6. Distributed Training - extractive body cue:** Similar to data parallel training, we create a model replica per-GPU, collect rollouts on each GPU, and synchronize gradients across GPUs.
- **p. 4 / 2.2. Learning Motor Control from Pixels - extractive body cue:** Compared to existing benchmarks, ours features a unique combination of hand-designed tasks, dense rewards, and complex robots (e.g., multi-finger hands).
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 3 (2.1. Masked Visual Pre-training), p. 3 (2.2. Learning Motor Control from Pixels), p. 4 (3.6. Distributed Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, training, computationally, expensive, poor, sample, complexity, especially, high-dimensional, inputs, actions, PPO, state-of-theart, policy | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | First, training, computationally, expensive, poor, sample, complexity, especially, high-dimensional, inputs | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | compare, visual, encoders, trained, supervised, learning, ImageNet, Deng, choice, encoder | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | adopt, masked, modeling, self-supervision, objective-specifically, autoencoder, MAE, PPO, state-of-theart, policy | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** First, training is computationally expensive and has poor sample complexity (especially with high-dimensional inputs and actions).
- **p. 3 / 2.2. Learning Motor Control from Pixels - extractive body cue:** PPO is a state-of-theart policy gradient method that has shown excellent performance on complex motor control tasks and successful transfer to real hardware (OpenAI et ...
- **p. 2 / 1. Introduction - extractive body cue:** As an upper bound, we consider oracle hand-engineered states for solving a task (e.g., 3D poses and direction-to-goal vectors).
- **p. 4 / 3.4. Observations and Actions - extractive body cue:** The benchmark provides proprioceptive information for the robots, as well as hand-engineered states typically including 3D poses or relevant objects, goals, and their relations.
- **p. 1 / 1. Introduction - extractive body cue:** Our network encodes the input image using a high-capacity visual encoder (Dosovitskiy et al., 2020) and combines it with proprioceptive information to obtain an embedding.
- **p. 3 / 2.1. Masked Visual Pre-training - extractive body cue:** Notice that the images are representative of everyday interactions making them well suited for our needs.
- **p. 1 / 1. Introduction - extractive body cue:** The required movement types vary from simple reaching to object interactions.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | We define reward-independent success metrics that typically quantify the distance from the agent or an object to a specified goal location over ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | We freeze the visual encoder throughout the entire training horizon. | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | To reduce randomness in the RL experiments (Agarwal et al., 2021), for each task and model we search for the best learning ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 2) Our self-supervised approach consistently outperforms - extractive body cue:** We believe that our work is a promising step in this direction and release the benchmark suite, pre-trained models, and the training code on the ...
- **p. 2 / 2) Our self-supervised approach consistently outperforms - extractive body cue:** supervised representations (up to 80% absolute success rate), and even matches the oracle performance in some cases. - 3) We find that pre-training on images ...
- **p. 4 / 2.2. Learning Motor Control from Pixels - extractive body cue:** Crucially, it leverages a fast simulator and provides distributed training for scaling learning-based motor control from pixel observations.
- **p. 4 / 3.6. Distributed Training - extractive body cue:** Similar to data parallel training, we create a model replica per-GPU, collect rollouts on each GPU, and synchronize gradients across GPUs.
- **p. 5 / 3.6. Distributed Training - extractive body cue:** The result shows that self-supervised pre-training markedly improves representation quality for motor control tasks.
- **p. 7 / 5.3. Ablations - extractive body cue:** For each model, we train 15 instances of the model with 3 learning rates and 5 seeds.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, proximal, policy, optimization, PPO, algorithm, Schulman, adopt, masked, modeling, self-supervision, objective-specifically, autoencoder, MAE, believe, promising, step, direction, release, benchmark.
- **Relevant PDF headings:** 2) Our self-supervised approach consistently outperforms (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | The benchmark provides proprioceptive information for the robots, as well as hand-engineered states typically including 3D poses or relevant objects, goals, and ... | p. 4 (3.4. Observations and Actions), p. 4 (3.1. Motivation) |
| Policy fitting | The MVP approach significantly outperforms the supervised baseline on 7 tasks and closely matches the oracle state model (considered the upper bound ... | p. 5 (3.6. Distributed Training), p. 6 (5.1. Sample Complexity) |
| Closed-loop rollout | Figure 5. Sample complexity. We plot the success rate as a function of environment steps on the 8 PixMC tasks. Each task ... | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 4. Experimental Setup - extractive body cue:** We pre-train supervised and self-supervised variants of the ViT model.
- **p. 5 / 4. Experimental Setup - extractive body cue:** We freeze the visual encoder throughout the entire training horizon.
- **p. 7 / 5.3. Ablations - extractive body cue:** We use the same visual encoder, initialize it randomly, and freeze.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Masked visual pre-training for motor control. Left: We first pre-train visual representations using self-supervision through masked image modeling (He et al., 2021) from ...
- **p. 4 / 3.1. Motivation - extractive body cue:** While there exist a number of excellent benchmarks for motor control, e.g., DMC (Tassa et al., 2018), RLBench (James et al., 2020), Robosuite (Zhu et ...
- **p. 7 / 5.3. Ablations - extractive body cue:** The random model fails on 6 out of 8 PixMC tasks (0 success rate).
- **p. 7 / 5.3. Ablations - extractive body cue:** We observed unstable training (the loss goes to NaN), and we decreased the learning rate until training successfully completed.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2.2. Learning Motor Control from Pixels), p. 3 (2.1. Masked Visual Pre-training), p. 2 (2) Our self-supervised approach consistently outperforms), p. 2 (2) Our self-supervised approach consistently outperforms), p. 4 (2.2. Learning Motor Control from Pixels), p. 4 (3.6. Distributed Training), objective p. 3 (2.1. Masked Visual Pre-training), p. 3 (2.2. Learning Motor Control from Pixels), p. 4 (3.6. Distributed Training), p. 4 (2.2. Learning Motor Control from Pixels), temporal p. 4 (3.4. Observations and Actions), p. 5 (4. Experimental Setup), p. 5 (4. Experimental Setup), p. 6 (5.2. Generalization), p. 6 (5.2. Generalization), p. 7 (5.3. Ablations).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
