# Method - Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=mIeKe74W43; PDF retrieval source: https://arxiv.org/pdf/2602.13810. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD)): First, we introduce the mean velocity policy (MVP), showing how its integration with a "generateand-select" mechanism enables a direct mapping from noise to optimal actions.

## Method Body Digest

- **p. 3 / 3 METHOD - extractive body cue:** First, we introduce the mean velocity policy (MVP), showing how its integration with a "generateand-select" mechanism enables a direct mapping from noise to optimal actions.
- **p. 5 / 3 METHOD - extractive body cue:** Inspired by this, we introduce the instantaneous velocity constraint (IVC), a training objective that explicitly enforces a boundary condition at t.
- **p. 4 / 3 METHOD - extractive body cue:** The resulting action, a⋆, then serves three purposes: (1) interacting with the environment, (2) acting as the target action for policy training, and (3) calculating ...
- **p. 6 / 3 METHOD - extractive body cue:** The policy training loss Lpolicy combines the mean velocity model loss in Eq.
- **p. 4 / 3 METHOD - extractive body cue:** In practice, at any given state s, the agent first generate N diverse candidate actions as ai = ai k(1) = ϵi + uθ(ϵi, 0, ...
- **p. 3 / 3 METHOD - extractive body cue:** In RL, a policy π(·/s) defines a distribution over actions given a state s.
- **p. 6 / 3 METHOD - extractive body cue:** (20) end for ▷Phase 2: Online Interaction and Fine-tuning for online training step k = 1, 2, . . . do Observe sk, execute a∗ ...
- **p. 4 / 3 METHOD - extractive body cue:** Let θ denote the learnable parameters, the training objective is to minimize the residual of the mean flow identity in Eq.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized threefold: • We propose a new flow-based policy, namely mean velocity policy (MVP), that enables fastest one-step action generation.
- **p. 3 / 3 METHOD - extractive body cue:** First, we introduce the mean velocity policy (MVP), showing how its integration with a "generateand-select" mechanism enables a direct mapping from noise to optimal actions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose the mean velocity policy (MVP) as an affirmative answer.

## Source Evidence Cues

- **p. 3 / 3 METHOD - extractive body cue:** First, we introduce the mean velocity policy (MVP), showing how its integration with a "generateand-select" mechanism enables a direct mapping from noise to optimal actions.
- **p. 5 / 3 METHOD - extractive body cue:** Inspired by this, we introduce the instantaneous velocity constraint (IVC), a training objective that explicitly enforces a boundary condition at t.
- **p. 4 / 3 METHOD - extractive body cue:** The resulting action, a⋆, then serves three purposes: (1) interacting with the environment, (2) acting as the target action for policy training, and (3) calculating ...
- **p. 6 / 3 METHOD - extractive body cue:** The policy training loss Lpolicy combines the mean velocity model loss in Eq.
- **p. 4 / 3 METHOD - extractive body cue:** In practice, at any given state s, the agent first generate N diverse candidate actions as ai = ai k(1) = ϵi + uθ(ϵi, 0, ...
- **p. 3 / 3 METHOD - extractive body cue:** In RL, a policy π(·/s) defines a distribution over actions given a state s.
- **p. 6 / 3 METHOD - extractive body cue:** (20) end for ▷Phase 2: Online Interaction and Fine-tuning for online training step k = 1, 2, . . . do Observe sk, execute a∗ ...
- **Detected method headings:** 3 METHOD (p. 3); A THEORETICAL ANALYSIS ON THE MEAN VELOCITY POLICY IMPROVEMENT (p. 14); A.1 IMPLEMENTATION PROCEDURES OF POLICY UPDATE (p. 14); A.3 PROOF OF THE MEAN VELOCITY POLICY IMPROVEMENT THEOREM (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | First, we introduce the mean velocity policy (MVP), showing how its integration with a "generateand-select" mechanism enables a direct mapping from noise ... | p. 3 (3 METHOD), p. 5 (3 METHOD) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | Inspired by this, we introduce the instantaneous velocity constraint (IVC), a training objective that explicitly enforces a boundary condition at t. | p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | The resulting action, a⋆, then serves three purposes: (1) interacting with the environment, (2) acting as the target action for policy training, ... | p. 4 (3 METHOD), p. 6 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 METHOD - extractive body cue:** Let θ denote the learnable parameters, the training objective is to minimize the residual of the mean flow identity in Eq.
- **p. 5 / 3 METHOD - extractive body cue:** Because the LMF loss is blind to the boundary, it cannot provide a gradient to force C(a, r) to zero.
- **p. 5 / 3 METHOD - extractive body cue:** Minimizing the IVC loss, LIVC = E[∥∆v∥2], forces the integration constant C(a, r) in Theorem 2 to zero.
- **p. 6 / 3 METHOD - extractive body cue:** (19) Update critic Qϕ by minimizing LQ(ϕ) with Eq.
- **p. 6 / 3 METHOD - extractive body cue:** To keep the IVC loss finite, the optimization must prevent this divergence, which requires C(a, r) = 0.
- **p. 3 / 3 METHOD - extractive body cue:** We then present the instantaneous velocity constraint (IVC) and theoretically justify its role in improving the learning accuracy.
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 5 (3 METHOD), p. 5 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | standard, flow-based, policies, mapping, framed, generative, process, velocity, model, transforms, Gaussian, noise, source, optimal | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | standard, flow-based, policies, mapping, framed, generative, process, velocity, model, transforms | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | contributions, summarized, threefold, flow-based, policy, namely, mean, velocity, MVP, enables | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Let, denote, learnable, parameters, training, objective, minimize, residual, mean, flow | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 METHOD - extractive body cue:** For standard flow-based policies, this mapping is framed as a generative process: a velocity model, v(a(t), t, s), transforms a standard Gaussian noise (source) into ...
- **p. 2 / 2 PRELIMINARIES - extractive body cue:** (1) Grounded in the off-policy learning paradigm, our approach utilizes an action-value function (Qfunction) to guide policy improvement, which denotes the expected cumulative return for ...
- **p. 3 / 3 METHOD - extractive body cue:** In RL, a policy π(·/s) defines a distribution over actions given a state s.
- **p. 4 / 3 METHOD - extractive body cue:** (11) Then the critic function Qϕ parameterized by ϕ is employed to evaluate all candidates, and the action yielding the highest Q-value is identified as ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized threefold: • We propose a new flow-based policy, namely mean velocity policy (MVP), that enables fastest one-step action generation.
- **p. 4 / 3 METHOD - extractive body cue:** The resulting action, a⋆, then serves three purposes: (1) interacting with the environment, (2) acting as the target action for policy training, and (3) calculating ...
- **p. 6 / 3 METHOD - extractive body cue:** Algorithm 1 Mean Flow RL Input: mean velocity policy πθ, where θ is the parameters of uθ, Critic Qϕ, offline dataset Doffline Initialize replay buffer ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | (20) end for ▷Phase 2: Online Interaction and Fine-tuning for online training step k = 1, 2, . . . do Observe ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | This result highlights its strong capability that is competitive with multi-step flow policies in solving long-horizon, sparse-reward tasks. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success Rate (a) Robomimic-lift 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 METHOD - extractive body cue:** Inspired by this, we introduce the instantaneous velocity constraint (IVC), a training objective that explicitly enforces a boundary condition at t.
- **p. 4 / 3 METHOD - extractive body cue:** The resulting action, a⋆, then serves three purposes: (1) interacting with the environment, (2) acting as the target action for policy training, and (3) calculating ...
- **p. 6 / 3 METHOD - extractive body cue:** The policy training loss Lpolicy combines the mean velocity model loss in Eq.
- **p. 6 / 3 METHOD - extractive body cue:** (20) end for ▷Phase 2: Online Interaction and Fine-tuning for online training step k = 1, 2, . . . do Observe sk, execute a∗ ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** (3) Training and inference time analysis.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The results are listed in Table 3. our MVP and FQL exhibit very similar inference times, with both approaches being significantly faster than BFN and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, introduce, mean, velocity, policy, MVP, showing, integration, generateand-select, mechanism, enables, direct, mapping, noise, optimal, actions, Inspired, instantaneous, constraint, IVC.
- **Relevant PDF headings:** 3 METHOD (p. 3); A THEORETICAL ANALYSIS ON THE MEAN VELOCITY POLICY IMPROVEMENT (p. 14); A.1 IMPLEMENTATION PROCEDURES OF POLICY UPDATE (p. 14); A.3 PROOF OF THE MEAN VELOCITY POLICY IMPROVEMENT THEOREM (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | We consider a total of 9 sparse-reward robotic manipulation tasks with varying difficulties. | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Coverage / augmentation | Figure 4: Training curves of ablation on the IVC. (2) Comparison with one-step variants of the aforementioned baselines. We compared our MVP ... | p. 8 (Figure/Table caption), p. 7 (4 EXPERIMENTS) |
| Downstream learning interface | Specifically, MVP consistently outperforms all baselines on Robomimic-square, Cube-doubletask4, and all Cube-triple tasks, where it consistently achieves the highest success rates. | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Our full version (λ = 1.0) was compared against variants with a reduced constraint (λ = 0.5) and without the constraint (λ = 0.0).
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Training curves of ablation on the IVC. (2) Comparison with one-step variants of the aforementioned baselines. We compared our MVP against one-step variants ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** To simulate a more realistic deployment scenario without hardware acceleration, we disabled JAX's Just-In-Time (JIT) compilation during all evaluations.
- **p. 18 / Figure/Table caption - extractive body cue:** Table 4: Ablation on the impact of IVC. Task MVP (λ = 0.0) MVP (λ = 0.5) MVP (λ = 1.0) Cube-triple-task3 0.65 ± 0.05 ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at a ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The poor performance of BFN and QC is primarily because they rely on a 10-step flow policy, which requires iterative computation to transform noise into ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD), objective p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 3 (3 METHOD), temporal p. 6 (3 METHOD), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 1 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
