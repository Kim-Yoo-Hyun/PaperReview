# Evaluation - BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7AMriz7I3K; PDF retrieval source: https://openreview.net/pdf/0723f863304fd597c9e6e38242914d49584b6776.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (3 Method), p. 9 (3 Method), p. 22 (A.2 Adaptive hierarchical feature selection), p. 27 (Figure/Table caption), p. 25 (Figure/Table caption), p. 2 (Figure/Table caption)): However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D.

## Evaluation Body Digest

- **p. 9 / 3 Method - extractive PDF cue:** However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D.
- **p. 23 / A.3 Prompting - extractive PDF cue:** System: You are a helpful robot to find an object in an unknown environment.
- **p. 9 / 3 Method - extractive PDF cue:** 4.3 Ablation study To evaluate the effectiveness of each module in our system, we conduct an ablation study on 400 randomly sampled episodes from the ...
- **p. 23 / A.3 Prompting - extractive PDF cue:** This information will be embedded with CLIP and must be useful for the robot to recognize the object. • Provide which room it is likely ...
- **p. 9 / 3 Method - extractive PDF cue:** However, omitting object-level semantics enhances efficiency (32.0), as fine-grained searches with object-level cues increase success rates but often result in slower, localized exploration, leading to ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The search process: BeliefMapNav plans frontier paths by minimizing the expected search distance based on the 3D voxel-based belief map, ensuring efficient and ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: The pipeline begins by passing the target and prompt to the LLM to generate hierarchical landmarks with relevance scores. Meanwhile, RGB and depth ...
- **p. 24 / Figure/Table caption - extractive PDF cue:** Figure 5: (a) is the input depth image. (b) shows the confidence computed from the depth image. Bluer regions indicate higher confidence, meaning the likelihood ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 3 Method | SYSTEM / EVALUATION SCOPE UNRESOLVED | However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D. | p. 9 (3 Method) |
| 3 Method | SYSTEM / EVALUATION SCOPE UNRESOLVED | Results indicate that incorporating more semantic levels generally improves SR. | p. 9 (3 Method) |
| A.2 Adaptive hierarchical feature selection | SYSTEM / EVALUATION SCOPE UNRESOLVED | For each image pixel p at hierarchical spatial level ls, we select the CLIP feature from all candidate patches across scales that achieves the ... | p. 22 (A.2 Adaptive hierarchical feature selection) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 9: Visualization of the search process. The color of each point in the image represents the belief of object presence: redder points indicate ... | p. 27 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 6: Error analysis of the algorithm for parameter tuning. All the results are based on 10 frontiers, over 50 different scenes, and each ... | p. 25 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / 3 Method - extractive PDF cue:** However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D.
- **p. 23 / A.3 Prompting - extractive PDF cue:** System: You are a helpful robot to find an object in an unknown environment.
- **p. 9 / 3 Method - extractive PDF cue:** 4.3 Ablation study To evaluate the effectiveness of each module in our system, we conduct an ablation study on 400 randomly sampled episodes from the ...
- **p. 23 / A.3 Prompting - extractive PDF cue:** This information will be embedded with CLIP and must be useful for the robot to recognize the object. • Provide which room it is likely ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The search process: BeliefMapNav plans frontier paths by minimizing the expected search distance based on the 3D voxel-based belief map, ensuring efficient and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: BeliefMapNav pipeline: The agent initializes with a 360° rotation. During exploration, the 3D voxel-based belief mapping module fuses sensor input, the 3D hierarchical ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: The pipeline begins by passing the target and prompt to the LLM to generate hierarchical landmarks with relevance scores. Meanwhile, RGB and depth ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Zero-shot object navigation results on MP3D, HM3D and HSSD. We compare the SR and SPL of state-of-the-art methods in different settings.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Impact of the planner and visibility map.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Impact of vision-language encoders. Encoder SR↑ SPL↑ BLIP [49] 59.3 31.0 BLIP2 [50]
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: Impact of different levels of landmarks. Landmarks SR↑ SPL↑ w/o 60.0 30.9 Room
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 5: Impact of different semantic levels. Semantics SR↑ SPL↑ Random Walking 21.5 10.8 Scene

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D. | embodiment, simulator version and control stack | p. 9 (3 Method), p. 23 (A.3 Prompting) |
| Task/environment | System: You are a helpful robot to find an object in an unknown environment. | reset, timeout, object/scene variation | p. 23 (A.3 Prompting), p. 9 (3 Method) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3 Method), p. 4 (3 Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 6 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, omitting object-level semantics enhances efficiency (32.0), as fine-grained searches with object-level cues increase success rates but often result in slower, localized exploration, leading ... | definition/direction/unit from same section | p. 9 (3 Method) |
| Figure 1: The search process: BeliefMapNav plans frontier paths by minimizing the expected search distance based on the 3D voxel-based belief map, ensuring efficient ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 3: The pipeline begins by passing the target and prompt to the LLM to generate hierarchical landmarks with relevance scores. Meanwhile, RGB and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 5: (a) is the input depth image. (b) shows the confidence computed from the depth image. Bluer regions indicate higher confidence, meaning the ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 9: Visualization of the search process. The color of each point in the image represents the belief of object presence: redder points indicate ... | definition/direction/unit from same section | p. 27 (Figure/Table caption) |
| Without the Visibility Map, relying on spatial priors alone leads to a 5.3% ↓drop in SR and 3.6 ↓in SPL, as the agent revisits ... | definition/direction/unit from same section | p. 9 (3 Method) |
| For each semantic level, we keep only the feature with the highest confidence score in each voxel. | definition/direction/unit from same section | p. 22 (A.2 Adaptive hierarchical feature selection) |
| If a feature already exists, we compare the new score with the stored score and retain the feature with the higher confidence. | definition/direction/unit from same section | p. 22 (A.2 Adaptive hierarchical feature selection) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 8: The proportion of different causes of failure in the HM3D dataset. A.6 Baselines We evaluate our approach in comparison with a range ... | comparison identity and matched condition | p. 26 (Figure/Table caption) |
| Table 1: Zero-shot object navigation results on MP3D, HM3D and HSSD. We compare the SR and SPL of state-of-the-art methods in different settings. | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Prior work [51] similarly shows that BLIP-2 slightly surpasses CLIP in zero-shot text-to-image retrieval accuracy, while both are significantly better than BLIP. | comparison identity and matched condition | p. 9 (3 Method) |
| The ablation study of the effectiveness of LLMs and image scale k are in Appendix A.8. | comparison identity and matched condition | p. 9 (3 Method) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The ablation study of the effectiveness of LLMs and image scale k are in Appendix A.8. | component/input/data sensitivity | p. 9 (3 Method) |
| Effectiveness of hierarchical landmarks: As shown in Table 4, without landmarks, we retrieve directly using the object name in the hierarchical 3D semantic map. | component/input/data sensitivity | p. 9 (3 Method) |
| Figure 9: Visualization of the search process. The color of each point in the image represents the belief of object presence: redder points indicate ... | component/input/data sensitivity | p. 27 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of our method are mainly summarized as follows: 1) We propose BeliefMapNav, an efficient zero-shot object navigation system that accurately predicts target ... | However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (3 Method), p. 9 (3 Method), p. 22 (A.2 Adaptive hierarchical feature selection), p. 27 (Figure/Table caption), p. 25 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Primary metric/result | Results indicate that incorporating more semantic levels generally improves SR. | numeric claim only at cited anchor | p. 9 (3 Method) |

- Numeric sentences retained from the body:
- **p. 9 / 3 Method - extractive PDF cue:** Semantics SR↑ SPL↑ Random Walking 21.5 10.8 Scene 59.0 30.4 Scene + Region 61.5 32.0 Scene + Region + Object 62.5 31.6 Effectiveness of different ...
- **p. 3 / 3 Method - extractive PDF cue:** 3.1 Task definition We define the ZSON task, where an agent is required to locate a specified target object in an unknown environment without task-specific ...
- **p. 3 / 3 Method - extractive PDF cue:** The task is successful if the agent issues a STOP within 0.1 m of the target object within 500 steps.
- **p. 7 / 3 Method - extractive PDF cue:** HM3D, the official dataset of the Habitat 2022 ObjectNav Challenge, includes 2,000 validation episodes across 20 environments and 6 object categories.
- **p. 7 / 3 Method - extractive PDF cue:** We conduct experiments on its validation set, consisting of 11 environments, 21 object categories, and 2,195 object-goal navigation episodes.
- **p. 7 / 3 Method - extractive PDF cue:** HSSD, a synthetic dataset with scenes based on real house layouts, contains 40 validation scenes, 1,248 navigation episodes, and 6 object categories.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Across all datasets, the performance limitations of the local planner in [7] lead to significant degradation, especially in narrow areas. | p. 9 (3 Method) |
| body limitation/failure cue | Second, there are a lot of mesh "holes" in MP3D, which allow the agent to see through obstacles, causing it to mistakenly prioritize these ... | p. 9 (3 Method) |
| body limitation/failure cue | Figure 8: The proportion of different causes of failure in the HM3D dataset. A.6 Baselines We evaluate our approach in comparison with a range ... | p. 26 (Figure/Table caption) |
| body limitation/failure cue | For each semantic level, if the voxel does not contain an existing feature, we directly store the current feature and its associated confidence score. | p. 22 (A.2 Adaptive hierarchical feature selection) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation details: We limit navigation to 500 steps, defining success as stopping within 0.1 m of the target. | p. 8 (3 Method) |
| However, CLIP demonstrates stronger generalization to out-of-distribution data and supports efficient inference via independent encoders and pre-computed features. | p. 9 (3 Method) |
| The task is successful if the agent issues a STOP within 0.1 m of the target object within 500 steps. | p. 3 (3 Method) |
| It involves three steps as shown in Fig. | p. 4 (3 Method) |
| The frontier observation belief estimation module computes frontier observation belief from the belief, frontiers, and visibility maps via FOV-based aggregation. | p. 4 (3 Method) |
| We back-project depth values of patches into 3D space to form a point cloud and compute two geometric properties: the volume V k h,w ... | p. 5 (3 Method) |
| Finally, landmarks encoded by text CLIP and the semantic map are combined via the belief map construction to update the 3D voxel-based belief map. ... | p. 5 (3 Method) |
| The final belief score at voxel u is computed as: bu = P lt∈Lt Pnlt i=1 αlt i ·plt u,i +pu,target. | p. 6 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 3 Method - extractive PDF cue:** Across all datasets, the performance limitations of the local planner in [7] lead to significant degradation, especially in narrow areas.
- **p. 9 / 3 Method - extractive PDF cue:** Second, there are a lot of mesh "holes" in MP3D, which allow the agent to see through obstacles, causing it to mistakenly prioritize these holes ...
- **p. 26 / Figure/Table caption - extractive PDF cue:** Figure 8: The proportion of different causes of failure in the HM3D dataset. A.6 Baselines We evaluate our approach in comparison with a range of ...
- **p. 22 / A.2 Adaptive hierarchical feature selection - extractive PDF cue:** For each semantic level, if the voxel does not contain an existing feature, we directly store the current feature and its associated confidence score.

- **PDF anchors reviewed:** datasets p. 9 (3 Method), p. 23 (A.3 Prompting), p. 9 (3 Method), p. 23 (A.3 Prompting), metrics p. 9 (3 Method), p. 2 (Figure/Table caption), p. 5 (Figure/Table caption), p. 24 (Figure/Table caption), p. 27 (Figure/Table caption), p. 9 (3 Method), baselines p. 26 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (3 Method), p. 9 (3 Method), results p. 9 (3 Method), p. 9 (3 Method), p. 22 (A.2 Adaptive hierarchical feature selection), p. 27 (Figure/Table caption), p. 25 (Figure/Table caption), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
