# Evaluation - Continuous 3D Perception Model with Persistent State

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.12387; PDF retrieval source: https://arxiv.org/pdf/2501.12387. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. 3D Reconstruction), p. 6 (4.1. Monocular and Video Depth Estimation), p. 8 (4.4. Analysis), p. 6 (4.1. Monocular and Video Depth Estimation), p. 5 (4.1. Monocular and Video Depth Estimation), p. 7 (4.3. 3D Reconstruction)): Our method significantly outperforms the other online approach Spann3R [101], and achieves comparable or sometimes better results than the top optimization-based method, DUSt3RGA, while operating online at 25× the speed.

## Evaluation Body Digest

- **p. 8 / 4.4. Analysis - extractive PDF cue:** For this experiment, we use the validation set of the MapFree [3] and ARKitScenes datasets, both with metric camera pose annotations.
- **p. 5 / 4.1. Monocular and Video Depth Estimation - extractive PDF cue:** Following MonST3R [125], we evaluate monocular depth estimation on KITTI [30], Sintel [12], Bonn [68] and NYU-v2 [65] datasets covering dynamic and static, indoor and ...
- **p. 5 / 4. Experiments - extractive PDF cue:** MonST3R finetunes DUSt3R on dynamic datasets to handle dynamic scenes, while Spann3R extends DUSt3R to support varying number of images via additional spatial memory and ...
- **p. 6 / 4.3. 3D Reconstruction - extractive PDF cue:** We evaluate scene-level reconstruction on the 7-scenes [83] and NRGBD [4] datasets using accuracy (Acc), completion (Comp), and normal consistency (NC) metrics, as in prior ...
- **p. 7 / 4.3. 3D Reconstruction - extractive PDF cue:** While operating online, our method achieves competitive performance, on par with and even surpassing offline methods that employ global alignment. the 7-Scenes dataset and 2 ...
- **p. 8 / 4.4. Analysis - extractive PDF cue:** State Update Analysis on 7-Scenes [83] and NRGBD [4] datasets. online revisiting … … Figure 5.
- **p. 7 / 4.3. 3D Reconstruction - extractive PDF cue:** Spann3R [101] is neither designed nor trained on dynamic scenes, making it less effective at handling moving objects, such as humans.
- **p. 6 / 4.1. Monocular and Video Depth Estimation - extractive PDF cue:** We report scale-invariant depth and metric depth accuracy on Sintel, Bonn, and KITTI datasets.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. 3D Reconstruction | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our method significantly outperforms the other online approach Spann3R [101], and achieves comparable or sometimes better results than the top optimization-based method, DUSt3RGA, while ... | p. 7 (4.3. 3D Reconstruction) |
| 4.1. Monocular and Video Depth Estimation | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our method achieves the best overall performance among all online methods. global alignment they use assumes that the scene is static, and enforcing multi-view ... | p. 6 (4.1. Monocular and Video Depth Estimation) |
| 4.4. Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | 5, revisiting improves performance compared to the online version, especially for accuracy. | p. 8 (4.4. Analysis) |
| 4.1. Monocular and Video Depth Estimation | SYSTEM / EVALUATION SCOPE UNRESOLVED | In the metric-scale setting, our method also significantly outperforms MASt3R for most metrics. | p. 6 (4.1. Monocular and Video Depth Estimation) |
| 4.1. Monocular and Video Depth Estimation | SYSTEM / EVALUATION SCOPE UNRESOLVED | 1 show our method achieves state-of-the-art or competitive performance, leading on Bonn and and NYU-v2 and ranking second on KITTI. | p. 5 (4.1. Monocular and Video Depth Estimation) |

## Dataset / Benchmark Role

- **p. 8 / 4.4. Analysis - extractive PDF cue:** For this experiment, we use the validation set of the MapFree [3] and ARKitScenes datasets, both with metric camera pose annotations.
- **p. 5 / 4.1. Monocular and Video Depth Estimation - extractive PDF cue:** Following MonST3R [125], we evaluate monocular depth estimation on KITTI [30], Sintel [12], Bonn [68] and NYU-v2 [65] datasets covering dynamic and static, indoor and ...
- **p. 5 / 4. Experiments - extractive PDF cue:** MonST3R finetunes DUSt3R on dynamic datasets to handle dynamic scenes, while Spann3R extends DUSt3R to support varying number of images via additional spatial memory and ...
- **p. 6 / 4.3. 3D Reconstruction - extractive PDF cue:** We evaluate scene-level reconstruction on the 7-scenes [83] and NRGBD [4] datasets using accuracy (Acc), completion (Comp), and normal consistency (NC) metrics, as in prior ...
- **p. 7 / 4.3. 3D Reconstruction - extractive PDF cue:** While operating online, our method achieves competitive performance, on par with and even surpassing offline methods that employ global alignment. the 7-Scenes dataset and 2 ...
- **p. 8 / 4.4. Analysis - extractive PDF cue:** State Update Analysis on 7-Scenes [83] and NRGBD [4] datasets. online revisiting … … Figure 5.
- **p. 7 / 4.3. 3D Reconstruction - extractive PDF cue:** Spann3R [101] is neither designed nor trained on dynamic scenes, making it less effective at handling moving objects, such as humans.
- **p. 6 / 4.1. Monocular and Video Depth Estimation - extractive PDF cue:** We report scale-invariant depth and metric depth accuracy on Sintel, Bonn, and KITTI datasets.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Continuous 3D Perception. Given a stream of RGB images as input, our approach enables dense 3D reconstruction in an online, continuous manner, estimating ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Querying Unseen Regions. In addition to reconstructing a scene from images, our method can also infer structure for unseen parts of the scene, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Method Overview. Our method performs online dense 3D reconstruction from a stream of images (video frames or a photo collection) by using a ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Single-frame Depth Evaluation. We report the perfor- mance on Sintel, Bonn, KITTI, and NYU-v2 (static) datasets. Video Depth Estimation. Video depth estimation evaluates ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Video Depth Evaluation. We report scale-invariant depth and metric depth accuracy on Sintel, Bonn, and KITTI datasets. Methods requiring global alignment are marked ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Evaluation on Camera Pose Estimation on Sintel [12], TUM-dynamic [89], and ScanNet [19] datasets. Our method achieves the best overall performance among all ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative Results on In-the-wild Internet Videos. We compare our method with concurrent works Spann3R [101] and MonST3R [125]. Our method achieves the best ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. 3D reconstruction comparison on 7-Scenes [83] and NRGBD [4] datasets. While operating online, our method achieves competitive performance, on par with and even ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For this experiment, we use the validation set of the MapFree [3] and ARKitScenes datasets, both with metric camera pose annotations. | embodiment, simulator version and control stack | p. 8 (4.4. Analysis), p. 5 (4.1. Monocular and Video Depth Estimation) |
| Task/environment | Following MonST3R [125], we evaluate monocular depth estimation on KITTI [30], Sintel [12], Bonn [68] and NYU-v2 [65] datasets covering dynamic and static, indoor ... | reset, timeout, object/scene variation | p. 5 (4.1. Monocular and Video Depth Estimation), p. 5 (4. Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 3 (3.1. State-Input Interaction Mechanism) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3.1. State-Input Interaction Mechanism), p. 4 (3.2. Querying the State with Unseen Views) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate scene-level reconstruction on the 7-scenes [83] and NRGBD [4] datasets using accuracy (Acc), completion (Comp), and normal consistency (NC) metrics, as in ... | definition/direction/unit from same section | p. 6 (4.3. 3D Reconstruction) |
| 5, revisiting improves performance compared to the online version, especially for accuracy. | definition/direction/unit from same section | p. 8 (4.4. Analysis) |
| We use absolute relative error (Abs Rel) and δ < 1.25 (percentage of predicted depths within a 1.25-factor of true depth) as metrics, with ... | definition/direction/unit from same section | p. 5 (4.1. Monocular and Video Depth Estimation) |
| We report scale-invariant depth and metric depth accuracy on Sintel, Bonn, and KITTI datasets. | definition/direction/unit from same section | p. 6 (4.1. Monocular and Video Depth Estimation) |
| In contrast, our method operates online and achieves state-ofthe-art performance across both static and dynamic scenes. | definition/direction/unit from same section | p. 7 (4.3. 3D Reconstruction) |
| From top to bottom: the input image; the ground truth (GT) image, used to query the state via its camera parameters (note: GT image ... | definition/direction/unit from same section | p. 8 (4.4. Analysis) |
| We report the performance on Sintel, Bonn, KITTI, and NYU-v2 (static) datasets. | definition/direction/unit from same section | p. 5 (4.1. Monocular and Video Depth Estimation) |
| We demonstrate this capability of our method in Tab. | definition/direction/unit from same section | p. 7 (4.4. Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We present a subset of baselines here; please refer to the supplementary material for full comparisons. | comparison identity and matched condition | p. 6 (4.1. Monocular and Video Depth Estimation) |
| Under per-sequence scale alignment, our method consistently outperforms DUSt3R [107] and MASt3R [51]. | comparison identity and matched condition | p. 5 (4.1. Monocular and Video Depth Estimation) |
| 1 show our method achieves state-of-the-art or competitive performance, leading on Bonn and and NYU-v2 and ranking second on KITTI. | comparison identity and matched condition | p. 5 (4.1. Monocular and Video Depth Estimation) |
| We compare to baselines that share this feature. | comparison identity and matched condition | p. 6 (4.2. Camera Pose Estimation) |
| Our method significantly outperforms the other online approach Spann3R [101], and achieves comparable or sometimes better results than the top optimization-based method, DUSt3RGA, while ... | comparison identity and matched condition | p. 7 (4.3. 3D Reconstruction) |
| 5, revisiting improves performance compared to the online version, especially for accuracy. | comparison identity and matched condition | p. 8 (4.4. Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For metric pointmap methods like ours and MASt3R, we also report results without alignment. | component/input/data sensitivity | p. 5 (4.1. Monocular and Video Depth Estimation) |
| We report scale-invariant depth and metric depth accuracy on Sintel, Bonn, and KITTI datasets. | component/input/data sensitivity | p. 6 (4.1. Monocular and Video Depth Estimation) |
| For the online category, we additionally include DUSt3R [107] where we align all video frames with first frame, without using GA. | component/input/data sensitivity | p. 6 (4.2. Camera Pose Estimation) |
| Our model continuously updates its state representation as new data arrives, relying solely on past and current observations without knowledge of future inputs. | component/input/data sensitivity | p. 7 (4.4. Analysis) |
| To the best of our knowledge, our method is the first to enable the inference of unseen structures in metric scale for general scenes, ... | component/input/data sensitivity | p. 8 (4.4. Analysis) |
| 4.3, we introduce an additional version of our approach called "revisiting": we first run our method online to obtain the final state that has ... | component/input/data sensitivity | p. 7 (4.4. Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability ... | Our method significantly outperforms the other online approach Spann3R [101], and achieves comparable or sometimes better results than the top optimization-based method, DUSt3RGA, while ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. 3D Reconstruction), p. 6 (4.1. Monocular and Video Depth Estimation), p. 8 (4.4. Analysis), p. 6 (4.1. Monocular and Video Depth Estimation), p. 5 (4.1. Monocular and Video Depth Estimation), p. 7 (4.3. 3D Reconstruction) |
| Primary metric/result | Our method achieves the best overall performance among all online methods. global alignment they use assumes that the scene is static, and enforcing multi-view ... | numeric claim only at cited anchor | p. 6 (4.1. Monocular and Video Depth Estimation) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Monocular and Video Depth Estimation - extractive PDF cue:** We also report the FPS on KITTI dataset using 512× 144 image resolution for all methods on an A100 GPU, except Spann3R which only supports ...
- **p. 6 / 4.3. 3D Reconstruction - extractive PDF cue:** To assess performance on image collections with minimal or no overlap, we evaluate using sparsely sampled images: 3 to 5 frames per scene for 6
- **p. 7 / 4.3. 3D Reconstruction - extractive PDF cue:** 7 scenes [83] NRGBD [4] Acc↓ Comp↓ NC↑ Acc↓ Comp↓ NC↑ Method Optim.
- **p. 7 / 4.3. 3D Reconstruction - extractive PDF cue:** While operating online, our method achieves competitive performance, on par with and even surpassing offline methods that employ global alignment. the 7-Scenes dataset and 2 ...
- **p. 5 / 3.4. Training Strategy - extractive PDF cue:** These two stages are trained on 224×224 images to reduce computational costs, following DUSt3R [107].
- **p. 5 / 3.4. Training Strategy - extractive PDF cue:** Both the encoder and decoders operate on 16×16 pixel patches.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration. | p. 6 (4.2. Camera Pose Estimation) |
| body limitation/failure cue | Most prior approaches do so through test-time optimization, as seen in RobustCVD [47] and CasualSAM [128], which jointly estimate camera parameters and dense depth ... | p. 6 (4.2. Camera Pose Estimation) |
| body limitation/failure cue | Table 6. Training Datasets. We provide more details of our training datasets. We classify a dataset as dynamic if annotations exist for moving objects ... | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use Adam-W optimizer [58] with an initial learning rate of 1e-4, applying linear warmup followed by cosine decay. | p. 5 (3.4. Training Strategy) |
| Both the encoder and decoders operate on 16×16 pixel patches. | p. 5 (3.4. Training Strategy) |
| We also report the FPS on KITTI dataset using 512× 144 image resolution for all methods on an A100 GPU, except Spann3R which only ... | p. 6 (4.1. Monocular and Video Depth Estimation) |
| 4.3, we introduce an additional version of our approach called "revisiting": we first run our method online to obtain the final state that has ... | p. 7 (4.4. Analysis) |
| This setup differs from the online setup by allowing the state to see the full context of the scene during the first run. | p. 8 (4.4. Analysis) |
| For each current image, It, it is first encoded into token representation by a ViT encoder [22]: Ft = Encoderi(It). | p. 3 (3.1. State-Input Interaction Mechanism) |
| Within the decoders, the outputs from both sides cross-attend to each other at each decoder block to ensure effective information transfer. | p. 3 (3.1. State-Input Interaction Mechanism) |
| Both processes occur simultaneously through two interconnected ViT decoders. | p. 4 (3.1. State-Input Interaction Mechanism) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Camera Pose Estimation - extractive PDF cue:** Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration.
- **p. 6 / 4.2. Camera Pose Estimation - extractive PDF cue:** Most prior approaches do so through test-time optimization, as seen in RobustCVD [47] and CasualSAM [128], which jointly estimate camera parameters and dense depth maps ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 6. Training Datasets. We provide more details of our training datasets. We classify a dataset as dynamic if annotations exist for moving objects like ...

- **PDF anchors reviewed:** datasets p. 8 (4.4. Analysis), p. 5 (4.1. Monocular and Video Depth Estimation), p. 5 (4. Experiments), p. 6 (4.3. 3D Reconstruction), p. 7 (4.3. 3D Reconstruction), p. 8 (4.4. Analysis), metrics p. 6 (4.3. 3D Reconstruction), p. 8 (4.4. Analysis), p. 5 (4.1. Monocular and Video Depth Estimation), p. 6 (4.1. Monocular and Video Depth Estimation), p. 7 (4.3. 3D Reconstruction), p. 8 (4.4. Analysis), baselines p. 6 (4.1. Monocular and Video Depth Estimation), p. 5 (4.1. Monocular and Video Depth Estimation), p. 5 (4.1. Monocular and Video Depth Estimation), p. 6 (4.2. Camera Pose Estimation), p. 7 (4.3. 3D Reconstruction), p. 8 (4.4. Analysis), results p. 7 (4.3. 3D Reconstruction), p. 6 (4.1. Monocular and Video Depth Estimation), p. 8 (4.4. Analysis), p. 6 (4.1. Monocular and Video Depth Estimation), p. 5 (4.1. Monocular and Video Depth Estimation), p. 7 (4.3. 3D Reconstruction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
