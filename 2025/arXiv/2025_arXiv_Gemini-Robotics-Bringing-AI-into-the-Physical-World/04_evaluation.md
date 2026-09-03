# Evaluation - Gemini Robotics: Bringing AI into the Physical World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.20020; PDF retrieval source: https://arxiv.org/abs/2503.20020. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (2.0 Pro Experimental)): (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories).

## Evaluation Body Digest

- **p. 5 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** Gemini Robotics: Bringing AI into the Physical World Gemini GPT Claude Benchmark
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** To capture progress in embodied reasoning for VLMs, we introduce ERQA, short for Embodied Reasoning Question Answering, a benchmark that focuses specifically on capabilities likely ...
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** Spatial Reasoning 84 Action Reasoning 72 Trajectory Reasoning 66 State Estimation 55 Task Reasoning 38 Multi-view Reasoning 37 Pointing 34 Other 14 Figure 4 / ...
- **p. 10 / 2.0 Pro Experimental - extractive body cue:** (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories).
- **p. 28 / 6. Discussion - extractive body cue:** In addition, while our initial results with Gemini Robotics demonstrate promising generalization capabilities, future work will focus on several key areas.
- **p. 28 / 6. Discussion - extractive body cue:** Robust human-level embodied reasoning is critical for robots and other physically grounded agents.
- **p. 29 / 6. Discussion - extractive body cue:** This involves developing techniques to seamlessly integrate abstract reasoning with precise execution, leading to more robust and generalizable performance.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark (p. 4); 2.0 Pro Experimental (p. 5); 2.0 Pro Experimental (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 2.0 Pro Experimental | EMPIRICAL / SOURCE-REPORTED EVALUATION | (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories). | p. 10 (2.0 Pro Experimental) |

## Dataset / Benchmark Role

- **p. 5 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** Gemini Robotics: Bringing AI into the Physical World Gemini GPT Claude Benchmark
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** To capture progress in embodied reasoning for VLMs, we introduce ERQA, short for Embodied Reasoning Question Answering, a benchmark that focuses specifically on capabilities likely ...
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** Spatial Reasoning 84 Action Reasoning 72 Trajectory Reasoning 66 State Estimation 55 Task Reasoning 38 Multi-view Reasoning 37 Pointing 34 Other 14 Figure 4 / ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption PDF body cue not selected; no claim inferred

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Gemini Robotics: Bringing AI into the Physical World Gemini GPT Claude Benchmark | embodiment, simulator version and control stack | p. 5 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark) |
| Task/environment | To capture progress in embodied reasoning for VLMs, we introduce ERQA, short for Embodied Reasoning Question Answering, a benchmark that focuses specifically on capabilities ... | reset, timeout, object/scene variation | p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 14 (3. Robot Actions with Gemini Robotics), p. 7 (2.0 Flash. Predicted point labels are not visualized) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 11 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 13 (2.0 Flash) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories). | definition/direction/unit from same section | p. 10 (2.0 Pro Experimental) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For each image pair, the left image with the point coordinates and the right image without coordinates are given, and the model predicts which ... | comparison identity and matched condition | p. 10 (2.0 Pro Experimental) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For each image pair, the left image with the point coordinates and the right image without coordinates are given, and the model predicts which ... | component/input/data sensitivity | p. 10 (2.0 Pro Experimental) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we introduce the Gemini Robotics family of embodied AI models, built on top of Gemini 2.0, our most advanced multimodal foundation ... | (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories). | PDF body cue; verify exact table/figure and matched conditions | p. 10 (2.0 Pro Experimental) |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** Spatial Reasoning 84 Action Reasoning 72 Trajectory Reasoning 66 State Estimation 55 Task Reasoning 38 Multi-view Reasoning 37 Pointing 34 Other 14 Figure 4 / ...
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** The Gemini Robotics backbone is formed by a distilled version of Gemini Robotics-ER and its query-to-response latency has been optimized from seconds to under 160ms.
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** When the backbone and local decoder are combined, the end-to-end latency from raw observations to low-level action chunks is approximately 250ms.
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** With multiple actions in the chunk (Zhao et al., 2023), the effective control frequency is 50Hz.
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** We collected a large-scale teleoperated robot action dataset on a fleet of ALOHA 2 robots (Team et al., 2024; Zhao et al., 2025) over 12 ...
- **p. 15 / 3. Robot Actions with Gemini Robotics - extractive body cue:** Gemini Robotics runs primarily in the cloud with a local action decoder, whereas both baselines run locally on a workstation equipped with an Nvidia RTX ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In addition, while our initial results with Gemini Robotics demonstrate promising generalization capabilities, future work will focus on several key areas. | p. 28 (6. Discussion) |
| body limitation/failure cue | Robust human-level embodied reasoning is critical for robots and other physically grounded agents. | p. 28 (6. Discussion) |
| body limitation/failure cue | This involves developing techniques to seamlessly integrate abstract reasoning with precise execution, leading to more robust and generalizable performance. | p. 29 (6. Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Gemini Robotics runs primarily in the cloud with a local action decoder, whereas both baselines run locally on a workstation equipped with an Nvidia ... | p. 15 (3. Robot Actions with Gemini Robotics) |
| backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini ... | p. 14 (3. Robot Actions with Gemini Robotics) |
| It consists of two components: a VLA backbone hosted in the cloud (Gemini Robotics backbone) and a local action decoder running on the robot's ... | p. 14 (3. Robot Actions with Gemini Robotics) |
| We compare Gemini Robotics to two state-of-the-art models: The first one is 𝜋0 reimplement, which is our re-implementation of the open-weights state-of-the-art 𝜋0 VLA ... | p. 15 (3. Robot Actions with Gemini Robotics) |
| Gemini Robotics brings Gemini's generalization to the physical world Lack of robust generalization is a key bottleneck for large-scale deployment of robots in domestic ... | p. 17 (3.3. Gemini Robotics can closely follow language instructions) |
| Right: success rate on "Pick" and "Pick and Place" tasks with detailed instructions for the new objects. diffusion baseline, even in simple in-distribution scenes, ... | p. 17 (3.3. Gemini Robotics can closely follow language instructions) |
| We speculate that these improvements result from the larger and more powerful VLM backbone, including the state-of-the-art vision encoder used in Gemini 2.0, combined ... | p. 19 (3.3. Gemini Robotics can closely follow language instructions) |
| We conduct 20 trials per task for each model for all tasks except for the spelling board game, for which 12 trials are conducted. | p. 21 (4.1. Long-horizon dexterity) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 28 / 6. Discussion - extractive body cue:** In addition, while our initial results with Gemini Robotics demonstrate promising generalization capabilities, future work will focus on several key areas.
- **p. 28 / 6. Discussion - extractive body cue:** Robust human-level embodied reasoning is critical for robots and other physically grounded agents.
- **p. 29 / 6. Discussion - extractive body cue:** This involves developing techniques to seamlessly integrate abstract reasoning with precise execution, leading to more robust and generalizable performance.

- **Evidence anchors reviewed:** datasets p. 5 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), metrics p. 10 (2.0 Pro Experimental), baselines p. 10 (2.0 Pro Experimental), results p. 10 (2.0 Pro Experimental).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (64 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Gemini Robotics: Bringing AI into the Physical World Gemini GPT Claude Benchmark (p. 5, 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark).
- **Metric evidence:** (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories). (p. 10, 2.0 Pro Experimental).
- **Baseline/ablation evidence:** For each image pair, the left image with the point coordinates and the right image without coordinates are given, and the model predicts which of the labeled points in the ... (p. 10, 2.0 Pro Experimental).
- **Failure/negative evidence:** While the PaliGemma-based 𝜋0 re-implement correctly approaches objects that were seen during training, it struggles with interpreting descriptive language attributes (e.g., "top black container", "blue clip") and fails to solve ... (p. 17, 3.3. Gemini Robotics can closely follow language instructions).
