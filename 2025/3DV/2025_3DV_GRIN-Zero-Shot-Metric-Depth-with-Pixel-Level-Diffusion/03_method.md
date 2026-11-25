# Method - GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00016; PDF retrieval source: https://openreview.net/attachment?id=VSG65wVNuL&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Sparse Unstructured Training), p. 5 (4.4. Training Procedure), p. 5 (4.4. Training Procedure), p. 4 (4.1. Sparse Unstructured Training)): To address these limitations we propose a combination of local and global conditioning which promote training with unstructured sparse data while still maintaining dense scene-level information.

## Method Body Digest

- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** To address these limitations we propose a combination of local and global conditioning which promote training with unstructured sparse data while still maintaining dense scene-level ...
- **원문 대조:** Log-depth 공간에서 주입 잡음 N_t에 noise schedule γ(t)를 적용한 값과 예측 잡음의 차이에 L2 손실을 적용한다. N_t는 표준 정규분포, t는 U(0,1)에서 샘플링한다. ([PDF p. 5](https://arxiv.org/pdf/2409.09896#page=5), §4.4 Training Procedure).
- **p. 5 / 4.4. Training Procedure - extractive body cue:** To improve iteration speed, we also randomly discard a percentage of valid local vectors, thus only supervising on a subset of L pixels, which leads ...
- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** Concretely, during training, we assume ground-truth in the form of a 2D grid D ∈RH×W with N < HW valid pixels.
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** (a) Latent tokens Zin read from input tokens Xin, are processed via a series of self-attention layers, and written back to output tokens Xout.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training data, ...
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** Although more efficient, this approach also has its drawbacks, namely the loss of fine-grained details due to latent compression, and the assumption that inputs will ...
- **p. 1 / 1. Introduction - extractive body cue:** In this work, we use input-level geometric embeddings from calibrated cameras [27] to learn physically-grounded priors capable of the zero-shot transfer of metric depth across ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training data, ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose several key modifications to this original framework to apply it to the task of depth estimation, including the use of 3D geometric positional ...
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** Capitalizing on these benefits, in the next section we introduce our approach for zero shot metric depth estimation with pixel-level diffusion.

## Source Evidence Cues

- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** To address these limitations we propose a combination of local and global conditioning which promote training with unstructured sparse data while still maintaining dense scene-level ...
- **원문 대조:** Log-depth 공간에서 주입 잡음 N_t에 noise schedule γ(t)를 적용한 값과 예측 잡음의 차이에 L2 손실을 적용한다. N_t는 표준 정규분포, t는 U(0,1)에서 샘플링한다. ([PDF p. 5](https://arxiv.org/pdf/2409.09896#page=5), §4.4 Training Procedure).
- **p. 5 / 4.4. Training Procedure - extractive body cue:** To improve iteration speed, we also randomly discard a percentage of valid local vectors, thus only supervising on a subset of L pixels, which leads ...
- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** Concretely, during training, we assume ground-truth in the form of a 2D grid D ∈RH×W with N < HW valid pixels.
- **Detected method headings:** 2.3. Diffusion Models for Depth Estimation (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | To address these limitations we propose a combination of local and global conditioning which promote training with unstructured sparse data while still ... | p. 4 (4.1. Sparse Unstructured Training), p. 5 (4.4. Training Procedure) |
| Noise predictor | Log-depth noise를 예측 | Noisy log-depth, timestep, image 조건 | L2 noise prediction loss | 예측 noise | 원문 대조: Log-depth 공간에서 주입 잡음 N_t에 noise schedule γ(t)를 적용한 값과 예측 잡음의 차이에 L2 손실을 적용한다. N_t는 표준 정규분포, t는 U(0,1)에서 샘플링한다. ([PDF p. 5](https://arxiv.org/pdf/2409.09896#page=5), §4.4 Training Procedure) | [PDF p. 5](https://arxiv.org/pdf/2409.09896#page=5), §4.4 Training Procedure |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | To improve iteration speed, we also randomly discard a percentage of valid local vectors, thus only supervising on a subset of L ... | p. 5 (4.4. Training Procedure), p. 4 (4.1. Sparse Unstructured Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **원문 대조:** Log-depth 공간에서 주입 잡음 N_t에 noise schedule γ(t)를 적용한 값과 예측 잡음의 차이에 L2 손실을 적용한다. N_t는 표준 정규분포, t는 U(0,1)에서 샘플링한다. ([PDF p. 5](https://arxiv.org/pdf/2409.09896#page=5), §4.4 Training Procedure).
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (4.4. Training Procedure).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Latent, tokens, Zin, read, input, Xin, processed, series, self-attention, layers, written, back, output, Xout | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Latent, tokens, Zin, read, input, Xin, processed, series, self-attention, layers | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | summary, contributions, follows, introduce, GRIN, novel, diffusion-based, monocular, depth, estimation | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | training, objective, loss, calculated, log-depth, scale, where, injected, noise, timestep | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** (a) Latent tokens Zin read from input tokens Xin, are processed via a series of self-attention layers, and written back to output tokens Xout.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training data, ...
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** Although more efficient, this approach also has its drawbacks, namely the loss of fine-grained details due to latent compression, and the assumption that inputs will ...
- **p. 1 / 1. Introduction - extractive body cue:** In this work, we use input-level geometric embeddings from calibrated cameras [27] to learn physically-grounded priors capable of the zero-shot transfer of metric depth across ...
- **p. 2 / 1. Introduction - extractive body cue:** In particular, we build on RIN (Recurrent Interface Networks) [35], a novel diffusion architecture that decouples its core computation from input dimensionality, making it much ...
- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** Differently from traditional U-Net architectures, RIN does not assume any spatial structure in its input tokens X.
- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** In GRIN, spatial structure is defined by geometric embeddings used as conditioning, and once incorporated each token is treated independently, which enables processing only parts ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | We use DDIM [61] with 1000 training and 10 evaluation timesteps, as well as EMA [40] with β = 0.999. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | We also apply horizontal flipping and color jittering as additional augmentations. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** To address these limitations we propose a combination of local and global conditioning which promote training with unstructured sparse data while still maintaining dense scene-level ...
- **원문 대조:** Log-depth 공간에서 주입 잡음 N_t에 noise schedule γ(t)를 적용한 값과 예측 잡음의 차이에 L2 손실을 적용한다. N_t는 표준 정규분포, t는 U(0,1)에서 샘플링한다. ([PDF p. 5](https://arxiv.org/pdf/2409.09896#page=5), §4.4 Training Procedure).
- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** Concretely, during training, we assume ground-truth in the form of a 2D grid D ∈RH×W with N < HW valid pixels.
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** For a fair comparison, we used the standard evaluation protocol for each of these benchmarks, and when necessary re-evaluated models under the same conditions with ...
- **p. 5 / 4.4. Training Procedure - extractive body cue:** At training time we discard pixels with missing depth information (i.e., djk = 0), resulting in a ˆV loc matrix with varying length N.
- **p. 6 / 5.2. Implementation Details - extractive body cue:** The second stage used this same training strategy for an additional 80k steps, with

## Method-Specific Formal Details

- **Body-defined terms:** address, limitations, combination, local, global, conditioning, promote, training, unstructured, sparse, data, while, still, maintaining, dense, scene-level, information, objective, loss, calculated.
- **Relevant PDF headings:** 2.3. Diffusion Models for Depth Estimation (p. 2).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | We trained GRIN using a diverse combination of indoor and outdoor datasets from both real-world and syn | p. 5 (5.1. Training Datasets), p. 6 (5.1. Training Datasets) |
| Denoiser / vector field | Results of this experiment are shown in Table 2, indicating that GRIN also outperforms the current state-of-the-art in relative depth estimation across ... | p. 7 (5.4. Zero-Shot Relative Depth Estimation), p. 6 (5.1. Training Datasets) |
| Sampling / downstream interface | We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left ... | p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 7 (5.4. Zero-Shot Relative Depth Estimation) |

## Failure and Ablation Link

- **p. 8 / 5.4. Zero-Shot Relative Depth Estimation - extractive body cue:** GRIN FT NI indicates our model (Table 1) fine-tuned without intrinsics.
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** We argue that our approach of directly ingesting sparse data is more scalable, since it enables supervised pre-training on much more diverse real-world datasets without ...
- **p. 8 / 5.6. Ablation Study - extractive body cue:** Ablation study of different design choices. ent depth parameterizations, namely linear and natural logarithm, each emphasizing different ranges.
- **p. 7 / 5.4. Zero-Shot Relative Depth Estimation - extractive body cue:** Thus, we replace them with default pinhole values: fx = cx = W/2 and fy = cy = H/2, and reutilize our pre-trained metric model ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 8. Degradation in depth estimation performance when removing global conditioning vectors during inference. The percentage value indicates how many global conditioning vectors are maintained, ...
- **p. 9 / 6. Conclusion - extractive body cue:** Interestingly, these uncertainty maps also accurately detect failure cases of our model, such as the mirror on the bottom of the second column, due to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot metric monocular depth estimation results on various indoor and outdoor datasets. Numbers in italics indicate results obtained by evaluating specific methods on ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4.1. Sparse Unstructured Training), p. 5 (4.4. Training Procedure), p. 5 (4.4. Training Procedure), p. 4 (4.1. Sparse Unstructured Training), objective p. 5 (4.4. Training Procedure), temporal p. 6 (5.2. Implementation Details), p. 6 (5.2. Implementation Details), p. 3 (3. Diffusion Preliminaries), p. 5 (4.5. Inference Procedure), p. 5 (4.3. GRIN Conditioning), p. 1 (1. Introduction).
