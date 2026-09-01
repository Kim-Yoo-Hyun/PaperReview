# Insights — Rapidly-Exploring Random Trees: A New Tool for Path Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (4 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://lavalle.pl/rrtpubs.html; PDF retrieval source: https://lavalle.pl/papers/Lav98c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints.
- **p. 1 / 1 Introduction - extractive body cue:** Both are designed with as few heutisties and arbitrary
- **p. 2 / 3. Nice Properties of RRTs - extractive body cue:** The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis ...
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** Path planning will generally be viewed as a search in a metric space, X, foF a continuous path from an initial state, nie to A ...
- **p. 1 / 1 Introduction - extractive body cue:** Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** For these reasons and out preliminary observations from. experimentation, it appears that an RRT-based planner may generally yield better performance than a probabilistic roadmap-based planner; ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** This leads to a ptobabilistically complete [4] holonomic planner.
- **Contribution anchor:** p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (3. Nice Properties of RRTs), p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction), p. 3 (3. Nice Properties of RRTs)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems.
- **p. 1 / 1 Introduction - extractive body cue:** For planning of holonomic systems or steerable nonholonomic systems (see [6] and references therein), the local planning step might be efficient; however, in general, the ...
- **p. 2 / 9 Return T - extractive body cue:** Collision detection can be performed by an incremental method such as Mirtich's V-Clip.
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with an obstacle in the world, or several ...
- **p. 3 / 4 Examples - extractive body cue:** In a related paper [7], we presented an RRT-based, planner that computes collision-free kinodynamic trajec~ tories that fire thrusters for hovercrafts and satellites in, cluttered ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Collision detection is a key bottleneck in path planning, and an RRT is completely suited for incremental collision detection, This allows the fastest-avaliable collision detection ...
- **Boundary to test:** Collision detection can be performed by an incremental method such as Mirtich's V-Clip.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints. | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | For holonomie planning, one can define (ru) = and /lull <1, which implies that any bounded velocity can be achieved. | p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract) |
| Failure/limitation | Collision detection can be performed by an incremental method such as Mirtich's V-Clip. | p. 2 (9 Return T), p. 2 (2. Rapidly-Exploring Random Trees) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 Step 5 selects an input, w, that m rizes the distance from year tO rand» and ensures that the state remains in Xj,,..를 A state transition equation of the form # = f(2,u) is defined to express the nonholonomic constraints, The vector u is selected from a set, U, of inputs.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Collision detection can be performed by an incremental method such as Mirtich's V-Clip.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, motion planning, RRT, kinodynamic planning`.
- **Reading predecessor in the generated track queue:** Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** CHOMP: Gradient Optimization Techniques for Efficient Motion Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Collision detection can be performed by an incremental method such as Mirtich's V-Clip.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many other applica. tions..
3. Compare against the body-reported baseline or a matched simpler baseline: The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an RRT approaches ....
4. Report the body metric and its denominator/aggregation: The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an RRT approaches ....
5. Re-run the body-reported ablation/failure condition: The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an RRT approaches ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (3. Nice Properties of RRTs), p. 1 (Abstract), p. 2 (2. Rapidly-Exploring Random Trees); the primary result is directionally consistent at p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract), p. 1 (1 Introduction); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, randomized, data mechanism이 The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward ... 대비 The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions ...을 개선하고, Collision detection can be performed by an incremental method such as Mirtich's V-Clip. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
