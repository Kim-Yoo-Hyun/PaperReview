# Insights — Impedance Control: An Approach to Manipulation: Part I—Theory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3140702; PDF retrieval source: https://doi.org/10.1115/1.3140702. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / body section boundary not confidently recovered - extractive body cue:** In Part I this approach is developed by considering the mechanics of interaction between physical systems.
- **p. 1 / body section boundary not confidently recovered - extractive body cue:** The approach developed encompasses and includes the simple positioning or transporting tasks typically performed by robots and/or prostheses.
- **p. 2 / body section boundary not confidently recovered - extractive body cue:** In the following it is developed from some simple and physically reasonable assumptions.
- **p. 6 / 1 Y - extractive body cue:** Several simple but fundamental observations may then be made: Command and control of a vector such as position or force is not enough to control ...
- **p. 5 / 1 Y - extractive body cue:** That network depicts the separation of the controller action into two distinct components, one (the flow source) representing the control of motion, the other (the ...
- **p. 6 / 1 Y - extractive body cue:** By assuming that no control algorithm may make a physical system behave like anything other than a physical system the network concepts of bond graphs ...
- **p. 5 / 1 Y - extractive body cue:** The manipulator behavior (assumed to be nodic) is then characterized by a static relation between force and position (modulated by the command set).
- **Contribution anchor:** p. 1 (body section boundary not confidently recovered), p. 1 (body section boundary not confidently recovered), p. 2 (body section boundary not confidently recovered), p. 6 (1 Y), p. 5 (1 Y), p. 6 (1 Y)

### Strongest assumption and failure boundary

- **p. 4 / body section boundary not confidently recovered - extractive body cue:** However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as ...
- **p. 3 / body section boundary not confidently recovered - extractive body cue:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output ...
- **p. 3 / body section boundary not confidently recovered - extractive body cue:** The kinematic transformation equations are: X1=Ll cos 6{+L2 cos d2+L3 cos d3 (3) X2=Lt smdl+L2smd2+L3sm61 (4) Again, joint angles uniquely define end-point position but the ...
- **p. 1 / body section boundary not confidently recovered - extractive body cue:** It will be shown (in Parts II and III) that the approach can lead to a simplification of some problems in manipulator control.
- **p. 1 / body section boundary not confidently recovered - extractive body cue:** It is shown that as manipulation is a fundamentally nonlinear problem, the distinction between impedance and admittance is essential, and given the environment contains inertial ...
- **p. 5 / 1 Y - extractive body cue:** The behavior of the manipulator may now be written as follows (assuming a state-determined system): V 0=V 0:jc) Virtual Source (10) f = V 0 ...
- **p. 2 / body section boundary not confidently recovered - extractive body cue:** The high-level supervisor, while it may have access to sensory data, does not use that data in an immediate feedback control mode to modulate its ...
- **Boundary to test:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output variable.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In Part I this approach is developed by considering the mechanics of interaction between physical systems. | p. 1 (body section boundary not confidently recovered), p. 1 (body section boundary not confidently recovered) |
| Reported outcome | The separation of the controller action into a (vector) motion component and a impedance component (which has the properties of a tensor) can be achieved for a general class of nonlinear controlled ... | p. 5 (1 Y) |
| Failure/limitation | Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output variable. | p. 3 (body section boundary not confidently recovered), p. 4 (body section boundary not confidently recovered) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** For example, the constitutive equation for a point mass is fundamentally written with velocity as the output variable, defined as a function of momentum; momentum in turn is the integral ... (p. 2, Body text (section boundary not confidently recovered)).
- **Paper-specific mechanism:** Control of position or force alone is inadequate; control of dynamic behavior is also required. (p. 1, Body text (section boundary not confidently recovered)).
- **Evidence boundary:** the reported outcome is This organization has been proposed as a general form of control and communication for man/machine systems [26]: it is commonly used for robots [2]; and there is some evidence that ... (p. 2, Body text (section boundary not confidently recovered)); the relevant task/metric cue is Strategies directed toward the control of a vector quantity such as position, velocity, or force will be inadequate as they are insufficient to control the mechanical work exchanged between the ... (p. 2, Body text (section boundary not confidently recovered)). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** A large class of manufacturing operations fall into this category: examples include drilling, reaming, routing, counterboring, grinding, bending, chipping, fettling-any task requiring work to be done on the environment. (p. 1, Body text (section boundary not confidently recovered)).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, Impedance Control, contact, manipulation`.
- **Reading predecessor in the generated track queue:** Hybrid Position/Force Control of Manipulators (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output variable.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: For example, the constitutive equation for a point mass is fundamentally written with velocity as the output variable, defined as a function of momentum; momentum in turn is the integral ... (p. 2, Body text (section boundary not confidently recovered)); preserve the objective/update rule: The kinematic transformations X = L(6) (equations (1), (2), (3) and (4)) are in fact part of the junction structure through which the various elements in a physical system interact2 ... (p. 3, Body text (section boundary not confidently recovered)).
2. Use the paper-reported task/data/environment cue: A unified framework for considering the action of both hardware and software in the control of dynamic behavior can be obtained by making the reasonable assumption that no controller can ... (p. 2, Body text (section boundary not confidently recovered)).
3. Compare against the reported or matched baseline: The superposition properties of the Norton equivalent network have been retained without restriction to linear systems. (p. 5, 1 Y).
4. Report the body metric with its denominator and aggregation: Strategies directed toward the control of a vector quantity such as position, velocity, or force will be inadequate as they are insufficient to control the mechanical work exchanged between the ... (p. 2, Body text (section boundary not confidently recovered)).
5. Re-run the reported ablation or stress/failure condition: In fact, linearized components of the impedance such as the stiffness and the viscosity are second-rank twice covariant tensors. (p. 4, Body text (section boundary not confidently recovered)); if none is reported, design one around: A large class of manufacturing operations fall into this category: examples include drilling, reaming, routing, counterboring, grinding, bending, chipping, fettling-any task requiring work to be done on the environment. (p. 1, Body text (section boundary not confidently recovered)).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), match the reported outcome at p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)), and measure the boundary at p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)).

## Falsifiable research question

Under the paper's stated interface (For example, the constitutive equation for a point mass is fundamentally written with velocity as the output variable, defined as a function ...), does the paper-specific mechanism (Control of position or force alone is inadequate; control of dynamic behavior is also required.) retain the reported evaluation outcome (Strategies directed toward the control of a vector quantity such as position, velocity, or force will be inadequate ...) when tested against the paper's strongest explicit boundary (A large class of manufacturing operations fall into this category: examples include drilling, reaming, routing, counterboring, grinding, bending, ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Strategies directed toward the control of a vector quantity such as position, velocity, or force will be inadequate ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Control of position or force alone is inadequate; control of dynamic behavior is also required. (p. 1, Body text (section boundary not confidently recovered)).
- **Paper-supported outcome:** This organization has been proposed as a general form of control and communication for man/machine systems [26]: it is commonly used for robots [2]; and there is some evidence that ... (p. 2, Body text (section boundary not confidently recovered)).
- **Strongest explicit boundary:** A large class of manufacturing operations fall into this category: examples include drilling, reaming, routing, counterboring, grinding, bending, chipping, fettling-any task requiring work to be done on the environment. (p. 1, Body text (section boundary not confidently recovered)).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
