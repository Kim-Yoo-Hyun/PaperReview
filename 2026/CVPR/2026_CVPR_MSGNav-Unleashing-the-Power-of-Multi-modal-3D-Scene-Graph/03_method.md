# Method - MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3.3.4. Visibility-based Viewpoint Decision (VVD)), p. 8 (4.3.3. Decision-making for "Last-mile"), p. 6 (3.3.3. Closed-Loop Reasoning (CLR)), p. 5 (3.3.1. Key Subgraph Selection (KSS)), p. 5 (3.3. MSGNav Embodied Navigation System), p. 3 (3.1.2. Overview)): To achieve this goal, we propose a Visibility-based Viewpoint Decision (VVD) module (in Algorithm 2).

## Method Body Digest

- **p. 6 / 3.3.4. Visibility-based Viewpoint Decision (VVD) - extractive body cue:** To achieve this goal, we propose a Visibility-based Viewpoint Decision (VVD) module (in Algorithm 2).
- **p. 8 / 4.3.3. Decision-making for "Last-mile" - extractive body cue:** The first row without any module, which represents our baseline model 3D-Mem [43] results. "VVD", "AVU", and "CRV" represent the Visibility-based Viewpoint Decision module, Adaptive ...
- **p. 6 / 3.3.3. Closed-Loop Reasoning (CLR) - extractive body cue:** In addition to modeling the scene as perception memory, we introduce the decision memory M for closed-loop reasoning.
- **p. 5 / 3.3.1. Key Subgraph Selection (KSS) - extractive body cue:** We first simplify the rich but vast scene graph S into the compact adjacency list representation ˆS = (ˆO, ˆE).
- **p. 5 / 3.3. MSGNav Embodied Navigation System - extractive body cue:** 3(b), our MSGNav first significantly reduces the tokens and time cost required for inference by selecting key subgraphs (Sec.
- **p. 3 / 3.1.2. Overview - extractive body cue:** This image edge preserves the benefits of 3D scene graphs while avoiding repeated, costly model queries and providing a more holistic scene representation.
- **p. 3 / 3.1.1. Problem definition - extractive body cue:** At each time step t, it obtains an RGB-D observation It and executes an action At (camera rotation or ego-motion) to actively explore until locating ...
- **p. 4 / 3.2.2. Incremental Construction of M3DSG - extractive body cue:** (4) This edge update process is efficient, eliminating the need for costly VLM queries.

## Design Rationale

- **p. 3 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • M3DSG: We propose a multi-modal 3D scene graph that incorporates visual information, overcoming pure-text limitations and enhancing ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this issue, we introduce a visibility-based viewpoint decision module in our MSGNav.
- **p. 2 / 1. Introduction - extractive body cue:** 1, we introduce the Multi-modal 3D Scene Graph (M3DSG), which replaces the pure-text relational edges with dynamically assigned images to incorporate visual cues, and facilitates ...

## Source Evidence Cues

- **p. 6 / 3.3.4. Visibility-based Viewpoint Decision (VVD) - extractive body cue:** To achieve this goal, we propose a Visibility-based Viewpoint Decision (VVD) module (in Algorithm 2).
- **p. 8 / 4.3.3. Decision-making for "Last-mile" - extractive body cue:** The first row without any module, which represents our baseline model 3D-Mem [43] results. "VVD", "AVU", and "CRV" represent the Visibility-based Viewpoint Decision module, Adaptive ...
- **p. 6 / 3.3.3. Closed-Loop Reasoning (CLR) - extractive body cue:** In addition to modeling the scene as perception memory, we introduce the decision memory M for closed-loop reasoning.
- **p. 5 / 3.3.1. Key Subgraph Selection (KSS) - extractive body cue:** We first simplify the rich but vast scene graph S into the compact adjacency list representation ˆS = (ˆO, ˆE).
- **p. 5 / 3.3. MSGNav Embodied Navigation System - extractive body cue:** 3(b), our MSGNav first significantly reduces the tokens and time cost required for inference by selecting key subgraphs (Sec.
- **p. 3 / 3.1.2. Overview - extractive body cue:** This image edge preserves the benefits of 3D scene graphs while avoiding repeated, costly model queries and providing a more holistic scene representation.
- **p. 3 / 3.1.1. Problem definition - extractive body cue:** At each time step t, it obtains an RGB-D observation It and executes an action At (camera rotation or ego-motion) to actively explore until locating ...
- **Detected method headings:** 3. Approach (p. 3); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To achieve this goal, we propose a Visibility-based Viewpoint Decision (VVD) module (in Algorithm 2). | p. 6 (3.3.4. Visibility-based Viewpoint Decision (VVD)), p. 8 (4.3.3. Decision-making for "Last-mile") |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The first row without any module, which represents our baseline model 3D-Mem [43] results. "VVD", "AVU", and "CRV" represent the Visibility-based Viewpoint ... | p. 8 (4.3.3. Decision-making for "Last-mile"), p. 6 (3.3.3. Closed-Loop Reasoning (CLR)) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | In addition to modeling the scene as perception memory, we introduce the decision memory M for closed-loop reasoning. | p. 6 (3.3.3. Closed-Loop Reasoning (CLR)), p. 5 (3.3.1. Key Subgraph Selection (KSS)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2.2. Incremental Construction of M3DSG - extractive body cue:** (4) This edge update process is efficient, eliminating the need for costly VLM queries.
- **p. 6 / 3.3.4. Visibility-based Viewpoint Decision (VVD) - extractive body cue:** t ∈[τ, ∥p -vi∥-τ] o 8: E(vi, p) = ∀q ∈Q(vi, p) : mins∈PC ∥q -s∥≥τ 9: Svi ← 1 /PC¯o/ P p∈PC¯o 1E(vi,p) ▷Visibility ...
- **p. 3 / 3.1.2. Overview - extractive body cue:** This image edge preserves the benefits of 3D scene graphs while avoiding repeated, costly model queries and providing a more holistic scene representation.
- **p. 3 / 3.1.1. Problem definition - extractive body cue:** In the zero-shot navigation setting, the agent performs navigation without task-specific training or fine-tuning in simulation, thereby reducing training cost and improving generalization to unseen ...
- **p. 4 / 3.1.2. Overview - extractive body cue:** To mitigate the inference cost of numerous images during exploration, we design a dynamic allocation algorithm that efficiently converts the multimodal 3D scene graph into ...
- **p. 5 / 3.3.2. Adaptive Vocabulary Update (AVU) - extractive body cue:** Such constraints hinder VLMs from handling diverse out-of-vocabulary scene representations in the real world.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.3.2. Adaptive Vocabulary Update (AVU)), p. 4 (3.2.2. Incremental Construction of M3DSG), p. 4 (3.2.2. Incremental Construction of M3DSG), p. 5 (3.3.2. Adaptive Vocabulary Update (AVU)), p. 8 (4.3.3. Decision-making for "Last-mile").
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | time, step, obtains, RGB-D, observation, executes, action, camera, rotation, ego-motion, actively, explore, until, locating | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | time, step, obtains, RGB-D, observation, executes, action, camera, rotation, ego-motion | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contributions, summarized, follows, M3DSG, multi-modal, scene, graph, incorporates, visual, information | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | edge, update, process, efficient, eliminating, need, costly, VLM, queries, mins | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1.1. Problem definition - extractive body cue:** At each time step t, it obtains an RGB-D observation It and executes an action At (camera rotation or ego-motion) to actively explore until locating ...
- **p. 4 / 3.1.2. Overview - extractive body cue:** At time step t, the agent incrementally constructs the scene graph St based on received observation It and its own pose.
- **p. 4 / 3.1.2. Overview - extractive body cue:** Observation Pose (a) Construction of M3DSG VFMs Visual Spatial Room Livingroom bathroom Kitchen … �� Attribution �1 �2 �3
- **p. 7 / 4.3.2. Advantage of M3DSG - extractive body cue:** Concept-graph outperforms Node-only by 4.4% in SR and 1.5% in SPL, especially for Language and Image goals, underscoring the value of relationship edges.
- **p. 2 / 1. Introduction - extractive body cue:** Notably, a series of methods [35, 36] that build explicit 3D scene graphs from observations and leverage LLMs to drive exploration have shown promising performance ...
- **p. 3 / 3.1.2. Overview - extractive body cue:** Formally, at each time step t, M3DSG incrementally integrates the RGB-D observation It into an evolving scene graph S.
- **p. 5 / 3.3. MSGNav Embodied Navigation System - extractive body cue:** Meanwhile, MSGNav performs closed-loop reasoning via decision memory and feedback (Sec.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Formally, at each time step t, M3DSG incrementally integrates the RGB-D observation It into an evolving scene graph S. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | At each time step t, it obtains an RGB-D observation It and executes an action At (camera rotation or ego-motion) to actively ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. MSGNav Embodied Navigation System - extractive body cue:** 3(b), our MSGNav first significantly reduces the tokens and time cost required for inference by selecting key subgraphs (Sec.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** achieve, goal, Visibility-based, Viewpoint, Decision, VVD, module, Algorithm, first, without, represents, baseline, model, D-Mem, AVU, CRV, represent, Adaptive, Vocabulary, Update.
- **Relevant PDF headings:** 3. Approach (p. 3); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We evaluate our proposed approach on two established goal-oriented navigation benchmarks: 1) GOAT-Bench [19] (Multi-modal lifelong open-vocabulary dataset, 360 episodes, 36 scenes, ... | p. 6 (4.1. Experimental Setting), p. 6 (4.1. Experimental Setting) |
| Global / local decision | As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the ... | p. 7 (4.2.2. HM3D-ObjNav Benchmark), p. 8 (Figure/Table caption) |
| Motion execution / recovery | As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the ... | p. 7 (4.2.2. HM3D-ObjNav Benchmark), p. 6 (4.1. Experimental Setting) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Component ablation experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. The first row without any module, ...
- **p. 7 / 4.3. Ablation Analysis - extractive body cue:** Specifically, this includes component ablation, the advantages of multimodal edges, and demonstrating how the VVD module aids in "last-mile" decision-making.
- **p. 7 / 4.2.2. HM3D-ObjNav Benchmark - extractive body cue:** Although our Success Path Length (SPL) is nearly the same as WMNav without any significant advantage, this may be because the VVD module prioritizes viewpoints ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Scene graph experiment across the first episode of each scene on the "Val Unseen" split of GOAT-Bench. "Node-only" indicates Concept-graph [9] without object ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Statistical box plot of candidate viewpoint scores com- puted by the VVD module and distances from GT viewpoints. representations in embodied navigation. Limitations ...
- **p. 8 / 5. Conclusion - extractive body cue:** In this paper, we propose the MSGNav, a zero-shot embodied navigation framework built upon a Multi-modal 3D Scene Graph (M3DSG) that preserves visual information for ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Demonstration of the "last-mile" problem. (a) Previ- ous methods select the nearest traversable position after target lo- calization, and often fail due to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3.3.4. Visibility-based Viewpoint Decision (VVD)), p. 8 (4.3.3. Decision-making for "Last-mile"), p. 6 (3.3.3. Closed-Loop Reasoning (CLR)), p. 5 (3.3.1. Key Subgraph Selection (KSS)), p. 5 (3.3. MSGNav Embodied Navigation System), p. 3 (3.1.2. Overview), objective p. 4 (3.2.2. Incremental Construction of M3DSG), p. 6 (3.3.4. Visibility-based Viewpoint Decision (VVD)), p. 3 (3.1.2. Overview), p. 3 (3.1.1. Problem definition), p. 4 (3.1.2. Overview), p. 5 (3.3.2. Adaptive Vocabulary Update (AVU)), temporal p. 3 (3.1.2. Overview), p. 3 (3.1.1. Problem definition), p. 4 (3.1.2. Overview), p. 6 (3.3.3. Closed-Loop Reasoning (CLR)), p. 6 (3.3.3. Closed-Loop Reasoning (CLR)), p. 8 (4.3.3. Decision-making for "Last-mile").
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
