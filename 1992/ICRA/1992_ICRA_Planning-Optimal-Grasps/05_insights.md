# Insights — Planning Optimal Grasps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.1992.219918; PDF retrieval source: https://doi.org/10.1109/ROBOT.1992.219918. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** In section four, we introduce and discuss the quality criteria we are proposing.
- **p. 1 / 1 Introduction - extractive body cue:** We give a geometric interpretation of the criteria which unifies them, and allows simple algorithms for optimal grasp planning according to either criterion.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at ...
- **p. 1 / 2 Working hypotheses - extractive body cue:** In this model, fingers can exert any force pointing into the friction cone at the point of contact.
- **p. 2 / 2 Working hypotheses - extractive body cue:** Hence we have an immediate representation of each point contact force exerted by the fingers.
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** 4.4 In this case we state the hypothesis that the sum of the magnitude of the forces at the contact points is upper-bounded, and we ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object ...
- **Contribution anchor:** p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (4.1 Representing Anger forces), p. 1 (2 Working hypotheses), p. 2 (2 Working hypotheses), p. 4 (4.3 Minimizing the maximum Anger force)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Because of their intricate design, they are difficult to control and plan.
- **p. 1 / 1 Introduction - extractive body cue:** The geometrical aspects of grasping will be emphasized while the problem of controlling compliance between the object and the jaws is not considered.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine the actual wrench acting on the object ...
- **Boundary to test:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to avoid collision among the fingers. It is ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In section four, we introduce and discuss the quality criteria we are proposing. | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | We therefore want to guarantee a level of performance as judged by the local quality measure over all possible wrenches, and this is the measure Q Notice that for a given direction ... | p. 3 (4.1 Representing Anger forces) |
| Failure/limitation | Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to avoid collision among the fingers. It is ... | p. 6 (Figure/Table caption), p. 3 (4.1 Representing Anger forces) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object to the point contact where ... (p. 4, 4.3 Minimizing the maximum Anger force).
- **Paper-specific mechanism:** In section four, we introduce and discuss the quality criteria we are proposing. (p. 1, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 1: Graphic Evaluation of the Quality Criteria 5 An Example of Using the Quality Criteria In the next subsections, we will present an algo- rithm that can evaluate the ... (p. 5, Figure/Table caption); the relevant task/metric cue is Then, Q is just the distance of the nearest point to the origin, from the origin itself. (p. 3, 4.1 Representing Anger forces). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In a force closure grasp, finger locations do not change to counter external forces. (p. 1, 2 Working hypotheses).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Grasp Planning, manipulation, contact`.
- **Reading predecessor in the generated track queue:** start of this track queue (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to avoid collision among the fingers. It is ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object to the point contact where ... (p. 4, 4.3 Minimizing the maximum Anger force); preserve the objective/update rule: Without loss of generality, we choose llwll so that 11g11 = 1. (p. 3, 4.1 Representing Anger forces).
2. Use the paper-reported task/data/environment cue: Avoiding large forces minimizes the deformation of both the object and the jaws. (p. 2, 4 The Quality of Grasp).
3. Compare against the reported or matched baseline: Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces. (p. 2, 4 The Quality of Grasp).
4. Report the body metric with its denominator and aggregation: Then, Q is just the distance of the nearest point to the origin, from the origin itself. (p. 3, 4.1 Representing Anger forces).
5. Re-run the reported ablation or stress/failure condition: Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces. (p. 2, 4 The Quality of Grasp); if none is reported, design one around: In a force closure grasp, finger locations do not change to counter external forces. (p. 1, 2 Working hypotheses).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 3 (4.1 Representing Anger forces), and measure the boundary at p. 1 (2 Working hypotheses), p. 3 (4.1 Representing Anger forces).

## Falsifiable research question

Under the paper's stated interface (The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass ...), does the paper-specific mechanism (In section four, we introduce and discuss the quality criteria we are proposing.) retain the reported evaluation outcome (Then, Q is just the distance of the nearest point to the origin, from the origin itself.) when tested against the paper's strongest explicit boundary (In a force closure grasp, finger locations do not change to counter external forces.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Then, Q is just the distance of the nearest point to the origin, from the origin itself.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (6 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In section four, we introduce and discuss the quality criteria we are proposing. (p. 1, 1 Introduction).
- **Paper-supported outcome:** Figure 1: Graphic Evaluation of the Quality Criteria 5 An Example of Using the Quality Criteria In the next subsections, we will present an algo- rithm that can evaluate the ... (p. 5, Figure/Table caption).
- **Strongest explicit boundary:** In a force closure grasp, finger locations do not change to counter external forces. (p. 1, 2 Working hypotheses).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
