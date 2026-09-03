# Method - GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method)): We empirically find that the perceptual loss in [14] based on VGG-19 network [53] provides a more stable training than LPIPS [73] used in [27,32,61,66], and we use it in ...

## Method Body Digest

- **p. 6 / 3 Method - extractive body cue:** We empirically find that the perceptual loss in [14] based on VGG-19 network [53] provides a more stable training than LPIPS [73] used in [27,32,61,66], ...
- **p. 4 / 3 Method - extractive body cue:** Multi-view image tokens are then concatenated and passed through a sequence of transformer blocks consisting of self-attention and MLP layers.
- **p. 5 / 3 Method - extractive body cue:** 2) and consists of Pre-LayerNorm [3], multi-head Self-Attention [60] and MLP.
- **p. 4 / 3 Method - extractive body cue:** 3.1 Transformer-based Model Architecture As shown in Fig.
- **p. 5 / 3 Method - extractive body cue:** GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting 5 Per-pixel Gaussians Transformer Block (×𝐿) MLP + Self-Att + Linear & Unpatchify Merged Gaussians Image + ...
- **p. 6 / 3 Method - extractive body cue:** 3.2 Loss Functions During training, we render the images at the M supervision views using the predicted Gaussian splats, and minimize the image reconstruction loss.
- **p. 2 / 1 Introduction - extractive body cue:** Unlike previous LRMs that require careful designs of additional (triplane) NeRF tokens for reconstruction, we align input (2D images) and output (3D Gaussians) in the ...
- **p. 6 / 3 Method - extractive body cue:** The final output of our model is simply the merge of 3D Gaussians from all N input views.

## Design Rationale

- **p. 4 / 3 Method - extractive body cue:** In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose GS-LRM, a novel transformer-based large reconstruction model that predicts 3D Gaussian primitives [30] from sparse input images, enabling fast and ...
- **p. 5 / 3 Method - extractive body cue:** 2) and consists of Pre-LayerNorm [3], multi-head Self-Attention [60] and MLP.

## Source Evidence Cues

- **p. 6 / 3 Method - extractive body cue:** We empirically find that the perceptual loss in [14] based on VGG-19 network [53] provides a more stable training than LPIPS [73] used in [27,32,61,66], ...
- **p. 4 / 3 Method - extractive body cue:** Multi-view image tokens are then concatenated and passed through a sequence of transformer blocks consisting of self-attention and MLP layers.
- **p. 5 / 3 Method - extractive body cue:** 2) and consists of Pre-LayerNorm [3], multi-head Self-Attention [60] and MLP.
- **p. 4 / 3 Method - extractive body cue:** 3.1 Transformer-based Model Architecture As shown in Fig.
- **p. 5 / 3 Method - extractive body cue:** GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting 5 Per-pixel Gaussians Transformer Block (×𝐿) MLP + Self-Att + Linear & Unpatchify Merged Gaussians Image + ...
- **p. 6 / 3 Method - extractive body cue:** 3.2 Loss Functions During training, we render the images at the M supervision views using the predicted Gaussian splats, and minimize the image reconstruction loss.
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We empirically find that the perceptual loss in [14] based on VGG-19 network [53] provides a more stable training than LPIPS [73] ... | p. 6 (3 Method), p. 4 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Multi-view image tokens are then concatenated and passed through a sequence of transformer blocks consisting of self-attention and MLP layers. | p. 4 (3 Method), p. 5 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 2) and consists of Pre-LayerNorm [3], multi-head Self-Attention [60] and MLP. | p. 5 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 Method - extractive body cue:** 3.2 Loss Functions During training, we render the images at the M supervision views using the predicted Gaussian splats, and minimize the image reconstruction loss.
- **p. 6 / 3 Method - extractive body cue:** We empirically find that the perceptual loss in [14] based on VGG-19 network [53] provides a more stable training than LPIPS [73] used in [27,32,61,66], ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3 Method), p. 6 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Unlike, previous, LRMs, require, careful, designs, additional, triplane, NeRF, tokens, reconstruction, align, input, images | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Unlike, previous, LRMs, require, careful, designs, additional, triplane, NeRF, tokens | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | section, present, technical, details, including, architecture, transformer-based, model, Sec, GS-LRM | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Loss, Functions, During, training, render, images, supervision, views, predicted, Gaussian | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Unlike previous LRMs that require careful designs of additional (triplane) NeRF tokens for reconstruction, we align input (2D images) and output (3D Gaussians) in the ...
- **p. 6 / 3 Method - extractive body cue:** The final output of our model is simply the merge of 3D Gaussians from all N input views.
- **p. 4 / 3 Method - extractive body cue:** We tokenize posed input images via a patchify operator [20].
- **p. 2 / 1 Introduction - extractive body cue:** Input images Prompt: a plush toy of a corgi nurse Our rendered novel views Our rendered novel views Input images Novel view depth Rendered novel ...
- **p. 4 / 3 Method - extractive body cue:** The inputs to our model are N multi-view images {Ii ∈RH×W ×3/i = 1, 2, .., N} and their camera intrinsic and extrinsic parameters; here ...
- **p. 5 / 3 Method - extractive body cue:** Similar to ViT [20], we patchify the inputs by dividing the per-view feature map into non-overlapping patches with a patch size of p.
- **p. 5 / 3 Method - extractive body cue:** By unpatchifying the transformer's output, each pixel is unprojected to a 3D Gaussian.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Multi-view image tokens are then concatenated and passed through a sequence of transformer blocks consisting of self-attention and MLP layers. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This property allows us to better handle high-frequency details in the inputs and large-scale scene captures. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | We also apply deferred backpropagation [71] for rendering the GS to save GPU memory. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive body cue:** We empirically find that the perceptual loss in [14] based on VGG-19 network [53] provides a more stable training than LPIPS [73] used in [27,32,61,66], ...
- **p. 6 / 3 Method - extractive body cue:** 3.2 Loss Functions During training, we render the images at the M supervision views using the predicted Gaussian splats, and minimize the image reconstruction loss.
- **p. 6 / 4 Experiments - extractive body cue:** 4.1), then introduce the implementation and training details (Sec.
- **p. 7 / 4 Experiments - extractive body cue:** 4.2 Implementation Details We have two models trained independently in this paper: object-level GS-LRM and scene-level GS-LRM.
- **p. 8 / 4 Experiments - extractive body cue:** We pre-train the model with a resolution of 256 × 256 and fine-tune the trained model with a resolution of 512 × 512 for a ...
- **p. 10 / 4 Experiments - extractive body cue:** It's worth noting that this is an almost equal-compute comparison: LGM is trained on 32 A100 (80G VRAM) for 4 days, while our lowres base ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** empirically, find, perceptual, loss, VGG-19, network, provides, more, stable, training, LPIPS, Multi-view, image, tokens, then, concatenated, passed, through, sequence, transformer.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We follow the standard training/testing split for the dataset, which is also used in pixelSplat [8]. | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Semantic / temporal fusion | We outperform relevant baselines by a large margin in both scenarios. | p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Robot query / planning handoff | Fig. 5: We compare scene-level GS-LRM with the best-performing baseline pixel- Splat [8]. We can observe that our model is better in ... | p. 10 (Figure/Table caption), p. 10 (4 Experiments) |

## Failure and Ablation Link

- **p. 7 / 4 Experiments - extractive body cue:** We only leverage the multi-view renderings of the objects without accessing explicit 3D information (such as depths).
- **p. 8 / 4 Experiments - extractive body cue:** We further fine-tune a model that takes 2 -4 input images of 512 × 512 for generating visual results.
- **p. 8 / 4 Experiments - extractive body cue:** We pre-train the model with a resolution of 256 × 256 and fine-tune the trained model with a resolution of 512 × 512 for a ...
- **p. 13 / 4 Experiments - extractive body cue:** 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future work.
- **p. 14 / 5 Conclusion - extractive body cue:** We hope that our work can inspire more future work in the space of data-driven feed-forward 3D reconstruction.
- **p. 8 / 4 Experiments - extractive body cue:** The Triplane-LRM cannot reconstruct high-frequency details (top left and top right) and thin structures (bottom left) well.
- **p. 14 / 4 Experiments - extractive body cue:** Please refer to our project page for the video and interactive rendering results. the view frustum, which means that unseen regions cannot be reconstructed.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method), objective p. 6 (3 Method), p. 6 (3 Method), temporal p. 4 (3 Method), p. 6 (3 Method), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
