# Evaluation - LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.18651; PDF retrieval source: https://arxiv.org/pdf/2311.18651. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies), p. 6 (5.3. Ablation Studies), p. 7 (5.3. Ablation Studies), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption)): Results show that our method consistently outperforms existing methods on all the evaluation sets, and surpasses the generation based method, 3D-LLM, by a large margin (+7.39% CiDEr score on the ...

## Evaluation Body Digest

- **p. 5 / 5. Experiments - extractive body cue:** In this paper, we experiment with 3D data from ScanNet [15], a 3D dataset covering 1,201 and 312 diverse and complex indoor 3D scenes for ...
- **p. 5 / 5.2. Comparison with SoTA Specialists - extractive body cue:** We benchmarks stateof-the-art methods on the widely-used ScanRefer [6] and Nr3D [1] dataset in Tab.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** However, the generalist model achieves poor results on Nr3D [1], which is because we did not try to differentiate between Nr3D and ScanRefer during training ...
- **p. 6 / 5.3. Ablation Studies - extractive body cue:** Our proposed LL3DA surpasses previous 3D specialists on both datasets.
- **p. 6 / 5.3. Ablation Studies - extractive body cue:** For fair comparison, we list methods that are trained under the standard per-word cross-entropy loss without additional 3D scenes.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** The following three rows list the performance of the model fine-tuned on each dataset.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Describe this object in the 3D scene.
- **p. 8 / 5.4. Qualitative Results - extractive body cue:** We present several visualization results on different tasks in Fig.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.4. Qualitative Results (p. 8); B. More Evaluations (p. 15).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Comparison with SoTA Specialists | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results show that our method consistently outperforms existing methods on all the evaluation sets, and surpasses the generation based method, 3D-LLM, by a large ... | p. 5 (5.2. Comparison with SoTA Specialists) |
| 5.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results show that the additional textual instructions and visual prompts improve the task diversity and further improve the performance on 3D Question Answering. | p. 7 (5.3. Ablation Studies) |
| 5.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | The "early fusion" enables direct interaction with the 3D scene, thus it achieves a better performance. | p. 6 (5.3. Ablation Studies) |
| 5.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results show that this technique would remove the ambiguities, and further improve the quality of the answers (+6.12% C). | p. 7 (5.3. Ablation Studies) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. Overview of the Proposed Approach. (a) The overall pipeline of our proposed LL3DA first extracts interaction-aware 3D scene embeddings, which are later ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 5. Experiments - extractive body cue:** In this paper, we experiment with 3D data from ScanNet [15], a 3D dataset covering 1,201 and 312 diverse and complex indoor 3D scenes for ...
- **p. 5 / 5.2. Comparison with SoTA Specialists - extractive body cue:** We benchmarks stateof-the-art methods on the widely-used ScanRefer [6] and Nr3D [1] dataset in Tab.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** However, the generalist model achieves poor results on Nr3D [1], which is because we did not try to differentiate between Nr3D and ScanRefer during training ...
- **p. 6 / 5.3. Ablation Studies - extractive body cue:** Our proposed LL3DA surpasses previous 3D specialists on both datasets.
- **p. 6 / 5.3. Ablation Studies - extractive body cue:** For fair comparison, we list methods that are trained under the standard per-word cross-entropy loss without additional 3D scenes.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** The following three rows list the performance of the model fine-tuned on each dataset.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Describe this object in the 3D scene.
- **p. 8 / 5.4. Qualitative Results - extractive body cue:** We present several visualization results on different tasks in Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose LL3DA, a Large Language 3D Assistant that demonstrates mighty instruction-following capacities of un- derstanding, reasoning, and planning in complex 3D environments. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the Proposed Approach. (a) The overall pipeline of our proposed LL3DA first extracts interaction-aware 3D scene embeddings, which are later projected ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative Comparisons for 3D Dense Captioning on ScanRefer[6] and Nr3D[1]. For fair comparison, we list methods that are trained under the standard per-word ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative Comparisons for 3D Question Answering on ScanQA[2]. We categorize previous works into classification based ("CLS") and generation based ("GEN") methods. The results ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Different Ways of Encoding Visual Prompts. We listed two ways of encoding visual prompts, (a) adopting a unified transformer to aggregate features from ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Effectiveness of Q-Former Design on ScanRefer[6]. We design two different ways of utilizing visual prompts. The "early fusion" enables direct interaction with the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Effectiveness of Instructions as 3D Dense Captioning Auxiliary Tasks. We train the models from scratch and evaluate on ScanRefer[6]. "Aux.Loc" identifies whether we ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Evaluation as a Generalist. The first three rows list the performance of models trained from scratch as experts on each dataset. The results ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In this paper, we experiment with 3D data from ScanNet [15], a 3D dataset covering 1,201 and 312 diverse and complex indoor 3D scenes ... | embodiment, simulator version and control stack | p. 5 (5. Experiments), p. 5 (5.2. Comparison with SoTA Specialists) |
| Task/environment | We benchmarks stateof-the-art methods on the widely-used ScanRefer [6] and Nr3D [1] dataset in Tab. | reset, timeout, object/scene variation | p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3.1. Problem Formatting) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.2. Model Design), p. 4 (3.2. Model Design) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Here, m ∈{C, B-4, M, R}, and the m score of a caption is set to 0 if the IoU between the predicted box ... | definition/direction/unit from same section | p. 5 (5.2. Comparison with SoTA Specialists) |
| Table 13. 3D Dense Captioning Performance with 3D Bounding Boxes Generated by LL3DA. Though there is still gap between LL3DA and 3D specialists for ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Results show that our method consistently outperforms existing methods on all the evaluation sets, and surpasses the generation based method, 3D-LLM, by a large ... | definition/direction/unit from same section | p. 5 (5.2. Comparison with SoTA Specialists) |
| Table 11. Quantitative Comparisons on Open-Vocabulary Detection with LL3DA. We treat 3D Detection as the 3D Dense Captioning problem. We simulate the click prompt ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| The "early fusion" enables direct interaction with the 3D scene, thus it achieves a better performance. | definition/direction/unit from same section | p. 6 (5.3. Ablation Studies) |
| For fair comparison, we list methods that are trained under the standard per-word cross-entropy loss without additional 3D scenes. | definition/direction/unit from same section | p. 6 (5.3. Ablation Studies) |
| The last row lists the performance of our model as a generalist. | definition/direction/unit from same section | p. 7 (5.3. Ablation Studies) |
| This illustrates the importance of visual interaction in complex 3D environments. | definition/direction/unit from same section | p. 7 (5.3. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The baseline method directly generates the captions given the input 3D scene and visual prompts without any textual instructions. | comparison identity and matched condition | p. 7 (5.3. Ablation Studies) |
| Results show that our method consistently outperforms existing methods on all both datasets. | comparison identity and matched condition | p. 5 (5.2. Comparison with SoTA Specialists) |
| We benchmark state-of-the-art methods on the ScanQA [2] validation set as well as two test benchmarks in Tab. | comparison identity and matched condition | p. 5 (5.2. Comparison with SoTA Specialists) |
| For fair comparison, we list methods that are trained under the standard per-word cross-entropy loss without additional 3D scenes. | comparison identity and matched condition | p. 6 (5.3. Ablation Studies) |
| The listed methods are evaluated without any visual interactions for fair comparison. | comparison identity and matched condition | p. 7 (5.3. Ablation Studies) |
| Quantitative Comparisons for 3D Question Answering on ScanQA[2]. | comparison identity and matched condition | p. 6 (5.3. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 7. Effectiveness of Instructions on 3D Dense Captioning. We perform experiments on ScanRefer[6]. The baseline method directly generates the captions given the input ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| In this section, we provide ablation studies on model designs and training strategies. | component/input/data sensitivity | p. 5 (5.3. Ablation Studies) |
| 5.2), and conduct quantitative ablation studies on the model design and training strategy (Sec. | component/input/data sensitivity | p. 5 (5. Experiments) |
| For fair comparison, we list methods that are trained under the standard per-word cross-entropy loss without additional 3D scenes. | component/input/data sensitivity | p. 6 (5.3. Ablation Studies) |
| The listed methods are evaluated without any visual interactions for fair comparison. | component/input/data sensitivity | p. 7 (5.3. Ablation Studies) |
| Figure 1. We propose LL3DA, a Large Language 3D Assistant that demonstrates mighty instruction-following capacities of un- derstanding, reasoning, and planning in complex 3D ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our ... | Results show that our method consistently outperforms existing methods on all the evaluation sets, and surpasses the generation based method, 3D-LLM, by a large ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies), p. 6 (5.3. Ablation Studies), p. 7 (5.3. Ablation Studies), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Results show that the additional textual instructions and visual prompts improve the task diversity and further improve the performance on 3D Question Answering. | numeric claim only at cited anchor | p. 7 (5.3. Ablation Studies) |

- Numeric sentences retained from the body:
- **p. 4 / 3.2. Model Design - extractive body cue:** The two types of the visual prompts are then projected with separate and identical Feed Forward Networks (FFN). fclick = FFNclick (pos (pclick)) fbox = ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For all the training tasks, we train with a total batch size of 16, and evaluate our method every 4k iterations. | p. 5 (5. Experiments) |
| We adopt the AdamW [35] optimizer with a weight decay of 0.1 and a learning rate decaying from 10-4 to 10-6 with a cosine ... | p. 5 (5. Experiments) |
| We adopt the masked transformer encoder pre-trained on ScanNet detection [9] as the scene encoder, 3 | p. 3 (3.2. Model Design) |
| 2 (b), which consists of a frozen 3D scene encoder E3D, a visual prompt encoder, and a Q-Former to transform the permutation-invariant 3D embeddings ... | p. 3 (3.2. Model Design) |
| In practice, we choose to keep the scene encoder frozen to save the memory cost during training. | p. 4 (3.2. Model Design) |
| Then, we encode pclick with the 3D Fourier positional embeddings [48] function: pos (pclick) = [sin (2πpclick · B) ; cos (2πpclick · B)] ... | p. 4 (3.2. Model Design) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 5 (5. Experiments), p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies), p. 6 (5.3. Ablation Studies), p. 6 (5.3. Ablation Studies), p. 7 (5.3. Ablation Studies), metrics p. 5 (5.2. Comparison with SoTA Specialists), p. 17 (Figure/Table caption), p. 5 (5.2. Comparison with SoTA Specialists), p. 17 (Figure/Table caption), p. 6 (5.3. Ablation Studies), p. 6 (5.3. Ablation Studies), baselines p. 7 (5.3. Ablation Studies), p. 5 (5.2. Comparison with SoTA Specialists), p. 5 (5.2. Comparison with SoTA Specialists), p. 6 (5.3. Ablation Studies), p. 7 (5.3. Ablation Studies), p. 6 (5.3. Ablation Studies), results p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies), p. 6 (5.3. Ablation Studies), p. 7 (5.3. Ablation Studies), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
