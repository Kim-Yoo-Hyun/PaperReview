# Evaluation - Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/shen23a.html; PDF retrieval source: https://proceedings.mlr.press/v229/shen23a/shen23a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Results), p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results)): Although this success rate is far from practical for industrial use, our overall strategy of using 2D visual priors for 3D scene understanding can leverage the rapid advancements in VLMs, ...

## Evaluation Body Digest

- **p. 6 / 4 Results - extractive body cue:** For each task, we evaluate in ten scenes that contain novel objects in arbitrary poses and distractor objects.
- **p. 7 / 4 Results - extractive body cue:** We compare the success rates over ten evaluation scenes given two demonstrations for each task.
- **p. 7 / 4 Results - extractive body cue:** We consider a run successful if the robot grasps or places the correct corresponding object part for the task.
- **p. 6 / 4 Results - extractive body cue:** While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of the ...
- **p. 8 / 4 Results - extractive body cue:** (Bottom Row) Robot executing grasps sequentially without rescanning.
- **p. 7 / 4 Results - extractive body cue:** Although this success rate is far from practical for industrial use, our overall strategy of using 2D visual priors for 3D scene understanding can leverage ...
- **p. 6 / 4 Results - extractive body cue:** We present the success rates in Table 1 and examples of robot executions in Figure 5.
- **p. 7 / 4 Results - extractive body cue:** Language query success rates across semantic categories.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Results (p. 6); A.4 Experimental Setup (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although this success rate is far from practical for industrial use, our overall strategy of using 2D visual priors for 3D scene understanding can ... | p. 7 (4 Results) |
| 4 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of ... | p. 6 (4 Results) |
| 4 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We present the success rates in Table 1 and examples of robot executions in Figure 5. | p. 6 (4 Results) |
| 4 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Language query success rates across semantic categories. | p. 7 (4 Results) |

## Dataset / Benchmark Role

- **p. 6 / 4 Results - extractive body cue:** For each task, we evaluate in ten scenes that contain novel objects in arbitrary poses and distractor objects.
- **p. 7 / 4 Results - extractive body cue:** We compare the success rates over ten evaluation scenes given two demonstrations for each task.
- **p. 7 / 4 Results - extractive body cue:** We consider a run successful if the robot grasps or places the correct corresponding object part for the task.
- **p. 6 / 4 Results - extractive body cue:** While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of the ...
- **p. 8 / 4 Results - extractive body cue:** (Bottom Row) Robot executing grasps sequentially without rescanning.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Distilled Feature Fields Enable Open-Ended Manipulation. (1) Robot uses a selfie stick to scan RGB images of the scene (camera frustums shown). (2) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Representing 6-DOF Poses. (a) Recording the gripper pose T∗in virtual reality (VR) on an example mug. (b) We approximate the continuous local field ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Pipeline for Language-Guided Manipulation. (a) Encode the language query with CLIP, and compare its similarity to the average query point features over a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Five Grasping and Place Tasks. (a) grasping a mug by its lip or handle (Fig.2); (b) a screwdriver by the handle; (c) the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Generalizing to Novel Objects. (Top Row) Mug is much bigger than the ones used for demonstration. (Bottom Row) This rack has shorter pegs ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Grasping in a Cluttered Scene. (a) Demonstration for grasping the caterpillar in its DINO feature field (color is PCA, red dots show query ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Success rates on grasping and placing tasks. We compare the success rates over ten evaluation scenes given two demonstrations for each task. We ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Success rates of Language-Guided Ma- nipulation. Language query success rates across semantic categories. 4.2

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For each task, we evaluate in ten scenes that contain novel objects in arbitrary poses and distractor objects. | embodiment, simulator version and control stack | p. 6 (4 Results), p. 7 (4 Results) |
| Task/environment | We compare the success rates over ten evaluation scenes given two demonstrations for each task. | reset, timeout, object/scene variation | p. 7 (4 Results), p. 7 (4 Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 3 (3. Language-Guided Manipulation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Language-Guided Manipulation), p. 4 (6 DOF Gripper Pose) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Although this success rate is far from practical for industrial use, our overall strategy of using 2D visual priors for 3D scene understanding can ... | definition/direction/unit from same section | p. 7 (4 Results) |
| We present the success rates in Table 1 and examples of robot executions in Figure 5. | definition/direction/unit from same section | p. 6 (4 Results) |
| Language query success rates across semantic categories. | definition/direction/unit from same section | p. 7 (4 Results) |
| We compare the performance of three types of distilled features: (1) DINO ViT, (2) CLIP ViT, and (3) CLIP ResNet. | definition/direction/unit from same section | p. 6 (4 Results) |
| Figure 1: Distilled Feature Fields Enable Open-Ended Manipulation. (1) Robot uses a selfie stick to scan RGB images of the scene (camera frustums shown). ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 3: Pipeline for Language-Guided Manipulation. (a) Encode the language query with CLIP, and compare its similarity to the average query point features over ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 3: Feature Map Resolu- tions. Resolutions of the fea- tures output by the vision models given a 1280 × 720 RGB image. NeRF ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We reset the scenes to about the same configuration for each compared method. | comparison identity and matched condition | p. 6 (4 Results) |
| While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of ... | comparison identity and matched condition | p. 6 (4 Results) |
| (Bottom Row) Robot executing grasps sequentially without rescanning. | comparison identity and matched condition | p. 8 (4 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| (Bottom Row) Robot executing grasps sequentially without rescanning. | component/input/data sensitivity | p. 8 (4 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 3 Feature Fields for Robotic Manipulation (F3RM) We present Feature Fields for Robotic Manipulation (F3RM), our approach for distilling pre-trained representations from vision and ... | Although this success rate is far from practical for industrial use, our overall strategy of using 2D visual priors for 3D scene understanding can ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Results), p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results) |
| Primary metric/result | While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of ... | numeric claim only at cited anchor | p. 6 (4 Results) |

- Numeric sentences retained from the body:
- **p. 3 / 3. Language-Guided Manipulation - extractive body cue:** These two techniques combined enable us to extract dense, high-resolution patch-level 2D features from RGB images at about 25 frames per second and does not ...
- **p. 4 / 6 DOF Gripper Pose - extractive body cue:** (c) We concatenate feature vectors at these query points, then average over n (we use n = 2) demonstrations.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In comparison, 21/27 failures for CLIP ViT and ResNet combined may be attributed to this issue. | p. 6 (4 Results) |
| body limitation/failure cue | The DINO ViT has a good part-level understanding of object geometry with 7/19 failure cases caused by inaccuracies in the grasp rotations and occasionally, ... | p. 6 (4 Results) |
| body limitation/failure cue | This is a typical failure case - six out of 19 failures stem from these poor grasp predictions with rotational or translational errors. | p. 7 (4 Results) |
| body limitation/failure cue | Figure 3: Pipeline for Language-Guided Manipulation. (a) Encode the language query with CLIP, and compare its similarity to the average query point features over ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | The robot failed to grasp the stainless steel jug by its handle due to a small error in the grasp rotation. | p. 7 (4 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Distilled Feature Fields (DFFs) were introduced in computer graphics for tasks such as decomposing and editing images [5, 6]. | p. 1 (1 Introduction) |
| We present pseudocode for this technique in Appendix A.2. | p. 3 (3. Language-Guided Manipulation) |
| The query points X and demo embedding zT thus jointly encode the demo pose T. | p. 4 (6 DOF Gripper Pose) |
| (a) Encode the language query with CLIP, and compare its similarity to the average query point features over a set of demos. | p. 5 (6 DOF Gripper Pose) |
| To incorporate language guidance, we first compute Jpose from Eq.3 using the two demonstrations retrieved in the first step. | p. 5 (6 DOF Gripper Pose) |
| We consider a run successful if the robot grasps or places the correct corresponding object part for the task. | p. 7 (4 Results) |
| Although this success rate is far from practical for industrial use, our overall strategy of using 2D visual priors for 3D scene understanding can ... | p. 7 (4 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4 Results - extractive body cue:** In comparison, 21/27 failures for CLIP ViT and ResNet combined may be attributed to this issue.
- **p. 6 / 4 Results - extractive body cue:** The DINO ViT has a good part-level understanding of object geometry with 7/19 failure cases caused by inaccuracies in the grasp rotations and occasionally, the ...
- **p. 7 / 4 Results - extractive body cue:** This is a typical failure case - six out of 19 failures stem from these poor grasp predictions with rotational or translational errors.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Pipeline for Language-Guided Manipulation. (a) Encode the language query with CLIP, and compare its similarity to the average query point features over a ...
- **p. 7 / 4 Results - extractive body cue:** The robot failed to grasp the stainless steel jug by its handle due to a small error in the grasp rotation.

- **PDF anchors reviewed:** datasets p. 6 (4 Results), p. 7 (4 Results), p. 7 (4 Results), p. 6 (4 Results), p. 8 (4 Results), metrics p. 7 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 6 (4 Results), p. 2 (Figure/Table caption), p. 5 (Figure/Table caption), baselines p. 6 (4 Results), p. 6 (4 Results), p. 8 (4 Results), results p. 7 (4 Results), p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
