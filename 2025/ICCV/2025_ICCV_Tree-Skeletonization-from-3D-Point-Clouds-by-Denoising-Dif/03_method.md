# Method - Tree Skeletonization from 3D Point Clouds by Denoising Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 3 (3. Our Approach), p. 4 (3.1. Denoising diffusion probabilistic models), p. 4 (3.1. Denoising diffusion probabilistic models), p. 5 (3.2. Diffusion tree skeletonization), p. 5 (3.2. Diffusion tree skeletonization)): To this end, we propose a tree skeletonization method based on a denoising diffusion probabilistic model (DDPM) that outputs a tree skeleton based on an input 3D point cloud.

## Method Body Digest

- **p. 3 / 3. Our Approach - extractive body cue:** To this end, we propose a tree skeletonization method based on a denoising diffusion probabilistic model (DDPM) that outputs a tree skeleton based on an ...
- **원문 대조:** Noisy input x^t, timestep t, 조건 c를 이용해 주입한 Gaussian noise ε를 예측하고 squared L2 오차로 학습한다. Classifier-free guidance 학습에서는 Bernoulli mask로 조건을 비우는 경우를 포함한다. ([PDF p. 4](https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf#page=4), §3.1, Eq. (5)).
- **p. 4 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** In our case, we use the classifier-free guidance since it does not require a pre-trained encoder.
- **p. 5 / 3.2. Diffusion tree skeletonization - extractive body cue:** (9) After the training, we then perform the reverse diffusion step with Eq.
- **p. 5 / 3.2. Diffusion tree skeletonization - extractive body cue:** To achieve this we first train our model by adding noise to the nodes md as defined in Eq.
- **p. 4 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** The training process optimizes the denoising model to predict the noise ϵ added at step t to a given input.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach takes as input a 3D point cloud that partially covers the tree and outputs a graph representing the branching structure of the trunk ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions are: • A tree skeletonization approach using 3D point clouds as input that employs a novel diffusion-based formulation for generating ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions are: • A tree skeletonization approach using 3D point clouds as input that employs a novel diffusion-based formulation for generating ...
- **p. 1 / 1. Introduction - extractive body cue:** Tree skeletonization consists of inferring from sensor data the graph representing the medial axes of the trunk, branches, and twigs, collectively referred to as branches, ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose a method for estimating skeletons from 3D point cloud data of trees with dense foliage, leveraging a denoising diffusion probabilistic ...

## Source Evidence Cues

- **p. 3 / 3. Our Approach - extractive body cue:** To this end, we propose a tree skeletonization method based on a denoising diffusion probabilistic model (DDPM) that outputs a tree skeleton based on an ...
- **원문 대조:** Noisy input x^t, timestep t, 조건 c를 이용해 주입한 Gaussian noise ε를 예측하고 squared L2 오차로 학습한다. Classifier-free guidance 학습에서는 Bernoulli mask로 조건을 비우는 경우를 포함한다. ([PDF p. 4](https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf#page=4), §3.1, Eq. (5)).
- **p. 4 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** In our case, we use the classifier-free guidance since it does not require a pre-trained encoder.
- **p. 5 / 3.2. Diffusion tree skeletonization - extractive body cue:** (9) After the training, we then perform the reverse diffusion step with Eq.
- **p. 5 / 3.2. Diffusion tree skeletonization - extractive body cue:** To achieve this we first train our model by adding noise to the nodes md as defined in Eq.
- **Detected method headings:** 3. Our Approach (p. 3); 3.1. Denoising diffusion probabilistic models (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | To this end, we propose a tree skeletonization method based on a denoising diffusion probabilistic model (DDPM) that outputs a tree skeleton ... | p. 3 (3. Our Approach), p. 4 (3.1. Denoising diffusion probabilistic models) |
| Conditional noise predictor | 주입 noise를 회귀 | Noisy input, timestep, 선택적으로 비운 condition | Squared L2 loss | Noise estimate | 원문 대조: Noisy input x^t, timestep t, 조건 c를 이용해 주입한 Gaussian noise ε를 예측하고 squared L2 오차로 학습한다. Classifier-free guidance 학습에서는 Bernoulli mask로 조건을 비우는 경우를 포함한다. ([PDF p. 4](https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf#page=4), §3.1, Eq. (5)) | [PDF p. 4](https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf#page=4), §3.1, Eq. (5) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | In our case, we use the classifier-free guidance since it does not require a pre-trained encoder. | p. 4 (3.1. Denoising diffusion probabilistic models), p. 5 (3.2. Diffusion tree skeletonization) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **원문 대조:** Noisy input x^t, timestep t, 조건 c를 이용해 주입한 Gaussian noise ε를 예측하고 squared L2 오차로 학습한다. Classifier-free guidance 학습에서는 Bernoulli mask로 조건을 비우는 경우를 포함한다. ([PDF p. 4](https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf#page=4), §3.1, Eq. (5)).
- **p. 4 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** The training process optimizes the denoising model to predict the noise ϵ added at step t to a given input.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 4 (3.1. Denoising diffusion probabilistic models).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | tree, skeletonization, denoising, diffusion, probabilistic, model, DDPM, outputs, skeleton, input, point, cloud, takes, partially | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | tree, skeletonization, denoising, diffusion, probabilistic, model, DDPM, outputs, skeleton, input | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | summary, contributions, tree, skeletonization, point, clouds, input, employs, novel, diffusion-based | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | Then, model, computes, noise, prediction, supervising, loss, training, process, optimizes | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Our Approach - extractive body cue:** To this end, we propose a tree skeletonization method based on a denoising diffusion probabilistic model (DDPM) that outputs a tree skeleton based on an ...
- **p. 2 / 1. Introduction - extractive body cue:** Our approach takes as input a 3D point cloud that partially covers the tree and outputs a graph representing the branching structure of the trunk ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions are: • A tree skeletonization approach using 3D point clouds as input that employs a novel diffusion-based formulation for generating ...
- **p. 4 / 3. Our Approach - extractive body cue:** [51] starting with an initialization of the vertex positions obtained by randomly sampling points from the input point cloud.
- **p. 4 / 3. Our Approach - extractive body cue:** We condition the DDPM predictions with the input point cloud, in order to predict the corresponding tree skeleton out of the learned distribution.
- **p. 5 / 3.2. Diffusion tree skeletonization - extractive body cue:** (8) Training the DDPM to predict the noise ϵ conditioned to an input tree point cloud S = {s1, . . . , sB} with ...
- **p. 5 / 3.2. Diffusion tree skeletonization - extractive body cue:** After iteratively removing the noise over T times, we arrive to a sample M0 θ ∼q (M) as the skeleton of the input tree point ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Due to memory constraints we had to find a tradeoff between efficiency and resolution, which led to predicting 3,000 nodes. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | As diffusion parameters, we used T = 1, 000 steps and tuned the noise factors β1 and βT for each dataset, as ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | Due to memory constraints we had to find a tradeoff between efficiency and resolution, which led to predicting 3,000 nodes. | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | As diffusion parameters, we used T = 1, 000 steps and tuned the noise factors β1 and βT for each dataset, as ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Denoising diffusion probabilistic models - extractive body cue:** In our case, we use the classifier-free guidance since it does not require a pre-trained encoder.
- **p. 5 / 3.2. Diffusion tree skeletonization - extractive body cue:** (9) After the training, we then perform the reverse diffusion step with Eq.
- **p. 5 / 3.2. Diffusion tree skeletonization - extractive body cue:** To achieve this we first train our model by adding noise to the nodes md as defined in Eq.
- **p. 7 / 4.1. Experimental setup - extractive body cue:** We trained our approach with a learning rate of 10-4 using the Adam optimizer [41].

## Method-Specific Formal Details

- **Body-defined terms:** tree, skeletonization, denoising, diffusion, probabilistic, model, DDPM, outputs, skeleton, input, point, cloud, Then, computes, noise, prediction, supervising, loss, case, classifier-free.
- **Relevant PDF headings:** 3. Our Approach (p. 3); 3.1. Denoising diffusion probabilistic models (p. 4).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | To test the performance on real-world data, we evaluated our method on our apple orchard dataset presented in Sec. | p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup) |
| Denoiser / vector field | As baselines, we use state-of-the-art methods for tree skeletonization. | p. 6 (4.1. Experimental setup), p. 7 (4.3. Performance on synthetic apple tree dataset) |
| Sampling / downstream interface | In fact, our approach still outperforms all baselines in the F1-Score, which gives a more complete picture than precision or recall individually. | p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 7 (4.2. Performance on multi-variety synthetic dataset) |

## Failure and Ablation Link

- **p. 8 / 4.4. Performance on BReTS dataset - extractive body cue:** Notice that our predictions are topological tree structures, however this is not always visible due to perfect overlap with the reference. the scan are leaves, ...
- **p. 7 / 4.1. Experimental setup - extractive body cue:** AdTree [15] creates an initial skeleton by building the minimum spanning tree of the point cloud and then prunes the initial tree skeleton by iteratively ...
- **p. 7 / 4.2. Performance on multi-variety synthetic dataset - extractive body cue:** Those are way less than the nodes predicted by AdTree, which is a potential limitation.
- **p. 7 / 4.4. Performance on BReTS dataset - extractive body cue:** This experiment, therefore, tests the realworld applicability of the compared methods, which cannot be shown on synthetic data alone.
- **p. 6 / 4.1. Experimental setup - extractive body cue:** As the synthetic dataset TreeNet3D does not contain apple trees, we performed additional experiments on the simulated apple tree data provided by Dobbs et al.
- **p. 6 / 4.1. Experimental setup - extractive body cue:** We also defined the train, validation and test splits by randomly splitting the dataset in a 80%, 10%, and 10% for each tree species, as ...
- **p. 8 / 5. Conclusion - extractive body cue:** Due to the extreme amount of occlusions, the learned distribution of tree shapes is very effective.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Our Approach), p. 4 (3.1. Denoising diffusion probabilistic models), p. 4 (3.1. Denoising diffusion probabilistic models), p. 5 (3.2. Diffusion tree skeletonization), p. 5 (3.2. Diffusion tree skeletonization), objective p. 4 (3.1. Denoising diffusion probabilistic models), p. 4 (3.1. Denoising diffusion probabilistic models), temporal p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 7 (4.1. Experimental setup), p. 4 (3.1. Denoising diffusion probabilistic models), p. 4 (3.1. Denoising diffusion probabilistic models), p. 3 (2. Related Work), p. 3 (2. Related Work).
