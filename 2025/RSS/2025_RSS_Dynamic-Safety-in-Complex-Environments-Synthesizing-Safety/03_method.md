# Method - Dynamic Safety in Complex Environments: Synthesizing Safety Filters with Poisson's Equation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p137.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p137.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1. IyrRopUCTION), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach), p. 2 (1. IyrRopUCTION), p. 4 (IV. FORCING FUNCTION CONSTRUCTION)): The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) we illustrate and prove how ...

## Method Body Digest

- **p. 2 / 1. IyrRopUCTION - extractive body cue:** The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** However. the condition V-v(y) <0 may not necessarily hold for all y < ©, which is sufficient to guarantee h(y) > 0 in 2. ‘To ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to ...
- **p. 2 / 1. IyrRopUCTION - extractive body cue:** We propose several methods for constructing the forcing function within Poisson's equation, including an average flux method and a guidance field method {26} that provides ...
- **p. 4 / IV. FORCING FUNCTION CONSTRUCTION - extractive body cue:** In this section, we present methods of designing forcing functions that ensure the solution to the boundary value problem for Poisson's equation (16) is a ...
- **p. 5 / B. Indirect Assignment - Variational Approach - extractive body cue:** Specifically, let h be the minimizer of the cost functional:
- **p. 5 / B. Indirect Assignment - Variational Approach - extractive body cue:** A twice differentiable minimizer of (24), h € C?(Q), satisfies the associated Euler-Lagrange equation, given by:
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** We obtain a smooth guidance field by solving Laplace's equation-the homogenous version ‘of Poisson's equation.

## Design Rationale

- **p. 2 / 1. IyrRopUCTION - extractive body cue:** The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** However. the condition V-v(y) <0 may not necessarily hold for all y < ©, which is sufficient to guarantee h(y) > 0 in 2. ‘To ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to ...

## Source Evidence Cues

- **p. 2 / 1. IyrRopUCTION - extractive body cue:** The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** However. the condition V-v(y) <0 may not necessarily hold for all y < ©, which is sufficient to guarantee h(y) > 0 in 2. ‘To ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to ...
- **p. 2 / 1. IyrRopUCTION - extractive body cue:** We propose several methods for constructing the forcing function within Poisson's equation, including an average flux method and a guidance field method {26} that provides ...
- **p. 4 / IV. FORCING FUNCTION CONSTRUCTION - extractive body cue:** In this section, we present methods of designing forcing functions that ensure the solution to the boundary value problem for Poisson's equation (16) is a ...
- **Detected method headings:** B. Indirect Assignment - Variational Approach (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via ... | p. 2 (1. IyrRopUCTION), p. 6 (B. Indirect Assignment - Variational Approach) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | However. the condition V-v(y) <0 may not necessarily hold for all y < ©, which is sufficient to guarantee h(y) > 0 ... | p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can ... | p. 6 (B. Indirect Assignment - Variational Approach), p. 2 (1. IyrRopUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / B. Indirect Assignment - Variational Approach - extractive body cue:** Specifically, let h be the minimizer of the cost functional:
- **p. 5 / B. Indirect Assignment - Variational Approach - extractive body cue:** A twice differentiable minimizer of (24), h € C?(Q), satisfies the associated Euler-Lagrange equation, given by:
- **p. 4 / IV. FORCING FUNCTION CONSTRUCTION - extractive body cue:** In this section, we present methods of designing forcing functions that ensure the solution to the boundary value problem for Poisson's equation (16) is a ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** We obtain a smooth guidance field by solving Laplace's equation-the homogenous version ‘of Poisson's equation.
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** To address this, (25) ‘ensures we find h © C°(Q) whose gradient best approximates ¥V by using the divergence, V - ¥, as the forcing ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 4 (IV. FORCING FUNCTION CONSTRUCTION), p. 5 (B. Indirect Assignment - Variational Approach), p. 5 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | focus, systems, defined, integrator, chains, input, appearing, last, layer-note, extended, classes, outputs, nonuniform, relative | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | focus, systems, defined, integrator, chains, input, appearing, last, layer-note, extended | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | main, contributions, threefold, present, constructive, generating, safe, sets, complex, environments | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Specifically, minimizer, cost, functional, twice, differentiable, satisfies, associated, Euler-Lagrange, equation | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to ...
- **p. 1 / 1. IyrRopUCTION - extractive body cue:** Achieving this level of dynamic safety necessitates a quantifiable description of the safety requirement, i.e. a functional representation of the environment via a safety constraint, ...
- **p. 2 / 1. IyrRopUCTION - extractive body cue:** where x © R" is the state and u € IR" is the control input. ‘The function f : R" > R™ denotes the drift ...
- **p. 3 / B. Ouputs and Relative Degree - extractive body cue:** To facilitate the construction of CBFs, we recall the notion of relative degree, which represents the layer of differentiation at which the control inputs affects ...
- **p. 1 / Abstract - extractive body cue:** Solving this problem can enable the construction of safety filters that guarantee safe control actions- ‘most notably by employing Control Barrier Functions (CBFS).
- **p. 2 / 1. IyrRopUCTION - extractive body cue:** ‘The key observation of this paper is that safety functions ‘obtained from Poisson's equation can be used 10 synthesize CBES and, therefore, safety filters.
- **p. 3 / B. Ouputs and Relative Degree - extractive body cue:** Given an output y with relative degree r, we define a new set of partial coordinates:
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | After considering the entire processing chain, we update the Poisson safety function A online at approximately 10 Hz. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | As mentioned earlier, we ‘compute the Poisson safety function online at approximately 10 Hz; however, this time we numerically incorporate the temporal ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | After considering the entire processing chain, we update the Poisson safety function A online at approximately 10 Hz. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** main, contributions, threefold, present, constructive, generating, safe, sets, complex, environments, perception, data, Poisson, equation, illustrate, prove, resulting, safety, functions, synthesize.
- **Relevant PDF headings:** B. Indirect Assignment - Variational Approach (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | First, we perceive and segment the environment using fixed RGB camera and the Meta SAM2 [49] segmentation algorithm, Next, we generate a ... | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |
| Balance-aware whole-body execution | In each ease, the nominal controller attempted to drive the system directly 10 the goal without safety considerations. | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |
| Recovery / adaptation | For dynamic environments, we improve the ‘computational speed of our PDE solver by warm-starting each PDE solution with the previous safety function, ... | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |

## Failure and Ablation Link

- **p. 8 / B. Hardware Experiments - extractive body cue:** In each ease, the nominal controller attempted to drive the system directly 10 the goal without safety considerations.
- **p. 8 / B. Hardware Experiments - extractive body cue:** From these results, itis clear thatthe Poisson safety funetion enabled collision avoidance without hindering the nominal objective.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Smooth guidance field generation via Laplace' equation (26) [left] Boundary conditions ¥ = bi encoding the desired negative ux fon obstacle surfaces: and ...
- **p. 9 / 2 Nomina (Orange) & Safe (Bie) Inputs - extractive body cue:** ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, These ...
- **p. 7 / VI. DEMONSTRATIONS - extractive body cue:** Simulations: Double Integrator We define a 2D occupancy map defined by an open, bounded and connected domain © where J® characterizes obstacle surfaces. and consider ...
- **p. 8 / B. Hardware Experiments - extractive body cue:** From these results, itis clear thatthe Poisson safety funetion enabled collision avoidance without hindering the nominal objective.
- **p. 8 / B. Hardware Experiments - extractive body cue:** ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several collision avoidance scenarios using Unitree's Go2 quadruped ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1. IyrRopUCTION), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach), p. 2 (1. IyrRopUCTION), p. 4 (IV. FORCING FUNCTION CONSTRUCTION), objective p. 5 (B. Indirect Assignment - Variational Approach), p. 5 (B. Indirect Assignment - Variational Approach), p. 4 (IV. FORCING FUNCTION CONSTRUCTION), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach), temporal p. 8 (B. Hardware Experiments), p. 9 (2 Nomina (Orange) & Safe (Bie) Inputs), p. 2 (1. IyrRopUCTION), p. 8 (B. Hardware Experiments), p. 1 (1. IyrRopUCTION), p. 1 (1. IyrRopUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
