# Evaluation - IPoD: Implicit Field Learning with Point Diffusion for Generalizable 3D Object Reconstruction from Single RGB-D Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wu_IPoD_Implicit_Field_Learning_with_Point_Diffusion_for_Generalizable_3D_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_IPoD_Implicit_Field_Learning_with_Point_Diffusion_for_Generalizable_3D_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.3. Ablation Study), p. 5 (4. Experiments), p. 7 (4.3. Ablation Study), p. 5 (4. Experiments)): With PVCNN, our method improves the performance of the baseline PC2-depth by 19.2% on Chamfer distance and 7.8% on F-score.

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive body cue:** We test the zero-shot generalization ability of the proposed method on the dataset of MVImgNet [65], which is a real-world dataset with 220k object videos ...
- **p. 6 / 4.2. Results on MVImgNet - extractive body cue:** 4, our method can well generalize to more various categories of objects than in the CO3D-v2 dataset.
- **p. 5 / 4. Experiments - extractive body cue:** We also contribute a dataset with 100k cleaned point clouds from MVImgNet.
- **p. 6 / 4. Experiments - extractive body cue:** Results on CO3D-v2 We show the evaluation results of the proposed method on the CO3D-v2 dataset in Tab.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Notably, when addressing objects with Table 2.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Visualization of reconstructions by different methods on CO3D-v2 unseen categories.
- **p. 5 / 4. Experiments - extractive body cue:** The metrics can be divided into two groups for measuring (i) the absolute distance: the Chamfer distance (CD) and its two components that measure the ...
- **p. 6 / 4. Experiments - extractive body cue:** With PVCNN, our method improves the performance of the baseline PC2-depth by 19.2% on Chamfer distance and 7.8% on F-score.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.2. Results on MVImgNet (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | With PVCNN, our method improves the performance of the baseline PC2-depth by 19.2% on Chamfer distance and 7.8% on F-score. | p. 6 (4. Experiments) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Based on Transformer, our method achieves SOTA performance, which surpasses the previously best algorithm NU-MCC overall metrics, specifically by 28.6% on Chamfer distance (0.266→0.190) ... | p. 6 (4. Experiments) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Adding diffusion learning only into NU-MCC can bring an obvious improvement by absolute 4.9% on F-score (80.9%→85.8%), and further adding selfconditioning also makes a ... | p. 7 (4.3. Ablation Study) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The last one is NU-MCC [28] that improves MCC by proposing a Repulsive UDF to replace the occupancy field and applying anchor representations for ... | p. 5 (4. Experiments) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1 that the proposed self-conditioning mechanism can provide more accurate and useful information about the target shape to improve the noise prediction in point ... | p. 7 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive body cue:** We test the zero-shot generalization ability of the proposed method on the dataset of MVImgNet [65], which is a real-world dataset with 220k object videos ...
- **p. 6 / 4.2. Results on MVImgNet - extractive body cue:** 4, our method can well generalize to more various categories of objects than in the CO3D-v2 dataset.
- **p. 5 / 4. Experiments - extractive body cue:** We also contribute a dataset with 100k cleaned point clouds from MVImgNet.
- **p. 6 / 4. Experiments - extractive body cue:** Results on CO3D-v2 We show the evaluation results of the proposed method on the CO3D-v2 dataset in Tab.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Notably, when addressing objects with Table 2.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Visualization of reconstructions by different methods on CO3D-v2 unseen categories.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our work focuses on the task of generalizable 3D object reconstruction from a single RGB-D image. The proposed method conducts implicit field learning ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed method. The network takes a single-view image and a partial point cloud unprojected from the image according to the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. The UDF prediction ν′ is first computed and sent into the the other decoder. As ν′ ∈RN×1 provides point- wise information, we simply ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Illustration of the Transformer-based (upper part) and the PVCNN-based (lower part) implementations. ⊗denotes the affine operation. The yellow arrow with double lines indicate ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Results on CO3D-v2, averaged on all samples from 10 held-out categories. The best results are highlighted in bold font.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6. As shown, the proposed method can produce better generations than the baseline method (Ours1 v.s. PC2-depth and Ours2 v.s. NU-MCC) on both higher ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Visualization on MVImgNet data. Upper: generalization results by Ours2; Lower: the comparison of generalization results before and after fine-tuning on cleaned MVImgNet data. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Visualization of the denoising process (t={1000, 750, 500, 250, 0}) of our method in inferring. Note we only sample 2k points in each ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We test the zero-shot generalization ability of the proposed method on the dataset of MVImgNet [65], which is a real-world dataset with 220k object ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 6 (4.2. Results on MVImgNet) |
| Task/environment | 4, our method can well generalize to more various categories of objects than in the CO3D-v2 dataset. | reset, timeout, object/scene variation | p. 6 (4.2. Results on MVImgNet), p. 5 (4. Experiments) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3.1. Preliminary), p. 4 (3.1. Preliminary) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (3.2. Implicit Field Learning with Point Diffusion), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The metrics can be divided into two groups for measuring (i) the absolute distance: the Chamfer distance (CD) and its two components that measure ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| With PVCNN, our method improves the performance of the baseline PC2-depth by 19.2% on Chamfer distance and 7.8% on F-score. | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Based on Transformer, our method achieves SOTA performance, which surpasses the previously best algorithm NU-MCC overall metrics, specifically by 28.6% on Chamfer distance (0.266→0.190) ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Individual impact To analyze the impact of the three components above, we evaluate the precision, recall, and F-score of each variant. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Among them, F1 holds the dominant since both accuracy and completeness are considered. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Using f X0 results in a worse Fscore than using occupancy values, but better than not using. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Baselines We compare the proposed method with four baselines. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Another baseline is MCC [61] which is implemented with a Transformer-based encoder-decoder, which conducts implicit learning based on an occupancy field. | comparison identity and matched condition | p. 5 (4. Experiments) |
| As shown, the proposed method can produce better generations than the baseline method (Ours1 v.s. | comparison identity and matched condition | p. 6 (4. Experiments) |
| With PVCNN, our method improves the performance of the baseline PC2-depth by 19.2% on Chamfer distance and 7.8% on F-score. | comparison identity and matched condition | p. 6 (4. Experiments) |
| Figure 1. Our work focuses on the task of generalizable 3D object reconstruction from a single RGB-D image. The proposed method conducts implicit field ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Individual impact To analyze the impact of the three components above, we evaluate the precision, recall, and F-score of each variant. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| We hire annotators to manually filter the 3D annotations with low quality and remove the background noise caused by COLMAP estimation for the rest ... | component/input/data sensitivity | p. 5 (4. Experiments) |
| Results of using different variants of self-condition. "None" denotes not using any self-conditioning. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| Figure 3. Illustration of the Transformer-based (upper part) and the PVCNN-based (lower part) implementations. ⊗denotes the affine operation. The yellow arrow with double lines ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Note that the categories in the cleaned data for fine-tuning have no overlap with the ones for evaluation. | component/input/data sensitivity | p. 6 (4.2. Results on MVImgNet) |
| We further use the cleaned MVImgNet point clouds to fine-tune the network and found that the generations are endowed with higher accuracy, which indicates ... | component/input/data sensitivity | p. 6 (4.2. Results on MVImgNet) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our key contributions are as follows: • We propose IPoD that conducts implicit field learning with point diffusion for generalizable 3D object ... | With PVCNN, our method improves the performance of the baseline PC2-depth by 19.2% on Chamfer distance and 7.8% on F-score. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.3. Ablation Study), p. 5 (4. Experiments), p. 7 (4.3. Ablation Study), p. 5 (4. Experiments) |
| Primary metric/result | Based on Transformer, our method achieves SOTA performance, which surpasses the previously best algorithm NU-MCC overall metrics, specifically by 28.6% on Chamfer distance (0.266→0.190) ... | numeric claim only at cited anchor | p. 6 (4. Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive body cue:** It consists of around 37k videos of 51 object categories, of which 10 are held out for evaluation and the remaining 41 for training.
- **p. 5 / 4. Experiments - extractive body cue:** Note that videos of MVImgNet are captured in N×3 Embed N×e t Embed scale shift Linear 1×e' 𝑋𝑋𝑡𝑡 N×e Linear P (M+N)×d 𝐸𝐸𝑋𝑋 I M×3 ...
- **p. 6 / 4. Experiments - extractive body cue:** Method Backbone Acc↓ Comp↓ CD↓ Prec↑ Recall↑ F1↑ PC2 [35] PVCNN 0.342 0.214 0.556 24.2 56.2 33.0 PC2-depth PVCNN 0.209 0.103 0.312 61.7 87.6 70.7 ...
- **p. 6 / 4. Experiments - extractive body cue:** Besides, T is set as 1,000 in our diffusion model, λ=1.0 in training, and N=50k, the distance threshold ρ=0.1 for evaluation.
- **p. 6 / 4. Experiments - extractive body cue:** Our model is trained with a batch size of 64 for 100 epochs (taking around 48 hours on NVIDIA V100 GPUs), and an Adam [24] ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations We have not validated the effectiveness of our method on 3D human and scene reconstruction. | p. 8 (5. Conclusion) |
| body limitation/failure cue | We also develop a self-conditioning mechanism to leverage implicit predictions to reversely assist the noise estimation in diffusion learning, which eventually forges a cooperative ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 1. Our work focuses on the task of generalizable 3D object reconstruction from a single RGB-D image. The proposed method conducts implicit field ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | In CO3D-v2, the object shape annotations are obtained via COLMAP [50, 51] and thus inevitably contain noise and voids. | p. 5 (4. Experiments) |
| body limitation/failure cue | We hire annotators to manually filter the 3D annotations with low quality and remove the background noise caused by COLMAP estimation for the rest ... | p. 5 (4. Experiments) |
| body limitation/failure cue | 5), the noise in point clouds can not be perfectly diminished. | p. 7 (4.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our model is trained with a batch size of 64 for 100 epochs (taking around 48 hours on NVIDIA V100 GPUs), and an Adam ... | p. 6 (4. Experiments) |
| Illustration of the Transformer-based (upper part) and the PVCNN-based (lower part) implementations. ⊗denotes the affine operation. | p. 5 (4. Experiments) |
| Another baseline is MCC [61] which is implemented with a Transformer-based encoder-decoder, which conducts implicit learning based on an occupancy field. | p. 5 (4. Experiments) |
| See supplementary materials for more model architecture details of PVCNN-based and Transformer-based implementations. | p. 6 (4. Experiments) |
| The whole denoising process with 1k steps in inferring is evenly divided into four stages. | p. 7 (4.3. Ablation Study) |
| The UDF prediction ν′ is first computed and sent into the the other decoder, 20435 | p. 4 (3.2. Implicit Field Learning with Point Diffusion) |
| In the Transformer-based implementation, we employ the similar anchor prediction operation following NU-MCC [28], which further encode the features of I and P into ... | p. 4 (3.2. Implicit Field Learning with Point Diffusion) |
| The noising stepsize in the diffusion process is defined by a variance schedule {βt}T t=0: q(X_t/X_ { t-1}) | p. 3 (3.1. Preliminary) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** Limitations We have not validated the effectiveness of our method on 3D human and scene reconstruction.
- **p. 8 / 5. Conclusion - extractive body cue:** We also develop a self-conditioning mechanism to leverage implicit predictions to reversely assist the noise estimation in diffusion learning, which eventually forges a cooperative system.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our work focuses on the task of generalizable 3D object reconstruction from a single RGB-D image. The proposed method conducts implicit field learning ...
- **p. 5 / 4. Experiments - extractive body cue:** In CO3D-v2, the object shape annotations are obtained via COLMAP [50, 51] and thus inevitably contain noise and voids.
- **p. 5 / 4. Experiments - extractive body cue:** We hire annotators to manually filter the 3D annotations with low quality and remove the background noise caused by COLMAP estimation for the rest of ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** 5), the noise in point clouds can not be perfectly diminished.

- **Evidence anchors reviewed:** datasets p. 5 (4. Experiments), p. 6 (4.2. Results on MVImgNet), p. 5 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), metrics p. 5 (4. Experiments), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.3. Ablation Study), p. 5 (4. Experiments), p. 7 (4.3. Ablation Study), baselines p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 1 (Figure/Table caption), results p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.3. Ablation Study), p. 5 (4. Experiments), p. 7 (4.3. Ablation Study), p. 5 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
