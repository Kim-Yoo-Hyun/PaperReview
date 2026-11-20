# EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Seungjun Lee, Zihan Wang, Yunsong Wang, Gim Hee Lee
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, open-vocabulary, semantic
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Nevertheless, all of them share two limitations in embodied scenarios:를 문제로 두고, Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 FPS inference speed. • Combination of 2D CLIP ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Understanding a 3D scene immediately with its exploration is essential for embodied tasks, where an agent must construct and comprehend the 3D representation in an ...
- **p. 1 / Abstract - extractive body cue:** In this study, we propose EmbodiedSplat, an online feed-forward 3DGS for open-vocabulary scene understanding that enables simultaneous online 3D reconstruction and 3D semantic understanding from ...
- **p. 1 / Abstract - extractive body cue:** Unlike existing openvocabulary 3DGS methods, our objectives are two-fold: 1) Reconstructs the semantic-embedded 3DGS of the entire scene from over 300 streaming images in an ...
- **p. 1 / 1. Introduction - extractive body cue:** Embodied tasks such as robotic manipulation and navigation [3, 25, 32, 45, 46, 54, 55, 57] require an agent to perceive the 3D scene immediately ...
- **p. 1 / 1. Introduction - extractive body cue:** Specifically, the embodied agent equipped with a precise SLAM system collects posed RGB or RGB-D images to understand the 3D scene, follow human instructions, and ...
- **p. 2 / 1. Introduction - extractive body cue:** Nevertheless, all of them share two limitations in embodied scenarios:
- **p. 1 / 1. Introduction - extractive body cue:** 3DGS is the recent 3D representation that supports real-time novel view synthesis with explicit structure which existing repreThis CVPR paper is the Open Access version, ...

## Core Idea

- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 FPS ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** To this end, we propose EmbodiedSplat, a novel online framework to endow pretrained feed-forward 3DGS [44] with open-vocabulary capability.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, our objective is to develop an embodied perception model that meets the above five conditions by leveraging 3D Gaussian Splatting (3DGS) [20].
- **p. 1 / 1. Introduction - extractive body cue:** 3DGS is the recent 3D representation that supports real-time novel view synthesis with explicit structure which existing repreThis CVPR paper is the Open Access version, ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since FreeSplat++ is designed for offline use, we modify its inference pipeline to enable online perception from streaming images: 1) Input selection.
- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** Prior works compress CLIP with encoder-decoder networks [19, 35, 56] or Product Quantization (PQ) [18].
- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** Local st l(i) is then fused with paired global CLIP feature st-1 g (mi) by following the confidenceweighted average from Eq.
- **p. 5 / 4.1. EmbodiedSplat - extractive body cue:** Algorithm 1 Online Fusion of Index/Weight Caches /* Note: Both I and Ωhave fixed length L. */ In : (i, mi) ∈Pt; // Gaussian pair ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, the embodied agent equipped with a precise SLAM system collects posed RGB or RGB-D images to understand the 3D scene, follow human instructions, and make autonomous decisions based on its own ... | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 3 (3. Preliminaries) |
| State/latent | Specifically, embodied, agent, equipped, precise, SLAM, system, collects, posed, RGB, RGB-D, images | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries) |
| Output/action | With It and the N reference views as input, the CNN encoder E predicts pixelwise local Gaussian triplets Θt l = {µt l, ωt l, f t l } and a depth ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4.1. EmbodiedSplat) |
| Cosine-query computational cost | 원문 대조: Text–codebook cosine을 O(KD)에 미리 계산하고 M개 Gaussian마다 최대 L−1개 codebook entry의 sparse weighted sum을 사용해 총 O(KD+M(L−1)) 비용으로 계산한다. 이는 해당 cosine 계산의 복잡도이며 전체 reconstruction 시간은 아니다. ([PDF p. 6](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf#page=6), Method, codebook cosine computation) | Codebook query 복잡도; robot behavior metric 아님 | [PDF p. 6](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf#page=6), Method, codebook cosine computation |

## Main Claims and Actual Contribution

- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 FPS ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** To this end, we propose EmbodiedSplat, a novel online framework to endow pretrained feed-forward 3DGS [44] with open-vocabulary capability.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, our objective is to develop an embodied perception model that meets the above five conditions by leveraging 3D Gaussian Splatting (3DGS) [20].
- **p. 1 / 1. Introduction - extractive body cue:** 3DGS is the recent 3D representation that supports real-time novel view synthesis with explicit structure which existing repreThis CVPR paper is the Open Access version, ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since FreeSplat++ is designed for offline use, we modify its inference pipeline to enable online perception from streaming images: 1) Input selection.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons on 3D Semantic Segmentation across ScanNet [6], ScanNet200 [38] and ScanNet++ [53]. We compare the performance of our EmbodiedSplat with existing ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** 4, our codebook-based cosine similarity (2nd row) significantly improves efficiency, achieving nearly 14× faster processing speed compared to the naive per-Gaussian cosine similarity computation (1st ...
- **p. 7 / 5.1. Experimental Results - extractive body cue:** Nevertheless, our model achieves performance comparable to clustering-based baselines [28, 48].

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 8 (5.2. Ablation Studies) |
| Embodiment/environment | Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization methods. | hardware/simulator version and reset protocol | p. 7 (5.1. Experimental Results), p. 6 (5. Experiments) |
| Dataset/benchmark | ScanNetv2 [6] is a large-scale RGB-D and point clouds dataset with 1,513 indoor scenes which also provides semantic annotations for 20 classes. | role, split, size and leakage | p. 7 (5.1. Experimental Results), p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.1. Experimental Results) |
| Metric | For each time step, we prune top L -1 indices by the confidence scores as described in Algorithm. | definition, denominator, direction and uncertainty | p. 8 (5.2. Ablation Studies), p. 6 (Figure/Table caption), p. 7 (5.2. Ablation Studies) |
| Baseline/ablation | Our EmbodiedSplat demonstrates better segmentation quality compared to the baselines, while combining the ground-truth depths (EmbodiedSplat-D) further enhances the quality of the visualization. | fair input/data/compute/action matching | p. 7 (5.1. Experimental Results), p. 3 (Figure/Table caption), p. 6 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.1. Experimental Results - extractive body cue:** Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** Splat [18] shares the same limitations.
- **p. 7 / 5.1. Experimental Results - extractive body cue:** Our model shows strong semantics generalizability in ScanNet++ →ScanNet transfer with performance degradation remaining below 1 mIoU compared to ScanNet →ScanNet setting in Tab.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Nevertheless, all of them share two limitations in embodied scenarios:를 문제로 두고, Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 FPS inference speed. • Combination of 2D CLIP ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
