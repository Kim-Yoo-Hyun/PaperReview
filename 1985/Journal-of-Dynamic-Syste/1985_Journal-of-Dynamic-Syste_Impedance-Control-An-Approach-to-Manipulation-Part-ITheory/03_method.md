# Method - Impedance Control: An Approach to Manipulation: Part I—Theory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3140702; PDF retrieval source: https://doi.org/10.1115/1.3140702. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered))): This can be stated as the following postulate:1 "It is impossible to devise a controller which will cause a physical system to present an apparent behavior to its enMANIPULATOR SUPERVISOR ...

## Method Body Digest

- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** This can be stated as the following postulate:1 "It is impossible to devise a controller which will cause a physical system to present an apparent ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** If it is assumed that at a minimum the manipulator should be capable of stably.positioning a simple mass it can be seen that this network ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** It might then be concluded that what is required in general is the control of a vector of interaction forces.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** If the environment is regarded as a source of "disturbances" to the manipulator, then modulating the "disturbance response" of the manipulator will permit control of ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In other situations the manipulator encounters constraints in its environment and the interaction forces are not negligible.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In some cases the interaction forces are negligible, the instantaneous Contributed by the Dynamic Systems and Control Division for publication in the JOURNAL OF DYNAMIC ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** In constrast, the corresponding transformation from forces applied at the interaction port to the resulting torques applied to the links is always well defined: r, ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The kinematic transformations X = L(6) (equations (1), (2), (3) and (4)) are in fact part of the junction structure through which the various elements ...

## Design Rationale

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In Part I this approach is developed by considering the mechanics of interaction between physical systems.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The approach developed encompasses and includes the simple positioning or transporting tasks typically performed by robots and/or prostheses.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** In the following it is developed from some simple and physically reasonable assumptions.

## Source Evidence Cues

- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** This can be stated as the following postulate:1 "It is impossible to devise a controller which will cause a physical system to present an apparent ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** If it is assumed that at a minimum the manipulator should be capable of stably.positioning a simple mass it can be seen that this network ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** It might then be concluded that what is required in general is the control of a vector of interaction forces.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** If the environment is regarded as a source of "disturbances" to the manipulator, then modulating the "disturbance response" of the manipulator will permit control of ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In other situations the manipulator encounters constraints in its environment and the interaction forces are not negligible.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In some cases the interaction forces are negligible, the instantaneous Contributed by the Dynamic Systems and Control Division for publication in the JOURNAL OF DYNAMIC ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** In constrast, the corresponding transformation from forces applied at the interaction port to the resulting torques applied to the links is always well defined: r, ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | This can be stated as the following postulate:1 "It is impossible to devise a controller which will cause a physical system to ... | p. 2 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | If it is assumed that at a minimum the manipulator should be capable of stably.positioning a simple mass it can be seen ... | p. 4 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | It might then be concluded that what is required in general is the control of a vector of interaction forces. | p. 4 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The kinematic transformations X = L(6) (equations (1), (2), (3) and (4)) are in fact part of the junction structure through which the various elements ...
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** Causality Several important constraints on the behavior of physical systems can be identified.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** When more than one degree of freedom is considered, kinematic relations may impose a further causal constraint.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In other situations the manipulator encounters constraints in its environment and the interaction forces are not negligible.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Along the tangent to a pure (i.e., frictionless) kinematic constraint the interaction forces are zero (F = 0) whereas along the normal into the surface ...
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** An obvious but important physical constraint is that no one system may determine both variables.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 3 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | constitutive, equation, point, mass, invertible, equations, written, Nomenclature, mechanical, force, position, link, lengths, eue2 | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | constitutive, equation, point, mass, invertible, equations, written, Nomenclature, mechanical, force | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | Part, developed, considering, mechanics, interaction, between, physical, systems, encompasses, includes | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | kinematic, transformations, equations, fact, part, junction, structure, through, various, elements | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** As the constitutive equation for a point mass is invertible the equations may also be written with Nomenclature W = mechanical work F,F, ,F2 = ...
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** For example, the constitutive equation for a point mass is fundamentally written with velocity as the output variable, defined as a function of momentum; momentum ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** Seen from the tip, this sytsem is properly described as an admittance. force as the output variable, defined as a function of the derivative of ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** However, they argued that when the manipulator was in contact with the environment the appropriate strategy was to "command a position or velocity and look ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** As discussed above, pure force control is also inadequate; however, the term is applied loosely to control strategies using force feedback in combination with other ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In other situations the manipulator encounters constraints in its environment and the interaction forces are not negligible.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Superposition of Impedances The most interesting consequence of the ^assumptions underlying impedance control is that if the dynamic behavior of the manipulator ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | It is shown that as manipulation is a fundamentally nonlinear problem, the distinction between impedance and admittance is essential, and given the ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In other situations the manipulator encounters constraints in its environment and the interaction forces are not negligible.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** stated, following, postulate, impossible, devise, controller, will, cause, physical, system, present, apparent, behavior, enMANIPULATOR, SUPERVISOR, PLANNER, REAL, TIME, SOFTWARE, ACTUATORS.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | This organization has been proposed as a general form of control and communication for man/machine systems [26]: it is commonly used for ... | p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)) |
| Grasp / trajectory generation | The superposition properties of the Norton equivalent network have been retained without restriction to linear systems. | p. 5 (1 Y), p. 4 (Body text (section boundary not confidently recovered)) |
| Contact execution / correction | The separation of the controller action into a (vector) motion component and a impedance component (which has the properties of a tensor) ... | p. 5 (1 Y), p. 3 (Body text (section boundary not confidently recovered)) |

## Failure and Ablation Link

- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** In fact, linearized components of the impedance such as the stiffness and the viscosity are second-rank twice covariant tensors.
- **p. 5 / 1 Y - extractive body cue:** Consider again the static relation between force and position: The nodic component of this relation is the part which may be maintained invariant under a ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** The controller must specify a vector quantity such as the desired position, but it must also specify a quantity which is fundamentally different: a relationship, ...
- **p. 5 / 1 Y - extractive body cue:** The superposition properties of the Norton equivalent network have been retained without restriction to linear systems.
- **p. 6 / 1 Y - extractive body cue:** Each component of the total impedance is represented by a generalized Norton equivalent network.
- **p. 6 / 1 Y - extractive body cue:** Note that any non-nodic component of the manipulator behavior may be included in this equivalent network by associating it with a flow source identically equal ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), objective p. 3 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), temporal p. 6 (1 Y), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** This can be stated as the following postulate:1 "It is impossible to devise a controller which will cause a physical system to present an apparent behavior to its enMANIPULATOR SUPERVISOR ... (p. 2, Body text (section boundary not confidently recovered)).
- **Objective/update evidence:** The kinematic transformations X = L(6) (equations (1), (2), (3) and (4)) are in fact part of the junction structure through which the various elements in a physical system interact2 ... (p. 3, Body text (section boundary not confidently recovered)).
- **Temporal/runtime evidence:** A unified framework in which to consider the action of both hardware and software in controlling dynamic interaction is desirable. (p. 2, Body text (section boundary not confidently recovered)).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
