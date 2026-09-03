# Method - GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=4SsNofUQf1; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168191. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Point Prompt), p. 4 (3.1. Point Prompt), p. 3 (3.1. Point Prompt), p. 5 (3.2. Point Shift Prompter), p. 5 (3.2. Point Shift Prompter), p. 3 (3. The Proposed Method)): Then we feed these tokens into our Prompt Propagation mechanism, injecting prompt tokens into the feature extraction process: ˜hi = Prompt-Propagation([hi; pi]), (3) where ˜hi ∈RLt×D is the propagated input ...

## Method Body Digest

- **p. 4 / 3.1. Point Prompt - extractive body cue:** Then we feed these tokens into our Prompt Propagation mechanism, injecting prompt tokens into the feature extraction process: ˜hi = Prompt-Propagation([hi; pi]), (3) where ˜hi ...
- **p. 4 / 3.1. Point Prompt - extractive body cue:** Furthermore, we adjust the tokens with adapters enhanced by shape feature f. ˆhi, ˆpi = Attn.([˜hi, pi]), (4) hi+1 = ˆhi + Adapter( ˆhi + ...
- **p. 3 / 3.1. Point Prompt - extractive body cue:** This module also generates instance-specific informative shape features f ∈RD, where D is the embedding dimension of transformers, formulated as: ˜x, f = Point-Shift-Prompter(x).
- **p. 5 / 3.2. Point Shift Prompter - extractive body cue:** Firstly, an upsampling strategy is employed to propagate features from center points to neighbor points.
- **p. 5 / 3.2. Point Shift Prompter - extractive body cue:** Then we further process the features with another pointnet: ˜d n j = Pointnet(Propagate(˜dj)), (10) where ˜d n j ∈RCj×Kj×Dj is features of neighbor points ...
- **p. 3 / 3. The Proposed Method - extractive body cue:** As shown in Figure 3, given a pre-trained 3D transformer with N blocks and a specific downstream task, we freeze the backbone and solely update ...
- **p. 4 / 3.2. Point Shift Prompter - extractive body cue:** Specifically, to acquire global shape information of point clouds without much computational cost, we utilize a hierarchical downsampling strategy.
- **p. 3 / 3.1. Point Prompt - extractive body cue:** Given a raw input point cloud x ∈RS×3 with S points, firstly we hybrid Point Prompt P ∈RP ×3 into its 3D space, denoted as ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the key contributions of this work are: (1) We propose GAPrompt, a novel geometry-aware prompt learning method tailored for pre-trained 3D vision models.
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt), specifically designed for parameter-efficient fine-tuning of 3D models.
- **p. 1 / 1. Introduction - extractive body cue:** This advancement has propelled the development of various 3D vision applications, including 3D reconstruction (Xu et al., 2022; Lu et al., 2024) and autonomous driving ...

## Source Evidence Cues

- **p. 4 / 3.1. Point Prompt - extractive body cue:** Then we feed these tokens into our Prompt Propagation mechanism, injecting prompt tokens into the feature extraction process: ˜hi = Prompt-Propagation([hi; pi]), (3) where ˜hi ...
- **p. 4 / 3.1. Point Prompt - extractive body cue:** Furthermore, we adjust the tokens with adapters enhanced by shape feature f. ˆhi, ˆpi = Attn.([˜hi, pi]), (4) hi+1 = ˆhi + Adapter( ˆhi + ...
- **p. 3 / 3.1. Point Prompt - extractive body cue:** This module also generates instance-specific informative shape features f ∈RD, where D is the embedding dimension of transformers, formulated as: ˜x, f = Point-Shift-Prompter(x).
- **p. 5 / 3.2. Point Shift Prompter - extractive body cue:** Firstly, an upsampling strategy is employed to propagate features from center points to neighbor points.
- **p. 5 / 3.2. Point Shift Prompter - extractive body cue:** Then we further process the features with another pointnet: ˜d n j = Pointnet(Propagate(˜dj)), (10) where ˜d n j ∈RCj×Kj×Dj is features of neighbor points ...
- **p. 3 / 3. The Proposed Method - extractive body cue:** As shown in Figure 3, given a pre-trained 3D transformer with N blocks and a specific downstream task, we freeze the backbone and solely update ...
- **Detected method headings:** 2.1. Pre-trained 3D Vision Model (p. 2); 3. The Proposed Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then we feed these tokens into our Prompt Propagation mechanism, injecting prompt tokens into the feature extraction process: ˜hi = Prompt-Propagation([hi; pi]), ... | p. 4 (3.1. Point Prompt), p. 4 (3.1. Point Prompt) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Furthermore, we adjust the tokens with adapters enhanced by shape feature f. ˆhi, ˆpi = Attn.([˜hi, pi]), (4) hi+1 = ˆhi + ... | p. 4 (3.1. Point Prompt), p. 3 (3.1. Point Prompt) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | This module also generates instance-specific informative shape features f ∈RD, where D is the embedding dimension of transformers, formulated as: ˜x, f ... | p. 3 (3.1. Point Prompt), p. 5 (3.2. Point Shift Prompter) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Point Shift Prompter - extractive body cue:** Specifically, to acquire global shape information of point clouds without much computational cost, we utilize a hierarchical downsampling strategy.
- **p. 3 / 3. The Proposed Method - extractive body cue:** As shown in Figure 3, given a pre-trained 3D transformer with N blocks and a specific downstream task, we freeze the backbone and solely update ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3. The Proposed Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Then, feed, tokens, Prompt, Propagation, mechanism, injecting, feature, extraction, process, Prompt-Propagation, where, RLt, propagated | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Then, feed, tokens, Prompt, Propagation, mechanism, injecting, feature, extraction, process | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, GAPrompt, novel, geometry-aware, prompt, learning, tailored, pre-trained, vision | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Specifically, acquire, global, shape, information, point, clouds, without, much, computational | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. Point Prompt - extractive body cue:** Then we feed these tokens into our Prompt Propagation mechanism, injecting prompt tokens into the feature extraction process: ˜hi = Prompt-Propagation([hi; pi]), (3) where ˜hi ...
- **p. 3 / 3.1. Point Prompt - extractive body cue:** Given a raw input point cloud x ∈RS×3 with S points, firstly we hybrid Point Prompt P ∈RP ×3 into its 3D space, denoted as ...
- **p. 4 / 3.1. Point Prompt - extractive body cue:** Then the hybrid point cloud [x; P] becomes prompted input point cloud [˜x; P] ∈R(S+P )×3.
- **p. 5 / 3.2. Point Shift Prompter - extractive body cue:** (8) After k levels of downsampling, we obtain center point features ˜dk ∈RCk×Dk where Ck × Dk = D and concatenate them as shape feature ...
- **p. 2 / 1. Introduction - extractive body cue:** This module extracts global shape information from the original point cloud and shifts the points accordingly, thereby enriching the geometric features at the input level.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach begins with the introduction of a Point Prompt, which explicitly incorporates point cloud data as input, allowing the model to better capture subtle ...
- **p. 1 / 1. Introduction - extractive body cue:** The advent of scanning sensor devices has significantly facilitated the acquisition of 3D point cloud data, an inherently irregular and unstructured geometric representation.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Then we respectively find out neighbor points nj ∈RCj×Kj×3 corresponding to each center with Knearest neighbor (KNN) algorithm: xj+1 = FPS(xj), (6) ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | As shown in Figure 3, the raw input point cloud x is sampled by multi-resolution grouping referring to PointNet++ (Qi et al., ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. The Proposed Method - extractive body cue:** As shown in Figure 3, given a pre-trained 3D transformer with N blocks and a specific downstream task, we freeze the backbone and solely update ...
- **p. 4 / 3.1. Point Prompt - extractive body cue:** Following the original architecture of the pre-trained model, the prompted point cloud is encoded into Lt point tokens h1 by the token embedding module.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, feed, tokens, Prompt, Propagation, mechanism, injecting, feature, extraction, process, Prompt-Propagation, where, RLt, propagated, input, Furthermore, adjust, adapters, enhanced, shape.
- **Relevant PDF headings:** 2.1. Pre-trained 3D Vision Model (p. 2); 3. The Proposed Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The ScanObjectNN (Uy et al., 2019) is a highly challenging 3D dataset comprising 15K real-world objects across 15 categories. | p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study) |
| Semantic / temporal fusion | In terms of FLOPs, our approach adds virtually no extra computational burden compared to baselines, significantly outperforming IDPT and Point-PEFT. | p. 7 (4.2. Quantitative Analysis), p. 6 (4. Experiments) |
| Robot query / planning handoff | In terms of FLOPs, our approach adds virtually no extra computational burden compared to baselines, significantly outperforming IDPT and Point-PEFT. | p. 7 (4.2. Quantitative Analysis), p. 7 (4.2. Quantitative Analysis) |

## Failure and Ablation Link

- **p. 7 / 4.3. Ablation Study - extractive body cue:** We conduct ablation studies on the most challenging PB T50 RS variant based on Point-FEMAE to investigate the rationalization and effectiveness of our GAPrompt.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Ablation study of Prompt Propagation mechanism and prompt enhancing factor βp. Effect of Point Shift Prompter Components. As shown in Table 4, we ...
- **p. 7 / 4.2. Quantitative Analysis - extractive body cue:** The effect of components in our GAPrompt.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Classification on three variants of the ScanObjectNN and the ModelNet40, including the number of trainable parameters (Param) and overall accuracy (Acc). We report ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our GAPrompt compares to full fine-tuning and existing PEFT methods. We compare the classification accuracy on the hardest variant of ScanObjectNN (Uy et ...
- **p. 5 / 3.4. Analysis and Discussion - extractive body cue:** The attention mechanism with prompt integration can be formally expressed as follows: oi = Attn.(WQhi, WKhi, WV hi), (17) ˆoi = Attn.(WQhi, WK[pi, hi], WV ...
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** As demonstrated in Table 1, we conducted experiments on three variants of ScanObjectNN, each with increasing complexity.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Point Prompt), p. 4 (3.1. Point Prompt), p. 3 (3.1. Point Prompt), p. 5 (3.2. Point Shift Prompter), p. 5 (3.2. Point Shift Prompter), p. 3 (3. The Proposed Method), objective p. 4 (3.2. Point Shift Prompter), p. 3 (3. The Proposed Method), temporal p. 4 (3.2. Point Shift Prompter), p. 4 (3.2. Point Shift Prompter), p. 5 (3.3. Prompt Propagation), p. 5 (3.3. Prompt Propagation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
