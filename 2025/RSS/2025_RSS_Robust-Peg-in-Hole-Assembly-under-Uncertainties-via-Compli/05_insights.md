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

- **Paper-specific interface:** Execution Task Space: Let Ax be the deviation between the steady state x, and the peg-in-hole state x", Based ‘on the estimated state distribution of Pr:(Tow), we aim to shrink ... (p. 4, B. Problem Statement).
- **Paper-specific mechanism:** By examining the role of compliance under contact constraints, ‘we present a manipulation system that plans coli (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than expecting the robot to precisely execute ... (p. 1, Figure/Table caption); the relevant task/metric cue is Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation study on the physical manipulation funnel; (d) Performance evaluation on the overall ... (p. 11, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We acknowledge the gap between the established objectcentric theory and real-world implementation; the failure mode can be divided into the following categories: 1) high contact force which breaks the condition ... (p. 12, 1 Liye).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, peg-in-hole, compliance, uncertainty, assembly`.
- **Reading predecessor in the generated track queue:** Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** pose +1 automatically falls into its nearby local minimum; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Execution Task Space: Let Ax be the deviation between the steady state x, and the peg-in-hole state x", Based ‘on the estimated state distribution of Pr:(Tow), we aim to shrink ... (p. 4, B. Problem Statement); preserve the objective/update rule: Interaction with inclined states is designed to identify and exploit its environmental contact constraints. (p. 5, A. Task Mechanics and Interaction Primitives).
2. Use the paper-reported task/data/environment cue: Despite the trajectory being a dominant action representation in manipulation planning, itis unsuitable for funnel-based ‘manipulations as interactions with the task environment are allowed to alter the motion of the ... (p. 5, A. Task Mechanics and Interaction Primitives).
3. Compare against the reported or matched baseline: Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so that vs tends to rest atv; without escaping. (p. 7, 2 Sample grid points G - Area).
4. Report the body metric with its denominator and aggregation: Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation study on the physical manipulation funnel; (d) Performance evaluation on the overall ... (p. 11, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so that vs tends to rest atv; without escaping. (p. 7, 2 Sample grid points G - Area); if none is reported, design one around: We acknowledge the gap between the established objectcentric theory and real-world implementation; the failure mode can be divided into the following categories: 1) high contact force which breaks the condition ... (p. 12, 1 Liye).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 5 (A. Task Mechanics and Interaction Primitives), match the reported outcome at p. 1 (Figure/Table caption), p. 11 (Figure/Table caption), p. 12 (Figure/Table caption), and measure the boundary at p. 12 (1 Liye), p. 10 (V. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (Execution Task Space: Let Ax be the deviation between the steady state x, and the peg-in-hole state x", Based ‘on the estimated ...), does the paper-specific mechanism (By examining the role of compliance under contact constraints, ‘we present a manipulation system that plans coli) retain the reported evaluation outcome (Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation ...) when tested against the paper's strongest explicit boundary (We acknowledge the gap between the established objectcentric theory and real-world implementation; the failure mode can be divided ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** By examining the role of compliance under contact constraints, ‘we present a manipulation system that plans coli (p. 1, Abstract).
- **Paper-supported outcome:** Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than expecting the robot to precisely execute ... (p. 1, Figure/Table caption).
- **Strongest explicit boundary:** We acknowledge the gap between the established objectcentric theory and real-world implementation; the failure mode can be divided into the following categories: 1) high contact force which breaks the condition ... (p. 12, 1 Liye).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
