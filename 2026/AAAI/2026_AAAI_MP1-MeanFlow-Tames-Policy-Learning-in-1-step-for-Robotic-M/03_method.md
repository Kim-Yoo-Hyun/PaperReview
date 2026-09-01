# Method - MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38919; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38919. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 4 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 1 (Abstract), p. 2 (Abstract)): Because subtle scene-context variations are critical for robot learning, especially in few-shot learning, we introduce a lightweight Dispersive Loss that repels state embeddings during training, boosting generalization without slowing i ...

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** Because subtle scene-context variations are critical for robot learning, especially in few-shot learning, we introduce a lightweight Dispersive Loss that repels state embeddings during training, ...
- **p. 4 / Abstract - extractive body cue:** This can lead to a form of "feature collapse", where the policy network maps distinct environmental states that demand fundamentally different actions to nearly identical ...
- **p. 3 / Abstract - extractive body cue:** MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D point clouds P ...
- **p. 4 / Abstract - extractive body cue:** Training Objective and Inference Our final training objective synergistically combines the trajectory generation and representation regularization goals: Ltotal(θ) = Lcfg(θ) + λLDisp(θ) (7) Here, Lcfg ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 2 / Abstract - extractive body cue:** Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference latency. ...
- **p. 3 / Abstract - extractive body cue:** This Lcfg is combined with a Dispersive Loss (Ldisp) imposed on the UNet's hidden states to jointly optimize the network parameters. inference time due to ...
- **p. 1 / Abstract - extractive body cue:** However, generative models within this field face a fundamental trade-off between the slow, iterative sampling of diffusion models and the architectural constraints of faster Flow-based ...

## Design Rationale

- **p. 2 / Abstract - extractive body cue:** Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework.
- **p. 1 / Abstract - extractive body cue:** We validate our method on the Adroit and Meta-World benchmarks, as well as in real-world scenarios.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** Because subtle scene-context variations are critical for robot learning, especially in few-shot learning, we introduce a lightweight Dispersive Loss that repels state embeddings during training, ...
- **p. 4 / Abstract - extractive body cue:** This can lead to a form of "feature collapse", where the policy network maps distinct environmental states that demand fundamentally different actions to nearly identical ...
- **p. 3 / Abstract - extractive body cue:** MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D point clouds P ...
- **p. 4 / Abstract - extractive body cue:** Training Objective and Inference Our final training objective synergistically combines the trajectory generation and representation regularization goals: Ltotal(θ) = Lcfg(θ) + λLDisp(θ) (7) Here, Lcfg ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 2 / Abstract - extractive body cue:** Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference latency. ...
- **p. 3 / Abstract - extractive body cue:** This Lcfg is combined with a Dispersive Loss (Ldisp) imposed on the UNet's hidden states to jointly optimize the network parameters. inference time due to ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | Because subtle scene-context variations are critical for robot learning, especially in few-shot learning, we introduce a lightweight Dispersive Loss that repels state ... | p. 1 (Abstract), p. 4 (Abstract) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | This can lead to a form of "feature collapse", where the policy network maps distinct environmental states that demand fundamentally different actions ... | p. 4 (Abstract), p. 3 (Abstract) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D ... | p. 3 (Abstract), p. 4 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** However, generative models within this field face a fundamental trade-off between the slow, iterative sampling of diffusion models and the architectural constraints of faster Flow-based ...
- **p. 4 / Abstract - extractive body cue:** Dispersive Loss functions as a "contrastive loss without positive pairs"; the repulsive force is supplied by the loss itself, while the alignment of a state ...
- **p. 4 / Abstract - extractive body cue:** Enhancing Representational generalization with Dispersive Loss While the MeanFlow objective Lcfg excels at learning the temporal dynamics required to produce accurate output trajectories, it provides ...
- **p. 2 / Abstract - extractive body cue:** However, a purely regression-based objective fails to impose explicit regularization on the policy's internal feature space (Wang and He 2025).
- **p. 2 / Abstract - extractive body cue:** These methods greatly accelerate inference by optimizing the generative process, but they typically require additional consistency constraints on the model's outputs to ensure valid trajectories.
- **p. 3 / Abstract - extractive body cue:** This Lcfg is combined with a Dispersive Loss (Ldisp) imposed on the UNet's hidden states to jointly optimize the network parameters. inference time due to ...
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 4 (Abstract), p. 4 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | MP1, One-Step, Trajectory, Generation, context, robot, learning, policy, task, sequence, observations, including, point, clouds | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | MP1, One-Step, Trajectory, Generation, context, robot, learning, policy, task, sequence | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | contributions, follows, introduce, MP1, first, MeanFlow-based, robot, learning, framework, validate | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | However, generative, models, within, field, face, fundamental, trade-off, between, slow | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / Abstract - extractive body cue:** MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D point clouds P ...
- **p. 3 / Abstract - extractive body cue:** The MP1 takes the historical observation point cloud and the robot's state as inputs.
- **p. 4 / Abstract - extractive body cue:** This can lead to a form of "feature collapse", where the policy network maps distinct environmental states that demand fundamentally different actions to nearly identical ...
- **p. 4 / Abstract - extractive body cue:** Enhancing Representational generalization with Dispersive Loss While the MeanFlow objective Lcfg excels at learning the temporal dynamics required to produce accurate output trajectories, it provides ...
- **p. 2 / Abstract - extractive body cue:** Related Work 2D Input Robot Learning Most methods that utilize 2D visual input predict robot actions based on images.
- **p. 1 / Abstract - extractive body cue:** These methods have enhanced the ability of robots to understand and execute complex actions in response to multimodal inputs (Chi et al.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Since action generation requires multiple time steps to denoise, the inference process can be time-consuming, which may become a bottleneck in applications ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | All training and testing are performed on an NVIDIA RTX 4090 GPU, with a batch size of 128, optimization uses the AdamW ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | All training and testing are performed on an NVIDIA RTX 4090 GPU, with a batch size of 128, optimization uses the AdamW ... | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | All training and testing are performed on an NVIDIA RTX 4090 GPU, with a batch size of 128, optimization uses the AdamW ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** Because subtle scene-context variations are critical for robot learning, especially in few-shot learning, we introduce a lightweight Dispersive Loss that repels state embeddings during training, ...
- **p. 4 / Abstract - extractive body cue:** Training Objective and Inference Our final training objective synergistically combines the trajectory generation and representation regularization goals: Ltotal(θ) = Lcfg(θ) + λLDisp(θ) (7) Here, Lcfg ...
- **p. 2 / Abstract - extractive body cue:** Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference latency. ...
- **p. 3 / Abstract - extractive body cue:** This Lcfg is combined with a Dispersive Loss (Ldisp) imposed on the UNet's hidden states to jointly optimize the network parameters. inference time due to ...
- **p. 5 / Abstract - extractive body cue:** All training and testing are performed on an NVIDIA RTX 4090 GPU, with a batch size of 128, optimization uses the AdamW optimizer with a ...
- **p. 3 / Abstract - extractive body cue:** This Lcfg is combined with a Dispersive Loss (Ldisp) imposed on the UNet's hidden states to jointly optimize the network parameters. inference time due to ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Because, subtle, scene-context, variations, critical, robot, learning, especially, few-shot, introduce, lightweight, Dispersive, Loss, repels, state, embeddings, during, training, boosting, generalization.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and ... | p. 2 (Abstract), p. 7 (Abstract) |
| Policy fitting | MP1 is capable of one-step inference and, compared to state-of-the-art (SOTA) methods, improves the average success rate by 7.3% (Tab. | p. 2 (Abstract), p. 5 (Figure/Table caption) |
| Closed-loop rollout | Table 1: Performance of different methods on 37 Tasks. We evaluate the performance of our method on 3 Adroit and 34 Meta- ... | p. 5 (Figure/Table caption), p. 6 (Abstract) |

## Failure and Ablation Link

- **p. 6 / Abstract - extractive body cue:** 3 compares the standard MP1 with a variant in which the Dispersive Loss is removed.
- **p. 2 / Abstract - extractive body cue:** Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference latency. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: The effect of the number of demonstrations on dif- ferent methods. As the number increases, the success rate gradually improves. Task /
- **p. 7 / Abstract - extractive body cue:** 0 2 5 10 20 0 50 100 Success Rate (%) 0 18 19 81 82 0 12 14 66 79 Lever Pull MP1 FlowPolicy ...
- **p. 2 / Abstract - extractive body cue:** Acting as a contrastivestyle regularizer without positive pairs, it sharpens state discrimination while the original regression term still aligns each state to its expert trajectory.
- **p. 3 / Abstract - extractive body cue:** Furthermore, by encouraging the latent embeddings of different input states to disperse, we improve the model's generalization abilities and task success rate, all without sacrificing ...
- **p. 4 / Abstract - extractive body cue:** Specifically, we adopt the InfoNCE-based variant of Dispersive Loss (using ℓ2 distance, with temperature τ = 1) and apply it to the output features of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 4 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 1 (Abstract), p. 2 (Abstract), objective p. 1 (Abstract), p. 4 (Abstract), p. 4 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), temporal p. 1 (Abstract), p. 5 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
