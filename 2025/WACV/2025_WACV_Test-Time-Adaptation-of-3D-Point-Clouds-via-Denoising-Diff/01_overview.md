# Test-Time Adaptation of 3D Point Clouds via Denoising Diffusion Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Dastmalchi_Test-Time_Adaptation_of_3D_Point_Clouds_via_Denoising_Diffusion_Models_WACV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Dastmalchi_Test-Time_Adaptation_of_3D_Point_Clouds_via_Denoising_Diffusion_Models_WACV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / WACV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/WACV2025/html/Dastmalchi_Test-Time_Adaptation_of_3D_Point_Clouds_via_Denoising_Diffusion_Models_WACV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/WACV2025/papers/Dastmalchi_Test-Time_Adaptation_of_3D_Point_Clouds_via_Denoising_Diffusion_Models_WACV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 While this approach has proven effective for 2D images [9,26,39,43], applying it to 3D point clouds presents a far greater challenge due to the unstructured nature of point clouds and the inherent ...를 문제로 두고, To this end, we introduce a novel, training-free test-time adaptation method called 3D Denoising Diffusion TestTime Adaptation (3DD-TTA).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Test-time adaptation (TTA) of 3D point clouds is crucial for mitigating discrepancies between training and testing samples in real-world scenarios, particularly when handling corrupted point ...
- **p. 1 / Abstract - extractive body cue:** LiDAR data, for instance, can be affected by sensor failures or environmental factors, causing domain gaps.
- **p. 1 / Abstract - extractive body cue:** Adapting models to these distribution shifts online is crucial, as training for every possible variation is impractical.
- **p. 1 / Abstract - extractive body cue:** Existing methods often focus on fine-tuning pre-trained models based on self-supervised learning or pseudo-labeling, which can lead to forgetting valuable source domain knowledge over time ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a novel 3D test-time adaptation method, termed 3DD-TTA, which stands for 3D Denoising Diffusion Test-Time Adaptation.
- **p. 2 / 1. Introduction - extractive body cue:** While this approach has proven effective for 2D images [9,26,39,43], applying it to 3D point clouds presents a far greater challenge due to the unstructured ...
- **p. 1 / 1. Introduction - extractive body cue:** For example, LiDAR point cloud data may be compromised by sensor failures or environmental factors, creating a domain gap that could lead to decreased performance.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce a novel, training-free test-time adaptation method called 3D Denoising Diffusion TestTime Adaptation (3DD-TTA).
- **p. 2 / 1. Introduction - extractive body cue:** (3) We introduced a modified Chamfer distance, named Selective Chamfer Distance (SCD), to increase the fidelity during the reverse diffusion process.
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** We introduce and employ the gradient of the Selective Chamfer distance (SCD) denoted as lλ cd, with respect to htw-1 as the regularization term: R ...
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** Additionally, given that the initial shape latent z0, obtained from the input point cloud, potentially leads to inaccurate guidance for the denoising network, we propose ...
- **p. 4 / 3.1. Preliminaries - extractive body cue:** In the first stage, the encoders and the decoder are simultaneously trained to maximize the variational lower bound over the data log-likelihood: LELBO = Ep(x),qz(z0/x),qh(h0/x,z0) ...
- **p. 4 / 3.1. Preliminaries - extractive body cue:** The LION model leverages a VAE network composed of two hierarchical encoders and one decoder.
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** Shape Latent Encoder 𝑞𝑧 Latent Point Encoder 𝑞ℎ Decoder 𝑝𝑑 Denoising Diffusion Network tw + 𝐳0 𝐡tw 𝐡𝟎 𝐫 𝛆 ෤𝐱 𝐱 𝐡0 ∇𝐡tlcd λ ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Similarly, the generative process is modeled as a Gaussian transition with a learned 1568

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Additionally, given that the initial shape latent z0, obtained from the input point cloud, potentially leads to inaccurate guidance for the denoising network, we propose an adjustment over the shape latent using ... | conditioning observation와 noisy/intermediate sample | p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 4 (3.1. Preliminaries) |
| State/latent | Additionally, given, initial, shape, latent, obtained, input, point, cloud, potentially, leads, inaccurate | latent/noise variable와 conditional distribution | p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 4 (3.1. Preliminaries), p. 4 (3.1. Preliminaries) |
| Output/action | Finally, the decoder denoted by pd(x/z0, h0) takes the shape latent and latent points as inputs and maps them back to the point cloud. | generated sample, action chunk 또는 trajectory | p. 4 (3.1. Preliminaries), p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method) |
| Objective/outcome | In the second stage, the two latent diffusion models are trained on the encodings z0 and h0 sampled from qz(z0/x) and qh(h0/z0, x), minimizing the following loss functions: LSMz = Et,ϵ,p(x),qz(z0/x) ∥ϵ ... | distribution fit, multimodality, sample quality와 latency | p. 4 (3.1. Preliminaries), p. 4 (3.2. Model Overview), p. 5 (3.3. Denoising Diffusion-based Adaption Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce a novel, training-free test-time adaptation method called 3D Denoising Diffusion TestTime Adaptation (3DD-TTA).
- **p. 2 / 1. Introduction - extractive body cue:** (3) We introduced a modified Chamfer distance, named Selective Chamfer Distance (SCD), to increase the fidelity during the reverse diffusion process.
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** We introduce and employ the gradient of the Selective Chamfer distance (SCD) denoted as lλ cd, with respect to htw-1 as the regularization term: R ...
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** Additionally, given that the initial shape latent z0, obtained from the input point cloud, potentially leads to inaccurate guidance for the denoising network, we propose ...
- **p. 6 / 4.3. Results - extractive body cue:** In addition, our 3DD-TTA outperforms other TTA frameworks on density-based corruptions such as cut-out and density increase.
- **p. 6 / 4.3. Results - extractive body cue:** The table clearly shows that the 3DD-TTA method outperforms the other methods by a significant margin in most corruption types.
- **p. 7 / 4.3. Results - extractive body cue:** 3DD-TTA boosts Point-MAE (source) in most corruption types, showing improved robustness across different corruptions.
- **p. 7 / 4.3. Results - extractive body cue:** Similarly, the model outperforms other methods in addressing densityrelated corruptions but is less effective for transformationbased corruptions, ranking second or third for these deformations.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.3. Results), p. 6 (4.3. Results) |
| Embodiment/environment | ScanObjectNN-c: ScanObjectNN [44], a real-world point cloud dataset with 15 categories, is corrupted using the same open-source code as ModelNet40-c [40], introducing 15 corruptions into the test set. | hardware/simulator version and reset protocol | p. 6 (4.1. Datasets and Corruption Methods), p. 7 (4.3. Results) |
| Dataset/benchmark | We refer to this dataset as ScanObjectNN-c. | role, split, size and leakage | p. 6 (4.1. Datasets and Corruption Methods), p. 7 (4.3. Results), p. 6 (4.1. Datasets and Corruption Methods), p. 7 (4.3. Results) |
| Metric | Notably, 3DD-TTA dramatically boosts the source classifier's performance on background noise, raising accuracy from 15.0% to 77.6%. | definition, denominator, direction and uncertainty | p. 6 (4.3. Results), p. 7 (4.3. Results), p. 8 (4.4. Ablation Study) |
| Baseline/ablation | In addition, our 3DD-TTA outperforms other TTA frameworks on density-based corruptions such as cut-out and density increase. | fair input/data/compute/action matching | p. 6 (4.3. Results), p. 6 (4.3. Results), p. 7 (4.3. Results) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Reconstruction of corrupted point clouds using the pro- posed 3DD-TTA method. between training and testing samples is minimal. However, real-world scenarios often feature ...
- **p. 6 / 4.3. Results - extractive body cue:** However, the model faces limitations in addressing the transformation-based deformations like shear and rotation.
- **p. 6 / 4.3. Results - extractive body cue:** This limitation is due to the trainingfree nature of the model, making it challenging to reverse transformations to their original shape without additional training.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Limitation: Our model performs well with just five denoising steps for most types of corruption, making it efficient and suitable for time-sensitive applications.
- **p. 8 / 5. Conclusion - extractive body cue:** Incorporating the proposed updating strategy based on the gradient of the Selective Chamfer Distance (SCD) ensures the generation of highfidelity, noise-free test samples.
- **p. 7 / 4.3. Results - extractive body cue:** We also conducted experiments on the corrupted version of the real-world ScanObjectNN dataset [44], which inherently suffers from noise, background issues, and occlusion.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. In the TTA setting, the source model encounters corrupted 3D point clouds with an unknown distribution shift, requiring adaptation without prior knowledge of ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 While this approach has proven effective for 2D images [9,26,39,43], applying it to 3D point clouds presents a far greater challenge due to the unstructured nature of point clouds and the inherent ...를 문제로 두고, To this end, we introduce a novel, training-free test-time adaptation method called 3D Denoising Diffusion TestTime Adaptation (3DD-TTA).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
