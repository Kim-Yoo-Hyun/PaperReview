# Method - SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.3.1. Design space), p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space), p. 4 (3.3. Compound 3D-Informed Design), p. 6 (3.3.1. Design space)): We introduce the design space considered in our work, i.e., choices of training data, model architecture, and training setup that advance the 3D spatial reasoning capabilities of LMMs.

## Method Body Digest

- **p. 5 / 3.3.1. Design space - extractive PDF cue:** We introduce the design space considered in our work, i.e., choices of training data, model architecture, and training setup that advance the 3D spatial reasoning ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** This step enables the model to learn rich visual features solely from visual signals. • Noisy image-text pairs: Large-scale image-text pairs [20, 37, 52] are ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** A standard LMM [39, 41] consists of a visual encoder to process the image, a multimodal connector to transform the visual feature to visual token, ...
- **p. 5 / 3.3.1. Design space - extractive PDF cue:** We consider two types of visual encoders: (i) Frozen & pretrained visual encoder CLIP [48] following [41] but with the option to mix a wider ...
- **p. 4 / 3.3. Compound 3D-Informed Design - extractive PDF cue:** 3.2.1, we consider two main aspects in our compound 3D-informed design - the architecture design that leads to visual encoders with strong 3D awareness and ...
- **p. 6 / 3.3.1. Design space - extractive PDF cue:** We investigate the 3D-awareness of mixed visual encoders, and incorporate 3D-informed data at each training stage across all architecture components.
- **p. 6 / 3.3.1. Design space - extractive PDF cue:** We then study a series of design decisions. • + mixed vision encoder.
- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** This stage focuses on developing foundational visual representations, often with reconstructionbased objectives (e.g., MAE [23], DINOv2 [47]).

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model.
- **p. 2 / 1. Introduction - extractive PDF cue:** Third, we present the first comprehensive search over the LMM design space for spatial reasoning tasks and propose a roadmap towards developing state-of-the-art models in ...
- **p. 3 / 3. Methods - extractive PDF cue:** We present the task of reasoning 3D spatial relationships and explain the challenges LMMs face when answering these questions in Sec.

## Source Evidence Cues

- **p. 5 / 3.3.1. Design space - extractive PDF cue:** We introduce the design space considered in our work, i.e., choices of training data, model architecture, and training setup that advance the 3D spatial reasoning ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** This step enables the model to learn rich visual features solely from visual signals. • Noisy image-text pairs: Large-scale image-text pairs [20, 37, 52] are ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** A standard LMM [39, 41] consists of a visual encoder to process the image, a multimodal connector to transform the visual feature to visual token, ...
- **p. 5 / 3.3.1. Design space - extractive PDF cue:** We consider two types of visual encoders: (i) Frozen & pretrained visual encoder CLIP [48] following [41] but with the option to mix a wider ...
- **p. 4 / 3.3. Compound 3D-Informed Design - extractive PDF cue:** 3.2.1, we consider two main aspects in our compound 3D-informed design - the architecture design that leads to visual encoders with strong 3D awareness and ...
- **p. 6 / 3.3.1. Design space - extractive PDF cue:** We investigate the 3D-awareness of mixed visual encoders, and incorporate 3D-informed data at each training stage across all architecture components.
- **p. 6 / 3.3.1. Design space - extractive PDF cue:** We then study a series of design decisions. • + mixed vision encoder.
- **Detected method headings:** 3. Methods (p. 3); Model (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We introduce the design space considered in our work, i.e., choices of training data, model architecture, and training setup that advance the ... | p. 5 (3.3.1. Design space), p. 3 (3.1. Preliminary of LMMs) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | This step enables the model to learn rich visual features solely from visual signals. • Noisy image-text pairs: Large-scale image-text pairs [20, ... | p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | A standard LMM [39, 41] consists of a visual encoder to process the image, a multimodal connector to transform the visual feature ... | p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** This stage focuses on developing foundational visual representations, often with reconstructionbased objectives (e.g., MAE [23], DINOv2 [47]).
- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** The success of deep learning in vision is largely due to well-curated data [20, 56], and LMMs similarly depend on this foundation, albeit with diverse ...
- **p. 5 / 3.3.1. Design space - extractive PDF cue:** We consider two types of visual encoders: (i) Frozen & pretrained visual encoder CLIP [48] following [41] but with the option to mix a wider ...
- **p. 8 / Model - extractive PDF cue:** Roadmap progression towards the best-performing model.
- **p. 8 / Model - extractive PDF cue:** Thorough exploration of the design space and roadmap progression.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Existing, pretraining, visual, instruction, tuning, data, LMMs, focused, detailed, descriptions, conversations, about, scenes, appearances | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Existing, pretraining, visual, instruction, tuning, data, LMMs, focused, detailed, descriptions | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Second, novel, compound, D-informed, design, introduces, improvements, across, multiple, dimensions | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | stage, focuses, developing, foundational, visual, representations, often, reconstructionbased, objectives, MAE | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2.1. Challenges of 3D spatial reasoning - extractive PDF cue:** Existing pretraining and visual instruction tuning data for LMMs [41, 58] focused on detailed descriptions and conversations about scenes, appearances, and actions, while being vague ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** At this stage, the model is trained to describe images in details to align visual and language representations in the same space. • Visual instruction ...
- **p. 5 / 3.3. Compound 3D-Informed Design - extractive PDF cue:** This compound design simultaneously considers 3D-informed data, architecture, and training methods to search for the best-performing models for spatial reasoning. image 2D bbox image caption ...
- **p. 6 / 3.3.1. Design space - extractive PDF cue:** (b) design of LLaVA-v1.5 (CVPR'24) Alignment Instruction tuning Visual Encoder CLIP Connector LLM Connector (c) design of SpatialVLM (CVPR'24) (a) our proposed design Visual Encoder ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** Prior works [39, 41, 46, 58] repurpose VQA benchmarks [22, 32] into instruction-tuning datasets.
- **p. 4 / 3.3. Compound 3D-Informed Design - extractive PDF cue:** While previous approaches focused on generating 3D-informed instruction tuning data to enable LMMs with the abilities to estimate distances, depths, or spatial relationships [14, 16], ...
- **p. 5 / 3.3.1. Design space - extractive PDF cue:** In a multimodal LLM, a pre-trained CLIP visual encoder extracts grid features from the input image.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Visual instruction tuning data is essential but challenging to collect, as it rarely exists in its natural form online. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This step prepares the model to handle more complex multimodal tasks by first refining its visual understanding. • Multimodal alignment pretraining. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3.1. Design space - extractive PDF cue:** We introduce the design space considered in our work, i.e., choices of training data, model architecture, and training setup that advance the 3D spatial reasoning ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive PDF cue:** This step enables the model to learn rich visual features solely from visual signals. • Noisy image-text pairs: Large-scale image-text pairs [20, 37, 52] are ...
- **p. 5 / 3.3.1. Design space - extractive PDF cue:** We consider two types of visual encoders: (i) Frozen & pretrained visual encoder CLIP [48] following [41] but with the option to mix a wider ...
- **p. 4 / 3.3. Compound 3D-Informed Design - extractive PDF cue:** 3.2.1, we consider two main aspects in our compound 3D-informed design - the architecture design that leads to visual encoders with strong 3D awareness and ...
- **p. 6 / 3.3.1. Design space - extractive PDF cue:** We investigate the 3D-awareness of mixed visual encoders, and incorporate 3D-informed data at each training stage across all architecture components.
- **p. 7 / 4.2. Results - extractive PDF cue:** 3D-informed pretraining of vision encoder?

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, design, space, considered, choices, training, data, model, architecture, setup, advance, spatial, reasoning, capabilities, LMMs, step, enables, learn, rich, visual.
- **Relevant PDF headings:** 3. Methods (p. 3); Model (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We build our SpatialVQA on images from Omni3D [11], with 3D bounding box annotations on diverse objects from both urban [12, 21] ... | p. 4 (3.2.2. SpatialVQA for Evaluation), p. 4 (3.2.2. SpatialVQA for Evaluation) |
| Semantic / temporal fusion | Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary ... | p. 7 (4.2. Results), p. 7 (4.2. Results) |
| Robot query / planning handoff | Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary ... | p. 7 (4.2. Results), p. 7 (4.2. Results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Thorough exploration of the design space and roadmap progression. We systematically examine the 3D-informed design space from the aspects of data, architecture and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Design instantiation and comparison. (a) Architecture and Training of our proposed design. We investigate the 3D-awareness of mixed visual encoders, and incorporate 3D-informed ...
- **p. 7 / 4.2. Results - extractive PDF cue:** 3D-informed pretraining of vision encoder?
- **p. 7 / 4.2. Results - extractive PDF cue:** We observe that pre-pretraining in stage 0 reduces performance, suggesting that tuning vi17255
- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive PDF cue:** Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different levels of 3D awareness and cannot be ...
- **p. 7 / 4.2. Results - extractive PDF cue:** Interestingly, although SpatialVLM [14] (implemented in SpaceLLaVA [2]) outperforms other open-source models in overall performance, it falls short in 3D orientation reasoning compared to LLaVA, ...
- **p. 7 / 4.2. Results - extractive PDF cue:** We will consider models with additional inputs in future work.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.3.1. Design space), p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space), p. 4 (3.3. Compound 3D-Informed Design), p. 6 (3.3.1. Design space), objective p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space), p. 8 (Model), p. 8 (Model), temporal p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs), p. 7 (4.2. Results), p. 8 (Model).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
