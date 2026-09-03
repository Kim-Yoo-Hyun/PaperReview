# Method - Mamba-3VL: Taming State Space Model for 3D Vision Language Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2.2. State Space Models and Visual Applications), p. 4 (3.2. Multi-Modal Mamba Mixer Block), p. 3 (3.1. Overall Framework), p. 4 (3.2. Multi-Modal Mamba Mixer Block), p. 5 (3.4. Output Heads and Losses), p. 5 (Method)): Vim [72] presents the first pure SSM-based model that efficiently compress the vision representation for intensive prediction tasks.

## Method Body Digest

- **p. 3 / 2.2. State Space Models and Visual Applications - extractive body cue:** Vim [72] presents the first pure SSM-based model that efficiently compress the vision representation for intensive prediction tasks.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** To establish the correspondence between 3D vision and task prompts, we first construct a hybrid feature chain by channel-wisely concatenating 3D instance queries and prompt ...
- **p. 3 / 3.1. Overall Framework - extractive body cue:** For the point cloud, we use the pre-trained PointNet++ [47] to obtain point features P={p0, p1, ..., pS} of the segments.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** To better adapt mamba to 3D-VL tasks, we introduce Mamba Mixer, which interprets spatial relationships of 3D objects and achieves holistic inter-modality and intra-modality interactions.
- **p. 5 / 3.4. Output Heads and Losses - extractive body cue:** The model is optimized through multi-task learning with combined losses.
- **p. 5 / Method - extractive body cue:** The output ¯xi of IDPA is incorporated into the mamba-based query decoder branch via a residual connection.
- **p. 5 / 3.4. Output Heads and Losses - extractive body cue:** We compute the cross entropy loss Lgrd and Lgen for both grounding and generation heads, while the dice loss Lmask is applied to the mask ...
- **p. 3 / 2.2. State Space Models and Visual Applications - extractive body cue:** Recent studies [32, 36, 65, 66] investigate the applicability of mamba on 3D tasks by employing distinct point cloud ordering policy.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To capture spatial relationships of 3D object sequences while enhancing fine-grained interactions of 3D-VL interaction, we develop a Mamba Mixer module, which consists of a ...
- **p. 2 / 1. Introduction - extractive body cue:** Motivated by this, we propose an Instance-aware Dynamic Position Adapter (IDPA) with intercalated EdgeConv [56-58] and Language-modulated InStance Adapter (LISA) layers.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** To better adapt mamba to 3D-VL tasks, we introduce Mamba Mixer, which interprets spatial relationships of 3D objects and achieves holistic inter-modality and intra-modality interactions.

## Source Evidence Cues

- **p. 3 / 2.2. State Space Models and Visual Applications - extractive body cue:** Vim [72] presents the first pure SSM-based model that efficiently compress the vision representation for intensive prediction tasks.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** To establish the correspondence between 3D vision and task prompts, we first construct a hybrid feature chain by channel-wisely concatenating 3D instance queries and prompt ...
- **p. 3 / 3.1. Overall Framework - extractive body cue:** For the point cloud, we use the pre-trained PointNet++ [47] to obtain point features P={p0, p1, ..., pS} of the segments.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** To better adapt mamba to 3D-VL tasks, we introduce Mamba Mixer, which interprets spatial relationships of 3D objects and achieves holistic inter-modality and intra-modality interactions.
- **p. 5 / 3.4. Output Heads and Losses - extractive body cue:** The model is optimized through multi-task learning with combined losses.
- **p. 5 / Method - extractive body cue:** The output ¯xi of IDPA is incorporated into the mamba-based query decoder branch via a residual connection.
- **Detected method headings:** 2.2. State Space Models and Visual Applications (p. 3); 3. Methods (p. 3); Method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Vim [72] presents the first pure SSM-based model that efficiently compress the vision representation for intensive prediction tasks. | p. 3 (2.2. State Space Models and Visual Applications), p. 4 (3.2. Multi-Modal Mamba Mixer Block) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To establish the correspondence between 3D vision and task prompts, we first construct a hybrid feature chain by channel-wisely concatenating 3D instance ... | p. 4 (3.2. Multi-Modal Mamba Mixer Block), p. 3 (3.1. Overall Framework) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | For the point cloud, we use the pre-trained PointNet++ [47] to obtain point features P={p0, p1, ..., pS} of the segments. | p. 3 (3.1. Overall Framework), p. 4 (3.2. Multi-Modal Mamba Mixer Block) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Output Heads and Losses - extractive body cue:** We compute the cross entropy loss Lgrd and Lgen for both grounding and generation heads, while the dice loss Lmask is applied to the mask ...
- **p. 5 / 3.4. Output Heads and Losses - extractive body cue:** The model is optimized through multi-task learning with combined losses.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.4. Output Heads and Losses), p. 5 (3.4. Output Heads and Losses).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Recent, studies, investigate, applicability, mamba, tasks, employing, distinct, point, cloud, ordering, policy, Leveraging, State | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Recent, studies, investigate, applicability, mamba, tasks, employing, distinct, point, cloud | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | capture, spatial, relationships, object, sequences, while, enhancing, fine-grained, interactions, D-VL | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | compute, cross, entropy, loss, Lgrd, Lgen, grounding, generation, heads, while | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2.2. State Space Models and Visual Applications - extractive body cue:** Recent studies [32, 36, 65, 66] investigate the applicability of mamba on 3D tasks by employing distinct point cloud ordering policy.
- **p. 2 / 1. Introduction - extractive body cue:** Leveraging State Space Models (SSMs) as its core, a flux of mamba proposes a selection scanning mechanism, enabling it to handle long-range sequences and spatial ...
- **p. 2 / 1. Introduction - extractive body cue:** Drawing inspiration from 2D vision-language (2D-VL) models [10, 14, 28, 33, 34], contemporary 3D-VL models rely heavily on transformer-based cross-modality interaction to fuse 3D scene ...
- **p. 3 / 3.1. Overall Framework - extractive body cue:** Each query is ultimately routed through three universal output heads to predict the instance mask, task-related score, and scene-grounded texts.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** Consider the prompt-based Mamba Mixer as an exemplar: (1) Intra-modality interactions.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** The spatial scanning exhibits channel independence, failing to capture multi-modal interactions.
- **p. 5 / 3.4. Output Heads and Losses - extractive body cue:** 3, our Mamba-3VL utilizes three output heads to support 3D-VL tasks.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Before feeding instance queries Ql ∈RN×d into the mamba block, a critical step involves reordering them into 1D sequences. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In detail, we sort Ql based on spatial proximity into two sequence: farthest and nearest neighbor orders. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Overall Framework - extractive body cue:** For the point cloud, we use the pre-trained PointNet++ [47] to obtain point features P={p0, p1, ..., pS} of the segments.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Vim, presents, first, pure, SSM-based, model, efficiently, compress, vision, representation, intensive, prediction, tasks, establish, correspondence, between, task, prompts, construct, hybrid.
- **Relevant PDF headings:** 2.2. State Space Models and Visual Applications (p. 3); 3. Methods (p. 3); Method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | (2) 80-epoch full-task training on all benchmark datasets with promptable queries. | p. 5 (4.1. Implementation Details), p. 6 (4.1. Implementation Details) |
| Semantic / temporal fusion | For the SQA3D [42], Mamba3VL outperforms all existing state-of-the-arts across different challenging question types as illustrated in Tab. | p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 8 (Figure/Table caption) |
| Robot query / planning handoff | The model achieves landmark accuracies of 79.9% (Unique) and 48.9% (Multiple) on the ScanRefer [6], outperforming PQ3D [74] by 1.7% and 2.7%, ... | p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Table 9. Ablation study of proposed modules' effectiveness, with average performance evaluated under IoU@0.5. in Tab. 2, Mamba-3VL establishes new competitive bench- marks for 3D ...
- **p. 6 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** Our method exhibits view-invariant robustness with 3.9% and 6.2% improvements over PQ3D on VD subsets of Nr3D/Sr3D benchmarks.
- **p. 7 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** Ablations of the selection of scanning mechanism.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** A), more framework ablations of Mamba-3VL (Tab.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** Removing either component (i.e., w/o.
- **p. 6 / 4.1. Implementation Details - extractive body cue:** For embodied AI tasks, we replace the T5-small [49] model of generation head with Vicuna-7B [13] using the instructionfollowing dataset [21].
- **p. 6 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** Our method exhibits view-invariant robustness with 3.9% and 6.2% improvements over PQ3D on VD subsets of Nr3D/Sr3D benchmarks.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2.2. State Space Models and Visual Applications), p. 4 (3.2. Multi-Modal Mamba Mixer Block), p. 3 (3.1. Overall Framework), p. 4 (3.2. Multi-Modal Mamba Mixer Block), p. 5 (3.4. Output Heads and Losses), p. 5 (Method), objective p. 5 (3.4. Output Heads and Losses), p. 5 (3.4. Output Heads and Losses), temporal p. 4 (3.2. Multi-Modal Mamba Mixer Block), p. 4 (3.2. Multi-Modal Mamba Mixer Block), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
