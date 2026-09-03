# Method - HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.1. 3DGS training), p. 4 (4. Methodology), p. 4 (4.1. 3DGS training), p. 6 (4.2.3. Multi-Sampling Strategy)): Specifically, the hallucination score network consists of two components: a multi-view feature encoder V that processes multiple input views, and a score estimation branch S that predicts hallucination scores for ...

## Method Body Digest

- **p. 5 / 4.2.2. Hallucination Score Estimation - extractive body cue:** Specifically, the hallucination score network consists of two components: a multi-view feature encoder V that processes multiple input views, and a score estimation branch S ...
- **p. 5 / 4.1. 3DGS training - extractive body cue:** Specifically, unlike Difix3D [41], which employs a two-phase training strategy that first fully trains a 3DGS model and then progressively updates it with diffusion priors ...
- **p. 4 / 4. Methodology - extractive body cue:** N}}, where I and C denote the RGB images and camera poses respectively, our goal is to reconstruct a high-fidelity 3DGS model capable of producing ...
- **p. 4 / 4.1. 3DGS training - extractive body cue:** We formulate the 3DGS training as arg min Φ λinputLinput + λnovelLnovel (6) where Linput and Lnovel are the rendering losses for input views and ...
- **p. 6 / 4.2.3. Multi-Sampling Strategy - extractive body cue:** More importantly, this strategy allows the diffusion prior to exploit broader multi-view information, effectively reducing hallucination issues in the final 3DGS model.
- **p. 4 / 4.1. 3DGS training - extractive body cue:** We follow 3DGS [21] to compute the rendering loss as in at input views by combining L1 and LD-SSIM: Linput = 0.8L1 (RΦ (c) , ...
- **p. 5 / 4.2.2. Hallucination Score Estimation - extractive body cue:** We supervise S with an L2 loss between the predicted score and the ground-truth score.
- **p. 6 / 4.2.3. Multi-Sampling Strategy - extractive body cue:** We then fuse the images by selecting pixels with the lowest hallucination score across all candidate versions: ˜i[i] = ˜ik∗ G [i], k∗= arg min ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling strategy ...
- **p. 2 / 1. Introduction - extractive body cue:** We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination ...
- **p. 5 / 4.2.3. Multi-Sampling Strategy - extractive body cue:** To further enhance HAD, we propose a multi-sampling strategy that creates multiple versions of augmented views and fuses them to produce higher-quality novel views for ...

## Source Evidence Cues

- **p. 5 / 4.2.2. Hallucination Score Estimation - extractive body cue:** Specifically, the hallucination score network consists of two components: a multi-view feature encoder V that processes multiple input views, and a score estimation branch S ...
- **p. 5 / 4.1. 3DGS training - extractive body cue:** Specifically, unlike Difix3D [41], which employs a two-phase training strategy that first fully trains a 3DGS model and then progressively updates it with diffusion priors ...
- **p. 4 / 4. Methodology - extractive body cue:** N}}, where I and C denote the RGB images and camera poses respectively, our goal is to reconstruct a high-fidelity 3DGS model capable of producing ...
- **p. 4 / 4.1. 3DGS training - extractive body cue:** We formulate the 3DGS training as arg min Φ λinputLinput + λnovelLnovel (6) where Linput and Lnovel are the rendering losses for input views and ...
- **p. 6 / 4.2.3. Multi-Sampling Strategy - extractive body cue:** More importantly, this strategy allows the diffusion prior to exploit broader multi-view information, effectively reducing hallucination issues in the final 3DGS model.
- **Detected method headings:** 4. Methodology (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Specifically, the hallucination score network consists of two components: a multi-view feature encoder V that processes multiple input views, and a score ... | p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.1. 3DGS training) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Specifically, unlike Difix3D [41], which employs a two-phase training strategy that first fully trains a 3DGS model and then progressively updates it ... | p. 5 (4.1. 3DGS training), p. 4 (4. Methodology) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | N}}, where I and C denote the RGB images and camera poses respectively, our goal is to reconstruct a high-fidelity 3DGS model ... | p. 4 (4. Methodology), p. 4 (4.1. 3DGS training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.1. 3DGS training - extractive body cue:** We formulate the 3DGS training as arg min Φ λinputLinput + λnovelLnovel (6) where Linput and Lnovel are the rendering losses for input views and ...
- **p. 4 / 4.1. 3DGS training - extractive body cue:** We follow 3DGS [21] to compute the rendering loss as in at input views by combining L1 and LD-SSIM: Linput = 0.8L1 (RΦ (c) , ...
- **p. 5 / 4.2.2. Hallucination Score Estimation - extractive body cue:** We supervise S with an L2 loss between the predicted score and the ground-truth score.
- **p. 5 / 4.1. 3DGS training - extractive body cue:** Specifically, unlike Difix3D [41], which employs a two-phase training strategy that first fully trains a 3DGS model and then progressively updates it with diffusion priors ...
- **p. 6 / 4.2.3. Multi-Sampling Strategy - extractive body cue:** We then fuse the images by selecting pixels with the lowest hallucination score across all candidate versions: ˜i[i] = ˜ik∗ G [i], k∗= arg min ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 4 (4.1. 3DGS training), p. 4 (4.1. 3DGS training), p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.1. 3DGS training), p. 6 (4.2.3. Multi-Sampling Strategy).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | feedforward, NVS, network, generalizable, takes, multiple, views, input, outputs, feature, enabling, rendering, images, novel | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | feedforward, NVS, network, generalizable, takes, multiple, views, input, outputs, feature | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | best, knowledge, first, study, hallucination, score, modeling, context, introduce, multi-sampling | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | formulate, DGS, training, inputLinput, novelLnovel, where, Linput, Lnovel, rendering, losses | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Preliminary - extractive body cue:** A feedforward NVS network is a generalizable network that takes multiple views as input and outputs a 3D feature, enabling the rendering of images from ...
- **p. 5 / 4.2.2. Hallucination Score Estimation - extractive body cue:** Thus, the multi-view encoder V outputs features aggregated at the novel view pose ˜c from the input views.
- **p. 5 / 4.2.2. Hallucination Score Estimation - extractive body cue:** To leverage the multi-view reasoning capability of existing novel view synthesis networks, we base our hallucination score network on the pre-trained LVSM [20], a stateof-the-art ...
- **p. 4 / 4. Methodology - extractive body cue:** N}}, where I and C denote the RGB images and camera poses respectively, our goal is to reconstruct a high-fidelity 3DGS model capable of producing ...
- **p. 4 / 3. Preliminary - extractive body cue:** View selection Selected Input views Outputs Ours GT Difix3D Hallucination After training Fix Render Figure 2.
- **p. 3 / 3. Preliminary - extractive body cue:** We formulate it as: ic = FFD(P / c), (3) where P denotes the input calibrated images, c represents novel view pose and ic is ...
- **p. 2 / 1. Introduction - extractive body cue:** To further enhance the performance of HAD, we propose a multi-sampling strategy that generates multiple images at the same novel view by conditioning the diffusion ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Nevertheless, we follow Difix3D [41] in alternating between view augmentation and training steps. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | We train the framework with the V frozen on a small curated dataset of novel view and original multi-view pairs. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | We fine-tune the network for 10k iterations with a batch size of 2 per GPU, requiring approximately 28 hours on eight NVIDIA ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. 3DGS training - extractive body cue:** Specifically, unlike Difix3D [41], which employs a two-phase training strategy that first fully trains a 3DGS model and then progressively updates it with diffusion priors ...
- **p. 4 / 4. Methodology - extractive body cue:** N}}, where I and C denote the RGB images and camera poses respectively, our goal is to reconstruct a high-fidelity 3DGS model capable of producing ...
- **p. 4 / 4.1. 3DGS training - extractive body cue:** We formulate the 3DGS training as arg min Φ λinputLinput + λnovelLnovel (6) where Linput and Lnovel are the rendering losses for input views and ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We fine-tune the network for 10k iterations with a batch size of 2 per GPU, requiring approximately 28 hours on eight NVIDIA V100 32GB GPUs.
- **p. 5 / 4.1. 3DGS training - extractive body cue:** Specifically, unlike Difix3D [41], which employs a two-phase training strategy that first fully trains a 3DGS model and then progressively updates it with diffusion priors ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** For 3DGS training, we set the learning rates to 8e-5 for Gaussian means, 5e-2 for opacity, 1e-3 for rotation, 5e-4 for the 0-th order spherical ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, hallucination, score, network, consists, components, multi-view, feature, encoder, processes, multiple, input, views, estimation, branch, predicts, scores, novel, view, images.
- **Relevant PDF headings:** 4. Methodology (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | We first curate training dataset of randomly selected 116 scenes from benchmark dataset for hallucination score network training. | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup) |
| Denoiser / vector field | Our method outperforms the baselines by a large margin across all metrics. | p. 6 (5.2. In-domain evaluation), p. 7 (5.3. Cross-domain evaluation) |
| Sampling / downstream interface | We select 3 views to achieve a trade-off between marginal improvement and computational overhead. | p. 8 (5.4. Ablation studies), p. 8 (5.4. Ablation studies) |

## Failure and Ablation Link

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** Note that ours* denotes a variant following the twophase 3DGS optimization strategy of Difix3D, enabling a fair comparison between diffusion priors with and without hallucination ...
- **p. 7 / 5.4. Ablation studies - extractive body cue:** We conduct ablation studies on different components, the number of versions and fusion strategy in the multisampling strategy (M.S.), the pretrained multiview encoder, and the ...
- **p. 8 / 5.4. Ablation studies - extractive body cue:** Similarly, our method without the pretrained multi-view encoder performs worse.
- **p. 8 / 5.4. Ablation studies - extractive body cue:** We study the performance of three hallucination score estimators: retrained Difix3D, ours without the pretrained multiview encoder, and our full method.
- **p. 6 / 5.2. In-domain evaluation - extractive body cue:** We compare against feedforward NVS networks (DepthSplat [44], LVSM [20]), two variants of 3DGS, and state-of-the-art diffusion prior-assisted 3DGS pipelines (Difix3D [41] and Difix3D+ [41]).
- **p. 7 / 5.4. Ablation studies - extractive body cue:** Except for the dense view setting where we use 24 views, all ablation studies employ the 9-views setting.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of framework - We train 3DGS with input images and HAD-augmented novel views. HAD combines a pretrained diffusion prior (which generates images ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.1. 3DGS training), p. 4 (4. Methodology), p. 4 (4.1. 3DGS training), p. 6 (4.2.3. Multi-Sampling Strategy), objective p. 4 (4.1. 3DGS training), p. 4 (4.1. 3DGS training), p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.1. 3DGS training), p. 6 (4.2.3. Multi-Sampling Strategy), temporal p. 5 (4.1. 3DGS training), p. 5 (4.2.2. Hallucination Score Estimation), p. 4 (3. Preliminary), p. 2 (2. Related Works), p. 2 (2. Related Works), p. 3 (2. Related Works).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
