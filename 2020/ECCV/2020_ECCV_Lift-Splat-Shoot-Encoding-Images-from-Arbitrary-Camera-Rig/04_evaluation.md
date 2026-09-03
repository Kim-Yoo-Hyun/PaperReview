# Evaluation - Lift, Splat, Shoot: Encoding Images from Arbitrary Camera Rigs by Implicitly Unprojecting to 3D

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2008.05711; PDF retrieval source: https://arxiv.org/pdf/2008.05711. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 4 (Figure/Table caption), p. 11 (6 DOF localization and rasterize), p. 13 (Figure/Table caption), p. 6 (3 Method), p. 9 (6 DOF localization and rasterize)): Table 2: Map IOU in BEV frame 5.2 Segmentation We demonstrate that our Lift-Splat model is able to learn semantic 3D repre- sentations given supervision in the bird's-eye-view frame. Results ...

## Evaluation Body Digest

- **p. 8 / 3 Method - extractive body cue:** 5 Experiments and Results We use the nuScenes [2] and Lyft Level 5 [13] datasets to evaluate our approach. nuScenes is a large dataset of ...
- **p. 10 / 6 DOF localization and rasterize - extractive body cue:** We also include reported IOU scores for two concurrent works [9] [28] although both of these papers use different definitions of the bird's-eye-view grid and ...
- **p. 11 / 6 DOF localization and rasterize - extractive body cue:** IOU 4 26.53 4 + 1fl 27.35 4 + 1bl 27.27 4 + 1bl + 1fl 27.94 Table 3: We train on images from only ...
- **p. 12 / 6 DOF localization and rasterize - extractive body cue:** We determine the weather of a scene from the description string that accompanies every scene token in the nuScenes dataset.
- **p. 13 / 6 DOF localization and rasterize - extractive body cue:** This task is also important for benchmarking the performance of camera-based approaches versus lidar-based approaches because although the ceiling for 3D object detection from camera-only ...
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** The Lyft dataset does not come with a canonical train/val split.
- **p. 12 / 6 DOF localization and rasterize - extractive body cue:** To acquire templates, we fit K-Means for K = 1000 to all ego trajectories in the training set of nuScenes.
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** We also outperform concurrent work that benchmarks on the same segmentation tasks [9] [28].

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2: Map IOU in BEV frame 5.2 Segmentation We demonstrate that our Lift-Splat model is able to learn semantic 3D repre- sentations given ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 3: We visualize the "lift" step of our model. For each pixel, we predict a categorical distribution over depth α ∈△D-1 (left) and ... | p. 4 (Figure/Table caption) |
| 6 DOF localization and rasterize | SYSTEM / EVALUATION SCOPE UNRESOLVED | In Table 3, we show that the performance of our model for car segmentation improves when additional cameras are available at test time without ... | p. 11 (6 DOF localization and rasterize) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 5: When compared to models that use oracle depth from lidar, there is still room for improvement. Video inference from camera rigs is ... | p. 13 (Figure/Table caption) |
| 3 Method | SYSTEM / EVALUATION SCOPE UNRESOLVED | At test time, planning using the inferred cost map can be achieved by "shooting" different trajectories, scoring their cost, then acting according to lowest ... | p. 6 (3 Method) |

## Dataset / Benchmark Role

- **p. 8 / 3 Method - extractive body cue:** 5 Experiments and Results We use the nuScenes [2] and Lyft Level 5 [13] datasets to evaluate our approach. nuScenes is a large dataset of ...
- **p. 10 / 6 DOF localization and rasterize - extractive body cue:** We also include reported IOU scores for two concurrent works [9] [28] although both of these papers use different definitions of the bird's-eye-view grid and ...
- **p. 11 / 6 DOF localization and rasterize - extractive body cue:** IOU 4 26.53 4 + 1fl 27.35 4 + 1bl 27.27 4 + 1bl + 1fl 27.94 Table 3: We train on images from only ...
- **p. 12 / 6 DOF localization and rasterize - extractive body cue:** We determine the weather of a scene from the description string that accompanies every scene token in the nuScenes dataset.
- **p. 13 / 6 DOF localization and rasterize - extractive body cue:** This task is also important for benchmarking the performance of camera-based approaches versus lidar-based approaches because although the ceiling for 3D object detection from camera-only ...
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** The Lyft dataset does not come with a canonical train/val split.
- **p. 12 / 6 DOF localization and rasterize - extractive body cue:** To acquire templates, we fit K-Means for K = 1000 to all ego trajectories in the training set of nuScenes.
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** We also outperform concurrent work that benchmarks on the same segmentation tasks [9] [28].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose a model that, given multi-view camera data (left), infers semantics directly in the bird's-eye-view (BEV) coordinate frame (right). We show vehicle ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: (left, from SegNet [1]) Traditionally, computer vision tasks such as semantic segmentation involve making predictions in the same coordinate frame as the input ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: We visualize the "lift" step of our model. For each pixel, we predict a categorical distribution over depth α ∈△D-1 (left) and a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Lift-Splat-Shoot Outline Our model takes as input n images (left) and their corresponding extrinsic and intrinsic parameters. In the "lift" step, a frustum-shaped ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: We visualize the 1K trajectory tem- plates that we "shoot" onto our cost map dur- ing training and testing. During training, the cost ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Segment. IOU in BEV frame Drivable Area Lane Boundary CNN 68.96 16.51 Frozen Encoder 61.62 16.95
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Map IOU in BEV frame 5.2 Segmentation We demonstrate that our Lift-Splat model is able to learn semantic 3D repre- sentations given supervision ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: We show that it is possible to train our network such that it is resilient to common sources of sensor error. On the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5 Experiments and Results We use the nuScenes [2] and Lyft Level 5 [13] datasets to evaluate our approach. nuScenes is a large dataset ... | embodiment, simulator version and control stack | p. 8 (3 Method), p. 10 (6 DOF localization and rasterize) |
| Task/environment | We also include reported IOU scores for two concurrent works [9] [28] although both of these papers use different definitions of the bird's-eye-view grid ... | reset, timeout, object/scene variation | p. 10 (6 DOF localization and rasterize), p. 11 (6 DOF localization and rasterize) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Method), p. 6 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Map IOU in BEV frame 5.2 Segmentation We demonstrate that our Lift-Splat model is able to learn semantic 3D repre- sentations given ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| We also include reported IOU scores for two concurrent works [9] [28] although both of these papers use different definitions of the bird's-eye-view grid ... | definition/direction/unit from same section | p. 10 (6 DOF localization and rasterize) |
| Our approach is inspired by the recently proposed Neural Motion Planner (NMP) [41], an architecture that conditions on point clouds and high-definition maps to ... | definition/direction/unit from same section | p. 6 (3 Method) |
| Fig. 7: We measure intersection-over-union of car segmentation when each of the cam- eras is missing. The backwards camera on the nuScenes camera rig ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 6: We show that it is possible to train our network such that it is resilient to common sources of sensor error. On ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 3: We visualize the "lift" step of our model. For each pixel, we predict a categorical distribution over depth α ∈△D-1 (left) and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 6: Since planning is framed as classification among a set of 1K template trajectories, we measure top-5, top-10, and top-20 accuracy. We find ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| In summary, ideally, we would like to generate a function gc : (x, y, z) ∈R3 → c ∈RC for each image that can ... | definition/direction/unit from same section | p. 5 (3 Method) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We outperform these baselines on all tasks, as shown in Tables 1 and 2. | comparison identity and matched condition | p. 9 (6 DOF localization and rasterize) |
| On all benchmarks, we outperform our baselines. | comparison identity and matched condition | p. 10 (6 DOF localization and rasterize) |
| Road segmentation is shown in orange, lane segmentation is shown in green, and vehicle segmentation is shown in blue. nuScenes Lyft Drivable Area Lane ... | comparison identity and matched condition | p. 13 (6 DOF localization and rasterize) |
| Table 5: When compared to models that use oracle depth from lidar, there is still room for improvement. Video inference from camera rigs is ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Philion et al. models including baselines. | comparison identity and matched condition | p. 8 (3 Method) |
| We also outperform concurrent work that benchmarks on the same segmentation tasks [9] [28]. | comparison identity and matched condition | p. 9 (6 DOF localization and rasterize) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 8: For a single time stamp, we remove each of the cameras and visualize how the loss the cameras effects the prediction of the ... | component/input/data sensitivity | p. 12 (6 DOF localization and rasterize) |
| This definition of p(τi/o) enables us to learn an interpretable spatial cost function without defining a hard-margin loss as in NMP [41]. | component/input/data sensitivity | p. 7 (3 Method) |
| We reason that sensor dropout forces the model to learn the correlation between images on different cameras, similar to other variants of dropout [33] ... | component/input/data sensitivity | p. 10 (6 DOF localization and rasterize) |
| For low amounts of noise at test-time, models that are trained without any noise in the extrinsics perform the best because the BEV CNN ... | component/input/data sensitivity | p. 10 (6 DOF localization and rasterize) |
| In Table 3, we show that the performance of our model for car segmentation improves when additional cameras are available at test time without ... | component/input/data sensitivity | p. 11 (6 DOF localization and rasterize) |
| When the front camera is removed (top middle), the network extrapolates the lane and drivable area in front of the ego and extrapolates the ... | component/input/data sensitivity | p. 12 (6 DOF localization and rasterize) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section, we present our approach for learning bird's-eye-view representations of scenes from image data captured by an arbitrary camera rig. | Table 2: Map IOU in BEV frame 5.2 Segmentation We demonstrate that our Lift-Splat model is able to learn semantic 3D repre- sentations given ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 4 (Figure/Table caption), p. 11 (6 DOF localization and rasterize), p. 13 (Figure/Table caption), p. 6 (3 Method), p. 9 (6 DOF localization and rasterize) |
| Primary metric/result | Fig. 3: We visualize the "lift" step of our model. For each pixel, we predict a categorical distribution over depth α ∈△D-1 (left) and ... | numeric claim only at cited anchor | p. 4 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 3 Method - extractive body cue:** In our experiments, we set bins in both x and y from -50 meters to 50 meters with cells of size 0.5 meters × 0.5 ...
- **p. 8 / 3 Method - extractive body cue:** The resultant grid is therefore 200×200.
- **p. 8 / 3 Method - extractive body cue:** We restrict D between 4.0 meters and 45.0 meters spaced by 1.0 meters.
- **p. 8 / 3 Method - extractive body cue:** With these hyperparameters and architectural design choices, the forward pass of the model runs at 35 hz on a Titan V GPU.
- **p. 8 / 3 Method - extractive body cue:** Instead of relying on autograd to backprop through all three steps, the analytic gradient for the module as a whole can be derived, speeding up ...
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** We separate 48 of the Lyft scenes for validation to get a validation set of roughly the same size as nuScenes (6048 samples for Lyft, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We present methods for training our model that make the network robust to simple models of calibration noise. | p. 14 (6 Conclusion) |
| body limitation/failure cue | Our model does not have access to the speed of the car so it is compelling that the model predicts low-speed trajectories near crosswalks ... | p. 14 (6 Conclusion) |
| body limitation/failure cue | 5.3 Robustness Because the bird's-eye-view CNN learns from data how to fuse information across cameras, we can train the model to be robust to ... | p. 10 (6 DOF localization and rasterize) |
| body limitation/failure cue | On the left, we show that by training with a large amount of noise in the extrinsics (blue), the network becomes more robust to ... | p. 11 (6 DOF localization and rasterize) |
| body limitation/failure cue | The Lyft dataset does not come with a canonical train/val split. | p. 9 (6 DOF localization and rasterize) |
| body limitation/failure cue | We follow an architecture similar to MonoLayout [21] which also trains a CNN to output bird's-eye-view labels from images only but does not leverage ... | p. 9 (6 DOF localization and rasterize) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In all cases, we train for 300k steps using Adam [14] with learning rate 1e -3 and weight decay 1e -7. | p. 9 (6 DOF localization and rasterize) |
| With these hyperparameters and architectural design choices, the forward pass of the model runs at 35 hz on a Titan V GPU. | p. 8 (3 Method) |
| 4 Implementation 4.1 Architecture Details The neural architecture of our model is similar to OFT [29]. | p. 7 (3 Method) |
| During training, the cost of each template trajectory is computed and interpreted as a 1K-dimensional Boltzman distribution over the templates. | p. 7 (3 Method) |
| Code can be found on our project page. | p. 8 (3 Method) |
| Philion et al. nuScenes Lyft Car Vehicles Car Vehicles CNN 22.78 24.25 30.71 31.91 Frozen Encoder 25.51 26.83 35.28 32.42 OFT 29.72 30.05 39.48 ... | p. 10 (6 DOF localization and rasterize) |
| IOU in BEV frame Drivable Area Lane Boundary CNN 68.96 16.51 Frozen Encoder 61.62 16.95 OFT 71.69 18.07 Lift-Splat (Us) 72.94 19.96 PON∗[28] 60.4 ... | p. 10 (6 DOF localization and rasterize) |
| Lyft Car Lyft Vehicle CNN 7.00 8.06 Frozen Encoder 15.08 15.82 OFT 16.25 16.27 Lift-Splat (Us) 21.35 22.59 5.5 Benchmarking Against Oracle Depth We ... | p. 12 (6 DOF localization and rasterize) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 6 Conclusion - extractive body cue:** We present methods for training our model that make the network robust to simple models of calibration noise.
- **p. 14 / 6 Conclusion - extractive body cue:** Our model does not have access to the speed of the car so it is compelling that the model predicts low-speed trajectories near crosswalks and ...
- **p. 10 / 6 DOF localization and rasterize - extractive body cue:** 5.3 Robustness Because the bird's-eye-view CNN learns from data how to fuse information across cameras, we can train the model to be robust to simple ...
- **p. 11 / 6 DOF localization and rasterize - extractive body cue:** On the left, we show that by training with a large amount of noise in the extrinsics (blue), the network becomes more robust to extrinsic ...
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** The Lyft dataset does not come with a canonical train/val split.
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** We follow an architecture similar to MonoLayout [21] which also trains a CNN to output bird's-eye-view labels from images only but does not leverage inductive ...

- **Evidence anchors reviewed:** datasets p. 8 (3 Method), p. 10 (6 DOF localization and rasterize), p. 11 (6 DOF localization and rasterize), p. 12 (6 DOF localization and rasterize), p. 13 (6 DOF localization and rasterize), p. 9 (6 DOF localization and rasterize), metrics p. 10 (Figure/Table caption), p. 10 (6 DOF localization and rasterize), p. 6 (3 Method), p. 11 (Figure/Table caption), p. 11 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 9 (6 DOF localization and rasterize), p. 10 (6 DOF localization and rasterize), p. 13 (6 DOF localization and rasterize), p. 13 (Figure/Table caption), p. 8 (3 Method), p. 9 (6 DOF localization and rasterize), results p. 10 (Figure/Table caption), p. 4 (Figure/Table caption), p. 11 (6 DOF localization and rasterize), p. 13 (Figure/Table caption), p. 6 (3 Method), p. 9 (6 DOF localization and rasterize).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
