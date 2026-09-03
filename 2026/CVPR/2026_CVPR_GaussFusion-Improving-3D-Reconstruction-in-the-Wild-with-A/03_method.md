# Method - GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. 3D Reconstruction Updating), p. 5 (3.4. 3D Reconstruction Updating)): 3.3) along this trajectory to obtain novel renderings, which are then refined by our geometry-aware video generator to produce artifactfree frames.

## Method Body Digest

- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** 3.3) along this trajectory to obtain novel renderings, which are then refined by our geometry-aware video generator to produce artifactfree frames.
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** Finally, we merge the generated novel views with the original inputs and optimize the 3D Gaussian splats using the standard photometric loss (Eq.
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** We employ an spline-based interpolation scheme that regularizes both camera translation and rotation to ensure physically plausible motion.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** (2) Feed-Forward 3DGS Reconstruction Models learn to directly predict a complete set of 3D Gaussian parameters from a small set of posed/unposed input images [4, ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Given a target sample x1 (e.g., image or video), random noise x0 ∼N(0, I), and a timestep t ∈[0, 1], the intermediate latent xt is ...
- **p. 2 / 1. Introduction - extractive body cue:** Thus a video-to-video generative model can encode informative cues about splat artifacts and better refine novel views; and (ii) a comprehensive artifact simulation strategy that ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these limitations, several methods [3, 32, 34, 41, 46, 49, 56, 66, 70] have explored leveraging generative priors to enhance 3D reconstruction by ...
- **p. 2 / 1. Introduction - extractive body cue:** A Geometry Adapter module further injects these appearance and geometry features into the transformer backbone of the video generator, enabling geometry-aware conditioning.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse reconstruction ...
- **p. 2 / 1. Introduction - extractive body cue:** We present GaussFusion, a video-to-video generative model for robust 3D reconstruction that features as key component the GP-Buffer, a pixel-aligned video representation that encodes multi-modal ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** The contribution γi is the product of the learned opacity αi and the 2D Gaussian function evaluated at the pixel center u with projected mean ...

## Source Evidence Cues

- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** 3.3) along this trajectory to obtain novel renderings, which are then refined by our geometry-aware video generator to produce artifactfree frames.
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** Finally, we merge the generated novel views with the original inputs and optimize the 3D Gaussian splats using the standard photometric loss (Eq.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 3.3) along this trajectory to obtain novel renderings, which are then refined by our geometry-aware video generator to produce artifactfree frames. | p. 5 (3.4. 3D Reconstruction Updating), p. 5 (3.4. 3D Reconstruction Updating) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Finally, we merge the generated novel views with the original inputs and optimize the 3D Gaussian splats using the standard photometric loss ... | p. 5 (3.4. 3D Reconstruction Updating) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 3.3) along this trajectory to obtain novel renderings, which are then refined by our geometry-aware video generator to produce artifactfree frames. | p. 5 (3.4. 3D Reconstruction Updating) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** Finally, we merge the generated novel views with the original inputs and optimize the 3D Gaussian splats using the standard photometric loss (Eq.
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** We employ an spline-based interpolation scheme that regularizes both camera translation and rotation to ensure physically plausible motion.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.4. 3D Reconstruction Updating).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Feed-Forward, DGS, Reconstruction, Models, learn, directly, predict, complete, Gaussian, parameters, small, posed/unposed, input, images | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Feed-Forward, DGS, Reconstruction, Models, learn, directly, predict, complete, Gaussian, parameters | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, follows, geometry-informed, video-to-video, generation, model, GaussFusion, conditioned, DGS | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Finally, merge, generated, novel, views, original, inputs, optimize, Gaussian, splats | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Preliminaries - extractive body cue:** (2) Feed-Forward 3DGS Reconstruction Models learn to directly predict a complete set of 3D Gaussian parameters from a small set of posed/unposed input images [4, ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Given a target sample x1 (e.g., image or video), random noise x0 ∼N(0, I), and a timestep t ∈[0, 1], the intermediate latent xt is ...
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** Finally, we merge the generated novel views with the original inputs and optimize the 3D Gaussian splats using the standard photometric loss (Eq.
- **p. 2 / 1. Introduction - extractive body cue:** Thus a video-to-video generative model can encode informative cues about splat artifacts and better refine novel views; and (ii) a comprehensive artifact simulation strategy that ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these limitations, several methods [3, 32, 34, 41, 46, 49, 56, 66, 70] have explored leveraging generative priors to enhance 3D reconstruction by ...
- **p. 2 / 1. Introduction - extractive body cue:** A Geometry Adapter module further injects these appearance and geometry features into the transformer backbone of the video generator, enabling geometry-aware conditioning.
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** 3.3) along this trajectory to obtain novel renderings, which are then refined by our geometry-aware video generator to produce artifactfree frames.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We train our model on 8 H200 GPUs for 100K steps with a batch size of 8 and a frame resolution of ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We train our model on 8 H200 GPUs for 100K steps with a batch size of 8 and a frame resolution of ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 15.11 FPS - extractive body cue:** We train our model on 8 H200 GPUs for 100K steps with a batch size of 8 and a frame resolution of 480×832.
- **p. 6 / 15.11 FPS - extractive body cue:** Training uses the AdamW optimizer with a linear learning rate (LR) warm-up over the first 1K steps, followed by a constant LR of 1×10-5.
- **p. 7 / 5.1. Results - extractive body cue:** 1, measuring the average frame rate based on end-to-end inference time on a single H200 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** along, trajectory, obtain, novel, renderings, then, refined, geometry-aware, video, generator, produce, artifactfree, frames, Finally, merge, generated, views, original, inputs, optimize.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Testing scenes are drawn from the official test splits of each dataset, which remain unseen during training. | p. 6 (15.11 FPS), p. 7 (5.1. Results) |
| Semantic / temporal fusion | The model trained exclusively on DL3DV outperforms all baselines trained on the same dataset by a substantial margin in terms of image ... | p. 6 (5.1. Results), p. 8 (5.1. Results) |
| Robot query / planning handoff | The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable ... | p. 6 (15.11 FPS), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 5.1. Results - extractive body cue:** GaussFusion effectively removes rendering artifacts such as blur, floaters, ghosting, and texture distortions, producing sharper geometry, cleaner reconstruction than Splatfacto [61], GenFusion [57], DiFiX3D+ [55], ...
- **p. 6 / 5.1. Results - extractive body cue:** We compare three variants of our model: Ours (Single), trained solely on DL3DV [31] with optimization-based data; Ours (Joint), jointly trained on all datasets with ...
- **p. 6 / 15.11 FPS - extractive body cue:** The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable performance with significantly ...
- **p. 7 / 5.1. Results - extractive body cue:** Although our method is evaluated on MVSplat outputs without ever being trained on MVSplat predictions, it performs on par with MVSplat360, which is fully trained ...
- **p. 8 / 5.1. Results - extractive body cue:** Ablation on Input Modalities on DL3DV Dataset.
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** Ablation on Artifact Simulation and Architecture.
- **p. 8 / 6. Conclusion - extractive body cue:** We discuss our limitations and future work in Supp.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.4. 3D Reconstruction Updating), p. 5 (3.4. 3D Reconstruction Updating), objective p. 5 (3.4. 3D Reconstruction Updating), p. 5 (3.4. 3D Reconstruction Updating), temporal p. 6 (15.11 FPS), p. 6 (15.11 FPS), p. 7 (5.1. Results), p. 1 (Abstract), p. 7 (5.1. Results), p. 8 (5.1. Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
