# Insights — Dynamic Safety in Complex Environments: Synthesizing Safety Filters with Poisson's Equation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p137.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p137.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. IyrRopUCTION - extractive body cue:** The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** However. the condition V-v(y) <0 may not necessarily hold for all y < ©, which is sufficient to guarantee h(y) > 0 in 2. ‘To ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to ...
- **p. 2 / 1. IyrRopUCTION - extractive body cue:** We propose several methods for constructing the forcing function within Poisson's equation, including an average flux method and a guidance field method {26} that provides ...
- **p. 4 / IV. FORCING FUNCTION CONSTRUCTION - extractive body cue:** In this section, we present methods of designing forcing functions that ensure the solution to the boundary value problem for Poisson's equation (16) is a ...
- **Contribution anchor:** p. 2 (1. IyrRopUCTION), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach), p. 2 (1. IyrRopUCTION), p. 4 (IV. FORCING FUNCTION CONSTRUCTION)

### Strongest assumption and failure boundary

- **p. 1 / 1. IyrRopUCTION - extractive body cue:** which present challenges in synthesizing safe controllers.
- **p. 3 / B. Ouputs and Relative Degree - extractive body cue:** In what follows, we demonstrate how Poisson's equation can be leveraged to overcome these challenges and generate a single smooth function /: for environments with ...
- **p. 4 / A. Direct Assignment - extractive body cue:** This limitation makes this choice of f unsuitable for control design for systems with outputs of relative degree > Las defined in Def.
- **p. 4 / A. Direct Assignment - extractive body cue:** Following from Theorem 1, the forcing function (19) yields a safety function h€ C2(O; Roo) that lacks orders of differentiability higher than 2.
- **p. 1 / Abstract - extractive body cue:** The result isa variational problem for which sta safety function-characterizes the sale set.
- **p. 9 / 2 Nomina (Orange) & Safe (Bie) Inputs - extractive body cue:** ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, These ...
- **p. 7 / VI. DEMONSTRATIONS - extractive body cue:** Simulations: Double Integrator We define a 2D occupancy map defined by an open, bounded and connected domain © where J® characterizes obstacle surfaces. and consider ...
- **Boundary to test:** ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, These equilibria can manifest as "deadlocks", where ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) we illustrate and prove how the resulting ... | p. 2 (1. IyrRopUCTION), p. 6 (B. Indirect Assignment - Variational Approach) |
| Reported outcome | For dynamic environments, we improve the ‘computational speed of our PDE solver by warm-starting each PDE solution with the previous safety function, producing | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |
| Failure/limitation | ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, These equilibria can manifest as "deadlocks", where ... | p. 9 (2 Nomina (Orange) & Safe (Bie) Inputs), p. 7 (VI. DEMONSTRATIONS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to classes of systems with outputs of nonuniform ...를 Achieving this level of dynamic safety necessitates a quantifiable description of the safety requirement, i.e. a functional representation of the environment via a safety constraint, Additionally, this representation must be integrated ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, These equilibria can manifest as "deadlocks", where ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) we illustrate and prove how the resulting ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, safety filter, control barrier function, perception, humanoid, quadruped`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, These equilibria can manifest as "deadlocks", where ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: First, we perceive and segment the environment using fixed RGB camera and the Meta SAM2 [49] segmentation algorithm, Next, we generate a 2D occupancy map, buffered for robot size..
3. Compare against the body-reported baseline or a matched simpler baseline: In each ease, the nominal controller attempted to drive the system directly 10 the goal without safety considerations..
4. Report the body metric and its denominator/aggregation: ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several collision avoidance scenarios using Unitree's Go2 quadruped and G1 humanoid robots..
5. Re-run the body-reported ablation/failure condition: In each ease, the nominal controller attempted to drive the system directly 10 the goal without safety considerations..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at method anchor 없음; the primary result is directionally consistent at p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, threefold mechanism이 In each ease, the nominal controller attempted to drive the system directly 10 the goal without ... 대비 ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several ...을 개선하고, ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
