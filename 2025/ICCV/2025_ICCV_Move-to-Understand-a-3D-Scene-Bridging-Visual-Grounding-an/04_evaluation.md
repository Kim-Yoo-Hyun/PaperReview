# Evaluation - Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Quantitative Results), p. 6 (Figure/Table caption), p. 7 (4.3. Discussions), p. 7 (4.3. Discussions), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption)): While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and HM3D-OVON, highlighting SG3D's inherent difficulty in requiring both ...

## Evaluation Body Digest

- **p. 6 / 4.2. Quantitative Results - extractive body cue:** Unlike other benchmarks, SG3D emphasizes task consistency across multiple steps, making it more complex.
- **p. 6 / 4.2. Quantitative Results - extractive body cue:** Notably, MTU3D achieves the highest SR in Val Unseen (40.8%), showcasing its strong generalization ability to unseen episodes.
- **p. 7 / 4.3. Discussions - extractive body cue:** Model speed and parameter metrics, results are average from 5 runs across multiple frames and episodes on 3090 Ti.
- **p. 7 / 4.3. Discussions - extractive body cue:** 4a show that VisionLanguage Exploration (VLE) Pre-training significantly improves navigation performance, as indicated by the SR across all datasets.
- **p. 8 / 4.4. Qualitative results - extractive body cue:** OVON GOAT SG3D Dataset 15 20 25 30 35 40 SR (%) 27.8 22.2 22.9 33.3 36.1 27.9 VLE w/o vle w/ vle (a) Effect ...
- **p. 8 / 4.4. Qualitative results - extractive body cue:** Object Description Image Goal Type 10 20 30 40 50 60 70 80 SR (%) 10.5 28.6 26.7 52.6 71.4 60.0 Memory w/o mem w ...
- **p. 6 / 4.2. Quantitative Results - extractive body cue:** While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and HM3D-OVON, highlighting SG3D's ...
- **p. 6 / 4.1. Experimental setting - extractive body cue:** Common metrics include Success Rate (SR = Nsuccess Ntotal ) and Success weighted by Path Length (SPL = 1 Ntotal PNtotal i=1 Si · li ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Experimental setting (p. 6); 4.2. Quantitative Results (p. 6); 4.4. Qualitative results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and HM3D-OVON, highlighting ... | p. 6 (4.2. Quantitative Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4. Sequential task navigation results on SG3D-Nav [87]. Multi-modal Lifelong Navigation. The results in Tab. 5 highlight the significant performance improvement of our ... | p. 6 (Figure/Table caption) |
| 4.3. Discussions | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4a show that VisionLanguage Exploration (VLE) Pre-training significantly improves navigation performance, as indicated by the SR across all datasets. | p. 7 (4.3. Discussions) |
| 4.3. Discussions | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4b show that memory significantly improves SR across all goal types. | p. 7 (4.3. Discussions) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1. Comparison of different paradigms. MTU3D uniquely integrates advantages from both sides, supporting online explo- ration and lifelong visual grounding. time decision-making. Specifically, ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Quantitative Results - extractive body cue:** Unlike other benchmarks, SG3D emphasizes task consistency across multiple steps, making it more complex.
- **p. 6 / 4.2. Quantitative Results - extractive body cue:** Notably, MTU3D achieves the highest SR in Val Unseen (40.8%), showcasing its strong generalization ability to unseen episodes.
- **p. 7 / 4.3. Discussions - extractive body cue:** Model speed and parameter metrics, results are average from 5 runs across multiple frames and episodes on 3090 Ti.
- **p. 7 / 4.3. Discussions - extractive body cue:** 4a show that VisionLanguage Exploration (VLE) Pre-training significantly improves navigation performance, as indicated by the SR across all datasets.
- **p. 8 / 4.4. Qualitative results - extractive body cue:** OVON GOAT SG3D Dataset 15 20 25 30 35 40 SR (%) 27.8 22.2 22.9 33.3 36.1 27.9 VLE w/o vle w/ vle (a) Effect ...
- **p. 8 / 4.4. Qualitative results - extractive body cue:** Object Description Image Goal Type 10 20 30 40 50 60 70 80 SR (%) 10.5 28.6 26.7 52.6 71.4 60.0 Memory w/o mem w ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. MTU3D is a versatile embodied navigation model capable of processing diverse inputs, including object categories, image snapshots, natural language descriptions, task plan sequences, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Our approach bridges online exploration with dynami- cally spatial memory updates for lifelong grounding. ries presents significant challenges, and methods for effec- tively ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Comparison of different paradigms. MTU3D uniquely integrates advantages from both sides, supporting online explo- ration and lifelong visual grounding. time decision-making. Specifically, MTU3D ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Our proposed model processes RGB-D sequences to generate object queries, which are stored in a memory bank. The spatial reasoning layer then selects ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Data source statistic for Vision-Language-Exploration Pre-training. Sim denotes simulation, VG denotes visual ground- ing, Exp denotes exploration, Traj denotes trajectory, Dec denotes decision ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Open-vocab navigation results on HM3D-OVON [79]. Task-oriented Sequential Navigation. Tab. 4 presents re- sults on task-oriented sequential navigation, a challenging task requiring an ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Sequential task navigation results on SG3D-Nav [87]. Multi-modal Lifelong Navigation. The results in Tab. 5 highlight the significant performance improvement of our MTU3D ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Multi-modal lifelong navigation results on GOAT-Bench [37]. a crucial factor in lifelong navigation. Overall, these re- sults emphasize that lifelong spatial memory is ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Unlike other benchmarks, SG3D emphasizes task consistency across multiple steps, making it more complex. | embodiment, simulator version and control stack | p. 6 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results) |
| Task/environment | Notably, MTU3D achieves the highest SR in Val Unseen (40.8%), showcasing its strong generalization ability to unseen episodes. | reset, timeout, object/scene variation | p. 6 (4.2. Quantitative Results), p. 7 (4.3. Discussions) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (3.4. Vision-Language-Exploration Training), p. 3 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and HM3D-OVON, highlighting ... | definition/direction/unit from same section | p. 6 (4.2. Quantitative Results) |
| Common metrics include Success Rate (SR = Nsuccess Ntotal ) and Success weighted by Path Length (SPL = 1 Ntotal PNtotal i=1 Si · ... | definition/direction/unit from same section | p. 6 (4.1. Experimental setting) |
| Furthermore, GPT4o with MTU3D achieves even better performance, reaching 51.1% LLM-SR and 42.6% LLM-SPL. | definition/direction/unit from same section | p. 7 (4.2. Quantitative Results) |
| 4c demonstrate that MTU surpasses frontier exploration in both SR and SPL as exploration steps increase. | definition/direction/unit from same section | p. 7 (4.3. Discussions) |
| 0 1 2 3 4 5 6 7 8 Explore Step 30 35 40 45 50 SR (%) MTU Frontier 0 1 2 3 ... | definition/direction/unit from same section | p. 8 (4.4. Qualitative results) |
| Table 1. Comparison of different paradigms. MTU3D uniquely integrates advantages from both sides, supporting online explo- ration and lifelong visual grounding. time decision-making. Specifically, ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Ablation studies showing (a) the impact of vision-language-exploration pretraining, (b) exploration efficiency on seen environments, and (c) the contribution of spatial memory to navigation ... | definition/direction/unit from same section | p. 8 (4.4. Qualitative results) |
| Figure 3. Our proposed model processes RGB-D sequences to generate object queries, which are stored in a memory bank. The spatial reasoning layer then ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 3 demonstrate that our proposed MTU3D significantly outperforms all baselines in terms of SR across both Val Seen and Val Unseen settings. | comparison identity and matched condition | p. 6 (4.2. Quantitative Results) |
| 6 demonstrate that our MTU3D-enhanced GPT-4V significantly outperforms the baseline GPT-4V model, achieving 44.2% LLM-SR vs. | comparison identity and matched condition | p. 7 (4.2. Quantitative Results) |
| 5 highlight the significant performance improvement of our MTU3D over baseline methods in lifelong setting. | comparison identity and matched condition | p. 6 (4.2. Quantitative Results) |
| This indicates that our approach enables a more efficient trajectory, avoiding the exhaustive search across all locations that baseline models rely on. | comparison identity and matched condition | p. 7 (4.2. Quantitative Results) |
| Table 1. Comparison of different paradigms. MTU3D uniquely integrates advantages from both sides, supporting online explo- ration and lifelong visual grounding. time decision-making. Specifically, ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Figure 1. MTU3D is a versatile embodied navigation model capable of processing diverse inputs, including object categories, image snapshots, natural language descriptions, task plan ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation studies showing (a) the impact of vision-language-exploration pretraining, (b) exploration efficiency on seen environments, and (c) the contribution of spatial memory to navigation ... | component/input/data sensitivity | p. 8 (4.4. Qualitative results) |
| OVON GOAT SG3D Dataset 15 20 25 30 35 40 SR (%) 27.8 22.2 22.9 33.3 36.1 27.9 VLE w/o vle w/ vle (a) ... | component/input/data sensitivity | p. 8 (4.4. Qualitative results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • ... | While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and HM3D-OVON, highlighting ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Quantitative Results), p. 6 (Figure/Table caption), p. 7 (4.3. Discussions), p. 7 (4.3. Discussions), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Primary metric/result | Table 4. Sequential task navigation results on SG3D-Nav [87]. Multi-modal Lifelong Navigation. The results in Tab. 5 highlight the significant performance improvement of our ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental setting - extractive body cue:** In Stage 1, we train for 50 epochs using AdamW (learning rate 1e-4, β1 = 0.9, β2 = 0.98) with loss weights λb = 1.0, ...
- **p. 6 / 4.1. Experimental setting - extractive body cue:** Stages 2 and 3 use identical optimizer settings for 10 epochs each.
- **p. 6 / 4.1. Experimental setting - extractive body cue:** All training runs on four NVIDIA A100 GPUs around 164 GPU hours.
- **p. 6 / 4.1. Experimental setting - extractive body cue:** For simulation evaluation, we follow [37, 79, 87] using Stretch embodiment (1.41m tall, 17cm base radius), processing 360×640 RGB images It, depth maps Dt, and ...
- **p. 6 / 4.1. Experimental setting - extractive body cue:** We subsample 18 frames along the trajectory between consecutive target positions.For A-EQA [51], our model is used solely to generate the exploration trajectory and collect ...
- **p. 7 / 4.3. Discussions - extractive body cue:** 7 shows that our model achieves efficient query proposal (192 ms) and fast reasoning (31 ms) while maintaining a competitive FPS (3.4) with 266M parameters.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In Stage 1, we train for 50 epochs using AdamW (learning rate 1e-4, β1 = 0.9, β2 = 0.98) with loss weights λb = ... | p. 6 (4.1. Experimental setting) |
| All training runs on four NVIDIA A100 GPUs around 164 GPU hours. | p. 6 (4.1. Experimental setting) |
| 4c demonstrate that MTU surpasses frontier exploration in both SR and SPL as exploration steps increase. | p. 7 (4.3. Discussions) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not stated or recoverable in the selected PDF body

- **Evidence anchors reviewed:** datasets p. 6 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results), p. 7 (4.3. Discussions), p. 7 (4.3. Discussions), p. 8 (4.4. Qualitative results), p. 8 (4.4. Qualitative results), metrics p. 6 (4.2. Quantitative Results), p. 6 (4.1. Experimental setting), p. 7 (4.2. Quantitative Results), p. 7 (4.3. Discussions), p. 8 (4.4. Qualitative results), p. 3 (Figure/Table caption), baselines p. 6 (4.2. Quantitative Results), p. 7 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results), p. 7 (4.2. Quantitative Results), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption), results p. 6 (4.2. Quantitative Results), p. 6 (Figure/Table caption), p. 7 (4.3. Discussions), p. 7 (4.3. Discussions), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 4. Sequential task navigation results on SG3D-Nav [87]. Multi-modal Lifelong Navigation. The results in Tab. 5 highlight the significant performance improvement of our MTU3D over baseline methods in lifelong ... (p. 6, Figure/Table caption).
- **Metric evidence:** Furthermore, GPT4o with MTU3D achieves even better performance, reaching 51.1% LLM-SR and 42.6% LLM-SPL. (p. 7, 4.2. Quantitative Results).
- **Baseline/ablation evidence:** 3 demonstrate that our proposed MTU3D significantly outperforms all baselines in terms of SR across both Val Seen and Val Unseen settings. (p. 6, 4.2. Quantitative Results).
- **Failure/negative evidence:** In contrast, reinforcement learning (RL)-based embodied agents can explore environments but often struggle with sample inefficiency [71], poor generalization due to limited training data [20, 57, 62] and the lack ... (p. 2, 1. Introduction).
