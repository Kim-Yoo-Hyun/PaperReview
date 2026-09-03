# Method - Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p071.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p071.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)), p. 3 (1) Teacher Model (EDM)), p. 5 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY), p. 5 (2) Student Model (Consistency Policy))): Single-step inference from our trained Consistency Policy works as follows: sample the initial position z ∼N(0, I), compute x = gθ(z, T, 0; o) where T is the max timestep ...

## Method Body Digest

- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** Single-step inference from our trained Consistency Policy works as follows: sample the initial position z ∼N(0, I), compute x = gθ(z, T, 0; o) where ...
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** [14] propose a training objective to distill a teacher model sϕ(xt, t; o) into a student model gθ(xt, t, s; o) and achieve state of ...
- **p. 3 / 1) Teacher Model (EDM) - extractive body cue:** A trained EDM model takes as input the current position xt and time t along a PFODE, as well as the conditioning o, and is ...
- **p. 5 / 2) Student Model (Consistency Policy) - extractive body cue:** For our student model, we use the same architecture except with expanded FiLM blocks to accomodate conditioning on the stop timestep, s.
- **p. 3 / III. CONSISTENCY POLICY - extractive body cue:** We then describe how to train a Consistency Policy, which requires training a teacher Diffusion Policy and then distilling this teacher model into a Consistency ...
- **p. 5 / 2) Student Model (Consistency Policy) - extractive body cue:** To this end, we also maintain the 1D Convolutional UNet architecture from Diffusion Policy for our teacher model.
- **p. 3 / 1) Teacher Model (EDM) - extractive body cue:** Following [13], we optimize the Denoising Score Matching (DSM) loss to train the EDM model: LDSM(θ) = Et,x0,xt/x0[d(x0, sϕ (xt, t; o))] (3) The DSM ...
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** 2, gradients from the loss are only calculated with respect to the operation from t →s (blue).

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, we demonstrate that inference speed of our approach is on average about an order of magnitude faster than the fastest baseline (see Table I) ...

## Source Evidence Cues

- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** Single-step inference from our trained Consistency Policy works as follows: sample the initial position z ∼N(0, I), compute x = gθ(z, T, 0; o) where ...
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** [14] propose a training objective to distill a teacher model sϕ(xt, t; o) into a student model gθ(xt, t, s; o) and achieve state of ...
- **p. 3 / 1) Teacher Model (EDM) - extractive body cue:** A trained EDM model takes as input the current position xt and time t along a PFODE, as well as the conditioning o, and is ...
- **p. 5 / 2) Student Model (Consistency Policy) - extractive body cue:** For our student model, we use the same architecture except with expanded FiLM blocks to accomodate conditioning on the stop timestep, s.
- **p. 3 / III. CONSISTENCY POLICY - extractive body cue:** We then describe how to train a Consistency Policy, which requires training a teacher Diffusion Policy and then distilling this teacher model into a Consistency ...
- **p. 5 / 2) Student Model (Consistency Policy) - extractive body cue:** To this end, we also maintain the 1D Convolutional UNet architecture from Diffusion Policy for our teacher model.
- **Detected method headings:** III. CONSISTENCY POLICY (p. 3); 1) Teacher Model (EDM) (p. 3); 2) Student Model (Consistency Policy) (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Single-step inference from our trained Consistency Policy works as follows: sample the initial position z ∼N(0, I), compute x = gθ(z, T, ... | p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | [14] propose a training objective to distill a teacher model sϕ(xt, t; o) into a student model gθ(xt, t, s; o) and ... | p. 4 (2) Student Model (Consistency Policy)), p. 3 (1) Teacher Model (EDM)) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | A trained EDM model takes as input the current position xt and time t along a PFODE, as well as the conditioning ... | p. 3 (1) Teacher Model (EDM)), p. 5 (2) Student Model (Consistency Policy)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1) Teacher Model (EDM) - extractive body cue:** Following [13], we optimize the Denoising Score Matching (DSM) loss to train the EDM model: LDSM(θ) = Et,x0,xt/x0[d(x0, sϕ (xt, t; o))] (3) The DSM ...
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** 2, gradients from the loss are only calculated with respect to the operation from t →s (blue).
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** The student model is trained using a combination of two objectives: the DSM loss (see Eq 3) and the CTM loss [14], which we now ...
- **p. 3 / III. CONSISTENCY POLICY - extractive body cue:** The gradient of the noised probability distribution, ∇log pt (xt/o), is known as the score.
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 3 (1) Teacher Model (EDM)), p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | figure, distributions, predicted, action, sequences, indicated, green, dots, different, stages, respective, generation, process, Diffusion | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | figure, distributions, predicted, action, sequences, indicated, green, dots, different, stages | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | Overall, demonstrate, inference, speed, average, about, order, magnitude, faster, fastest | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Following, optimize, Denoising, Score, Matching, DSM, loss, train, EDM, model | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** The figure shows distributions of predicted action sequences (indicated by the sequences of red to green dots) at different stages of the respective generation process. ...
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** Single-step inference from our trained Consistency Policy works as follows: sample the initial position z ∼N(0, I), compute x = gθ(z, T, 0; o) where ...
- **p. 3 / III. CONSISTENCY POLICY - extractive body cue:** Our diffusion models learn to map random actions xT sampled from the unit Gaussian N(0, I) to specific actions x0 drawn from the expert action ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Diffusion models produce outputs by sequentially denoising from an initial, noisy state.
- **p. 3 / III. CONSISTENCY POLICY - extractive body cue:** A fully denoised action is the policy's prediction of the expert action.
- **p. 5 / 2) Student Model (Consistency Policy) - extractive body cue:** This architecture conditions on observations and the diffusion timestep t using FiLM blocks, and diffuses through the action domain using 1D convolutional blocks.
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** [14] propose a training objective to distill a teacher model sϕ(xt, t; o) into a student model gθ(xt, t, s; o) and achieve state of ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | Given chaining timesteps {t1, t2}, we denoise from T →0 as usual, then noise to time t1, denoise back to time 0, ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | Specifically, we take as input two frames of observations (including wrist camera image and third person view camera image, and end effector ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | Policy NFE Inference Time (ms) DDPM 100 110 DDiM 15 11 CP (ours) 1 1 CP (ours) 3 2 Table III: Simulation ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** Single-step inference from our trained Consistency Policy works as follows: sample the initial position z ∼N(0, I), compute x = gθ(z, T, 0; o) where ...
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** [14] propose a training objective to distill a teacher model sϕ(xt, t; o) into a student model gθ(xt, t, s; o) and achieve state of ...
- **p. 3 / 1) Teacher Model (EDM) - extractive body cue:** A trained EDM model takes as input the current position xt and time t along a PFODE, as well as the conditioning o, and is ...
- **p. 3 / III. CONSISTENCY POLICY - extractive body cue:** We then describe how to train a Consistency Policy, which requires training a teacher Diffusion Policy and then distilling this teacher model into a Consistency ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Policy NFE Inference Time (ms) DDPM 100 110 DDiM 15 11 CP (ours) 1 1 CP (ours) 3 2 Table III: Simulation Inference Speeds - ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** We also report inference time on the 3070 Ti GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Single-step, inference, trained, Consistency, Policy, works, follows, sample, initial, position, compute, where, timestep, during, training, current, observation, deploy, action, environment.
- **Relevant PDF headings:** III. CONSISTENCY POLICY (p. 3); 1) Teacher Model (EDM) (p. 3); 2) Student Model (Consistency Policy) (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | 1) Robomimic: From the robomimic [17] benchmark suite, we evaluate our method on the Lift, Can, Square and Tool Hang tasks, which ... | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Coverage / augmentation | Thus, we construct an optimistically strong baseline by assuming these speedups can be realized without degrading performance from the standard sequential samplers. | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Downstream learning interface | This divergence can be explained by stochasticity on an easy task: if the first CP generation is already earning .98 success rate, ... | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Finally, we perform ablations over our core design choices and explore the intricacies of our model.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Thus, we construct an optimistically strong baseline by assuming these speedups can be realized without degrading performance from the standard sequential samplers.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Ablations We perform several ablations to validate and explore our design choices.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Thus, we choose as our baseline method the faster and more realistic DDiM variant of Diffusion Policy, which uses 15 steps for policy inference.
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** In our ablation (see Table V) comparing all three objectives, we vary the consistency objective but maintain the auxillary DSM objective as in Eq.
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** As in other ablations, we think the benefit of this choice is most apparent on harder tasks such as Tool Hang where there is more ...
- **p. 9 / IV. EXPERIMENTS - extractive body cue:** As an initial step towards exploring this hypothesis, we removed dropout from only the two generations from s →0 at training time while retaining it ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)), p. 3 (1) Teacher Model (EDM)), p. 5 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY), p. 5 (2) Student Model (Consistency Policy)), objective p. 3 (1) Teacher Model (EDM)), p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY), temporal p. 4 (2) Student Model (Consistency Policy)), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 9 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Single-step inference from our trained Consistency Policy works as follows: sample the initial position z ∼N(0, I), compute x = gθ(z, T, 0; o) where T is the max timestep ... (p. 4, 2) Student Model (Consistency Policy)).
- **Objective/update evidence:** Following [13], we optimize the Denoising Score Matching (DSM) loss to train the EDM model: LDSM(θ) = Et,x0,xt/x0[d(x0, sϕ (xt, t; o))] (3) The DSM objective takes a sampled point ... (p. 3, 1) Teacher Model (EDM)).
- **Temporal/runtime evidence:** Specifically, we take as input two frames of observations (including wrist camera image and third person view camera image, and end effector pose) and output a sequence of end effector ... (p. 5, IV. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
