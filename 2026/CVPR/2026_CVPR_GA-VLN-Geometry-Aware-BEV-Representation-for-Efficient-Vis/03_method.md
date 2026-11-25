# Method - GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Geometry-Aware VLN Framework), p. 3 (3. Methods), p. 4 (3.2. Geometry-Aware BEV Representation), p. 5 (3.2. Geometry-Aware BEV Representation), p. 4 (3.2. Geometry-Aware BEV Representation), p. 3 (3. Methods)): In the first round, the model is conditioned on the language instruction, the current front-view image, and a unified BEV feature aggregated from up to eight historical observations.

## Method Body Digest

- **p. 5 / 3.3. Geometry-Aware VLN Framework - extractive body cue:** In the first round, the model is conditioned on the language instruction, the current front-view image, and a unified BEV feature aggregated from up to ...
- **p. 3 / 3. Methods - extractive body cue:** We propose the Geometry-Aware Vision-Language Navigation (GA-VLN) framework, which incorporates a Geometry-Aware BEV (GA-BEV) - a compact and 3Dgrounded spatial representation that transforms RGB-D observations ...
- **p. 4 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** To incorporate broader 3D geometric priors for better spatial reasoning, we introduce representation from a pretrained 3D foundation model (e.g., VGGT [27]) f3DFM(·), which encodes ...
- **p. 5 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** It is also worth noting that although we introduce the additional t × Hg × Wg geometry tokens from 3D foundation models, the grid-based aggregation ...
- **원문 대조:** 과거 image sequence를 pretrained 3D foundation model에 넣어 implicit multi-view geometry를 포함한 patch feature를 얻는다. 이후 projection layer로 visual feature 차원을 맞추고 depth-guided projection과 BEV aggregation에 사용한다. ([PDF p. 4](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.pdf#page=4), §3.2 Implicit 3D Geometry Priors, Eq. (2)).
- **p. 3 / 3. Methods - extractive body cue:** We then introduce the design details of the proposed GA-BEV representation.
- **p. 8 / 4.4. Design Analysis of GA-BEV - extractive body cue:** ThirdPerson View FirstPerson View Action=[→, →, →, →] T=2 T=4 T=6 T=8 T=10 T=12 T=14 T=16 T=18 T=0 Action=[→, →, →, ↑] Action=[↑, ←, ←, ...
- **p. 5 / 3.3. Geometry-Aware VLN Framework - extractive body cue:** To minimize computational overhead, the second round queries the model using only the newly updated front-view image while reusing the BEV feature from the first ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose Geometry-Aware BEV (GA-BEV), a compact and 3D-grounded representation that combines explicit depth-based projected features with ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose the GeometryAware BEV (GA-BEV) - a compact and spatially grounded feature representation that integrates explicit and implicit geometric cues ...
- **p. 3 / 3. Methods - extractive body cue:** We propose the Geometry-Aware Vision-Language Navigation (GA-VLN) framework, which incorporates a Geometry-Aware BEV (GA-BEV) - a compact and 3Dgrounded spatial representation that transforms RGB-D observations ...

## Source Evidence Cues

- **p. 5 / 3.3. Geometry-Aware VLN Framework - extractive body cue:** In the first round, the model is conditioned on the language instruction, the current front-view image, and a unified BEV feature aggregated from up to ...
- **p. 3 / 3. Methods - extractive body cue:** We propose the Geometry-Aware Vision-Language Navigation (GA-VLN) framework, which incorporates a Geometry-Aware BEV (GA-BEV) - a compact and 3Dgrounded spatial representation that transforms RGB-D observations ...
- **p. 4 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** To incorporate broader 3D geometric priors for better spatial reasoning, we introduce representation from a pretrained 3D foundation model (e.g., VGGT [27]) f3DFM(·), which encodes ...
- **p. 5 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** It is also worth noting that although we introduce the additional t × Hg × Wg geometry tokens from 3D foundation models, the grid-based aggregation ...
- **원문 대조:** 과거 image sequence를 pretrained 3D foundation model에 넣어 implicit multi-view geometry를 포함한 patch feature를 얻는다. 이후 projection layer로 visual feature 차원을 맞추고 depth-guided projection과 BEV aggregation에 사용한다. ([PDF p. 4](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.pdf#page=4), §3.2 Implicit 3D Geometry Priors, Eq. (2)).
- **p. 3 / 3. Methods - extractive body cue:** We then introduce the design details of the proposed GA-BEV representation.
- **p. 8 / 4.4. Design Analysis of GA-BEV - extractive body cue:** ThirdPerson View FirstPerson View Action=[→, →, →, →] T=2 T=4 T=6 T=8 T=10 T=12 T=14 T=16 T=18 T=0 Action=[→, →, →, ↑] Action=[↑, ←, ←, ...
- **Detected method headings:** 3. Methods (p. 3); 4.2. Comparison with State-of-the-Art Methods (p. 5); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | In the first round, the model is conditioned on the language instruction, the current front-view image, and a unified BEV feature aggregated ... | p. 5 (3.3. Geometry-Aware VLN Framework), p. 3 (3. Methods) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We propose the Geometry-Aware Vision-Language Navigation (GA-VLN) framework, which incorporates a Geometry-Aware BEV (GA-BEV) - a compact and 3Dgrounded spatial representation that ... | p. 3 (3. Methods), p. 4 (3.2. Geometry-Aware BEV Representation) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | To incorporate broader 3D geometric priors for better spatial reasoning, we introduce representation from a pretrained 3D foundation model (e.g., VGGT [27]) ... | p. 4 (3.2. Geometry-Aware BEV Representation), p. 5 (3.2. Geometry-Aware BEV Representation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Geometry-Aware VLN Framework - extractive body cue:** To minimize computational overhead, the second round queries the model using only the newly updated front-view image while reusing the BEV feature from the first ...
- **p. 4 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** To better align with this motion constraint, we further project all 3D features onto an agent-centric BEV plane.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive body cue:** An overly fine grid (row #4) fails to effectively compress redundant features, while an overly coarse grid (row #5) leads to the loss of important ...
- **p. 7 / Method - extractive body cue:** Unlike Table 2, all models in this table are trained without incorporating the SRDF dataset to reduce computational overhead. of our BEV-based representation, which accommodates ...
- **p. 5 / 3.3. Geometry-Aware VLN Framework - extractive body cue:** Consequently, the BEV representation is efficiently updated only once every eight actions (i.e., upon the completion of a two-round dialogue), and the agent terminates navigation ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3.2. Geometry-Aware BEV Representation), p. 7 (4.4. Design Analysis of GA-BEV), p. 5 (3.3. Geometry-Aware VLN Framework), p. 5 (3.3. Geometry-Aware VLN Framework).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | first, round, model, conditioned, language, instruction, current, front-view, image, unified, BEV, feature, aggregated, eight | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | first, round, model, conditioned, language, instruction, current, front-view, image, unified | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, Geometry-Aware, BEV, GA-BEV, compact, D-grounded, representation | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | minimize, computational, overhead, second, round, queries, model, only, newly, updated | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.3. Geometry-Aware VLN Framework - extractive body cue:** In the first round, the model is conditioned on the language instruction, the current front-view image, and a unified BEV feature aggregated from up to ...
- **p. 1 / 1. Introduction - extractive body cue:** Recent advances in multimodal large language models (MLLMs) [17, 48] have greatly enhanced agents' abilities to comprehend instructions, ground them in visual contexts, and predict ...
- **p. 4 / 3.1. Preliminary - extractive body cue:** At each time step t, the agent receives a language instruction L, the current visual observation It, and all previous observations {I1, . . . ...
- **원문 대조:** 기본 VLN formulation은 instruction L과 현재까지의 visual token sequence를 MLLM에 입력해 다음 action a_t를 예측한다. 이 일반 formulation과 §3.2의 GA-BEV 압축 representation을 구분한다. ([PDF p. 4](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.pdf#page=4), §3.1 Preliminary).
- **p. 2 / 1. Introduction - extractive body cue:** These compact BEV features - together with the visual tokens from the current front-view frame and the language instruction - are then fed into the ...
- **p. 8 / 4.4. Design Analysis of GA-BEV - extractive body cue:** ThirdPerson View FirstPerson View Action=[→, →, →, →] T=2 T=4 T=6 T=8 T=10 T=12 T=14 T=16 T=18 T=0 Action=[→, →, →, ↑] Action=[↑, ←, ←, ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose Geometry-Aware BEV (GA-BEV), a compact and 3D-grounded representation that combines explicit depth-based projected features with ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At each time step t, the agent receives a language instruction L, the current visual observation It, and all previous observations {I1, ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | All historical 3D points P are transformed into the current agent-centric coordinate frame at each navigation step, ensuring that past observations remain ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | This paradigm shift demands significantly stronger abilities in online environment representation, obstacle avoidance, and spatial memory construction, enabling the agent to understand ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Geometry-Aware BEV Representation - extractive body cue:** To incorporate broader 3D geometric priors for better spatial reasoning, we introduce representation from a pretrained 3D foundation model (e.g., VGGT [27]) f3DFM(·), which encodes ...
- **p. 6 / 4.3. Ablation Study and Efficiency Analysis - extractive body cue:** Furthermore, Table 2 reports the per-inference theoretical TFLOPs and model latency evaluated on identical samples and hardware to demonstrate the computational efficiency of our method.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive body cue:** The token numbers represent the average number of visual tokens required per navigation step, computed over 121 sampled navigation trajectories across 61 training scenes.

## Method-Specific Formal Details

- **Body-defined terms:** first, round, model, conditioned, language, instruction, current, front-view, image, unified, BEV, feature, aggregated, eight, historical, observations, Geometry-Aware, Vision-Language, Navigation, GA-VLN.
- **Relevant PDF headings:** 3. Methods (p. 3); 4.2. Comparison with State-of-the-Art Methods (p. 5); Method (p. 7).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We evaluate our approach on standard continuous-environment VLN-CE [15] benchmarks: R2R-CE [3], RxR-CE [16], and NavRAG-CE [38] val unseen split in the ... | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Global / local decision | Ultimately, GA-VLN outperforms the image-based baseline in both navigation performance and inference speed. | p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 6 (4.2. Comparison with State-of-the-Art Methods) |
| Motion execution / recovery | Navigation performance is measured using four standard metrics: Navigation Error (NE), Success Rate (SR), Oracle Success Rate (OSR), and Success weighted by ... | p. 5 (4.1. Experimental Setup), p. 5 (4.2. Comparison with State-of-the-Art Methods) |

## Failure and Ablation Link

- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive body cue:** To rigorously demonstrate that the performance gains of our model are driven by fundamental architectural innovations rather than solely by data scaling, Rows #1-3 in ...
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive body cue:** Effect of the Number of Historical Frames.
- **p. 6 / 4.3. Ablation Study and Efficiency Analysis - extractive body cue:** All the ablation and analysis experiments in this section and the following sections are conducted on the R2R-CE val unseen split.
- **p. 6 / 4.2. Comparison with State-of-the-Art Methods - extractive body cue:** Notably, unlike most recent methods that rely on DAgger augmentation, our framework achieves competitive performance using only high-quality curated data, without any DAgger-enhanced trajectories or ...
- **p. 8 / 4.5. Real-World Robot Experiments - extractive body cue:** 3, despite operating without any auxiliary obstacle avoidance or mapping modules, the agent successfully executes complex natural-language instructions and constructs meaningful geometric surrounding BEV representations.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** All reported results are obtained using models pretrained for 2 epochs.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The parameters of f3DFM are kept frozen during training, while all other modules are fine-tuned.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Geometry-Aware VLN Framework), p. 3 (3. Methods), p. 4 (3.2. Geometry-Aware BEV Representation), p. 5 (3.2. Geometry-Aware BEV Representation), p. 4 (3.2. Geometry-Aware BEV Representation), p. 3 (3. Methods), objective p. 5 (3.3. Geometry-Aware VLN Framework), p. 4 (3.2. Geometry-Aware BEV Representation), p. 7 (4.4. Design Analysis of GA-BEV), p. 7 (Method), p. 5 (3.3. Geometry-Aware VLN Framework), temporal p. 4 (3.1. Preliminary), p. 4 (3.2. Geometry-Aware BEV Representation), p. 7 (4.4. Design Analysis of GA-BEV), p. 8 (4.4. Design Analysis of GA-BEV), p. 1 (1. Introduction), p. 2 (2. Related Work).
