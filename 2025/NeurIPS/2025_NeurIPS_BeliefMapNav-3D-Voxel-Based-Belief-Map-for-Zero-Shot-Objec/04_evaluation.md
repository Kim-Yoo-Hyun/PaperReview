# Evaluation - BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7AMriz7I3K; PDF retrieval source: https://arxiv.org/pdf/2506.06487.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method), p. 14 (A.2 Adaptive hierarchical feature selection), p. 7 (3 Method)): On the HM3D dataset, our method improves SPL by 46.4% compared to the zero-shot method InstructNav [9], which achieves the highest SR.

## Evaluation Body Digest

- **p. 7 / 3 Method - extractive body cue:** HSSD, a synthetic dataset with scenes based on real house layouts, contains 40 validation scenes, 1,248 navigation episodes, and 6 object categories.
- **p. 7 / 3 Method - extractive body cue:** HM3D, the official dataset of the Habitat 2022 ObjectNav Challenge, includes 2,000 validation episodes across 20 environments and 6 object categories.
- **p. 8 / 3 Method - extractive body cue:** However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D.
- **p. 15 / A.3 Prompting - extractive body cue:** System: You are a helpful robot to find an object in an unknown environment.
- **p. 8 / 3 Method - extractive body cue:** 4.3 Ablative study To evaluate the effectiveness of each module in our system, we conduct an ablation study on 400 randomly sampled episodes from the ...
- **p. 15 / A.3 Prompting - extractive body cue:** This information will be embedded with CLIP and must be useful for the robot to recognize the object. • Provide which room it is likely ...
- **p. 9 / 3 Method - extractive body cue:** However, this improvement is less significant than the gain from incorporating spatial semantics at different hierarchical levels in Table 5, as object names already show ...
- **p. 9 / 3 Method - extractive body cue:** Semantics SR↑ SPL↑ Random Walking 21.5 10.8 Scene 59.0 30.4 Scene + Region 61.5 32.0 Scene + Region + Object 62.5 31.6 Effectiveness of different ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3 Method | SYSTEM / EVALUATION SCOPE UNRESOLVED | On the HM3D dataset, our method improves SPL by 46.4% compared to the zero-shot method InstructNav [9], which achieves the highest SR. | p. 8 (3 Method) |
| 3 Method | SYSTEM / EVALUATION SCOPE UNRESOLVED | However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D. | p. 8 (3 Method) |
| 3 Method | SYSTEM / EVALUATION SCOPE UNRESOLVED | Results indicate that incorporating more semantic levels generally improves SR. | p. 9 (3 Method) |
| 3 Method | SYSTEM / EVALUATION SCOPE UNRESOLVED | Semantics SR↑ SPL↑ Random Walking 21.5 10.8 Scene 59.0 30.4 Scene + Region 61.5 32.0 Scene + Region + Object 62.5 31.6 Effectiveness of ... | p. 9 (3 Method) |
| A.2 Adaptive hierarchical feature selection | SYSTEM / EVALUATION SCOPE UNRESOLVED | For each image pixel p at hierarchical spatial level ls, we select the CLIP feature from all candidate patches across scales that achieves the ... | p. 14 (A.2 Adaptive hierarchical feature selection) |

## Dataset / Benchmark Role

- **p. 7 / 3 Method - extractive body cue:** HSSD, a synthetic dataset with scenes based on real house layouts, contains 40 validation scenes, 1,248 navigation episodes, and 6 object categories.
- **p. 7 / 3 Method - extractive body cue:** HM3D, the official dataset of the Habitat 2022 ObjectNav Challenge, includes 2,000 validation episodes across 20 environments and 6 object categories.
- **p. 8 / 3 Method - extractive body cue:** However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D.
- **p. 15 / A.3 Prompting - extractive body cue:** System: You are a helpful robot to find an object in an unknown environment.
- **p. 8 / 3 Method - extractive body cue:** 4.3 Ablative study To evaluate the effectiveness of each module in our system, we conduct an ablation study on 400 randomly sampled episodes from the ...
- **p. 15 / A.3 Prompting - extractive body cue:** This information will be embedded with CLIP and must be useful for the robot to recognize the object. • Provide which room it is likely ...
- **p. 9 / 3 Method - extractive body cue:** However, this improvement is less significant than the gain from incorporating spatial semantics at different hierarchical levels in Table 5, as object names already show ...
- **p. 9 / 3 Method - extractive body cue:** Semantics SR↑ SPL↑ Random Walking 21.5 10.8 Scene 59.0 30.4 Scene + Region 61.5 32.0 Scene + Region + Object 62.5 31.6 Effectiveness of different ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The search process: BeliefMapNav plans frontier paths by minimizing the expected search distance based on the 3D voxel-based belief map, ensuring efficient and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: BeliefMapNav pipeline: The agent initializes with a 360° rotation. During exploration, the 3D voxel-based belief mapping module fuses sensor input, the 3D hierarchical ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: The pipeline begins by passing the target and prompt to the LLM to generate hierarchical landmarks with relevance scores. Meanwhile, RGB and depth ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: BeliefMapNav can outperform previous SOTAs on both HM3D and MP3D benchmark.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Impact of the planner and visibility map.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Impact of vision-language encoders. Encoder SR↑ SPL↑ Blip [46] 59.3 31.0 Blip2 [47]
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of the prior belief map, visibility map, and the posterior belief map, with an enlarged section highlighting the target object. Effectiveness of ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Impact of the different level landmarks. Landmarks SR↑ SPL↑ w/o 60.0 30.9 Room

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | HSSD, a synthetic dataset with scenes based on real house layouts, contains 40 validation scenes, 1,248 navigation episodes, and 6 object categories. | embodiment, simulator version and control stack | p. 7 (3 Method), p. 7 (3 Method) |
| Task/environment | HM3D, the official dataset of the Habitat 2022 ObjectNav Challenge, includes 2,000 validation episodes across 20 environments and 6 object categories. | reset, timeout, object/scene variation | p. 7 (3 Method), p. 8 (3 Method) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3 Method), p. 4 (3 Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 6 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Evaluation Metrics: We use two standard metrics: Success Rate (SR) and Success weighted by Path Length (SPL). | definition/direction/unit from same section | p. 7 (3 Method) |
| While InstructNav prioritizes SR with a dense search strategy, our approach maintains high success rates and boosts search efficiency by generating more accurate target ... | definition/direction/unit from same section | p. 8 (3 Method) |
| However, omitting object-level semantics enhances efficiency (32.0), as fine-grained searches with object-level cues increase success rates but often result in slower, localized exploration, leading ... | definition/direction/unit from same section | p. 9 (3 Method) |
| Figure 1: The search process: BeliefMapNav plans frontier paths by minimizing the expected search distance based on the 3D voxel-based belief map, ensuring efficient ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 3: The pipeline begins by passing the target and prompt to the LLM to generate hierarchical landmarks with relevance scores. Meanwhile, RGB and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| 3.3.3 Belief map construction After obtaining hierarchical textual landmarks with associated relevance scores, we project both the landmarks and the target object name into ... | definition/direction/unit from same section | p. 6 (3 Method) |
| Figure 5: (a) is the input depth image. (b) shows the confidence computed from the depth image. Bluer regions indicate higher confidence, meaning the ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| To extract these landmarks, we prompt an LLM (GPT-4 [35]) with the target object description, asking it to generate two outputs: (1) a set ... | definition/direction/unit from same section | p. 6 (3 Method) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 1, our method outperforms all existing zero-shot baselines, achieving significant improvements across multiple benchmarks. | comparison identity and matched condition | p. 8 (3 Method) |
| 4.2 Comparison with SOTA methods Table 1: BeliefMapNav can outperform previous SOTAs on both HM3D and MP3D benchmark. | comparison identity and matched condition | p. 8 (3 Method) |
| Figure 8: The proportion of different causes of failure in the HM3D dataset. A.6 Baselines We evaluate our approach in comparison with a range ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |
| 4 Experimental Results In this section, we outline datasets and key implementation details, then compare BeliefMapNav's performance against SOTA baselines on HM3D [17], MP3D ... | comparison identity and matched condition | p. 7 (3 Method) |
| Baseline summaries and HM3D failure analyses appear in Appendix A.6 and A.7, respectively. | comparison identity and matched condition | p. 7 (3 Method) |
| Prior work [48] similarly shows that BLIP-2 slightly surpasses CLIP in zero-shot text-to-image retrieval accuracy, while both are significantly better than BLIP. | comparison identity and matched condition | p. 9 (3 Method) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.3 Ablative study To evaluate the effectiveness of each module in our system, we conduct an ablation study on 400 randomly sampled episodes from ... | component/input/data sensitivity | p. 8 (3 Method) |
| Effectiveness of hierarchical landmarks: As shown in Table 4, without landmarks, we retrieve directly using the object name in the hierarchical 3D semantic map. | component/input/data sensitivity | p. 9 (3 Method) |
| Figure 4: Visualization of the prior belief map, visibility map, and the posterior belief map, with an enlarged section highlighting the target object. Effectiveness ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Ablation studies assess each component's contribution. | component/input/data sensitivity | p. 7 (3 Method) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of our method are mainly summarized as follows: 1)We propose BeliefMapNav, an efficient zero-shot object navigation system that accurately predicts target location ... | On the HM3D dataset, our method improves SPL by 46.4% compared to the zero-shot method InstructNav [9], which achieves the highest SR. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method), p. 14 (A.2 Adaptive hierarchical feature selection), p. 7 (3 Method) |
| Primary metric/result | However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D. | numeric claim only at cited anchor | p. 8 (3 Method) |

- Numeric sentences retained from the body:
- **p. 7 / 3 Method - extractive body cue:** HM3D, the official dataset of the Habitat 2022 ObjectNav Challenge, includes 2,000 validation episodes across 20 environments and 6 object categories.
- **p. 7 / 3 Method - extractive body cue:** We conduct experiments on its validation set, consisting of 11 environments, 21 object categories, and 2,195 object-goal navigation episodes.
- **p. 7 / 3 Method - extractive body cue:** HSSD, a synthetic dataset with scenes based on real house layouts, contains 40 validation scenes, 1,248 navigation episodes, and 6 object categories.
- **p. 8 / 3 Method - extractive body cue:** Implementation details: We limit navigation to 500 steps, defining success as stopping within 0.1m of the target.
- **p. 8 / 3 Method - extractive body cue:** The RGB-D camera, mounted 0.88m high, captures 640×480 images.
- **p. 9 / 3 Method - extractive body cue:** Semantics SR↑ SPL↑ Random Walking 21.5 10.8 Scene 59.0 30.4 Scene + Region 61.5 32.0 Scene + Region + Object 62.5 31.6 Effectiveness of different ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Baseline summaries and HM3D failure analyses appear in Appendix A.6 and A.7, respectively. | p. 7 (3 Method) |
| body limitation/failure cue | Across all datasets, the performance limitations of the local planner in [7] lead to significant degradation, especially in narrow areas. | p. 8 (3 Method) |
| body limitation/failure cue | Second, a lot of mesh "holes" in MP3D, which allow the agent to see through obstacles, causing it to mistakenly prioritize these holes as ... | p. 8 (3 Method) |
| body limitation/failure cue | Figure 8: The proportion of different causes of failure in the HM3D dataset. A.6 Baselines We evaluate our approach in comparison with a range ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | Figure 1: The search process: BeliefMapNav plans frontier paths by minimizing the expected search distance based on the 3D voxel-based belief map, ensuring efficient ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | For each semantic level, if the voxel does not contain an existing feature, we directly store the current feature and its associated confidence score. | p. 14 (A.2 Adaptive hierarchical feature selection) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation details: We limit navigation to 500 steps, defining success as stopping within 0.1m of the target. | p. 8 (3 Method) |
| However, CLIP demonstrates stronger generalization to out-of-distribution data and supports efficient inference via independent encoders and pre-computed features. | p. 9 (3 Method) |
| The task is successful if the agent issues a STOP within 0.1m of the target object within 500 steps. | p. 3 (3 Method) |
| It involves three steps as shown in Fig 3: 1) constructing a 3D hierarchical semantic voxel map based on visual observations in Sec. | p. 4 (3 Method) |
| The frontier observation belief estimation module computes frontier observation belief from the belief, frontiers, and visibility maps via FOV-based aggregation. | p. 4 (3 Method) |
| We back-project depth values patches into 3D space to form a point cloud and compute two geometric properties: the volume V k h,w and ... | p. 5 (3 Method) |
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

- **p. 7 / 3 Method - extractive body cue:** Baseline summaries and HM3D failure analyses appear in Appendix A.6 and A.7, respectively.
- **p. 8 / 3 Method - extractive body cue:** Across all datasets, the performance limitations of the local planner in [7] lead to significant degradation, especially in narrow areas.
- **p. 8 / 3 Method - extractive body cue:** Second, a lot of mesh "holes" in MP3D, which allow the agent to see through obstacles, causing it to mistakenly prioritize these holes as targets, ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 8: The proportion of different causes of failure in the HM3D dataset. A.6 Baselines We evaluate our approach in comparison with a range (ZSGN) ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The search process: BeliefMapNav plans frontier paths by minimizing the expected search distance based on the 3D voxel-based belief map, ensuring efficient and ...
- **p. 14 / A.2 Adaptive hierarchical feature selection - extractive body cue:** For each semantic level, if the voxel does not contain an existing feature, we directly store the current feature and its associated confidence score.

- **Evidence anchors reviewed:** datasets p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 15 (A.3 Prompting), p. 8 (3 Method), p. 15 (A.3 Prompting), metrics p. 7 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 2 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (3 Method), baselines p. 8 (3 Method), p. 8 (3 Method), p. 18 (Figure/Table caption), p. 7 (3 Method), p. 7 (3 Method), p. 9 (3 Method), results p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method), p. 14 (A.2 Adaptive hierarchical feature selection), p. 7 (3 Method).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
