# Method - Contact-Invariant Optimization for Hand Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://homes.cs.washington.edu/~zoran/behavior-discovery.html; PDF retrieval source: https://homes.cs.washington.edu/~zoran/behavior-discovery.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction)): These algorithms are successful because they exploit domain-specific knowledge: state machines synchronized to the relatively simple and stereotypical pattern of foot-ground contacts, reduced models based on invertedpendulum dynamics or ...

## Method Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** These algorithms are successful because they exploit domain-specific knowledge: state machines synchronized to the relatively simple and stereotypical pattern of foot-ground contacts, reduced models based ...
- **p. 1 / Abstract - extractive body cue:** At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- **p. 2 / 1 Introduction - extractive body cue:** These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized together with the ...
- **p. 2 / 1 Introduction - extractive body cue:** Additional innovations include a continuation scheme allowing helper forces at the potential contacts rather than the torso, as well as a feature-based model of physics ...
- **p. 2 / 1 Introduction - extractive body cue:** Once this is done, optimizing the remaining aspects of the movement tends to be relatively straightforward.
- **p. 2 / 1 Introduction - extractive body cue:** The specific sets of active contacts that are suitable for each phase of each behavior are then discovered by the optimizer fully automatically.
- **p. 1 / 1 Introduction - extractive body cue:** Instead, movement details and complexity should emerge from an automated procedure whose only inputs are intuitive high-level goals that are easy to specify.
- **p. 1 / 1 Introduction - extractive body cue:** After three decades of intensive research, we now have algorithms that can make simulated humanoids walk robustly and realistically in response to high-level interactive inputs ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc
- **p. 2 / 1 Introduction - extractive body cue:** The important difference is that the domain to which our method is tailored is much larger, and includes any behavior of any articulated character where ...

## Source Evidence Cues

- **p. 1 / 1 Introduction - extractive body cue:** These algorithms are successful because they exploit domain-specific knowledge: state machines synchronized to the relatively simple and stereotypical pattern of foot-ground contacts, reduced models based ...
- **p. 1 / Abstract - extractive body cue:** At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- **p. 2 / 1 Introduction - extractive body cue:** These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized together with the ...
- **p. 2 / 1 Introduction - extractive body cue:** Additional innovations include a continuation scheme allowing helper forces at the potential contacts rather than the torso, as well as a feature-based model of physics ...
- **Detected method headings:** A Simplified Character Model (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | These algorithms are successful because they exploit domain-specific knowledge: state machines synchronized to the relatively simple and stereotypical pattern of foot-ground contacts, ... | p. 1 (1 Introduction), p. 1 (Abstract) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | At the core of our framework is the contact-invariant optimization (CIO) method we introduce here. | p. 1 (Abstract), p. 2 (1 Introduction) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized together with the ...
- **p. 1 / 1 Introduction - extractive body cue:** These algorithms are successful because they exploit domain-specific knowledge: state machines synchronized to the relatively simple and stereotypical pattern of foot-ground contacts, reduced models based ...
- **p. 2 / 1 Introduction - extractive body cue:** Once this is done, optimizing the remaining aspects of the movement tends to be relatively straightforward.
- **p. 2 / 1 Introduction - extractive body cue:** The specific sets of active contacts that are suitable for each phase of each behavior are then discovered by the optimizer fully automatically.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Instead, movement, details, complexity, should, emerge, automated, procedure, whose, only, inputs, intuitive, high-level, goals | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Instead, movement, details, complexity, should, emerge, automated, procedure, whose, only | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | core, framework, contact-invariant, optimization, CIO, introduce, here, present, step, towards | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | auxiliary, variables, affect, only, cost, function, dynamics, enabling, disabling, contact | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive body cue:** Instead, movement details and complexity should emerge from an automated procedure whose only inputs are intuitive high-level goals that are easy to specify.
- **p. 1 / 1 Introduction - extractive body cue:** After three decades of intensive research, we now have algorithms that can make simulated humanoids walk robustly and realistically in response to high-level interactive inputs ...
- **p. 2 / 1 Introduction - extractive body cue:** These include getting up from the ground, crawling, climbing, moving heavy objects, acrobatics (hand-stands in particular), and various cooperative actions involving two characters and their ...
- **p. 2 / 1 Introduction - extractive body cue:** This is a very large domain because almost all limb movements performed on land are made for the purpose of establishing contact with some object ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | The overall movement time T is partitioned into K intervals or phases, and 1 ≤φ (t) ≤K is the index of the ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | In this subsection we focus on a single time step and omit the time index t. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** algorithms, successful, because, they, exploit, domain-specific, knowledge, state, machines, synchronized, relatively, simple, stereotypical, pattern, foot-ground, contacts, reduced, models, invertedpendulum, dynamics.
- **Relevant PDF headings:** A Simplified Character Model (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object. | p. 6 (5 Results), p. 6 (5 Results) |
| Grasp / trajectory generation | For example, animal trot pattern of contacts (moving front leg and opposite hind leg together) emerges for quadruped walking without explicitly being ... | p. 6 (5 Results), p. 6 (5 Results) |
| Contact execution / correction | Because contacts can be made with the surfaces of other characters, the task is achieved by one character climbing on top of ... | p. 6 (5 Results), p. 6 (5 Results) |

## Failure and Ablation Link

- **p. 6 / 5 Results - extractive body cue:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.
- **p. 6 / 5 Results - extractive body cue:** For example, animal trot pattern of contacts (moving front leg and opposite hind leg together) emerges for quadruped walking without explicitly being specified.
- **p. 6 / 5 Results - extractive body cue:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.
- **p. 6 / 5 Results - extractive body cue:** These limitations may be removed by using full-body inverse dynamics to calculate the character's joint torques, and penalizing the torques or some related quantity.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, K., COROS, S., BEAUDOIN, P., AND VAN ...
- **p. 5 / 2 Related Work - extractive body cue:** Exactly the same continuation scheme was successful in all of the diverse behaviors we studied, and so our method does not need behavior-specific adjustments.
- **p. 5 / 2 Related Work - extractive body cue:** The solution obtained at the end of each phase is perturbed with small zero-mean Gaussian noise (to break any symmetries) and used to initialize the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), objective p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), temporal p. 3 (2 Related Work), p. 4 (2 Related Work), p. 1 (1 Introduction), p. 2 (2 Related Work), p. 2 (2 Related Work), p. 6 (5 Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** These algorithms are successful because they exploit domain-specific knowledge: state machines synchronized to the relatively simple and stereotypical pattern of foot-ground contacts, reduced models based on invertedpendulum dynamics or ... (p. 1, 1 Introduction).
- **Objective/update evidence:** These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized together with the movement trajectory. (p. 1, Abstract).
- **Temporal/runtime evidence:** In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc (p. 1, 1 Introduction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
