# Method - Ov3R: Open-Vocabulary Semantic 3D Reconstruction from RGB Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.2. 2D-3D OVS), p. 3 (3. Method), p. 3 (3.1. CLIP3R), p. 5 (3.2. 2D-3D OVS), p. 4 (3.1. CLIP3R), p. 4 (3.1. CLIP3R)): Therefore, we introduce a 2D-3D fused descriptor that combines these three complementary feature types extracted from i) CLIP3R, ii) DINO, and iii) a 3D-CLIP encoder [21]: i) To capture the ...

## Method Body Digest

- **p. 5 / 3.2. 2D-3D OVS - extractive PDF cue:** Therefore, we introduce a 2D-3D fused descriptor that combines these three complementary feature types extracted from i) CLIP3R, ii) DINO, and iii) a 3D-CLIP encoder ...
- **p. 3 / 3. Method - extractive PDF cue:** It consists of two main components, highlighted in yellow and blue: (i) a CLIP-informed 3Rbased model (CLIP3R) and (ii) a 2D-3D OVS module.
- **p. 3 / 3.1. CLIP3R - extractive PDF cue:** We introduce CLIP3R, a CLIP-informed 3D reconstruction model that integrates the rich semantic understanding embedded in CLIP features and enables open-vocabulary semantic segmentation as a ...
- **p. 5 / 3.2. 2D-3D OVS - extractive PDF cue:** Dscene = Fscene CLIP3R + Fscene cat + softmax(Fscene CLIP3R · Fscene T cat √ d ) · Fscene cat (9) Dinst = Finst CLIP3R+Finst ...
- **p. 4 / 3.1. CLIP3R - extractive PDF cue:** These features are then processed by the keyframe decoder Dkey and the supporting decoder Dsup from the original I2P.
- **p. 4 / 3.1. CLIP3R - extractive PDF cue:** Then, FoCLIP and Fvit are processed through cross-attention to obtain the fused features Ffuse, which are added to FViT.
- **p. 6 / Method - extractive PDF cue:** The weights wi are obtained by a shallow model comprising a cross-attention layer, an MLP, and a softmax layer.
- **p. 4 / 3.1. CLIP3R - extractive PDF cue:** The former is similar to the loss used to supervise I2P: LL2W = L X i=1 Mi · ( ˆC · // ˆP ′ i ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions are as follows: • We present Ov3R, a novel framework that unifies 3R models and open-vocabulary 3D semantic segmentation. • We design ...
- **p. 3 / 3.1. CLIP3R - extractive PDF cue:** We introduce CLIP3R, a CLIP-informed 3D reconstruction model that integrates the rich semantic understanding embedded in CLIP features and enables open-vocabulary semantic segmentation as a ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we introduce Ov3R, an open-vocabulary semantic 3D reconstruction framework that processes RGBonly video streams.

## Source Evidence Cues

- **p. 5 / 3.2. 2D-3D OVS - extractive PDF cue:** Therefore, we introduce a 2D-3D fused descriptor that combines these three complementary feature types extracted from i) CLIP3R, ii) DINO, and iii) a 3D-CLIP encoder ...
- **p. 3 / 3. Method - extractive PDF cue:** It consists of two main components, highlighted in yellow and blue: (i) a CLIP-informed 3Rbased model (CLIP3R) and (ii) a 2D-3D OVS module.
- **p. 3 / 3.1. CLIP3R - extractive PDF cue:** We introduce CLIP3R, a CLIP-informed 3D reconstruction model that integrates the rich semantic understanding embedded in CLIP features and enables open-vocabulary semantic segmentation as a ...
- **p. 5 / 3.2. 2D-3D OVS - extractive PDF cue:** Dscene = Fscene CLIP3R + Fscene cat + softmax(Fscene CLIP3R · Fscene T cat √ d ) · Fscene cat (9) Dinst = Finst CLIP3R+Finst ...
- **p. 4 / 3.1. CLIP3R - extractive PDF cue:** These features are then processed by the keyframe decoder Dkey and the supporting decoder Dsup from the original I2P.
- **p. 4 / 3.1. CLIP3R - extractive PDF cue:** Then, FoCLIP and Fvit are processed through cross-attention to obtain the fused features Ffuse, which are added to FViT.
- **p. 6 / Method - extractive PDF cue:** The weights wi are obtained by a shallow model comprising a cross-attention layer, an MLP, and a softmax layer.
- **Detected method headings:** 3. Method (p. 3); Method (p. 6); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Therefore, we introduce a 2D-3D fused descriptor that combines these three complementary feature types extracted from i) CLIP3R, ii) DINO, and iii) ... | p. 5 (3.2. 2D-3D OVS), p. 3 (3. Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | It consists of two main components, highlighted in yellow and blue: (i) a CLIP-informed 3Rbased model (CLIP3R) and (ii) a 2D-3D OVS ... | p. 3 (3. Method), p. 3 (3.1. CLIP3R) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We introduce CLIP3R, a CLIP-informed 3D reconstruction model that integrates the rich semantic understanding embedded in CLIP features and enables open-vocabulary semantic ... | p. 3 (3.1. CLIP3R), p. 5 (3.2. 2D-3D OVS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. CLIP3R - extractive PDF cue:** The former is similar to the loss used to supervise I2P: LL2W = L X i=1 Mi · ( ˆC · // ˆP ′ i ...
- **p. 6 / Method - extractive PDF cue:** We pre-trained our 2D-3D fusion model by minimizing the sigmoid cosine similarity loss: Lsim = -1 /B/ /B/ X i /B/ X j log  ...
- **p. 4 / 3.1. CLIP3R - extractive PDF cue:** The revised I2P network is trained endto-end through a confidence-aware loss over ground truth scene points: LI2P = L X i=1 Mi · (C · ...
- **p. 8 / 4.5. Runtime Analysis - extractive PDF cue:** However, we argue that replacing SAM2 with faster variants [62] would allow Ov3R to meet real-time constraints.
- **p. 7 / 4.2. Camera Tracking - extractive PDF cue:** Only VGGTSLAM achieves better results on 7Scenes, thanks to the SL(4) optimization performed outside of the model.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.1. CLIP3R), p. 4 (3.1. CLIP3R), p. 6 (Method), p. 8 (4.5. Runtime Analysis).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | main, contributions, follows, present, Ov3R, novel, framework, unifies, models, open-vocabulary, semantic, segmentation, design, CLIP3R | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | main, contributions, follows, present, Ov3R, novel, framework, unifies, models, open-vocabulary | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, follows, present, Ov3R, novel, framework, unifies, models, open-vocabulary | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | former, similar, loss, supervise, I2P, LL2W, Pi//1, while, latter, minimizes | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions are as follows: • We present Ov3R, a novel framework that unifies 3R models and open-vocabulary 3D semantic segmentation. • We design ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The latter flavor is the most suitable approach for developing Spatial AI systems, although it poses greater challenges compared to offline methods, as input images ...
- **p. 5 / 3.2. 2D-3D OVS - extractive PDF cue:** This 3D encoder is pre-trained on triplets of point clouds, corresponding images, and text using natural language supervision.
- **p. 7 / Method - extractive PDF cue:** Overall, Ov3R outperforms all state-of-the-art methods while maintaining up to 15 FPS processing speed.
- **p. 3 / 3.1. CLIP3R - extractive PDF cue:** Finally, the object-level features F(H×W ×D) oCLIP are obtained by combining the individual CLIP features obtained from the M masked images within a single features ...
- **p. 7 / 4.3. Open-Vocabulary 3D Semantic Segmentation - extractive PDF cue:** We conduct experiments under two different settings: segmentation performed on geometry reconstructed from (i) ground truth depth maps, simulating an offline setting, and (ii) RGB-only ...
- **p. 2 / 1. Introduction - extractive PDF cue:** struction pipelines [24, 39-41, 49, 51] or RGBD SLAM methods that require depth sensors [36], and therefore do not address the aforementioned gap.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Methods are grouped into: 3R methods with low FPS, SLAM approaches, and real-time 3R models. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We adopt standard metrics including Accuracy (cm), completion (cm) for 3D reconstruction, Absolute Trajectory Error (ATE RMSE) for tracking accuracy, and Frame ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The 2D-3D OVS model is trained for 15 epochs, with batch size 512. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4. Experiments - extractive PDF cue:** The 2D-3D OVS model is trained for 15 epochs, with batch size 512.
- **p. 6 / Method - extractive PDF cue:** At inference time, the similarity between fused descriptors and a set of text embeddings corresponding to semantic classes is computed to select the class with ...
- **p. 5 / 3.2. 2D-3D OVS - extractive PDF cue:** This 3D encoder is pre-trained on triplets of point clouds, corresponding images, and text using natural language supervision.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Therefore, introduce, D-3D, fused, descriptor, combines, three, complementary, feature, types, extracted, CLIP3R, DINO, D-CLIP, encoder, capture, relationship, between, local, global.
- **Relevant PDF headings:** 3. Method (p. 3); Method (p. 6); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For the 3D reconstruction task, we follow [35] and train CLIP3R on ScanNet++ [58], Aria Synthetic Environments [2], and CO3D-v2 [44], which ... | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Semantic / temporal fusion | Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: ... | p. 7 (Figure/Table caption), p. 6 (4.1. 3D Reconstruction) |
| Robot query / planning handoff | Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 4.5. Runtime Analysis - extractive PDF cue:** However, we argue that replacing SAM2 with faster variants [62] would allow Ov3R to meet real-time constraints.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. 2D-3D OVS Overview. After matching 2D and 3D segments across images and pointmaps, CLIP3R, DINO, and 3D-CLIP features are combined into a 2D-3D ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation study of CLIP3R on Replica. We study the impact of CLIP-insertion in I2P (CLIP-insert) and the CLIP- semantic supervision in L2W (CLIP ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. Ablation study of 2D-3D OV. We report the advance- ment brought by different fusion strategies. shown in Figure 6, Ov3R accurately identifies the ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** Ov3R inherits one of the limitations of 3R models, i.e., the suboptimal accuracy of the retrieved camera poses.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Future research will aim to overcome this limitation by integrating techniques from the SLAM literature, such as global bundle adjustment.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. 2D-3D OVS Overview. After matching 2D and 3D segments across images and pointmaps, CLIP3R, DINO, and 3D-CLIP features are combined into a 2D-3D ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.2. 2D-3D OVS), p. 3 (3. Method), p. 3 (3.1. CLIP3R), p. 5 (3.2. 2D-3D OVS), p. 4 (3.1. CLIP3R), p. 4 (3.1. CLIP3R), objective p. 4 (3.1. CLIP3R), p. 6 (Method), p. 4 (3.1. CLIP3R), p. 8 (4.5. Runtime Analysis), p. 7 (4.2. Camera Tracking), temporal p. 6 (Method), p. 6 (4. Experiments), p. 7 (Method), p. 7 (4.2. Camera Tracking), p. 8 (4.4. Ablation Study), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
