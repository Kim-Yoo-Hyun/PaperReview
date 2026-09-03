# Evaluation - RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=itonej9GIV; PDF retrieval source: https://openreview.net/pdf/7cbb20fa3292d18ddb89823a5e7c3df7e52a3eb3.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiment), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 8 (4 Experiment), p. 18 (Figure/Table caption), p. 10 (4 Experiment)): Results show that our method improves success rates, particularly for robots with constrained planning spaces, achieving an average improvement of 8.3% across all embodiments.

## Evaluation Body Digest

- **p. 7 / 4 Experiment - extractive body cue:** We design experiments to evaluate the effectiveness of RoboTwin 2.0 in three key aspects: (1) automating the generation of high-quality expert code for manipulation tasks; ...
- **p. 10 / 4 Experiment - extractive body cue:** We compare three training settings: (1) 10 real-world demonstrations in clean tabletop environments; (2) the same demonstrations augmented with 1,000 domain-randomized synthetic trajectories generated under ...
- **p. 10 / 4 Experiment - extractive body cue:** This setup directly tests whether RoboTwin 2.0 enables robust policy generalization without additional real-world data from visually complex environments.
- **p. 7 / 50 Tasks for Data Generation and Benchmarking - extractive body cue:** We further support data collection and evaluation on five distinct robot platforms, enabling comprehensive cross-embodiment benchmarking.
- **p. 9 / 4 Experiment - extractive body cue:** As a result, models pretrained with RoboTwin 2.0 can adapt to new tasks without requiring additional data augmentation or complex scene variations.
- **p. 8 / 4 Experiment - extractive body cue:** Evaluated on the subset of tasks supported by both RoboTwin 1.0 and RoboTwin 2.0.
- **p. 8 / 4 Experiment - extractive body cue:** Method Aloha-AgileX Piper Franka UR5 ARX-X5 Average RoboTwin 1.0 65.1% 2.4% 67.3% 57.6% 68.6% 52.2% RoboTwin 2.0 78.8% 25.1% 67.2% 57.1% 74.2% 60.5% Difference +13.7% ...
- **p. 9 / 4 Experiment - extractive body cue:** 4.4 Evaluation on Sim-to-Real Performance Seen Bg + not Cluttered Unseen Bg + not Cluttered Seen Bg + Cluttered Unseen Bg + Cluttered Figure 10: ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 50 Tasks for Data Generation and Benchmarking (p. 7); 4 Experiment (p. 7); B Benchmarking RoboTwin 2.0 Against Existing Datasets (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | BENCHMARK / DATASET | Results show that our method improves success rates, particularly for robots with constrained planning spaces, achieving an average improvement of 8.3% across all embodiments. | p. 8 (4 Experiment) |
| 4 Experiment | BENCHMARK / DATASET | This also suggests that the low success rate of pretrained VLAs in simulation is not due to a Real-to-Sim gap, since we provide clean ... | p. 9 (4 Experiment) |
| 4 Experiment | BENCHMARK / DATASET | Stack Bowls Two 0.0% 0.0% 30.0% 41.0% 8.0% 55.0% 49.0% 62.0% Pick Dual Bottles 0.0% 0.0% 13.0% 12.0% 12.0% 15.0% 17.0% 7.0% Move Can ... | p. 9 (4 Experiment) |
| 4 Experiment | BENCHMARK / DATASET | We evaluate performance with four metrics: ASR (Average Success Rate), Top5-ASR (success over the top-5 candidates per task), CR-Iter (average refinement iterations before termination), ... | p. 8 (4 Experiment) |
| Figure/Table caption | BENCHMARK / DATASET | Table 8: Task-Specific Performance Comparison between RoboTwin 2.0 and RoboTwin 1.0. R1.0/R2.0: RoboTwin 1.0 / 2.0. Bold numbers indicate the best result for each ... | p. 18 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiment - extractive body cue:** We design experiments to evaluate the effectiveness of RoboTwin 2.0 in three key aspects: (1) automating the generation of high-quality expert code for manipulation tasks; ...
- **p. 10 / 4 Experiment - extractive body cue:** We compare three training settings: (1) 10 real-world demonstrations in clean tabletop environments; (2) the same demonstrations augmented with 1,000 domain-randomized synthetic trajectories generated under ...
- **p. 10 / 4 Experiment - extractive body cue:** This setup directly tests whether RoboTwin 2.0 enables robust policy generalization without additional real-world data from visually complex environments.
- **p. 7 / 50 Tasks for Data Generation and Benchmarking - extractive body cue:** We further support data collection and evaluation on five distinct robot platforms, enabling comprehensive cross-embodiment benchmarking.
- **p. 9 / 4 Experiment - extractive body cue:** As a result, models pretrained with RoboTwin 2.0 can adapt to new tasks without requiring additional data augmentation or complex scene variations.
- **p. 8 / 4 Experiment - extractive body cue:** Evaluated on the subset of tasks supported by both RoboTwin 1.0 and RoboTwin 2.0.
- **p. 8 / 4 Experiment - extractive body cue:** Method Aloha-AgileX Piper Franka UR5 ARX-X5 Average RoboTwin 1.0 65.1% 2.4% 67.3% 57.6% 68.6% 52.2% RoboTwin 2.0 78.8% 25.1% 67.2% 57.1% 74.2% 60.5% Difference +13.7% ...
- **p. 9 / 4 Experiment - extractive body cue:** 4.4 Evaluation on Sim-to-Real Performance Seen Bg + not Cluttered Unseen Bg + not Cluttered Seen Bg + Cluttered Unseen Bg + Cluttered Figure 10: ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Overview of RoboTwin 2.0. RoboTwin 2.0 is a scalable framework for bimanual manipu- lation, integrating an expert data generation pipeline with a 50-task ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: RoboTwin 2.0 Pipeline. Built on RoboTwin-OD and a skill API, the framework uses MLLM-based code generation with simulation feedback to produce expert task ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Expert Code Generation Pipeline. Input Specification. Each task is defined by a task name (e.g., Handover Block) and a natural language description of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of domain randomization and our texture library. Scene Clutter. To enhance robustness to environmental variation, we augment tabletop scenes with task-irrelevant distractors ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Five RoboTwin 2.0 Embodiments.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Different Grasp- ing Behavior. To address embodiment-specific variations, we annotate each object with a rich set of candidate manipulation poses that cover multiple ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7: RoboTwin-OD. A large-scale object dataset for robotic manipulation with 147 categories and 731 objects, annotated with rich interaction labels and diverse language descriptions. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8: 50 RoboTwin 2.0 Bimanual Manipulation Tasks. 4

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We design experiments to evaluate the effectiveness of RoboTwin 2.0 in three key aspects: (1) automating the generation of high-quality expert code for manipulation ... | embodiment, simulator version and control stack | p. 7 (4 Experiment), p. 10 (4 Experiment) |
| Task/environment | We compare three training settings: (1) 10 real-world demonstrations in clean tabletop environments; (2) the same demonstrations augmented with 1,000 domain-randomized synthetic trajectories generated ... | reset, timeout, object/scene variation | p. 10 (4 Experiment), p. 10 (4 Experiment) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 3 (2 Method), p. 2 (1 Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 3 (1 Introduction), p. 5 (2 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate performance with four metrics: ASR (Average Success Rate), Top5-ASR (success over the top-5 candidates per task), CR-Iter (average refinement iterations before termination), ... | definition/direction/unit from same section | p. 8 (4 Experiment) |
| Per-task success rates are provided in Appendix 8. | definition/direction/unit from same section | p. 8 (4 Experiment) |
| Success rates for all tasks can be found in Appendix L. | definition/direction/unit from same section | p. 9 (4 Experiment) |
| This also suggests that the low success rate of pretrained VLAs in simulation is not due to a Real-to-Sim gap, since we provide clean ... | definition/direction/unit from same section | p. 9 (4 Experiment) |
| Table 8: Task-Specific Performance Comparison between RoboTwin 2.0 and RoboTwin 1.0. R1.0/R2.0: RoboTwin 1.0 / 2.0. Bold numbers indicate the best result for each ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Table 9: Per-task success rates of our proposed R2.0 + MM FB algorithm on all RoboTwin 2.0-supported tasks. Task Rate Task Rate Task Rate | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Table 11: Success Rates of Different Embodiments on RoboTwin 2.0 Tasks. RoboTwin1.0 RoboTwin2.0 Task Name Aloha ARX Franka Piper | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| To further improve robustness to camera jitter and calibration errors, we apply random 3D perturbations to simulated camera poses (position and orientation), with the ... | definition/direction/unit from same section | p. 10 (4 Experiment) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Stack Bowls Two 0.0% 0.0% 30.0% 41.0% 8.0% 55.0% 49.0% 62.0% Pick Dual Bottles 0.0% 0.0% 13.0% 12.0% 12.0% 15.0% 17.0% 7.0% Move Can ... | comparison identity and matched condition | p. 9 (4 Experiment) |
| As shown in Table 2, we compare our RoboTwin 2.0 pipeline against the RoboTwin 1.0 baseline, which lacks diverse grasping and candidate augmentation. | comparison identity and matched condition | p. 8 (4 Experiment) |
| 4.2 Evaluating Efficiency with and without Adaptive Grasping Table 2: Overall Performance Comparison between RoboTwin 1.0 and RoboTwin 2.0. | comparison identity and matched condition | p. 8 (4 Experiment) |
| For comparison, we also evaluate the released pretrained weights of RDT and Pi0 without additional fine-tuning. | comparison identity and matched condition | p. 9 (4 Experiment) |
| This setup directly tests whether RoboTwin 2.0 enables robust policy generalization without additional real-world data from visually complex environments. | comparison identity and matched condition | p. 10 (4 Experiment) |
| Table 7: Code Generation Efficiency and Quality Comparison. Evaluation of prompt and generated code characteristics, along with code similarity metrics (AST Structural Similarity, CodeBERT, ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For comparison, we also evaluate the released pretrained weights of RDT and Pi0 without additional fine-tuning. | component/input/data sensitivity | p. 9 (4 Experiment) |
| Stack Bowls Two 0.0% 0.0% 30.0% 41.0% 8.0% 55.0% 49.0% 62.0% Pick Dual Bottles 0.0% 0.0% 13.0% 12.0% 12.0% 15.0% 17.0% 7.0% Move Can ... | component/input/data sensitivity | p. 9 (4 Experiment) |
| 4.2 Evaluating Efficiency with and without Adaptive Grasping Table 2: Overall Performance Comparison between RoboTwin 1.0 and RoboTwin 2.0. | component/input/data sensitivity | p. 8 (4 Experiment) |
| This setup directly tests whether RoboTwin 2.0 enables robust policy generalization without additional real-world data from visually complex environments. | component/input/data sensitivity | p. 10 (4 Experiment) |
| Table 1: Overall performance comparison across RoboTwin variants. Evaluated on the subset of tasks supported by both RoboTwin 1.0 and RoboTwin 2.0. Per- task ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 7: Code Generation Efficiency and Quality Comparison. Evaluation of prompt and generated code characteristics, along with code similarity metrics (AST Structural Similarity, CodeBERT, ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are as follows: (1) We develop an automated expert data generation framework that integrates multimodal large language models with ... | Results show that our method improves success rates, particularly for robots with constrained planning spaces, achieving an average improvement of 8.3% across all embodiments. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiment), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 8 (4 Experiment), p. 18 (Figure/Table caption), p. 10 (4 Experiment) |
| Primary metric/result | This also suggests that the low success rate of pretrained VLAs in simulation is not due to a Real-to-Sim gap, since we provide clean ... | numeric claim only at cited anchor | p. 9 (4 Experiment) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiment - extractive body cue:** Method Aloha-AgileX Piper Franka UR5 ARX-X5 Average RoboTwin 1.0 65.1% 2.4% 67.3% 57.6% 68.6% 52.2% RoboTwin 2.0 78.8% 25.1% 67.2% 57.1% 74.2% 60.5% Difference +13.7% ...
- **p. 9 / 4 Experiment - extractive body cue:** To this end, we first pre-train RDT and Pi0 on 9,600 expert trajectories collected from 32 tasks (300 per task) under two settings: clean (non-randomized) ...
- **p. 5 / 2 Method - extractive body cue:** To enhance robustness to environmental variation, we augment tabletop scenes with task-irrelevant distractors drawn from RoboTwin-OD (731 objects across 147 categories; see Section 3.1).
- **p. 5 / 2 Method - extractive body cue:** To build it, we first collected 1,000 diverse surface descriptions via LLM prompting and web crawling, then used Stable Diffusion v2 to generate 20 samples ...
- **p. 6 / 2 Method - extractive body cue:** A large-scale object dataset for robotic manipulation with 147 categories and 731 objects, annotated with rich interaction labels and diverse language descriptions.
- **p. 7 / 2 Method - extractive body cue:** In addition, RoboTwin-OD incorporates 153 objects from 27 categories in Objaverse [10], and 44 articulated object instances from 9 categories in SAPIEN PartNet-Mobility [48].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our system integrates MLLM-based task generation, embodiment-adaptive behavior synthesis, and comprehensive domain randomization to address key limitations in prior synthetic data generator. | p. 12 (6 Conclusion) |
| body limitation/failure cue | Figure 4: Visualization of domain randomization and our texture library. Scene Clutter. To enhance robustness to environmental variation, we augment tabletop scenes with task-irrelevant ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Overall, three findings emerge: (1) vision-language feedback not only detects failures but also guides precise repairs; (2) architectural improvements in RoboTwin 2.0 accelerate convergence ... | p. 8 (4 Experiment) |
| body limitation/failure cue | RoboTwin 2.0 provides a foundation for unified benchmarks and scalable sim-to-real pipelines, with future work focusing on real-world deployment and multi-object task complexity. | p. 12 (6 Conclusion) |
| body limitation/failure cue | These results demonstrate that our approach provides additional feasible grasp options that effectively mitigate the planning limitations of low-DoF manipulators. | p. 9 (4 Experiment) |
| body limitation/failure cue | Stack Bowls Two 0.0% 0.0% 30.0% 41.0% 8.0% 55.0% 49.0% 62.0% Pick Dual Bottles 0.0% 0.0% 13.0% 12.0% 12.0% 15.0% 17.0% 7.0% Move Can ... | p. 9 (4 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each configuration, the code-generation agent produces multiple candidate programs, which are executed in simulation to account for stochasticity 7 | p. 7 (4 Experiment) |
| 4.1 Evaluation of Automated Expert Code Generation We evaluate our closed-loop expert data generation system on a suite of 10 robotic manipulation tasks, each ... | p. 7 (4 Experiment) |
| 1236.6), reflecting more concise initial code. | p. 8 (4 Experiment) |
| Together, these results validate the effectiveness of our closed-loop, self-improving code generation architecture. | p. 8 (4 Experiment) |
| After each execution batch, the system generates a structured execution log that records the success or failure of each trial and annotates failure cases ... | p. 4 (2 Method) |
| The system adopts a closed-loop architecture with two agents: a code-generation agent and a vision-language model (VLM) observer. | p. 3 (2 Method) |
| The code agent synthesizes task programs from instructions, while the observer monitors execution in simulation, detects failures, and suggests corrections. | p. 3 (2 Method) |
| Code Repair and Iterative Refinement. | p. 4 (2 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / 6 Conclusion - extractive body cue:** Our system integrates MLLM-based task generation, embodiment-adaptive behavior synthesis, and comprehensive domain randomization to address key limitations in prior synthetic data generator.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of domain randomization and our texture library. Scene Clutter. To enhance robustness to environmental variation, we augment tabletop scenes with task-irrelevant distractors ...
- **p. 8 / 4 Experiment - extractive body cue:** Overall, three findings emerge: (1) vision-language feedback not only detects failures but also guides precise repairs; (2) architectural improvements in RoboTwin 2.0 accelerate convergence and ...
- **p. 12 / 6 Conclusion - extractive body cue:** RoboTwin 2.0 provides a foundation for unified benchmarks and scalable sim-to-real pipelines, with future work focusing on real-world deployment and multi-object task complexity.
- **p. 9 / 4 Experiment - extractive body cue:** These results demonstrate that our approach provides additional feasible grasp options that effectively mitigate the planning limitations of low-DoF manipulators.
- **p. 9 / 4 Experiment - extractive body cue:** Stack Bowls Two 0.0% 0.0% 30.0% 41.0% 8.0% 55.0% 49.0% 62.0% Pick Dual Bottles 0.0% 0.0% 13.0% 12.0% 12.0% 15.0% 17.0% 7.0% Move Can Pot ...

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiment), p. 10 (4 Experiment), p. 10 (4 Experiment), p. 7 (50 Tasks for Data Generation and Benchmarking), p. 9 (4 Experiment), p. 8 (4 Experiment), metrics p. 8 (4 Experiment), p. 8 (4 Experiment), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 18 (Figure/Table caption), p. 19 (Figure/Table caption), baselines p. 9 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment), p. 9 (4 Experiment), p. 10 (4 Experiment), p. 17 (Figure/Table caption), results p. 8 (4 Experiment), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 8 (4 Experiment), p. 18 (Figure/Table caption), p. 10 (4 Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
