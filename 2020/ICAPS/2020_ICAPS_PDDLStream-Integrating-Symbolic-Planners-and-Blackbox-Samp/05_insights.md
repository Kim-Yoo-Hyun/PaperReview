# Insights — PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/ICAPS/article/view/6739; PDF retrieval source: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; ...
- **p. 1 / Abstract - extractive body cue:** This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce ...
- **p. 1 / 1 Introduction - extractive body cue:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.
- **p. 1 / 1 Introduction - extractive body cue:** Each algorithm constructs and solves a sequence of finite PDDL problems, any off-theshelf PDDL planner to be used as a search subroutine.
- **Contribution anchor:** p. 1 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction), p. 1 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.
- **p. 1 / 1 Introduction - extractive body cue:** Adaptive greatly outperforms the two existing algorithms (Garrett, Lozano-P´erez, and Kaelbling 2018) on constrained and 440
- **p. 8 / 9 Experiments - extractive body cue:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.
- **Boundary to test:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; from AFOSR grant FA9550-17-1-0165; from ONR grant ... | p. 1 (1 Introduction), p. 1 (Abstract) |
| Reported outcome | Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan. | p. 8 (9 Experiments), p. 8 (9 Experiments) |
| Failure/limitation | Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. | p. 8 (9 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 The declarative component specifies the facts that these input and output values satisfy.를 The procedural component is a conditional generator, a function from input values to a possibly infinite sequence of output values.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; from AFOSR grant FA9550-17-1-0165; from ONR grant ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, task and motion planning, symbolic planning, sampling, manipulation planning`.
- **Reading predecessor in the generated track queue:** Information Theoretic MPC for Model-Based Reinforcement Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 9.1 Real-World Validation We applied PDDLStream to four real-world task and motion planning problems..
3. Compare against the body-reported baseline or a matched simpler baseline: The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018)..
4. Report the body metric and its denominator/aggregation: Figure 4: From left to right: Domain 3 success percent, Domain 3 mean runtime, and plan cost over time for Domain 2. evaluation time. An open-source Python implementation is available at https://github.com/caelan/pddlstream. ....
5. Re-run the body-reported ablation/failure condition: Figure 1: Left: Domain 1 (with 5 blocks). Right: A real- world robot planning to "serve a meal" on the brown tray. pling procedures in Planning Domain Definition Language (PDDL) (McDermott et ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (1 Introduction), p. 1 (1 Introduction); the primary result is directionally consistent at p. 8 (9 Experiments), p. 8 (9 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 PDDLStream, planning, language mechanism이 The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, ... 대비 Figure 4: From left to right: Domain 3 success percent, Domain 3 mean runtime, and plan cost over ...을 개선하고, Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
