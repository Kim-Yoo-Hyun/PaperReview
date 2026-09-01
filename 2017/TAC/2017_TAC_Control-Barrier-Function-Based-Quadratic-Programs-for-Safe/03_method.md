# Method - Control Barrier Function Based Quadratic Programs for Safety Critical Systems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1609.06408; PDF retrieval source: https://arxiv.org/pdf/1609.06408. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (I. INTRODUCTION), p. 2 (B. Contributions), p. 1 (Abstract), p. 7 (III. CONTROL BARRIER FUNCTIONS), p. 2 (B. Contributions), p. 6 (III. CONTROL BARRIER FUNCTIONS)): While it is tempting to decompose the problem into the design of a controller for each individual objective and then integrate the resulting controllers via software, the integration problem is ...

## Method Body Digest

- **p. 1 / I. INTRODUCTION - extractive body cue:** While it is tempting to decompose the problem into the design of a controller for each individual objective and then integrate the resulting controllers via ...
- **p. 2 / B. Contributions - extractive body cue:** The relations established for barrier functions then extend to control barrier functions. perspective allows for the consideration of multiple control objectives (expressed via multiple CLFs) ...
- **p. 1 / Abstract - extractive body cue:** As a means of creating a formal framework for controlling systems of this form, and with a view toward automotive applications, this paper develops a ...
- **p. 7 / III. CONTROL BARRIER FUNCTIONS - extractive body cue:** Then any locally Lipschitz continuous controller u : Int(C) →U such that u(x) ∈Krcbf(x) will render the set Int(C) forward invariant.
- **p. 2 / B. Contributions - extractive body cue:** The experimental realization of CLF inspired controllers on a bipedal robot resulted in the observation that, since CLF conditions are affine in torque, they can ...
- **p. 6 / III. CONTROL BARRIER FUNCTIONS - extractive body cue:** When the set Int(C) is not forward invariant under the natural dynamics of the system, ˙x = f(x), how can a controller be specified that ...
- **p. 3 / II. RECIPROCAL AND ZEROING BARRIER FUNCTIONS - extractive body cue:** For (8) to be an acceptable condition, we need to verify that its satisfaction guarantees that solutions to (1) stay in Int(C).
- **p. 1 / Abstract - extractive body cue:** Safety critical systems involve the tight coupling between potentially conflicting control objectives and safety constraints.

## Design Rationale

- **p. 2 / B. Contributions - extractive body cue:** Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in ...
- **p. 2 / B. Contributions - extractive body cue:** The first contribution of this paper is to formulate conditions on the derivative of a (reciprocal or zeroing) barrier function that are minimally restrictive on ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** More recently, barrier functions were used in the paper [4] to develop an interior penalty method for converting constrained optimal control methods into unconstrained ones1.

## Source Evidence Cues

- **p. 1 / I. INTRODUCTION - extractive body cue:** While it is tempting to decompose the problem into the design of a controller for each individual objective and then integrate the resulting controllers via ...
- **p. 2 / B. Contributions - extractive body cue:** The relations established for barrier functions then extend to control barrier functions. perspective allows for the consideration of multiple control objectives (expressed via multiple CLFs) ...
- **p. 1 / Abstract - extractive body cue:** As a means of creating a formal framework for controlling systems of this form, and with a view toward automotive applications, this paper develops a ...
- **p. 7 / III. CONTROL BARRIER FUNCTIONS - extractive body cue:** Then any locally Lipschitz continuous controller u : Int(C) →U such that u(x) ∈Krcbf(x) will render the set Int(C) forward invariant.
- **p. 2 / B. Contributions - extractive body cue:** The experimental realization of CLF inspired controllers on a bipedal robot resulted in the observation that, since CLF conditions are affine in torque, they can ...
- **p. 6 / III. CONTROL BARRIER FUNCTIONS - extractive body cue:** When the set Int(C) is not forward invariant under the natural dynamics of the system, ˙x = f(x), how can a controller be specified that ...
- **p. 3 / II. RECIPROCAL AND ZEROING BARRIER FUNCTIONS - extractive body cue:** For (8) to be an acceptable condition, we need to verify that its satisfaction guarantees that solutions to (1) stay in Int(C).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | While it is tempting to decompose the problem into the design of a controller for each individual objective and then integrate the ... | p. 1 (I. INTRODUCTION), p. 2 (B. Contributions) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | The relations established for barrier functions then extend to control barrier functions. perspective allows for the consideration of multiple control objectives (expressed ... | p. 2 (B. Contributions), p. 1 (Abstract) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | As a means of creating a formal framework for controlling systems of this form, and with a view toward automotive applications, this ... | p. 1 (Abstract), p. 7 (III. CONTROL BARRIER FUNCTIONS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** Safety critical systems involve the tight coupling between potentially conflicting control objectives and safety constraints.
- **p. 2 / B. Contributions - extractive body cue:** In particular, relaxation is used to make the stability objective a soft constraint on the QP, while safety is maintained as a hard constraint.
- **p. 2 / B. Contributions - extractive body cue:** Safety-critical control problems often include performance objectives, such as stabilization to a point or a surface, in addition to safety constraints.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, the approach developed here will pose a feedback design problem that mediates the safety and stabilization requirements, in the sense that safety is ...
- **p. 3 / B. Contributions - extractive body cue:** 3 conflict, such as when the desired cruising speed is faster than the speed of the leading car, while provably satisfying the safety-oriented constraints is ...
- **p. 7 / III. CONTROL BARRIER FUNCTIONS - extractive body cue:** Note that if U̸ = Rm, i.e., there are constraints on the input u, then the construction shown above for higher relative degree h may ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 2 (B. Contributions), p. 2 (B. Contributions), p. 1 (I. INTRODUCTION), p. 3 (B. Contributions), p. 7 (III. CONTROL BARRIER FUNCTIONS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Here, where, velocity, following, leading, vehicle, respectively, distance, between, vehicles, mass, f1vf, f2v2, aerodynamic | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Here, where, velocity, following, leading, vehicle, respectively, distance, between, vehicles | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Importantly, under, mild, conditions, demonstrated, necessary, sufficient, forward, invariance, result | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | Safety, critical, systems, involve, tight, coupling, between, potentially, conflicting, control | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 10 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** (43) Here, x = (x1, x2, x3) := (vf, vl, D) where vf and vl are the velocity of the following and leading vehicle (in ...
- **p. 13 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** The model parameters a, b, Cr, Iz and v0 are all positive, and hence the system is exponentially stable, and therefore input-to-state stable [41].
- **p. 10 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** Initially, we will suppose that the control input is unbounded, that is, U = R, and later, we address realistic bounds on wheel force.
- **p. 2 / B. Contributions - extractive body cue:** The latter condition may be somewhat surprising in view of the well-known Nagumo's Theorem, which states that for a system without inputs and a C1 ...
- **p. 11 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** 3) Force Constraints and CBFs: The QP formulated in subsection V-A2 generates a control input u ∈R for the ACCcontrolled vehicle.
- **p. 12 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** 1) Lane Keeping Problem Setup: Under the assumptions of constant longitudinal speed and a linear tire-force model, a two-state handling model can be augmented to ...
- **p. 12 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** In the model, the state is x := (y, ν, ψ, r), where y and ψ are the lateral displacement and the error yaw angle ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | As a means of creating a formal framework for controlling systems of this form, and with a view toward automotive applications, this ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Index Terms-Control Lyapunov function, Barrier function, Nonlinear control, Quadratic program, Safety, Set invariance | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / B. Contributions - extractive body cue:** The relations established for barrier functions then extend to control barrier functions. perspective allows for the consideration of multiple control objectives (expressed via multiple CLFs) ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** While, tempting, decompose, problem, design, controller, individual, objective, then, integrate, resulting, controllers, software, integration, being, simple, relations, established, barrier, functions.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | The parameters used for the simulation are given in Table I. | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS) |
| Filtering / recovery | Simulation results for ACC Various problem formulations are compared here. | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS) |
| Monitoring / re-entry | A video of the results is available on YouTube [57]. | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS) |

## Failure and Ablation Link

- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 3. The projection of CF onto the (y, ˙y)-plane is bounded by the upper and lower curves. The subset CLK ⊂Int(CF ) is bounded ...
- **p. 14 / VII. CONCLUSIONS - extractive body cue:** Future work will be devoted to building upon the foundations presented in this paper in the context of safety-critical control of cyber-physical systems, with a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (I. INTRODUCTION), p. 2 (B. Contributions), p. 1 (Abstract), p. 7 (III. CONTROL BARRIER FUNCTIONS), p. 2 (B. Contributions), p. 6 (III. CONTROL BARRIER FUNCTIONS), objective p. 1 (Abstract), p. 2 (B. Contributions), p. 2 (B. Contributions), p. 1 (I. INTRODUCTION), p. 3 (B. Contributions), p. 7 (III. CONTROL BARRIER FUNCTIONS), temporal p. 1 (Abstract), p. 1 (Abstract), p. 2 (B. Contributions), p. 2 (B. Contributions), p. 3 (II. RECIPROCAL AND ZEROING BARRIER FUNCTIONS), p. 3 (B. Contributions).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
