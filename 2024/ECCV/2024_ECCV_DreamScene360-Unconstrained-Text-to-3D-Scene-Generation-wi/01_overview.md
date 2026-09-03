# DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/996_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00996.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/996_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00996.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This absence of parallax - critical for depth perception through binocular disparity - along with the lack of multiple observational cues typically provided by a baseline, poses substantial challenges in accurately determining ...를 문제로 두고, Collectively, our framework, DreamScene360, enables the creation of immersive and realistic 3D environments from a simple user command, offering a novel solution to the pressing demand for high-quality 3D scenes (see the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** The vast potential applications of text-to-3D to VR/MR platforms, industrial design, and gaming sectors have significantly propelled research efforts aimed at developing a reliable method ...
- **p. 2 / 1 Introduction - extractive body cue:** Recent developments in the 2D domain have seen the successful generation or editing of high-quality and adaptable images/videos using large-scale pre-trained diffusion models [48,51] on ...
- **p. 2 / 1 Introduction - extractive body cue:** Moving beyond 2D, the generation of 3D content, particularly 3D scenes, is constrained by the limited availability of annotated 3D image-text data pairs.
- **p. 2 / 1 Introduction - extractive body cue:** Consequently, efforts in 3D content creation often rely on leveraging large-scale 2D models.
- **p. 2 / 1 Introduction - extractive body cue:** This line of approach facilitates the creation of 3D scenes through a time-consuming distillation process.
- **p. 7 / 1 Introduction - extractive body cue:** This absence of parallax - critical for depth perception through binocular disparity - along with the lack of multiple observational cues typically provided by a ...
- **p. 3 / 1 Introduction - extractive body cue:** While the generated panorama images overcome the view consistency issue across different viewpoints, they still lack depth information and any layout priors in unconstrained settings, ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Collectively, our framework, DreamScene360, enables the creation of immersive and realistic 3D environments from a simple user command, offering a novel solution to the pressing ...
- **p. 9 / 1 Introduction - extractive body cue:** To mitigate this, we introduce a geometric regularization strategy designed to penalize discontinuities between pixels that exhibit inaccurate depth relationships.
- **p. 3 / 1 Introduction - extractive body cue:** DreamScene360 3 To address the above challenges in creating a holistic 360◦text-to-3D scene generation pipeline, we introduce DreamScene360.
- **p. 4 / 1 Introduction - extractive body cue:** In this work, we propose a method for text to 360◦3D scene generation, by using panorama images as an intermediate representation.
- **p. 4 / 1 Introduction - extractive body cue:** Our work requires a text prompt input; however, unlike prior work, we propose using panoramic images as an intermediate input for globally consistent scenes.
- **p. 4 / 1 Introduction - extractive body cue:** Since then, several works have emerged enabling sparse view [66,76] and compressed [10, 27, 38, 40, 42] 3D Gaussian representations, as well as representation of ...
- **p. 5 / 1 Introduction - extractive body cue:** We use StitchDiffusion [62] as the pretrained 2D diffusion model, where a stitch method is employed in the generation process for synthesizing seamless 360◦panoramic images.
- **p. 6 / 1 Introduction - extractive body cue:** 3.2 Lifting in-the-wild Panorama to 360 Scene Transforming a single image, specifically an in-the-wild 360◦panoramic image, into a 3D model poses significant challenges due to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The parameters of MLPs Θ are initialized with an input dimension of three and an output dimension of one. | RGB-D, image set, point cloud, depth와 camera pose | p. 7 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | parameters, MLPs, initialized, input, dimension, three, output, Additional, control, generation, been, possible | geometry, map, object/relationship state | p. 7 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | Additional control of generation has also been shown to be possible, through auxiliary inputs such as layout [74], pose [73] and depth maps [5]. | point map, pose, scene graph, affordance 또는 query result | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Objective/outcome | In order to address invisible issues inherent in single-view inputs, we impose semantic and geometric constraints on both synthesized and input camera views as regularizations. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (360 Panorama), p. 5 (1 Introduction), p. 7 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Collectively, our framework, DreamScene360, enables the creation of immersive and realistic 3D environments from a simple user command, offering a novel solution to the pressing ...
- **p. 9 / 1 Introduction - extractive body cue:** To mitigate this, we introduce a geometric regularization strategy designed to penalize discontinuities between pixels that exhibit inaccurate depth relationships.
- **p. 3 / 1 Introduction - extractive body cue:** DreamScene360 3 To address the above challenges in creating a holistic 360◦text-to-3D scene generation pipeline, we introduce DreamScene360.
- **p. 4 / 1 Introduction - extractive body cue:** In this work, we propose a method for text to 360◦3D scene generation, by using panorama images as an intermediate representation.
- **p. 4 / 1 Introduction - extractive body cue:** Our work requires a text prompt input; however, unlike prior work, we propose using panoramic images as an intermediate input for globally consistent scenes.
- **p. 13 / 4 Experiments - extractive body cue:** These functionalities are otherwise hard to achieve in previous baselines that do not have global 2D representations, and as a result, our results provide a ...
- **p. 11 / 4 Experiments - extractive body cue:** However, the works utilizing a bounded NeRF representation using score distillation do not work very well in this case.
- **p. 12 / 4 Experiments - extractive body cue:** 4.2 Main Results 360◦Scene Generation.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 13 (4 Experiments), p. 11 (4 Experiments) |
| Embodiment/environment | QAlign [65] is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets. | hardware/simulator version and reset protocol | p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Dataset/benchmark | Their pipeline, which inpaints each patch separately based on the same text prompt, tends to produce repetitive results especially when generating complex scenes. | role, split, size and leakage | p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments) |
| Metric | However, the works utilizing a bounded NeRF representation using score distillation do not work very well in this case. | definition, denominator, direction and uncertainty | p. 11 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments) |
| Baseline/ablation | Thus, the comparisons are conducted between DreamScene360 (ours) and the state-of-the-art LucidDreamer [7]. | fair input/data/compute/action matching | p. 11 (4 Experiments), p. 10 (Figure/Table caption), p. 11 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 12 / 4 Experiments - extractive body cue:** In the case of the Yosemite text prompt, LucidDreamer merely replicates the waterfall seen in the initial view throughout.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This absence of parallax - critical for depth perception through binocular disparity - along with the lack of multiple observational cues typically provided by a baseline, poses substantial challenges in accurately determining ...를 문제로 두고, Collectively, our framework, DreamScene360, enables the creation of immersive and realistic 3D environments from a simple user command, offering a novel solution to the pressing demand for high-quality 3D scenes (see the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 7 (1 Introduction), p. 3 (1 Introduction), p. 7 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
