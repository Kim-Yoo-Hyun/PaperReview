# Method - BridgeData V2: A Dataset for Robot Learning at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2308.12952; PDF retrieval source: https://arxiv.org/pdf/2308.12952. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 14 (B.2 Diffusion goal-conditioned behavior cloning), p. 14 (B.4 Contrastive RL), p. 15 (B.6 RT-1), p. 13 (B Learning Method Implementation Details), p. 15 (B.5 Language-conditioned behavior cloning), p. 13 (B Learning Method Implementation Details)): We use the DDPM (Denoising Diffusion Probabilistic Models) style objective as introduced by Ho et al.

## Method Body Digest

- **p. 14 / B.2 Diffusion goal-conditioned behavior cloning - extractive PDF cue:** We use the DDPM (Denoising Diffusion Probabilistic Models) style objective as introduced by Ho et al.
- **p. 14 / B.4 Contrastive RL - extractive PDF cue:** Those image encodings then pass through two MLPs to get representations of the observation and the goal.
- **p. 15 / B.6 RT-1 - extractive PDF cue:** We use the same hyper-parameters as the original RT-1 paper [7], except for increasing the sequence length of the transformer from 6 to 15 to ...
- **p. 13 / B Learning Method Implementation Details - extractive PDF cue:** During training, the goal associated with an observation is selected by uniformly sampling an observation from the future timesteps in the trajectory.
- **p. 15 / B.5 Language-conditioned behavior cloning - extractive PDF cue:** The language instruction is first encoded with a frozen MUSE encoder and passed through 2 fully connected layers.
- **p. 13 / B Learning Method Implementation Details - extractive PDF cue:** All the goal-conditioned methods take in both an observation and goal.
- **p. 14 / B.4 Contrastive RL - extractive PDF cue:** Our contrastive RL objective retains the temporal-difference (TD) style used in [53].
- **p. 15 / B.5 Language-conditioned behavior cloning - extractive PDF cue:** We use the Adam optimizer [60] with a learning rate of 3e-4.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge Dataset ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are a new dataset of robotic manipulation behaviors as well as the empirical study of state-of-the-art offline learning methods using the introduced dataset.
- **p. 15 / B.4 Contrastive RL - extractive PDF cue:** The greater size and diversity of BridgeData V2 enables significantly better generalization to these unseen tasks.

## Source Evidence Cues

- **p. 14 / B.2 Diffusion goal-conditioned behavior cloning - extractive PDF cue:** We use the DDPM (Denoising Diffusion Probabilistic Models) style objective as introduced by Ho et al.
- **p. 14 / B.4 Contrastive RL - extractive PDF cue:** Those image encodings then pass through two MLPs to get representations of the observation and the goal.
- **p. 15 / B.6 RT-1 - extractive PDF cue:** We use the same hyper-parameters as the original RT-1 paper [7], except for increasing the sequence length of the transformer from 6 to 15 to ...
- **p. 13 / B Learning Method Implementation Details - extractive PDF cue:** During training, the goal associated with an observation is selected by uniformly sampling an observation from the future timesteps in the trajectory.
- **p. 15 / B.5 Language-conditioned behavior cloning - extractive PDF cue:** The language instruction is first encoded with a frozen MUSE encoder and passed through 2 fully connected layers.
- **p. 13 / B Learning Method Implementation Details - extractive PDF cue:** All the goal-conditioned methods take in both an observation and goal.
- **Detected method headings:** B Learning Method Implementation Details (p. 13)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | We use the DDPM (Denoising Diffusion Probabilistic Models) style objective as introduced by Ho et al. | p. 14 (B.2 Diffusion goal-conditioned behavior cloning), p. 14 (B.4 Contrastive RL) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | Those image encodings then pass through two MLPs to get representations of the observation and the goal. | p. 14 (B.4 Contrastive RL), p. 15 (B.6 RT-1) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | We use the same hyper-parameters as the original RT-1 paper [7], except for increasing the sequence length of the transformer from 6 ... | p. 15 (B.6 RT-1), p. 13 (B Learning Method Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / B.4 Contrastive RL - extractive PDF cue:** Our contrastive RL objective retains the temporal-difference (TD) style used in [53].
- **p. 14 / B.2 Diffusion goal-conditioned behavior cloning - extractive PDF cue:** We use the DDPM (Denoising Diffusion Probabilistic Models) style objective as introduced by Ho et al.
- **p. 15 / B.5 Language-conditioned behavior cloning - extractive PDF cue:** We use the Adam optimizer [60] with a learning rate of 3e-4.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 14 (B.4 Contrastive RL), p. 14 (B.2 Diffusion goal-conditioned behavior cloning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, given, observation, goal, images, feed, them, separately, through, ResNet-34, encoder, instead, layer, CNN | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | First, given, observation, goal, images, feed, them, separately, through, ResNet-34 | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | dataset, call, BridgeData, Figure, because, greatly, expands, previously, released, Bridge | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | contrastive, objective, retains, temporal-difference, style, DDPM, Denoising, Diffusion, Probabilistic, Models | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 14 / B.4 Contrastive RL - extractive PDF cue:** First, given the observation and goal images, we feed them separately through a ResNet-34 encoder instead of a 3-layer CNN image encoder to get output ...
- **p. 2 / 1 Introduction - extractive PDF cue:** These methods cover a range of key design decisions involving the policy architecture, the use of observation histories, action discretization, and action prediction horizon.
- **p. 2 / 1 Introduction - extractive PDF cue:** Additionally, the dataset should support flexible task conditioning, through goal images or natural language instructions, so that researchers can easily command policies trained on the ...
- **p. 14 / B.1 Goal-conditioned behavior cloning - extractive PDF cue:** The observation and goal are stacked channel-wise before being passed into a ResNet-34 image encoder.
- **p. 15 / B.5 Language-conditioned behavior cloning - extractive PDF cue:** The image observation is then passed into the ResNet, which is conditioned on the language embedding using FiLM layers.
- **p. 13 / B Learning Method Implementation Details - extractive PDF cue:** All the goal-conditioned methods take in both an observation and goal.
- **p. 13 / B Learning Method Implementation Details - extractive PDF cue:** During training, the goal associated with an observation is selected by uniformly sampling an observation from the future timesteps in the trajectory.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | The original ACT has chunk size 100 to accommodate for high-frequency control (50Hz) and long trajectories (1000 steps), while in our case ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | During training, the goal associated with an observation is selected by uniformly sampling an observation from the future timesteps in the trajectory. | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | The original ACT has chunk size 100 to accommodate for high-frequency control (50Hz) and long trajectories (1000 steps), while in our case ... | hardware, batch and throughput |

## Training vs Inference

- **p. 13 / B Learning Method Implementation Details - extractive PDF cue:** During training, the goal associated with an observation is selected by uniformly sampling an observation from the future timesteps in the trajectory.
- **p. 13 / B Learning Method Implementation Details - extractive PDF cue:** During training, the goal associated with an observation is selected by uniformly sampling an observation from the future timesteps in the trajectory.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** DDPM, Denoising, Diffusion, Probabilistic, Models, style, objective, introduced, image, encodings, then, pass, through, MLPs, representations, observation, goal, same, hyper-parameters, original.
- **Relevant PDF headings:** B Learning Method Implementation Details (p. 13).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | Assembling a large real-world dataset is time-consuming and expensive, so there has also been significant work on developing simulated environments and datasets ... | p. 3 (Dataset), p. 3 (Dataset) |
| Policy fitting | Once again, RT-1 greatly outperformed the LCBC baseline. | p. 7 (5 Experiments), p. 6 (5 Experiments) |
| Closed-loop rollout | ResNet-18 ResNet-34 ResNet-50 Image Encoder 0.0 0.2 0.4 0.6 0.8 1.0 Average Success Rate 0.25 0.50 0.75 1.00 Proportion of Dataset 0.0 ... | p. 8 (5 Experiments), p. 7 (5 Experiments) |

## Failure and Ablation Link

- **p. 7 / 5 Experiments - extractive PDF cue:** Note that these evaluations were performed zero-shot, without any new data collected in Lab 2, and we expect fine-tuning on a small amount of data ...
- **p. 3 / Dataset - extractive PDF cue:** Additionally, unlike many prior datasets [23, 5], our experiments isolate the effect of data diversity and show that greater diversity improves generalization, corroborating the result ...
- **p. 15 / B.4 Contrastive RL - extractive PDF cue:** Task BridgeData V1 + PTR BridgeData V2 Put marker in bowl† 0.05 0.65 Put mushroom in pot‡ 0.10 0.70 Average 0.08 0.70 † Unseen objects, ...
- **p. 8 / 5 Experiments - extractive PDF cue:** 6 Discussion, Limitations, and Future Work We presented BridgeData V2, a dataset with 60,096 trajectories of robotic manipulation behaviors designed to enable research on scalable ...
- **p. 4 / Dataset - extractive PDF cue:** While this policy fails frequently, we can run it autonomously to collect a large amount of pick-and-place data for a wide range of objects more ...
- **p. 7 / 5 Experiments - extractive PDF cue:** Additionally, the "put eggplant in pot" is a very challenging task in both labs since the eggplant easily slips out of the gripper.
- **p. 3 / Dataset - extractive PDF cue:** Training on a combination of the largest datasets released so far is an exciting and promising direction for future work.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 14 (B.2 Diffusion goal-conditioned behavior cloning), p. 14 (B.4 Contrastive RL), p. 15 (B.6 RT-1), p. 13 (B Learning Method Implementation Details), p. 15 (B.5 Language-conditioned behavior cloning), p. 13 (B Learning Method Implementation Details), objective p. 14 (B.4 Contrastive RL), p. 14 (B.2 Diffusion goal-conditioned behavior cloning), p. 15 (B.5 Language-conditioned behavior cloning), temporal p. 14 (B.3 Action Chunking with Transformers), p. 13 (B Learning Method Implementation Details), p. 15 (B.6 RT-1), p. 6 (5 Experiments), p. 8 (5 Experiments), p. 14 (B.1 Goal-conditioned behavior cloning).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
