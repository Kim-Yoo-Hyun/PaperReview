# Evaluation - NavBench: Probing Multimodal Large Language Models for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=nf8PKQKtl2; PDF retrieval source: https://arxiv.org/pdf/2506.01031. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5.3 Discussion), p. 9 (5.3 Discussion), p. 8 (C Progress Level), p. 7 (C Progress Level), p. 8 (C Progress Level), p. 4 (C Progress Level)): As shown in Table 2, the presence of map information consistently improves success rates, with the largest gain observed under medium difficulty, yielding an increase of 4.86 percentage points.

## Evaluation Body Digest

- **p. 5 / C Progress Level - extractive body cue:** Navigation Comprehension Source Raw Datasets R2R / RxR … Step A1 Extract Multimodal Navigation Data Step A2 Navigation Execution Sample Navigation Episodes MatterPort3D Simulator Step ...
- **p. 5 / C Progress Level - extractive body cue:** Statistics We report statistics in Figure 3(c), including distribution of comprehension subtasks and coverage of scenes and episodes in execution.
- **p. 6 / C Progress Level - extractive body cue:** 3.2.2 Navigation Episodes Collection We sample 432 navigation cases from 72 unique scenes in the Matterport3D simulator [55].
- **p. 8 / C Progress Level - extractive body cue:** Annotating the entire dataset with human responses is impractical due to scale, so we select 120 multiple-choice questions for the Global Instruction Alignment task, 100 ...
- **p. 7 / C Progress Level - extractive body cue:** For real-world deployment, we integrate our pipeline with a dual-arm composite mobile robot equipped with an Intel RealSense D435 camera and a Water Drop 2 ...
- **p. 7 / C Progress Level - extractive body cue:** To demonstrate the real-world feasibility of MLLMguided embodied navigation, we implement a modular pipeline that complements our benchmark evaluation, as illustrated in Figure 5.
- **p. 8 / C Progress Level - extractive body cue:** Among open-source models, Qwen2.5-VL-7B performs best (45.26%, 21.77%), approaching GPT-4o-mini (46.42%, 27.99%) and demonstrating potential for deployment in real-world robotics.
- **p. 9 / 5.3 Discussion - extractive body cue:** Effect of Map Information on Action Decisions Although our benchmark evaluations assume no access to map information, reflecting real-world constraints, we investigate whether providing map ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.3 Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, the presence of map information consistently improves success rates, with the largest gain observed under medium difficulty, yielding an ... | p. 9 (5.3 Discussion) |
| 5.3 Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 7, models show consistent performance across both, with GPT-4o clearly outperforming all others, consistent with its strong results in Navigation ... | p. 9 (5.3 Discussion) |
| C Progress Level | EMPIRICAL / REAL-ROBOT OR HARDWARE | Turning to comprehension subtasks, InternVL2.5-2B achieves strong performance on Global Instruction Alignment (67.25%), even surpassing GPT-4o (51.33%). | p. 8 (C Progress Level) |
| C Progress Level | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success Rate (SR) measures the percentage of episodes where the target object is visible from the agent's final viewpoint, defined as being within a ... | p. 7 (C Progress Level) |
| C Progress Level | EMPIRICAL / REAL-ROBOT OR HARDWARE | GPT-4o achieves the highest comprehension average (53.34%) and execution average (41.33%). | p. 8 (C Progress Level) |

## Dataset / Benchmark Role

- **p. 5 / C Progress Level - extractive body cue:** Navigation Comprehension Source Raw Datasets R2R / RxR … Step A1 Extract Multimodal Navigation Data Step A2 Navigation Execution Sample Navigation Episodes MatterPort3D Simulator Step ...
- **p. 5 / C Progress Level - extractive body cue:** Statistics We report statistics in Figure 3(c), including distribution of comprehension subtasks and coverage of scenes and episodes in execution.
- **p. 6 / C Progress Level - extractive body cue:** 3.2.2 Navigation Episodes Collection We sample 432 navigation cases from 72 unique scenes in the Matterport3D simulator [55].
- **p. 8 / C Progress Level - extractive body cue:** Annotating the entire dataset with human responses is impractical due to scale, so we select 120 multiple-choice questions for the Global Instruction Alignment task, 100 ...
- **p. 7 / C Progress Level - extractive body cue:** For real-world deployment, we integrate our pipeline with a dual-arm composite mobile robot equipped with an Intel RealSense D435 camera and a Water Drop 2 ...
- **p. 7 / C Progress Level - extractive body cue:** To demonstrate the real-world feasibility of MLLMguided embodied navigation, we implement a modular pipeline that complements our benchmark evaluation, as illustrated in Figure 5.
- **p. 8 / C Progress Level - extractive body cue:** Among open-source models, Qwen2.5-VL-7B performs best (45.26%, 21.77%), approaching GPT-4o-mini (46.42%, 27.99%) and demonstrating potential for deployment in real-world robotics.
- **p. 9 / 5.3 Discussion - extractive body cue:** Effect of Map Information on Action Decisions Although our benchmark evaluations assume no access to map information, reflecting real-world constraints, we investigate whether providing map ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: NavBench evaluates MLLMs across three comprehension tasks and a step-by-step execution task, assessing their ability to understand navigation behavior, track progress, reason about ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of the Navigation Comprehension task. introduce NavBench, a benchmark that systematically evaluates both the reasoning and execution capabilities of MLLMs in embodied ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: NavBench construction pipeline and statistics. (a) QA generation for comprehension tasks at global, progress, and local levels. (b) Execution pipeline combining automatic difficulty ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Radar chart of average complexity scores across cognitive, spatial, and execution dimensions for different difficulty levels. Difficulty Categorization Based on the final scores, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Overview of the real-world embodied navigation pipeline. To demonstrate the real-world feasibility of MLLM- guided embodied navigation, we implement a modular pipeline that ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison on Navigation Comprehension and Execution.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Model Performance under Different Instruction Perturbations.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Model performance on Local Observation-Action Reasoning. radius. Success weighted by Path Length (SPL) adjusts SR by path efficiency and is computed as SPL ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Navigation Comprehension Source Raw Datasets R2R / RxR … Step A1 Extract Multimodal Navigation Data Step A2 Navigation Execution Sample Navigation Episodes MatterPort3D Simulator ... | embodiment, simulator version and control stack | p. 5 (C Progress Level), p. 5 (C Progress Level) |
| Task/environment | Statistics We report statistics in Figure 3(c), including distribution of comprehension subtasks and coverage of scenes and episodes in execution. | reset, timeout, object/scene variation | p. 5 (C Progress Level), p. 6 (C Progress Level) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 4 (C Progress Level) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (C Progress Level), p. 8 (C Progress Level) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Their responses were automatically scored using the same metrics applied to model evaluation, including accuracy for comprehension tasks and SR/SPL for execution. | definition/direction/unit from same section | p. 8 (C Progress Level) |
| As shown in Table 2, the presence of map information consistently improves success rates, with the largest gain observed under medium difficulty, yielding an ... | definition/direction/unit from same section | p. 9 (5.3 Discussion) |
| Map SR SPL Avg Gain Easy ✗ 67.36 54.31 60.84 - ✓ 70.14 54.11 62.13 +1.29 Med. ✗ 41.67 35.71 38.69 - ✓ 46.53 ... | definition/direction/unit from same section | p. 9 (C Progress Level) |
| Success Rate (SR) measures the percentage of episodes where the target object is visible from the agent's final viewpoint, defined as being within a ... | definition/direction/unit from same section | p. 7 (C Progress Level) |
| Figure 7: Model performance on Local Observation-Action Reasoning. radius. Success weighted by Path Length (SPL) adjusts SR by path efficiency and is computed as ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 4: Radar chart of average complexity scores across cognitive, spatial, and execution dimensions for different difficulty levels. Difficulty Categorization Based on the final ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| To systematically assess the difficulty of each case, we define a composite complexity score across three orthogonal dimensions: spatial, cognitive, and execution complexity. | definition/direction/unit from same section | p. 6 (C Progress Level) |
| The spatial complexity score is defined as: Φspatial " α1 ¨ logp1 ` dq ` α2 ¨ logp1 ` θq ` α3 ¨ Ipz ... | definition/direction/unit from same section | p. 6 (C Progress Level) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Figure 7, models show consistent performance across both, with GPT-4o clearly outperforming all others, consistent with its strong results in Navigation ... | comparison identity and matched condition | p. 9 (5.3 Discussion) |
| Table 1: Performance comparison on Navigation Comprehension and Execution. | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Using GPT-4o, we compare performance with and without map input across different difficulty levels. | comparison identity and matched condition | p. 9 (5.3 Discussion) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Effect of Map Information on Action Decisions Although our benchmark evaluations assume no access to map information, reflecting real-world constraints, we investigate whether providing ... | component/input/data sensitivity | p. 9 (5.3 Discussion) |
| We design two variants: (1) Future-Observation Prediction - the model observes the current view and an action, and selects the correct resulting view. | component/input/data sensitivity | p. 4 (C Progress Level) |
| Using GPT-4o, we compare performance with and without map input across different difficulty levels. | component/input/data sensitivity | p. 9 (5.3 Discussion) |
| 3 Benchmark Design 3.1 Task Formulation We evaluate the navigation capabilities of MLLMs by decomposing the task into two core components: Navigation Comprehension, which ... | component/input/data sensitivity | p. 4 (C Progress Level) |
| The distractors are generated using four perturbation strategies: (1) Basic: random instructions sampled from unrelated trajectories, testing global relevance; (2) Directional replacements, where spatial ... | component/input/data sensitivity | p. 5 (C Progress Level) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are as follows: (1) We introduce NavBench, a benchmark for evaluating MLLMs in embodied navigation under zero-shot settings. | As shown in Table 2, the presence of map information consistently improves success rates, with the largest gain observed under medium difficulty, yielding an ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5.3 Discussion), p. 9 (5.3 Discussion), p. 8 (C Progress Level), p. 7 (C Progress Level), p. 8 (C Progress Level), p. 4 (C Progress Level) |
| Primary metric/result | As shown in Figure 7, models show consistent performance across both, with GPT-4o clearly outperforming all others, consistent with its strong results in Navigation ... | numeric claim only at cited anchor | p. 9 (5.3 Discussion) |

- Numeric sentences retained from the body:
- **p. 4 / C Progress Level - extractive body cue:** 3 Benchmark Design 3.1 Task Formulation We evaluate the navigation capabilities of MLLMs by decomposing the task into two core components: Navigation Comprehension, which assesses ...
- **p. 6 / C Progress Level - extractive body cue:** We collect 500 examples for each format, yielding a total of 1,000 samples.
- **p. 6 / C Progress Level - extractive body cue:** The score is computed as: Φexecution " γ1 ¨ logp1 ` Nq ` γ2 ¨ logp1 ` Tq ` γ3 ¨ F ` γ4 ¨ ...
- **p. 1 / Abstract - extractive body cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...
- **p. 2 / 1 Introduction - extractive body cue:** The benchmark includes 432 navigation cases across 72 scenes.
- **p. 4 / C Progress Level - extractive body cue:** 3 Benchmark Design 3.1 Task Formulation We evaluate the navigation capabilities of MLLMs by decomposing the task into two core components: Navigation Comprehension, which assesses ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Error Analysis We manually analyze 100 failed cases to understand model failures. | p. 9 (5.3 Discussion) |
| body limitation/failure cue | The models' failure in this setting highlights their limited ability to reason about temporal order within complex instructions. | p. 9 (5.3 Discussion) |
| body limitation/failure cue | All physical experiments are conducted in a controlled indoor lab to assess robustness and feasibility. | p. 7 (C Progress Level) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details Proprietary models are accessed via APIs, while open-source models are deployed using vLLM [64] and lmdeploy [65] on a single NVIDIA A6000 ... | p. 7 (C Progress Level) |
| Step-by-step Navigation Comprehension - Progress Level Given the steps taken so far, how far along am I in the instruction? | p. 1 (Body text (section not recovered)) |
| NavBench: Probing Multimodal Large Language Models for Embodied Navigation Yanyuan Qiao1 Haodong Hong23 Wenqi Lyu1 Dong An4 Siqi Zhang5 Yutong Xie4 Xinyu Wang1 Qi ... | p. 1 (Body text (section not recovered)) |
| Furthermore, navigation tasks in real-world environments can vary significantly in difficulty due to differences in spatial layout, instruction complexity, and required decision-making steps. | p. 2 (1 Introduction) |
| (c) Benchmark statistics, including comprehension (comp.) task distribution, QA counts, and execution statistics (e.g., instruction length, steps, distance). | p. 5 (C Progress Level) |
| Navigation Comprehension Source Raw Datasets R2R / RxR … Step A1 Extract Multimodal Navigation Data Step A2 Navigation Execution Sample Navigation Episodes MatterPort3D Simulator ... | p. 5 (C Progress Level) |
| These features are computed from agent poses and scene connectivity data. | p. 6 (C Progress Level) |
| We consider: (1) number of steps N, (2) number of turns T, (3) floor change indicator F, and (4) number of decision points D. | p. 6 (C Progress Level) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5.3 Discussion - extractive body cue:** Error Analysis We manually analyze 100 failed cases to understand model failures.
- **p. 9 / 5.3 Discussion - extractive body cue:** The models' failure in this setting highlights their limited ability to reason about temporal order within complex instructions.
- **p. 7 / C Progress Level - extractive body cue:** All physical experiments are conducted in a controlled indoor lab to assess robustness and feasibility.

- **Evidence anchors reviewed:** datasets p. 5 (C Progress Level), p. 5 (C Progress Level), p. 6 (C Progress Level), p. 8 (C Progress Level), p. 7 (C Progress Level), p. 7 (C Progress Level), metrics p. 8 (C Progress Level), p. 9 (5.3 Discussion), p. 9 (C Progress Level), p. 7 (C Progress Level), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 9 (5.3 Discussion), p. 8 (Figure/Table caption), p. 9 (5.3 Discussion), results p. 9 (5.3 Discussion), p. 9 (5.3 Discussion), p. 8 (C Progress Level), p. 7 (C Progress Level), p. 8 (C Progress Level), p. 4 (C Progress Level).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
