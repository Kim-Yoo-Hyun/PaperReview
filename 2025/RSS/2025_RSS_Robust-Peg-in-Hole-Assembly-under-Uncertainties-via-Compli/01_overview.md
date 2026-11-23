# Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p060.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p060.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Yiting Chen, Kenneth Kimble, Howard H. Qian, Podshara Chanrungmaneekul, Robert Seney, Kaiyu Hang
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, contact-rich manipulation, peg-in-hole, compliance, uncertainty, assembly
- Official paper: https://www.roboticsproceedings.org/rss21/p060.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p060.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

이 연구는 순응 제어로 접촉을 의도적으로 만들고 그 제약을 활용해 구멍 위치가 불확실한 정밀 삽입을 수행한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p060.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robust and adaptive robotic peg-in-hole assembly. tunder tight tolerances is e
- **p. 1 / Abstract - extractive body cue:** However, it remains an physical uncertainties from contact-rie exceed the allowed clearance.
- **p. 1 / Abstract - extractive body cue:** In this paper, we study hon age contact between the peg and its matching hole to ‘uncertainties in the assembly process under unstructured settings.
- **p. 1 / Abstract - extractive body cue:** By examining the role of compliance under contact constraints, ‘we present a manipulation system that plans coli
- **p. 1 / Abstract - extractive body cue:** interactions for the peg to 1) iter
- **p. 3 / A. Preliminaries - extractive body cue:** Fig, 2: (a) The peg-in-hole problem is considered as inserting peg into its matching hole on a planar board (a randomly generated peg is adopted ...
- **p. 4 / B. Problem Statement - extractive body cue:** As % shrinks over steps, the expected spread of Ton) decreases and the uncertainty range of the perceived hole's state is reduced,

## Core Idea

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process.
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Let n represents the positive direction of Z-axis of {'} with reference to {O} at the inclined state, we use a as the inclined angle ...
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** We first define the task-specific interactions based on the task mechanics in Section IV-A.
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** Then, we introsuce the formal approach to construct manipulation funnels in perception state space (Section IV-B) and execution task space (Section IV-C),

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | An interaction command cy = (xe, x3) at time ¢ is defined by its starting state x, (considered steady as %¢ - 0) and a desired state x}. | RGB-D/point cloud, object state와 contact/task observation | p. 4 (A. Preliminaries), p. 4 (B. Problem Statement) |
| State/latent | interaction, command, time, defined, starting, state, considered, steady, desired, Execution, Task, Space | object geometry, affordance, contact mode 또는 end-effector state | p. 4 (A. Preliminaries), p. 4 (B. Problem Statement), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Output/action | Execution Task Space: Let Ax be the deviation between the steady state x, and the peg-in-hole state x", Based ‘on the estimated state distribution of Pr:(Tow), we aim to shrink Ax at ... | grasp, pose, force 또는 end-effector trajectory | p. 4 (B. Problem Statement), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Objective/outcome | forming an aligned comer between the inclined peg and the target hole to create contact constraints for undesired motion freedoms and progressively enter the allowed clearance (as illustrated in Fig. | task completion, contact success, pose/force error와 generalization | p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |

## Main Claims and Actual Contribution

- 탐색 접촉으로 구멍을 국소화하는 과정과 삽입 오차를 줄이는 과정을 서로 다른 상태 공간의 퍼널로 구성했다. [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p060.pdf#page=4) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p060.pdf#page=6)
- NIST 조립 보드와 추가 부품에서 치수·형상·재료가 달라질 때 별도의 정책 학습 없이 삽입을 검증했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p060.pdf#page=1) · [PDF 10쪽](https://www.roboticsproceedings.org/rss21/p060.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (B. Perception Manipulation Funnet), p. 8 (2 Sample grid points G - Area) |
| Embodiment/environment | Despite the trajectory being a dominant action representation in manipulation planning, itis unsuitable for funnel-based ‘manipulations as interactions with the task environment are allowed to alter the motion of the manipulator [39]. | hardware/simulator version and reset protocol | p. 5 (A. Task Mechanics and Interaction Primitives), p. 6 (2 Sample grid points G - Area) |
| Dataset/benchmark | Interaction with inclined states is designed to identify and exploit its environmental contact constraints. | role, split, size and leakage | p. 5 (A. Task Mechanics and Interaction Primitives), p. 6 (2 Sample grid points G - Area), p. 5 (A. Task Mechanics and Interaction Primitives), p. 7 (2 Sample grid points G - Area) |
| Metric | Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than expecting the robot to precisely execute any t ... | definition, denominator, direction and uncertainty | p. 1 (Figure/Table caption), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Baseline/ablation | Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so that vs tends to rest atv; without escaping. | fair input/data/compute/action matching | p. 7 (2 Sample grid points G - Area), p. 11 (Figure/Table caption), p. 7 (2 Sample grid points G - Area) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** pose +1 automatically falls into its nearby local minimum
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** The peg cannot break the alignment according to Lemma 4, as the result {M} is always lower than {C} in the work! frame.
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** Theoretically, the robustness of the insertion process is conditioned on the peg's state x, instead of its geometric size.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (A. Preliminaries), p. 4 (B. Problem Statement), p. 4 (A. Preliminaries), p. 5 (A. Task Mechanics and Interaction Primitives), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** As % shrinks over steps, the expected spread of Ton) decreases and the uncertainty range of the perceived hole's state is reduced, (p. 4, B. Problem Statement).
- **Actual contribution:** By examining the role of compliance under contact constraints, ‘we present a manipulation system that plans coli (p. 1, Abstract).
- **Evaluation boundary:** Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than expecting the robot to precisely execute ... (p. 1, Figure/Table caption).
- **Explicit failure boundary:** We acknowledge the gap between the established objectcentric theory and real-world implementation; the failure mode can be divided into the following categories: 1) high contact force which breaks the condition ... (p. 12, 1 Liye).
