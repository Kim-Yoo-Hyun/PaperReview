# Evaluation - Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p060.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p060.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (B. Perception Manipulation Funnet), p. 8 (2 Sample grid points G - Area), p. 11 (Figure/Table caption)): Additionally, a maximum entropy-based method is introduced to improve convergence efficiency.

## Evaluation Body Digest

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Despite the trajectory being a dominant action representation in manipulation planning, itis unsuitable for funnel-based ‘manipulations as interactions with the task environment are allowed to ...
- **p. 6 / 2 Sample grid points G - Area - extractive body cue:** The physical manipulation funnel aims to leverage environmental contacts as physical constraints in the execution task space to iteratively reduce Ax for peg-in-hole insertion Based ...
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** energy under the non-penetration environmental constraints as Ulex) > Ulxea) > UEP)
- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** Since the footprint fully contains the projection of the intersection part beneath the board surface plane, the environmental constraints as defined in Eq.
- **p. 8 / 2 Sample grid points G - Area - extractive body cue:** Insertion under Motion Constraints: As constant contact between the peg and its matching hole is established, we aim to leverage the motion constraints from the ...
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** 6, the translation motion v is a result refined by the passive force from the environmental contacts.
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** The insertion process introduced by inclined angle adjustment after comer alignment is a manipulation funnel in the execution task space based on the general Definition ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 10); Experiments (p. 11).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B. Perception Manipulation Funnet | SYSTEM / EVALUATION SCOPE UNRESOLVED | Additionally, a maximum entropy-based method is introduced to improve convergence efficiency. | p. 6 (B. Perception Manipulation Funnet) |
| 2 Sample grid points G - Area | SYSTEM / EVALUATION SCOPE UNRESOLVED | Successful insertion motions are formulated as a sequence of interactions $ = [e},¢¥, ..¢?] that connect the initial inclined state to the target peg-inhole ... | p. 8 (2 Sample grid points G - Area) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation study on the physical manipulation funnel; ... | p. 11 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Despite the trajectory being a dominant action representation in manipulation planning, itis unsuitable for funnel-based ‘manipulations as interactions with the task environment are allowed to ...
- **p. 6 / 2 Sample grid points G - Area - extractive body cue:** The physical manipulation funnel aims to leverage environmental contacts as physical constraints in the execution task space to iteratively reduce Ax for peg-in-hole insertion Based ...
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** energy under the non-penetration environmental constraints as Ulex) > Ulxea) > UEP)
- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** Since the footprint fully contains the projection of the intersection part beneath the board surface plane, the environmental constraints as defined in Eq.
- **p. 8 / 2 Sample grid points G - Area - extractive body cue:** Insertion under Motion Constraints: As constant contact between the peg and its matching hole is established, we aim to leverage the motion constraints from the ...
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** 6, the translation motion v is a result refined by the passive force from the environmental contacts.
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** The insertion process introduced by inclined angle adjustment after comer alignment is a manipulation funnel in the execution task space based on the general Definition ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than expecting ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: (a) The task mechanics of peg-in-hole insertion: first, ‘constant contact between the peg and the hole is formed; second, the formed constraints are ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: The observation P,,oprin.+ from ef can be divided into binary categories, (a) contact point when /P,,soagrn.e] = 1
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: (a) The peg's state x; is projected as [2c
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 6: An overview of the motion constraints based on the XY-plane (planar view 1) and X Z-plane (planar view 2) of {C'} Planar View ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation study on the physical manipulation funnel; (d) ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 8: Overview of the Peg-in-Hole Tasks in Real-world
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 9: Experimental result of the uncertainty elimination process in simulation with different levels of action uncertainty

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Despite the trajectory being a dominant action representation in manipulation planning, itis unsuitable for funnel-based ‘manipulations as interactions with the task environment are allowed ... | embodiment, simulator version and control stack | p. 5 (A. Task Mechanics and Interaction Primitives), p. 6 (2 Sample grid points G - Area) |
| Task/environment | The physical manipulation funnel aims to leverage environmental contacts as physical constraints in the execution task space to iteratively reduce Ax for peg-in-hole insertion ... | reset, timeout, object/scene variation | p. 6 (2 Sample grid points G - Area), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 4 (A. Preliminaries), p. 4 (B. Problem Statement) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Such a formu lation offers several advantages: 1) when the peg engages with the task board from above (as illustrated in Fig. | definition/direction/unit from same section | p. 5 (A. Task Mechanics and Interaction Primitives) |
| To integrate the alignment mechanism as an inductive bias for interactions, the task-specific interaction ce = (xf,x1) is extended as ¢? - (xf,x1,p.) in ... | definition/direction/unit from same section | p. 5 (A. Task Mechanics and Interaction Primitives) |
| Via € RS and the angle value Oweni © R of Zvigert 10 describe the pose as W(x+) neral: Otaera> a8 illustrated in Fig. | definition/direction/unit from same section | p. 7 (2 Sample grid points G - Area) |
| As illustrated in Fig, 5-(c12), for an angle formed by the target comer vertex v= Tiong and its nearby vertices, its edges are considered ... | definition/direction/unit from same section | p. 7 (2 Sample grid points G - Area) |
| Successful insertion motions are formulated as a sequence of interactions $ = [e},¢¥, ..¢?] that connect the initial inclined state to the target peg-inhole ... | definition/direction/unit from same section | p. 8 (2 Sample grid points G - Area) |
| As long as ‘is in contact with the wall, the component of the energy gradient Foyegy that is normal to the wall is canceled ... | definition/direction/unit from same section | p. 8 (2 Sample grid points G - Area) |
| As illustrated in the Planar View 1 of Fig. | definition/direction/unit from same section | p. 9 (2 Sample grid points G - Area) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so that vs ... | comparison identity and matched condition | p. 7 (2 Sample grid points G - Area) |
| Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation study on the physical manipulation funnel; ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so that vs ... | component/input/data sensitivity | p. 7 (2 Sample grid points G - Area) |
| Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation study on the physical manipulation funnel; ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |
| Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| As long as ‘is in contact with the wall, the component of the energy gradient Foyegy that is normal to the wall is canceled ... | component/input/data sensitivity | p. 8 (2 Sample grid points G - Area) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process. | Additionally, a maximum entropy-based method is introduced to improve convergence efficiency. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (B. Perception Manipulation Funnet), p. 8 (2 Sample grid points G - Area), p. 11 (Figure/Table caption) |
| Primary metric/result | Successful insertion motions are formulated as a sequence of interactions $ = [e},¢¥, ..¢?] that connect the initial inclined state to the target peg-inhole ... | numeric claim only at cited anchor | p. 8 (2 Sample grid points G - Area) |

- Numeric sentences retained from the body:
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** 6, We denote the instantaneous relative motion of {.} with reference to {C'} at time t asa twist vector & = [wv]. in which w ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | pose +1 automatically falls into its nearby local minimum | p. 7 (2 Sample grid points G - Area) |
| body limitation/failure cue | The peg cannot break the alignment according to Lemma 4, as the result {M} is always lower than {C} in the work! frame. | p. 9 (2 Sample grid points G - Area) |
| body limitation/failure cue | Theoretically, the robustness of the insertion process is conditioned on the peg's state x, instead of its geometric size. | p. 9 (2 Sample grid points G - Area) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Proof: Since Xe is the intersection of 2; with another constraint set gev1(Tyouy) = 0 and {g4(Tyom) = 0} 4 {ae1(Tyouy) > 0} under ... | p. 6 (B. Perception Manipulation Funnet) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** pose +1 automatically falls into its nearby local minimum
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** The peg cannot break the alignment according to Lemma 4, as the result {M} is always lower than {C} in the work! frame.
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** Theoretically, the robustness of the insertion process is conditioned on the peg's state x, instead of its geometric size.

- **PDF anchors reviewed:** datasets p. 5 (A. Task Mechanics and Interaction Primitives), p. 6 (2 Sample grid points G - Area), p. 5 (A. Task Mechanics and Interaction Primitives), p. 7 (2 Sample grid points G - Area), p. 7 (2 Sample grid points G - Area), p. 8 (2 Sample grid points G - Area), metrics p. 1 (Figure/Table caption), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives), p. 7 (2 Sample grid points G - Area), p. 7 (2 Sample grid points G - Area), p. 8 (2 Sample grid points G - Area), baselines p. 7 (2 Sample grid points G - Area), p. 11 (Figure/Table caption), results p. 6 (B. Perception Manipulation Funnet), p. 8 (2 Sample grid points G - Area), p. 11 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
