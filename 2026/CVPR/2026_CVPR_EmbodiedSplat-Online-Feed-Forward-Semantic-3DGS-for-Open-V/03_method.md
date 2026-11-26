# Method - EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat), p. 5 (4.1. EmbodiedSplat), p. 2 (1) They require per-scene optimization that cannot be gen), p. 2 (1) They require per-scene optimization that cannot be gen), p. 6 (Method)): Prior works compress CLIP with encoder-decoder networks [19, 35, 56] or Product Quantization (PQ) [18].

## Method Body Digest

- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** Prior works compress CLIP with encoder-decoder networks [19, 35, 56] or Product Quantization (PQ) [18].
- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** Local st l(i) is then fused with paired global CLIP feature st-1 g (mi) by following the confidenceweighted average from Eq.
- **p. 5 / 4.1. EmbodiedSplat - extractive body cue:** Algorithm 1 Online Fusion of Index/Weight Caches /* Note: Both I and Ωhave fixed length L. */ In : (i, mi) ∈Pt; // Gaussian pair ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** In contrast to existing memory-compression methods such as Auto-encoder [35], Product Quantization (PQ) Index [18] and per-scene optimized codebook [28, 48], our approach requires no ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** Combining those two types of features enable mutual compensation between rich semantics from CLIP and 3D geometric prior from 3D module, resulting in clear performance ...
- **p. 6 / Method - extractive body cue:** Since K ≪M and L is small, this is substantially cheaper than O(MD) which leads to much faster inference (cf.
- **원문 대조:** Text–codebook cosine을 O(KD)에 미리 계산하고 M개 Gaussian마다 최대 L−1개 codebook entry의 sparse weighted sum을 사용해 총 O(KD+M(L−1)) 비용으로 계산한다. 이는 해당 cosine 계산의 복잡도이며 전체 reconstruction 시간은 아니다. ([PDF p. 6](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf#page=6), Method, codebook cosine computation).
- **원문 대조:** Text feature와 K개 global codebook entry의 cosine similarity를 먼저 계산한다. Feature dimension D에 대해 이 단계의 비용은 O(KD)이며 이후 Gaussian별 sparse combination에서 재사용한다. ([PDF p. 6](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf#page=6), Method, codebook cosine computation).

## Design Rationale

- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 FPS ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** To this end, we propose EmbodiedSplat, a novel online framework to endow pretrained feed-forward 3DGS [44] with open-vocabulary capability.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, our objective is to develop an embodied perception model that meets the above five conditions by leveraging 3D Gaussian Splatting (3DGS) [20].

## Source Evidence Cues

- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** Prior works compress CLIP with encoder-decoder networks [19, 35, 56] or Product Quantization (PQ) [18].
- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** Local st l(i) is then fused with paired global CLIP feature st-1 g (mi) by following the confidenceweighted average from Eq.
- **p. 5 / 4.1. EmbodiedSplat - extractive body cue:** Algorithm 1 Online Fusion of Index/Weight Caches /* Note: Both I and Ωhave fixed length L. */ In : (i, mi) ∈Pt; // Gaussian pair ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** In contrast to existing memory-compression methods such as Auto-encoder [35], Product Quantization (PQ) Index [18] and per-scene optimized codebook [28, 48], our approach requires no ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** Combining those two types of features enable mutual compensation between rich semantics from CLIP and 3D geometric prior from 3D module, resulting in clear performance ...
- **p. 6 / Method - extractive body cue:** Since K ≪M and L is small, this is substantially cheaper than O(MD) which leads to much faster inference (cf.
- **Detected method headings:** 4. Our Methods (p. 3); Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Prior works compress CLIP with encoder-decoder networks [19, 35, 56] or Product Quantization (PQ) [18]. | p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Local st l(i) is then fused with paired global CLIP feature st-1 g (mi) by following the confidenceweighted average from Eq. | p. 4 (4.1. EmbodiedSplat), p. 5 (4.1. EmbodiedSplat) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Algorithm 1 Online Fusion of Index/Weight Caches /* Note: Both I and Ωhave fixed length L. */ In : (i, mi) ∈Pt; ... | p. 5 (4.1. EmbodiedSplat), p. 2 (1) They require per-scene optimization that cannot be gen) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **원문 대조:** Text–codebook cosine을 O(KD)에 미리 계산하고 M개 Gaussian마다 최대 L−1개 codebook entry의 sparse weighted sum을 사용해 총 O(KD+M(L−1)) 비용으로 계산한다. 이는 해당 cosine 계산의 복잡도이며 전체 reconstruction 시간은 아니다. ([PDF p. 6](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf#page=6), Method, codebook cosine computation).
- **원문 대조:** Text feature와 K개 global codebook entry의 cosine similarity를 먼저 계산한다. Feature dimension D에 대해 이 단계의 비용은 O(KD)이며 이후 Gaussian별 sparse combination에서 재사용한다. ([PDF p. 6](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf#page=6), Method, codebook cosine computation).
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** In contrast to existing memory-compression methods such as Auto-encoder [35], Product Quantization (PQ) Index [18] and per-scene optimized codebook [28, 48], our approach requires no ...
- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** This design: 1) does not require any pretraining or per-scene optimization, 2) effectively reduces memory while preserving original openvocabulary semantics of CLIP, and 3) supports ...
- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** It accumulates related codebook indices and weights over the time steps for each Gaussian (Lines 1-4) while the weights are updated based on the confidence-weighted ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** However, it still requires heavy per-scene optimization, failing to achieve real-time semantic reconstruction (< 2FPS).
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (1) They require per-scene optimization that cannot be gen), p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat), p. 5 (4.1. EmbodiedSplat), p. 6 (Method), p. 6 (Method).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, embodied, agent, equipped, precise, SLAM, system, collects, posed, RGB, RGB-D, images, understand, scene | 연속 RGB 영상, 조건별 측정 깊이 및 텍스트 클래스 | body cue; exact tensor/frame verify |
| State/latent | Specifically, embodied, agent, equipped, precise, SLAM, system, collects, posed, RGB | 3D 가우시안의 기하 특징과 의미 코드북 계수 | body cue; notation verify |
| Action/output | contributions, follows, Novel, framework, embodied, perception, enables, online, whole-scene, reconstruction | 텍스트 질의에 따른 의미 분할 | body cue; unit/decoder verify |
| Objective/constraint | resulting, total, cost, L-1, precompute, global, codebook, where, size, contrast | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive body cue:** Specifically, the embodied agent equipped with a precise SLAM system collects posed RGB or RGB-D images to understand the 3D scene, follow human instructions, and ...
- **p. 3 / 3. Preliminaries - extractive body cue:** With It and the N reference views as input, the CNN encoder E predicts pixelwise local Gaussian triplets Θt l = {µt l, ωt l, ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since FreeSplat++ is designed for offline use, we modify its inference pipeline to enable online perception from streaming images: 1) Input selection.
- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** The key observation is that the number of unique semantics in a scene is far smaller than the number of Gaussians [28].
- **p. 1 / 1. Introduction - extractive body cue:** 4) Whole-scene Understanding: Reconstructing and interpreting large-scale 3D scenes are demanded to perform long-term actions.
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** Nonetheless, it does not support online settings or full-scene reconstruction as it operates with only two or a few input views.
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** LSM [12] and SIU3R [49] propose language-embedded feed-forward 3DGS that can be easily generalized to the new scene.
- **Normalized interface:** observation=연속 RGB 영상, 조건별 측정 깊이 및 텍스트 클래스; state=3D 가우시안의 기하 특징과 의미 코드북 계수; output/action=텍스트 질의에 따른 의미 분할.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 1) To warm up the model, we first train our EmbodiedSplat as single-view perception model by using the individual RGB frames with ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Given the current frame It ∈RH×W ×3, we select N past frames from time steps t-N to t-1 to reflect the online ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | This design: 1) does not require any pretraining or per-scene optimization, 2) effectively reduces memory while preserving original openvocabulary semantics of CLIP, ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | 4) By combining the real-time 2D models, our EmbodiedSplat-fast shows nearly real-time reconstruction speed that is 5-6 FPS of per-frame processing time. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. EmbodiedSplat - extractive body cue:** Algorithm 1 Online Fusion of Index/Weight Caches /* Note: Both I and Ωhave fixed length L. */ In : (i, mi) ∈Pt; // Gaussian pair ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** In contrast to existing memory-compression methods such as Auto-encoder [35], Product Quantization (PQ) Index [18] and per-scene optimized codebook [28, 48], our approach requires no ...
- **p. 6 / Method - extractive body cue:** Since K ≪M and L is small, this is substantially cheaper than O(MD) which leads to much faster inference (cf.
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** To this end, we propose a novel Online Sparse Coefficient Field with CLIP Global Codebook which stores per-Gaussian semantics in a memory-efficient manner.

## Method-Specific Formal Details

- **Body-defined terms:** Prior, works, compress, CLIP, encoder-decoder, networks, Product, Quantization, Local, then, fused, paired, global, feature, st-1, following, confidenceweighted, average, Algorithm, Online.
- **Relevant PDF headings:** 4. Our Methods (p. 3); Method (p. 6).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to ... | p. 7 (5.1. Experimental Results), p. 6 (5. Experiments) |
| Semantic / temporal fusion | Our EmbodiedSplat demonstrates better segmentation quality compared to the baselines, while combining the ground-truth depths (EmbodiedSplat-D) further enhances the quality of the ... | p. 7 (5.1. Experimental Results), p. 3 (Figure/Table caption) |
| Robot query / planning handoff | Table 1. Quantitative comparisons on 3D Semantic Segmentation across ScanNet [6], ScanNet200 [38] and ScanNet++ [53]. We compare the performance of our ... | p. 6 (Figure/Table caption), p. 8 (5.2. Ablation Studies) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Online 3D reasoning for class "Bed". tures to each Gaussian, but incurs heavy memory overhead (2295 MB) due to the high dimensionality of ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** Ablations on codebook-based cosine similarity Methods Type / Feature dimension Size (MB) pretraining information loss LangSplat [35] Auto-encoder / 3 30 ✓ ✓ Dr.
- **p. 6 / 5. Experiments - extractive body cue:** Specifically, the model is trained for 50,000 iterations without memory adapter.
- **p. 6 / 5. Experiments - extractive body cue:** Following [18], we modify their inference strategy to support direct 3D referring operation without rendering 2D feature maps.
- **p. 7 / 5.1. Experimental Results - extractive body cue:** Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** Splat [18] shares the same limitations.
- **p. 7 / 5.1. Experimental Results - extractive body cue:** Our model shows strong semantics generalizability in ScanNet++ →ScanNet transfer with performance degradation remaining below 1 mIoU compared to ScanNet →ScanNet setting in Tab.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat), p. 5 (4.1. EmbodiedSplat), p. 2 (1) They require per-scene optimization that cannot be gen), p. 2 (1) They require per-scene optimization that cannot be gen), p. 6 (Method), objective p. 6 (Method), p. 6 (Method), p. 2 (1) They require per-scene optimization that cannot be gen), p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat), p. 2 (1) They require per-scene optimization that cannot be gen), temporal p. 6 (5. Experiments), p. 3 (3. Preliminaries), p. 4 (4.1. EmbodiedSplat), p. 7 (5.1. Experimental Results), p. 2 (1) They require per-scene optimization that cannot be gen), p. 4 (4.1. EmbodiedSplat).
