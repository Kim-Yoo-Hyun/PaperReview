# Method - CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2601.09512; PDF retrieval source: https://arxiv.org/pdf/2601.09512. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY)): To achieve this, we draw inspiration from the mixture-of-experts (MoE) approach in large language models (LLMs) [35], [36], which combines the outputs of specialized sub-networks during inference.

## Method Body Digest

- **p. 3 / IV. METHODOLOGY - extractive PDF cue:** To achieve this, we draw inspiration from the mixture-of-experts (MoE) approach in large language models (LLMs) [35], [36], which combines the outputs of specialized sub-networks ...
- **p. 3 / IV. METHODOLOGY - extractive PDF cue:** Prior work [37], [38] has shown that a large fraction of factual associations and high-level knowledge in transformerbased LLMs is stored inside mid-layer feedforward network ...
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** By training the discriminators added at stage n with the loss Lrecon(Dn ℓ) = Exℓ∼Dn  en ℓ(xℓ)  , (5) we ensure they have ...
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** A straightforward approach would be to Task 1 Adapter Task 3 Adapter Task 1 Discriminator Task 2 Discriminator Task 3 Discriminator Pre-Trained Module z-score threshold ...
- **p. 5 / IV. METHODOLOGY - extractive PDF cue:** Then, the routing mechanism activates only adapters from earlier stages in layer ℓ1 during training of Ai ℓ2.
- **p. 5 / IV. METHODOLOGY - extractive PDF cue:** As a consequence, the input features xℓ2 to layer ℓ2 when performing task Tn are different from those seen during training of Ai ℓ2.
- **p. 3 / IV. METHODOLOGY - extractive PDF cue:** We adopt the standard conditional flow matching loss L(θn)= Es,(A1,o),A0
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** First, we jointly train the new adapters using the flow-matching loss (1).

## Design Rationale

- **p. 3 / IV. METHODOLOGY - extractive PDF cue:** As our method is architecture-agnostic, we keep the following sections general.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In a continual learning setting, where new tasks and ∗Equal contribution.
- **p. 5 / IV. METHODOLOGY - extractive PDF cue:** We found that introducing at least some new parameters per task is essential for the policy to acquire and retain novel skills.

## Source Evidence Cues

- **p. 3 / IV. METHODOLOGY - extractive PDF cue:** To achieve this, we draw inspiration from the mixture-of-experts (MoE) approach in large language models (LLMs) [35], [36], which combines the outputs of specialized sub-networks ...
- **p. 3 / IV. METHODOLOGY - extractive PDF cue:** Prior work [37], [38] has shown that a large fraction of factual associations and high-level knowledge in transformerbased LLMs is stored inside mid-layer feedforward network ...
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** By training the discriminators added at stage n with the loss Lrecon(Dn ℓ) = Exℓ∼Dn  en ℓ(xℓ)  , (5) we ensure they have ...
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** A straightforward approach would be to Task 1 Adapter Task 3 Adapter Task 1 Discriminator Task 2 Discriminator Task 3 Discriminator Pre-Trained Module z-score threshold ...
- **p. 5 / IV. METHODOLOGY - extractive PDF cue:** Then, the routing mechanism activates only adapters from earlier stages in layer ℓ1 during training of Ai ℓ2.
- **p. 5 / IV. METHODOLOGY - extractive PDF cue:** As a consequence, the input features xℓ2 to layer ℓ2 when performing task Tn are different from those seen during training of Ai ℓ2.
- **Detected method headings:** IV. METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | To achieve this, we draw inspiration from the mixture-of-experts (MoE) approach in large language models (LLMs) [35], [36], which combines the outputs ... | p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Prior work [37], [38] has shown that a large fraction of factual associations and high-level knowledge in transformerbased LLMs is stored inside ... | p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | By training the discriminators added at stage n with the loss Lrecon(Dn ℓ) = Exℓ∼Dn  en ℓ(xℓ)  , (5) we ... | p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / IV. METHODOLOGY - extractive PDF cue:** We adopt the standard conditional flow matching loss L(θn)= Es,(A1,o),A0
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** First, we jointly train the new adapters using the flow-matching loss (1).
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** Then, we freeze all parameters except for the new discriminators and train them using the reconstruction loss (5).
- **p. 5 / IV. METHODOLOGY - extractive PDF cue:** The auxiliary discriminator is linked to the same adapter as the existing discriminator with the smallest reconstruction error (4), i.e., Bℓ(Dn ℓ) = Ai ℓ= ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Train, layers, consisting, camera, images, INc, proprioceptive, state, language, command, generates, action, chunk, H-1 | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Train, layers, consisting, camera, images, INc, proprioceptive, state, language, command | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | architecture-agnostic, keep, following, sections, general, continual, learning, setting, where, tasks | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | adopt, standard, conditional, flow, matching, loss, First, jointly, train, adapters | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PROBLEM SETUP - extractive PDF cue:** 23: Train Dn ℓof all layers ℓ∈E from Dn via (5). consisting of camera images I1 t , . . . , INc t , ...
- **p. 2 / III. PROBLEM SETUP - extractive PDF cue:** We assume the availability of a base VLA policy π0 = πθ0 with model parameters θ0 that takes as input an observation ot = (I1 ...
- **p. 3 / III. PROBLEM SETUP - extractive PDF cue:** Specifically, given an expert demonstration dataset Dn = {(on t , an t ), ln}T t=1 of observation-action pairs for task Tn, we aim to ...
- **p. 2 / III. PROBLEM SETUP - extractive PDF cue:** A task Tn = (ρn 0, ln) is defined by an initial distribution of the state of the robot and the environment ρn 0 and ...
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** (3) Injecting adapters as parallel side branches to the model is beneficial as it preserves the network structure and does not change the input and ...
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** A straightforward approach would be to Task 1 Adapter Task 3 Adapter Task 1 Discriminator Task 2 Discriminator Task 3 Discriminator Pre-Trained Module z-score threshold ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Recent advances in vision-language-action models (VLAs) [5]-[8] have demonstrated strong performance on complex, long-horizon manipulation tasks by integrating perception, language understanding, and action generation within ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The first h ≤H actions in At are applied to the robot, and the policy generates a new chunk at timestep t+h ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The policy generates chunks of H = 16 end-effector displacement actions, and the first h = 8 actions are sent to a ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | This dynamic expansion strategy, illustrated in Figure 2, results in a memory-efficient, sublinear increase in the number of adapter parameters. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | The policy generates chunks of H = 16 end-effector displacement actions, and the first h = 8 actions are sent to a ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / IV. METHODOLOGY - extractive PDF cue:** To achieve this, we draw inspiration from the mixture-of-experts (MoE) approach in large language models (LLMs) [35], [36], which combines the outputs of specialized sub-networks ...
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** By training the discriminators added at stage n with the loss Lrecon(Dn ℓ) = Exℓ∼Dn  en ℓ(xℓ)  , (5) we ensure they have ...
- **p. 4 / IV. METHODOLOGY - extractive PDF cue:** A straightforward approach would be to Task 1 Adapter Task 3 Adapter Task 1 Discriminator Task 2 Discriminator Task 3 Discriminator Pre-Trained Module z-score threshold ...
- **p. 5 / IV. METHODOLOGY - extractive PDF cue:** Then, the routing mechanism activates only adapters from earlier stages in layer ℓ1 during training of Ai ℓ2.
- **p. 5 / IV. METHODOLOGY - extractive PDF cue:** As a consequence, the input features xℓ2 to layer ℓ2 when performing task Tn are different from those seen during training of Ai ℓ2.
- **p. 5 / IV. METHODOLOGY - extractive PDF cue:** Real Sim. # Params (linear proj.) 0.38M 3.2M 6.08M 1.4M # Params (AdaLN) 0.75M 0.26M 1.00M 0.33M Learning rate 2 × 10-4 1 × 10-4 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** achieve, draw, inspiration, mixture-of-experts, MoE, large, language, models, LLMs, combines, outputs, specialized, sub-networks, during, inference, Prior, fraction, factual, associations, high-level.
- **Relevant PDF headings:** IV. METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We pre-train the policy on a mix of 1000 demonstrations collected in our lab for tasks different from the five continual learning ... | p. 5 (V. EVALUATION), p. 5 (V. EVALUATION) |
| Action / skill decoding | 5) Baselines: We include seven baselines for continual learning without oracle task IDs. | p. 6 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Receding execution / feedback | Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates ... | p. 10 (Figure/Table caption), p. 6 (V. EVALUATION) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: CLARE autonomously and continually injects lightweight adapters into selected layers of a pre-trained vision-language-action model (VLA). During inference, the most relevant adapters are ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** 5) Baselines: We include seven baselines for continual learning without oracle task IDs.
- **p. 6 / V. EVALUATION - extractive PDF cue:** As an ablation, we also consider an encoder-decoder backbone (DiT-EncDec), for which adapters can be added to all 12 transformer layers.
- **p. 7 / V. EVALUATION - extractive PDF cue:** CLARE achieves the highest overall performance, as measured by AUC, and demonstrates strong capabilities to acquire new skills without forgetting. "NA" indicates not available.
- **p. 6 / V. EVALUATION - extractive PDF cue:** In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of 23%.
- **p. 7 / 5. LEGO - extractive PDF cue:** SeqFFT and SeqLoRA achieve high performance on new tasks, but cannot sufficiently retain the relevant representations from previous tasks.
- **p. 7 / V. EVALUATION - extractive PDF cue:** 5: Increasing the dynamic expansion threshold γ reduces the number of added adapters and, consequently, the capability to learn new tasks (lower FWT), but does ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), objective p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), temporal p. 3 (III. PROBLEM SETUP), p. 5 (V. EVALUATION), p. 3 (IV. METHODOLOGY), p. 5 (V. EVALUATION), p. 2 (III. PROBLEM SETUP), p. 4 (IV. METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
