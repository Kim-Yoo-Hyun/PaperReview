# Evaluation - Uncertainty-Aware Gaussian Map for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=LPv59noPAy; PDF retrieval source: https://openreview.net/pdf/465d0779d3489df4f9f1afa9b725d78970007e26.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT)): On the val unseen split, it achieves an SR of 78% compared to 76% from VER [17] and improves SPL from 65% to 66%, corresponding to gains of 2% in ...

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** All datasets are built upon the Matterport3D simulator [80], and are split into train, val-seen, val-unseen, and test sets according to scenes.
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** We evaluate our agent on three benchmarks, each posing distinct challenges for VLN.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** We compare our agent with VER [17] on the R2R val unseen split.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Our agent attains higher SR and nDTW (65.2% vs 64.1%, 65.6% vs 63.9%) and comparable SDTW (53.5% vs 52.6%) on theval unseensplit.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** 4.4 DIAGNOSTIC EXPERIMENT For thorough examination, we conduct a series of ablative studies on the val unseen split of R2R [1] and REVERIE [28].
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** In contrast, row #3 leverages only the uncertainty information (i.e., Table 4: Ablation studies on val unseen split of R2R [1] and REVERIE [28].
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by Path Length (SPL).
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** R2R [1] val unseen test unseen Method TL ↓ NE ↓ SR ↑ SPL ↑ TL ↓ NE ↓ SR ↑ SPL ↑ HAMT [76] ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 EXPERIMENT (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENT | EMPIRICAL / SIMULATION | On the val unseen split, it achieves an SR of 78% compared to 76% from VER [17] and improves SPL from 65% to 66%, ... | p. 8 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / SIMULATION | Row #4 reports the scores of our full framework. i) Row #1 vs #2: SGM leads to notable performance improvements against the baseline (e.g., ... | p. 9 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / SIMULATION | On the val unseen split, our agent outperforms the best reported results (i.e., BEVBert [15]) by a significant margin in terms of RGS (37.65% ... | p. 7 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / SIMULATION | For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by Path Length ... | p. 7 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / SIMULATION | Such improvements further demonstrate the benefit of the uncertainty information in long-horizon navigation. | p. 8 (4 EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** All datasets are built upon the Matterport3D simulator [80], and are split into train, val-seen, val-unseen, and test sets according to scenes.
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** We evaluate our agent on three benchmarks, each posing distinct challenges for VLN.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** We compare our agent with VER [17] on the R2R val unseen split.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Our agent attains higher SR and nDTW (65.2% vs 64.1%, 65.6% vs 63.9%) and comparable SDTW (53.5% vs 52.6%) on theval unseensplit.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** 4.4 DIAGNOSTIC EXPERIMENT For thorough examination, we conduct a series of ablative studies on the val unseen split of R2R [1] and REVERIE [28].
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** In contrast, row #3 leverages only the uncertainty information (i.e., Table 4: Ablation studies on val unseen split of R2R [1] and REVERIE [28].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Motivation. Previous VLN agents typically ignore perceptual uncertainty when making decisions. As a result, they often confuse visually similar structures (e.g., multiple doors) ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Pipeline overview. At each step, our agent constructs a Semantic Gaussian Map (§3.1) from its panoramic observation O = {I, D}. On top ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative results on REVERIE [28]. ‘-': unavailable statistics. See §4.2 for more details. REVERIE [28] val unseen test unseen
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3: Qualitative results on R2R [1]. (a) Under the instruction "straight towards the windows", VER [17] misinterprets the layout and stops early, whereas our ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Representative visual results on R2R [1]. At each step, we show the constructed SGM, the rendered observations, and the aggregated uncertainty map. While ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative results on R2R [1] val unseen. ‘-': unavailable statistics. See §4.2 for more details. R2R [1] val unseen test unseen
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative results on RxR [27] val unseen. ‘-': unavailable statistics. See §4.2.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Visualization of diverse perceptual forms. From left to right: current observation, SGM, rendered observation, geometric uncertainty map, semantic uncertainty map, appearance uncertainty map. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | All datasets are built upon the Matterport3D simulator [80], and are split into train, val-seen, val-unseen, and test sets according to scenes. | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Task/environment | We evaluate our agent on three benchmarks, each posing distinct challenges for VLN. | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3 METHOD), p. 6 (3 METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 7 (3 METHOD), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by Path Length ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENT) |
| R2R [1] val unseen test unseen Method TL ↓ NE ↓ SR ↑ SPL ↑ TL ↓ NE ↓ SR ↑ SPL ↑ HAMT ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |
| Row #4 reports the scores of our full framework. i) Row #1 vs #2: SGM leads to notable performance improvements against the baseline (e.g., ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENT) |
| On the val unseen split, it achieves an SR of 78% compared to 76% from VER [17] and improves SPL from 65% to 66%, ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |
| For row #2, the scores are obtained by using SGM as the 3D scene representation without uncertainty values. | definition/direction/unit from same section | p. 9 (4 EXPERIMENT) |
| Table 11: Statistical Significance Tests on R2R val unseen split. We report the mean ± std, confidence intervals (CI), and paired t-test p-values over ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Table 13: Effectiveness of Uncertainty Information on R2R val unseen split. The uncertainty infor- mation encoded in our 3D Value Map is rendered into ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| These improvements of 3.94% in RGS and 3.31% in RGSPL clearly demonstrate the effectiveness of our 3D Value Map for accurate navigation and precise ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENT) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by Path Length ... | comparison identity and matched condition | p. 7 (4 EXPERIMENT) |
| On the val unseen split, our agent outperforms the best reported results (i.e., BEVBert [15]) by a significant margin in terms of RGS (37.65% ... | comparison identity and matched condition | p. 7 (4 EXPERIMENT) |
| As shown in Table 2, our agent consistently surpasses recent state-of-the-art methods on R2R. | comparison identity and matched condition | p. 8 (4 EXPERIMENT) |
| On the val unseen split, it achieves an SR of 78% compared to 76% from VER [17] and improves SPL from 65% to 66%, ... | comparison identity and matched condition | p. 8 (4 EXPERIMENT) |
| Row #4 reports the scores of our full framework. i) Row #1 vs #2: SGM leads to notable performance improvements against the baseline (e.g., ... | comparison identity and matched condition | p. 9 (4 EXPERIMENT) |
| This demonstrates that the agent benefits from the geometric structure and semantic cues within SGM, achieving stronger navigation performance. ii) Row #1 vs #3: ... | comparison identity and matched condition | p. 9 (4 EXPERIMENT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Components R2R [1] REVERIE [28] # SGM 3DVM SR ↑ SPL ↑ SR ↑ RGS ↑ RGSPL ↑ 1 - - 72.22 60.41 46.98 ... | component/input/data sensitivity | p. 9 (4 EXPERIMENT) |
| (b) Our agent bypasses the obstacle and enters the designated region, while VER halts at the "table" without completing the task. | component/input/data sensitivity | p. 8 (4 EXPERIMENT) |
| For row #2, the scores are obtained by using SGM as the 3D scene representation without uncertainty values. | component/input/data sensitivity | p. 9 (4 EXPERIMENT) |
| Table 10: Sensitivity Analysis of uncertainty-related hyperparameters on R2R val unseen split. (a) δ and (b) η regulate geometric uncertainty, while (c) ε governs ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |
| Table 12: Robustness to observation noise on R2R val unseen split. We evaluate an epistemic only variant (geometric + semantic), an aleatoric only variant ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by ... | On the val unseen split, it achieves an SR of 78% compared to 76% from VER [17] and improves SPL from 65% to 66%, ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Primary metric/result | Row #4 reports the scores of our full framework. i) Row #1 vs #2: SGM leads to notable performance improvements against the baseline (e.g., ... | numeric claim only at cited anchor | p. 9 (4 EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** RxR [27] offers 126K multilingual instructions (i.e., English, Hindi, Telugu) over 16,522 trajectories, requiring the agent to cope with long-horizon navigation across diverse languages.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** R2R [1] val unseen test unseen Method TL ↓ NE ↓ SR ↑ SPL ↑ TL ↓ NE ↓ SR ↑ SPL ↑ HAMT [76] ...
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Method NE ↓ SR ↑ nDTW ↑ SDTW ↑ LSTM [27] 10.9 22.8 38.9 18.2 EnvDrop+ [84] - 42.6 55.7 - HAMT [76] - 56.5 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation already provides sufficient evidence of the ... | p. 22 (Figure/Table caption) |
| body limitation/failure cue | 5 illustrates our diverse perceptual forms. i) SGM preserves detailed geometric structures while maintaining high-fidelity rendering of the scene. ii) Geometric uncertainty reveals structural ... | p. 9 (4 EXPERIMENT) |
| body limitation/failure cue | Figure 1: Motivation. Previous VLN agents typically ignore perceptual uncertainty when making decisions. As a result, they often confuse visually similar structures (e.g., multiple ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Table 12: Robustness to observation noise on R2R val unseen split. We evaluate an epistemic only variant (geometric + semantic), an aleatoric only variant ... | p. 21 (Figure/Table caption) |
| body limitation/failure cue | To control SGM scale, we apply pruning thresholds τe and τα to filter out Gaussians with small scale (∥ei∥2 < τe) or low opacity ... | p. 9 (4 EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Pretraining is conducted for 100k iterations with a batch size of 64, optimized by Adam [78] with a learning rate of 1e-4. | p. 6 (3 METHOD) |
| These cases show how uncertainty helps disambiguate confounding structures and encode traversability constraints. | p. 8 (4 EXPERIMENT) |
| This demonstrates that the agent benefits from the geometric structure and semantic cues within SGM, achieving stronger navigation performance. ii) Row #1 vs #3: ... | p. 9 (4 EXPERIMENT) |
| Following the same principle, the rendered depth ˆD(u, v) and semantic ˆS(u, v) are computed as: ˆD(u, v) = X i ziα′ i Yi-1 ... | p. 4 (3 METHOD) |
| To quantify spatial reliability of SGM, we model position and scale parameters of each Gaussian as random variables with learnable perturbations χµ i ∈R3 ... | p. 4 (3 METHOD) |
| In traditional 3D scene reasoning and robotics, a value map represents a spatial field in which each element encodes task-relevant signals that guide downstream ... | p. 5 (3 METHOD) |
| (See details in Appendix.) 3.5 IMPLEMENTATION DETAILS Topological Memory. | p. 6 (3 METHOD) |
| (See details in Appendix.) Runtime Analysis. | p. 7 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 22 / Figure/Table caption - extractive PDF cue:** Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation already provides sufficient evidence of the target, ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** 5 illustrates our diverse perceptual forms. i) SGM preserves detailed geometric structures while maintaining high-fidelity rendering of the scene. ii) Geometric uncertainty reveals structural reliability, ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Motivation. Previous VLN agents typically ignore perceptual uncertainty when making decisions. As a result, they often confuse visually similar structures (e.g., multiple doors) ...
- **p. 21 / Figure/Table caption - extractive PDF cue:** Table 12: Robustness to observation noise on R2R val unseen split. We evaluate an epistemic only variant (geometric + semantic), an aleatoric only variant (appearance), ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** To control SGM scale, we apply pruning thresholds τe and τα to filter out Gaussians with small scale (∥ei∥2 < τe) or low opacity (αi ...

- **PDF anchors reviewed:** datasets p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), metrics p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 20 (Figure/Table caption), baselines p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), results p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
