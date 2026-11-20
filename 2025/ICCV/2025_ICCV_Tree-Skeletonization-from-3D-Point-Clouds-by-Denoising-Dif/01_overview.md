# Tree Skeletonization from 3D Point Clouds by Denoising Diffusion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Elias Ariel Marks, Lucas Nunes, Federico Magistri, Matteo Sodano, Rodrigo Marcuzzi, Lars Zimmermann, Jens Behley, Cyrill Stachniss
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 The world around us is filled with natural structures, such as trees, that humans can interpret even when parts of them are occluded; however, this remains a challenge for computer vision systems.를 문제로 두고, In summary, our key contributions are: • A tree skeletonization approach using 3D point clouds as input that employs a novel diffusion-based formulation for generating an implicit representation of a graphlike structure ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The natural world presents complex organic structures, such as tree canopies, that humans can interpret even when only partially visible.
- **p. 1 / Abstract - extractive body cue:** Understanding tree structures is key for forest monitoring, orchard management, and automated harvesting applications.
- **p. 1 / Abstract - extractive body cue:** However, reconstructing tree topologies from sensor data, called tree skeletonization, remains a challenge for computer vision approaches.
- **p. 1 / Abstract - extractive body cue:** Traditional methods for tree skeletonization rely on handcrafted features, regression, or generative models, whereas recent advances focus on deep learning approaches.
- **p. 1 / Abstract - extractive body cue:** Existing methods often struggle with occlusions caused by dense foliage, limiting their applicability over the annual vegetation cycle.
- **p. 1 / 1. Introduction - extractive body cue:** The world around us is filled with natural structures, such as trees, that humans can interpret even when parts of them are occluded; however, this ...
- **p. 2 / 1. Introduction - extractive body cue:** One major limiting factor in the development of tree skeletonization methods is the lack of real-world reference data for evaluating developed methods.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions are: • A tree skeletonization approach using 3D point clouds as input that employs a novel diffusion-based formulation for generating ...
- **p. 1 / 1. Introduction - extractive body cue:** Tree skeletonization consists of inferring from sensor data the graph representing the medial axes of the trunk, branches, and twigs, collectively referred to as branches, ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose a method for estimating skeletons from 3D point cloud data of trees with dense foliage, leveraging a denoising diffusion probabilistic ...
- **p. 3 / 3. Our Approach - extractive body cue:** To this end, we propose a tree skeletonization method based on a denoising diffusion probabilistic model (DDPM) that outputs a tree skeleton based on an ...
- **p. 4 / 3. Our Approach - extractive body cue:** In the following, we first describe the DDPM formulation and then we present our formulation to adapt it to the tree skeletonization task.
- **원문 대조:** Noisy input x^t, timestep t, 조건 c를 이용해 주입한 Gaussian noise ε를 예측하고 squared L2 오차로 학습한다. Classifier-free guidance 학습에서는 Bernoulli mask로 조건을 비우는 경우를 포함한다. ([PDF p. 4](https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf#page=4), §3.1, Eq. (5)).
- **p. 4 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** In our case, we use the classifier-free guidance since it does not require a pre-trained encoder.
- **p. 5 / 3.2. Diffusion tree skeletonization - extractive body cue:** (9) After the training, we then perform the reverse diffusion step with Eq.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To this end, we propose a tree skeletonization method based on a denoising diffusion probabilistic model (DDPM) that outputs a tree skeleton based on an input 3D point cloud. | conditioning observation와 noisy/intermediate sample | p. 3 (3. Our Approach), p. 2 (1. Introduction) |
| State/latent | tree, skeletonization, denoising, diffusion, probabilistic, model, DDPM, outputs, skeleton, input, point, cloud | latent/noise variable와 conditional distribution | p. 3 (3. Our Approach), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Our approach takes as input a 3D point cloud that partially covers the tree and outputs a graph representing the branching structure of the trunk and canopy. | generated sample, action chunk 또는 trajectory | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Our Approach) |
| Training objective | 원문 대조: Noisy input x^t, timestep t, 조건 c를 이용해 주입한 Gaussian noise ε를 예측하고 squared L2 오차로 학습한다. Classifier-free guidance 학습에서는 Bernoulli mask로 조건을 비우는 경우를 포함한다. ([PDF p. 4](https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf#page=4), §3.1, Eq. (5)) | Noise-prediction loss; tree reconstruction metric은 별도 근거 | [PDF p. 4](https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf#page=4), §3.1, Eq. (5) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions are: • A tree skeletonization approach using 3D point clouds as input that employs a novel diffusion-based formulation for generating ...
- **p. 1 / 1. Introduction - extractive body cue:** Tree skeletonization consists of inferring from sensor data the graph representing the medial axes of the trunk, branches, and twigs, collectively referred to as branches, ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose a method for estimating skeletons from 3D point cloud data of trees with dense foliage, leveraging a denoising diffusion probabilistic ...
- **p. 3 / 3. Our Approach - extractive body cue:** To this end, we propose a tree skeletonization method based on a denoising diffusion probabilistic model (DDPM) that outputs a tree skeleton based on an ...
- **p. 4 / 3. Our Approach - extractive body cue:** In the following, we first describe the DDPM formulation and then we present our formulation to adapt it to the tree skeletonization task.
- **p. 7 / 4.2. Performance on multi-variety synthetic dataset - extractive body cue:** In fact, our approach still outperforms all baselines in the F1-Score, which gives a more complete picture than precision or recall individually.
- **p. 7 / 4.2. Performance on multi-variety synthetic dataset - extractive body cue:** 1, we outperform all baselines in the Chamfer distance and F1-Score, showing that our predicted skeletons are closer to the reference and more accurate.
- **p. 6 / 4.1. Experimental setup - extractive body cue:** To evaluate the tree skeletonization performance, we use commonly used metrics: the Chamfer distance, precision, recall, and F1-score.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 7 (4.2. Performance on multi-variety synthetic dataset) |
| Embodiment/environment | To test the performance on real-world data, we evaluated our method on our apple orchard dataset presented in Sec. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup) |
| Dataset/benchmark | The batch size and the learning rate were tuned on the validation set of the different datasets. | role, split, size and leakage | p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup), p. 7 (4.1. Experimental setup), p. 7 (4.2. Performance on multi-variety synthetic dataset) |
| Metric | To evaluate the tree skeletonization performance, we use commonly used metrics: the Chamfer distance, precision, recall, and F1-score. | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup), p. 7 (4.3. Performance on synthetic apple tree dataset) |
| Baseline/ablation | As baselines, we use state-of-the-art methods for tree skeletonization. | fair input/data/compute/action matching | p. 6 (4.1. Experimental setup), p. 7 (4.3. Performance on synthetic apple tree dataset), p. 7 (4.2. Performance on multi-variety synthetic dataset) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Performance on multi-variety synthetic dataset - extractive body cue:** Those are way less than the nodes predicted by AdTree, which is a potential limitation.
- **p. 7 / 4.4. Performance on BReTS dataset - extractive body cue:** This experiment, therefore, tests the realworld applicability of the compared methods, which cannot be shown on synthetic data alone.
- **p. 6 / 4.1. Experimental setup - extractive body cue:** As the synthetic dataset TreeNet3D does not contain apple trees, we performed additional experiments on the simulated apple tree data provided by Dobbs et al.
- **p. 6 / 4.1. Experimental setup - extractive body cue:** We also defined the train, validation and test splits by randomly splitting the dataset in a 80%, 10%, and 10% for each tree species, as ...
- **p. 8 / 5. Conclusion - extractive body cue:** Due to the extreme amount of occlusions, the learned distribution of tree shapes is very effective.
- **p. 8 / 5. Conclusion - extractive body cue:** We showed that our method is robust to different tree species, scales, and appearances and compared its performance to state-of-the-art methods both on synthetic and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of our tree skeletonization approach. Given a tree and its point cloud scan S, we define the initial set of nodes MT ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 The world around us is filled with natural structures, such as trees, that humans can interpret even when parts of them are occluded; however, this remains a challenge for computer vision systems.를 문제로 두고, In summary, our key contributions are: • A tree skeletonization approach using 3D point clouds as input that employs a novel diffusion-based formulation for generating an implicit representation of a graphlike structure ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Our Approach), p. 4 (3.1. Denoising diffusion probabilistic models) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
