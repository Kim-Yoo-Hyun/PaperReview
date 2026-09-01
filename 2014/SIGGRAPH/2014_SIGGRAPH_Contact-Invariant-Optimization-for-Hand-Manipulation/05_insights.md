# Insights — Contact-Invariant Optimization for Hand Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://homes.cs.washington.edu/~zoran/behavior-discovery.html; PDF retrieval source: https://homes.cs.washington.edu/~zoran/behavior-discovery.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc
- **p. 2 / 1 Introduction - extractive body cue:** The important difference is that the domain to which our method is tailored is much larger, and includes any behavior of any articulated character where ...
- **p. 2 / 1 Introduction - extractive body cue:** Intuitively, CIO is a way of reshaping a highly discontinuous and local-minima-prone search space of movements and contacts, into a slightly larger but much better-behaved ...
- **p. 1 / 1 Introduction - extractive body cue:** These algorithms are successful because they exploit domain-specific knowledge: state machines synchronized to the relatively simple and stereotypical pattern of foot-ground contacts, reduced models based ...
- **p. 2 / 1 Introduction - extractive body cue:** These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized together with the ...
- **p. 2 / 1 Introduction - extractive body cue:** Additional innovations include a continuation scheme allowing helper forces at the potential contacts rather than the torso, as well as a feature-based model of physics ...
- **Contribution anchor:** p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** In complex behaviors and in complex environments, however, it is difficult to know in advance what these contact sets should be and how they should ...
- **p. 1 / 1 Introduction - extractive body cue:** Automated synthesis of complex human behaviors is one of the long-standing grand challenges in computer graphics, that would also have an impact on robotics, biomechanics, ...
- **p. 1 / 1 Introduction - extractive body cue:** With the current state-of-the-art in automated motion synthesis, any additional complex behavior would require a new movement model carefully crafted by experts from scratch.
- **p. 2 / 1 Introduction - extractive body cue:** 1.1 The key idea: Contact-Invariant Optimization (CIO) As with prior methods for automated behavior synthesis, our CIO method also comes down to exploiting domain-specific knowledge.
- **p. 6 / 5 Results - extractive body cue:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.
- **p. 6 / 5 Results - extractive body cue:** These limitations may be removed by using full-body inverse dynamics to calculate the character's joint torques, and penalizing the torques or some related quantity.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, K., COROS, S., BEAUDOIN, P., AND VAN ...
- **Boundary to test:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | At the core of our framework is the contact-invariant optimization (CIO) method we introduce here. | p. 1 (Abstract), p. 1 (1 Introduction) |
| Reported outcome | Because contacts can be made with the surfaces of other characters, the task is achieved by one character climbing on top of the other. | p. 6 (5 Results), p. 6 (5 Results) |
| Failure/limitation | One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density. | p. 6 (5 Results), p. 6 (5 Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 Instead, movement details and complexity should emerge from an automated procedure whose only inputs are intuitive high-level goals that are easy to specify.를 After three decades of intensive research, we now have algorithms that can make simulated humanoids walk robustly and realistically in response to high-level interactive inputs such as desired body velocity and orientation.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, trajectory optimization, contact invariant`.
- **Reading predecessor in the generated track queue:** GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object..
3. Compare against the body-reported baseline or a matched simpler baseline: For example, animal trot pattern of contacts (moving front leg and opposite hind leg together) emerges for quadruped walking without explicitly being specified..
4. Report the body metric and its denominator/aggregation: The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology..
5. Re-run the body-reported ablation/failure condition: One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction); the primary result is directionally consistent at p. 6 (5 Results), p. 6 (5 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 core, framework, contact-invariant mechanism이 For example, animal trot pattern of contacts (moving front leg and opposite hind leg together) emerges ... 대비 The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology.을 개선하고, One way to remove this limitation is to simply increase the number of potential contacts and ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
