# Method - VGMamba: Attribute-to-Location Clue Reasoning for Quantity-Agnostic 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_VGMamba_Attribute-to-Location_Clue_Reasoning_for_Quantity-Agnostic_3D_Visual_Grounding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_VGMamba_Attribute-to-Location_Clue_Reasoning_for_Quantity-Agnostic_3D_Visual_Grounding_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (3. Overview of State Space Models), p. 5 (4.4. Training Objectives), p. 2 (3. Overview of State Space Models), p. 3 (3. Overview of State Space Models), p. 3 (3. Overview of State Space Models)): Recently, state space models (SSMs) [9, 12, 30, 32] have attracted much attention for their ability to model continuous systems, constructing the foundation for the popular Mamba architecture [11].

## Method Body Digest

- **p. 2 / 3. Overview of State Space Models - extractive body cue:** Recently, state space models (SSMs) [9, 12, 30, 32] have attracted much attention for their ability to model continuous systems, constructing the foundation for the ...
- **p. 5 / 4.4. Training Objectives - extractive body cue:** Building on previous work [42], the loss of VGMamba consists of the 3D Visual Grounding loss Lref, text-object contrastive loss Lcon, and object detection loss ...
- **p. 2 / 3. Overview of State Space Models - extractive body cue:** Particularly, SSMs generally take an input sequence x(t) ∈RL as the input and output the corresponding sequence y(t) ∈RL through hidden states h(t) ∈RN, where ...
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** (2) The discretized state-space output can be represented as: hk = Ahk-1 + Bxk, yk = Chk.
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** Though Mamba-based networks have been verified to be effective in many tasks [19, 24], it is underexplored for 3D Visual Grounding.
- **p. 2 / 3. Overview of State Space Models - extractive body cue:** The system is governed by differential equations that describe how the hidden state evolves over time: h′(t) = Ah(t) + Bx(t), y(t) = Ch(t), (1) ...
- **p. 1 / 1. Introduction - extractive body cue:** This task has become a key challenge at the intersection of computer vision and natural language processing, with significant applications in areas such as human-robot ...
- **p. 1 / 1. Introduction - extractive body cue:** Experimental results on multiple datasets verify the effectiveness of this mechanism. of 3D environments, this task becomes even more complex due to the sparsity and ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our chief contributions are threefold: • We explore a novel mechanism, i.e., attribute-to-location clue reasoning, for performing 3D visual grounding. • We propose a novel ...
- **p. 2 / 1. Introduction - extractive body cue:** To be specific, we propose VGMamba, a novel architecture that systematically models attribute-to-location dependencies while efficiently capturing long-range interactions.
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** Finally, we present an Instructive Dual-Mamba block to localize the object that matches the given query. Δ to convert continuous parameters into discrete ones.

## Source Evidence Cues

- **p. 2 / 3. Overview of State Space Models - extractive body cue:** Recently, state space models (SSMs) [9, 12, 30, 32] have attracted much attention for their ability to model continuous systems, constructing the foundation for the ...
- **p. 5 / 4.4. Training Objectives - extractive body cue:** Building on previous work [42], the loss of VGMamba consists of the 3D Visual Grounding loss Lref, text-object contrastive loss Lcon, and object detection loss ...
- **p. 2 / 3. Overview of State Space Models - extractive body cue:** Particularly, SSMs generally take an input sequence x(t) ∈RL as the input and output the corresponding sequence y(t) ∈RL through hidden states h(t) ∈RN, where ...
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** (2) The discretized state-space output can be represented as: hk = Ahk-1 + Bxk, yk = Chk.
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** Though Mamba-based networks have been verified to be effective in many tasks [19, 24], it is underexplored for 3D Visual Grounding.
- **Detected method headings:** 3. Overview of State Space Models (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Recently, state space models (SSMs) [9, 12, 30, 32] have attracted much attention for their ability to model continuous systems, constructing the ... | p. 2 (3. Overview of State Space Models), p. 5 (4.4. Training Objectives) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Building on previous work [42], the loss of VGMamba consists of the 3D Visual Grounding loss Lref, text-object contrastive loss Lcon, and ... | p. 5 (4.4. Training Objectives), p. 2 (3. Overview of State Space Models) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Particularly, SSMs generally take an input sequence x(t) ∈RL as the input and output the corresponding sequence y(t) ∈RL through hidden states ... | p. 2 (3. Overview of State Space Models), p. 3 (3. Overview of State Space Models) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.4. Training Objectives - extractive body cue:** Building on previous work [42], the loss of VGMamba consists of the 3D Visual Grounding loss Lref, text-object contrastive loss Lcon, and object detection loss ...
- **p. 2 / 3. Overview of State Space Models - extractive body cue:** The system is governed by differential equations that describe how the hidden state evolves over time: h′(t) = Ah(t) + Bx(t), y(t) = Ch(t), (1) ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (3. Overview of State Space Models), p. 5 (4.4. Training Objectives).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Particularly, SSMs, generally, take, input, sequence, output, corresponding, through, hidden, states, where, number, system | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Particularly, SSMs, generally, take, input, sequence, output, corresponding, through, hidden | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | chief, contributions, threefold, explore, novel, mechanism, attribute-to-location, clue, reasoning, performing | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Building, previous, loss, VGMamba, consists, Visual, Grounding, Lref, text-object, contrastive | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3. Overview of State Space Models - extractive body cue:** Particularly, SSMs generally take an input sequence x(t) ∈RL as the input and output the corresponding sequence y(t) ∈RL through hidden states h(t) ∈RN, where ...
- **p. 2 / 3. Overview of State Space Models - extractive body cue:** The system is governed by differential equations that describe how the hidden state evolves over time: h′(t) = Ah(t) + Bx(t), y(t) = Ch(t), (1) ...
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** (2) The discretized state-space output can be represented as: hk = Ahk-1 + Bxk, yk = Chk.
- **p. 1 / 1. Introduction - extractive body cue:** This task has become a key challenge at the intersection of computer vision and natural language processing, with significant applications in areas such as human-robot ...
- **p. 1 / 1. Introduction - extractive body cue:** Experimental results on multiple datasets verify the effectiveness of this mechanism. of 3D environments, this task becomes even more complex due to the sparsity and ...
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** To this end, we study whether the Mamba could be used to capture the relation between objects and language descriptions.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Here, xt T/G represents the input at time step t. ←- AT and -→ AT are the state transition matrices used for ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To validate the effectiveness of each proposed module within our VGMamba framework, we conduct ablation studies on the Multi3DRefer dataset, as shown ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 5.1.2. Implementation Details - extractive body cue:** We implement the proposed VGMamba model using PyTorch and train it end-to-end on a single NVIDIA A6000 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Recently, state, space, models, SSMs, have, attracted, much, attention, ability, model, continuous, systems, constructing, foundation, popular, Mamba, architecture, Building, previous.
- **Relevant PDF headings:** 3. Overview of State Space Models (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The ScanRefer dataset comprises 51,583 natural language descriptions for 11,046 objects across 800 3D scenes from the ScanNet dataset [8]. | p. 5 (5.1.1. Datasets and Evaluation Metrics), p. 6 (5.1.1. Datasets and Evaluation Metrics) |
| Semantic / temporal fusion | 1, with the following key observations: (i) Our method achieves state-of-the-art performance with an overall accuracy of 60.0% at IoU 0.25 and ... | p. 6 (5.1.3. Baseline Comparison), p. 6 (Figure/Table caption) |
| Robot query / planning handoff | Table 4. Ablation study of proposed modules on Multi3DRefer. its intricate and free-form textual descriptions, which in- crease the difficulty of cross-modal ... | p. 7 (Figure/Table caption), p. 8 (5.3. Ablation Studies) |

## Failure and Ablation Link

- **p. 7 / 5.3. Ablation Studies - extractive body cue:** To validate the effectiveness of each proposed module within our VGMamba framework, we conduct ablation studies on the Multi3DRefer dataset, as shown in Tab.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** More ablation results are detailed in supplementary.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** A black chair without armrests, back to the window.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** A wooden chair without arms is tucked under the table.
- **p. 6 / 5.1.2. Implementation Details - extractive body cue:** Following prior work [42], we employ a pre-trained PointGroup [17] module as the detector, which is fine-tuned on the ScanNet dataset.
- **p. 6 / 5.1.3. Baseline Comparison - extractive body cue:** (iii) Unlike previous methods [13, 44] that show notable performance variations across settings, our VGMamba maintains consistently high accuracy, validating its robust generalization capability in ...
- **p. 7 / 5.2.3. Baseline Comparison - extractive body cue:** 46.7%, surpassing the second-best competitor by 3.1%, which highlights its robustness in managing complex scenes with multiple potential matches.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (3. Overview of State Space Models), p. 5 (4.4. Training Objectives), p. 2 (3. Overview of State Space Models), p. 3 (3. Overview of State Space Models), p. 3 (3. Overview of State Space Models), objective p. 5 (4.4. Training Objectives), p. 2 (3. Overview of State Space Models), temporal p. 5 (4.3. Multi-modal Mamba Fusion), p. 7 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies), p. 2 (2. Related Work), p. 2 (1. Introduction), p. 3 (3. Overview of State Space Models).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
