# Method - RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3.6. Training Losses), p. 5 (3.4. Denoising and Occupancy Map Pre-processing), p. 5 (3.5. Radar Gaussian Splatting), p. 6 (3.6. Training Losses), p. 3 (3. Methods), p. 3 (3. Methods)): To refine the model, we introduce two regularization losses.

## Method Body Digest

- **p. 6 / 3.6. Training Losses - extractive body cue:** To refine the model, we introduce two regularization losses.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** We propose a denoising algorithm that removes noise across detected noisy azimuth angles, θnoise ∈Θsat ∪Θmulti, identified in Sec.
- **p. 5 / 3.5. Radar Gaussian Splatting - extractive body cue:** Next, we introduce our rendering pipeline, which incorporates elevation and azimuth projection along with spectral leakage modeling.
- **p. 6 / 3.6. Training Losses - extractive body cue:** Additionally, Locc corresponds to the L1 error between the rendered occupancy state Iα output by RadarSplat and the initial occupancy map Iocc estimated in the ...
- **p. 3 / 3. Methods - extractive body cue:** Finally, we define the RadarSplat training loss (Sec.
- **p. 3 / 3. Methods - extractive body cue:** 3.2) and model multipath effects by identifying their sources, enabling recovery in novel view rendering (Sec.
- **p. 4 / 3.2. Multipath and Saturation Noise Detection - extractive body cue:** Based on this observation, we identify the significant frequency with index km that has maximum magnitude.
- **p. 5 / 3.5.1. Rendering with Elevation Projection - extractive body cue:** The rendering equation is defined as: Pr(θ, n) = i X ϕi Pt · G(ϕi)2 · σi (4π)3R4n (11) Note that the wavelength, λ, and ...

## Design Rationale

- **p. 3 / 3. Methods - extractive body cue:** To account for radar noise, we propose a noise detection method (Sec.
- **p. 3 / 3. Methods - extractive body cue:** For scene reconstruction, we present a radar model that renders radar images from 3D Gaussians based on radar physics (Sec.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** Our method produces a clear denoised image, whereas Radar Fields struggles with multipath effects.

## Source Evidence Cues

- **p. 6 / 3.6. Training Losses - extractive body cue:** To refine the model, we introduce two regularization losses.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** We propose a denoising algorithm that removes noise across detected noisy azimuth angles, θnoise ∈Θsat ∪Θmulti, identified in Sec.
- **p. 5 / 3.5. Radar Gaussian Splatting - extractive body cue:** Next, we introduce our rendering pipeline, which incorporates elevation and azimuth projection along with spectral leakage modeling.
- **p. 6 / 3.6. Training Losses - extractive body cue:** Additionally, Locc corresponds to the L1 error between the rendered occupancy state Iα output by RadarSplat and the initial occupancy map Iocc estimated in the ...
- **p. 3 / 3. Methods - extractive body cue:** Finally, we define the RadarSplat training loss (Sec.
- **p. 3 / 3. Methods - extractive body cue:** 3.2) and model multipath effects by identifying their sources, enabling recovery in novel view rendering (Sec.
- **p. 4 / 3.2. Multipath and Saturation Noise Detection - extractive body cue:** Based on this observation, we identify the significant frequency with index km that has maximum magnitude.
- **Detected method headings:** 3. Methods (p. 3); 3.3. Modeling Multipath Effects (p. 4); 3.5.3. Spectral Leakage Modeling (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To refine the model, we introduce two regularization losses. | p. 6 (3.6. Training Losses), p. 5 (3.4. Denoising and Occupancy Map Pre-processing) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We propose a denoising algorithm that removes noise across detected noisy azimuth angles, θnoise ∈Θsat ∪Θmulti, identified in Sec. | p. 5 (3.4. Denoising and Occupancy Map Pre-processing), p. 5 (3.5. Radar Gaussian Splatting) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Next, we introduce our rendering pipeline, which incorporates elevation and azimuth projection along with spectral leakage modeling. | p. 5 (3.5. Radar Gaussian Splatting), p. 6 (3.6. Training Losses) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.5.1. Rendering with Elevation Projection - extractive body cue:** The rendering equation is defined as: Pr(θ, n) = i X ϕi Pt · G(ϕi)2 · σi (4π)3R4n (11) Note that the wavelength, λ, and ...
- **p. 5 / 3.5. Radar Gaussian Splatting - extractive body cue:** Additionally, a regularization loss term is designed to make αi and ηi sum to one.
- **p. 6 / 3.6. Training Losses - extractive body cue:** To refine the model, we introduce two regularization losses.
- **p. 3 / 3. Methods - extractive body cue:** Finally, we define the RadarSplat training loss (Sec.
- **p. 3 / 3. Methods - extractive body cue:** This section first introduces the radar sensing equation and common noise types in radar images (Sec.
- **p. 4 / 3.2. Multipath and Saturation Noise Detection - extractive body cue:** Unlike [5], which removes noise using a dynamic threshold that does not adapt to the radar equation, we instead detect and model radar noise to ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.5.1. Rendering with Elevation Projection), p. 3 (3. Methods), p. 3 (3. Methods), p. 4 (3.2. Multipath and Saturation Noise Detection), p. 5 (3.5. Radar Gaussian Splatting), p. 6 (3.6. Training Losses).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Additionally, Locc, corresponds, error, between, rendered, occupancy, state, output, RadarSplat, initial, Iocc, estimated, preprocessing | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Additionally, Locc, corresponds, error, between, rendered, occupancy, state, output, RadarSplat | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | account, radar, noise, detection, Sec, scene, reconstruction, present, model, renders | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | rendering, equation, defined, R4n, Note, wavelength, general, loss, factor, Additionally | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3.6. Training Losses - extractive body cue:** Additionally, Locc corresponds to the L1 error between the rendered occupancy state Iα output by RadarSplat and the initial occupancy map Iocc estimated in the ...
- **p. 6 / 3.5.2. Rendering with Azimuth Projection - extractive body cue:** Azimuth projection is then applied via a 1D convolution along the azimuth axis with kernel size 2Q and stride size Q, and a kernel weighted ...
- **p. 4 / 3.2. Multipath and Saturation Noise Detection - extractive body cue:** X[k] is the frequency domain output from the discrete Fourier transform, with k as the frequency index.
- **p. 4 / 3.2. Multipath and Saturation Noise Detection - extractive body cue:** Based on this observation, we identify the significant frequency with index km that has maximum magnitude.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** The denoised image and occupancy map are shown in Figure 6.
- **p. 5 / 3.4. Denoising and Occupancy Map Pre-processing - extractive body cue:** The denoised image is then used to generate an initial occupancy map following [5].
- **p. 3 / 3. Methods - extractive body cue:** To account for radar noise, we propose a noise detection method (Sec.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Each selected sequence has > 10 seconds duration, which contains more than 40 radar frames. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This uniform power distribution results in a constant term in the frequency domain. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The radar image rendering speed reaches 4.5 FPS on an NVIDIA A6000 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3.6. Training Losses - extractive body cue:** Additionally, Locc corresponds to the L1 error between the rendered occupancy state Iα output by RadarSplat and the initial occupancy map Iocc estimated in the ...
- **p. 3 / 3. Methods - extractive body cue:** Finally, we define the RadarSplat training loss (Sec.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** refine, model, introduce, regularization, losses, denoising, algorithm, removes, noise, across, detected, noisy, azimuth, angles, multi, identified, Sec, Next, rendering, pipeline.
- **Relevant PDF headings:** 3. Methods (p. 3); 3.3. Modeling Multipath Effects (p. 4); 3.5.3. Spectral Leakage Modeling (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Image synthesis and geometry reconstruction evaluation on Boreas dataset [7]. | p. 6 (4.3. Occupancy State Estimation), p. 6 (4.3. Occupancy State Estimation) |
| Semantic / temporal fusion | With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× ... | p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation) |
| Robot query / planning handoff | With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× ... | p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 12. Ablation studies on image synthesis. RadarSplat fails to model multipath effects when disabling the proposed multipath modeling. Radar- Splat also fails to model ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Our proposed radar image denoising method preserves rich information while remaining robust to multipath effects. In contrast, the dynamic threshold approach used in ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Multipath modeling and denoising. The multipath effect is modeled by peak frequency and source power reflection and attenu- ation. The denoising method removes ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation studies on scene reconstruction. 27602
- **p. 6 / 4.2. Novel Radar View Rendering - extractive body cue:** In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** RadarSplat also fails to model other noises when disabling the proposed noise probability. reconstruction.
- **p. 8 / 5. Conclusion - extractive body cue:** This enables radar inverse rendering for radar signal decomposition, high-fidelity radar data synthesis, and robust noise-free occupancy prediction.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3.6. Training Losses), p. 5 (3.4. Denoising and Occupancy Map Pre-processing), p. 5 (3.5. Radar Gaussian Splatting), p. 6 (3.6. Training Losses), p. 3 (3. Methods), p. 3 (3. Methods), objective p. 5 (3.5.1. Rendering with Elevation Projection), p. 5 (3.5. Radar Gaussian Splatting), p. 6 (3.6. Training Losses), p. 3 (3. Methods), p. 3 (3. Methods), p. 4 (3.2. Multipath and Saturation Noise Detection), temporal p. 6 (4.1. Experimental Setup), p. 4 (3.2. Multipath and Saturation Noise Detection), p. 4 (3.2. Multipath and Saturation Noise Detection), p. 5 (3.3. Modeling Multipath Effects), p. 5 (3.5.1. Rendering with Elevation Projection), p. 6 (4.2. Novel Radar View Rendering).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
