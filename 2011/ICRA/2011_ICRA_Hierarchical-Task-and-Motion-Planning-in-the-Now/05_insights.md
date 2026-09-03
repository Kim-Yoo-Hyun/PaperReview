# Insights — Hierarchical Task and Motion Planning in the Now

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980391; PDF retrieval source: https://people.csail.mit.edu/tlp/pdf/2011/hpnICRA11Final.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 7 / V. ALGORITHMS - extractive body cue:** The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.
- **p. 7 / V. ALGORITHMS - extractive body cue:** The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; ...
- **Contribution anchor:** p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** We attempt to avoid such failures by constraining the abstract plan steps so that they are serializable [1]; that is, so that for any realization ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** If, for some reason, serializability fails, then we formulate an interleaved plan for achieving the effects of both steps; as long as actions in the ...
- **p. 6 / C C - extractive body cue:** Because these variables both have infinite domains in our setting, we cannot enumerate them.
- **p. 6 / C C - extractive body cue:** If at attempt at serializing operations at an abstract level fails, then the planning problem is
- **p. 7 / V. ALGORITHMS - extractive body cue:** SuggestPoses(O, R, Taboos): finds a set of poses for O where it is completely inside region R, there is no collision with taboo regions, and ...
- **p. 7 / V. ALGORITHMS - extractive body cue:** SuggestParking(O, Taboos, start): find an "out of the way" location for O that does not overlap any of the regions in Taboos.
- **Boundary to test:** Because these variables both have infinite domains in our setting, we cannot enumerate them.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below. | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS) |
| Reported outcome | Note that executing the operator for removing c from the swept volume of a requires no further planning or execution, as the condition it was intended to establish has already been achieved ... | p. 3 (B C), p. 6 (C C) |
| Failure/limitation | Because these variables both have infinite domains in our setting, we cannot enumerate them. | p. 6 (C C), p. 6 (C C) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 HPN(currentState, goal, operators, absLevel, world): if holds(goal, currentState): return TRUE else p = PLAN(currentState, goal, operators, absLevel) for (oi, gi) in p if prim(oi): currentState = world.execute(oi) else HPN(currentState, ...를 The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; goal is a conjunction of fluents describing ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Because these variables both have infinite domains in our setting, we cannot enumerate them.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Planning, task and motion planning, manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Because these variables both have infinite domains in our setting, we cannot enumerate them.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The first requires that a swept volume of the robot moving to object a and picking it up be free..
3. Compare against the body-reported baseline or a matched simpler baseline: First, it may not be possible to make pn true without undoing p1, . . . , pn-1..
4. Report the body metric and its denominator/aggregation: To operate in infinite domains, we augment the standard operator descriptions with the following features: Suggesters, which are procedures that map current start and goal states, and bindings of other variables, to ....
5. Re-run the body-reported ablation/failure condition: In goal regression, when applying an operation to a goal g, the goal fluent and any side effect fluents are always removed from g; in addition, we remove any fluents in g ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS); the primary result is directionally consistent at p. 3 (B C), p. 6 (C C), p. 6 (C C); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 architecture, thought, doing mechanism이 First, it may not be possible to make pn true without undoing p1, . . . ... 대비 To operate in infinite domains, we augment the standard operator descriptions with the following features: Suggesters, which are ...을 개선하고, Because these variables both have infinite domains in our setting, we cannot enumerate them. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
