# Evaluation - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2506.01844; PDF retrieval source: https://arxiv.org/pdf/2506.01844. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (4 Experiments), p. 12 (4 Experiments), p. 14 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments)): Asynchronous inference achieves similar success rates (left) but is significantly faster (middle) and complete more tasks (right) in fixed-time settings.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** For real-world evaluation, we collected three datasets using the SO-100 robot arm (Knight et al.) and 1 with SO-101 arm (Knight et al.), each corresponding ...
- **p. 8 / 4 Experiments - extractive body cue:** In particular, we benchmark real-world pick and placing capabilities3, stacking capabilities4, and sorting capabilities5 for the SO100 robot, alongside real-world pick and placing capabilities for ...
- **p. 10 / 4 Experiments - extractive body cue:** For fine-tuning on simulation benchmarks, we train for 100,000 steps with a batch size of 64, while for real-world tasks, we fine-tune for 200,000 steps.
- **p. 9 / 4 Experiments - extractive body cue:** 4.2 Robots Across simulation and real-world enviroments, we use a variety of robotic platforms. • SO100 and SO101 (Cadene et al., 2024).
- **p. 11 / 4 Experiments - extractive body cue:** For the SO101 benchmark, the model is trained on a combination of three datasets, and success rates are reported per task as well as on ...
- **p. 11 / 4 Experiments - extractive body cue:** Single-task Training ACT 70 50 25 48.3 Multi-task Training π0 (3.5B) 100 40 45 61.7 SmolVLA (0.45B) 75 90 70 78.3 Table 3 ∣Real-world benchmarks ...
- **p. 10 / 4 Experiments - extractive body cue:** In Table 2, we further evaluate SmolVLA on two major simulation benchmarks-LIBERO and Meta-World-using a multi-task training setup.
- **p. 9 / 4 Experiments - extractive body cue:** 7Datasets can be easily explored via visualize_dataset 8Pick-Place-Lego dataset: lerobot/svla_so101_pickplace.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 8); A.1 Community datasets (p. 20).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Asynchronous inference achieves similar success rates (left) but is significantly faster (middle) and complete more tasks (right) in fixed-time settings. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 5a, both inference modes achieve comparable success rates across three real-world tasks. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Sampling new observations more frequently (e.g., every 1 or 10 steps) significantly improves performance. | p. 14 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that, pretraining on community datasets leads to a substantial performance improvement (from 51.7 to 78.3). | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | SmolVLA outperforms both ACT (Zhao et al., 2023), which is trained individually on each task, and π0, a significantly larger model in terms of ... | p. 11 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** For real-world evaluation, we collected three datasets using the SO-100 robot arm (Knight et al.) and 1 with SO-101 arm (Knight et al.), each corresponding ...
- **p. 8 / 4 Experiments - extractive body cue:** In particular, we benchmark real-world pick and placing capabilities3, stacking capabilities4, and sorting capabilities5 for the SO100 robot, alongside real-world pick and placing capabilities for ...
- **p. 10 / 4 Experiments - extractive body cue:** For fine-tuning on simulation benchmarks, we train for 100,000 steps with a batch size of 64, while for real-world tasks, we fine-tune for 200,000 steps.
- **p. 9 / 4 Experiments - extractive body cue:** 4.2 Robots Across simulation and real-world enviroments, we use a variety of robotic platforms. • SO100 and SO101 (Cadene et al., 2024).
- **p. 11 / 4 Experiments - extractive body cue:** For the SO101 benchmark, the model is trained on a combination of three datasets, and success rates are reported per task as well as on ...
- **p. 11 / 4 Experiments - extractive body cue:** Single-task Training ACT 70 50 25 48.3 Multi-task Training π0 (3.5B) 100 40 45 61.7 SmolVLA (0.45B) 75 90 70 78.3 Table 3 ∣Real-world benchmarks ...
- **p. 10 / 4 Experiments - extractive body cue:** In Table 2, we further evaluate SmolVLA on two major simulation benchmarks-LIBERO and Meta-World-using a multi-task training setup.
- **p. 9 / 4 Experiments - extractive body cue:** 7Datasets can be easily explored via visualize_dataset 8Pick-Place-Lego dataset: lerobot/svla_so101_pickplace.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For real-world evaluation, we collected three datasets using the SO-100 robot arm (Knight et al.) and 1 with SO-101 arm (Knight et al.), each ... | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | In particular, we benchmark real-world pick and placing capabilities3, stacking capabilities4, and sorting capabilities5 for the SO100 robot, alongside real-world pick and placing capabilities ... | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 10 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (Abstract), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use a dataset (Kim et al., 2024; Pertsch et al., 2025)1 containing 1,693 episodes covering all tasks, and evaluate with 10 trials per ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Inference Success Rate (%) - Real World Pick-Place Stacking Sorting Avg Sync 75 90 70 78.3 Async 80 90 50 73.3 (a) ∣Performance (success ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| We report success rate (SR) as the primary metric across all benchmarks. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Success rates (%) for various policies. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Success Rate (%) - Simulation LIBERO Spatial Object Goal Long Avg. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| For both inference modes, we report the success rate and policy speed (Figure 5). | definition/direction/unit from same section | p. 12 (4 Experiments) |
| Larger capacities yield better success rates. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Expert width Success Rate (%) - LIBERO (w.r.t. | definition/direction/unit from same section | p. 13 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| SmolVLA outperforms other VLA-based approaches such as Octo (Team et al., 2024) and OpenVLA (Kim et al., 2024), as well as the diffusion policy ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| 4.4 Baselines We compare our model against two popular and strong baselines, both available in the LeRobot library (Cadene et al., 2024). π0 (Black ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| SmolVLA outperforms both ACT (Zhao et al., 2023), which is trained individually on each task, and π0, a significantly larger model in terms of ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| As shown in Table 6, cross-attention outperforms self-attention significantly. | comparison identity and matched condition | p. 12 (4 Experiments) |
| On average, it completes the task in 9.7 seconds, compared to 13.75 seconds in the synchronous setting (∼30% faster). | comparison identity and matched condition | p. 12 (4 Experiments) |
| Skipping every second layer is a competitive baseline. | comparison identity and matched condition | p. 13 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Effect of pretraining and multitask learning. | component/input/data sensitivity | p. 11 (4 Experiments) |
| We also compare against two variants of π0: one initialized from a vision-language model (Paligemma-3B), and another further pretrained on robotics datasets (intitialized from ... | component/input/data sensitivity | p. 10 (4 Experiments) |
| Unless otherwise noted, models are trained from scratch without any pretraining on robotics data. | component/input/data sensitivity | p. 12 (4 Experiments) |
| We study the effect of varying n on the overall performance. | component/input/data sensitivity | p. 14 (4 Experiments) |
| However, we observe in practice that the model can be trained for a much smaller number of steps without sacrificing significant performance levels. | component/input/data sensitivity | p. 10 (4 Experiments) |
| All ablations are conducted on the LIBERO benchmark. | component/input/data sensitivity | p. 12 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present SmolVLA, a compact and efficient vision-language agent optimized for training on consumer-grade GPUs and deployment on CPUs. | Asynchronous inference achieves similar success rates (left) but is significantly faster (middle) and complete more tasks (right) in fixed-time settings. | PDF body cue; verify exact table/figure and matched conditions | p. 12 (4 Experiments), p. 12 (4 Experiments), p. 14 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments) |
| Primary metric/result | As shown in Figure 5a, both inference modes achieve comparable success rates across three real-world tasks. | numeric claim only at cited anchor | p. 12 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive body cue:** To evaluate SmolVLA in simulation, we collected a new dataset for MetaWorld (Yu et al., 2020) comprising of 50 demonstrations for each of the 50 ...
- **p. 8 / 4 Experiments - extractive body cue:** For real-world evaluation, we collected three datasets using the SO-100 robot arm (Knight et al.) and 1 with SO-101 arm (Knight et al.), each corresponding ...
- **p. 8 / 4 Experiments - extractive body cue:** Each dataset contains demonstrations relative to one task, with 10 trajectories for each of 5 distinct starting positions, resulting in a total of 50 demonstrations ...
- **p. 8 / 4 Experiments - extractive body cue:** LIBERO assesses diverse visuomotor skills across four categoriesSpatial, Object, Goal, and Long-with 10 tasks per category (40 total).
- **p. 8 / 4 Experiments - extractive body cue:** We use a dataset (Kim et al., 2024; Pertsch et al., 2025)1 containing 1,693 episodes covering all tasks, and evaluate with 10 trials per task, ...
- **p. 8 / 4 Experiments - extractive body cue:** Meta-World evaluates generalization across 50 tasks of varying difficulty: easy, medium, hard, and very hard (Seo et al., 2023).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 5.1 Limitations We identify several limitations remaining in our contribution. | p. 14 (5 Discussion) |
| body limitation/failure cue | The robot exhibits greater robustness to shifts in object positions and external disturbances, and overall is capable to solve the same tasks a significantly ... | p. 12 (4 Experiments) |
| body limitation/failure cue | Success Rate (%) - Real World Policy In Distribution Out of Distribution Single-task Training ACT 70 40 SmolVLA (0.45B) 90 50 Table 4 ∣ ... | p. 11 (4 Experiments) |
| body limitation/failure cue | Similarly, on SO101 (see Table 4), SmolVLA surpasses ACT in both in-distribution and out-of-distribution (OOD) settings. | p. 11 (4 Experiments) |
| body limitation/failure cue | However, Table 12 shows that both very small and very large values of n degrade performance. | p. 14 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During pretraining, we train for 200,000 steps with a global batch size of 256 on all our community datasets. | p. 10 (4 Experiments) |
| Pretraining was conducted using 4 GPUs to accomodate for large batch size, but the model can easily be trained on a single GPU due ... | p. 10 (4 Experiments) |
| Inference Time (s) - Real World Total Avg Std Sync 137.5 13.75 2.42 Async 97.0 9.70 2.95 (b) ∣Task completion time. | p. 12 (4 Experiments) |
| A larger n allows the robot to execute more actions at inference time before needing to process new observations and predict the next chunk. | p. 14 (4 Experiments) |
| We use a dataset2 of 2,500 episodes (50 per task), and mirror the evaluation protocol used for LIBERO: 10 trials per task, with trials ... | p. 8 (4 Experiments) |
| We use a dataset (Kim et al., 2024; Pertsch et al., 2025)1 containing 1,693 episodes covering all tasks, and evaluate with 10 trials per ... | p. 8 (4 Experiments) |
| Hyperparameters have been optimized for Pick-Place and reused across tasks. | p. 12 (4 Experiments) |
| The VLM backbone consists of a vision encoder followed by an LLM. | p. 13 (4 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 5 Discussion - extractive body cue:** 5.1 Limitations We identify several limitations remaining in our contribution.
- **p. 12 / 4 Experiments - extractive body cue:** The robot exhibits greater robustness to shifts in object positions and external disturbances, and overall is capable to solve the same tasks a significantly larger ...
- **p. 11 / 4 Experiments - extractive body cue:** Success Rate (%) - Real World Policy In Distribution Out of Distribution Single-task Training ACT 70 40 SmolVLA (0.45B) 90 50 Table 4 ∣ Real-world ...
- **p. 11 / 4 Experiments - extractive body cue:** Similarly, on SO101 (see Table 4), SmolVLA surpasses ACT in both in-distribution and out-of-distribution (OOD) settings.
- **p. 14 / 4 Experiments - extractive body cue:** However, Table 12 shows that both very small and very large values of n degrade performance.

- **PDF anchors reviewed:** datasets p. 8 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), metrics p. 8 (4 Experiments), p. 12 (4 Experiments), p. 8 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), baselines p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), results p. 12 (4 Experiments), p. 12 (4 Experiments), p. 14 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
