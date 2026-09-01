# Method - DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.06949; PDF retrieval source: https://arxiv.org/abs/2602.06949. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (3.3.1. Model Architecture), p. 7 (3.3.2. Pretraining from Human Videos), p. 5 (3.3.1. Model Architecture), p. 6 (3.3.1. Model Architecture), p. 7 (3.3.2. Pretraining from Human Videos), p. 8 (3.3.4. Distillation)): DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos x1 x2 Latent Action Encoder Latent Action Decoder ât ft ft+1 ft+1 ft+1 ft+1 ft+1 ft+1 ft ft ft ft ...

## Method Body Digest

- **p. 6 / 3.3.1. Model Architecture - extractive body cue:** DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos x1 x2 Latent Action Encoder Latent Action Decoder ât ft ft+1 ft+1 ft+1 ft+1 ft+1 ...
- **p. 7 / 3.3.2. Pretraining from Human Videos - extractive body cue:** We establish a latent action model as a VAE (Kingma and Welling, 2013) using the spatiotemporal Transformer architecture (Bruce et al., 2024).
- **p. 5 / 3.3.1. Model Architecture - extractive body cue:** To realize precise action following, we propose two improvements based on the original architecture.
- **p. 6 / 3.3.1. Model Architecture - extractive body cue:** [Left]: The information bottleneck design of our latent action model enforces action disentanglement, producing a continuous latent vector that represents actions between frames.
- **p. 7 / 3.3.2. Pretraining from Human Videos - extractive body cue:** The last layer of the action MLP is initialized with zeros to avoid perturbing the pretrained model state at the beginning of training (Zhang et ...
- **p. 8 / 3.3.4. Distillation - extractive body cue:** However, existing video diffusion models are often limited in achieving this due to (1) their bidirectional attention architecture, which defines a fixed horizon length, and ...
- **p. 3 / 3.1. Overview - extractive body cue:** 3.2, and then describe the architecture of DreamDojo and its training recipe in Sec.
- **p. 8 / 3.3.4. Distillation - extractive body cue:** To supervise the student's prediction, we randomly select a window of size 𝑁, which receives gradients via the ℒdistill loss (Eq.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** By scaling up human videos and introducing continuous latent actions as unified proxy, we present DreamDojo, the first world model of its kind that shows ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce DreamDojo, a foundation world model for open-world dexterous robot tasks.
- **p. 3 / 3.1. Overview - extractive body cue:** Our whole training procedure consists of three phases: 3

## Source Evidence Cues

- **p. 6 / 3.3.1. Model Architecture - extractive body cue:** DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos x1 x2 Latent Action Encoder Latent Action Decoder ât ft ft+1 ft+1 ft+1 ft+1 ft+1 ...
- **p. 7 / 3.3.2. Pretraining from Human Videos - extractive body cue:** We establish a latent action model as a VAE (Kingma and Welling, 2013) using the spatiotemporal Transformer architecture (Bruce et al., 2024).
- **p. 5 / 3.3.1. Model Architecture - extractive body cue:** To realize precise action following, we propose two improvements based on the original architecture.
- **p. 6 / 3.3.1. Model Architecture - extractive body cue:** [Left]: The information bottleneck design of our latent action model enforces action disentanglement, producing a continuous latent vector that represents actions between frames.
- **p. 7 / 3.3.2. Pretraining from Human Videos - extractive body cue:** The last layer of the action MLP is initialized with zeros to avoid perturbing the pretrained model state at the beginning of training (Zhang et ...
- **p. 8 / 3.3.4. Distillation - extractive body cue:** However, existing video diffusion models are often limited in achieving this due to (1) their bidirectional attention architecture, which defines a fixed horizon length, and ...
- **p. 3 / 3.1. Overview - extractive body cue:** 3.2, and then describe the architecture of DreamDojo and its training recipe in Sec.
- **Detected method headings:** 3. Approach (p. 3); 3.3. DreamDojo Foundation World Model (p. 5); 3.3.1. Model Architecture (p. 5); 0.219 Method (p. 10)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos x1 x2 Latent Action Encoder Latent Action Decoder ât ft ft+1 ft+1 ... | p. 6 (3.3.1. Model Architecture), p. 7 (3.3.2. Pretraining from Human Videos) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | We establish a latent action model as a VAE (Kingma and Welling, 2013) using the spatiotemporal Transformer architecture (Bruce et al., 2024). | p. 7 (3.3.2. Pretraining from Human Videos), p. 5 (3.3.1. Model Architecture) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | To realize precise action following, we propose two improvements based on the original architecture. | p. 5 (3.3.1. Model Architecture), p. 6 (3.3.1. Model Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 3.3.4. Distillation - extractive body cue:** To supervise the student's prediction, we randomly select a window of size 𝑁, which receives gradients via the ℒdistill loss (Eq.
- **p. 8 / 3.3.4. Distillation - extractive body cue:** (7) Computing the loss in this form is intractable, but we can directly compute its gradient, using real and fake diffusion models 𝑠real and 𝑠fake ...
- **p. 7 / 3.3.2. Pretraining from Human Videos - extractive body cue:** Therefore, our final training objective becomes: ℒfinal(𝜃) = ℒflow(𝜃) + 𝜆ℒtemporal(𝜃), (5) where 𝜆> 0 is a trade-off coefficient to balance the optimization.
- **p. 7 / 3.3.2. Pretraining from Human Videos - extractive body cue:** 2, Cosmos-Predict2.5 employs the standard flow matching loss (Eq.
- **p. 4 / 3.2. DreamDojo-HV Dataset - extractive body cue:** However, this may not be the most efficient approach to encompass all potential interaction types, as each new trajectory involves costly teleoperation.
- **p. 6 / 3.3.2. Pretraining from Human Videos - extractive body cue:** Nevertheless, since world models must learn the consequences of actions, relying solely on actionless videos may lead to an inadequate understanding of the causality, ultimately ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 8 (3.3.4. Distillation), p. 8 (3.3.4. Distillation), p. 7 (3.3.2. Pretraining from Human Videos), p. 7 (3.3.2. Pretraining from Human Videos).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, instead, absolute, robot, joint, poses, transform, them, relative, actions, rebaselining, inputs, pose, beginning | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | First, instead, absolute, robot, joint, poses, transform, them, relative, actions | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | scaling, human, videos, introducing, continuous, latent, actions, unified, proxy, present | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | supervise, student, prediction, randomly, select, window, size, receives, gradients, distill | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.3.1. Model Architecture - extractive body cue:** First, instead of using the absolute robot joint poses, we transform them into relative actions by rebaselining the inputs with the pose at the beginning ...
- **p. 2 / 1. Introduction - extractive body cue:** Naively training on passive videos overlooks the causality between video observations and actions, leading to inferior knowledge transfer for action-conditioned world simulation.
- **p. 3 / 2. Preliminary - extractive body cue:** The objective of an interactive world model is to infer future states based on actions.
- **p. 3 / 2. Preliminary - extractive body cue:** Formally, given an action 𝑎∈𝒜, the interactive world model acts as a state transition function that samples the next state: 𝑠𝑡+1 ∼𝑝(·/𝑠𝑡, 𝑎𝑡), (1) where ...
- **p. 5 / 3.3.1. Model Architecture - extractive body cue:** Different from interactive games with discrete inputs (Parker-Holder et al., 2024), achieving genuine controllability for robot actions presents more challenges due to its high dimensionality ...
- **p. 7 / 3.3.2. Pretraining from Human Videos - extractive body cue:** The last layer of the action MLP is initialized with zeros to avoid perturbing the pretrained model state at the beginning of training (Zhang et ...
- **p. 7 / 3.3.3. Post-Training on Target Robots - extractive body cue:** Although learning from human videos exposes the model to a wide range of physics interactions, we still require a post-training stage on the target robot ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Our distilled model is significantly faster, able to inference at real-time 10.81 FPS with minor degradation in long-horizon rollouts and performance close ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | The value prediction module is trained to estimate the number of time steps remaining until each subtask boundary, which is defined as ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Our distilled model is significantly faster, able to inference at real-time 10.81 FPS with minor degradation in long-horizon rollouts and performance close ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3.3.2. Pretraining from Human Videos - extractive body cue:** The last layer of the action MLP is initialized with zeros to avoid perturbing the pretrained model state at the beginning of training (Zhang et ...
- **p. 8 / 3.3.4. Distillation - extractive body cue:** However, existing video diffusion models are often limited in achieving this due to (1) their bidirectional attention architecture, which defines a fixed horizon length, and ...
- **p. 3 / 3.1. Overview - extractive body cue:** 3.2, and then describe the architecture of DreamDojo and its training recipe in Sec.
- **p. 9 / 4.1. Experimental Setup - extractive body cue:** By default, post-training is conducted with 128 NVIDIA H100 GPUs for 50k steps with a batch size of 512.
- **p. 9 / 4.1. Experimental Setup - extractive body cue:** Both models are pretrained for 140k steps with an effective batch size of 1024 using 256 NVIDIA H100 GPUs.
- **p. 13 / 4.7. Downstream Applications - extractive body cue:** We ensemble 5 model checkpoints from training to generate action proposals that exhibit sufficient variance at inference time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** DreamDojo, Generalist, Robot, World, Model, Large-Scale, Human, Videos, Latent, Action, Encoder, Decoder, Figure, establish, VAE, Kingma, Welling, spatiotemporal, Transformer, architecture.
- **Relevant PDF headings:** 3. Approach (p. 3); 3.3. DreamDojo Foundation World Model (p. 5); 3.3.1. Model Architecture (p. 5); 0.219 Method (p. 10).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | Our curated data mixture excels in both scale and diversity, encompassing 15× longer duration, 96× more skills, and 2,000× more scenes than ... | p. 5 (3.2. DreamDojo-HV Dataset), p. 9 (4. Experiments) |
| Filtering / recovery | Table 7: Generalization ability after distillation. Thanks to our strong pretraining, DreamDojo shows consistently better generalization than the baseline after distillation. Lastly, ... | p. 13 (Figure/Table caption), p. 8 (4. Experiments) |
| Monitoring / re-entry | Table 7: Generalization ability after distillation. Thanks to our strong pretraining, DreamDojo shows consistently better generalization than the baseline after distillation. Lastly, ... | p. 13 (Figure/Table caption), p. 14 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 10 / 0.219 Method - extractive body cue:** When evaluating the models without distillation, we generate 100 future videos over three rounds by autoregressively resetting the condition frame with the last prediction to ...
- **p. 11 / 4.3. Effects of Different Data Mixtures - extractive body cue:** Unlike our final models, the sampling ratio is uniform across each dataset for the model variants in this ablation study.
- **p. 11 / 4.2. Effects of Different Action Conditions - extractive body cue:** Pretraining with latent actions can reach a much higher upper bound than action-free pretraining and without pretraining.
- **p. 12 / 4.4. Generalization to Unseen Scenarios - extractive body cue:** To benchmark the generalization ability in unseen scenarios, we generate video samples using the two final models, DreamDojo-2B and DreamDojo-14B, and conduct evaluations with Cosmos-Predict2.5 ...
- **p. 13 / 4.6. Benefits of Distillation - extractive body cue:** 7, evaluating the distillation results of a teacher pretrained on human videos versus one without pretraining (Cosmos-Predict2.5).
- **p. 12 / Figure/Table caption - extractive body cue:** Table 5: Ablations of architecture and loss designs. Our design choices can effectively enhance the simulation quality of both expert and counterfactual trajectories.
- **p. 8 / 4. Experiments - extractive body cue:** Specifically, we aim to answer the following questions: (1) Compared to actionless pretraining, can latent actions enable more effective transfer from human videos?

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (3.3.1. Model Architecture), p. 7 (3.3.2. Pretraining from Human Videos), p. 5 (3.3.1. Model Architecture), p. 6 (3.3.1. Model Architecture), p. 7 (3.3.2. Pretraining from Human Videos), p. 8 (3.3.4. Distillation), objective p. 8 (3.3.4. Distillation), p. 8 (3.3.4. Distillation), p. 7 (3.3.2. Pretraining from Human Videos), p. 7 (3.3.2. Pretraining from Human Videos), p. 4 (3.2. DreamDojo-HV Dataset), p. 6 (3.3.2. Pretraining from Human Videos), temporal p. 13 (4.6. Benefits of Distillation), p. 20 (5. Conclusion), p. 2 (1. Introduction), p. 9 (4.1. Experimental Setup), p. 9 (4.1. Experimental Setup), p. 10 (0.219 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
