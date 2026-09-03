# Insights — OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.18743; PDF retrieval source: https://arxiv.org/pdf/2409.18743. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried ...
- **p. 3 / III. METHOD - extractive body cue:** The OpenObject-NAV system framework consists of two main modules.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This update enables efficient point-to-point navigation for the third task. dynamic and subject to interference, making it challenging to efficiently and effectively navigate to them.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Based on the CRSG, we designed an object-oriented navigation strategy, modeling the object search process as a Markov Decision Process (MDP) [21].
- **p. 3 / III. METHOD - extractive body cue:** The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) ...
- **p. 4 / III. METHOD - extractive body cue:** Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object ...
- **p. 2 / III. METHOD - extractive body cue:** Unlike ConceptGraph [19], each instance object Oi ∈O (O is the set of all objects) not only contains a CLIP feature V Fi but also ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, they struggle to represent everyday dynamic environments due to two key challenges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, they are often limited to searching for semantic-level objects and lack the capability to update scenes.
- **p. 4 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** If the robot fails to reach the target, the SPL score is zero.
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** VLMap Ours ConceptGraph Result: Success Result: Success Result: Failed ---Find a chair Result: Failed ---Find yellow bottle Result: Failed ---Find chairs Task 1: black bottle ...
- **Boundary to test:** If the robot fails to reach the target, the SPL score is zero.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried relationships between objects. • We design a ... | p. 2 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Reported outcome | 4 illustrates an example of long-sequence navigation, where the efficiency of navigating to the target significantly improves as the number of navigated objects increases. | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Failure/limitation | If the robot fails to reach the target, the SPL score is zero. | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) (8) policy π(·): Given current state St ...를 We model the exploration of a displaced object as a fixedpolicy Markov decision process (MDP) below. state space S: In the current step t, we define: 1. the robot's pose Lt ∈L, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 If the robot fails to reach the target, the SPL score is zero.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried relationships between objects. • We design a ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Navigation, Graph Reasoning, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** If the robot fails to reach the target, the SPL score is zero.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Real-World Validation We validated our algorithm using an Autolabor robot in a real scene, equipped with an industrial computer featuring an NVIDIA GeForce RTX 3080..
3. Compare against the body-reported baseline or a matched simpler baseline: The resulting feature is then compared with the SBERT or CLIP features of each object in the CRSG S G using cosine similarity, similar to Eq..
4. Report the body metric and its denominator/aggregation: We report Success Rate(SR) and Success weighted by inverse Path Length (SPL) [39]..
5. Re-run the body-reported ablation/failure condition: IV-B, while the second and third figures show the results of the ablation experiments with and without CRSG updates in Sec..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD); the primary result is directionally consistent at p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 The resulting feature is then compared with the SBERT or CLIP features of each object in ... 대비 We report Success Rate(SR) and Success weighted by inverse Path Length (SPL) [39].을 개선하고, If the robot fails to reach the target, the SPL score is zero. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
