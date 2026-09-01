# Evaluation - Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.1. Real-Robot Task Finetuning), p. 5 (4.1. Baselines), p. 5 (4.4. CALVIN), p. 6 (4.6. Ablation Study), p. 6 (4.4. CALVIN), p. 8 (5.1. Real-Robot Task Finetuning)): Overall, Dita achieves a 63.8% success rate on two-step 7692

## Evaluation Body Digest

- **p. 6 / 4.4. CALVIN - extractive PDF cue:** The results illustrate that Dita excels at discerning subtle visual nuances in long-horizon tasks and generalizes proficiently across diverse environments, effectively transferring knowledge from extensive, ...
- **p. 4 / 4. Simulation Experiments - extractive PDF cue:** We strive to develop a robust foundational VLA model that is both scalable across diverse simulation benchmarks and adaptive to new complex tasks in unseen ...
- **p. 4 / 4. Simulation Experiments - extractive PDF cue:** To assess the capabilities of the pretrained model, we conduct evaluations across four simulation benchmarks in this section: 1) SimplerEnv [37] (Google Robot) demonstrates the ...
- **p. 5 / 4.3. LIBERO - extractive PDF cue:** LIBERO [40] is a comprehensive benchmark for knowledge transfer in multitask and lifelong robot learning.
- **p. 7 / 5.1. Real-Robot Task Finetuning - extractive PDF cue:** Given the data domain gap between our robot platform and the pretrain dataset, we primarily evaluate Dita on 10-shot generalization for the following challenging tasks ...
- **p. 7 / 5. Real-Robot Experiments - extractive PDF cue:** For real-robot experiments, We employ 10-shot finetuning to assess the model's adaptability in complex, long-horizon, multi-modal tasks within unseen robot environments.
- **p. 5 / 4.2. SimplerEnv - extractive PDF cue:** SimplerEnv [37] is a Real-to-Sim platform designed to evaluate policies learned from real robot data within a simulation environment.
- **p. 6 / 4.6. Ablation Study - extractive PDF cue:** We argue that 2-frame observations strike an optimal balance, providing sufficient visual distinction between objects in the workspace and the robot states.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Simulation Experiments (p. 4); 5. Real-Robot Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Real-Robot Task Finetuning | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, Dita achieves a 63.8% success rate on two-step 7692 | p. 7 (5.1. Real-Robot Task Finetuning) |
| 4.1. Baselines | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rate comparison with RT-1-X [8], Octo-Base [72] and OpenVLA-7B [32] on SimplerEnv (both match and variant results of Google Robot [8]). | p. 5 (4.1. Baselines) |
| 4.4. CALVIN | EMPIRICAL / REAL-ROBOT OR HARDWARE | Without whistles and bells, the proposed Dita achieves comparable performance among methods relying solely on a single RGB camera for observation. | p. 5 (4.4. CALVIN) |
| 4.6. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | When the trajectory length is 32, Dita with 2-frame observations achieves superior performance. | p. 6 (4.6. Ablation Study) |
| 4.4. CALVIN | EMPIRICAL / REAL-ROBOT OR HARDWARE | Additionally, Dita shows superior performance on more complex tasks and outperforms EDiff ω↑s by 20% in the PickSingleYCB task and by 12% in the ... | p. 6 (4.4. CALVIN) |

## Dataset / Benchmark Role

- **p. 6 / 4.4. CALVIN - extractive PDF cue:** The results illustrate that Dita excels at discerning subtle visual nuances in long-horizon tasks and generalizes proficiently across diverse environments, effectively transferring knowledge from extensive, ...
- **p. 4 / 4. Simulation Experiments - extractive PDF cue:** We strive to develop a robust foundational VLA model that is both scalable across diverse simulation benchmarks and adaptive to new complex tasks in unseen ...
- **p. 4 / 4. Simulation Experiments - extractive PDF cue:** To assess the capabilities of the pretrained model, we conduct evaluations across four simulation benchmarks in this section: 1) SimplerEnv [37] (Google Robot) demonstrates the ...
- **p. 5 / 4.3. LIBERO - extractive PDF cue:** LIBERO [40] is a comprehensive benchmark for knowledge transfer in multitask and lifelong robot learning.
- **p. 7 / 5.1. Real-Robot Task Finetuning - extractive PDF cue:** Given the data domain gap between our robot platform and the pretrain dataset, we primarily evaluate Dita on 10-shot generalization for the following challenging tasks ...
- **p. 7 / 5. Real-Robot Experiments - extractive PDF cue:** For real-robot experiments, We employ 10-shot finetuning to assess the model's adaptability in complex, long-horizon, multi-modal tasks within unseen robot environments.
- **p. 5 / 4.2. SimplerEnv - extractive PDF cue:** SimplerEnv [37] is a Real-to-Sim platform designed to evaluate policies learned from real robot data within a simulation environment.
- **p. 6 / 4.6. Ablation Study - extractive PDF cue:** We argue that 2-frame observations strike an optimal balance, providing sufficient visual distinction between objects in the workspace and the robot states.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We introduce Dita, an open-source, simple yet effective policy for generalist robotic learning. Pretrained on large-scale cross- embodiment datasets, Dita enables 10-shot adaptation ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Illustrations of different generalist robot policy architec- tures. Left head: the common robot Transformer architecture with discretization actions, e.g., Robot Transformer [8, 9] ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Our model employs a Transformer-based diffusion architecture, integrating a pretrained CLIP network to extract language instruction tokens. The DinoV2 [53] model encodes image ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Success rate comparison with RT-1-X [8], Octo-Base [72] and OpenVLA-7B [32] on SimplerEnv (both match and variant results of Google Robot [8]).
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison with Diffusion Policy (denoted as DP*, training from scratch) [17], Octo [72], and OpenVLA [32] on LIBERO [40]. Except for Dita results, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. The comparisons with state-of-the-art approaches on Calvin (ABC→D) with the metrics of success rate and average success length. The abbreviations denote different input ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Comparison of our model with two baseline methods (dis- cretization and diffusion head) on ManiSkill2 success rate. The abbreviations denote the task names: ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation on ManiSkill2 about the observation length (# obs) and the trajectory length (# traj). # obs # traj All PickC StackC S-YCB ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The results illustrate that Dita excels at discerning subtle visual nuances in long-horizon tasks and generalizes proficiently across diverse environments, effectively transferring knowledge from ... | embodiment, simulator version and control stack | p. 6 (4.4. CALVIN), p. 4 (4. Simulation Experiments) |
| Task/environment | We strive to develop a robust foundational VLA model that is both scalable across diverse simulation benchmarks and adaptive to new complex tasks in ... | reset, timeout, object/scene variation | p. 4 (4. Simulation Experiments), p. 4 (4. Simulation Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3.1. Architecture), p. 4 (3.2. Training Objective) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Success rate comparison with RT-1-X [8], Octo-Base [72] and OpenVLA-7B [32] on SimplerEnv (both match and variant results of Google Robot [8]). | definition/direction/unit from same section | p. 5 (4.1. Baselines) |
| Method SPATIAL OBJECT GOAL LONG Averge DP*[17] 78.3% 92.5% 68.3% 50.5% 72.4% Octo [72] 78.9% 85.7% 84.6% 51.1% 75.1% OpenVLA [32] 84.9% 88.4% 79.2% ... | definition/direction/unit from same section | p. 5 (4.3. LIBERO) |
| As shown in Table 5, success rate drops sharply when the observation length is increased to 3. | definition/direction/unit from same section | p. 6 (4.6. Ablation Study) |
| Comparison of our model with two baseline methods (discretization and diffusion head) on ManiSkill2 success rate. | definition/direction/unit from same section | p. 6 (4.4. CALVIN) |
| Overall, Dita achieves a 63.8% success rate on two-step 7692 | definition/direction/unit from same section | p. 7 (5.1. Real-Robot Task Finetuning) |
| Since the open/close drawer tasks are single-step, they are excluded from the calculation of the average success rate. | definition/direction/unit from same section | p. 8 (5.1. Real-Robot Task Finetuning) |
| In each stacked bar, the light-colored region represents the model's success rate in the first stage, while the dark-colored region indicates the contribution of ... | definition/direction/unit from same section | p. 8 (5.1. Real-Robot Task Finetuning) |
| Figure 1. We introduce Dita, an open-source, simple yet effective policy for generalist robotic learning. Pretrained on large-scale cross- embodiment datasets, Dita enables 10-shot ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also implement RT-1 [8] style baseline model EDisc ω↑s with an architecture similar to ours for comparison. | comparison identity and matched condition | p. 6 (4.4. CALVIN) |
| Comparison of our model with two baseline methods (discretization and diffusion head) on ManiSkill2 success rate. | comparison identity and matched condition | p. 6 (4.4. CALVIN) |
| Therefore, in addition to Octo and OpenVLA, we design a multimodal diffusion policy baseline based on a causal Transformer for comparison, which incorporates a ... | comparison identity and matched condition | p. 7 (5.1. Real-Robot Task Finetuning) |
| According to the visualized comparison, those baseline methods usually fail to grasp the correct position under the 10-shot setting, e.g., "fail to insert the ... | comparison identity and matched condition | p. 8 (5.2. Qualitative Comparison) |
| This approach introduces additional parameters (the extra MLP) compared to Dita. | comparison identity and matched condition | p. 5 (4.1. Baselines) |
| Dita does not utilize the play data which provides external trajectory data compared to the labeled data, while GR-MG uses it for training the ... | comparison identity and matched condition | p. 5 (4.4. CALVIN) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Furthermore, Dita surpasses its non-pretrained variant by a margin of 1.23, underscoring its superior transferability. | component/input/data sensitivity | p. 5 (4.4. CALVIN) |
| Success rate comparison with RT-1-X [8], Octo-Base [72] and OpenVLA-7B [32] on SimplerEnv (both match and variant results of Google Robot [8]). | component/input/data sensitivity | p. 5 (4.1. Baselines) |
| In this section, we conduct an ablation study on key factors in the model architecture design, including observation length, trajectory length, and denoising steps. | component/input/data sensitivity | p. 6 (4.6. Ablation Study) |
| The results illustrate that Dita excels at discerning subtle visual nuances in long-horizon tasks and generalizes proficiently across diverse environments, effectively transferring knowledge from ... | component/input/data sensitivity | p. 6 (4.4. CALVIN) |
| Ablation on ManiSkill2 about the observation length (# obs) and the trajectory length (# traj). # obs # traj All PickC StackC S-YCB C-YCB ... | component/input/data sensitivity | p. 7 (4.6. Ablation Study) |
| Figure 1. We introduce Dita, an open-source, simple yet effective policy for generalist robotic learning. Pretrained on large-scale cross- embodiment datasets, Dita enables 10-shot ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce Dita, a Diffusion Transformer (DiT) Policy that capitalizes on the Transformer architecture, as demonstrated in prior work [8, 9, ... | Overall, Dita achieves a 63.8% success rate on two-step 7692 | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.1. Real-Robot Task Finetuning), p. 5 (4.1. Baselines), p. 5 (4.4. CALVIN), p. 6 (4.6. Ablation Study), p. 6 (4.4. CALVIN), p. 8 (5.1. Real-Robot Task Finetuning) |
| Primary metric/result | Success rate comparison with RT-1-X [8], Octo-Base [72] and OpenVLA-7B [32] on SimplerEnv (both match and variant results of Google Robot [8]). | numeric claim only at cited anchor | p. 5 (4.1. Baselines) |

- Numeric sentences retained from the body:
- **p. 5 / 4.4. CALVIN - extractive PDF cue:** In contrast, employing diffusion head underperforms Dita by 0.45 points with similar pretrained weights, highlighting the 7690
- **p. 6 / 4.4. CALVIN - extractive PDF cue:** To construct the benchmark, we select 5 tasks (PickCube-v0, StackCube-v0, PickSingleYCB-v0, PickClutterYCB-v0, PickSingleEGAD-v0) from ManiSkill2 and create a camera pool comprising 300K random cameras.
- **p. 7 / 5.1. Real-Robot Task Finetuning - extractive PDF cue:** The system is operating under control frequency of 3Hz.
- **p. 7 / 5.1. Real-Robot Task Finetuning - extractive PDF cue:** 10 samples are collected for each task, with position variances introduced during evaluation to assess generalization performance. • Pour.
- **p. 7 / 5.1. Real-Robot Task Finetuning - extractive PDF cue:** We further devise several longhorizon tasks (more than 3 steps), including "Pick up the bowl within the drawer and pour the coffee beans into the ...
- **p. 7 / 5.1. Real-Robot Task Finetuning - extractive PDF cue:** We finetune the Dita on the aforementioned multiple manipulation tasks, with data collected on the same platform, using LoRA [26] for fair comparison and AdamW ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Failures are highlighted with red circles. | p. 8 (5.1. Real-Robot Task Finetuning) |
| body limitation/failure cue | For long-horizon tasks, OpenVLA effectively completes the first task but fails to handle the longhorizon task, such as completely misunderstanding the insert operation. | p. 8 (5.1. Real-Robot Task Finetuning) |
| body limitation/failure cue | Dita does not utilize the play data which provides external trajectory data compared to the labeled data, while GR-MG uses it for training the ... | p. 5 (4.4. CALVIN) |
| body limitation/failure cue | Figure 1. We introduce Dita, an open-source, simple yet effective policy for generalist robotic learning. Pretrained on large-scale cross- embodiment datasets, Dita enables 10-shot ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Illustrations of different generalist robot policy architec- tures. Left head: the common robot Transformer architecture with discretization actions, e.g., Robot Transformer [8, ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | We strive to develop a robust foundational VLA model that is both scalable across diverse simulation benchmarks and adaptive to new complex tasks in ... | p. 4 (4. Simulation Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training is conducted with a batch size of 8192 across 32 NVIDIA A100 GPUs, allocating 256 samples per GPU. | p. 4 (3.4. Pretraining Details) |
| The network is optimized by AdamW [43] for 100,000 steps, with learning rates of 1e↓4 for both the causal Transformer and Q-Former, and 1e↓5 ... | p. 4 (3.4. Pretraining Details) |
| The number of timesteps is set to 100 for DDPM [25], and the batch size of 512. | p. 7 (5.1. Real-Robot Task Finetuning) |
| Robot control is managed from a desktop computer running ROS, communicating with the model-deploy server with 1 NVIDIA A100 GPU. | p. 7 (5.1. Real-Robot Task Finetuning) |
| Octo & OpenVLA We also reproduce these two opensource VLA models using their released checkpoints, as they employ the same multimodal inputs (language instruction ... | p. 5 (4.1. Baselines) |
| In this section, we conduct an ablation study on key factors in the model architecture design, including observation length, trajectory length, and denoising steps. | p. 6 (4.6. Ablation Study) |
| Each task is manually divided into two sequential steps, except for the last two single-step tasks. | p. 8 (5.1. Real-Robot Task Finetuning) |
| Finally, we present the data and implementation specifics for the pretraining of our model. | p. 3 (3. Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5.1. Real-Robot Task Finetuning - extractive PDF cue:** Failures are highlighted with red circles.
- **p. 8 / 5.1. Real-Robot Task Finetuning - extractive PDF cue:** For long-horizon tasks, OpenVLA effectively completes the first task but fails to handle the longhorizon task, such as completely misunderstanding the insert operation.
- **p. 5 / 4.4. CALVIN - extractive PDF cue:** Dita does not utilize the play data which provides external trajectory data compared to the labeled data, while GR-MG uses it for training the policy.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We introduce Dita, an open-source, simple yet effective policy for generalist robotic learning. Pretrained on large-scale cross- embodiment datasets, Dita enables 10-shot adaptation ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Illustrations of different generalist robot policy architec- tures. Left head: the common robot Transformer architecture with discretization actions, e.g., Robot Transformer [8, 9] ...
- **p. 4 / 4. Simulation Experiments - extractive PDF cue:** We strive to develop a robust foundational VLA model that is both scalable across diverse simulation benchmarks and adaptive to new complex tasks in unseen ...

- **PDF anchors reviewed:** datasets p. 6 (4.4. CALVIN), p. 4 (4. Simulation Experiments), p. 4 (4. Simulation Experiments), p. 5 (4.3. LIBERO), p. 7 (5.1. Real-Robot Task Finetuning), p. 7 (5. Real-Robot Experiments), metrics p. 5 (4.1. Baselines), p. 5 (4.3. LIBERO), p. 6 (4.6. Ablation Study), p. 6 (4.4. CALVIN), p. 7 (5.1. Real-Robot Task Finetuning), p. 8 (5.1. Real-Robot Task Finetuning), baselines p. 6 (4.4. CALVIN), p. 6 (4.4. CALVIN), p. 7 (5.1. Real-Robot Task Finetuning), p. 8 (5.2. Qualitative Comparison), p. 5 (4.1. Baselines), p. 5 (4.4. CALVIN), results p. 7 (5.1. Real-Robot Task Finetuning), p. 5 (4.1. Baselines), p. 5 (4.4. CALVIN), p. 6 (4.6. Ablation Study), p. 6 (4.4. CALVIN), p. 8 (5.1. Real-Robot Task Finetuning).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
