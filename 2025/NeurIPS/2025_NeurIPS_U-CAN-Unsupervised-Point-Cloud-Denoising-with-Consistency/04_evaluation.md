# Evaluation - U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=hVFtXE19Me; PDF retrieval source: https://arxiv.org/pdf/2510.25210. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments)): 3, where our method significantly outperforms DMR-TTD and ScoreDenoise-TTD, and also achieve better performance than the supervised method PU-Net designed for the upsampling task.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** 4.2 Point Cloud Denoising on Scanned Data For demonstrating the capability of U-CAN to handle real-world point cloud noises, we conduct evaluations under the Paris-rue-Madame ...
- **p. 6 / 4 Experiments - extractive body cue:** We split the dataset into training and testing sets with the same setting as ScoreDenoise [29].
- **p. 8 / 4 Experiments - extractive body cue:** For evaluating in the image denoising task, we follow ZS-N2N [32] to conduct experiments under the McMaster18 dataset [22].
- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Point Cloud Denoising on Synthetic Data Dataset and Metrics.
- **p. 7 / 4 Experiments - extractive body cue:** Noisy Points PCN DMR-TTD ScoreDenoise-TTD U-CAN (Ours) Noisy Points Denoised Points by U-CAN Figure 5: Denoising on the real scans under Paris-rue-Madame dataset.
- **p. 9 / 4 Experiments - extractive body cue:** We follow ScoreDenoise [29] to conduct the point cloud upsampling experiments under the PU-Net dataset.
- **p. 9 / 4 Experiments - extractive body cue:** Sparse DMR-TTD ScoreD-TTD Ours Dense Figure 7: Visual Comparison under PU-Net. #Points 5K 10K CD P2M CD P2M PU-Net [56] 3.445 1.669 2.862 1.166 ScoreDenoise ...
- **p. 7 / 4 Experiments - extractive body cue:** Top: The visualization of the noisy points and denoised points obtained by U-CAN under the whole scene.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3, where our method significantly outperforms DMR-TTD and ScoreDenoise-TTD, and also achieve better performance than the supervised method PU-Net designed for the upsampling task. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As presented, our model significantly outperforms previous unsupervised denoising methods, especially for noises with large variances, and can even rival the results of supervised ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Specifically, by introducing the proposed denoising consistency constraint into ZS-N2N, we achieve significant improvements of nearly 1 dB over the baseline ZS-N2N. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In particular, at the 10K resolution and under noise levels of 2% and 3%, our method outperforms all other supervised and unsupervised methods in ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the scene in the top row, our method demonstrates a marked improvement over the other compared methods, particularly around complex structures like trees ... | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** 4.2 Point Cloud Denoising on Scanned Data For demonstrating the capability of U-CAN to handle real-world point cloud noises, we conduct evaluations under the Paris-rue-Madame ...
- **p. 6 / 4 Experiments - extractive body cue:** We split the dataset into training and testing sets with the same setting as ScoreDenoise [29].
- **p. 8 / 4 Experiments - extractive body cue:** For evaluating in the image denoising task, we follow ZS-N2N [32] to conduct experiments under the McMaster18 dataset [22].
- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Point Cloud Denoising on Synthetic Data Dataset and Metrics.
- **p. 7 / 4 Experiments - extractive body cue:** Noisy Points PCN DMR-TTD ScoreDenoise-TTD U-CAN (Ours) Noisy Points Denoised Points by U-CAN Figure 5: Denoising on the real scans under Paris-rue-Madame dataset.
- **p. 9 / 4 Experiments - extractive body cue:** We follow ScoreDenoise [29] to conduct the point cloud upsampling experiments under the PU-Net dataset.
- **p. 9 / 4 Experiments - extractive body cue:** Sparse DMR-TTD ScoreD-TTD Ours Dense Figure 7: Visual Comparison under PU-Net. #Points 5K 10K CD P2M CD P2M PU-Net [56] 3.445 1.669 2.862 1.166 ScoreDenoise ...
- **p. 7 / 4 Experiments - extractive body cue:** Top: The visualization of the noisy points and denoised points obtained by U-CAN under the whole scene.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Overview of our method. (a) We design a multi-step denoising framework to gradually filter the noisy point cloud. (b) We introduce a novel ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Illustrations on the effect of proposed constraint on denoising consistency. The noise errors indicate the Chamfer distance between the denoised and the clean ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Transferring the denoising consistency constraint of U-CAN to the unsupervised image denoising. We provide an illustration as shown in Fig. 2 to show ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Denoising comparisons under PUNet dataset. CD×104 and P2M ×104.The best results under the unsupervised (Un-Sup) point cloud denoising setting are highlighted. Point Number ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Visual comparisons under PUNet dataset. The noise errors at each point is shown in color, where the points closer to the ground truth ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Denoising on the real scans under Paris-rue-Madame dataset. Top: The visualization of the noisy points and denoised points obtained by U-CAN under the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Visual comparison of unsupervised image denoising under McMaster18 dataset. 4.2 Point Cloud Denoising on Scanned Data For demonstrating the capability of U-CAN to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Unsupervised image denoising under Mc- Master18 dataset. The PSNR scores in dB are reported. Best results are marked in bold and the second-best ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.2 Point Cloud Denoising on Scanned Data For demonstrating the capability of U-CAN to handle real-world point cloud noises, we conduct evaluations under the ... | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 6 (4 Experiments) |
| Task/environment | We split the dataset into training and testing sets with the same setting as ScoreDenoise [29]. | reset, timeout, object/scene variation | p. 6 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (Abstract), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| This includes classic optimizationbased methods such as Bilateral [10], Jet [5], MRPCA [34], GLR [58]; supervised learning-based methods like PCNet [42], GPDNet [38], DMR ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| 3, where our method significantly outperforms DMR-TTD and ScoreDenoise-TTD, and also achieve better performance than the supervised method PU-Net designed for the upsampling task. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| We further apply the adaption from denoising to upsampling to the state-of-the-art unsupervised point cloud denoising methods DMR-TTD and ScoreDenoise-TTD and report their upsampling ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| We split the dataset into training and testing sets with the same setting as ScoreDenoise [29]. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| For the experiments on synthetic shapes, we follow ScoreDenoise [29] to train our network on the PUNet [56] dataset. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| The PSNR scores in dB are reported. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Figure 2: Illustrations on the effect of proposed constraint on denoising consistency. The noise errors indicate the Chamfer distance between the denoised and the ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We provide the visual comparison among the state-of-the-art supervised and unsupervised point cloud denoising methods in Fig. | comparison identity and matched condition | p. 7 (4 Experiments) |
| We evaluate the performance of U-CAN and other baselines under the commonly used metrics L2 Chamfer distance (CD) and the point-to-mesh distance (P2M), following ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| The denoised images of U-CAN are more accurate and with more details than previous state-of-the-art methods. | comparison identity and matched condition | p. 8 (4 Experiments) |
| 2, where the denoising consistency constraint demonstrates superior performance compared to the previous methods. | comparison identity and matched condition | p. 8 (4 Experiments) |
| 3, where our method significantly outperforms DMR-TTD and ScoreDenoise-TTD, and also achieve better performance than the supervised method PU-Net designed for the upsampling task. | comparison identity and matched condition | p. 9 (4 Experiments) |
| We further apply the adaption from denoising to upsampling to the state-of-the-art unsupervised point cloud denoising methods DMR-TTD and ScoreDenoise-TTD and report their upsampling ... | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without LDC, performance significantly drops (e.g., CD Table 4: Ablation studies on the framework and loss designs. | component/input/data sensitivity | p. 9 (4 Experiments) |
| To justify the effectiveness of constraint LDC, we remove it and vary the underlying distance metric. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Traditional optimization-based point cloud denoising methods rely heavily on geometric priors to inform their smoothing algorithms and show increased sensitivity to noises with unseen ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| We directly leverage the U-CAN model trained on PUNet dataset for evaluating, without requiring extra training. | component/input/data sensitivity | p. 8 (4 Experiments) |
| Figure 2: Illustrations on the effect of proposed constraint on denoising consistency. The noise errors indicate the Chamfer distance between the denoised and the ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural ... | 3, where our method significantly outperforms DMR-TTD and ScoreDenoise-TTD, and also achieve better performance than the supervised method PU-Net designed for the upsampling task. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | As presented, our model significantly outperforms previous unsupervised denoising methods, especially for noises with large variances, and can even rival the results of supervised ... | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Point Cloud Denoising on Synthetic Data Dataset and Metrics.
- **p. 8 / 4 Experiments - extractive body cue:** 4.2 Point Cloud Denoising on Scanned Data For demonstrating the capability of U-CAN to handle real-world point cloud noises, we conduct evaluations under the Paris-rue-Madame ...
- **p. 9 / 4 Experiments - extractive body cue:** 4.4 Point Upsampling via Denoising Implementation.
- **p. 9 / 4 Experiments - extractive body cue:** Dataset: PU 10K, 1% 10K, 2% 10K, 3% Ablation CD P2M CD P2M CD P2M 1 step 2.676 1.046 3.903 1.700 5.251 2.720 2 steps ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal ... | p. 7 (4 Experiments) |
| body limitation/failure cue | For unsupervised denoising, the TTD [14] fails to produce high-fidelity local geometries with only the global constraints. | p. 7 (4 Experiments) |
| body limitation/failure cue | Note that U-CAN does not require (1) sparse-to-dense point cloud pairs and (2) clean point clouds, where the only required data is the noise ... | p. 9 (4 Experiments) |
| body limitation/failure cue | Figure 1: Overview of our method. (a) We design a multi-step denoising framework to gradually filter the noisy point cloud. (b) We introduce a ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Illustrations on the effect of proposed constraint on denoising consistency. The noise errors indicate the Chamfer distance between the denoised and the ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | We split the dataset into training and testing sets with the same setting as ScoreDenoise [29]. | p. 6 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.4 Point Upsampling via Denoising Implementation. | p. 9 (4 Experiments) |
| Dataset: PU 10K, 1% 10K, 2% 10K, 3% Ablation CD P2M CD P2M CD P2M 1 step 2.676 1.046 3.903 1.700 5.251 2.720 2 ... | p. 9 (4 Experiments) |
| 3D point clouds have been a fundamental representation in 3D computer vision and play a key role in autonomous driving [15], augmented/virtual reality [59] ... | p. 1 (1 Introduction) |
| U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching Junsheng Zhou1∗ Xingyu Shi1∗ Haichuan Song2† Yi Fang3 Yu-Shen Liu1† Zhizhong Han4 School of Software, ... | p. 1 (Body text (section not recovered)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4 Experiments - extractive body cue:** The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance ...
- **p. 7 / 4 Experiments - extractive body cue:** For unsupervised denoising, the TTD [14] fails to produce high-fidelity local geometries with only the global constraints.
- **p. 9 / 4 Experiments - extractive body cue:** Note that U-CAN does not require (1) sparse-to-dense point cloud pairs and (2) clean point clouds, where the only required data is the noise point ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Overview of our method. (a) We design a multi-step denoising framework to gradually filter the noisy point cloud. (b) We introduce a novel ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Illustrations on the effect of proposed constraint on denoising consistency. The noise errors indicate the Chamfer distance between the denoised and the clean ...
- **p. 6 / 4 Experiments - extractive body cue:** We split the dataset into training and testing sets with the same setting as ScoreDenoise [29].

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), metrics p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), baselines p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), results p. 9 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
