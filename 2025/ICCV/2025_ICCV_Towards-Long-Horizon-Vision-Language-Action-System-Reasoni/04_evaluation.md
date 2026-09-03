# Evaluation - Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.3. Ablation Study), p. 7 (5.2.1. Performance on Real World Tasks), p. 8 (5.2.2. Performance of Different Components), p. 7 (5.2.1. Performance on Real World Tasks), p. 6 (5.1. Implementation Details), p. 6 (Figure/Table caption)): As shown in Table 6, the performance of the AE using pure vision declined due to the lack of spatial information, and the RGB-based BE achieves just a 10% success ...

## Evaluation Body Digest

- **p. 8 / 5.3. Ablation Study - extractive body cue:** Compared to DeepSeek-VL2 and InternVL2.5, although they are on par with Qwen2-VL in some benchmark indicators, they lack scalability for real-world tasks in embodied systems, ...
- **p. 3 / 3. The System Dataset - extractive body cue:** CoT Dataset: SandThink-21k Effective robotic task execution requires goal comprehension, subgoal decomposition, and precise action sequencing.
- **p. 3 / 3. The System Dataset - extractive body cue:** To address Challenge 3, we collect a multi-task embodied operation dataset SandGo-1k, using a tracked mobile robot with a single-arm manipulator (as shown in Figure ...
- **p. 6 / 5.2.1. Performance on Real World Tasks - extractive body cue:** We evaluate 24 real-world robotic tasks categorized into four types, each containing six distinct tasks.
- **p. 8 / 5.2.2. Performance of Different Components - extractive body cue:** By combining spatial information with color and texture information from RGB images, the BE and AE achieve better alignment between object semantics and text instructions ...
- **p. 6 / 5.2.1. Performance on Real World Tasks - extractive body cue:** The robot must reason about motion and manipulation tasks in combination, such as grasping a specified object to place in a container (Task 13-15) and ...
- **p. 7 / 5.2.1. Performance on Real World Tasks - extractive body cue:** (%) GPT-4o-latest 33.02 47.00 37.54 50.00 41.59 61.00 29.17 21.00 Gemini-2.0-Flash 29.52 43.00 33.69 49.00 43.53 55.00 24.36 18.00 InternVL2.5-8B 14.71 33.00 17.45 40.00 19.37 ...
- **p. 7 / 5.2.1. Performance on Real World Tasks - extractive body cue:** The robot must generalize over different objects (branches, bottles, and stones), recognize and manipulate objects despite variations in texture, shape, and weight, and adjust to ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 3. The System Dataset (p. 3); 5. Experiments (p. 6); 5.1. Implementation Details (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 6, the performance of the AE using pure vision declined due to the lack of spatial information, and the RGB-based ... | p. 8 (5.3. Ablation Study) |
| 5.2.1. Performance on Real World Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | In multi-skill coordination, MindExplore outperforms single-expert models with a higher success rate due to the MoPE. | p. 7 (5.2.1. Performance on Real World Tasks) |
| 5.2.2. Performance of Different Components | EMPIRICAL / REAL-ROBOT OR HARDWARE | By combining spatial information with color and texture information from RGB images, the BE and AE achieve better alignment between object semantics and text ... | p. 8 (5.2.2. Performance of Different Components) |
| 5.2.1. Performance on Real World Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, in instruction-following, MindExplore's performance improves as instruction granularity increases, whereas OpenVLA and RDT perform better with coarse-grained instructions than ... | p. 7 (5.2.1. Performance on Real World Tasks) |
| 5.1. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate the MindExplore system directly in the same sandpit scenario, using success rates as the metric, which is the ratio of successful trials ... | p. 6 (5.1. Implementation Details) |

## Dataset / Benchmark Role

- **p. 8 / 5.3. Ablation Study - extractive body cue:** Compared to DeepSeek-VL2 and InternVL2.5, although they are on par with Qwen2-VL in some benchmark indicators, they lack scalability for real-world tasks in embodied systems, ...
- **p. 3 / 3. The System Dataset - extractive body cue:** CoT Dataset: SandThink-21k Effective robotic task execution requires goal comprehension, subgoal decomposition, and precise action sequencing.
- **p. 3 / 3. The System Dataset - extractive body cue:** To address Challenge 3, we collect a multi-task embodied operation dataset SandGo-1k, using a tracked mobile robot with a single-arm manipulator (as shown in Figure ...
- **p. 6 / 5.2.1. Performance on Real World Tasks - extractive body cue:** We evaluate 24 real-world robotic tasks categorized into four types, each containing six distinct tasks.
- **p. 8 / 5.2.2. Performance of Different Components - extractive body cue:** By combining spatial information with color and texture information from RGB images, the BE and AE achieve better alignment between object semantics and text instructions ...
- **p. 6 / 5.2.1. Performance on Real World Tasks - extractive body cue:** The robot must reason about motion and manipulation tasks in combination, such as grasping a specified object to place in a container (Task 13-15) and ...
- **p. 7 / 5.2.1. Performance on Real World Tasks - extractive body cue:** (%) GPT-4o-latest 33.02 47.00 37.54 50.00 41.59 61.00 29.17 21.00 Gemini-2.0-Flash 29.52 43.00 33.69 49.00 43.53 55.00 24.36 18.00 InternVL2.5-8B 14.71 33.00 17.45 40.00 19.37 ...
- **p. 7 / 5.2.1. Performance on Real World Tasks - extractive body cue:** The robot must generalize over different objects (branches, bottles, and stones), recognize and manipulate objects despite variations in texture, shape, and weight, and adjust to ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview of MindExplore System: A hierarchical embodied intelligence system including reasoning, acting, and memory, offering state-of-the-art generalizability in highly dynamic scenes. Unlike conventional ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Left: AgileX Robotic arm degrees of freedom and envi- ronmental layout (rugged terrain, obstacles, pits, dunes). Middle: Base movement states. Right: Collected data ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. MindExplore System Overview. MindExplore comprises a reasoning layer for task decomposition and an acting layer for execution. The Reasoning Layer, built on Qwen2-VL, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. The details of Memory Mechanism To enhance the coordination between the Reasoning Layer and the Acting Layer and achieve global control over both ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. The success rates of different VLA models across 24 tasks in four long-horizon tasks. Coarse-Grained Long-Horizon Tasks Intensive Instruction-Following Tasks
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. During long-horizon tasks, the reasoning layer decomposes the instruction into a structured sequence of executable steps. The acting layer then orchestrates the hierarchical ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Comparison results with the most powerful closed-source and open-source MLLMs on three tasks.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Success Rates of the Acting Layer across 5 meta-actions: Moving to a Target Location (MTL), Crossing Obstacles (CO), Grasping a Specified Object (GSO), ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Compared to DeepSeek-VL2 and InternVL2.5, although they are on par with Qwen2-VL in some benchmark indicators, they lack scalability for real-world tasks in embodied ... | embodiment, simulator version and control stack | p. 8 (5.3. Ablation Study), p. 3 (3. The System Dataset) |
| Task/environment | CoT Dataset: SandThink-21k Effective robotic task execution requires goal comprehension, subgoal decomposition, and precise action sequencing. | reset, timeout, object/scene variation | p. 3 (3. The System Dataset), p. 3 (3. The System Dataset) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 5 (4.2.2. Mixture of Policy Experts) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (4.2.2. Mixture of Policy Experts), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, without timely state feedback and error correction from acting layer, the system is highly susceptible to error accumulation, resulting in a decrease in ... | definition/direction/unit from same section | p. 8 (5.3. Ablation Study) |
| As shown in Table 6, the performance of the AE using pure vision declined due to the lack of spatial information, and the RGB-based ... | definition/direction/unit from same section | p. 8 (5.3. Ablation Study) |
| We evaluate the MindExplore system directly in the same sandpit scenario, using success rates as the metric, which is the ratio of successful trials ... | definition/direction/unit from same section | p. 6 (5.1. Implementation Details) |
| Avg. - Average Success Rate, BE - Base Expert, AE - Arm Expert. | definition/direction/unit from same section | p. 7 (5.2.1. Performance on Real World Tasks) |
| In multi-skill coordination, MindExplore outperforms single-expert models with a higher success rate due to the MoPE. | definition/direction/unit from same section | p. 7 (5.2.1. Performance on Real World Tasks) |
| Table 1. The success rates of different VLA models across 24 tasks in four long-horizon tasks. Coarse-Grained Long-Horizon Tasks Intensive Instruction-Following Tasks | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Based on SandGo-1k, we generate a reasoningacting embodied instruction dataset SandThink-21k. | definition/direction/unit from same section | p. 3 (3. The System Dataset) |
| Additionally, we incorporate 5,700 public complex surface images to leverage their similarity to sand terrain. | definition/direction/unit from same section | p. 3 (3. The System Dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In terms of generalization, compared to end-to-end MLLM and VLAs without world knowledge, MindExplore demonstrates strong generalization capabilities in unseen scenarios. | comparison identity and matched condition | p. 7 (5.2.1. Performance on Real World Tasks) |
| In multi-skill coordination, MindExplore outperforms single-expert models with a higher success rate due to the MoPE. | comparison identity and matched condition | p. 7 (5.2.1. Performance on Real World Tasks) |
| Nonetheless, it still outperforms other VLAs, demonstrating that the MoPE structure can ensure accurate completion of base tasks. | comparison identity and matched condition | p. 8 (5.3. Ablation Study) |
| Compared to DeepSeek-VL2 and InternVL2.5, although they are on par with Qwen2-VL in some benchmark indicators, they lack scalability for real-world tasks in embodied ... | comparison identity and matched condition | p. 8 (5.3. Ablation Study) |
| Figure 1. Overview of MindExplore System: A hierarchical embodied intelligence system including reasoning, acting, and memory, offering state-of-the-art generalizability in highly dynamic scenes. Unlike ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| The tests are conducted with varying scene configurations and ensures that all comparison models are tested under the same conditions. | comparison identity and matched condition | p. 6 (5.1. Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To prove the effectiveness of the Reasoning Layer training method, we performed detailed ablation experiments on three tasks, which involved adding our training methods ... | component/input/data sensitivity | p. 8 (5.3. Ablation Study) |
| We conduct an ablation study on the core components of the MindExplore system. | component/input/data sensitivity | p. 8 (5.3. Ablation Study) |
| In terms of generalization, compared to end-to-end MLLM and VLAs without world knowledge, MindExplore demonstrates strong generalization capabilities in unseen scenarios. | component/input/data sensitivity | p. 7 (5.2.1. Performance on Real World Tasks) |
| We also assess the performance of the two key components, reasoning and acting layer. | component/input/data sensitivity | p. 7 (5.2.2. Performance of Different Components) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our key contributions are summarized as follows: • We propose MindExplore, a novel expert-level hierarchical embodied system to adapt long-horizon tasks in unstructured and ... | As shown in Table 6, the performance of the AE using pure vision declined due to the lack of spatial information, and the RGB-based ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.3. Ablation Study), p. 7 (5.2.1. Performance on Real World Tasks), p. 8 (5.2.2. Performance of Different Components), p. 7 (5.2.1. Performance on Real World Tasks), p. 6 (5.1. Implementation Details), p. 6 (Figure/Table caption) |
| Primary metric/result | In multi-skill coordination, MindExplore outperforms single-expert models with a higher success rate due to the MoPE. | numeric claim only at cited anchor | p. 7 (5.2.1. Performance on Real World Tasks) |

- Numeric sentences retained from the body:
- **p. 3 / 3. The System Dataset - extractive body cue:** Therefore, to investigate the capabilities of mobile manipulation systems in highly dynamic and complex environments, we select sand as the primary experimental setting, including potholes, ...
- **p. 6 / 5.2.1. Performance on Real World Tasks - extractive body cue:** All these evaluated tasks can be divided into four categories according to their ability to complete long-horizon tasks, and we conducted 615 trials on real ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The high dynamic fluidity of sand demands adaptive adjustments, while its visual noise complicates perception and calibration. | p. 3 (3. The System Dataset) |
| body limitation/failure cue | Enhancing generalization in unstructured environments remains a key challenge, and our experiments show that a system robust in sandy conditions can more easily generalize ... | p. 3 (3. The System Dataset) |
| body limitation/failure cue | Similarly, the point-cloud-based BE also shows lower success rates, as point cloud data failed to align effectively with the semantic content of instructions. | p. 8 (5.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We evaluate the MindExplore system directly in the same sandpit scenario, using success rates as the metric, which is the ratio of successful trials ... | p. 6 (5.1. Implementation Details) |
| All these evaluated tasks can be divided into four categories according to their ability to complete long-horizon tasks, and we conducted 615 trials on ... | p. 6 (5.2.1. Performance on Real World Tasks) |
| During long-horizon tasks, the reasoning layer decomposes the instruction into a structured sequence of executable steps. | p. 7 (5.2.1. Performance on Real World Tasks) |
| Method Input Modality Depth Type MTL GSO AE RGB - - 23/50 AE Depth+RGB PC - 40/50 BE RGB - 5/50 - BE LiDAR+Depth ... | p. 8 (5.2.2. Performance of Different Components) |
| We employ the robot manipulation visual encoder R3M, proposed in [25], to encode the RGB images. | p. 5 (4.2.1. Multimodal Diffusion Policy) |
| Additionally, we propose a fusion adapters for both the sensor data and text, consisting of two linear layers, to map encoder outputs into an ... | p. 5 (4.2.1. Multimodal Diffusion Policy) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / 3. The System Dataset - extractive body cue:** The high dynamic fluidity of sand demands adaptive adjustments, while its visual noise complicates perception and calibration.
- **p. 3 / 3. The System Dataset - extractive body cue:** Enhancing generalization in unstructured environments remains a key challenge, and our experiments show that a system robust in sandy conditions can more easily generalize to ...
- **p. 8 / 5.3. Ablation Study - extractive body cue:** Similarly, the point-cloud-based BE also shows lower success rates, as point cloud data failed to align effectively with the semantic content of instructions.

- **Evidence anchors reviewed:** datasets p. 8 (5.3. Ablation Study), p. 3 (3. The System Dataset), p. 3 (3. The System Dataset), p. 6 (5.2.1. Performance on Real World Tasks), p. 8 (5.2.2. Performance of Different Components), p. 6 (5.2.1. Performance on Real World Tasks), metrics p. 8 (5.3. Ablation Study), p. 8 (5.3. Ablation Study), p. 6 (5.1. Implementation Details), p. 7 (5.2.1. Performance on Real World Tasks), p. 7 (5.2.1. Performance on Real World Tasks), p. 6 (Figure/Table caption), baselines p. 7 (5.2.1. Performance on Real World Tasks), p. 7 (5.2.1. Performance on Real World Tasks), p. 8 (5.3. Ablation Study), p. 8 (5.3. Ablation Study), p. 1 (Figure/Table caption), p. 6 (5.1. Implementation Details), results p. 8 (5.3. Ablation Study), p. 7 (5.2.1. Performance on Real World Tasks), p. 8 (5.2.2. Performance of Different Components), p. 7 (5.2.1. Performance on Real World Tasks), p. 6 (5.1. Implementation Details), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
