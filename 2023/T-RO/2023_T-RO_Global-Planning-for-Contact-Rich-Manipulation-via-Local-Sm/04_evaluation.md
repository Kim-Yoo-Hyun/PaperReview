# Evaluation - Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2206.10787; PDF retrieval source: https://arxiv.org/pdf/2206.10787. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 17 (Figure/Table caption), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 15 (Figure/Table caption), p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 11 (Figure/Table caption)): Fig. 11: Planning performance for the tasks in Fig. 10. Results include running RRT with the enhancements proposed in Sec. VII using the three smoothing schemes from Sec. II-C, as ...

## Evaluation Body Digest

- **p. 18 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** 2) Missed Contacts: Due to the non-smooth nature of contact dynamics, small discrepancies in object trajectory caused by the phase gap can lead to the ...
- **p. 18 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** 4) Hardware Setup: To verify results on actual hardware, we create a variant of the PlanarHand environment, where the object is replaced by a bucket, ...
- **p. 17 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** For this purpose, we run the obtained plans from Sec.VIII in open-loop on a higher fidelity simulator Drake [32], as well as an actual hardware ...
- **p. 17 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** In addition, we expect that the metric ∆will depend on how much movement is inside the reference trajectory of the plan.
- **p. 17 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** 2) Evaluation Metrics: To evaluate the performance of sim2real transfer, we first define the mean error ∆(·, ·) between the two trajectories qu sim(·) and ...
- **p. 18 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** 10, we obtain at least 10 segments and evaluate our error metrics.
- **p. 18 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** Last Two Columns: Box plot for the normalized error ¯∆for positions (third column) and orientation (fourth column).
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: Performance of iMPC with different smoothing schemes: analytic, randomized (first-order), randomized zero-order, and exact (no smoothing). For each method, the solid line represents ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** VIII. PLANNING RESULTS & DISCUSSION (p. 15); IX. SIM2REAL TRANSFER & HARDWARE RESULTS (p. 17).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 11: Planning performance for the tasks in Fig. 10. Results include running RRT with the enhancements proposed in Sec. VII using the three ... | p. 17 (Figure/Table caption) |
| IX. SIM2REAL TRANSFER & HARDWARE RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | On trajectory segments with good sim2real performance, this only results in harmless oscillations of qu real around qu sim. | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 9: (a-d) RRT trees, shown in the space of qu, at different iterations of a complete run of the enhanced RRT for the ... | p. 15 (Figure/Table caption) |
| IX. SIM2REAL TRANSFER & HARDWARE RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Rolling out u(·) on the real dynamics gives qreal : [0, T] →Rnu+na, which is compared against qsim(·) to evaluate the sim2real performance. | p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| IX. SIM2REAL TRANSFER & HARDWARE RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results & Discussion We plot the results of our experiments in Fig.12. | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |

## Dataset / Benchmark Role

- **p. 18 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** 2) Missed Contacts: Due to the non-smooth nature of contact dynamics, small discrepancies in object trajectory caused by the phase gap can lead to the ...
- **p. 18 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** 4) Hardware Setup: To verify results on actual hardware, we create a variant of the PlanarHand environment, where the object is replaced by a bucket, ...
- **p. 17 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** For this purpose, we run the obtained plans from Sec.VIII in open-loop on a higher fidelity simulator Drake [32], as well as an actual hardware ...
- **p. 17 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** In addition, we expect that the metric ∆will depend on how much movement is inside the reference trajectory of the plan.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Examples of contact-rich plans generated by our method. Each row corresponds to a time-snapshot of five different tasks: (a) 3D in-hand manipulation, (b) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Polynomial f (black) and its smooth surrogate fρ (red), for the case where ρ is a Gaussian (green). The plotted fρ is obtained ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: A. analytic, R.F. randomized first, R.Z. randomized zero. Left: ReLU f (black), its smooth surrogate fρ, the softplus (red), and the Monte-Carlo approximation ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Figure for Example 3, where quasi-dynamics of motion is interpreted as a projection operator. (a) Illustration of the system. (b) Distribution of q+w ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5: (a) A system consisting of an actuated cart constrained to slide on a frictionless surface, and a wall occupying qa ≤0. The actuator ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: Performance of iMPC with different smoothing schemes: analytic, randomized (first-order), randomized zero-order, and exact (no smoothing). For each method, the solid line represents ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7: Tasks and results for the trajectory optimization case study. Problem PlanarPushing PlanarHand AllegroHand
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 8: (a) Two different sublevel sets Ru ρ,ε,γ, represented as ellipsoids, shown in the space of qu, with ε = 1, and γ = ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 2) Missed Contacts: Due to the non-smooth nature of contact dynamics, small discrepancies in object trajectory caused by the phase gap can lead to ... | embodiment, simulator version and control stack | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| Task/environment | 4) Hardware Setup: To verify results on actual hardware, we create a variant of the PlanarHand environment, where the object is replaced by a ... | reset, timeout, object/scene variation | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 5 (II. LOCAL THEORY OF SMOOTHING), p. 2 (I. INTRODUCTION) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 7 (III. CONVEX QUASI-DYNAMIC DIFFERENTIABLE), p. 8 (IV. SMOOTHING OF CONTACT DYNAMICS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 2) Evaluation Metrics: To evaluate the performance of sim2real transfer, we first define the mean error ∆(·, ·) between the two trajectories qu sim(·) ... | definition/direction/unit from same section | p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| 10, we obtain at least 10 segments and evaluate our error metrics. | definition/direction/unit from same section | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| Last Two Columns: Box plot for the normalized error ¯∆for positions (third column) and orientation (fourth column). | definition/direction/unit from same section | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| Fig. 6: Performance of iMPC with different smoothing schemes: analytic, randomized (first-order), randomized zero-order, and exact (no smoothing). For each method, the solid line ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 1: Examples of contact-rich plans generated by our method. Each row corresponds to a time-snapshot of five different tasks: (a) 3D in-hand manipulation, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| In this section, we apply our algorithm on difficult 3D contactrich manipulation problems previously only tackled by heavy offline approaches in RL [2], [38], ... | definition/direction/unit from same section | p. 15 (VIII. PLANNING RESULTS & DISCUSSION) |
| Rolling out u(·) on the real dynamics gives qreal : [0, T] →Rnu+na, which is compared against qsim(·) to evaluate the sim2real performance. | definition/direction/unit from same section | p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| Fig. 5: (a) A system consisting of an actuated cart constrained to slide on a frictionless surface, and a wall occupying qa ≤0. The ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Rolling out u(·) on the real dynamics gives qreal : [0, T] →Rnu+na, which is compared against qsim(·) to evaluate the sim2real performance. | comparison identity and matched condition | p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| Fig. 8: (a) Two different sublevel sets Ru ρ,ε,γ, represented as ellipsoids, shown in the space of qu, with ε = 1, and γ ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Fig. 9: (a-d) RRT trees, shown in the space of qu, at different iterations of a complete run of the enhanced RRT for the ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |
| Fig. 11: Planning performance for the tasks in Fig. 10. Results include running RRT with the enhancements proposed in Sec. VII using the three ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 11: Planning performance for the tasks in Fig. 10. Results include running RRT with the enhancements proposed in Sec. VII using the three ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Fig. 9: (a-d) RRT trees, shown in the space of qu, at different iterations of a complete run of the enhanced RRT for the ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| 4) Hardware Setup: To verify results on actual hardware, we create a variant of the PlanarHand environment, where the object is replaced by a ... | component/input/data sensitivity | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| Fig. 13: Hardware for the IiwaBimanual setup, where the goal is to rotate the bucket by 180◦. The left and right pictures correspond to ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our first contribution is to establish the theoretical equivalence of the two smoothing schemes for simple systems under our framework (Sec.II,IV-C). | Fig. 11: Planning performance for the tasks in Fig. 10. Results include running RRT with the enhancements proposed in Sec. VII using the three ... | PDF body cue; verify exact table/figure and matched conditions | p. 17 (Figure/Table caption), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 15 (Figure/Table caption), p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 11 (Figure/Table caption) |
| Primary metric/result | On trajectory segments with good sim2real performance, this only results in harmless oscillations of qu real around qu sim. | numeric claim only at cited anchor | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |

- Numeric sentences retained from the body:
- **p. 18 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** System abbreviations: AH(AllegroHand), AHPe(AllegroPen), AHPl (AllegroPlate), PP(PlanarPushing), PH(PlanarHand), AHD (AllegroDoor), IB(IiwaBimanual) the length of the trajectory in the original plan, and denote the normalized error ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | These experiments further shed light on the efficacy and the limitations of our proposed method. | p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| body limitation/failure cue | The collision geometries, robot controller stiffness and coefficients of friction are kept consistent between the CQDC dynamics and Drake. | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| body limitation/failure cue | However, the necessary damping to uphold the quasidynamic assumption does not always exist on 3D systems. | p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For the dynamics derivatives (Sec.III-C), we have a custom implementation for differentiating through the KKT optimality conditions of an SOCP using Eigen's [57] linear ... | p. 7 (III. CONVEX QUASI-DYNAMIC DIFFERENTIABLE) |
| In this section, we apply our algorithm on difficult 3D contactrich manipulation problems previously only tackled by heavy offline approaches in RL [2], [38], ... | p. 15 (VIII. PLANNING RESULTS & DISCUSSION) |
| For this purpose, we run the obtained plans from Sec.VIII in open-loop on a higher fidelity simulator Drake [32], as well as an actual ... | p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |
| Each row corresponds to a time-snapshot of five different tasks: (a) 3D in-hand manipulation, (b) plate pickup using extrinsic dexterity, (c) door opening with ... | p. 1 (I. INTRODUCTION) |
| We further show that the gradients of the smoothed contact model can be easily computed with the implicit function theorem. | p. 2 (I. INTRODUCTION) |
| Most importantly, the model should be able to (iii) predict long-term behavior, so that the planner can look far ahead while taking few steps. | p. 2 (I. INTRODUCTION) |
| Before discussing complex systems with contact, we formalize mathematically what it means to smooth a function, as well as different algorithms to compute their ... | p. 3 (II. LOCAL THEORY OF SMOOTHING) |
| We investigate three major methods to compute these quantities. | p. 4 (II. LOCAL THEORY OF SMOOTHING) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 17 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** These experiments further shed light on the efficacy and the limitations of our proposed method.
- **p. 18 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** The collision geometries, robot controller stiffness and coefficients of friction are kept consistent between the CQDC dynamics and Drake.
- **p. 18 / IX. SIM2REAL TRANSFER & HARDWARE RESULTS - extractive body cue:** However, the necessary damping to uphold the quasidynamic assumption does not always exist on 3D systems.

- **Evidence anchors reviewed:** datasets p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), metrics p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 11 (Figure/Table caption), p. 1 (Figure/Table caption), p. 15 (VIII. PLANNING RESULTS & DISCUSSION), baselines p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 13 (Figure/Table caption), p. 15 (Figure/Table caption), p. 17 (Figure/Table caption), results p. 17 (Figure/Table caption), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 15 (Figure/Table caption), p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 11 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** On trajectory segments with good sim2real performance, this only results in harmless oscillations of qu real around qu sim. (p. 18, IX. SIM2REAL TRANSFER & HARDWARE RESULTS).
- **Metric evidence:** 2) Evaluation Metrics: To evaluate the performance of sim2real transfer, we first define the mean error ∆(·, ·) between the two trajectories qu sim(·) and qu real(·) as ∆(qu sim, ... (p. 17, IX. SIM2REAL TRANSFER & HARDWARE RESULTS).
- **Baseline/ablation evidence:** Rolling out u(·) on the real dynamics gives qreal : [0, T] →Rnu+na, which is compared against qsim(·) to evaluate the sim2real performance. (p. 17, IX. SIM2REAL TRANSFER & HARDWARE RESULTS).
- **Failure/negative evidence:** The consequence of these failed grasps is that plates are dropped on the table in AllegroHandPlate, and door handles are missed in AllegroHandDoor. (p. 19, IX. SIM2REAL TRANSFER & HARDWARE RESULTS).
