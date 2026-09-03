# Evaluation - GaussReg: Fast 3D Registration with Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2380_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (4 Experiment), p. 11 (4 Experiment), p. 12 (4 Experiment), p. 11 (4 Experiment), p. 13 (4 Experiment), p. 10 (4 Experiment)): Moreover, our method (ours) significantly outperforms our coarse registration (ours w./o. fine), proving the effectiveness of our fine registration.

## Evaluation Body Digest

- **p. 10 / 4 Experiment - extractive body cue:** Furthermore, to validate the generalization of our method, we collected 10 real-world scenes for testing, called GSReg dataset, which includes 6 indoor and 4 outdoor ...
- **p. 10 / 4 Experiment - extractive body cue:** Implementation Details Our GaussReg is merely trained on the ScanNetGSReg training set and evaluated on the ScanNet-GSReg test set, Objaverse test set, and GSReg dataset.
- **p. 9 / 4 Experiment - extractive body cue:** ScanNet [8] is a frequently used 3D dataset for indoor scenes, consisting of 1513 training scenes and 100 test scenes.
- **p. 9 / 4 Experiment - extractive body cue:** 4.1 Experiment Setup Dataset As there is currently no scene-level dataset available for our task, it is necessary for us to create a dataset in ...
- **p. 11 / 4 Experiment - extractive body cue:** GaussReg 11 Table 2: Evaluation on the Objaverse dataset. ↓means lower is better.
- **p. 11 / 4 Experiment - extractive body cue:** For indoor scenes in ScanNetGSReg, SuperPoint [10] sometimes fails to extract effective keypoints, leading to registration failures.
- **p. 12 / 4 Experiment - extractive body cue:** Visualizations of our method on the GSReg dataset are presented in the last two rows of Figure 4.
- **p. 12 / 4 Experiment - extractive body cue:** Evaluation on the GSReg Dataset The ground-truth registration results of our GSReg dataset are obtained when HLoc was successful.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiment (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, our method (ours) significantly outperforms our coarse registration (ours w./o. fine), proving the effectiveness of our fine registration. | p. 12 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, for 82 scenes in ScanNet-GSReg, HLoc only registers 75.6% of them successfully, while our method achieves a 100% success ... | p. 11 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, our method achieves registration results close to HLoc without fine-tuning, proving the strong generalizability of our approach. | p. 12 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method outperforms HLoc in RTE and RSE metrics and is comparable in RRE. | p. 11 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Comparing Index-5 and Index-6, we observe that although Index-5 has better depth estimation accuracy, the registration results are poor, proving that extracting geometric information ... | p. 13 (4 Experiment) |

## Dataset / Benchmark Role

- **p. 10 / 4 Experiment - extractive body cue:** Furthermore, to validate the generalization of our method, we collected 10 real-world scenes for testing, called GSReg dataset, which includes 6 indoor and 4 outdoor ...
- **p. 10 / 4 Experiment - extractive body cue:** Implementation Details Our GaussReg is merely trained on the ScanNetGSReg training set and evaluated on the ScanNet-GSReg test set, Objaverse test set, and GSReg dataset.
- **p. 9 / 4 Experiment - extractive body cue:** ScanNet [8] is a frequently used 3D dataset for indoor scenes, consisting of 1513 training scenes and 100 test scenes.
- **p. 9 / 4 Experiment - extractive body cue:** 4.1 Experiment Setup Dataset As there is currently no scene-level dataset available for our task, it is necessary for us to create a dataset in ...
- **p. 11 / 4 Experiment - extractive body cue:** GaussReg 11 Table 2: Evaluation on the Objaverse dataset. ↓means lower is better.
- **p. 11 / 4 Experiment - extractive body cue:** For indoor scenes in ScanNetGSReg, SuperPoint [10] sometimes fails to extract effective keypoints, leading to registration failures.
- **p. 12 / 4 Experiment - extractive body cue:** Visualizations of our method on the GSReg dataset are presented in the last two rows of Figure 4.
- **p. 12 / 4 Experiment - extractive body cue:** Evaluation on the GSReg Dataset The ground-truth registration results of our GSReg dataset are obtained when HLoc was successful.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: The purpose of our method is to register scenes A and B with Gaussian Splat- ting [17] models, and then combine A with ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: The architecture of GaussReg. Please refer to the text for detailed architecture. 3.1 Overview As shown in Figure 2, the proposed GaussReg mainly ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: The illustration of our overlap image selection and I3D feature extraction. of spherical harmonics. First, we select confidence points whose opacity α is ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4: Visualization of our final registration results on ScanNet-GSReg and GSReg. The first two columns are visualizations of GS point clouds to be registered. ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Evaluation on the ScanNet-GSReg dataset. ↓means lower is better, and ↑ means higher is better. We include the time of obtaining point cloud ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Evaluation on the Objaverse dataset. ↓means lower is better. Methods RRE↓ATE↓ FGR [45] 61.59 13.50 REGTR [39] 113.78 43.31
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Evaluation on the GSReg dataset. ↓means lower is better. Methods RRE↓RTE↓RSE↓ Ours w/o. fine 6.904 0.074 0.051 Ours 2.989 0.065 0.047 during training. ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 4. More visual results can be found in Supplementary Material. These experiments fully demonstrate the efficiency and accuracy of our method. Evaluation on the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Furthermore, to validate the generalization of our method, we collected 10 real-world scenes for testing, called GSReg dataset, which includes 6 indoor and 4 ... | embodiment, simulator version and control stack | p. 10 (4 Experiment), p. 10 (4 Experiment) |
| Task/environment | Implementation Details Our GaussReg is merely trained on the ScanNetGSReg training set and evaluated on the ScanNet-GSReg test set, Objaverse test set, and GSReg ... | reset, timeout, object/scene variation | p. 10 (4 Experiment), p. 9 (4 Experiment) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 6 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 7 (3 Method), p. 6 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For a fair comparison, we follow DReg-NeRF [7] to evaluate GaussReg on the Objaverse dataset with two metrics: 1) Relative Rotational Error (RRE); 2) ... | definition/direction/unit from same section | p. 10 (4 Experiment) |
| Finally, we evaluate GaussReg on the ScanNetGSReg and GSReg datasets with three metrics: 1) Relative Rotational Error (RRE), the geodesic distance between the estimated ... | definition/direction/unit from same section | p. 10 (4 Experiment) |
| These experiments fully demonstrate the efficiency and accuracy of our method. | definition/direction/unit from same section | p. 11 (4 Experiment) |
| Effectiveness of Image-Guided 3D Feature Extraction Here, we also report the Relative Depth Error (RDE), which is the ratio of the Euclidean distance between ... | definition/direction/unit from same section | p. 12 (4 Experiment) |
| For the sake of accuracy and efficiency, we believe that 10 is enough for k. | definition/direction/unit from same section | p. 12 (4 Experiment) |
| Comparing Index-5 and Index-6, we observe that although Index-5 has better depth estimation accuracy, the registration results are poor, proving that extracting geometric information ... | definition/direction/unit from same section | p. 13 (4 Experiment) |
| Our GS fusion and filtering strategy successfully merges the two GS models. | definition/direction/unit from same section | p. 13 (4 Experiment) |
| Both networks are trained separately for 40 epochs with a batch size of 1. | definition/direction/unit from same section | p. 11 (4 Experiment) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Therefore, we select the current SOTA method, HLoc [28] (SuperPoint [10] + SuperGlue [29]), as the baseline for comparison on ScanNet. | comparison identity and matched condition | p. 11 (4 Experiment) |
| In Table 2, our coarse registration method (ours w/o. fine) outperforms other methods without finetuning, demonstrating its strong generalization capability to objects. | comparison identity and matched condition | p. 12 (4 Experiment) |
| Our method outperforms HLoc in RTE and RSE metrics and is comparable in RRE. | comparison identity and matched condition | p. 11 (4 Experiment) |
| Moreover, our method (ours) significantly outperforms our coarse registration (ours w./o. fine), proving the effectiveness of our fine registration. | comparison identity and matched condition | p. 12 (4 Experiment) |
| Fig. 5: Quantitative Results on the GSReg dataset. The first two rows are indoor scenes, and the last two rows are outdoor scenes. The ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| For a fair comparison, we follow DReg-NeRF [7] to evaluate GaussReg on the Objaverse dataset with two metrics: 1) Relative Rotational Error (RRE); 2) ... | comparison identity and matched condition | p. 10 (4 Experiment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.3 Ablation Study To deeply analyze GaussReg, we conduct detailed ablation studies on the ScanNetGSReg dataset to evaluate the effectiveness of the proposed components. | component/input/data sensitivity | p. 12 (4 Experiment) |
| As shown in Table 2, our method achieves registration results close to HLoc without fine-tuning, proving the strong generalizability of our approach. | component/input/data sensitivity | p. 12 (4 Experiment) |
| GaussReg 13 Table 5: Ablation study with different k in overlap image selection on ScanNetGSReg. ↓means lower is better. | component/input/data sensitivity | p. 13 (4 Experiment) |
| I3D 3.169 0.036 0.061 0.066 6 Ours 2.827 0.042 0.032 0.080 As shown in Table 6, in Index-5, we remove the image-guided 3D (I3D) ... | component/input/data sensitivity | p. 13 (4 Experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions can be summarized as: • To the best of our knowledge, we are the first to explore the registration of 3D ... | Moreover, our method (ours) significantly outperforms our coarse registration (ours w./o. fine), proving the effectiveness of our fine registration. | PDF body cue; verify exact table/figure and matched conditions | p. 12 (4 Experiment), p. 11 (4 Experiment), p. 12 (4 Experiment), p. 11 (4 Experiment), p. 13 (4 Experiment), p. 10 (4 Experiment) |
| Primary metric/result | As shown in Table 1, for 82 scenes in ScanNet-GSReg, HLoc only registers 75.6% of them successfully, while our method achieves a 100% success ... | numeric claim only at cited anchor | p. 11 (4 Experiment) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiment - extractive body cue:** To evaluate the performance of GaussReg on objects, we also conduct tests on the Objaverse dataset [9] used in DReg-NeRF [7], whose test set contains ...
- **p. 11 / 4 Experiment - extractive body cue:** In the image-guided fine registration network, we render n = 5 images per GS model as input and set the number of depth hypotheses to ...
- **p. 11 / 4 Experiment - extractive body cue:** Both networks are trained separately for 40 epochs with a batch size of 1.
- **p. 11 / 4 Experiment - extractive body cue:** As shown in Table 1, for 82 scenes in ScanNet-GSReg, HLoc only registers 75.6% of them successfully, while our method achieves a 100% success ratio.
- **p. 11 / 4 Experiment - extractive body cue:** Notably, our method was significantly faster than HLoc (4.8s vs.
- **p. 12 / 4 Experiment - extractive body cue:** Meanwhile, our fine registration is faster than HLoc (4.8s vs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations and Future Work We only adopt a simple strategy to fuse and filter two GS models. | p. 13 (5 Discussion) |
| body limitation/failure cue | For indoor scenes in ScanNetGSReg, SuperPoint [10] sometimes fails to extract effective keypoints, leading to registration failures. | p. 11 (4 Experiment) |
| body limitation/failure cue | Future work can further explore to address this issue. | p. 13 (5 Discussion) |
| body limitation/failure cue | Eventually, after excluding cases of failed initial point cloud generation or unsuccessful GS reconstruction, we obtain 1297 training samples and 82 test samples. | p. 10 (4 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Both networks are trained separately for 40 epochs with a batch size of 1. | p. 11 (4 Experiment) |
| The learning rate starts from 1e -4 and decays exponentially by 0.05 every epoch. | p. 11 (4 Experiment) |
| Implementation Details Our GaussReg is merely trained on the ScanNetGSReg training set and evaluated on the ScanNet-GSReg test set, Objaverse test set, and GSReg ... | p. 10 (4 Experiment) |
| Specifically, in Figure 2, our Image-Guided Fine Registration primarily involves two steps: 1) Efficiently and accurately selecting highly overlapping cameras and rendering images accordingly; ... | p. 6 (3 Method) |
| Our selection follows 3 steps: 1) For every pair (Ca i , ˆCb j), we calculate the cosine value of the angle between their ... | p. 7 (3 Method) |
| Building the cost volume requires the minimum and maximum distances, which can be automatically computed from the rendered depth map of the reference image. | p. 7 (3 Method) |
| The rotation RB→A ∈ R3×3 and scale SB→A ∈R3 of the 3D gaussian can be computed as: \la b el {e q:eq 4 .2} ... | p. 8 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / 5 Discussion - extractive body cue:** Limitations and Future Work We only adopt a simple strategy to fuse and filter two GS models.
- **p. 11 / 4 Experiment - extractive body cue:** For indoor scenes in ScanNetGSReg, SuperPoint [10] sometimes fails to extract effective keypoints, leading to registration failures.
- **p. 13 / 5 Discussion - extractive body cue:** Future work can further explore to address this issue.
- **p. 10 / 4 Experiment - extractive body cue:** Eventually, after excluding cases of failed initial point cloud generation or unsuccessful GS reconstruction, we obtain 1297 training samples and 82 test samples.

- **Evidence anchors reviewed:** datasets p. 10 (4 Experiment), p. 10 (4 Experiment), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 11 (4 Experiment), p. 11 (4 Experiment), metrics p. 10 (4 Experiment), p. 10 (4 Experiment), p. 11 (4 Experiment), p. 12 (4 Experiment), p. 12 (4 Experiment), p. 13 (4 Experiment), baselines p. 11 (4 Experiment), p. 12 (4 Experiment), p. 11 (4 Experiment), p. 12 (4 Experiment), p. 14 (Figure/Table caption), p. 10 (4 Experiment), results p. 12 (4 Experiment), p. 11 (4 Experiment), p. 12 (4 Experiment), p. 11 (4 Experiment), p. 13 (4 Experiment), p. 10 (4 Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
