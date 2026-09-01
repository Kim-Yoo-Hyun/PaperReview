# Evaluation - Scene-LLM: Extending Language Model for 3D Visual Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation)): Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state updates. 3D egocentric representation outperforms ...

## Evaluation Body Digest

- **p. 5 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** This benchmark tests a model's ability to understand 3D scenes using questionanswering tasks using ScanNet dataset [14].
- **p. 5 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** To evaluate Scene-LLM in tasks related to 3D scene reasoning and planning, we utilized three primary datasets for benchmarking.
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** Responses for the top 3 non-interactive scenes are generated without task-specific finetuning, and those for the bottom interactive scene are generated with finetuning.
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** Our evaluation of Scene-LLM on 3D visual question answering (3D-VQA) benchmarks is summarized in Table 1 for ScanQA and Table 2 for SQA3D, comparing it ...
- **p. 7 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** Performance on ScanQA benchmark validation set.
- **p. 7 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** Scene-LLM performs the best among most metrics.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state updates. ...
- **p. 5 / 5. Experiments - extractive PDF cue:** In this section, we detail our benchmark results and provide examples to illustrate Scene-LLM's capabilities in 3D visual understanding and reasoning.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Results and Benchmark Evaluation (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3. Result on Alfred dataset on test unseen/seen set and valid unseen/seen set. The metrics reported include success rate (SR), goal-conditioned success rate(GC), ... | p. 7 (Figure/Table caption) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The inference setup, more results and analysis are detailed in the supplementary material. | p. 5 (5. Experiments) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In this section, we detail our benchmark results and provide examples to illustrate Scene-LLM's capabilities in 3D visual understanding and reasoning. | p. 5 (5. Experiments) |
| 5.1. Results and Benchmark Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5.1.2 Performance on 3D-VQA benchmarks. | p. 6 (5.1. Results and Benchmark Evaluation) |

## Dataset / Benchmark Role

- **p. 5 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** This benchmark tests a model's ability to understand 3D scenes using questionanswering tasks using ScanNet dataset [14].
- **p. 5 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** To evaluate Scene-LLM in tasks related to 3D scene reasoning and planning, we utilized three primary datasets for benchmarking.
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** Responses for the top 3 non-interactive scenes are generated without task-specific finetuning, and those for the bottom interactive scene are generated with finetuning.
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** Our evaluation of Scene-LLM on 3D visual question answering (3D-VQA) benchmarks is summarized in Table 1 for ScanQA and Table 2 for SQA3D, comparing it ...
- **p. 7 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** Performance on ScanQA benchmark validation set.
- **p. 7 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** Scene-LLM performs the best among most metrics.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. An interactive 3D indoor scene example from an example iThor [1] scene. Scene-LLM is a 3D-visual-language model that can process both ego-centric and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of the data generation process and Scene-LLM's architecture. The data generation comprises two stages: a 3D frame-language generation stage, which uses image ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Examples using Scene-LLM for non-interactive and interactive tasks. On the right of the static scenes are visualization of input scene features. Bold texts ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Performance on ScanQA benchmark validation set. Met- ric reported include Exact Match (EM), BLEU (B), ROUGE-L (R-L), METEOR (M), and CIDEr (C). The ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Exact Match Metric on SQA3D test set. Metric is re- ported under 6 for different question types. The ‘*' symbol indi- cates task-specific ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Result on Alfred dataset on test unseen/seen set and valid unseen/seen set. The metrics reported include success rate (SR), goal-conditioned success rate(GC), and ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation Studies comparing different input modalities, 3D representation, pertaining strategy, and data augmentation on ScanQA and SQA3D benchmarks. #Param reports the number of ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state updates. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This benchmark tests a model's ability to understand 3D scenes using questionanswering tasks using ScanNet dataset [14]. | embodiment, simulator version and control stack | p. 5 (5.1. Results and Benchmark Evaluation), p. 5 (5.1. Results and Benchmark Evaluation) |
| Task/environment | To evaluate Scene-LLM in tasks related to 3D scene reasoning and planning, we utilized three primary datasets for benchmarking. | reset, timeout, object/scene variation | p. 5 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (4.3. Inference), p. 5 (4.3. Inference) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 7 (C VoteNet+MCAN [78]), p. 4 (3.1. Frame Data Generation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 3. Result on Alfred dataset on test unseen/seen set and valid unseen/seen set. The metrics reported include success rate (SR), goal-conditioned success rate(GC), ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| In this section, we detail our benchmark results and provide examples to illustrate Scene-LLM's capabilities in 3D visual understanding and reasoning. | definition/direction/unit from same section | p. 5 (5. Experiments) |
| We conducted ablation studies by replacing visual representation and extractor with those from other methods to demonstrate the effectiveness of our 3D visual representation, ... | definition/direction/unit from same section | p. 5 (5. Experiments) |
| 5.1.2 Performance on 3D-VQA benchmarks. | definition/direction/unit from same section | p. 6 (5.1. Results and Benchmark Evaluation) |
| Responses for the top 3 non-interactive scenes are generated without task-specific finetuning, and those for the bottom interactive scene are generated with finetuning. | definition/direction/unit from same section | p. 6 (5.1. Results and Benchmark Evaluation) |
| Performance on ScanQA benchmark validation set. | definition/direction/unit from same section | p. 7 (5.1. Results and Benchmark Evaluation) |
| Figure 2. Overview of the data generation process and Scene-LLM's architecture. The data generation comprises two stages: a 3D frame-language generation stage, which uses ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our evaluation of Scene-LLM on 3D visual question answering (3D-VQA) benchmarks is summarized in Table 1 for ScanQA and Table 2 for SQA3D, comparing ... | comparison identity and matched condition | p. 6 (5.1. Results and Benchmark Evaluation) |
| Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| We conducted ablation studies by replacing visual representation and extractor with those from other methods to demonstrate the effectiveness of our 3D visual representation, ... | comparison identity and matched condition | p. 5 (5. Experiments) |
| We present results both with and without task-specific finetuning for a comprehensive anal2200 | comparison identity and matched condition | p. 6 (5.1. Results and Benchmark Evaluation) |
| Table 4. Ablation Studies comparing different input modalities, 3D representation, pertaining strategy, and data augmentation on ScanQA and SQA3D benchmarks. #Param reports the number ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conducted ablation studies by replacing visual representation and extractor with those from other methods to demonstrate the effectiveness of our 3D visual representation, ... | component/input/data sensitivity | p. 5 (5. Experiments) |
| We present results both with and without task-specific finetuning for a comprehensive anal2200 | component/input/data sensitivity | p. 6 (5.1. Results and Benchmark Evaluation) |
| Responses for the top 3 non-interactive scenes are generated without task-specific finetuning, and those for the bottom interactive scene are generated with finetuning. | component/input/data sensitivity | p. 6 (5.1. Results and Benchmark Evaluation) |
| Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 4. Ablation Studies comparing different input modalities, 3D representation, pertaining strategy, and data augmentation on ScanQA and SQA3D benchmarks. #Param reports the number ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| The ‘*' symbol indicates task-specific fine-tuning. | component/input/data sensitivity | p. 7 (5.1. Results and Benchmark Evaluation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on ... | Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation) |
| Primary metric/result | Table 3. Result on Alfred dataset on test unseen/seen set and valid unseen/seen set. The metrics reported include success rate (SR), goal-conditioned success rate(GC), ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / C VoteNet+MCAN [78] - extractive PDF cue:** 17.3 28.0 16.7 10.8 6.2 11.4 29.8 54.7 ScanRefer+MCAN [78] 18.6 26.9 16.6 11.6 7.9 11.5 30 55.4 ScanQA [7] 21.0 30.2 20.4 15.1 10.1 ...
- **p. 7 / C VoteNet+MCAN [78] - extractive PDF cue:** What Is How Can Which Other GPT-3 39.7 46.0 40.5 45.6 36.1 38.4 41.0 ClipBERT [33] 30.2 60.1 38.7 63.3 42.5 42.7 43.3 SQA3D [42] ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, lacking geometry feature, and language hallucinations. | p. 8 (6. Conclusion) |
| body limitation/failure cue | A: To enhance safety, consider laying down anti-slip mats by the sink and in any zones where spills are likely to happen. | p. 6 (5.1. Results and Benchmark Evaluation) |
| body limitation/failure cue | While Q-Former is a robust downsampling technique, it exhibits slightly lower performance compared to direct spatial down-sampling in our benchmarks, aligning with findings from ... | p. 8 (5.2. Ablation Studies and Discussions) |
| body limitation/failure cue | It measures the ability to create precise and robust plans from a high-level goal in 3D interactive environments from iTHOR [1]. | p. 6 (5.1. Results and Benchmark Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3D visual information is important for a wide range of tasks in indoor scenes, encompassing both egocentric tasks such as object interaction [29] and ... | p. 1 (1. Introduction) |
| For egocentric information representation, previous works have employed images [15], or agent coordinates [42] necessitating multiple modality encoders. | p. 2 (1. Introduction) |
| Lastly, A visibility map V ∈{0, 1}X×Y ×Z is computed, indicating the presence(1) or absence(0) of points in each voxel. | p. 5 (4.1. 3D Visual Feature) |
| The instruction is composed of the current frame description, task description, completed steps, and the "Next-step:" identifier, with bold parts being updated per timestep. | p. 5 (4.3. Inference) |
| We finetune Scene-LLM with only 2k steps to align its output with Alfred's highlevel command format. | p. 7 (C VoteNet+MCAN [78]) |
| These features are reduced to three dimensions via Principal Component Analysis (PCA) and color-coded based on their PCA components for clarity. | p. 7 (C VoteNet+MCAN [78]) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive PDF cue:** Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, lacking geometry feature, and language hallucinations.
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** A: To enhance safety, consider laying down anti-slip mats by the sink and in any zones where spills are likely to happen.
- **p. 8 / 5.2. Ablation Studies and Discussions - extractive PDF cue:** While Q-Former is a robust downsampling technique, it exhibits slightly lower performance compared to direct spatial down-sampling in our benchmarks, aligning with findings from [38].
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** It measures the ability to create precise and robust plans from a high-level goal in 3D interactive environments from iTHOR [1].

- **PDF anchors reviewed:** datasets p. 5 (5.1. Results and Benchmark Evaluation), p. 5 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation), p. 7 (5.1. Results and Benchmark Evaluation), p. 7 (5.1. Results and Benchmark Evaluation), metrics p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation), baselines p. 6 (5.1. Results and Benchmark Evaluation), p. 8 (Figure/Table caption), p. 5 (5. Experiments), p. 6 (5.1. Results and Benchmark Evaluation), p. 8 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
