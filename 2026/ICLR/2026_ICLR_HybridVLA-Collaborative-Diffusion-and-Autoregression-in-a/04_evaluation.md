# Evaluation - HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=H1KDMNOKQn; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245878. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (12.3 Hz), p. 7 (12.3 Hz), p. 9 (12.3 Hz), p. 8 (12.3 Hz), p. 2 (Figure/Table caption), p. 10 (12.3 Hz)): As shown in Table 2, HybridVLA (7B) achieves an average success rate of 78% across 10 distinct tasks, outperforming the previous SOTA autoregressive-based VLA (OpenVLA) and diffusion-based VLA (π0) by ...

## Evaluation Body Digest

- **p. 8 / 12.3 Hz - extractive body cue:** CAE indicates the collaborative action ensemble method, whereas LSP refers to large-scale pretraining on robotic datasets.
- **p. 8 / 12.3 Hz - extractive body cue:** Although Ex6 is initialized with pretrained VLM parameters, it suffers from a significant drop in accuracy, highlighting the essential role of large-scale pretraining on robot ...
- **p. 10 / 12.3 Hz - extractive body cue:** All methods maintain satisfactory performance, demonstrating that large-scale pretraining on robotic datasets enhances their generalization across diverse data distributions.
- **p. 6 / 4 EXPERIMENT - extractive body cue:** To systematically evaluate our method, we select the RLBench (James et al., 2020) benchmark in the CoppeliaSim simulator, which contains 10 different tabletop tasks.
- **p. 10 / 12.3 Hz - extractive body cue:** By effectively inheriting the continuous nature of diffusionbased action generation and leveraging the pretrained knowledge of LLMs, HybridVLA achieves outstanding performance and strong generalization across ...
- **p. 6 / 4 EXPERIMENT - extractive body cue:** 4.1 SIMULATION EXPERIMENT Simulation benchmark.
- **p. 7 / 12.3 Hz - extractive body cue:** tasks are performed using a Franka Panda robot and a front-view camera.
- **p. 7 / 12.3 Hz - extractive body cue:** Following the frame-sampling method used in previous works (Shridhar et al., 2022; Goyal et al., 2023; Jia et al., 2024), we construct the training dataset, ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 EXPERIMENT (p. 6); B ADDITIONAL DATASET DETAILS (p. 19); B.1 LARGE-SCALE PRETRAINING DATASET (p. 19); B.2 SELF-COLLECTED REAL-WORLD DATASET (p. 20); C ADDITIONAL QUANTITATIVE RESULTS (p. 21); C.1 ADDITIONAL SIMULATION EXPERIMENTS (p. 21); C.3 ADDITIONAL GENERALIZATION EXPERIMENTS (p. 23); C.4 ADDITIONAL MOTIVATION EXPERIMENTS (p. 24).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 12.3 Hz | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, HybridVLA (7B) achieves an average success rate of 78% across 10 distinct tasks, outperforming the previous SOTA autoregressive-based VLA ... | p. 7 (12.3 Hz) |
| 12.3 Hz | EMPIRICAL / REAL-ROBOT OR HARDWARE | Remarkably, compared to CogACT and π0, HybridVLA-dif (7B) also achieves performance improvements of 12% and 11%, respectively. | p. 7 (12.3 Hz) |
| 12.3 Hz | EMPIRICAL / REAL-ROBOT OR HARDWARE | For Pick and place and Unplug charger, HybridVLA achieves success rates of 90% and 95%, respectively, demonstrating accurate object position prediction. | p. 9 (12.3 Hz) |
| 12.3 Hz | EMPIRICAL / REAL-ROBOT OR HARDWARE | For collaborative action ensemble, as evidenced by the results of Ex2, Ex4, and Ex5 in Table 3, the performance of HybridVLA (Ex5) is further ... | p. 8 (12.3 Hz) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: (a) Unlike recent diffusion-based VLA methods that attach a separate diffusion head after VLMs, (b) HybridVLA innovatively integrates diffusion and autoregressive action ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 12.3 Hz - extractive body cue:** CAE indicates the collaborative action ensemble method, whereas LSP refers to large-scale pretraining on robotic datasets.
- **p. 8 / 12.3 Hz - extractive body cue:** Although Ex6 is initialized with pretrained VLM parameters, it suffers from a significant drop in accuracy, highlighting the essential role of large-scale pretraining on robot ...
- **p. 10 / 12.3 Hz - extractive body cue:** All methods maintain satisfactory performance, demonstrating that large-scale pretraining on robotic datasets enhances their generalization across diverse data distributions.
- **p. 6 / 4 EXPERIMENT - extractive body cue:** To systematically evaluate our method, we select the RLBench (James et al., 2020) benchmark in the CoppeliaSim simulator, which contains 10 different tabletop tasks.
- **p. 10 / 12.3 Hz - extractive body cue:** By effectively inheriting the continuous nature of diffusionbased action generation and leveraging the pretrained knowledge of LLMs, HybridVLA achieves outstanding performance and strong generalization across ...
- **p. 6 / 4 EXPERIMENT - extractive body cue:** 4.1 SIMULATION EXPERIMENT Simulation benchmark.
- **p. 7 / 12.3 Hz - extractive body cue:** tasks are performed using a Franka Panda robot and a front-view camera.
- **p. 7 / 12.3 Hz - extractive body cue:** Following the frame-sampling method used in previous works (Shridhar et al., 2022; Goyal et al., 2023; Jia et al., 2024), we construct the training dataset, ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) Unlike recent diffusion-based VLA methods that attach a separate diffusion head after VLMs, (b) HybridVLA innovatively integrates diffusion and autoregressive action prediction ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: HybridVLA Framework. All multimodal inputs are encoded into tokens and subsequently organized into our designed token sequence formulation within the LLM's embedding space. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Exploration of token sequence formulations. All models are trained using hybrid objectives. Dif and AR refer to using only autoregressive or diffusion-based generation ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Comparison of HybridVLA and baselines on RLBench. We train all methods in the multi-task setting (Shridhar et al., 2022) and report the success ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Impact of each component. AR and Dif denote that use solely autoregressive and diffusion- based action, respectively. CAE indicates the col- laborative action ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: The impact of different confidence threshold. We report success rates for HybridVLA (7B) and HybridVLA (2.7B) on various tasks with confidence threshold from ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5: Real-world experiments. The manipulation success is determined by human evaluation. Since CogACT lacks support for multi-view images, which are crucial for dual-arm tasks ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 6: Generalization. "Object", "Background", "Height", and "Lighting" denote unseen manipu- lated objects, backgrounds, spatial positions, and lighting conditions, respectively. The image on the left ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | CAE indicates the collaborative action ensemble method, whereas LSP refers to large-scale pretraining on robotic datasets. | embodiment, simulator version and control stack | p. 8 (12.3 Hz), p. 8 (12.3 Hz) |
| Task/environment | Although Ex6 is initialized with pretrained VLM parameters, it suffers from a significant drop in accuracy, highlighting the essential role of large-scale pretraining on ... | reset, timeout, object/scene variation | p. 8 (12.3 Hz), p. 10 (12.3 Hz) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We train all methods in the multi-task setting (Shridhar et al., 2022) and report the success rates (S.R.) and variances (Var.). | definition/direction/unit from same section | p. 7 (4 EXPERIMENT) |
| For evaluation, following previous VLA method (Kim et al., 2024), we test all methods with 20 rollouts per task from the latest epoch checkpoint, ... | definition/direction/unit from same section | p. 7 (12.3 Hz) |
| We report success rates for HybridVLA (7B) and HybridVLA (2.7B) on various tasks with confidence threshold from 0.90 to 0.98. | definition/direction/unit from same section | p. 8 (12.3 Hz) |
| For Pick and place and Unplug charger, HybridVLA achieves success rates of 90% and 95%, respectively, demonstrating accurate object position prediction. | definition/direction/unit from same section | p. 9 (12.3 Hz) |
| Table 11: Task success rates under different ratios of AR and diffusion losses. LAR : LDif 10:1 5:1 2:1 1:1 1:2 1:5 | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Figure 5: The impact of denoising steps, where the x-axis and y-axis represent the denoising steps and manipulation success rate. that a ratio between ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| To provide a clearer overview, in the Table 6 below, we summarize the average score and average accuracy drop percentage across all unseen configurations. | definition/direction/unit from same section | p. 10 (12.3 Hz) |
| The superior performance on Wipe blackboard and Open drawer and place inside further underscores the robustness of our method in long-horizon tasks. | definition/direction/unit from same section | p. 9 (12.3 Hz) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The results show that our method reduces the accuracy drop by approximately 5-16% compared to the baselines under generalization scenarios. | comparison identity and matched condition | p. 10 (12.3 Hz) |
| As shown in Table 2, HybridVLA (7B) achieves an average success rate of 78% across 10 distinct tasks, outperforming the previous SOTA autoregressive-based VLA ... | comparison identity and matched condition | p. 7 (12.3 Hz) |
| For Pour water, HybridVLA outperforms the previous SOTA method by 35%, showcasing its ability to comprehend object relationships and predict precise rotations. | comparison identity and matched condition | p. 9 (12.3 Hz) |
| Remarkably, compared to CogACT and π0, HybridVLA-dif (7B) also achieves performance improvements of 12% and 11%, respectively. | comparison identity and matched condition | p. 7 (12.3 Hz) |
| Our method consistently outperforms previous VLA approaches across five distinct tasks, highlighting HybridVLA's ability to effectively leverage LLM's pretrained knowledge for dual-arm coordination in ... | comparison identity and matched condition | p. 9 (12.3 Hz) |
| Figure 7: The model architectures of variation1. The transformer-based diffusion head is attached to HybridVLA. Figure 7 and 8 shows schematic diagrams of the ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The above ablation studies corroborate our initial motivation that the two action-generation paradigms possess distinct advantages, and HybridVLA effectively integrates them during both training ... | component/input/data sensitivity | p. 8 (12.3 Hz) |
| Figure 3: Respective strengths of diffusion-based and autoregressive action generation paradigms. We evaluate the performance of Our-ar and Our-dif across a variety of scenarios. ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |
| 4.2 ABLATION STUDY The impact of each component. | component/input/data sensitivity | p. 7 (12.3 Hz) |
| The effectiveness of each component is validated in Section 4.2 and Appendix C.2. | component/input/data sensitivity | p. 6 (4 EXPERIMENT) |
| Note that all models are run with bfloat16 precision during inference, without employing action chunking. | component/input/data sensitivity | p. 7 (12.3 Hz) |
| Due to space limitations, Appendix C.2 provides additional ablation studies on: (1) confidence thresholds in the collaborative action ensemble, (2) the influence of the ... | component/input/data sensitivity | p. 8 (12.3 Hz) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and ... | As shown in Table 2, HybridVLA (7B) achieves an average success rate of 78% across 10 distinct tasks, outperforming the previous SOTA autoregressive-based VLA ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (12.3 Hz), p. 7 (12.3 Hz), p. 9 (12.3 Hz), p. 8 (12.3 Hz), p. 2 (Figure/Table caption), p. 10 (12.3 Hz) |
| Primary metric/result | Remarkably, compared to CogACT and π0, HybridVLA-dif (7B) also achieves performance improvements of 12% and 11%, respectively. | numeric claim only at cited anchor | p. 7 (12.3 Hz) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENT - extractive body cue:** Models Close Close Toilet Sweep Close Phone Umbrella Frame Wine at Water Mean Infer. box laptop lid seat down to dustpan fridge on base out ...
- **p. 7 / 12.3 Hz - extractive body cue:** Following the frame-sampling method used in previous works (Shridhar et al., 2022; Goyal et al., 2023; Jia et al., 2024), we construct the training dataset, ...
- **p. 7 / 12.3 Hz - extractive body cue:** Our models are trained for 300 epochs on downstream tasks using mixed-precision.
- **p. 7 / 12.3 Hz - extractive body cue:** For evaluation, following previous VLA method (Kim et al., 2024), we test all methods with 20 rollouts per task from the latest epoch checkpoint, repeating ...
- **p. 9 / 12.3 Hz - extractive body cue:** For single-arm tasks, we use a Franka Research 3 robot with a static front-view and a wrist-view camera.
- **p. 9 / 12.3 Hz - extractive body cue:** We perform 5 tasks: 1) Pick and place, 2) Unplug charger, 3) Open drawer and place object inside, 4) Pour water, 5) Wipe blackboard using ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additional qualitative results and failure case analyses are provided in Appendix D and Appendix E, respectively, and execution videos are available in the supplementary ... | p. 9 (12.3 Hz) |
| body limitation/failure cue | Figure 9: Single-arm Execution Visualization. We visualize key frames of the agent's execution process from the front perspective. E FAILURE CASE ANALYSIS. Through extensive ... | p. 26 (Figure/Table caption) |
| body limitation/failure cue | Due to space limitations, Appendix C.2 provides additional ablation studies on: (1) confidence thresholds in the collaborative action ensemble, (2) the influence of the ... | p. 8 (12.3 Hz) |
| body limitation/failure cue | One limitation of HybridVLA is that its inference speed is constrained by the slower autoregressive generation, similar to prior autoregressive VLA methods (Kim et ... | p. 10 (12.3 Hz) |
| body limitation/failure cue | 5 CONCLUSION AND LIMITATION In this paper, we introduce HybridVLA, a unified Vision-Language-Action (VLA) framework that equips a single LLM with both diffusion-based and ... | p. 10 (12.3 Hz) |
| body limitation/failure cue | Figure 4: Real-World Assets and Experimental Settings. We provide visualizations of the assets used and the settings for single-arm FR3 robot tasks and dual-arm ... | p. 21 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our models are trained for 300 epochs on downstream tasks using mixed-precision. | p. 7 (12.3 Hz) |
| Note that all models are run with bfloat16 precision during inference, without employing action chunking. | p. 7 (12.3 Hz) |
| Due to space limitations, Appendix C.2 provides additional ablation studies on: (1) confidence thresholds in the collaborative action ensemble, (2) the influence of the ... | p. 8 (12.3 Hz) |
| For evaluation, we use the checkpoint from the latest epoch to perform 20 rollouts across diverse tabletop positions. | p. 9 (12.3 Hz) |
| The implementation details remain consistent with our simulation experiments, except for using two-view inputs for single-arm tasks and three-view inputs for dual-arm tasks. | p. 9 (12.3 Hz) |
| 1State Key Laboratory of Multimedia Information Processing, School of Computer Science.
| As shown in the right of Figure 1, HybridVLA is first pretrained on large-scale, diverse, cross-embodiment robotic datasets, including Open XEmbodiment (O'Neill et al., ... | p. 2 (1 INTRODUCTION) |
| Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 ... | p. 2 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 12.3 Hz - extractive body cue:** Additional qualitative results and failure case analyses are provided in Appendix D and Appendix E, respectively, and execution videos are available in the supplementary materials.
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 9: Single-arm Execution Visualization. We visualize key frames of the agent's execution process from the front perspective. E FAILURE CASE ANALYSIS. Through extensive real-world ...
- **p. 8 / 12.3 Hz - extractive body cue:** Due to space limitations, Appendix C.2 provides additional ablation studies on: (1) confidence thresholds in the collaborative action ensemble, (2) the influence of the diffusion-based ...
- **p. 10 / 12.3 Hz - extractive body cue:** One limitation of HybridVLA is that its inference speed is constrained by the slower autoregressive generation, similar to prior autoregressive VLA methods (Kim et al., ...
- **p. 10 / 12.3 Hz - extractive body cue:** 5 CONCLUSION AND LIMITATION In this paper, we introduce HybridVLA, a unified Vision-Language-Action (VLA) framework that equips a single LLM with both diffusion-based and autoregressive ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 4: Real-World Assets and Experimental Settings. We provide visualizations of the assets used and the settings for single-arm FR3 robot tasks and dual-arm AgileX ...

- **Evidence anchors reviewed:** datasets p. 8 (12.3 Hz), p. 8 (12.3 Hz), p. 10 (12.3 Hz), p. 6 (4 EXPERIMENT), p. 10 (12.3 Hz), p. 6 (4 EXPERIMENT), metrics p. 7 (4 EXPERIMENT), p. 7 (12.3 Hz), p. 8 (12.3 Hz), p. 9 (12.3 Hz), p. 23 (Figure/Table caption), p. 23 (Figure/Table caption), baselines p. 10 (12.3 Hz), p. 7 (12.3 Hz), p. 9 (12.3 Hz), p. 7 (12.3 Hz), p. 9 (12.3 Hz), p. 24 (Figure/Table caption), results p. 7 (12.3 Hz), p. 7 (12.3 Hz), p. 9 (12.3 Hz), p. 8 (12.3 Hz), p. 2 (Figure/Table caption), p. 10 (12.3 Hz).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
