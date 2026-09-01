# Evaluation - Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=mIeKe74W43; PDF retrieval source: https://arxiv.org/pdf/2602.13810. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS)): Specifically, MVP consistently outperforms all baselines on Robomimic-square, Cube-doubletask4, and all Cube-triple tasks, where it consistently achieves the highest success rates.

## Evaluation Body Digest

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** We consider a total of 9 sparse-reward robotic manipulation tasks with varying difficulties.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** This includes 3 tasks from the Robomimic benchmark (Mandlekar et al., 2021), Lift, Can and Square, and 6 tasks from OGBench (Park et al., 2024), ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success Rate (a) Robomimic-lift 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Since robotic platforms often have limited computational resources, our experiments were conducted on a CPU-only environment, AMD Ryzen Threadripper 3960X 24-Core Processor.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Furthermore, benchmark results indicate that its success rate is very low, averaging only half of our MVP's.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** As shown in Table 1, our MVP matches or exceeds state-of-the-art multi-step flow-matching baselines on eight of nine tasks.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** In stark contrast, our MVP achieves success rates of 0.71 ± 0.06 and 0.52 ± 0.11 on these tasks, respectively.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** For example, the success rate on the challenging Cube-triple-task4 significantly increases from 0.30 ± 0.21 (with no IVC) to 0.45 ± 0.15 (with a partial ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); A.1 IMPLEMENTATION PROCEDURES OF POLICY UPDATE (p. 14); B SUPPLEMENTARY RESULTS (p. 18); B.1 NUMERICAL RESULTS OF ABLATION STUDY (p. 18).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Specifically, MVP consistently outperforms all baselines on Robomimic-square, Cube-doubletask4, and all Cube-triple tasks, where it consistently achieves the highest success rates. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | For instance, on the most difficult task, Cube-triple-task4, MVP achieves a success rate of 0.52 ± 0.11, which is significantly higher than the next-best ... | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our MVP achieves highest success rate and fastest training speed. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In stark contrast, our MVP achieves success rates of 0.71 ± 0.06 and 0.52 ± 0.11 on these tasks, respectively. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, benchmark results indicate that its success rate is very low, averaging only half of our MVP's. | p. 9 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** We consider a total of 9 sparse-reward robotic manipulation tasks with varying difficulties.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** This includes 3 tasks from the Robomimic benchmark (Mandlekar et al., 2021), Lift, Can and Square, and 6 tasks from OGBench (Park et al., 2024), ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success Rate (a) Robomimic-lift 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Since robotic platforms often have limited computational resources, our experiments were conducted on a CPU-only environment, AMD Ryzen Threadripper 3960X 24-Core Processor.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Furthermore, benchmark results indicate that its success rate is very low, averaging only half of our MVP's.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** As shown in Table 1, our MVP matches or exceeds state-of-the-art multi-step flow-matching baselines on eight of nine tasks.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** In stark contrast, our MVP achieves success rates of 0.71 ± 0.06 and 0.52 ± 0.11 on these tasks, respectively.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** For example, the success rate on the challenging Cube-triple-task4 significantly increases from 0.30 ± 0.21 (with no IVC) to 0.45 ± 0.15 (with a partial ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Performance-efficiency com- parison on 9 robotic manipulation tasks. A question naturally arises: Can we unify the expressive- ness of generative policies with the ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at a ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Training curves on benchmarks. The solid lines correspond to mean and shaded regions correspond to 95% confidence interval over five runs. The shadow ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Success rates. Mean ± Std over 5 seeds. Bold = best, underlined = 2nd-best. Task FQL BFN QC MVP (ours) Robomimic-lift 0.96 ± ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Training curves of ablation on the IVC. (2) Comparison with one-step variants of the aforementioned baselines. We compared our MVP against one-step variants ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Training curves of comparison with one-step flow.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison of online training speed Metric FQL BFN QC MVP (ours) Average 108.5 ± 7.7 iter/s
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Comparison of inference time Metric FQL BFN QC MVP (ours) Average 10.76 ± 1.02 ms

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We consider a total of 9 sparse-reward robotic manipulation tasks with varying difficulties. | embodiment, simulator version and control stack | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | This includes 3 tasks from the Robomimic benchmark (Mandlekar et al., 2021), Lift, Can and Square, and 6 tasks from OGBench (Park et al., ... | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 3 (3 METHOD), p. 2 (2 PRELIMINARIES) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 3 (3 METHOD), p. 4 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Overall, our MVP secures the top position with an average success rate of 0.88 ± 0.05. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Specifically, MVP consistently outperforms all baselines on Robomimic-square, Cube-doubletask4, and all Cube-triple tasks, where it consistently achieves the highest success rates. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Our MVP achieves highest success rate and fastest training speed. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2026 (Oral, top 1%) Table 1: Success rates. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Furthermore, benchmark results indicate that its success rate is very low, averaging only half of our MVP's. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| When considering FQL's overall low success rate and slow training speed, our MVP still maintains a significant advantage. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| We consider a total of 9 sparse-reward robotic manipulation tasks with varying difficulties. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Figure 6: Snapshots of the 9 challenging long-horizon, sparse-reward manipulation tasks. (7) Cube-triple-task2 (move): Three cubes are initialized at (0.35, -0.2, 0.02), (0.35, 0.0, ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Training curves of ablation on the IVC. (2) Comparison with one-step variants of the aforementioned baselines. We compared our MVP against one-step ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| As shown in Table 1, our MVP matches or exceeds state-of-the-art multi-step flow-matching baselines on eight of nine tasks. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Specifically, MVP consistently outperforms all baselines on Robomimic-square, Cube-doubletask4, and all Cube-triple tasks, where it consistently achieves the highest success rates. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Our full version (λ = 1.0) was compared against variants with a reduced constraint (λ = 0.5) and without the constraint (λ = 0.0). | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| To simulate a more realistic deployment scenario without hardware acceleration, we disabled JAX's Just-In-Time (JIT) compilation during all evaluations. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2026 (Oral, top 1%) 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success Rate (a) ... | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our full version (λ = 1.0) was compared against variants with a reduced constraint (λ = 0.5) and without the constraint (λ = 0.0). | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Figure 4: Training curves of ablation on the IVC. (2) Comparison with one-step variants of the aforementioned baselines. We compared our MVP against one-step ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| To simulate a more realistic deployment scenario without hardware acceleration, we disabled JAX's Just-In-Time (JIT) compilation during all evaluations. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Table 4: Ablation on the impact of IVC. Task MVP (λ = 0.0) MVP (λ = 0.5) MVP (λ = 1.0) Cube-triple-task3 0.65 ± ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized threefold: • We propose a new flow-based policy, namely mean velocity policy (MVP), that enables fastest one-step action generation. | Specifically, MVP consistently outperforms all baselines on Robomimic-square, Cube-doubletask4, and all Cube-triple tasks, where it consistently achieves the highest success rates. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Primary metric/result | For instance, on the most difficult task, Cube-triple-task4, MVP achieves a success rate of 0.52 ± 0.11, which is significantly higher than the next-best ... | numeric claim only at cited anchor | p. 7 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** This includes 3 tasks from the Robomimic benchmark (Mandlekar et al., 2021), Lift, Can and Square, and 6 tasks from OGBench (Park et al., 2024), ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success Rate (a) Robomimic-lift 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** On the remaining task, MVP ranks second, with a performance of 0.92, which is just 0.02 points below the top-performing baseline's score of 0.94.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** For instance, on the most difficult task, Cube-triple-task4, MVP achieves a success rate of 0.52 ± 0.11, which is significantly higher than the next-best baseline, ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Overall, our MVP secures the top position with an average success rate of 0.88 ± 0.05.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Task FQL BFN QC MVP (ours) Robomimic-lift 0.96 ± 0.03 1.00 ± 0.01 1.00 ± 0.00 1.00 ± 0.00 Robomimic-can 0.74 ± 0.11 0.82 ± ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | The poor performance of BFN and QC is primarily because they rely on a 10-step flow policy, which requires iterative computation to transform noise ... | p. 9 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| (3) Training and inference time analysis. | p. 8 (4 EXPERIMENTS) |
| The results are listed in Table 3. our MVP and FQL exhibit very similar inference times, with both approaches being significantly faster than BFN ... | p. 9 (4 EXPERIMENTS) |
| 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success Rate (a) Robomimic-lift 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 ... | p. 7 (4 EXPERIMENTS) |
| To simulate a more realistic deployment scenario without hardware acceleration, we disabled JAX's Just-In-Time (JIT) compilation during all evaluations. | p. 9 (4 EXPERIMENTS) |
| Specifically, we assume the specific target a∗has been selected in the previous Steps 1 and 2, then generation of the final action anew is ... | p. 14 (A.1 IMPLEMENTATION PROCEDURES OF POLICY UPDATE) |
| The difference between M(·/a∗) and πnew is that M(·/a∗) describes the action distribution conditioned on a specific target action a∗, whereas πnew represents the ... | p. 14 (A.1 IMPLEMENTATION PROCEDURES OF POLICY UPDATE) |
| Finally, the complete pseudo-code for our mean flow RL algorithm is provided. | p. 3 (3 METHOD) |
| (15): Lpolicy(θ) = LMF(θ) + λLIVC(θ), (19) where the balancing hyperparameter λ > 0 is called IVC coefficient, and the default value is 1.0. | p. 6 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at a ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** The poor performance of BFN and QC is primarily because they rely on a 10-step flow policy, which requires iterative computation to transform noise into ...

- **PDF anchors reviewed:** datasets p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), metrics p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), baselines p. 8 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), results p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
