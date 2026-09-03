# Evaluation - Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2509.23107. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption)): Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial edges in ConceptGraph.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Unlike static benchmarks, these videos feature continuous scene evolution, where objects are moved, occluded, rotated, duplicated, or removed.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Static Representation Construction To evaluate the quality of the proposed static scene representation, we conducted experiments on the Replica dataset [32], which provides high-fidelity indoor ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We designed tasks in which latency fundamentally changes the grounding: (i) Occlusion-after-command: the target is visible at issue time but becomes occluded before robot received ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** These tags enable the planner to align grounding with the scene state that existed when the operator issued the instruction, rather than the delayed state ...
- **p. 2 / 3) Extensive experiments demonstrate that ST-OVSG ef - extractive body cue:** fectively models temporal variations and strengthens delay awareness in robotic planning, while achieving performance comparable to state-of-the-art methods in other aspects.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Across 17 trials, ST-OVSG achieved a success rate of 70.5%.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** This majority-vote strategy mitigates subjective bias and yields a stable estimate of accuracy.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial edges ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 3) Extensive experiments demonstrate that ST-OVSG ef (p. 2); IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Across 17 trials, ST-OVSG achieved a success rate of 70.5%. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | While the absolute improvement is small, this result reflects a consistent trend: adding structured scene information via ST-OVSG does not degrade planning quality, and ... | p. 6 (IV. EXPERIMENTS) |
| 3) Extensive experiments demonstrate that ST-OVSG ef | EMPIRICAL / SOURCE-REPORTED EVALUATION | fectively models temporal variations and strengthens delay awareness in robotic planning, while achieving performance comparable to state-of-the-art methods in other aspects. | p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | This majority-vote strategy mitigates subjective bias and yields a stable estimate of accuracy. | p. 5 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Unlike static benchmarks, these videos feature continuous scene evolution, where objects are moved, occluded, rotated, duplicated, or removed.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Static Representation Construction To evaluate the quality of the proposed static scene representation, we conducted experiments on the Replica dataset [32], which provides high-fidelity indoor ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We designed tasks in which latency fundamentally changes the grounding: (i) Occlusion-after-command: the target is visible at issue time but becomes occluded before robot received ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** These tags enable the planner to align grounding with the scene state that existed when the operator issued the instruction, rather than the delayed state ...
- **p. 2 / 3) Extensive experiments demonstrate that ST-OVSG ef - extractive body cue:** fectively models temporal variations and strengthens delay awareness in robotic planning, while achieving performance comparable to state-of-the-art methods in other aspects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. System overview. Based on the tn-1+∆t moment scene feedback, the local operator issues natural-language commands. These commands are sent over the data network ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. ST-OVSG builds a spatio-temporal open-vocabulary scene graph from RGB-D video sequences. Objects are detected and segmented from RGB frames, fused with depth to ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3. Execution process of the proposed method in a task. Left: users provide a natural-language grasp-and-place instruction at the local side (issue at 5.5s ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Unlike static benchmarks, these videos feature continuous scene evolution, where objects are moved, occluded, rotated, duplicated, or removed. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | Static Representation Construction To evaluate the quality of the proposed static scene representation, we conducted experiments on the Replica dataset [32], which provides high-fidelity ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Across 17 trials, ST-OVSG achieved a success rate of 70.5%. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| This majority-vote strategy mitigates subjective bias and yields a stable estimate of accuracy. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Nonetheless, the results demonstrate that latency tags allow instructions to be grounded to the correct historical state, substantially reducing referential errors caused by delayed ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| fectively models temporal variations and strengthens delay awareness in robotic planning, while achieving performance comparable to state-of-the-art methods in other aspects. | definition/direction/unit from same section | p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef) |
| Fig. 3. Execution process of the proposed method in a task. Left: users provide a natural-language grasp-and-place instruction at the local side (issue at ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| With ST-OVSG, the average similarity score is 0.1702, compared to 0.164 without STOVSG. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| fectively models temporal variations and strengthens delay awareness in robotic planning, while achieving performance comparable to state-of-the-art methods in other aspects. | comparison identity and matched condition | p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef) |
| These static results establish a baseline for subsequent experiments on dynamic environments, where temporal reasoning and latency-awareness play a central role. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Compared with static scenes (Subsection. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Fig. 3. Execution process of the proposed method in a task. Left: users provide a natural-language grasp-and-place instruction at the local side (issue at ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 3. Execution process of the proposed method in a task. Left: users provide a natural-language grasp-and-place instruction at the local side (issue at ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Unlike static benchmarks, these videos feature continuous scene evolution, where objects are moved, occluded, rotated, duplicated, or removed. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| With ST-OVSG, the average similarity score is 0.1702, compared to 0.164 without STOVSG. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| These scenarios are intentionally adversarial for non-latency-aware planners, which only operate on the most recent frame without historical alignment. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models ... | Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Primary metric/result | Across 17 trials, ST-OVSG achieved a success rate of 70.5%. | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Artificial delays in the range 0.25s-5s were injected between the local operator and the remote robot+planner.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Across 17 trials, ST-OVSG achieved a success rate of 70.5%.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** When the local feedback interface indicates that the hand is approaching Orange A, the operator issues the command: "Grasp the orange next to the hand, ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Spatio-Temporal Scene Representation Given a time-ordered set of posed RGB-D frames D = {(Irgb n , Id n, ∆tn, τn)}N n=1 where ∆Tn and τn ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** We maintain ST-OVSG, the representation is G1:N = ({Mn}N n=1, Etemp), where each per-frame graph is Mn = (On, Espa n ).
- **p. 3 / III. METHODOLOGY - extractive body cue:** Here, On = {oi,n}No i=1, No is number of all nodes of a frame, denotes object nodes at frame n, Espa n ⊆On × On ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by ... | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | In practice, many predicted actions were semantically correct but expressed with different phrasing or level of detail, which lowers embedding-based similarity without indicating execution ... | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Because our representation is designed for openvocabulary settings, automated evaluation of nodes and edges is unreliable: object categories and relational boundaries under open vocabulary ... | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | Motion blur, viewpoint shifts, and occlusions destabilize open-vocabulary detections. | p. 5 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each action sequence is linearized into imperative sentences, normalized, and encoded, after which cosine similarity is computed at the sequence level. | p. 6 (IV. EXPERIMENTS) |
| For implementation, the detection-description LVLM is instantiated with Qwen2.5-VL-7B [29]. | p. 5 (IV. EXPERIMENTS) |
| Dataset and Implementation Details Our evaluation is conducted on a custom dataset designed to capture the challenges of dynamic, non-static tabletop environments. | p. 5 (IV. EXPERIMENTS) |
| Across 17 trials, ST-OVSG achieved a success rate of 70.5%. | p. 6 (IV. EXPERIMENTS) |
| Pixels under mi,n are lifted into the world frame using the camera intrinsics K, and the camera-frame point is then computed | p. 3 (III. METHODOLOGY) |
| An image encoder Φv and a text encoder Φt (e.g., CLIP [27]) are adopted to extract masked visual features f img i = Φv(Irgb ... | p. 3 (III. METHODOLOGY) |
| The command is embedded with the CLIP text encoder, gu = Φt(u), and object nodes are scored by si,t = cos(gu, f txt i ... | p. 4 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In practice, many predicted actions were semantically correct but expressed with different phrasing or level of detail, which lowers embedding-based similarity without indicating execution failure.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Because our representation is designed for openvocabulary settings, automated evaluation of nodes and edges is unreliable: object categories and relational boundaries under open vocabulary cannot ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Motion blur, viewpoint shifts, and occlusions destabilize open-vocabulary detections.

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef), metrics p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef), p. 7 (Figure/Table caption), baselines p. 6 (IV. EXPERIMENTS), p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), results p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** These static results establish a baseline for subsequent experiments on dynamic environments, where temporal reasoning and latency-awareness play a central role. (p. 5, IV. EXPERIMENTS).
- **Metric evidence:** Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial edges in ConceptGraph. (p. 5, IV. EXPERIMENTS).
- **Baseline/ablation evidence:** With ST-OVSG, the average similarity score is 0.1702, compared to 0.164 without STOVSG. (p. 6, IV. EXPERIMENTS).
- **Failure/negative evidence:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses. (p. 6, IV. EXPERIMENTS).
