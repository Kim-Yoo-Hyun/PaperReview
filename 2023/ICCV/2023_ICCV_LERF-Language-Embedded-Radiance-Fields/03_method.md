# Method - LERF: Language Embedded Radiance Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.09553; PDF retrieval source: https://arxiv.org/pdf/2303.09553. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3.4. Field Architecture), p. 7 (3.6. Implementation Details), p. 7 (3.6. Implementation Details), p. 6 (3.4. Field Architecture)): We capture this inductive bias in LERF by training two separate networks: one for feature vectors (DINO, CLIP), and the other for standard NeRF outputs (color, density).

## Method Body Digest

- **p. 6 / 3.4. Field Architecture - extractive body cue:** We capture this inductive bias in LERF by training two separate networks: one for feature vectors (DINO, CLIP), and the other for standard NeRF outputs ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the Adam optimizer for proposal networks and fields with weight decay 10-9, with an exponential learning rate scheduler from 10-2 to 10-3 over ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to smin = .5 ...
- **p. 6 / 3.4. Field Architecture - extractive body cue:** Scale s is passed into the CLIP MLP as an extra input in addition to the concatenated hashgrid features.
- **p. 6 / 3.4. Field Architecture - extractive body cue:** Gradients from Llang and Ldino do not affect the NeRF outputs, and can be viewed as jointly optimizing a language field in conjunction with a ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** The λ used in weighting CLIP loss is 0.01, chosen empirically and ablated in Sec 4.4.
- **p. 6 / 3.4. Field Architecture - extractive body cue:** Intuitively, optimizing a language embedding in 3D should not influence the distribution of density in the underlying scene representation.
- **p. 2 / 1. Introduction - extractive body cue:** We construct a LERF by optimizing a language field jointly with NeRF, which takes both position and physical scale as input and outputs a single ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose Language Embedded Radiance Fields (LERF), a novel approach that grounds language within NeRF by optimizing embeddings from an offthe-shelf vision-language ...
- **p. 2 / 1. Introduction - extractive body cue:** Upon completion of the training process, LERF allows for the generation of 3D relevancy maps for a wide range of language prompts in realtime.
- **p. 6 / 3.4. Field Architecture - extractive body cue:** We adopt the Nerfacto method from Nerfstudio [35] as the backbone for our approach, leveraging the same proposal sampling, scene contraction, and appearance embeddings

## Source Evidence Cues

- **p. 6 / 3.4. Field Architecture - extractive body cue:** We capture this inductive bias in LERF by training two separate networks: one for feature vectors (DINO, CLIP), and the other for standard NeRF outputs ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the Adam optimizer for proposal networks and fields with weight decay 10-9, with an exponential learning rate scheduler from 10-2 to 10-3 over ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to smin = .5 ...
- **p. 6 / 3.4. Field Architecture - extractive body cue:** Scale s is passed into the CLIP MLP as an extra input in addition to the concatenated hashgrid features.
- **Detected method headings:** 3.4. Field Architecture (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We capture this inductive bias in LERF by training two separate networks: one for feature vectors (DINO, CLIP), and the other for ... | p. 6 (3.4. Field Architecture), p. 7 (3.6. Implementation Details) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We use the Adam optimizer for proposal networks and fields with weight decay 10-9, with an exponential learning rate scheduler from 10-2 ... | p. 7 (3.6. Implementation Details), p. 7 (3.6. Implementation Details) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to ... | p. 7 (3.6. Implementation Details), p. 6 (3.4. Field Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.4. Field Architecture - extractive body cue:** Gradients from Llang and Ldino do not affect the NeRF outputs, and can be viewed as jointly optimizing a language field in conjunction with a ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** The λ used in weighting CLIP loss is 0.01, chosen empirically and ablated in Sec 4.4.
- **p. 6 / 3.4. Field Architecture - extractive body cue:** Intuitively, optimizing a language embedding in 3D should not influence the distribution of density in the underlying scene representation.
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the Adam optimizer for proposal networks and fields with weight decay 10-9, with an exponential learning rate scheduler from 10-2 to 10-3 over ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3.4. Field Architecture), p. 7 (3.6. Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | construct, LERF, optimizing, language, field, jointly, NeRF, takes, position, physical, scale, input, outputs, single | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | construct, LERF, optimizing, language, field, jointly, NeRF, takes, position, physical | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Language, Embedded, Radiance, Fields, LERF, novel, grounds, within, NeRF, optimizing | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Gradients, Llang, Ldino, affect, NeRF, outputs, viewed, jointly, optimizing, language | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** We construct a LERF by optimizing a language field jointly with NeRF, which takes both position and physical scale as input and outputs a single ...
- **p. 2 / 1. Introduction - extractive body cue:** This requires not only the capacity to handle natural language input queries but also the ability to incorporate semantics at multiple scales and relate to ...
- **p. 6 / 3.4. Field Architecture - extractive body cue:** The language hashgrid has two output MLPs for CLIP and DINO respectively.
- **p. 6 / 3.4. Field Architecture - extractive body cue:** Gradients from Llang and Ldino do not affect the NeRF outputs, and can be viewed as jointly optimizing a language field in conjunction with a ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** The CLIP MLP used for Flang has 3 hidden layers with width 256 before the final 512 dimension CLIP output.
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to smin = .5 ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We train on an NVIDIA A100, which takes roughly 20GB of memory total. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | One can interactively query in real-time within the Nerfstudio viewer. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | We train on an NVIDIA A100, which takes roughly 20GB of memory total. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3.4. Field Architecture - extractive body cue:** We capture this inductive bias in LERF by training two separate networks: one for feature vectors (DINO, CLIP), and the other for standard NeRF outputs ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the Adam optimizer for proposal networks and fields with weight decay 10-9, with an exponential learning rate scheduler from 10-2 to 10-3 over ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to smin = .5 ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the Adam optimizer for proposal networks and fields with weight decay 10-9, with an exponential learning rate scheduler from 10-2 to 10-3 over ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to smin = .5 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** capture, inductive, bias, LERF, training, separate, networks, feature, vectors, DINO, CLIP, other, standard, NeRF, outputs, color, density, Adam, optimizer, proposal.
- **Relevant PDF headings:** 3.4. Field Architecture (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Emphasizing the capability of LERF to handle real-world data, we collect 13 scenes containing a mixture of in-the-wild (grocery store, kitchen, bookstore) ... | p. 7 (4. Experiments), p. 7 (4. Experiments) |
| Semantic / temporal fusion | OwL-ViT outperforms LSeg in 3D, but suffers compared to LERF on long-tail queries. | p. 8 (4.3. Localization), p. 8 (4.3. Localization) |
| Robot query / planning handoff | OwL-ViT outperforms LSeg in 3D, but suffers compared to LERF on long-tail queries. | p. 8 (4.3. Localization), p. 8 (4.4. Ablations) |

## Failure and Ablation Link

- **p. 7 / 4. Experiments - extractive body cue:** Though existing 3D scan datasets exist, they tend to be either of singulated objects [29, 13], or are RGB-D scans without enough views to optimize ...
- **p. 8 / 4.2. Existence Determination - extractive body cue:** We remove scale as a parameter to Flang for LSeg since it outputs pixel-aligned features.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Ablations: We ablate DINO regularization and multi- scale training (Sec. 4.4), and highlight qualitative degradation in relevancy maps here. by a constant λlang ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 15: Geometric separation impacts quality: Queries without much geometric separation can blur between objects and foreground-background. In the toaster case, very few viewing an- ...
- **p. 8 / 4.4. Ablations - extractive body cue:** No DINO: Removing DINO results in a qualitative deterioration in the smoothness and boundaries of relevancy maps, especially in regions with few surrounding views or ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: LERF Optimization: Left: LERF represents a field of 3D volumes, parameterized by position x, y, z and scale s (orange cube). To render ...
- **p. 8 / 5. Limitations - extractive body cue:** LERF has limitations associated with both CLIP and NeRF; some are visualized in Fig.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3.4. Field Architecture), p. 7 (3.6. Implementation Details), p. 7 (3.6. Implementation Details), p. 6 (3.4. Field Architecture), objective p. 6 (3.4. Field Architecture), p. 7 (3.6. Implementation Details), p. 6 (3.4. Field Architecture), p. 7 (3.6. Implementation Details), temporal p. 7 (3.6. Implementation Details), p. 7 (3.6. Implementation Details), p. 1 (Body text (section not recovered)), p. 1 (Abstract), p. 2 (2. Related Work), p. 3 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
