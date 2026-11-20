# GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Jiahao Yang, Zihan Wang, Xiangyang Li, Xing Zhu, Yujun Shen, Yinghao Xu, Shuqiang Jiang
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Navigation, geometry, BEV
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

문제 관련 발췌 — (A) Dense image-based representations contain heavy token redundancy and lack explicit spatial structure.

방법 관련 발췌 — Our main contributions are summarized as follows: • We propose Geometry-Aware BEV (GA-BEV), a compact and 3D-grounded representation that combines explicit depth-based projected features with implicit geometric priors from pretrained 3D ...

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Despite significant progress in Vision-Language Navigation (VLN), existing approaches still rely on dense RGB videos that produce excessive patch tokens and lack explicit spatial structure, ...
- **p. 1 / Abstract - extractive body cue:** To address these issues, we introduce the Geometry-Aware BEV (GABEV) - a compact, 3D-grounded feature representation that integrates both explicit and implicit geometric cues into ...
- **p. 1 / Abstract - extractive body cue:** We construct BEV spatial maps from RGBD inputs by projecting visual features into 3D space and aggregating them into an agent-centric layout that preserves geometric ...
- **p. 1 / Abstract - extractive body cue:** To further enrich geometric understanding, we incorporate features from a pretrained 3D foundation model into the BEV space, injecting structural priors learned from large-scale 3D ...
- **p. 1 / Abstract - extractive body cue:** Together, these complementary cues - explicit depth-based projection and implicit learned priors - yield compact yet spatially expressive representations that substantially improve navigation efficiency and ...
- **p. 1 / 1. Introduction - extractive body cue:** (A) Dense image-based representations contain heavy token redundancy and lack explicit spatial structure.
- **p. 1 / 1. Introduction - extractive body cue:** While effective to some extent, this imagecentric paradigm lacks explicit spatial structure and treats visual observations as flat patch embeddings without modeling geometric relationships across ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose Geometry-Aware BEV (GA-BEV), a compact and 3D-grounded representation that combines explicit depth-based projected features with ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose the GeometryAware BEV (GA-BEV) - a compact and spatially grounded feature representation that integrates explicit and implicit geometric cues ...
- **p. 3 / 3. Methods - extractive body cue:** We propose the Geometry-Aware Vision-Language Navigation (GA-VLN) framework, which incorporates a Geometry-Aware BEV (GA-BEV) - a compact and 3Dgrounded spatial representation that transforms RGB-D observations ...
- **p. 4 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** To address this, we introduce the Grid-Based BEV Aggregation method for efficient aggregation and making the representation more suitable for the navigation task.
- **p. 4 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** To incorporate broader 3D geometric priors for better spatial reasoning, we introduce representation from a pretrained 3D foundation model (e.g., VGGT [27]) f3DFM(·), which encodes ...
- **p. 5 / 3.3. Geometry-Aware VLN Framework - extractive body cue:** In the first round, the model is conditioned on the language instruction, the current front-view image, and a unified BEV feature aggregated from up to ...
- **p. 5 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** It is also worth noting that although we introduce the additional t × Hg × Wg geometry tokens from 3D foundation models, the grid-based aggregation ...
- **원문 대조:** 과거 image sequence를 pretrained 3D foundation model에 넣어 implicit multi-view geometry를 포함한 patch feature를 얻는다. 이후 projection layer로 visual feature 차원을 맞추고 depth-guided projection과 BEV aggregation에 사용한다. ([PDF p. 4](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.pdf#page=4), §3.2 Implicit 3D Geometry Priors, Eq. (2)).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the first round, the model is conditioned on the language instruction, the current front-view image, and a unified BEV feature aggregated from up to eight historical observations. | camera/depth stream, pose, map와 language goal | p. 5 (3.3. Geometry-Aware VLN Framework), p. 1 (1. Introduction) |
| State/latent | first, round, model, conditioned, language, instruction, current, front-view, image, unified, BEV, feature | robot pose, free-space/semantic map와 local goal | p. 5 (3.3. Geometry-Aware VLN Framework), p. 1 (1. Introduction), p. 4 (3.1. Preliminary) |
| Output/action | Recent advances in multimodal large language models (MLLMs) [17, 48] have greatly enhanced agents' abilities to comprehend instructions, ground them in visual contexts, and predict coherent action sequences. … (A) Dense Image-Based ... | collision-free trajectory 또는 velocity command | p. 1 (1. Introduction), p. 4 (3.1. Preliminary), p. 4 (3.1. Preliminary) |
| Objective/outcome | To minimize computational overhead, the second round queries the model using only the newly updated front-view image while reusing the BEV feature from the first round. | goal reach, safety, localization error와 replanning latency | p. 5 (3.3. Geometry-Aware VLN Framework), p. 4 (3.2. Geometry-Aware BEV Representation), p. 7 (4.4. Design Analysis of GA-BEV) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose Geometry-Aware BEV (GA-BEV), a compact and 3D-grounded representation that combines explicit depth-based projected features with ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose the GeometryAware BEV (GA-BEV) - a compact and spatially grounded feature representation that integrates explicit and implicit geometric cues ...
- **p. 3 / 3. Methods - extractive body cue:** We propose the Geometry-Aware Vision-Language Navigation (GA-VLN) framework, which incorporates a Geometry-Aware BEV (GA-BEV) - a compact and 3Dgrounded spatial representation that transforms RGB-D observations ...
- **p. 4 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** To address this, we introduce the Grid-Based BEV Aggregation method for efficient aggregation and making the representation more suitable for the navigation task.
- **p. 4 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** To incorporate broader 3D geometric priors for better spatial reasoning, we introduce representation from a pretrained 3D foundation model (e.g., VGGT [27]) f3DFM(·), which encodes ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Navigation performance is measured using four standard metrics: Navigation Error (NE), Success Rate (SR), Oracle Success Rate (OSR), and Success weighted by Path Length (SPL).
- **p. 5 / 4.2. Comparison with State-of-the-Art Methods - extractive body cue:** Across most metrics on these benchmarks, our GA-VLN achieves the best overall performance, consistently surpassing previous Image-based MLLM frameworks [10, 39, 41, 42] and pipelines ...
- **p. 6 / 4.3. Ablation Study and Efficiency Analysis - extractive body cue:** Ultimately, GA-VLN outperforms the image-based baseline in both navigation performance and inference speed.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (4.1. Experimental Setup), p. 5 (4.2. Comparison with State-of-the-Art Methods) |
| Embodiment/environment | We evaluate our approach on standard continuous-environment VLN-CE [15] benchmarks: R2R-CE [3], RxR-CE [16], and NavRAG-CE [38] val unseen split in the Habitat simulator [25]. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Dataset/benchmark | Comparison with state-of-the-art VLN methods on R2R-CE, RxR-CE, and NavRAG-CE val unseen benchmarks. "System" groups methods into modular planners, 3D end-to-end agents, and Image-based MLLM agents, while "DAgger" indicates the use of ... | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 6 (4.3. Ablation Study and Efficiency Analysis) |
| Metric | Navigation performance is measured using four standard metrics: Navigation Error (NE), Success Rate (SR), Oracle Success Rate (OSR), and Success weighted by Path Length (SPL). | definition, denominator, direction and uncertainty | p. 5 (4.1. Experimental Setup), p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 7 (4.4. Design Analysis of GA-BEV) |
| Baseline/ablation | Ultimately, GA-VLN outperforms the image-based baseline in both navigation performance and inference speed. | fair input/data/compute/action matching | p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 5 (4.1. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive body cue:** An overly fine grid (row #4) fails to effectively compress redundant features, while an overly coarse grid (row #5) leads to the loss of important ...
- **p. 8 / 4.4. Design Analysis of GA-BEV - extractive body cue:** Robustness to Sensor Noise on R2R-CE val unseen.
- **p. 6 / 4.3. Ablation Study and Efficiency Analysis - extractive body cue:** Their combination strengthens spatial reasoning, enhances data efficiency, and yields a more robust navigation representation.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive body cue:** Crucially, these consistent relative improvements across different data scales confirm that GAVLN provides a robust spatial inductive bias independent of data volume.
- **p. 8 / 4.4. Design Analysis of GA-BEV - extractive body cue:** Noise N(0, σ2) NE↓ OSR↑ SR↑ SPL↑ w/o Noise - 4.80 67.59 60.96 55.19 Depth σ = 0.05m 4.82 65.63 59.11 54.25 Pose σ = ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Preliminary), p. 5 (3.3. Geometry-Aware VLN Framework)이다.
