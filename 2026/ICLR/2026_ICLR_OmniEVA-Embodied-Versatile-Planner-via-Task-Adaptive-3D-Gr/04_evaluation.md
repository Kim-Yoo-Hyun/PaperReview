# Evaluation - OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (52 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=tkEmIJv1tB; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247599. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING)): Figure 5: Ablation Results of the proposed TE-GRPO Method on Local Mobile-Manipulation Tasks As shown in Figure 5, OmniEVA-ER-jointly optimized with rtask and rembod -demonstrates sub- stantial performance gains over ...

## Evaluation Body Digest

- **p. 27 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** For example: RT-1 (Brohan et al., 2022) dataset comprises over 130,000 real-world robotic demonstrations (episodes), covering more than 700 different tasks.
- **p. 30 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** E.2 END-TO-END ONLINE EVALUATION WITHIN SIMULATORS While previous works often evaluate the performance of the MLLMs on offline dataset, we also perform end-to-end evaluation to ...
- **p. 30 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** E.3 EXAMPLES OF THE IN-HOUSE PRIMITIVE EMBODIED BENCHMARKS E.3.1 WHERE2GO The Where2Go benchmark is constructed using the validation splits of the HM3D (Chang et al., ...
- **p. 27 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** It focus on hardware and kitchen tool objects to facilitate research in practical scenarios in which a robot manipulator needs to interact with the environment ...
- **p. 35 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** E.4 DOWNSTREAM TASK DESCRIPTION E.4.1 MOBILE PLACEMENT EASY For the Mobile Placement Easy benchmark, we constructed scenes with 8 tables in an office environment, with ...
- **p. 25 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** 2D Visual Grounding To endow OmniEVA with robust object detection and geometric localization capabilities, we incorporated the LVIS (Gupta et al., 2019) dataset-a comprehensive benchmark ...
- **p. 28 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** We train on the Scan2Cap dataset (Chen et al., 2021), which comprises 37K annotated samples across diverse indoor scenes.
- **p. 28 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Video-based Spatial Reasoning Despite the emergence of benchmarks such as OpenEQA (Majumdar et al., 2024) and VSI-Bench (Yang et al., 2025b), large-scale training datasets for ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** A IMPLEMENTATION DETAILS (p. 17); A.3 IMPLEMENTATION DETAIL OF EMBODIMENT-AWARE REASONING (p. 18); A.5 IMPLEMENTATION DETAIL OF EMBODIMENT-AWARE REINFORCED FINETUNING (p. 20); C ABLATION STUDY IMPLEMENTATION DETAILS (p. 23); C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION (p. 23).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Ablation Results of the proposed TE-GRPO Method on Local Mobile-Manipulation Tasks As shown in Figure 5, OmniEVA-ER-jointly optimized with rtask and rembod ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Results of Different Embodiment Execution Success Rate. Models / Embodiments Average (SR) Seen Arm Length (cm) Unseen Arm Length (cm) 75 88 ... | p. 10 (Figure/Table caption) |
| C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING | EMPIRICAL / REAL-ROBOT OR HARDWARE | The evaluation involves navigating to target poses, followed by assessing trajectory planning for safe mug placement on the table, with success rates calculated based ... | p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING | EMPIRICAL / REAL-ROBOT OR HARDWARE | Performance is assessed in 100 simulated scenarios, where we measure the success rates of planning placement trajectories. | p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING | EMPIRICAL / REAL-ROBOT OR HARDWARE | We select two metrics, the overall success rates and the average task completion times, to evaluate the effectiveness of the pipeline. | p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |

## Dataset / Benchmark Role

- **p. 27 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** For example: RT-1 (Brohan et al., 2022) dataset comprises over 130,000 real-world robotic demonstrations (episodes), covering more than 700 different tasks.
- **p. 30 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** E.2 END-TO-END ONLINE EVALUATION WITHIN SIMULATORS While previous works often evaluate the performance of the MLLMs on offline dataset, we also perform end-to-end evaluation to ...
- **p. 30 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** E.3 EXAMPLES OF THE IN-HOUSE PRIMITIVE EMBODIED BENCHMARKS E.3.1 WHERE2GO The Where2Go benchmark is constructed using the validation splits of the HM3D (Chang et al., ...
- **p. 27 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** It focus on hardware and kitchen tool objects to facilitate research in practical scenarios in which a robot manipulator needs to interact with the environment ...
- **p. 35 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** E.4 DOWNSTREAM TASK DESCRIPTION E.4.1 MOBILE PLACEMENT EASY For the Mobile Placement Easy benchmark, we constructed scenes with 8 tables in an office environment, with ...
- **p. 25 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** 2D Visual Grounding To endow OmniEVA with robust object detection and geometric localization capabilities, we incorporated the LVIS (Gupta et al., 2019) dataset-a comprehensive benchmark ...
- **p. 28 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** We train on the Scan2Cap dataset (Chen et al., 2021), which comprises 37K annotated samples across diverse indoor scenes.
- **p. 28 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Video-based Spatial Reasoning Despite the emergence of benchmarks such as OpenEQA (Majumdar et al., 2024) and VSI-Bench (Yang et al., 2025b), large-scale training datasets for ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Performance Comparison across 2D and 3D Embodied Reasoning Benchmarks. Despite recent progress, two core challenges remain. First, the geometric adaptability gap: mod- els ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Model Architecture of OmniEVA. Left: The overall architecture of OmniEVA, featuring a novel task-adaptive gated router that dynamically incorporates 3D positional embeddings. Middle: ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Training Paradigm of OmniEVA. The two-stage cascade progressively enhances embodied intelli- gence: Stage 1 builds a broad reasoning foundation, while Stage 2 grounds ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Results of Different 3D-Integration Methods. To ensure a fair comparison and isolate the impact of 3D integration, models were trained exclusively on the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: 3D Activation Analysis by Prompt Clustering: Prompts are embedded using a lightweight sentence transformer and clustered into semantic groups. The chart shows the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: 2D General Reasoning Benchmarks and In-house Benchmarks. [1] Hurst et al. (2024),[2] Team et al. (2025b),[3] Zhang et al. (2024b),[4] Li et al. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: 3D Reasoning Benchmarks. [1] Hong et al. (2023),[2] Zhu et al. (2024b),[3] Huang et al. (2023c),[4] Chen et al. (2024d),[5] Zhang et al. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: ObjNav Benchmarks [1] Wijmans et al. (2019),[2] Zhou et al. (2023),[3] Wu et al. (2024),[4] Yokoyama et al. (2024),[5] Huang et al. (2024),[6] ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For example: RT-1 (Brohan et al., 2022) dataset comprises over 130,000 real-world robotic demonstrations (episodes), covering more than 700 different tasks. | embodiment, simulator version and control stack | p. 27 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Task/environment | E.2 END-TO-END ONLINE EVALUATION WITHIN SIMULATORS While previous works often evaluate the performance of the MLLMs on offline dataset, we also perform end-to-end evaluation ... | reset, timeout, object/scene variation | p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 17 (A.2 INPUT MODALITIES AND OUTPUT REPRESENTATIONS), p. 18 (A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 5: Ablation Results of the proposed TE-GRPO Method on Local Mobile-Manipulation Tasks As shown in Figure 5, OmniEVA-ER-jointly optimized with rtask and rembod ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| The evaluation involves navigating to target poses, followed by assessing trajectory planning for safe mug placement on the table, with success rates calculated based ... | definition/direction/unit from same section | p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| We select two metrics, the overall success rates and the average task completion times, to evaluate the effectiveness of the pipeline. | definition/direction/unit from same section | p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Performance is assessed in 100 simulated scenarios, where we measure the success rates of planning placement trajectories. | definition/direction/unit from same section | p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Table 5: Results of Different Embodiment Execution Success Rate. Models / Embodiments Average (SR) Seen Arm Length (cm) Unseen Arm Length (cm) 75 88 ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| We use the success rate of placing objects as the evaluation metric. | definition/direction/unit from same section | p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Figure 8: OmniEVA's Performance with Dynamic Obstructions. (Top) Sequence showing successful detec- tion of a table after an occluding pedestrian moves away. (Bottom) Accurate ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Given a reward for the i-th response: ri,t(q, oi) = rformat i (oi) + racc i,t (q, oi) (11) 18 | definition/direction/unit from same section | p. 18 (A.3 IMPLEMENTATION DETAIL OF EMBODIMENT-AWARE REASONING) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 9: Case study illustrating OmniEVA's reasoning process under embodiment-aware constraints. C ABLATION STUDY IMPLEMENTATION DETAILS C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION To ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |
| As discussed in Section 4.2, both cross-attention variants led to significant performance drops compared to our gated fusion. | comparison identity and matched condition | p. 24 (C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION) |
| Figure 10: Architectural diagrams of the cross-attention-based 3D fusion baselines. (a) Separate Tokens: Visual and 3D tokens are processed as separate sequences. (b) Interleaved ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| Compared to simulator-based online evaluation, this VQA-style approach substantially reduces evaluation overhead. | comparison identity and matched condition | p. 29 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Table 1: Results of Different 3D-Integration Methods. To ensure a fair comparison and isolate the impact of 3D integration, models were trained exclusively on ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We categorize the benchmark into three progressive evaluation stages: • Large-Space Object Seeking: It is also referred as object navigation in prior work. | comparison identity and matched condition | p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 9: Case study illustrating OmniEVA's reasoning process under embodiment-aware constraints. C ABLATION STUDY IMPLEMENTATION DETAILS C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION To ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |
| Figure 6: Case Study of Gate Activation State. Selected examples from the validation dataset illustrate the most prominently activated and deactivated words within the ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| The architectural details are illustrated in Figure 10. • Separate Tokens Arrangement: In this variant, the sequences of visual tokens (V I) and 3D ... | component/input/data sensitivity | p. 23 (C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION) |
| As discussed in Section 4.2, both cross-attention variants led to significant performance drops compared to our gated fusion. | component/input/data sensitivity | p. 24 (C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION) |
| A standard cross-attention layer is then employed to enable interaction between these two modalities. • Interleaved Tokens Arrangement: In this variant, tokens are grouped ... | component/input/data sensitivity | p. 24 (C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION) |
| It poses a significant challenge for MLLMs, which often struggle to generate accurate 3D bounding boxes without priors from off-the28 | component/input/data sensitivity | p. 28 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these limitations, we introduce OmniEVA (Embodied Versatile Planner), a novel architecture that pioneers Task-Adaptive 3D Grounding and Embodiment-aware Reasoning. | Figure 5: Ablation Results of the proposed TE-GRPO Method on Local Mobile-Manipulation Tasks As shown in Figure 5, OmniEVA-ER-jointly optimized with rtask and rembod ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Primary metric/result | Table 5: Results of Different Embodiment Execution Success Rate. Models / Embodiments Average (SR) Seen Arm Length (cm) Unseen Arm Length (cm) 75 88 ... | numeric claim only at cited anchor | p. 10 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** For video-based inputs, we uniformly sample 16 frames during training and 32 frames during inference, striking a balance between temporal granularity and computational efficiency.
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** To handle 3D spatial information, we voxelize both point clouds for positioning and 3D bounding boxes using a fixed voxel size of 0.1 meters.
- **p. 27 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** The dataset contains approximately 20 million (20M) question-answer (QA) pairs, covering 31 spatial relation categories, and supports multi-step reasoning of up to 5 steps.
- **p. 27 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** These were collected by 13 robots over a period of 17 months.
- **p. 28 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** To support this, we curated 18K training samples from HM3D (Ramakrishnan et al., 2021) and MP3D (Chang et al., 2017), covering 6 and 21 object ...
- **p. 30 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** The benchmark is built based on a 3000m2 office environment containing 8 core operation scenarios and 95 object categories representative of common workplace items.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: Performance Comparison across 2D and 3D Embodied Reasoning Benchmarks. Despite recent progress, two core challenges remain. First, the geometric adaptability gap: mod- ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Designed to overcome the limitations of traditional multimodal models-which primarily operate at the image-level or bounding box-level-it incorporates regional masks linked with precise language ... | p. 26 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| body limitation/failure cue | To overcome these limitations, we introduce a 3D-aware planning framework that ingests sequential RGB-D observations and directly generates subgoals in continuous 3D coordinate space. | p. 29 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| body limitation/failure cue | Physical constraints, including object location, size, collision potential, must be considered, making this task highly relevant to the Mobile Placement (Easy) tasks. • Where2Approach: ... | p. 29 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| body limitation/failure cue | In addition, it incorporates critical physical constraints, including object dimensions, fit within the available space, and collision avoidance with other objects. | p. 32 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| body limitation/failure cue | The entire benchmark consists of 464 samples, including 200 generation tasks that require the model to output corresponding points, and 264 judgment tasks where ... | p. 32 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The ViT encoder is frozen, while the LLM backbone is updated with a reduced learning rate of 5e -7 to prioritize learning within the ... | p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS) |
| We apply cosine decay for learning rate scheduling and use exponential decay to control the Gumbelsoftmax temperature τ, defined as τinit · exp( -4.5·steps ... | p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS) |
| This method leverages a language model encoder (e.g., a lightweight Sentence Transformer) to capture the overall meaning of a prompt before categorizing it. | p. 24 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| The action or activity Walk, run, throw, placing Other Uncategorized or low-similarity prompts (sim. < 0.25) General Data 12.7% Image Rsn. | p. 26 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| The dataset contains approximately 20 million (20M) question-answer (QA) pairs, covering 31 spatial relation categories, and supports multi-step reasoning of up to 5 steps. | p. 27 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| It focus on hardware and kitchen tool objects to facilitate research in practical scenarios in which a robot manipulator needs to interact with the ... | p. 27 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Using the A* algorithm, we compute the shortest path while merging trajectory points of adjacent objects belonging to the same entity. | p. 28 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| The evaluation code is consistent with Where2Place. | p. 29 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Performance Comparison across 2D and 3D Embodied Reasoning Benchmarks. Despite recent progress, two core challenges remain. First, the geometric adaptability gap: mod- els ...
- **p. 26 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Designed to overcome the limitations of traditional multimodal models-which primarily operate at the image-level or bounding box-level-it incorporates regional masks linked with precise language descriptions ...
- **p. 29 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** To overcome these limitations, we introduce a 3D-aware planning framework that ingests sequential RGB-D observations and directly generates subgoals in continuous 3D coordinate space.
- **p. 29 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Physical constraints, including object location, size, collision potential, must be considered, making this task highly relevant to the Mobile Placement (Easy) tasks. • Where2Approach: The ...
- **p. 32 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** In addition, it incorporates critical physical constraints, including object dimensions, fit within the available space, and collision avoidance with other objects.
- **p. 32 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** The entire benchmark consists of 464 samples, including 200 generation tasks that require the model to output corresponding points, and 264 judgment tasks where the ...

- **Evidence anchors reviewed:** datasets p. 27 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 27 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 35 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 25 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), metrics p. 9 (Figure/Table caption), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 10 (Figure/Table caption), p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), baselines p. 23 (Figure/Table caption), p. 24 (C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION), p. 24 (Figure/Table caption), p. 29 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 7 (Figure/Table caption), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), results p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 36 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
