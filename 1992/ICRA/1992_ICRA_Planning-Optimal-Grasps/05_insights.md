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

- **p. 1 / 1 Introduction - extractive body cue:** Because of their intricate design, they are difficult to control and plan *Supported by the Italian Ministry for University and Scientific Research.
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

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object to the point contact where the force ...를 Of course, there can still be some directions where the reaction wrench can be greater, but we want to be assured we get a lower bound over all directions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to avoid collision among the fingers. It is ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In section four, we introduce and discuss the quality criteria we are proposing.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Grasp Planning, manipulation, contact`.
- **Reading predecessor in the generated track queue:** start of this track queue (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to avoid collision among the fingers. It is ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Avoiding large forces minimizes the deformation of both the object and the jaws..
3. Compare against the body-reported baseline or a matched simpler baseline: Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces..
4. Report the body metric and its denominator/aggregation: Without loss of generality, we choose llwll so that 11g11 = 1..
5. Re-run the body-reported ablation/failure condition: Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (4.1 Representing Anger forces), p. 1 (2 Working hypotheses), p. 2 (2 Working hypotheses); the primary result is directionally consistent at p. 3 (4.1 Representing Anger forces); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 section, four, introduce mechanism이 Some grasp configurations can be better than others in the sense that they can balance every ... 대비 Without loss of generality, we choose llwll so that 11g11 = 1.을 개선하고, Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
