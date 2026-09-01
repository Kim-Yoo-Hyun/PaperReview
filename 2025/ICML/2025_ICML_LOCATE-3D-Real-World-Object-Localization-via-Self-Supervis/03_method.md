# Method - LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=FKi6yjXwCN; PDF retrieval source: https://openreview.net/pdf/ad047cb665efb75be8a655bf9cb4f4ab3b97d687.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (2.3.2. TRAINING LOCATE 3D), p. 5 (2.3.2. TRAINING LOCATE 3D)): In order to not destroy the pretrained features we use a stage-wise learning rate scheduler (Kumar et al., 2022); specifically we start by training the decoder with frozen encoder features, ...

## Method Body Digest

- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** In order to not destroy the pretrained features we use a stage-wise learning rate scheduler (Kumar et al., 2022); specifically we start by training the ...
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** We apply progressively weighted deep supervision at every decoder layer and maintain an Exponential Moving Average (EMA) of the model weights to use for evaluation ...
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** Specifically, LOCATE 3D optimizes a composite loss function, which includes: (1) a mask loss, combining Dice and cross-entropy loss terms (Cheng et al., 2021); (2) ...
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** Following (Carion et al., 2020), we define a matching cost and use Hungarian Matching to assign object query predictions to ground truth objects.
- **p. 3 / 1. Introduction - extractive PDF cue:** Preprocessing: Lifting 2D Foundation Model Features into 3D Point Clouds We begin by preprocessing the inputs (posed RGB-D images) by constructing a 3D pointcloud to ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In the first preprocessing phase, we leverage the underlying sensor observation stream to lift features from 2D foundation models (Radford et al., 2021; Oquab et ...
- **p. 2 / 1. Introduction - extractive PDF cue:** It takes as inputs 3D point clouds with features lifted from 2D foundation models.
- **p. 3 / 1. Introduction - extractive PDF cue:** Concretely, let PtC be the input point cloud with some features (in our case, it Figure 2: 3D-JEPA training framework: The context encoder computes latent ...

## Design Rationale

- **p. 4 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive PDF cue:** Specifically, each decoder module consists of three attention blocks: (1) a self-attention block that enables queries to refine their representations through mutual interaction, (2) a ...
- **p. 5 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive PDF cue:** Our decoder consists of three parallel prediction heads (Figure 7) that process the refined learned queries Q independently as object proposals.
- **p. 1 / 1. Introduction - extractive PDF cue:** We outline our contributions in this work below.

## Source Evidence Cues

- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** In order to not destroy the pretrained features we use a stage-wise learning rate scheduler (Kumar et al., 2022); specifically we start by training the ...
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** We apply progressively weighted deep supervision at every decoder layer and maintain an Exponential Moving Average (EMA) of the model weights to use for evaluation ...
- **Detected method headings:** 4.1. How does LOCATE 3D compare to prior methods (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In order to not destroy the pretrained features we use a stage-wise learning rate scheduler (Kumar et al., 2022); specifically we start ... | p. 5 (2.3.2. TRAINING LOCATE 3D), p. 5 (2.3.2. TRAINING LOCATE 3D) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We apply progressively weighted deep supervision at every decoder layer and maintain an Exponential Moving Average (EMA) of the model weights to ... | p. 5 (2.3.2. TRAINING LOCATE 3D) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In order to not destroy the pretrained features we use a stage-wise learning rate scheduler (Kumar et al., 2022); specifically we start ... | p. 5 (2.3.2. TRAINING LOCATE 3D) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** Specifically, LOCATE 3D optimizes a composite loss function, which includes: (1) a mask loss, combining Dice and cross-entropy loss terms (Cheng et al., 2021); (2) ...
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** Following (Carion et al., 2020), we define a matching cost and use Hungarian Matching to assign object query predictions to ground truth objects.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (2.3.2. TRAINING LOCATE 3D), p. 5 (2.3.2. TRAINING LOCATE 3D).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Preprocessing, Lifting, Foundation, Model, Features, Point, Clouds, begin, inputs, posed, RGB-D, images, constructing, pointcloud | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Preprocessing, Lifting, Foundation, Model, Features, Point, Clouds, begin, inputs, posed | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Specifically, decoder, module, consists, three, attention, blocks, self-attention, block, enables | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Specifically, LOCATE, optimizes, composite, loss, function, includes, mask, combining, Dice | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1. Introduction - extractive PDF cue:** Preprocessing: Lifting 2D Foundation Model Features into 3D Point Clouds We begin by preprocessing the inputs (posed RGB-D images) by constructing a 3D pointcloud to ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In the first preprocessing phase, we leverage the underlying sensor observation stream to lift features from 2D foundation models (Radford et al., 2021; Oquab et ...
- **p. 2 / 1. Introduction - extractive PDF cue:** It takes as inputs 3D point clouds with features lifted from 2D foundation models.
- **p. 3 / 1. Introduction - extractive PDF cue:** Concretely, let PtC be the input point cloud with some features (in our case, it Figure 2: 3D-JEPA training framework: The context encoder computes latent ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Notably, LOCATE 3D operates directly on sensor observation streams without requiring manual post-processing (e.g., 3D mesh refinement or ground-truth instance segmentations), making it readily deployable ...
- **p. 2 / 1. Introduction - extractive PDF cue:** LOCATE 3D is designed to operate on RGB-D sensor observations of static environments (e.g., homes in which objects remain stationary over short intervals).
- **p. 4 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive PDF cue:** As illustrated in Figure 3, the decoder processes two inputs: the 3D-JEPA features Eθ(PtClift) and a text query t.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In stage 1, a VLM - either Llama-3 (Meta AI, 2024) or GPT-4o (OpenAI, 2024) - is used to select a single ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In stage 2, a VLM selects an object in the selected frame, by choosing from 2D object masks generated with GroundingDINO (Liu ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** In order to not destroy the pretrained features we use a stage-wise learning rate scheduler (Kumar et al., 2022); specifically we start by training the ...
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** We apply progressively weighted deep supervision at every decoder layer and maintain an Exponential Moving Average (EMA) of the model weights to use for evaluation ...
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** In order to not destroy the pretrained features we use a stage-wise learning rate scheduler (Kumar et al., 2022); specifically we start by training the ...
- **p. 6 / 4.1. How does LOCATE 3D compare to prior methods - extractive PDF cue:** Most prior work assumes access to refined meshes and mesh (object) region proposals at training and inference time.
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive PDF cue:** LOCATE 3D trains the language-conditioned 3D decoder from scratch and fine-tunes the 3D-JEPA pretrained PTv3 encoder.
- **p. 7 / 4.2. Understanding the impact of 3D-JEPA - extractive PDF cue:** For each configuration, we train the same type of decoder.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** order, destroy, pretrained, features, stage-wise, learning, rate, scheduler, Kumar, specifically, start, training, decoder, frozen, encoder, then, fine-tune, jointly, lower, apply.
- **Relevant PDF headings:** 4.1. How does LOCATE 3D compare to prior methods (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | First, replacing raw RGB inputs with lifted foundation features (CF) significantly improves crossdataset performance across all benchmarks (SN++: 37.5% →51.5%, ARKitScenes: 11.3% ... | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| Semantic / temporal fusion | Notably, LOCATE 3D outperforms both baselines across most metrics, showcasing the robustness of our approach. | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| Robot query / planning handoff | Our results show that LOCATE 3D achieved a success rate of 8/10 trials, outperforming baselines with a maximum success rate of 5.66/10 ... | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |

## Failure and Ablation Link

- **p. 18 / Figure/Table caption - extractive PDF cue:** Table 5: Ablation study on decoder supervision and bounding box prediction head architectures. We evaluate accuracy (@25 and @50 IoU) on the combined SR3D, NR3D, ...
- **p. 6 / 4. Experiments and Analysis - extractive PDF cue:** Section 4.3 presents ablation studies on various components of our architecture, and Section 4.4 evaluates generalization capabilities on novel environments and robotic deployment.
- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive PDF cue:** Our ablation studies reveal the key components enabling this strong generalization.
- **p. 6 / 4. Experiments and Analysis - extractive PDF cue:** We evaluate top-1 accuracy on the validation set without any assumption of ground-truth proposals.
- **p. 7 / 4.3. LOCATE 3D ablations - extractive PDF cue:** To tease this apart, we trained variants of LOCATE 3D using different 2D foundation features.
- **p. 7 / 4.3. LOCATE 3D ablations - extractive PDF cue:** We find that using larger models (CLIP-L, SAM-H) improves results over smaller variants (CLIP-B, MobileSAM), suggesting benefits from scaling.
- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive PDF cue:** Method Evaluation Dataset ScanNet LX3D Joint Eval SN++ ARKitScenes FRE Baselines GPT-4o VLM 37.6∗ 60.5∗ 26.8 18.9 CF + 3D-Decoder 53.8 46.1 21.8 48.9 Ablations ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (2.3.2. TRAINING LOCATE 3D), p. 5 (2.3.2. TRAINING LOCATE 3D), objective p. 5 (2.3.2. TRAINING LOCATE 3D), p. 5 (2.3.2. TRAINING LOCATE 3D), temporal p. 6 (4.1. How does LOCATE 3D compare to prior methods), p. 6 (4.1. How does LOCATE 3D compare to prior methods), p. 8 (4.5. Computational Analysis), p. 1 (Abstract), p. 3 (1. Introduction), p. 3 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
