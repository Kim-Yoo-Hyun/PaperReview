# Evaluation - CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluations Results), p. 8 (4.3. Ablation Study), p. 6 (4.2. Evaluations Results), p. 7 (4.3. Ablation Study)): Table 1. LIBERO benchmark experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each. ...

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We conduct evaluations across three complementary settings: the LIBERO benchmark [37] for evaluation in simulation environments, the Bridge-V2 platform [60] with its dataset of 45k ...
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate the effectiveness of our approach and our system through a set of experiments spanning both simulation benchmarks and real-world robot manipulation tasks.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Pretraining Our training pipeline has two stages, pretraining VILA-U on the OpenX dataset augmented with actionless video data (Section 3.3), and task-specific post-training on robot ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For each task, the dataset contains between 10 and 150 demonstrations.
- **p. 8 / 4.4. Better Visual Reasoning Helps - extractive body cue:** To investigate how visual reasoning capabilities transfer to robot performance, we conduct an ablation study on the Franka-Tabletop setup using novel, long-horizon tasks that combine ...
- **p. 6 / 4.2. Evaluations Results - extractive body cue:** Models pretrained on the OpenX dataset - Octo, OpenVLA, and CoT-VLA - demonstrate better adaptation and performance on multi-instruction tasks where language grounding is critical.
- **p. 8 / 4.4. Better Visual Reasoning Helps - extractive body cue:** We build our system upon VILA-U, demonstrating strong performance across diverse robotic manipulation tasks.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** As shown in Figure 6, both benchmark suites demonstrate that action sequence prediction consistently outperforms single-action prediction.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 10. For complete dataset specifications and training hyper (p. 4); 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Evaluations Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. LIBERO benchmark experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved ... | p. 8 (Figure/Table caption) |
| 4.2. Evaluations Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, CoT-VLA achieves the highest average performance compared to baseline approaches, showing improvements in both single and multi-instruction scenarios. | p. 6 (4.2. Evaluations Results) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our results show that CoT-VLA with our pretraining stage achieves a 46.7% relative improvement, from 53.7% to 78.8%, compared to directly fine-tuning the base ... | p. 8 (4.3. Ablation Study) |
| 4.2. Evaluations Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | SUSIE [2] generates visually higher-quality goal images through its diffusion prior (see Section 5 for a detailed discussion on our limitations) but achieves lower ... | p. 6 (4.2. Evaluations Results) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We conduct evaluations across three complementary settings: the LIBERO benchmark [37] for evaluation in simulation environments, the Bridge-V2 platform [60] with its dataset of 45k ...
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate the effectiveness of our approach and our system through a set of experiments spanning both simulation benchmarks and real-world robot manipulation tasks.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Pretraining Our training pipeline has two stages, pretraining VILA-U on the OpenX dataset augmented with actionless video data (Section 3.3), and task-specific post-training on robot ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For each task, the dataset contains between 10 and 150 demonstrations.
- **p. 8 / 4.4. Better Visual Reasoning Helps - extractive body cue:** To investigate how visual reasoning capabilities transfer to robot performance, we conduct an ablation study on the Franka-Tabletop setup using novel, long-horizon tasks that combine ...
- **p. 6 / 4.2. Evaluations Results - extractive body cue:** Models pretrained on the OpenX dataset - Octo, OpenVLA, and CoT-VLA - demonstrate better adaptation and performance on multi-instruction tasks where language grounding is critical.
- **p. 8 / 4.4. Better Visual Reasoning Helps - extractive body cue:** We build our system upon VILA-U, demonstrating strong performance across diverse robotic manipulation tasks.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** As shown in Figure 6, both benchmark suites demonstrate that action sequence prediction consistently outperforms single-action prediction.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison between vanilla VLA and CoT-VLA frameworks. Prior VLA models (top) directly predict robot ac- tions from task inputs without explicit reasoning steps ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of CoT-VLA framework. We build our model on VILA-U [67], a generative multimodal model pretrained on interleaved text-image data. The base model ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Hybrid attention mechanism in CoT-VLA. We use causal attention for image or text generation and full attention for action generation. [x], [θ] and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. LIBERO benchmark experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Franka-Tabletop comparisons. Evaluation across six distinct manipulation tasks, with separate models trained per task. Left: Representative initial states for each task setup. Right: ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Task execution examples for LIBERO, Bridge-V2, and Franka-Tabletop using CoT-VLA. For each task: Left: text instruction (l) and initial state (sobs 0 ). ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Bridge-V2 Comparison. Success rates across four gener- alization categories, with 10 trials per category and partial credit scoring following [29]. Visual: "put eggplant ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Ablation studies of CoT-VLA components. a) Results on LIBERO-Spatial and LIBERO-Goal benchmarks demonstrate the effectiveness of three components: action chunking, hybrid attention, and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct evaluations across three complementary settings: the LIBERO benchmark [37] for evaluation in simulation environments, the Bridge-V2 platform [60] with its dataset of ... | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments) |
| Task/environment | We evaluate the effectiveness of our approach and our system through a set of experiments spanning both simulation benchmarks and real-world robot manipulation tasks. | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 7 (4.3. Ablation Study) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (10. For complete dataset specifications and training hyper), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Success rates are reported with means and standard error. | definition/direction/unit from same section | p. 6 (4.2. Evaluations Results) |
| Compared to OpenVLA [29], CoT-VLA shows slightly lower success rates in visual and language generalization tasks due to grasping failures from action chunking (see ... | definition/direction/unit from same section | p. 6 (4.2. Evaluations Results) |
| Table 1. LIBERO benchmark experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Success rates across four generalization categories, with 10 trials per category and partial credit scoring following [29]. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| As shown in Table 3, using groundtruth goal images improves the absolute success rate by 40% for both tasks. | definition/direction/unit from same section | p. 8 (4.4. Better Visual Reasoning Helps) |
| Success rates comparing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. | definition/direction/unit from same section | p. 8 (4.4. Better Visual Reasoning Helps) |
| While the dataset was incorporated into the pretraining phase alongside OpenX, we performed additional task-specific fine-tuning exclusively on Bridge-V2 until achieving a training action ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| Right: final state (sobs T ) upon task completion. | definition/direction/unit from same section | p. 7 (4.2. Evaluations Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our experiments aim to addresses following questions: • How does our system perform compared to state-of-the-art baselines across multiple benchmarks and embodiments? | comparison identity and matched condition | p. 5 (4. Experiments) |
| Overall, CoT-VLA achieves the highest average performance compared to baseline approaches, showing improvements in both single and multi-instruction scenarios. | comparison identity and matched condition | p. 6 (4.2. Evaluations Results) |
| Results demonstrate that CoT-VLA effectively adapts to tasks in the LIBERO simulation environment, achieving best or competitive performance compared to baseline approaches. | comparison identity and matched condition | p. 6 (4.2. Evaluations Results) |
| Second, our autoregressive image generation produces lower visual quality compared to state-of-the-art diffusion-based models. | comparison identity and matched condition | p. 8 (4.4. Better Visual Reasoning Helps) |
| CoT-VLA achieves the best or competitive performance across all LIBERO benchmarks suites compared to baseline approaches. | comparison identity and matched condition | p. 5 (10. For complete dataset specifications and training hyper) |
| We evaluate four model variants: VLA - a baseline implementation following the standard VLA framework [29], with the same VILA-U backbone but without chain-of-thought ... | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation studies of CoT-VLA components. a) Results on LIBERO-Spatial and LIBERO-Goal benchmarks demonstrate the effectiveness of three components: action chunking, hybrid attention, and visual ... | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| We evaluate four model variants: VLA - a baseline implementation following the standard VLA framework [29], with the same VILA-U backbone but without chain-of-thought ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| OpenVLA [29] is an open-source VLA model that fine-tunes pretrained vision-language models on the OpenX dataset; and Octo [59] is a generalist model pretrained ... | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| To assess the importance of our pretraining stage, we conduct ablation studies on the Franka-Tabletop setup. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| To investigate how visual reasoning capabilities transfer to robot performance, we conduct an ablation study on the Franka-Tabletop setup using novel, long-horizon tasks that ... | component/input/data sensitivity | p. 8 (4.4. Better Visual Reasoning Helps) |
| While the dataset was incorporated into the pretraining phase alongside OpenX, we performed additional task-specific fine-tuning exclusively on Bridge-V2 until achieving a training action ... | component/input/data sensitivity | p. 5 (4.1. Experimental Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our key contributions include: • We introduce a method of visual chain-of-thought reasoning through subgoal image generation as an intermediate reasoning step for robotic ... | Table 1. LIBERO benchmark experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluations Results), p. 8 (4.3. Ablation Study), p. 6 (4.2. Evaluations Results), p. 7 (4.3. Ablation Study) |
| Primary metric/result | Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive body cue:** Average (↑) Spatial (↑) Object (↑) Goal (↑) Long (↑) Diffusion Policy 72.4 ± 0.7% 78.3 ± 1.1% 92.5 ± 0.7% 68.3 ± 1.2% 50.5 ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive body cue:** For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We conduct evaluations across three complementary settings: the LIBERO benchmark [37] for evaluation in simulation environments, the Bridge-V2 platform [60] with its dataset of 45k ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We follow the same preprocessed pipeline as in [29]: (1) removing pause intervals from trajectories, (2) standardizing image resolution to 256×256 pixels, and (3) applying ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** CoT-VLA achieves best average performance and demonstrates strong capabilities in both single-instruction and multi-instruction scenarios. perform evaluations across 6 tasks: 3 narrow domain singleinstruction tasks ...
- **p. 6 / 4.2. Evaluations Results - extractive body cue:** LIBERO We present quantitative results in Table 1, where each method is evaluated over 500 trials per task suite, with 3 random seeds.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Conclusion, Limitations and Future Work In this work, we introduce CoT-VLA, bridging visionlanguage-action models with chain-of-thought reasoning by introducing intermediate visual goals as explicit ... | p. 8 (4.4. Better Visual Reasoning Helps) |
| body limitation/failure cue | By analyzing rollout videos of failure cases, we found that baseline methods occasionally overfit to visual cues while disregarding language instructions. | p. 6 (4.2. Evaluations Results) |
| body limitation/failure cue | Compared to OpenVLA [29], CoT-VLA shows slightly lower success rates in visual and language generalization tasks due to grasping failures from action chunking (see ... | p. 6 (4.2. Evaluations Results) |
| body limitation/failure cue | Following [29], we evaluate on four tasks designed in [29] to evaluate visual robustness (varying distractors), motion generalization (novel object positions), semantic generalization (unseen ... | p. 5 (4.1. Experimental Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| LIBERO We present quantitative results in Table 1, where each method is evaluated over 500 trials per task suite, with 3 random seeds. | p. 6 (4.2. Evaluations Results) |
| At each visual position j, the depth transformer, Pδ, autoregressively predicts D residual tokens (kj1, ..., kjD) based on the LLM-generated code embedding hj. | p. 4 (3.3. Training Procedures) |
| For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each. | p. 5 (10. For complete dataset specifications and training hyper) |
| We evaluate SUSIE using their published checkpoint on Bridge-V2. | p. 6 (4.1. Experimental Setup) |
| Success rates across four generalization categories, with 10 trials per category and partial credit scoring following [29]. | p. 7 (4.3. Ablation Study) |
| We evaluate four model variants: VLA - a baseline implementation following the standard VLA framework [29], with the same VILA-U backbone but without chain-of-thought ... | p. 7 (4.3. Ablation Study) |
| We evaluate each task across 5 trials under two conditions: (1) CoT-VLA using its generated goal images and (2) CoT-VLA using ground-truth goal images ... | p. 8 (4.4. Better Visual Reasoning Helps) |
| Recent advancement in fast image generation or fast LLM inference techniques could potentially improve the throughput of the model [7, 31, 33, 57, 73] ... | p. 8 (4.4. Better Visual Reasoning Helps) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved visual ...
- **p. 8 / 4.4. Better Visual Reasoning Helps - extractive body cue:** Conclusion, Limitations and Future Work In this work, we introduce CoT-VLA, bridging visionlanguage-action models with chain-of-thought reasoning by introducing intermediate visual goals as explicit reasoning ...
- **p. 6 / 4.2. Evaluations Results - extractive body cue:** By analyzing rollout videos of failure cases, we found that baseline methods occasionally overfit to visual cues while disregarding language instructions.
- **p. 6 / 4.2. Evaluations Results - extractive body cue:** Compared to OpenVLA [29], CoT-VLA shows slightly lower success rates in visual and language generalization tasks due to grasping failures from action chunking (see Section ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Following [29], we evaluate on four tasks designed in [29] to evaluate visual robustness (varying distractors), motion generalization (novel object positions), semantic generalization (unseen language ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments), p. 7 (4.3. Ablation Study), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Better Visual Reasoning Helps), p. 6 (4.2. Evaluations Results), metrics p. 6 (4.2. Evaluations Results), p. 6 (4.2. Evaluations Results), p. 5 (Figure/Table caption), p. 7 (4.3. Ablation Study), p. 8 (4.4. Better Visual Reasoning Helps), p. 8 (4.4. Better Visual Reasoning Helps), baselines p. 5 (4. Experiments), p. 6 (4.2. Evaluations Results), p. 6 (4.2. Evaluations Results), p. 8 (4.4. Better Visual Reasoning Helps), p. 5 (10. For complete dataset specifications and training hyper), p. 7 (4.3. Ablation Study), results p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluations Results), p. 8 (4.3. Ablation Study), p. 6 (4.2. Evaluations Results), p. 7 (4.3. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
