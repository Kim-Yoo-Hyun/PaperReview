# Insights — A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://cs.stanford.edu/group/manips/publications.html; PDF retrieval source: https://cs.stanford.edu/group/manips/publications/pdfs/Khatib_1987_RA.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn
- **p. 1 / Abstract - extractive body cue:** A framework for the analysis and control of manipulator systems with respect to the dynamic behavior of their end-effectors is developed.
- **p. 3 / I. Inrropucrion - extractive body cue:** This allows a more efficient implementation of the control system for real-time operations.
- **p. 6 / IV. Exp-Errecror Morton Controt - extractive body cue:** The real-time computation of these coefficients can then be paced by the rate of configuration changes, which is much lower than that of the mechanism ...
- **p. 1 / I. Inrropucrion - extractive body cue:** However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector.
- **p. 1 / I. Inrropucrion - extractive body cue:** ‘The issue of end-effector dynamic modeling and control is yet more acute for tasks that involve combined motion and ‘contact forces of the end-effector.
- **p. 3 / I. Inrropucrion - extractive body cue:** However, the control of end-effector motion and contact forces, or the analysis and characterization of endeffector dynamic performance requires the construction of the model describing ...
- **Contribution anchor:** p. 1 (Abstract), p. 1 (Abstract), p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt), p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion)

### Strongest assumption and failure boundary

- **p. 1 / I. Inrropucrion - extractive body cue:** The magnitude of these dynamic forces cannot be ignored when large accelerations and fast motions are considered.
- **p. 1 / I. Inrropucrion - extractive body cue:** Obviously, these characteristics cannot be found in the manipulator joint space dynamic model, which only provides a description of the interaction between joint motions.
- **p. 2 / I. Inrropucrion - extractive body cue:** Tl, GeneRALizeD Task SpEciricaTion MarRices
- **p. 2 / I. Inrropucrion - extractive body cue:** In this paper, a new approach for dealing with the problem of kinematic singularities within the operational space framework is presented.
- **p. 3 / I. Inrropucrion - extractive body cue:** First, let us consider the case of nonredundant manipulators, where a set of operational coordinates can be selected asa system of generalized coordinates for the ...
- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15]
- **p. 7 / VI. ReDunpaNT MANIPULATORS - extractive body cue:** ‘The configuration of a redundant manipulator cannot be specified by a set of parameters that only describes the endeffector position and orientation.
- **Boundary to test:** This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15]

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn | p. 1 (Abstract), p. 1 (Abstract) |
| Reported outcome | The construction of the end-effector dynamic model is achieved by expressing the relationships between its ‘operational positions, velocities, accelerations, and the virtual ‘operational forces acting on it. | p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt) |
| Failure/limitation | This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15] | p. 5 (IV. Exp-Errecror Morton Controt), p. 7 (VI. ReDunpaNT MANIPULATORS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector. (p. 1, I. Inrropucrion).
- **Paper-specific mechanism:** These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks. (p. 5, IV. Exp-Errecror Morton Controt); the relevant task/metric cue is In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks. (p. 5, IV. Exp-Errecror Morton Controt). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** This performance has been obtained despite the limitations in controlling the manipulator joint torques [27]. ‘Accurate identification of the PUMA. (p. 10, IX. Susmary ano Discussion).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, operational space control, force control, manipulation`.
- **Reading predecessor in the generated track queue:** Planning and Acting in Partially Observable Stochastic Domains (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Hybrid Position/Force Control of Manipulators (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15]; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector. (p. 1, I. Inrropucrion); preserve the objective/update rule: The number of degrees of freedom of the constrained end-effector is given by the difference between mo and the number of independent ‘equations specifying the geometric constraints, assumed to be ... (p. 2, I. Inrropucrion).
2. Use the paper-reported task/data/environment cue: For control systems implemented for tasks specified with respect to the end-effector coordinate frame, these matrices will be specified with respect to that, coordinate frame as well. (p. 3, I. Inrropucrion).
3. Compare against the reported or matched baseline: In the reference frame (o, the system of my equations expressing the components of x as functions of joint coordinates, i.e., the geometric model, is given by (p. 3, X 1 column matrix x of independent configuration parame).
4. Report the body metric with its denominator and aggregation: In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks. (p. 5, IV. Exp-Errecror Morton Controt).
5. Re-run the reported ablation or stress/failure condition: where Ag(q) and 6,(g, 4) are defined similarly to A(q) and (q, 4) with J(g) being replaced by Jo(q). (p. 6, V. Constnainep Motion Operarions); if none is reported, design one around: This performance has been obtained despite the limitations in controlling the manipulator joint torques [27]. ‘Accurate identification of the PUMA. (p. 10, IX. Susmary ano Discussion).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 1 (I. Inrropucrion), match the reported outcome at p. 5 (IV. Exp-Errecror Morton Controt), p. 7 (V. Constnainep Motion Operarions), p. 3 (I. Inrropucrion), and measure the boundary at p. 10 (IX. Susmary ano Discussion), p. 10 (IX. Susmary ano Discussion).

## Falsifiable research question

Under the paper's stated interface (However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector.), does the paper-specific mechanism (These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn) retain the reported evaluation outcome (In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related ...) when tested against the paper's strongest explicit boundary (This performance has been obtained despite the limitations in controlling the manipulator joint torques [27]. ‘Accurate identification of ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn (p. 1, Abstract).
- **Paper-supported outcome:** In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks. (p. 5, IV. Exp-Errecror Morton Controt).
- **Strongest explicit boundary:** This performance has been obtained despite the limitations in controlling the manipulator joint torques [27]. ‘Accurate identification of the PUMA. (p. 10, IX. Susmary ano Discussion).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
