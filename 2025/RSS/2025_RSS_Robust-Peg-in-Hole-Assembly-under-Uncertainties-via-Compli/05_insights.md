# Insights — Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p060.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p060.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process.
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Let n represents the positive direction of Z-axis of {'} with reference to {O} at the inclined state, we use a as the inclined angle ...
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** We first define the task-specific interactions based on the task mechanics in Section IV-A.
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** Then, we introsuce the formal approach to construct manipulation funnels in perception state space (Section IV-B) and execution task space (Section IV-C),
- **Contribution anchor:** p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING)

### Strongest assumption and failure boundary

- **p. 3 / A. Preliminaries - extractive body cue:** Fig, 2: (a) The peg-in-hole problem is considered as inserting peg into its matching hole on a planar board (a randomly generated peg is adopted ...
- **p. 4 / B. Problem Statement - extractive body cue:** As % shrinks over steps, the expected spread of Ton) decreases and the uncertainty range of the perceived hole's state is reduced,
- **p. 4 / A. Preliminaries - extractive body cue:** Except for the virtually defined desired state x}, any physical existing state Xe.1 during this process is constrained by its task environment as follows:
- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** pose +1 automatically falls into its nearby local minimum
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** The peg cannot break the alignment according to Lemma 4, as the result {M} is always lower than {C} in the work! frame.
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** Theoretically, the robustness of the insertion process is conditioned on the peg's state x, instead of its geometric size.
- **Boundary to test:** pose +1 automatically falls into its nearby local minimum

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process. | p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Reported outcome | Additionally, a maximum entropy-based method is introduced to improve convergence efficiency. | p. 6 (B. Perception Manipulation Funnet), p. 8 (2 Sample grid points G - Area) |
| Failure/limitation | pose +1 automatically falls into its nearby local minimum | p. 7 (2 Sample grid points G - Area), p. 9 (2 Sample grid points G - Area) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 An interaction command cy = (xe, x3) at time ¢ is defined by its starting state x, (considered steady as %¢ - 0) and a desired state x}.를 Execution Task Space: Let Ax be the deviation between the steady state x, and the peg-in-hole state x", Based ‘on the estimated state distribution of Pr:(Tow), we aim to shrink Ax at ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 pose +1 automatically falls into its nearby local minimum에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, peg-in-hole, compliance, uncertainty, assembly`.
- **Reading predecessor in the generated track queue:** Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** pose +1 automatically falls into its nearby local minimum; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Despite the trajectory being a dominant action representation in manipulation planning, itis unsuitable for funnel-based ‘manipulations as interactions with the task environment are allowed to alter the motion of the manipulator [39]..
3. Compare against the body-reported baseline or a matched simpler baseline: Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so that vs tends to rest atv; without escaping..
4. Report the body metric and its denominator/aggregation: Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than expecting the robot to precisely execute any t ....
5. Re-run the body-reported ablation/failure condition: Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so that vs tends to rest atv; without escaping..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING); the primary result is directionally consistent at p. 6 (B. Perception Manipulation Funnet), p. 8 (2 Sample grid points G - Area), p. 11 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 paired, comer, hole mechanism이 Specifically, our objective is to formulate a potential well to let vj be the local minimum ... 대비 Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process ...을 개선하고, pose +1 automatically falls into its nearby local minimum 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
