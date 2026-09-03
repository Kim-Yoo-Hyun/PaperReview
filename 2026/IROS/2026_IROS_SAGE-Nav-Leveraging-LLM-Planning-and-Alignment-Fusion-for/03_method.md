# Method - SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.25497; PDF retrieval source: https://arxiv.org/pdf/2606.25497. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (IV. PROPOSED METHOD), p. 3 (IV. PROPOSED METHOD), p. 2 (IV. PROPOSED METHOD)): Finally, the unified state representation is fed into an attentive Actor-Critic [6] network featuring a two-layer LSTM [40] to maintain temporal coherence and generate the action policy πθ(at / ht, ...

## Method Body Digest

- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** Finally, the unified state representation is fed into an attentive Actor-Critic [6] network featuring a two-layer LSTM [40] to maintain temporal coherence and generate the ...
- **p. 3 / IV. PROPOSED METHOD - extractive body cue:** 1: Pipeline Overview: (i) LLM-Guided Hierarchical Global Planner (H-GP) generates semantic waypoint sequences; (ii) Hierarchical Scene Graph Encoder (HSGE) grounds the plan in structured spatial-semantic ...
- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** These structural priors are then adaptively fused with real-time egocentric observations via the Goal-Aware Alignment-Fusion Network (GAFN).
- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** Upon merging, the cluster's spatial and visual attributes (pk, fk) are updated via online averaging of its children.
- **p. 2 / I. INTRODUCTION - extractive body cue:** It decomposes abstract instructions into semantic waypoints, effectively decoupling asynchronous global reasoning from high-frequency control. • We design the Hierarchical Scene Graph Encoder (HSGE) to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Deep Reinforcement Learning (DRL) has empowered agents to learn end-to-end navigation policies [4, 5] directly from egocentric visual inputs, achieving efficient exploration and object-goal approach ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This forces lowlevel DRL policies to infer long-horizon strategies directly from fused features, compromising interpretability and leaving the agent without progress feedback during execution.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are threefold: • We propose SAGE-Nav, a hierarchical navigation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our method constructs a hierarchical scene graph as an explicit environment prior.
- **p. 2 / I. INTRODUCTION - extractive body cue:** By leveraging relational graph convolutions, it produces structure-aware embeddings designed to capture both semantic and spatial hierarchies. • We develop the Goal-aware Alignment-Fusion Network (GAFN) ...

## Source Evidence Cues

- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** Finally, the unified state representation is fed into an attentive Actor-Critic [6] network featuring a two-layer LSTM [40] to maintain temporal coherence and generate the ...
- **p. 3 / IV. PROPOSED METHOD - extractive body cue:** 1: Pipeline Overview: (i) LLM-Guided Hierarchical Global Planner (H-GP) generates semantic waypoint sequences; (ii) Hierarchical Scene Graph Encoder (HSGE) grounds the plan in structured spatial-semantic ...
- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** These structural priors are then adaptively fused with real-time egocentric observations via the Goal-Aware Alignment-Fusion Network (GAFN).
- **Detected method headings:** IV. PROPOSED METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Finally, the unified state representation is fed into an attentive Actor-Critic [6] network featuring a two-layer LSTM [40] to maintain temporal coherence ... | p. 2 (IV. PROPOSED METHOD), p. 3 (IV. PROPOSED METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | 1: Pipeline Overview: (i) LLM-Guided Hierarchical Global Planner (H-GP) generates semantic waypoint sequences; (ii) Hierarchical Scene Graph Encoder (HSGE) grounds the plan ... | p. 3 (IV. PROPOSED METHOD), p. 2 (IV. PROPOSED METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | These structural priors are then adaptively fused with real-time egocentric observations via the Goal-Aware Alignment-Fusion Network (GAFN). | p. 2 (IV. PROPOSED METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** Upon merging, the cluster's spatial and visual attributes (pk, fk) are updated via online averaging of its children.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 2 (IV. PROPOSED METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Finally, unified, state, representation, attentive, Actor-Critic, network, featuring, two-layer, LSTM, maintain, temporal, coherence, generate | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Finally, unified, state, representation, attentive, Actor-Critic, network, featuring, two-layer, LSTM | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, contributions, threefold, SAGE-Nav, hierarchical, navigation, arXiv, Jun, contrast, constructs | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Upon, merging, cluster, spatial, visual, attributes, updated, online, averaging, children | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** Finally, the unified state representation is fed into an attentive Actor-Critic [6] network featuring a two-layer LSTM [40] to maintain temporal coherence and generate the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** It decomposes abstract instructions into semantic waypoints, effectively decoupling asynchronous global reasoning from high-frequency control. • We design the Hierarchical Scene Graph Encoder (HSGE) to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Deep Reinforcement Learning (DRL) has empowered agents to learn end-to-end navigation policies [4, 5] directly from egocentric visual inputs, achieving efficient exploration and object-goal approach ...
- **p. 3 / IV. PROPOSED METHOD - extractive body cue:** 1: Pipeline Overview: (i) LLM-Guided Hierarchical Global Planner (H-GP) generates semantic waypoint sequences; (ii) Hierarchical Scene Graph Encoder (HSGE) grounds the plan in structured spatial-semantic ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This forces lowlevel DRL policies to infer long-horizon strategies directly from fused features, compromising interpretability and leaving the agent without progress feedback during execution.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Following CogNav [27], our online 3D scene graph integrates OpenSEED [48] segmentation, multi-frame fusion, and VLM-driven relation reasoning, dynamically aggregating nodes via ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | SG-Nav reduces this latency to 0.85 s but requires frequent LLM queries (32 calls per episode). | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | SG-Nav reduces this latency to 0.85 s but requires frequent LLM queries (32 calls per episode). | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / V. EXPERIMENTS - extractive body cue:** The A3C [6] policy is trained for 6 million episodes using Adam (learning rate 1 × 10-4).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Finally, unified, state, representation, attentive, Actor-Critic, network, featuring, two-layer, LSTM, maintain, temporal, coherence, generate, action, policy, Pipeline, Overview, LLM-Guided, Hierarchical.
- **Relevant PDF headings:** IV. PROPOSED METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Experimental Setup 1) Datasets: We evaluate the proposed framework across two widely used embodied simulation datasets: iTHOR [45] and RoboTHOR [46]. iTHOR ... | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Global / local decision | In iTHOR, SAGE-Nav achieves state-of-the-art Success Rates (SR) of 82.47% overall and 77.22% in challenging long-horizon scenarios (L ≥5), outperforming TSOG and ... | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Motion execution / recovery | In iTHOR, SAGE-Nav achieves state-of-the-art Success Rates (SR) of 82.47% overall and 77.22% in challenging long-horizon scenarios (L ≥5), outperforming TSOG and ... | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Ablation Study on Zero-shot Generalization.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Ablation Studies Table IV summarizes the ablation study of proposed modules.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Notably, when GAFN is removed and substituted with simple feature concatenation (ID 6), the model exhibits a marginal SPL gain but a concurrent deterioration in ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Consequently, the optimization exclusively focuses on tuning the learnable components, namely the Hierarchical Scene Graph Encoder (HSGE) and the LSTM-based policy network.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Component analysis further elucidates the hierarchical contributions of each module to the zero-shot capability.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Limitations We analyze the failure cases (Fig.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** 5), which fall into four categories: (a) Target Visibility Failure, where the agent terminates despite the target (e.g., plates on high shelves) being outside the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (IV. PROPOSED METHOD), p. 3 (IV. PROPOSED METHOD), p. 2 (IV. PROPOSED METHOD), objective p. 2 (IV. PROPOSED METHOD), temporal p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 2 (IV. PROPOSED METHOD), p. 2 (IV. PROPOSED METHOD), p. 3 (IV. PROPOSED METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
