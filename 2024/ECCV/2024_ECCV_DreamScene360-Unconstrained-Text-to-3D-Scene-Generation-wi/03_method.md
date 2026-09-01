# Method - DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/996_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00996.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction), p. 2 (1 Introduction), p. 6 (1 Introduction)): Since then, several works have emerged enabling sparse view [66,76] and compressed [10, 27, 38, 40, 42] 3D Gaussian representations, as well as representation of multidimensional feature fields [75].

## Method Body Digest

- **p. 4 / 1 Introduction - extractive PDF cue:** Since then, several works have emerged enabling sparse view [66,76] and compressed [10, 27, 38, 40, 42] 3D Gaussian representations, as well as representation of ...
- **p. 4 / 1 Introduction - extractive PDF cue:** In this work, we propose a method for text to 360◦3D scene generation, by using panorama images as an intermediate representation.
- **p. 5 / 1 Introduction - extractive PDF cue:** We use StitchDiffusion [62] as the pretrained 2D diffusion model, where a stitch method is employed in the generation process for synthesizing seamless 360◦panoramic images.
- **p. 6 / 1 Introduction - extractive PDF cue:** 3.2 Lifting in-the-wild Panorama to 360 Scene Transforming a single image, specifically an in-the-wild 360◦panoramic image, into a 3D model poses significant challenges due to ...
- **p. 2 / 1 Introduction - extractive PDF cue:** These methods attempt to bridge the gap between 2D and 3D generation by initializing with an explicit 3D representation, and then progressively expanding the learned ...
- **p. 6 / 1 Introduction - extractive PDF cue:** Rather than beginning with a sparse point cloud (3DGS), we initialize with a dense point cloud utilizing pixel-wise depth information from the panoramic image of ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Generative Adversarial Networks [15] were the original state of the art for image generation.
- **p. 2 / 360 Panorama - extractive PDF cue:** In order to address invisible issues inherent in single-view inputs, we impose semantic and geometric constraints on both synthesized and input camera views as regularizations.

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** Collectively, our framework, DreamScene360, enables the creation of immersive and realistic 3D environments from a simple user command, offering a novel solution to the pressing ...
- **p. 9 / 1 Introduction - extractive PDF cue:** To mitigate this, we introduce a geometric regularization strategy designed to penalize discontinuities between pixels that exhibit inaccurate depth relationships.
- **p. 3 / 1 Introduction - extractive PDF cue:** DreamScene360 3 To address the above challenges in creating a holistic 360◦text-to-3D scene generation pipeline, we introduce DreamScene360.

## Source Evidence Cues

- **p. 4 / 1 Introduction - extractive PDF cue:** Since then, several works have emerged enabling sparse view [66,76] and compressed [10, 27, 38, 40, 42] 3D Gaussian representations, as well as representation of ...
- **p. 4 / 1 Introduction - extractive PDF cue:** In this work, we propose a method for text to 360◦3D scene generation, by using panorama images as an intermediate representation.
- **p. 5 / 1 Introduction - extractive PDF cue:** We use StitchDiffusion [62] as the pretrained 2D diffusion model, where a stitch method is employed in the generation process for synthesizing seamless 360◦panoramic images.
- **p. 6 / 1 Introduction - extractive PDF cue:** 3.2 Lifting in-the-wild Panorama to 360 Scene Transforming a single image, specifically an in-the-wild 360◦panoramic image, into a 3D model poses significant challenges due to ...
- **p. 2 / 1 Introduction - extractive PDF cue:** These methods attempt to bridge the gap between 2D and 3D generation by initializing with an explicit 3D representation, and then progressively expanding the learned ...
- **p. 6 / 1 Introduction - extractive PDF cue:** Rather than beginning with a sparse point cloud (3DGS), we initialize with a dense point cloud utilizing pixel-wise depth information from the panoramic image of ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Generative Adversarial Networks [15] were the original state of the art for image generation.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Since then, several works have emerged enabling sparse view [66,76] and compressed [10, 27, 38, 40, 42] 3D Gaussian representations, as well ... | p. 4 (1 Introduction), p. 4 (1 Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In this work, we propose a method for text to 360◦3D scene generation, by using panorama images as an intermediate representation. | p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We use StitchDiffusion [62] as the pretrained 2D diffusion model, where a stitch method is employed in the generation process for synthesizing ... | p. 5 (1 Introduction), p. 6 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 360 Panorama - extractive PDF cue:** In order to address invisible issues inherent in single-view inputs, we impose semantic and geometric constraints on both synthesized and input camera views as regularizations.
- **p. 5 / 1 Introduction - extractive PDF cue:** No Optimized 3D Gaussians Geometric Field Backward Losses Given Cameras [CLS] Semantic Loss Geometric Loss Render DPT , Virtual Cameras [CLS] , Fig.
- **p. 7 / 1 Introduction - extractive PDF cue:** _{\ a lpha , \ beta , \Theta } \bigg \{ // \alpha \cdot \boldsymbol {D}^{\text {Mono}} + \boldsymbol {\beta } - \operatorname {MLPs}(\boldsymbol {v}; ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The gaps, stemming from single-view observations, can be filled by deforming the Gaussians to the unseen regions by creating a set of pseudo-views with a ...
- **p. 5 / 1 Introduction - extractive PDF cue:** For each patch Pi(It), we ensure the distance against their denoised version Φ(Pi(It)) is minimized.
- **p. 2 / 1 Introduction - extractive PDF cue:** However, the progressive optimization frameworks leveraged by these methods struggle to inpaint substantial missing areas, especially when targeting 360◦scenes under unconstrained conditions, resulting in notably ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (360 Panorama), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 7 (1 Introduction), p. 5 (1 Introduction), p. 7 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | parameters, MLPs, initialized, input, dimension, three, output, Additional, control, generation, been, possible, through, auxiliary | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | parameters, MLPs, initialized, input, dimension, three, output, Additional, control, generation | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Collectively, framework, DreamScene360, enables, creation, immersive, realistic, environments, simple, user | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | order, address, invisible, issues, inherent, single-view, inputs, impose, semantic, geometric | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 1 Introduction - extractive PDF cue:** The parameters of MLPs Θ are initialized with an input dimension of three and an output dimension of one.
- **p. 3 / 1 Introduction - extractive PDF cue:** Additional control of generation has also been shown to be possible, through auxiliary inputs such as layout [74], pose [73] and depth maps [5].
- **p. 3 / 1 Introduction - extractive PDF cue:** While the generated panorama images overcome the view consistency issue across different viewpoints, they still lack depth information and any layout priors in unconstrained settings, ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Our work requires a text prompt input; however, unlike prior work, we propose using panoramic images as an intermediate input for globally consistent scenes.
- **p. 5 / 1 Introduction - extractive PDF cue:** DreamScene360 5 "Yosemite National Park with a waterfall" Input Text Diffusion Model Draft Image Self-refinement (round += 1) Multi-round Draft Images Yes Best Candidate Text2Panorama ...
- **p. 6 / 1 Introduction - extractive PDF cue:** 3.2 Lifting in-the-wild Panorama to 360 Scene Transforming a single image, specifically an in-the-wild 360◦panoramic image, into a 3D model poses significant challenges due to ...
- **p. 7 / 1 Introduction - extractive PDF cue:** This absence of parallax - critical for depth perception through binocular disparity - along with the lack of multiple observational cues typically provided by a ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Moreover, the issue of prompt engineering in text-to-image generation [51, 52], becomes more pronounced in text-to-3D generation frameworks [1, 7, 46] that ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The framework constructs a global point cloud by progressive inpainting into 360◦views and then distills a set of 3D Gaussians. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 1 Introduction - extractive PDF cue:** We use StitchDiffusion [62] as the pretrained 2D diffusion model, where a stitch method is employed in the generation process for synthesizing seamless 360◦panoramic images.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Since, then, several, works, have, emerged, enabling, sparse, view, compressed, Gaussian, representations, well, representation, multidimensional, feature, fields, text, scene, generation.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | QAlign [65] is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment ... | p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Semantic / temporal fusion | Thus, the comparisons are conducted between DreamScene360 (ours) and the state-of-the-art LucidDreamer [7]. | p. 11 (4 Experiments), p. 10 (Figure/Table caption) |
| Robot query / planning handoff | These functionalities are otherwise hard to achieve in previous baselines that do not have global 2D representations, and as a result, our ... | p. 13 (4 Experiments), p. 11 (4 Experiments) |

## Failure and Ablation Link

- **p. 13 / Figure/Table caption - extractive PDF cue:** Fig. 6: Ablation of Optimization Loss. We demonstrate the impact of Semantic and Geometric losses on the synthesized virtual cameras. (a) Utilizing photometric loss on ...
- **p. 12 / 4 Experiments - extractive PDF cue:** In conclusion, our results demonstrate global semantic, stylized, and geometric consistency, offering complete 360◦coverage without any blind spots.
- **p. 13 / 4 Experiments - extractive PDF cue:** 4.3 Ablation Study Self-refinement Process We further evaluate the importance of the selfrefinement process.
- **p. 14 / 4 Experiments - extractive PDF cue:** 7: Ablation Study on 3D Initialization.
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 5: Ablation of Self-Refinement. We demonstrate that the self-refinement pro- cess greatly enhances the image quality by improving the text prompt. As shown in ...
- **p. 11 / 4 Experiments - extractive PDF cue:** QAlign [65] is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets.
- **p. 12 / 4 Experiments - extractive PDF cue:** In the case of the Yosemite text prompt, LucidDreamer merely replicates the waterfall seen in the initial view throughout.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction), p. 2 (1 Introduction), p. 6 (1 Introduction), objective p. 2 (360 Panorama), p. 5 (1 Introduction), p. 7 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), temporal p. 2 (1 Introduction), p. 11 (4 Experiments), p. 2 (360 Panorama), p. 3 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
