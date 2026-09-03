# Evaluation - Vision-Language-Action Instruction Tuning: From Understanding to Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=tsxwloasw5; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248397. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 EXPERIMENT), p. 9 (5 EXPERIMENT), p. 30 (Figure/Table caption), p. 8 (5 EXPERIMENT), p. 26 (Figure/Table caption), p. 36 (Figure/Table caption)): Meanwhile, InstructVLA (generalist) not only maintains strong performance on SimplerEnv's atomic instructions but also achieves a 31.7% relative improvement on SimplerEnv-Instruct over the state-of-the-art baseline (OpenVLA with GPT-4o).

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENT - extractive body cue:** (b) SimplerEnv: This benchmark (Li et al., 2024d) provides real-to-sim evaluation on large-scale manipulation datasets, incorporating visual matching and variance aggregation to assess generalization.
- **p. 8 / 5 EXPERIMENT - extractive body cue:** 5.2 REAL-WORLD EXPERIMENTS To evaluate InstructVLA in real-world scenarios, we conduct zero-shot experiments on the WidowX250 Arm and few-shot experiments on the Franka Research 3 ...
- **p. 8 / 5 EXPERIMENT - extractive body cue:** The zero-shot tasks are set in a kitchen environment following the Bridge dataset.
- **p. 9 / 5 EXPERIMENT - extractive body cue:** 15.3 65.0 48.4 InstructVLA 29.1 64.8 52.9 0 10 20 30 40 50 60 70 WidowX Robot Google Robot Overall Finetuning Action Expert Freeze Action ...
- **p. 7 / 5 EXPERIMENT - extractive body cue:** In addition, we assess embodied understanding in Section A.2 and manipulation performance on the LIBERO (Liu et al., 2024b) benchmark in Section A.3.
- **p. 9 / 5 EXPERIMENT - extractive body cue:** As shown in Table 2 the expert model with robot state generally performs better.
- **p. 26 / Figure/Table caption - extractive body cue:** Table 10: LIBERO benchmark results. We present the success rate and standard error for each method across four task suites, which are averaged over three ...
- **p. 44 / Figure/Table caption - extractive body cue:** Table 20: Evaluation results under different training settings. We report mean success rates (%± standard error) across tasks, with Overall denoting the average over all ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 EXPERIMENT (p. 7); A.2 Embodied Understanding Evaluation (p. 18); A.3 Extra Manipulation Benchmark (p. 18); A MORE EXPERIMENTS AND ANALYSIS (p. 20); A.2 EMBODIED UNDERSTANDING EVALUATION (p. 24); A.3 EXTRA MANIPULATION BENCHMARK (p. 26).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Meanwhile, InstructVLA (generalist) not only maintains strong performance on SimplerEnv's atomic instructions but also achieves a 31.7% relative improvement on SimplerEnv-Instruct over the state-of-the-art ... | p. 8 (5 EXPERIMENT) |
| 5 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 3, introducing "language motion" (textual descriptions of low-level actions) supervision enhances the VLM's ability to associate visual cues with manipulation ... | p. 9 (5 EXPERIMENT) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm ... | p. 30 (Figure/Table caption) |
| 5 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | On reasoning and math tasks, InstructVLA achieves a 2.5× improvement over π0, which behaves close to random guessing. | p. 8 (5 EXPERIMENT) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 10: LIBERO benchmark results. We present the success rate and standard error for each method across four task suites, which are averaged over ... | p. 26 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENT - extractive body cue:** (b) SimplerEnv: This benchmark (Li et al., 2024d) provides real-to-sim evaluation on large-scale manipulation datasets, incorporating visual matching and variance aggregation to assess generalization.
- **p. 8 / 5 EXPERIMENT - extractive body cue:** 5.2 REAL-WORLD EXPERIMENTS To evaluate InstructVLA in real-world scenarios, we conduct zero-shot experiments on the WidowX250 Arm and few-shot experiments on the Franka Research 3 ...
- **p. 8 / 5 EXPERIMENT - extractive body cue:** The zero-shot tasks are set in a kitchen environment following the Bridge dataset.
- **p. 9 / 5 EXPERIMENT - extractive body cue:** 15.3 65.0 48.4 InstructVLA 29.1 64.8 52.9 0 10 20 30 40 50 60 70 WidowX Robot Google Robot Overall Finetuning Action Expert Freeze Action ...
- **p. 7 / 5 EXPERIMENT - extractive body cue:** In addition, we assess embodied understanding in Section A.2 and manipulation performance on the LIBERO (Liu et al., 2024b) benchmark in Section A.3.
- **p. 9 / 5 EXPERIMENT - extractive body cue:** As shown in Table 2 the expert model with robot state generally performs better.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Method overview. InstructVLA integrates vision-language understanding with precise robotic control to achieve reasoning-guided manipulation. Its core training strategy, Vision-Language- Action Instruction Tuning, enhances ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the InstructVLA. InstructVLA integrates the multimodal reasoning capa- bilities of a vision-language model with robotic manipulation. Generation consists of three steps: ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Vision-language-action instruction tuning data examples. Annotations focus on: (1) improving scene understanding and (2) learning instruction following and planning. Inference. InstructVLA integrates language ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Simpler-Instruct. Six representative test cases with instructions and InstructVLA responses. Prior VLAs exhibit limited generalization compared to InstructVLA. Vision-language-action instruction tuning data. To ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Multimodal understanding. #Params is the size of LLM backbone. S. denotes robot state. Methods #Params Multi-modal Understanding Benchmarks VQA Benchmarks MMMUVal MM-Vet MMStar
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Robotic manipulation. Google and WidowX Robot denote two embodiments in SimplerEnv. For SimplerEnv-Instruct, we focus on two reasoning levels instead of embodiments. Magma† ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Real-world experiments. "Atomic" refers to atomic instructions. For the Kitchen and math settings, InstructVLA's responses are presented. 5.1 MAIN RESULTS We present our ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Ablation of action expert vision design and language motion. "w/o Lang." denotes without using lan- guage motion. "w/o FiLM" denotes us- ing only ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (b) SimplerEnv: This benchmark (Li et al., 2024d) provides real-to-sim evaluation on large-scale manipulation datasets, incorporating visual matching and variance aggregation to assess generalization. | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENT), p. 8 (5 EXPERIMENT) |
| Task/environment | 5.2 REAL-WORLD EXPERIMENTS To evaluate InstructVLA in real-world scenarios, we conduct zero-shot experiments on the WidowX250 Arm and few-shot experiments on the Franka Research ... | reset, timeout, object/scene variation | p. 8 (5 EXPERIMENT), p. 8 (5 EXPERIMENT) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3. Atomic-Instruction Manipulation), p. 5 (3. Atomic-Instruction Manipulation) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (ABSTRACT), p. 2 (3. Atomic-Instruction Manipulation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 10: LIBERO benchmark results. We present the success rate and standard error for each method across four task suites, which are averaged over ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Table 20: Evaluation results under different training settings. We report mean success rates (%± standard error) across tasks, with Overall denoting the average over ... | definition/direction/unit from same section | p. 44 (Figure/Table caption) |
| As shown in Table 3, introducing "language motion" (textual descriptions of low-level actions) supervision enhances the VLM's ability to associate visual cues with manipulation ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENT) |
| Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm ... | definition/direction/unit from same section | p. 30 (Figure/Table caption) |
| Table 13: Data annotation success rate. GPT- 4o shows a significant performance drop without ground truth instructions during data annotation. | definition/direction/unit from same section | p. 36 (Figure/Table caption) |
| Figure 18: Reasoning cases in SimplerEnv-Instruct. Three cases of the VL fine-tuned OpenVLA and InstructVLA-Generalist. "SR" denotes success rate. We present three representative reasoning ... | definition/direction/unit from same section | p. 29 (Figure/Table caption) |
| Accordingly, we report its official score on SimplerEnv and re-evaluate its performance on SimplerEnv-Instruct under the sampling setting. | definition/direction/unit from same section | p. 7 (5 EXPERIMENT) |
| (2024), a β distribution is used to enhance accuracy on the noisier time steps. | definition/direction/unit from same section | p. 7 (5 EXPERIMENT) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In Table 2, InstructVLA (expert) outperforms the expert baseline SpatialVLA by 33.3% on SimplerEnv. | comparison identity and matched condition | p. 8 (5 EXPERIMENT) |
| In Table 1, using the same generalist model InstructVLA (generalist), it not only outperforms the co-trained baseline Magma, but is also comparable to its ... | comparison identity and matched condition | p. 8 (5 EXPERIMENT) |
| During evaluation, InstructVLA and other baselines use a temperature of 0 without sampling to expedite generation. | comparison identity and matched condition | p. 7 (5 EXPERIMENT) |
| Figure 21: GPT-4o as the auxiliary system 2. We prompt GPT-4o with the first image from the environment along with the instruction, asking it ... | comparison identity and matched condition | p. 31 (Figure/Table caption) |
| We categorize the baselines into three groups: (1) Multimodal VLMs, including Bunny(He et al., 2024), PaliGemma (Beyer et al., 2024), Eagle2 (Li et al., ... | comparison identity and matched condition | p. 7 (5 EXPERIMENT) |
| As shown in Figure 6 (b), four paradigms are compared. | comparison identity and matched condition | p. 9 (5 EXPERIMENT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 11: Test-time tinking and dual-frequency evaluation. "Expert" refers to the model after action pretraining, while "Generalist" denotes the model after VLA-IT tuning. For ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| We observe that it consistently generates manipulationstyle CoT responses, without demonstrating effective instruction-following ability. | component/input/data sensitivity | p. 8 (5 EXPERIMENT) |
| Table 3: Ablation of action expert vision design and language motion. "w/o Lang." denotes without using lan- guage motion. "w/o FiLM" denotes us- ing ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 5: Instruction tuning data ablation. We evaluate three settings: without VLA-IT data, with data only on Bridge, and with VLA-IT data on both ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| As shown in Figure 6(a), we examine the effect of VLA instruction tuning by comparing two configurations: (1) finetuning only the VLM, and (2) ... | component/input/data sensitivity | p. 9 (5 EXPERIMENT) |
| During evaluation, InstructVLA and other baselines use a temperature of 0 without sampling to expedite generation. | component/input/data sensitivity | p. 7 (5 EXPERIMENT) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a unified framework that enables simultaneous multimodal reasoning and language-steered latent action planning using a single VLM (Figure 2 (1) and (2)). | Meanwhile, InstructVLA (generalist) not only maintains strong performance on SimplerEnv's atomic instructions but also achieves a 31.7% relative improvement on SimplerEnv-Instruct over the state-of-the-art ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 EXPERIMENT), p. 9 (5 EXPERIMENT), p. 30 (Figure/Table caption), p. 8 (5 EXPERIMENT), p. 26 (Figure/Table caption), p. 36 (Figure/Table caption) |
| Primary metric/result | As shown in Table 3, introducing "language motion" (textual descriptions of low-level actions) supervision enhances the VLM's ability to associate visual cues with manipulation ... | numeric claim only at cited anchor | p. 9 (5 EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 8 / 5 EXPERIMENT - extractive body cue:** 5.2 REAL-WORLD EXPERIMENTS To evaluate InstructVLA in real-world scenarios, we conduct zero-shot experiments on the WidowX250 Arm and few-shot experiments on the Franka Research 3 ...
- **p. 6 / 3. Atomic-Instruction Manipulation - extractive body cue:** In total, we curated 80 tasks with 1.1K trials, about one third the size of SimplerEnv, keeping evaluation practical. • Task aggregation.
- **p. 6 / 3. Atomic-Instruction Manipulation - extractive body cue:** (50 tasks; examples shown in Figure 4, left).
- **p. 6 / 3. Atomic-Instruction Manipulation - extractive body cue:** (30 tasks; examples shown in Figure 4, right).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm ... | p. 30 (Figure/Table caption) |
| body limitation/failure cue | Figure 18: Reasoning cases in SimplerEnv-Instruct. Three cases of the VL fine-tuned OpenVLA and InstructVLA-Generalist. "SR" denotes success rate. We present three representative reasoning ... | p. 29 (Figure/Table caption) |
| body limitation/failure cue | Figure 19: Failure case 1 of InstructVLA. The model receives only a third-person view image as visual input, making it difficult to estimate depth ... | p. 30 (Figure/Table caption) |
| body limitation/failure cue | However, GPT-4o faces the same challenges in accurate instruction rewriting as noted in Section 4.1, and fails to outperform InstructVLA (Generalist). | p. 8 (5 EXPERIMENT) |
| body limitation/failure cue | Figure 34: Light distraction. Stable visual features from DINO and SigLIP enable the model to operate robustly under extreme out-of-distribution lighting conditions. 46 | p. 46 (Figure/Table caption) |
| body limitation/failure cue | However, we observe that finetuning OpenVLA on multimodal and manipulation datasets does not fully restore its original multimodal capabilities, although it does improve task ... | p. 8 (5 EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| (2025c), while the action expert operates at 224 × 224 as in (Kim et al., 2024), using a fixed learning rate of 5e-5 without ... | p. 7 (5 EXPERIMENT) |
| We re-evaluate Magma with official checkpoint1. | p. 7 (5 EXPERIMENT) |
| Incorporating FiLM to the ViT encoder yields a further 15.3% improvement by modulating visual features with latent actions. | p. 9 (5 EXPERIMENT) |
| Removing the DINOv2-based ViT encoder from the action expert results in a 50.0% performance drop, highlighting its critical role in capturing task-relevant visual cues. | p. 9 (5 EXPERIMENT) |
| Large-scale pretraining has produced versatile foundation models in computer vision (CV) (Oquab et al., 2023; Radford et al., 2021) and natural language processing (NLP) ... | p. 1 (1 INTRODUCTION) |
| The flow matching action expert decodes the final actions, conditioned on latent actions. | p. 4 (3. Atomic-Instruction Manipulation) |
| Generation consists of three steps: (1) asynchronous auto-regressive reasoning by the VLM, (2) latent action generation, and (3) action decoding. | p. 4 (3. Atomic-Instruction Manipulation) |
| The remaining action queries are then decoded in parallel within a single forward pass of the VLM. | p. 5 (3. Atomic-Instruction Manipulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 30 / Figure/Table caption - extractive body cue:** Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm reflection ...
- **p. 29 / Figure/Table caption - extractive body cue:** Figure 18: Reasoning cases in SimplerEnv-Instruct. Three cases of the VL fine-tuned OpenVLA and InstructVLA-Generalist. "SR" denotes success rate. We present three representative reasoning cases ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 19: Failure case 1 of InstructVLA. The model receives only a third-person view image as visual input, making it difficult to estimate depth or ...
- **p. 8 / 5 EXPERIMENT - extractive body cue:** However, GPT-4o faces the same challenges in accurate instruction rewriting as noted in Section 4.1, and fails to outperform InstructVLA (Generalist).
- **p. 46 / Figure/Table caption - extractive body cue:** Figure 34: Light distraction. Stable visual features from DINO and SigLIP enable the model to operate robustly under extreme out-of-distribution lighting conditions. 46
- **p. 8 / 5 EXPERIMENT - extractive body cue:** However, we observe that finetuning OpenVLA on multimodal and manipulation datasets does not fully restore its original multimodal capabilities, although it does improve task performance.

- **Evidence anchors reviewed:** datasets p. 7 (5 EXPERIMENT), p. 8 (5 EXPERIMENT), p. 8 (5 EXPERIMENT), p. 9 (5 EXPERIMENT), p. 7 (5 EXPERIMENT), p. 9 (5 EXPERIMENT), metrics p. 26 (Figure/Table caption), p. 44 (Figure/Table caption), p. 9 (5 EXPERIMENT), p. 30 (Figure/Table caption), p. 36 (Figure/Table caption), p. 29 (Figure/Table caption), baselines p. 8 (5 EXPERIMENT), p. 8 (5 EXPERIMENT), p. 7 (5 EXPERIMENT), p. 31 (Figure/Table caption), p. 7 (5 EXPERIMENT), p. 9 (5 EXPERIMENT), results p. 8 (5 EXPERIMENT), p. 9 (5 EXPERIMENT), p. 30 (Figure/Table caption), p. 8 (5 EXPERIMENT), p. 26 (Figure/Table caption), p. 36 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
