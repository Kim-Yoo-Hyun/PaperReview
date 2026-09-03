# Method - ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. QT-Former), p. 4 (3.3. Generative Planner), p. 4 (3.1. QT-Former), p. 5 (3.3. Generative Planner), p. 5 (3.3. Generative Planner), p. 3 (3. Method)): To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a querybased temporal module, as shown in Fig.

## Method Body Digest

- **p. 3 / 3.1. QT-Former - extractive body cue:** To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a querybased temporal module, ...
- **p. 4 / 3.3. Generative Planner - extractive body cue:** As there are essential differences in the distribution between the reasoning space of VLM and the action space of trajectory, we use the VAE [29] ...
- **p. 4 / 3.1. QT-Former - extractive body cue:** Then they interact with image features Fm with 3D positional encoding [38] Pm in the cross-attention (CA) module.
- **p. 5 / 3.3. Generative Planner - extractive body cue:** (5) We then use the GRU decoder in GenAD [72] to decode the trajectory from the latent space z.
- **p. 5 / 3.3. Generative Planner - extractive body cue:** We then use Kullback-Leibler divergence loss to enforce distribution matching, represented as: Lvae = DKL(p(z/s), p(z/t)).
- **p. 3 / 3. Method - extractive body cue:** 2, ORION first encodes the image tokens with a vision encoder.
- **p. 5 / 3.4. Training Objectives - extractive body cue:** The total loss of QTFormer is: Lqt = Ldet + Ltra + Lm.
- **p. 5 / 3.4. Training Objectives - extractive body cue:** (8) The loss weight follows [26, 60, 72] without special design.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION.
- **p. 2 / 1. Introduction - extractive body cue:** Instead, motivated by OmniDrive [61], which extracts features through Q-Former-styled architecture, we introduce QT-Former, a query-based temporal module.
- **p. 3 / 3.1. QT-Former - extractive body cue:** To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a querybased temporal module, ...

## Source Evidence Cues

- **p. 3 / 3.1. QT-Former - extractive body cue:** To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a querybased temporal module, ...
- **p. 4 / 3.3. Generative Planner - extractive body cue:** As there are essential differences in the distribution between the reasoning space of VLM and the action space of trajectory, we use the VAE [29] ...
- **p. 4 / 3.1. QT-Former - extractive body cue:** Then they interact with image features Fm with 3D positional encoding [38] Pm in the cross-attention (CA) module.
- **p. 5 / 3.3. Generative Planner - extractive body cue:** (5) We then use the GRU decoder in GenAD [72] to decode the trajectory from the latent space z.
- **p. 5 / 3.3. Generative Planner - extractive body cue:** We then use Kullback-Leibler divergence loss to enforce distribution matching, represented as: Lvae = DKL(p(z/s), p(z/t)).
- **p. 3 / 3. Method - extractive body cue:** 2, ORION first encodes the image tokens with a vision encoder.
- **Detected method headings:** 2.2. Vision-Language Models (VLMs) (p. 2); 3. Method (p. 3); 3.2. Large Language Model (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a ... | p. 3 (3.1. QT-Former), p. 4 (3.3. Generative Planner) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | As there are essential differences in the distribution between the reasoning space of VLM and the action space of trajectory, we use ... | p. 4 (3.3. Generative Planner), p. 4 (3.1. QT-Former) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Then they interact with image features Fm with 3D positional encoding [38] Pm in the cross-attention (CA) module. | p. 4 (3.1. QT-Former), p. 5 (3.3. Generative Planner) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Training Objectives - extractive body cue:** The total loss of QTFormer is: Lqt = Ldet + Ltra + Lm.
- **p. 5 / 3.4. Training Objectives - extractive body cue:** (8) The loss weight follows [26, 60, 72] without special design.
- **p. 4 / 3.3. Generative Planner - extractive body cue:** Specifically, we formulate the current trajectory a in action space as a conditional probability distribution p(a / s), where s is the planning token.
- **p. 4 / 3.1. QT-Former - extractive body cue:** Finally, we leverage two-layer MLP to convert the updated history queries ˆQh and current scene features Qs to corresponding history tokens xh and scene tokens ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.4. Training Objectives), p. 5 (3.4. Training Objectives), p. 4 (3.1. QT-Former), p. 4 (3.1. QT-Former).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | user, instruction, including, scene, description, history, information, review, analysis, action, reasoning, first, encoded, language | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | user, instruction, including, scene, description, history, information, review, analysis, action | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | tackle, problem, hOlistic, E2E, autonomous, dRiving, framework, vIsion-language, instructed, actiON | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | total, loss, QTFormer, Lqt, Ldet, Ltra, weight, follows, without, special | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Large Language Model - extractive body cue:** 2, the user instruction Xq, including scene description, history information review, scene analysis, and action reasoning, is first encoded into language tokens xq ∈RL×C by ...
- **p. 5 / 3.3. Generative Planner - extractive body cue:** The former only uses a single token encoded in the reasoning space from the perspective of the ego vehicle as input, aiming to bridge the ...
- **p. 2 / 1. Introduction - extractive body cue:** Other methods endeavor to bridge the gap via utilizing VLM output meta-action (e.g., turn left) to assist classic E2E methods [27, 41], as shown in ...
- **p. 2 / 1. Introduction - extractive body cue:** To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION.
- **p. 4 / 3.1. QT-Former - extractive body cue:** After that, the perception queries are fed into the multiple auxiliary heads for object detection(e.g., objects and map), traffic state (e.g. traffic signs, traffic lights, ...
- **p. 5 / 3.3. Generative Planner - extractive body cue:** Benefiting from the proposed method that bridges the gap between the reasoning and action space through distribution learning in latent space, our framework still demonstrates ...
- **p. 3 / 3. Method - extractive body cue:** 3.2) subsequently combines the vision features with user instructions to generate a planning token.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Although some methods [52, 60] also leverage the memory bank to store preceding information, they typically perceive all or one-step compressed vision ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Additionally, we employ a set of history queries Qh ∈ RNh×Cq and a long-term memory bank M ∈R(Nh×n)×Cq to efficiently retrieve and ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Although some methods [52, 60] also leverage the memory bank to store preceding information, they typically perceive all or one-step compressed vision ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** compress, extract, multi-view, image, features, derived, vision, encoder, while, achieving, long-term, information, modeling, introduce, QT-Former, querybased, temporal, module, Fig, there.
- **Relevant PDF headings:** 2.2. Vision-Language Models (VLMs) (p. 2); 3. Method (p. 3); 3.2. Large Language Model (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Additionally, we compare our method with other baselines on nuScenes [7] open-loop evaluation (details in Appendix). | p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics) |
| Semantic / temporal fusion | By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] ... | p. 7 (4.5. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics) |
| Robot query / planning handoff | By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] ... | p. 7 (4.5. Ablation Study), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |

## Failure and Ablation Link

- **p. 7 / 4.5. Ablation Study - extractive body cue:** We then investigate the effect of employing different generative planners to bridge the reasoning-action space.
- **p. 6 / 4.5. Ablation Study - extractive body cue:** To ensure the fairness of the ablations, experiments of different paradigms use the same sensor inputs, vision encoder, QT-former, and VLM as our ORION and ...
- **p. 7 / 4.5. Ablation Study - extractive body cue:** Ablation on diverse generative planner.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Ablation of history queries number.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Ablation on QT-Former designs in different frameworks.
- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** For open-loop evaluation, we use the L2 distance error and the collision rate.
- **p. 6 / 25.00 71.11 78.33 30.00 69.15 54.72(+16.12) - extractive body cue:** On the other hand, our model falls behind DriveAdapter in Merging and Give Way, which shows that ORION is not good at making lane-changing decisions.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. QT-Former), p. 4 (3.3. Generative Planner), p. 4 (3.1. QT-Former), p. 5 (3.3. Generative Planner), p. 5 (3.3. Generative Planner), p. 3 (3. Method), objective p. 5 (3.4. Training Objectives), p. 5 (3.4. Training Objectives), p. 4 (3.3. Generative Planner), p. 4 (3.1. QT-Former), temporal p. 4 (3.1. QT-Former), p. 4 (3.1. QT-Former), p. 2 (1. Introduction), p. 8 (4.5. Ablation Study), p. 3 (2.3. VLM for End-to-End Autonomous Driving), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
