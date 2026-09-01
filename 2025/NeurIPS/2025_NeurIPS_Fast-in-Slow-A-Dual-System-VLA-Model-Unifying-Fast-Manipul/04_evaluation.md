# Evaluation - Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=4asFznbzJg; PDF retrieval source: https://openreview.net/pdf/a69b5a0fb05a1e5009d25d054e59a97fcc5a4d0d.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 8 (4 Experiments), p. 29 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments)): Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA consistently outperforms the baseline π0 across eight real-world ...

## Evaluation Body Digest

- **p. 9 / 4 Experiments - extractive PDF cue:** Models Agilex Dual-Arm Robot Task AlphaBot Dual-Arm Robot Task Pick Lift ball Place bottles Wipe Mean Pick bowl and Handover Pour water Fold towel Mean ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We evaluate FiS-VLA against π0 [23], using the same training setup as in simulation, with the exception of three-view RGB inputs for real-world dual-arm tasks.
- **p. 7 / 4 Experiments - extractive PDF cue:** In order to fully evaluate our method, we tested on 10 various manipulation tasks in the RLBench [33] benchmark based on the CoppeliaSim simulator, including ...
- **p. 8 / 4 Experiments - extractive PDF cue:** On the Agilex Robot, we conduct the following four tasks: 1) Pick objects and place in basket, 2) Lift ball and place in basket, 3) ...
- **p. 9 / 4 Experiments - extractive PDF cue:** To simulate distracting environments, we introduce visually cluttered scenes containing irrelevant objects such as mugs, hamburgers, and bottles.
- **p. 7 / 4 Experiments - extractive PDF cue:** 4.1 Simulation Experiment Simulation benchmark.
- **p. 7 / 4 Experiments - extractive PDF cue:** Following [22, 5], we evaluate all methods using 20 rollouts from the latest epoch checkpoint, repeating the evaluation three times for each task and reporting ...
- **p. 29 / Figure/Table caption - extractive PDF cue:** Figure 7: Ablation studies on action chunk size and input variants of FiS-VLA. (Left) Impact of different action chunk sizes on success rate and inference ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 7); A Additional Dataset Details (p. 26); A.1 Large-scale pretraining dataset (p. 26); A.2 Simulation dataset (p. 26); A.3 Self-collected real-world dataset (p. 27); B Additional Quantitative Results (p. 29); B.5 The detailed results for each experimental setting (p. 30).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA consistently outperforms ... | p. 9 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | FiS-VLA achieves a 73% average success rate with plan-based co-training, outperforming the 69% obtained using discrete actions. | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Ablation studies on action chunk size and input variants of FiS-VLA. (Left) Impact of different action chunk sizes on success rate and ... | p. 29 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: Ablation study. We investigate the impact of (1) the parameters of System 1's shared blocks within System 2, (2) different modality inputs ... | p. 8 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, FiS-VLA achieves an average success rate of 69% across 10 diverse tasks, surpassing the previous SOTA methods CogACT and ... | p. 7 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiments - extractive PDF cue:** Models Agilex Dual-Arm Robot Task AlphaBot Dual-Arm Robot Task Pick Lift ball Place bottles Wipe Mean Pick bowl and Handover Pour water Fold towel Mean ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We evaluate FiS-VLA against π0 [23], using the same training setup as in simulation, with the exception of three-view RGB inputs for real-world dual-arm tasks.
- **p. 7 / 4 Experiments - extractive PDF cue:** In order to fully evaluate our method, we tested on 10 various manipulation tasks in the RLBench [33] benchmark based on the CoppeliaSim simulator, including ...
- **p. 8 / 4 Experiments - extractive PDF cue:** On the Agilex Robot, we conduct the following four tasks: 1) Pick objects and place in basket, 2) Lift ball and place in basket, 3) ...
- **p. 9 / 4 Experiments - extractive PDF cue:** To simulate distracting environments, we introduce visually cluttered scenes containing irrelevant objects such as mugs, hamburgers, and bottles.
- **p. 7 / 4 Experiments - extractive PDF cue:** 4.1 Simulation Experiment Simulation benchmark.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Overview of FiS-VLA. (a) Unlike previous dual-system VLA methods [1, 2] that attach a separate policy head as System 1, FiS-VLA (b) repurposes ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Framework of FiS-VLA. FiS-VLA leverages an intact VLM for System 2 reasoning while repurposing the final transformer blocks of the LLM for System ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of FiS-VLA and baselines on RLBench. All methods are trained in the multi-task setting [73], and we report success rates (S.R.) based ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3: Ablation study. We investigate the impact of (1) the parameters of System 1's shared blocks within System 2, (2) different modality inputs to ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison of FiS-VLA and π0 in real-world scenarios. We train all methods in a single-task setting [26] and report the success rates. Success ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA consistently outperforms the ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 3: Generalization experiments. "Object", "Background", and "Lighting" refer to unseen manipulated objects, complex backgrounds, and illumination disruption, respectively. Task Place Bottles at Rack Pick ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 5: Visualization of generalization setting with key differences highlighted using red box. importance of the heterogeneous modality input design in FiS-VLA's dual systems, which ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Models Agilex Dual-Arm Robot Task AlphaBot Dual-Arm Robot Task Pick Lift ball Place bottles Wipe Mean Pick bowl and Handover Pour water Fold towel ... | embodiment, simulator version and control stack | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | We evaluate FiS-VLA against π0 [23], using the same training setup as in simulation, with the exception of three-view RGB inputs for real-world dual-arm ... | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (Abstract), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Following [22, 5], we evaluate all methods using 20 rollouts from the latest epoch checkpoint, repeating the evaluation three times for each task and ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Figure 7: Ablation studies on action chunk size and input variants of FiS-VLA. (Left) Impact of different action chunk sizes on success rate and ... | definition/direction/unit from same section | p. 29 (Figure/Table caption) |
| As shown in Table 1, FiS-VLA achieves an average success rate of 69% across 10 diverse tasks, surpassing the previous SOTA methods CogACT and ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| FiS-VLA achieves a 73% average success rate with plan-based co-training, outperforming the 69% obtained using discrete actions. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| We investigate the impact of (1) the parameters of System 1's shared blocks within System 2, (2) different modality inputs to System 1, and ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| We train all methods in a single-task setting [26] and report the success rates. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| On the Agilex Robot, FiS-VLA achieves a mean success rate of 68%, compared to 59% for π0. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 12: Failure case visualization. We visualize the failure cases observed in four real-world experiments, with key error frames during execution highlighted using red ... | definition/direction/unit from same section | p. 35 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA consistently outperforms ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| We compare FiS-VLA against four state-of-the-art (SOTA) VLA models, including ManipLLM [48], OpenVLA [7], π0[23], and CogACT[22], where the latter two are dual-system methods ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| For baselines, we load the official pretrained parameters provided by each method and adhere to their respective fine-tuning settings. | comparison identity and matched condition | p. 7 (4 Experiments) |
| FiS-VLA achieves a 73% average success rate with plan-based co-training, outperforming the 69% obtained using discrete actions. | comparison identity and matched condition | p. 8 (4 Experiments) |
| FiS-VLA demonstrates a smaller performance drop compared to π0 across both platforms. | comparison identity and matched condition | p. 9 (4 Experiments) |
| More ablation experiments can be found in Appendix B. | comparison identity and matched condition | p. 8 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 7: Ablation studies on action chunk size and input variants of FiS-VLA. (Left) Impact of different action chunk sizes on success rate and ... | component/input/data sensitivity | p. 29 (Figure/Table caption) |
| 4.2 Ablation Study To analyze the impact of each component on overall performance within the FiS-VLA, we conduct ablation experiments on 10 RLBench tasks ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| The effectiveness of each component is evaluated in Section 4.2 and Appendix B. | component/input/data sensitivity | p. 7 (4 Experiments) |
| More ablation experiments can be found in Appendix B. | component/input/data sensitivity | p. 8 (4 Experiments) |
| If Lslow is removed during training, manipulation performance drops from 69% to 62%. | component/input/data sensitivity | p. 8 (4 Experiments) |
| These results demonstrate that under the proposed FiS-VLA dual-system paradigm, embedding the System 1 execution module within the VLM-based System 2 allows it to ... | component/input/data sensitivity | p. 9 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a ... | Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA consistently outperforms ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 8 (4 Experiments), p. 29 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Primary metric/result | FiS-VLA achieves a 73% average success rate with plan-based co-training, outperforming the 69% obtained using discrete actions. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive PDF cue:** Building upon the frame-sampling technique employed in previous studies [73, 5, 28], we construct a training dataset where each task contains 100 trajectories.
- **p. 7 / 4 Experiments - extractive PDF cue:** For FiS-VLA's input, the single-view RGB image is resized to 224×224, the point cloud is downsampled to 1024 points, the text instruction is derived from ...
- **p. 7 / 4 Experiments - extractive PDF cue:** FiS-VLA model is trained for 300 epochs using the AdamW optimizer [74] on 8 NVIDIA A800 GPUs, with mixed-precision training employed.
- **p. 7 / 4 Experiments - extractive PDF cue:** Following [22, 5], we evaluate all methods using 20 rollouts from the latest epoch checkpoint, repeating the evaluation three times for each task and reporting ...
- **p. 7 / 4 Experiments - extractive PDF cue:** In particular, FiS-VLA achieves superior performance on 8 out of 10 tasks, highlighting the robustness of its action generation capabilities.
- **p. 7 / 4 Experiments - extractive PDF cue:** In terms of control frequency, FiS-VLA operates at 21.9 Hz, over 2× faster than CogACT (9.8 Hz) and more than 1.6× faster than π0 (13.8 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additional visualizations and failure cases are provided in Appendix C and D, respectively. | p. 9 (4 Experiments) |
| body limitation/failure cue | Figure 5: Visualization of generalization setting with key differences highlighted using red box. importance of the heterogeneous modality input design in FiS-VLA's dual systems, ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Figure 11: AlphaBot task execution visualization. We visualize key frames of the agent's execution process from a static exterior view. D Failure Case Analysis. ... | p. 34 (Figure/Table caption) |
| body limitation/failure cue | Figure 12: Failure case visualization. We visualize the failure cases observed in four real-world experiments, with key error frames during execution highlighted using red ... | p. 35 (Figure/Table caption) |
| body limitation/failure cue | We hypothesize that enabling dynamic adaptation of these factors based on task demands and environmental complexity could lead to a more robust and generalizable ... | p. 10 (A B) |
| body limitation/failure cue | In particular, FiS-VLA achieves superior performance on 8 out of 10 tasks, highlighting the robustness of its action generation capabilities. | p. 7 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature ... | p. 2 (1 Introduction) |
| FiS-VLA model is trained for 300 epochs using the AdamW optimizer [74] on 8 NVIDIA A800 GPUs, with mixed-precision training employed. | p. 7 (4 Experiments) |
| Following [22, 5], we evaluate all methods using 20 rollouts from the latest epoch checkpoint, repeating the evaluation three times for each task and ... | p. 7 (4 Experiments) |
| Additional implementation details can be found in the Appendix A. | p. 8 (4 Experiments) |
| Evaluation is conducted using the final checkpoint over 20 rollouts across varied tabletop positions. | p. 8 (4 Experiments) |
| Notably, since 3D geometric information is critical for precise manipulation [26, 27], we utilize a fast 3D embedding strategy that tokenizes point clouds [28] ... | p. 2 (1 Introduction) |
| With a 1:4 operating frequency ratio between System 2 and System 1, FiS-VLA achieves a 117.7 Hz control frequency on an NVIDIA 4090 GPU ... | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive PDF cue:** Additional visualizations and failure cases are provided in Appendix C and D, respectively.
- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 5: Visualization of generalization setting with key differences highlighted using red box. importance of the heterogeneous modality input design in FiS-VLA's dual systems, which ...
- **p. 34 / Figure/Table caption - extractive PDF cue:** Figure 11: AlphaBot task execution visualization. We visualize key frames of the agent's execution process from a static exterior view. D Failure Case Analysis. Through ...
- **p. 35 / Figure/Table caption - extractive PDF cue:** Figure 12: Failure case visualization. We visualize the failure cases observed in four real-world experiments, with key error frames during execution highlighted using red bounding ...
- **p. 10 / A B - extractive PDF cue:** We hypothesize that enabling dynamic adaptation of these factors based on task demands and environmental complexity could lead to a more robust and generalizable model, ...
- **p. 7 / 4 Experiments - extractive PDF cue:** In particular, FiS-VLA achieves superior performance on 8 out of 10 tasks, highlighting the robustness of its action generation capabilities.

- **PDF anchors reviewed:** datasets p. 9 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), metrics p. 7 (4 Experiments), p. 29 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), baselines p. 9 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), results p. 9 (Figure/Table caption), p. 8 (4 Experiments), p. 29 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
