# Insights — BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (43 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/li23s.html; PDF retrieval source: https://arxiv.org/pdf/2403.09227. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27].
- **p. 8 / Method - extractive body cue:** We also evaluate to what extent the simplifications we introduce in physics and actuation (grasping, motion execution) during training impact the performance of RL-Prim. during ...
- **p. 2 / 1 Introduction - extractive body cue:** We hope that the BEHAVIOR-1K benchmark, our survey, and our analysis will serve to support and guide the development of future embodied AI agents and ...
- **p. 7 / Method - extractive body cue:** We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL ...
- **p. 7 / Method - extractive body cue:** The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in the history observations ...
- **p. 8 / Method - extractive body cue:** 6.1), policy failures (i.e., selecting the wrong action primitive) dominate.
- **Contribution anchor:** p. 2 (1 Introduction), p. 8 (Method), p. 2 (1 Introduction), p. 7 (Method), p. 7 (Method), p. 8 (Method)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Concretely, the difficulties derive in part from the length of BEHAVIOR-1K's activities and the complexity of the physical manipulation required.
- **p. 2 / 1 Introduction - extractive body cue:** To calibrate the simulation-to-real gap of BEHAVIOR-1K, we provide an initial study on transferring solutions learned with a mobile manipulator in a simulated apartment to ...
- **p. 8 / Method - extractive body cue:** The failure cases are depicted in Fig.
- **p. 8 / Method - extractive body cue:** 6.1), policy failures (i.e., selecting the wrong action primitive) dominate.
- **p. 7 / Method - extractive body cue:** RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. and RL-Prim.Hist. with action primitives are able achieve decent performance.
- **p. 7 / Method - extractive body cue:** Furthermore, to accelerate training, the action primitives check only the feasibility (e.g., reachability, collisions) of the final configuration, e.g. the grasping pose for pick or ...
- **Boundary to test:** The failure cases are depicted in Fig.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27]. | p. 2 (1 Introduction), p. 8 (Method) |
| Reported outcome | Table 2: Task success rates across three baseline methods. RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. and RL-Prim.Hist. with action primitives are able achieve ... | p. 7 (Figure/Table caption), p. 8 (Method) |
| Failure/limitation | The failure cases are depicted in Fig. | p. 8 (Method), p. 8 (Method) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in the history observations (3 steps) as additional inputs to help ...를 We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL solution based on Soft Actor-Critic (SAC) [48]; ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The failure cases are depicted in Fig.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27].
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Benchmark, Embodied AI, long-horizon tasks, simulation, household robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The failure cases are depicted in Fig.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The survey reveals systematicity in what activities people want robots to do, but more importantly, highlights two key factors that we should prioritize when designing robotic benchmarks: diversity in the type of ....
3. Compare against the body-reported baseline or a matched simpler baseline: We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL solution based on Soft Actor-Critic (SAC) [48]; ....
4. Report the body metric and its denominator/aggregation: Following the metrics proposed in BEHAVIOR-100 [27], we report the success rate and efficiency metrics (distance traveled, time invested, and disarrangement caused) in Table 2 and 3, and the success score Q ....
5. Re-run the body-reported ablation/failure condition: We include an ablation analysis of the effect of these assumptions and simplifications in our evaluation (see Table 4)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (Method), p. 7 (Method), p. 8 (Method); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 8 (Method), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, BEHAVIOR-1K, Benchmark mechanism이 We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a ... 대비 Following the metrics proposed in BEHAVIOR-100 [27], we report the success rate and efficiency metrics (distance traveled, time ...을 개선하고, The failure cases are depicted in Fig. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
