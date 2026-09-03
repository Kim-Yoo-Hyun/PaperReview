# Evaluation - Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2503.05189v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 6 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract)): Tier 1 Tier 2 Perturbations Success Rate Time (s) Success Rate Time (s) Clockwise 24/25 6.30 20/25 12.26 CCW 24/25 5.72 20/25 13.06 Follow Target 24/25 - 21/25 - TABLE ...

## Evaluation Body Digest

- **p. 2 / Abstract - extractive body cue:** As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require continuous interaction with ...
- **p. 2 / Abstract - extractive body cue:** This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Human & Robot Manipulation We deploy POGS for tracking human and robot manipulation tasks where objects may be in varying poses compared to their initial ...
- **p. 8 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Fox, "Contactgraspnet: Efficient 6-dof grasp generation in cluttered scenes," in 2021 IEEE International Conference on Robotics and Automation (ICRA), IEEE, 2021, pp.
- **p. 3 / Abstract - extractive body cue:** Robot See Robot Do [45] tracks partlevel objects using monocular video, though only in an offline processing setting for zero-shot motion planning robot imitation from ...
- **p. 3 / Abstract - extractive body cue:** We extend this work to support online rigid multi-object tracking along with the aforementioned semantic and object-centric feature fields to create a unified 3D scene ...
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** We evaluate POGS on two robotic manipulation tasks across various objects.
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** These tasks test POGS's ability to track objects of interest when manipulated by a robot or a human.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3) Persistent Object Tracking phase for online tracking | EMPIRICAL / REAL-ROBOT OR HARDWARE | Tier 1 Tier 2 Perturbations Success Rate Time (s) Success Rate Time (s) Clockwise 24/25 6.30 20/25 12.26 CCW 24/25 5.72 20/25 13.06 Follow ... | p. 6 (3) Persistent Object Tracking phase for online tracking) |
| 3) Persistent Object Tracking phase for online tracking | EMPIRICAL / REAL-ROBOT OR HARDWARE | Similar performance trends were observed in the other tasks, where POGS consistently outperformed ablations that either had depth perception turned off or were optimized ... | p. 5 (3) Persistent Object Tracking phase for online tracking) |
| 3) Persistent Object Tracking phase for online tracking | EMPIRICAL / REAL-ROBOT OR HARDWARE | For example, in the "Clothes Iron to Shelf" task under Tier 1, POGS achieved a maximum of 12 consecutive successful object resets, with a ... | p. 5 (3) Persistent Object Tracking phase for online tracking) |
| 6) Object surfaces exhibit low specularity for more robust | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate this experiment by recording the success rate and average time taken to recover from in-grasp tool perturbations. | p. 3 (6) Object surfaces exhibit low specularity for more robust) |
| 3) Persistent Object Tracking phase for online tracking | EMPIRICAL / REAL-ROBOT OR HARDWARE | During each trial, the target object is moved to five random poses in the workspace and we record the success rate for how often ... | p. 6 (3) Persistent Object Tracking phase for online tracking) |

## Dataset / Benchmark Role

- **p. 2 / Abstract - extractive body cue:** As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require continuous interaction with ...
- **p. 2 / Abstract - extractive body cue:** This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Human & Robot Manipulation We deploy POGS for tracking human and robot manipulation tasks where objects may be in varying poses compared to their initial ...
- **p. 8 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Fox, "Contactgraspnet: Efficient 6-dof grasp generation in cluttered scenes," in 2021 IEEE International Conference on Robotics and Automation (ICRA), IEEE, 2021, pp.
- **p. 3 / Abstract - extractive body cue:** Robot See Robot Do [45] tracks partlevel objects using monocular video, though only in an offline processing setting for zero-shot motion planning robot imitation from ...
- **p. 3 / Abstract - extractive body cue:** We extend this work to support online rigid multi-object tracking along with the aforementioned semantic and object-centric feature fields to create a unified 3D scene ...
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** We evaluate POGS on two robotic manipulation tasks across various objects.
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** These tasks test POGS's ability to track objects of interest when manipulated by a robot or a human.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Autonomous Object Manipulation and Tracking with POGS Unified Representation (Top) A robot autonomously performs a pick and place primitive to move the shoe ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: POGS Pipeline After capturing multiple images of a scene using a robot wrist-mounted ZED mini, POGS segments objects using Detic, extracts DINO features, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Occluded Grasp Sampling POGS is capable of sampling and performing robot grasps on geometry that is fully occluded from the observation camera view ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Object Reset Experimental Setup Middle: A human randomly perturbs the configuration of the tracked objects according to the two tiers. Right: A robot ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Tool Servoing Experimental Setup The robot continuously attempts to align the tracked tool with the target. Top: A human perturbs the tracked tool ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require continuous interaction ... | embodiment, simulator version and control stack | p. 2 (Abstract), p. 2 (Abstract) |
| Task/environment | This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly ... | reset, timeout, object/scene variation | p. 2 (Abstract), p. 4 (3) Persistent Object Tracking phase for online tracking) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The performance metrics included the maximum and mean number of consecutive successful object resets without losing tracking, the successful object reset rates, and the ... | definition/direction/unit from same section | p. 5 (3) Persistent Object Tracking phase for online tracking) |
| We evaluate this experiment by recording the success rate and average time taken to recover from in-grasp tool perturbations. | definition/direction/unit from same section | p. 3 (6) Object surfaces exhibit low specularity for more robust) |
| During each trial, the target object is moved to five random poses in the workspace and we record the success rate for how often ... | definition/direction/unit from same section | p. 6 (3) Persistent Object Tracking phase for online tracking) |
| When the tool-in-gripper rotation increased to 30°, the success rate drops to 40 of 50 trials at a longer time average of 12.66 seconds ... | definition/direction/unit from same section | p. 6 (3) Persistent Object Tracking phase for online tracking) |
| For example, in the "Clothes Iron to Shelf" task under Tier 1, POGS achieved a maximum of 12 consecutive successful object resets, with a ... | definition/direction/unit from same section | p. 5 (3) Persistent Object Tracking phase for online tracking) |
| We evaluate this experiment by recording the maximum number of sequential object resets before failure, the object grasp rate, the object place rate, and ... | definition/direction/unit from same section | p. 3 (6) Object surfaces exhibit low specularity for more robust) |
| The Gaussian means representing that object cluster are passed as a point cloud to Contact-GraspNet [57], which generates potential grasp candidates along with their ... | definition/direction/unit from same section | p. 4 (3) Persistent Object Tracking phase for online tracking) |
| However, these methods are prone to tracking errors when objects rotate and keypoints become occluded. | definition/direction/unit from same section | p. 2 (Abstract) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Similar performance trends were observed in the other tasks, where POGS consistently outperformed ablations that either had depth perception turned off or were optimized ... | comparison identity and matched condition | p. 5 (3) Persistent Object Tracking phase for online tracking) |
| Human & Robot Manipulation We deploy POGS for tracking human and robot manipulation tasks where objects may be in varying poses compared to their ... | comparison identity and matched condition | p. 4 (3) Persistent Object Tracking phase for online tracking) |
| This process repeats until errors in object state estimation are too high to recover for grasping. means, the object grasp is based on the ... | comparison identity and matched condition | p. 5 (3) Persistent Object Tracking phase for online tracking) |
| Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed ... | comparison identity and matched condition | p. 6 (3) Persistent Object Tracking phase for online tracking) |
| Each Gaussian cluster pose parameter is optimized independently, allowing POGS to track multiple moving objects, without imposing constraints on their relative movements. unlike prior ... | comparison identity and matched condition | p. 4 (3) Persistent Object Tracking phase for online tracking) |
| Jigsaw to Shelf Clothes Iron to Shelf Shoe to Shoerack Tier 1 Tier 2 Tier 1 Tier 2 Tier 1 Tier 2 No Depth ... | comparison identity and matched condition | p. 6 (3) Persistent Object Tracking phase for online tracking) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Jigsaw to Shelf Clothes Iron to Shelf Shoe to Shoerack Tier 1 Tier 2 Tier 1 Tier 2 Tier 1 Tier 2 No Depth ... | component/input/data sensitivity | p. 6 (3) Persistent Object Tracking phase for online tracking) |
| By embedding features from encoders and detectors pretrained on internet-scale datasets such as CLIP [8], DINO [9], and Detic [10], POGS can respond to ... | component/input/data sensitivity | p. 2 (Abstract) |
| In this work, we develop a method capable of updating the scene where a human can also move the objects repeatedly without any partial ... | component/input/data sensitivity | p. 2 (Abstract) |
| Without dimensionality reduction, storing per-Gaussian feature vectors would be computationally prohibitive. | component/input/data sensitivity | p. 4 (3) Persistent Object Tracking phase for online tracking) |
| Each Gaussian cluster pose parameter is optimized independently, allowing POGS to track multiple moving objects, without imposing constraints on their relative movements. unlike prior ... | component/input/data sensitivity | p. 4 (3) Persistent Object Tracking phase for online tracking) |
| The ablations highlight the critical role that both depth perception and robust visual features play in achieving accurate object localization and successful sequential object ... | component/input/data sensitivity | p. 5 (3) Persistent Object Tracking phase for online tracking) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly ... | Tier 1 Tier 2 Perturbations Success Rate Time (s) Success Rate Time (s) Clockwise 24/25 6.30 20/25 12.26 CCW 24/25 5.72 20/25 13.06 Follow ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 6 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract) |
| Primary metric/result | Similar performance trends were observed in the other tasks, where POGS consistently outperformed ablations that either had depth perception turned off or were optimized ... | numeric claim only at cited anchor | p. 5 (3) Persistent Object Tracking phase for online tracking) |

- Numeric sentences retained from the body:
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** To integrate the DINO features efficiently, we apply principal component analysis (PCA) to reduce their dimensionality from several hundred to d = 64 dimensions.
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** This model operates effectively at an image resolution of 1080p, with depth inference frequency at approximately 30 Hz.
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** The POGS model is trained and initialized on a PC workstation with an NVIDIA 4090 GPU.
- **p. 6 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Tier 1 Tier 2 Perturbations Success Rate Time (s) Success Rate Time (s) Clockwise 24/25 6.30 20/25 12.26 CCW 24/25 5.72 20/25 13.06 Follow Target ...
- **p. 6 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Tier 1 experiments have the target object stay on the tabletop plane and can move anywhere within a 55 cm by 50 cm square, and ...
- **p. 6 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Overall, POGS can be used to recover from tool perturbances in gripper up to 15° in 48 of 50 trials at an average of 6.01 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed ... | p. 6 (3) Persistent Object Tracking phase for online tracking) |
| body limitation/failure cue | After each object reset, a human will randomly reconfigure both objects to different poses and the process is repeated until failure. | p. 3 (6) Object surfaces exhibit low specularity for more robust) |
| body limitation/failure cue | We evaluate this experiment by recording the maximum number of sequential object resets before failure, the object grasp rate, the object place rate, and ... | p. 3 (6) Object surfaces exhibit low specularity for more robust) |
| body limitation/failure cue | Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the objects, defined as when repeated grasp ... | p. 5 (3) Persistent Object Tracking phase for online tracking) |
| body limitation/failure cue | This variation arises because each trial was executed until a grasping failure occurred-i.e., when the error in object state estimation became too high to ... | p. 6 (3) Persistent Object Tracking phase for online tracking) |
| body limitation/failure cue | mask does not exist) is helpful in reducing group feature noise for the scene background (anything in the scene that is not a tracked ... | p. 4 (3) Persistent Object Tracking phase for online tracking) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use Nerfstudio's [55] Splatfacto implementation of Gaussian Splatting with the gsplat [53] backend and modify it with the aforementioned image encoders and feature ... | p. 4 (3) Persistent Object Tracking phase for online tracking) |
| We run this experiment on two tiers with five trials each tier. | p. 6 (3) Persistent Object Tracking phase for online tracking) |
| The challenge is greater when dealing with irregularly shaped objects for which obtaining an accurate Computer-Aided Design (CAD) model is impractical. | p. 1 (Abstract) |
| After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder ... | p. 1 (Abstract) |
| Object Tracking for Manipulation Object pose estimation networks [29-32] are able to track the 6DOF pose of an object of interest, but typically not ... | p. 2 (Abstract) |
| By embedding features from encoders and detectors pretrained on internet-scale datasets such as CLIP [8], DINO [9], and Detic [10], POGS can respond to ... | p. 2 (Abstract) |
| We run DBSCAN [47] on the fused pointcloud to filter noise and floater points. | p. 3 (3) Persistent Object Tracking phase for online tracking) |
| For this we use Nerfstudio's [52, 53] 3DGS tile-based rasterizer implementation, with gradients backpropagated through the MLP within Femb. | p. 3 (3) Persistent Object Tracking phase for online tracking) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed objects ...
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** After each object reset, a human will randomly reconfigure both objects to different poses and the process is repeated until failure.
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** We evaluate this experiment by recording the maximum number of sequential object resets before failure, the object grasp rate, the object place rate, and the ...
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the objects, defined as when repeated grasp planning ...
- **p. 6 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** This variation arises because each trial was executed until a grasping failure occurred-i.e., when the error in object state estimation became too high to recover-resulting ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** mask does not exist) is helpful in reducing group feature noise for the scene background (anything in the scene that is not a tracked object).

- **Evidence anchors reviewed:** datasets p. 2 (Abstract), p. 2 (Abstract), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 8 (3) Persistent Object Tracking phase for online tracking), p. 3 (Abstract), p. 3 (Abstract), metrics p. 5 (3) Persistent Object Tracking phase for online tracking), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 6 (3) Persistent Object Tracking phase for online tracking), p. 6 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking), p. 3 (6) Object surfaces exhibit low specularity for more robust), baselines p. 5 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking), p. 6 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 6 (3) Persistent Object Tracking phase for online tracking), results p. 6 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 6 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Jigsaw to Shelf Clothes Iron to Shelf Shoe to Shoerack Tier 1 Tier 2 Tier 1 Tier 2 Tier 1 Tier 2 No Depth No DINO POGS POGS No Depth ... (p. 6, 3) Persistent Object Tracking phase for online tracking).
- **Metric evidence:** The performance metrics included the maximum and mean number of consecutive successful object resets without losing tracking, the successful object reset rates, and the mean and standard deviation of the ... (p. 5, 3) Persistent Object Tracking phase for online tracking).
- **Baseline/ablation evidence:** Each Gaussian cluster pose parameter is optimized independently, allowing POGS to track multiple moving objects, without imposing constraints on their relative movements. unlike prior work in real-time tracking of gaussian ... (p. 4, 3) Persistent Object Tracking phase for online tracking).
- **Failure/negative evidence:** Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the objects, defined as when repeated grasp planning failures occur due to irrecoverable ... (p. 5, 3) Persistent Object Tracking phase for online tracking).
