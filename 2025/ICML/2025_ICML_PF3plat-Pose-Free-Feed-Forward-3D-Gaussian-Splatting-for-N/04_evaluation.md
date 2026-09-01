# Evaluation - PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting for Novel View Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=VjI1NnsW4t; PDF retrieval source: https://openreview.net/pdf/1de18a350e0bb48018a9598f9f8511c407b8b26b.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4.5. Analysis and More Results), p. 9 (4.5. Analysis and More Results), p. 8 (4.4. Ablation Study), p. 7 (4.3. Experimental Results), p. 6 (4.3. Experimental Results), p. 8 (4.4. Ablation Study)): 5d, show that our method achieves a PSNR of over 20 dB for both datasets, significantly outperforming (Hong et al., 2024).

## Evaluation Body Digest

- **p. 5 / 4.2. Experimental Setting - extractive PDF cue:** For RealEstate10K, due to some unavailable videos on YouTube, we use a subset of the full dataset, comprising a training set of 21,618 scenes and ...
- **p. 5 / 4.2. Experimental Setting - extractive PDF cue:** We train and evaluate our method on three largescale datasets: RealEstate10K (Zhou et al., 2018), a collection of both indoor and outdoor scenes; ACID (Liu ...
- **p. 7 / 4.3. Experimental Results - extractive PDF cue:** While RealEstate-10K and ACID encompass a variety of indoor and outdoor scenes, RealEstate-10K predominantly includes indoor environments, whereas ACID features numerous dynamic scenes.
- **p. 7 / 4.3. Experimental Results - extractive PDF cue:** This highlights the effectiveness of our method in managing varied scene and object types, reinforcing its applicability for practical view synthesis tasks.
- **p. 6 / 4.2. Experimental Setting - extractive PDF cue:** Due to absence of GT depth in our datasets, we leverage their pre-trained weights and direct comparison is avoided.
- **p. 9 / 4.5. Analysis and More Results - extractive PDF cue:** 5d, show that our method achieves a PSNR of over 20 dB for both datasets, significantly outperforming (Hong et al., 2024).
- **p. 9 / 4.5. Analysis and More Results - extractive PDF cue:** To demonstrate the generalization capability, we conduct a cross-dataset evaluation and compare against (Hong et al., 2024).
- **p. 6 / 4.2. Experimental Setting - extractive PDF cue:** Evaluation Protocol For evaluation, we follow the protocol outlined by (Hong et al., 2024) using unposed triplet images (I1, I2, It), with the test set ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Implementation Details (p. 5); 4.2. Experimental Setting (p. 5); 4.3. Experimental Results (p. 6); 4.5. Analysis and More Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.5. Analysis and More Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5d, show that our method achieves a PSNR of over 20 dB for both datasets, significantly outperforming (Hong et al., 2024). | p. 9 (4.5. Analysis and More Results) |
| 4.5. Analysis and More Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | From these results, we find that our method achieves significantly better performance than the others, highlighting our capability to extend to multiple N views. | p. 9 (4.5. Analysis and More Results) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | We also demonstrate that without pre-trained weights for the depth and correspondence networks, the training either fails or achieves significantly lower performance. | p. 8 (4.4. Ablation Study) |
| 4.3. Experimental Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | From these results, we observe that our method outperforms CoPoNeRF (Hong et al., 2024) by over 5 dB in large-overlap scenarios and by 4 ... | p. 7 (4.3. Experimental Results) |
| 4.3. Experimental Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, our method significantly outperforms previous pose-free generalizable methods (Chen & Lee, 2023; Smith et al., 6 | p. 6 (4.3. Experimental Results) |

## Dataset / Benchmark Role

- **p. 5 / 4.2. Experimental Setting - extractive PDF cue:** For RealEstate10K, due to some unavailable videos on YouTube, we use a subset of the full dataset, comprising a training set of 21,618 scenes and ...
- **p. 5 / 4.2. Experimental Setting - extractive PDF cue:** We train and evaluate our method on three largescale datasets: RealEstate10K (Zhou et al., 2018), a collection of both indoor and outdoor scenes; ACID (Liu ...
- **p. 7 / 4.3. Experimental Results - extractive PDF cue:** While RealEstate-10K and ACID encompass a variety of indoor and outdoor scenes, RealEstate-10K predominantly includes indoor environments, whereas ACID features numerous dynamic scenes.
- **p. 7 / 4.3. Experimental Results - extractive PDF cue:** This highlights the effectiveness of our method in managing varied scene and object types, reinforcing its applicability for practical view synthesis tasks.
- **p. 6 / 4.2. Experimental Setting - extractive PDF cue:** Due to absence of GT depth in our datasets, we leverage their pre-trained weights and direct comparison is avoided.
- **p. 9 / 4.5. Analysis and More Results - extractive PDF cue:** 5d, show that our method achieves a PSNR of over 20 dB for both datasets, significantly outperforming (Hong et al., 2024).
- **p. 9 / 4.5. Analysis and More Results - extractive PDF cue:** To demonstrate the generalization capability, we conduct a cross-dataset evaluation and compare against (Hong et al., 2024).
- **p. 6 / 4.2. Experimental Setting - extractive PDF cue:** Evaluation Protocol For evaluation, we follow the protocol outlined by (Hong et al., 2024) using unposed triplet images (I1, I2, It), with the test set ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1. Overall architecture and loss of the proposed method. (a) Given a set of unposed images and their camera intrinsics, our method aligns the ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Tab. 4. A possible solution to mitigate this issue is to em- poloy iterative scene-specific optimization steps (Fu et al., 2023) or to assume ground-truth ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 2. Proposed refinement and confidence estimation modules. In our Fine Alignment module, we refine depth and pose to improve 3D reconstruction and view synthesis ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative Comparison on RealEstate-10K and ACID. Given two context views (a) and (b), we compare novel view rendering results. Baselines. Following (Hong et ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Novel View Synthesis Performance on RealEstate-10K and ACID. Gray entries indicate methods that use ground truth camera poses during evaluation and are not ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Pose Estimation Performance on RealEstate-10K and ACID. Gray entries indicate methods that were not trained on the same dataset due to missing ground-truth ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Novel View Synthesis and Pose Estimation Performance on DL3DV. We include PixelSplat and MVSplat for reference only. DL3DV Pose-Free
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Component ablations on RealEstate10K. Components Avg PSNR SSIM LPIPS Rotation Translation

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For RealEstate10K, due to some unavailable videos on YouTube, we use a subset of the full dataset, comprising a training set of 21,618 scenes ... | embodiment, simulator version and control stack | p. 5 (4.2. Experimental Setting), p. 5 (4.2. Experimental Setting) |
| Task/environment | We train and evaluate our method on three largescale datasets: RealEstate10K (Zhou et al., 2018), a collection of both indoor and outdoor scenes; ACID ... | reset, timeout, object/scene variation | p. 5 (4.2. Experimental Setting), p. 7 (4.3. Experimental Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.2.1. COARSE ALIGNMENT OF 3D GAUSSIANS), p. 3 (3.1. Problem Formulation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.2.4. 3D GAUSSIAN PARAMTER PREDICTIONS), p. 4 (3.2.3. CAMERA POSE REFINEMENT) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| From these results, we observe that our method outperforms CoPoNeRF (Hong et al., 2024) by over 5 dB in large-overlap scenarios and by 4 ... | definition/direction/unit from same section | p. 7 (4.3. Experimental Results) |
| We also report the Absolute Trajectory Error (ATE). | definition/direction/unit from same section | p. 9 (4.5. Analysis and More Results) |
| Additionally, our approach also demonstrates superior pose estimation performance on both datasets, even surpassing (Hong et al., 2024) that trains its network with GT ... | definition/direction/unit from same section | p. 7 (4.3. Experimental Results) |
| The performance gap widens further when we adopt a similar test-time optimization (TTO) strategy. | definition/direction/unit from same section | p. 8 (4.5. Analysis and More Results) |
| Classical methods tend to achieve higher precision, whereas learning-based approaches generally offer greater robustness. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Table 6. Different Strategies for Coarse Alignment. Pro (Bochkovskii et al., 2024) for coarse alignment. The results, presented in Tab. 6, reveal that using ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| For the DL3DV dataset, we start with a frame distance of 5 and increase it to 10. | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |
| Our model is trained on 4 NVIDIA A100 GPU for 50,000 iterations using the Adam optimizer (Kingma, 2014), with a learning rate set to ... | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, our method significantly outperforms previous pose-free generalizable methods (Chen & Lee, 2023; Smith et al., 6 | comparison identity and matched condition | p. 6 (4.3. Experimental Results) |
| Additionally, our approach also demonstrates superior pose estimation performance on both datasets, even surpassing (Hong et al., 2024) that trains its network with GT ... | comparison identity and matched condition | p. 7 (4.3. Experimental Results) |
| In other words, we cannot train our approach on their dataset, nor can they train theirs on ours. *: We also include a MASt3R ... | comparison identity and matched condition | p. 7 (4.3. Experimental Results) |
| With only the photometric loss, we observe that after certain iterations, as the baseline becomes wider, the training loss quickly diverges. | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |
| Finally, CF-3DGS struggles to find accurate camera poses and suffers in rendering quality, likely because its design does not adequately handle wide-baseline images. | comparison identity and matched condition | p. 8 (4.5. Analysis and More Results) |
| 5d, show that our method achieves a PSNR of over 20 dB for both datasets, significantly outperforming (Hong et al., 2024). | comparison identity and matched condition | p. 9 (4.5. Analysis and More Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In this ablation study, we aim to investigate the effectiveness of each component of our method. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| Component ablations on RealEstate10K. | component/input/data sensitivity | p. 8 (4.3. Experimental Results) |
| For novel view synthesis, we compare our approach against established generalized NeRF and 3DGS variants, including PixelNeRF (Yu et al., 2021), (Du et al., ... | component/input/data sensitivity | p. 6 (4.2. Experimental Setting) |
| In other words, we cannot train our approach on their dataset, nor can they train theirs on ours. *: We also include a MASt3R ... | component/input/data sensitivity | p. 7 (4.3. Experimental Results) |
| The code and pretrained weights will be made publicly available. | component/input/data sensitivity | p. 5 (4.1. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our contributions below: • We propose PF3plat, a feed-forward network that reconstructs 3D scenes, parameterized by 3D Gaussians, from sparse, unposed views ... | 5d, show that our method achieves a PSNR of over 20 dB for both datasets, significantly outperforming (Hong et al., 2024). | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4.5. Analysis and More Results), p. 9 (4.5. Analysis and More Results), p. 8 (4.4. Ablation Study), p. 7 (4.3. Experimental Results), p. 6 (4.3. Experimental Results), p. 8 (4.4. Ablation Study) |
| Primary metric/result | From these results, we find that our method achieves significantly better performance than the others, highlighting our capability to extend to multiple N views. | numeric claim only at cited anchor | p. 9 (4.5. Analysis and More Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4.2. Experimental Setting - extractive PDF cue:** For RealEstate10K, due to some unavailable videos on YouTube, we use a subset of the full dataset, comprising a training set of 21,618 scenes and ...
- **p. 5 / 4.2. Experimental Setting - extractive PDF cue:** For ACID, we train on 10,935 scenes and evaluate on 1,893 scenes.
- **p. 5 / 4.2. Experimental Setting - extractive PDF cue:** Lastly, for DL3DV, we train on 10,510 different scenes and evaluate on the standard benchmark set of 140 scenes for testing (Ling et al., 2024).
- **p. 7 / 4.3. Experimental Results - extractive PDF cue:** In other words, we cannot train our approach on their dataset, nor can they train theirs on ours. *: We also include a MASt3R variant ...
- **p. 8 / 4.5. Analysis and More Results - extractive PDF cue:** However, for N = 12, our inference speed is slower than that of DBARF, as our method involves estimating camera poses via a robust solver ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our framework, PFSplat, is built on foundation models to overcome inherent limitations of 3DGS. | p. 9 (5. Conclusion) |
| body limitation/failure cue | Similar observations are made in (I-I), (I-II), and (I-V), where we identify that directly tuning the depth network or training only with photometric losses ... | p. 8 (4.4. Ablation Study) |
| body limitation/failure cue | Tab. 4. A possible solution to mitigate this issue is to em- poloy iterative scene-specific optimization steps (Fu et al., 2023) or to assume ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Additionally, our approach also demonstrates superior pose estimation performance on both datasets, even surpassing (Hong et al., 2024) that trains its network with GT ... | p. 7 (4.3. Experimental Results) |
| body limitation/failure cue | In other words, we cannot train our approach on their dataset, nor can they train theirs on ours. *: We also include a MASt3R ... | p. 7 (4.3. Experimental Results) |
| body limitation/failure cue | We also demonstrate that without pre-trained weights for the depth and correspondence networks, the training either fails or achieves significantly lower performance. | p. 8 (4.4. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our model is trained on 4 NVIDIA A100 GPU for 50,000 iterations using the Adam optimizer (Kingma, 2014), with a learning rate set to ... | p. 5 (4.1. Implementation Details) |
| Finally, we provide the inference time of each of our components: overall inference time, UniDepth processing time, and decoder time. | p. 8 (4.5. Analysis and More Results) |
| The code and pretrained weights will be made publicly available. | p. 5 (4.1. Implementation Details) |
| PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting for Novel View Synthesis 𝒯pose 𝒯depth transformer encoder ×6 𝜙MLP Δ𝛿 𝐹 [∙] transformer encoder 𝐸pos ×6 sinusoidal ... | p. 6 (4.2. Experimental Setting) |
| Additionally, we compute a set of pixelaligned 3D Gaussians denoted as G = {µi, σi, Σi, ci}N i=1. | p. 3 (3.1. Problem Formulation) |
| Finally, the opacity is represented by σi(p) ∈[0, 1), Σi(p) ∈R3×3 is the covariance matrix, and the color is encoded using spherical harmonics ci(p) ... | p. 3 (3.1. Problem Formulation) |
| We define the process as following: Cagg i = Tagg(Cmulti i , Cguide i ), (3) where T (·) is a deep transformer architecture ... | p. 4 (3.2.4. 3D GAUSSIAN PARAMTER PREDICTIONS) |
| For each of the K depth candidates within specified near and far ranges along the epipolar lines, we compute matching scores using cosine similarity ... | p. 4 (3.2.4. 3D GAUSSIAN PARAMTER PREDICTIONS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5. Conclusion - extractive PDF cue:** Our framework, PFSplat, is built on foundation models to overcome inherent limitations of 3DGS.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Similar observations are made in (I-I), (I-II), and (I-V), where we identify that directly tuning the depth network or training only with photometric losses leads ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Tab. 4. A possible solution to mitigate this issue is to em- poloy iterative scene-specific optimization steps (Fu et al., 2023) or to assume ground-truth ...
- **p. 7 / 4.3. Experimental Results - extractive PDF cue:** Additionally, our approach also demonstrates superior pose estimation performance on both datasets, even surpassing (Hong et al., 2024) that trains its network with GT camera ...
- **p. 7 / 4.3. Experimental Results - extractive PDF cue:** In other words, we cannot train our approach on their dataset, nor can they train theirs on ours. *: We also include a MASt3R variant ...
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** We also demonstrate that without pre-trained weights for the depth and correspondence networks, the training either fails or achieves significantly lower performance.

- **PDF anchors reviewed:** datasets p. 5 (4.2. Experimental Setting), p. 5 (4.2. Experimental Setting), p. 7 (4.3. Experimental Results), p. 7 (4.3. Experimental Results), p. 6 (4.2. Experimental Setting), p. 9 (4.5. Analysis and More Results), metrics p. 7 (4.3. Experimental Results), p. 9 (4.5. Analysis and More Results), p. 7 (4.3. Experimental Results), p. 8 (4.5. Analysis and More Results), p. 8 (4.4. Ablation Study), p. 14 (Figure/Table caption), baselines p. 6 (4.3. Experimental Results), p. 7 (4.3. Experimental Results), p. 7 (4.3. Experimental Results), p. 8 (4.4. Ablation Study), p. 8 (4.5. Analysis and More Results), p. 9 (4.5. Analysis and More Results), results p. 9 (4.5. Analysis and More Results), p. 9 (4.5. Analysis and More Results), p. 8 (4.4. Ablation Study), p. 7 (4.3. Experimental Results), p. 6 (4.3. Experimental Results), p. 8 (4.4. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
