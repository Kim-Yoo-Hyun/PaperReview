# Method - ReferSplat: Referring Segmentation in 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=reuShgiHdg; PDF retrieval source: https://openreview.net/pdf/646ff3c7806367b3d28461db1cfc8b52b4856ec6.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 4 (3.2. Problem Statement and Method Overview), p. 3 (3.2. Problem Statement and Method Overview), p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 4 (3.3. 3D Gaussian Referring Fields), p. 6 (3.5. Gaussian-Text Contrastive Learning)): To address these issues, we propose a Position-aware CrossModal Interaction module that injects position information into the cross-modal attention mechanism to facilitate interactions between textual entities and 3D Gaussians beyond ...

## Method Body Digest

- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive PDF cue:** To address these issues, we propose a Position-aware CrossModal Interaction module that injects position information into the cross-modal attention mechanism to facilitate interactions between textual ...
- **p. 4 / 3.2. Problem Statement and Method Overview - extractive PDF cue:** Firstly, to infuse language-awareness into the 3D Gaussians, we introduce a new property called referring features, constructing 3D Gaussian Referring Fields.
- **p. 3 / 3.2. Problem Statement and Method Overview - extractive PDF cue:** To enhance the interaction between referring features and word features fw, we introduce a Position-aware Cross-Modal Interaction in Sec.
- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive PDF cue:** To integrate position information, we first extract position features from 3D Gaussian representations.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive PDF cue:** Inspired by methods that incorporate semantic feature vectors to construct semantic-aware fields (Qin et al., 2024; Zhou et al., 2024b; Qu et al., 2024), we ...
- **p. 6 / 3.5. Gaussian-Text Contrastive Learning - extractive PDF cue:** To address this issue, we introduce Gaussian-Text Contrastive Learning in the Gaussian feature space.
- **p. 6 / 3.5. Gaussian-Text Contrastive Learning - extractive PDF cue:** The total training objective is: Lloss = Lbce + λLcon, (10) where λ is used for balancing the contrastive loss Lcon.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive PDF cue:** (3) Finally, we employ a binary cross-entropy (BCE) loss to supervise the output mask, enforcing consistency with the pseudo ground truth mask, which we introduce ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), aims at segmenting objects in a 3D Gaussian scene based ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To enhance spatial reasoning, we introduce a Position-aware Cross-Modal Interaction module that extracts position features for both Gaussians and language descriptions.
- **p. 2 / 1. Introduction - extractive PDF cue:** In this work, we propose ReferSplat, an end-to-end framework that models 3D Gaussian points with natural language expressions in a spatially aware paradigm for Referring ...

## Source Evidence Cues

- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive PDF cue:** To address these issues, we propose a Position-aware CrossModal Interaction module that injects position information into the cross-modal attention mechanism to facilitate interactions between textual ...
- **p. 4 / 3.2. Problem Statement and Method Overview - extractive PDF cue:** Firstly, to infuse language-awareness into the 3D Gaussians, we introduce a new property called referring features, constructing 3D Gaussian Referring Fields.
- **p. 3 / 3.2. Problem Statement and Method Overview - extractive PDF cue:** To enhance the interaction between referring features and word features fw, we introduce a Position-aware Cross-Modal Interaction in Sec.
- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive PDF cue:** To integrate position information, we first extract position features from 3D Gaussian representations.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive PDF cue:** Inspired by methods that incorporate semantic feature vectors to construct semantic-aware fields (Qin et al., 2024; Zhou et al., 2024b; Qu et al., 2024), we ...
- **p. 6 / 3.5. Gaussian-Text Contrastive Learning - extractive PDF cue:** To address this issue, we introduce Gaussian-Text Contrastive Learning in the Gaussian feature space.
- **p. 6 / 3.5. Gaussian-Text Contrastive Learning - extractive PDF cue:** The total training objective is: Lloss = Lbce + λLcon, (10) where λ is used for balancing the contrastive loss Lcon.
- **Detected method headings:** 3. Method (p. 3); 3.2. Problem Statement and Method Overview (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To address these issues, we propose a Position-aware CrossModal Interaction module that injects position information into the cross-modal attention mechanism to facilitate ... | p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 4 (3.2. Problem Statement and Method Overview) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Firstly, to infuse language-awareness into the 3D Gaussians, we introduce a new property called referring features, constructing 3D Gaussian Referring Fields. | p. 4 (3.2. Problem Statement and Method Overview), p. 3 (3.2. Problem Statement and Method Overview) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To enhance the interaction between referring features and word features fw, we introduce a Position-aware Cross-Modal Interaction in Sec. | p. 3 (3.2. Problem Statement and Method Overview), p. 5 (3.4. Position-aware Cross-Modal Interaction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.5. Gaussian-Text Contrastive Learning - extractive PDF cue:** The total training objective is: Lloss = Lbce + λLcon, (10) where λ is used for balancing the contrastive loss Lcon.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive PDF cue:** (3) Finally, we employ a binary cross-entropy (BCE) loss to supervise the output mask, enforcing consistency with the pseudo ground truth mask, which we introduce ...
- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive PDF cue:** We integrate structural geometry constraints to guide attention computation: f ′ r,i = fr,i + softmax (fr,i + fp,i)(fw + fp,w,i)T √ D  fw.
- **p. 6 / 3.5. Gaussian-Text Contrastive Learning - extractive PDF cue:** This formulation encourages the model to maximize similarity between Gaussians and their corresponding textual descriptions while ensuring sufficient separation from unrelated textual descriptions, ultimately enhancing ...
- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive PDF cue:** (7) This formulation ensures that the updated referring feature f ′ r,i is enriched with both position and semantic cues, improving its ability to localize ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3.5. Gaussian-Text Contrastive Learning), p. 4 (3.3. 3D Gaussian Referring Fields), p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 5 (3.4. Position-aware Cross-Modal Interaction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | While, Position-aware, Cross-Modal, Interaction, module, effectively, captures, relationship, between, Gaussian, representations, text, descriptions, distinguishing | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | While, Position-aware, Cross-Modal, Interaction, module, effectively, captures, relationship, between, Gaussian | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | bridge, introduce, task, Referring, Gaussian, Splatting, Segmentation, R3DGS, aims, segmenting | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | total, training, objective, Lloss, Lbce, Lcon, where, balancing, contrastive, loss | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.5. Gaussian-Text Contrastive Learning - extractive PDF cue:** While the proposed Position-aware Cross-Modal Interaction module effectively captures the relationship between Gaussian representations and text descriptions, distinguishing between languages with similar meanings but referring ...
- **p. 2 / 1. Introduction - extractive PDF cue:** During inference, output masks are obtained by matching the input open-vocabulary class names with the rendered feature, as shown in Fig.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive PDF cue:** To generate high-quality 2D pseudo masks, we input the image and referring expression into Grounded SAM (Ren et al., 2024).
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive PDF cue:** Unlike traditional 3DGS, which primarily renders color values or predefined semantic features, our approach directly renders Gaussian-language similarity responses, enabling explicit interaction between textual descriptions ...
- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive PDF cue:** The proposed Position-aware Cross-Modal Interaction module establishes a stronger relationship between Gaussian referring features and text descriptions by explicitly integrating position information.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, despite these advancements, free-form natural language interactions with 3D scenes remain underexplored.
- **p. 1 / 1. Introduction - extractive PDF cue:** Training Testing "The one standing on the table has a long nose" "green object placed between pumpkin and red chair" "A small cube object with ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 2, our method surpasses existing approaches, establishing a superior referring segmentation framework in 3D Gaussian scenes. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In our framework, the referring feature encodes semantic and referring information, allowing us to compute the text response for each Gaussian by ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3.5. Gaussian-Text Contrastive Learning - extractive PDF cue:** The total training objective is: Lloss = Lbce + λLcon, (10) where λ is used for balancing the contrastive loss Lcon.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** We optimize the Gaussian referring features for 45,000 iterations, using a learning rate of 0.0025, while other parameters, such as the MLP, are trained with ...
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** ReferSplat also has the shortest training time, thanks to a lightweight preprocessing pipeline that avoids costly operations like language feature compression (LangSplat) or mask association ...
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** Training is conducted on an NVIDIA RTX A6000 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, issues, Position-aware, CrossModal, Interaction, module, injects, position, information, cross-modal, attention, mechanism, facilitate, interactions, between, textual, entities, Gaussians, beyond, mere.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. Problem Statement and Method Overview (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The LERF dataset (Kerr et al., 2023) is collected using the Polycam iPhone app and consists of four diverse, complex, real-world scenes. | p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 7 (4.3. Ablation Study) |
| Semantic / temporal fusion | 1, incorporating PCMI (index 1) improves mIoU by 5.1% and 4.3%, respectively compared to the baseline, which is our constructed Referring Feature ... | p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study) |
| Robot query / planning handoff | Results show that ReferSplat achieves significantly lower computational complexity and faster inference speed than LangSplat (Qin et al., 2024). | p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study) |

## Failure and Ablation Link

- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We conduct ablation experiments to evaluate the effectiveness of different components.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** 4, removing components fp,i and fp,w,i from Eq.7 results in performance dropping below the baseline, indicating that vanilla cross-attention alone is ineffective for our task.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** We study the effect of the referring feature dimension dr in Tab.
- **p. 8 / 4.4. Results on the Ref-LERF Dataset - extractive PDF cue:** Ablation study on number of feature dims.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 2021; Kirillov et al., 2023) as ground ...
- **p. 9 / 6. Limitation and Future Work - extractive PDF cue:** 1) Our current method does not account for dynamic factors, which are crucial for real-world applications.
- **p. 9 / 6. Limitation and Future Work - extractive PDF cue:** 2) While we focus on 3D referring segmentation in Gaussian Splatting, our method does not incorporate 3D visual grounding.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 4 (3.2. Problem Statement and Method Overview), p. 3 (3.2. Problem Statement and Method Overview), p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 4 (3.3. 3D Gaussian Referring Fields), p. 6 (3.5. Gaussian-Text Contrastive Learning), objective p. 6 (3.5. Gaussian-Text Contrastive Learning), p. 4 (3.3. 3D Gaussian Referring Fields), p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 6 (3.5. Gaussian-Text Contrastive Learning), p. 5 (3.4. Position-aware Cross-Modal Interaction), temporal p. 4 (3.3. 3D Gaussian Referring Fields), p. 4 (3.3. 3D Gaussian Referring Fields), p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
