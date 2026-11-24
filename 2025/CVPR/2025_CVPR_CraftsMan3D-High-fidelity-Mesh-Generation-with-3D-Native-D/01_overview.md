# CraftsMan3D: High-fidelity Mesh Generation with 3D Native Diffusion and Interactive Geometry Refiner

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Weiyu Li, Jiarui Liu, Hongyu Yan, Rui Chen, Yixun Liang, Xuelin Chen, Ping Tan, Xiaoxiao Long
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf)

## Why This Paper Is Here

CraftsMan3D는 초기 메시 생성과 국소 기하 정제를 나눠 영상으로부터 물체 형상을 만들고 사용자가 세부 형상을 수정할 수 있게 한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a novel generative 3D modeling system, coined CraftsMan3D, which can generate high-fidelity 3D geometries with highly varied shapes, detailed surfaces, and, notably, allows ...
- **p. 1 / Abstract - extractive body cue:** Despite the significant advancements in 3D generation, existing methods still struggle with lengthy optimization processes, self-occlusion, irregular mesh topologies, and difficulties in accommodating user editing, ...
- **p. 1 / Abstract - extractive body cue:** Our work is inspired by the craftsman, who usually roughs out the holistic figure of the work first and elaborates the surface details subsequently.
- **p. 1 / Abstract - extractive body cue:** Specifically, we first introduce a robust data preprocessing pipeline that utilizes visibility check and winding mumber to maximize the use of existing 3D data.
- **p. 1 / Abstract - extractive body cue:** Leveraging this data, we employ a 3D-native DiT model that directly models the distribution of 3D data in latent space, generating coarse geometries in seconds.
- **p. 2 / 1. Introduction - extractive body cue:** However, none of these methods can generate high-fidelity geometric details and limitations in mesh-to-SDF conversions still result in training difficulty.
- **p. 1 / 1. Introduction - extractive body cue:** However, existing methods still struggle to produce results that are ready to use.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Built on the 3D data, we present a two-stage generative 3D native generation system, coined CraftsMan, which takes as input single images as reference or ...
- **p. 3 / 3. Method - extractive body cue:** Finally, our framework features a normal map-based geometry refinement scheme (Sec.3.3).
- **p. 3 / 3.1. Data Preprocessing - extractive body cue:** Therefore, we propose an efficient and effective method for converting mesh into a watertight one.
- **p. 5 / 3.3. Normal-based Geometry Refinement - extractive body cue:** To further enhance the coarse mesh, we propose to improve the initial mesh using normal maps as an intermediate representation.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contribution lies in three aspects: • A robust and efficient data pre-processing pipeline that integrates visibility checks enhanced by the winding ...
- **p. 4 / 3.2. Multi-view guided 3D generation model - extractive body cue:** The encoder is trained to map points Pc and Pn into a latent vector set Z, which a decoder then translates into an implicit field ...
- **p. 5 / 3.2. Multi-view guided 3D generation model - extractive body cue:** (a.) We first train a 3D Variational Autoencoder (VAE) to compress 3D shape into a latent space, which takes point clouds with normals as input ...
- **p. 4 / 3.1. Data Preprocessing - extractive body cue:** The generated multi-view image is then fed into our Latent Set-based DiT model as conditioning to produce a coarse mesh.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (a.) We first train a 3D Variational Autoencoder (VAE) to compress 3D shape into a latent space, which takes point clouds with normals as input and outputs TSDF fields. | conditioning observation와 noisy/intermediate sample | p. 5 (3.2. Multi-view guided 3D generation model), p. 4 (3.1. Data Preprocessing) |
| State/latent | first, train, Variational, Autoencoder, VAE, compress, shape, latent, space, takes, point, clouds | latent/noise variable와 conditional distribution | p. 5 (3.2. Multi-view guided 3D generation model), p. 4 (3.1. Data Preprocessing), p. 4 (3.1. Data Preprocessing) |
| Output/action | When the input point cloud has well-defined normals, the winding number can reliably differentiate between the inside and outside in a global manner. | generated sample, action chunk 또는 trajectory | p. 4 (3.1. Data Preprocessing), p. 4 (3.1. Data Preprocessing), p. 5 (3.3. Normal-based Geometry Refinement) |
| Objective/outcome | In each step, an update operation is executed to update the position for each vertex according to the gradient computed in the loss backward process. | distribution fit, multimodality, sample quality와 latency | p. 5 (3.3. Normal-based Geometry Refinement), p. 3 (3. Method), p. 4 (3.1. Data Preprocessing) |

## Main Claims and Actual Contribution

- 가시성과 감김수로 훈련용 메시의 내부·외부 판정을 보완하고 3D 잠재 표현에서 확산 트랜스포머로 초기 형상을 생성한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf#page=5)
- 여러 시점의 표면 법선을 이용해 메시의 기하를 정제하고 초기 결과와의 차이 및 사용자 편집 예를 제시했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.4. Ablation Study), p. 8 (4.3. Evaluation of Mesh Refinement) |
| Embodiment/environment | Additional details, including dataset, training settings can be found in our supplementary. | hardware/simulator version and reset protocol | p. 6 (4.1. Implementation Details), p. 7 (4.2. Evaluation of Mesh Generation) |
| Dataset/benchmark | We selected 20 objects from the Objaverse dataset and employed the same text descriptions as guidance. | role, split, size and leakage | p. 6 (4.1. Implementation Details), p. 7 (4.2. Evaluation of Mesh Generation), p. 8 (4.3. Evaluation of Mesh Refinement), p. 7 (4.2. Evaluation of Mesh Generation) |
| Metric | To demonstrate the superiority of our design in the context of multi-view images with camera pose injection, we conducted a comparison on our selected subset, which evaluated by the metrics of Chamfer ... | definition, denominator, direction and uncertainty | p. 8 (4.4. Ablation Study), p. 7 (4.2. Evaluation of Mesh Generation), p. 8 (4.2. Evaluation of Mesh Generation) |
| Baseline/ablation | We present the qualitative and quantitative evaluation of our method as described in Section 4.2 and Section 3.3, as well as comparison results against other baseline methods, showing the effectiveness and efficiency ... | fair input/data/compute/action matching | p. 6 (4. Experiments), p. 7 (4.1. Implementation Details), p. 7 (4.1. Implementation Details) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Error maps of different mesh-to-sdf methods. We sample surface points from the processed meshes for each method and show the differences compared to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison on subset which contained self- occlusion in the input images. Our 3D generative model demon- strated a significant performance.
- **p. 7 / 4.2. Evaluation of Mesh Generation - extractive body cue:** We notice that the distribution of the GSO dataset is kind of monotonous,lacking mesh with complex structures and self occlusion, which is exactly where our ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Our proposed regularization terms eliminate the global distortions introduced in the detail enhancement process by normal stable diffusion, constraint the vertices towards the proximity of ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Multi-view guided 3D generation model), p. 5 (3.2. Multi-view guided 3D generation model), p. 4 (3.1. Data Preprocessing)이다.
