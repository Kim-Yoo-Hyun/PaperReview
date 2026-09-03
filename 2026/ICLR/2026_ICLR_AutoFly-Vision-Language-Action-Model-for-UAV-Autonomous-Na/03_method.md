# Method - AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=88RKxlFUNY; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247860. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES), p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL)): 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language instruction L, and coarse positional or directional guidance ...

## Method Body Digest

- **p. 4 / 3 METHOD - extractive body cue:** 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language instruction L, and ...
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We replace the SigLIP visual backbone with SigLIP 2 (fused with DINOv2), a state-of-the-art RGB encoder, to assess whether improved visual features can substitute for ...
- **p. 4 / 3 METHOD - extractive body cue:** To enhance geometric reasoning capability, we introduce AutoFly, a VLA architecture augmented with pseudo-depth encoding.
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We compare the following approaches against our baseline (we use the OpenVLA here) and the full AutoFly model: • Data Scaling.
- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** To overcome these limitations, we develop specialized obstacle avoidance agents using reinforcement learning, training independent models for each scene.
- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** Qθ(s, a) represents the current Q-network's estimate for the state-action pair (s, a), indicating the expected cumulative reward obtainable after taking action a from state ...
- **p. 22 / A.5.4 PARALLEL INFERENCE ARCHITECTURE - extractive body cue:** This pipelining strategy leverages the observation that LLM inference typically dominates the computational bottleneck in VLA models.
- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** When d = 0 (episode continues), the target includes both the immediate reward r and the discounted estimate of future returns.

## Design Rationale

- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive body cue:** This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework.
- **p. 4 / 3 METHOD - extractive body cue:** To enhance geometric reasoning capability, we introduce AutoFly, a VLA architecture augmented with pseudo-depth encoding.
- **p. 4 / 3 METHOD - extractive body cue:** Our framework integrates three core components, including a visionlanguage model, pseudo-depth encoder, and action de-tokenizer, as illustrated in Figure 2.

## Source Evidence Cues

- **p. 4 / 3 METHOD - extractive body cue:** 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language instruction L, and ...
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We replace the SigLIP visual backbone with SigLIP 2 (fused with DINOv2), a state-of-the-art RGB encoder, to assess whether improved visual features can substitute for ...
- **p. 4 / 3 METHOD - extractive body cue:** To enhance geometric reasoning capability, we introduce AutoFly, a VLA architecture augmented with pseudo-depth encoding.
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We compare the following approaches against our baseline (we use the OpenVLA here) and the full AutoFly model: • Data Scaling.
- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** To overcome these limitations, we develop specialized obstacle avoidance agents using reinforcement learning, training independent models for each scene.
- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** Qθ(s, a) represents the current Q-network's estimate for the state-action pair (s, a), indicating the expected cumulative reward obtainable after taking action a from state ...
- **p. 22 / A.5.4 PARALLEL INFERENCE ARCHITECTURE - extractive body cue:** This pipelining strategy leverages the observation that LLM inference typically dominates the computational bottleneck in VLA models.
- **Detected method headings:** 3 METHOD (p. 4); A.2.3 DATA COLLECTION ALGORITHM BASED ON RL (p. 16); A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES (p. 20); A.4 METHODOLOGY DETAILS (p. 21); A.5.1 DISTRIBUTED SYSTEM ARCHITECTURE (p. 21); A.5.3 MODEL ACCELERATION (p. 22); A.5.4 PARALLEL INFERENCE ARCHITECTURE (p. 22)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language ... | p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We replace the SigLIP visual backbone with SigLIP 2 (fused with DINOv2), a state-of-the-art RGB encoder, to assess whether improved visual features ... | p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES), p. 4 (3 METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | To enhance geometric reasoning capability, we introduce AutoFly, a VLA architecture augmented with pseudo-depth encoding. | p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** When d = 0 (episode continues), the target includes both the immediate reward r and the discounted estimate of future returns.
- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** The specific supervision process for the actor network is as follows: Lπ(ϕ) = Es∼D  α log πϕ(a/s) -min i=1,2 Qθ(s, a)  , (7) ...
- **p. 4 / 3 METHOD - extractive body cue:** The goal is to derive an optimal policy π∗: (O, L) →A that generates a collision-free planning trajectory τ respecting UAV kinodynamic constraints, ultimately reaching ...
- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive body cue:** Given the constraints of our UAV navigation domain, we adapt baseline architectures while preserving their core methodological contributions: • RT-1 (Brohan et al., 2022): We ...
- **p. 22 / A.5.4 PARALLEL INFERENCE ARCHITECTURE - extractive body cue:** To minimize end-to-end latency, we implement a pipelined multi-process inference system that overlaps visual processing with LLM computation, as shown in Figure 14.
- **p. 22 / A.5.4 PARALLEL INFERENCE ARCHITECTURE - extractive body cue:** The architecture employs two parallel processes: a vision pipeline handling RGB encoding, depth generation, and feature projection, and an LLM pipeline processing multimodal tokens for ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3 METHOD), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | TASK, FORMULATION, formulate, autonomous, navigation, learning, control, policy, takes, current, RGB, observation, language, instruction | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | TASK, FORMULATION, formulate, autonomous, navigation, learning, control, policy, takes, current | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | standardized, backbone, enables, fair, comparison, core, contributions, while, maintaining, implementation | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | When, episode, continues, target, includes, immediate, reward, discounted, estimate, future | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 METHOD - extractive body cue:** 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language instruction L, and ...
- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** For a stochastic policy, the target value y is calculated as: y = r + γ(1 -d)  min i=1,2 Qθ′ i(s′, a′) -α log ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Vision-language navigation (VLN) (Chen et al., 2019; Ku et al., 2020; Misra et al., 2018; Krantz et al., 2020; Anderson et al., 2018; Thomason et ...
- **p. 4 / 3 METHOD - extractive body cue:** Our framework integrates three core components, including a visionlanguage model, pseudo-depth encoder, and action de-tokenizer, as illustrated in Figure 2.
- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** Qθ(s, a) represents the current Q-network's estimate for the state-action pair (s, a), indicating the expected cumulative reward obtainable after taking action a from state ...
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We collect an additional 1,000 episodes (∼350K vision-language-action pairs) to evaluate the effect of increased training data. • Data Augmentation.
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We replace the SigLIP visual backbone with SigLIP 2 (fused with DINOv2), a state-of-the-art RGB encoder, to assess whether improved visual features can substitute for ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | This represents a significant improvement over sequential processing, reducing end-toend latency from 120ms to 85ms per frame, enabling real-time UAV control at ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | After the initial sequential cycle, visual processing for frame t+1 overlaps with LLM inference for frame t, reducing per-frame latency from 120ms ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | This represents a significant improvement over sequential processing, reducing end-toend latency from 120ms to 85ms per frame, enabling real-time UAV control at ... | hardware, batch and throughput |

## Training vs Inference

- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We replace the SigLIP visual backbone with SigLIP 2 (fused with DINOv2), a state-of-the-art RGB encoder, to assess whether improved visual features can substitute for ...
- **p. 17 / A.2.3 DATA COLLECTION ALGORITHM BASED ON RL - extractive body cue:** To overcome these limitations, we develop specialized obstacle avoidance agents using reinforcement learning, training independent models for each scene.
- **p. 22 / A.5.4 PARALLEL INFERENCE ARCHITECTURE - extractive body cue:** This pipelining strategy leverages the observation that LLM inference typically dominates the computational bottleneck in VLA models.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We maintain the default cross-entropy loss function from the base language model and employ a learning rate of 2e-5 for the VLM backbone and 1e-4 ...
- **p. 22 / A.5.4 PARALLEL INFERENCE ARCHITECTURE - extractive body cue:** The optimized pipeline achieves near-optimal throughput where total inference time approaches the LLM inference duration plus inter-process communication overhead (approximately 15-20ms).
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 4.1 IMPLEMENTATION DETAILS This section presents implementation details across three components: training details, evaluation details, and robot setup.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** TASK, FORMULATION, formulate, autonomous, navigation, learning, control, policy, takes, current, RGB, observation, language, instruction, coarse, positional, directional, guidance, encoded, initial.
- **Relevant PDF headings:** 3 METHOD (p. 4); A.2.3 DATA COLLECTION ALGORITHM BASED ON RL (p. 16); A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES (p. 20); A.4 METHODOLOGY DETAILS (p. 21); A.5.1 DISTRIBUTED SYSTEM ARCHITECTURE (p. 21); A.5.3 MODEL ACCELERATION (p. 22); A.5.4 PARALLEL INFERENCE ARCHITECTURE (p. 22).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Our training set comprises 10 scenes with 50 object instances, totaling over 13K episodes and 2.5M image-language-action triplets. | p. 16 (A.2.2 DATASET SPLIT), p. 15 (A.2.1 DATASET CONSTRUCTION) |
| Global / local decision | The results in Table 4 demonstrate that the method with the pseudo-depth encoder (47.9%, 21.9%) in success rate and collision rate significantly ... | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Motion execution / recovery | Results demonstrate clear performance differences: SigLIP achieves the highest success rate among single encoders (46.6%), outperforming CLIP (43.1%) by 3.5% and DINO ... | p. 19 (A.3.2 ABLATION EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** To validate the effectiveness of our pseudo-depth encoder, we conduct ablation studies comparing models with and without the depth encoder.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.4 ABLATION EXPERIMENTS We conduct comprehensive ablation studies to validate our model's effectiveness, systematically evaluating five key components: pseudo-depth encoder ablation, specialized depth projector validation, ...
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We collect an additional 1,000 episodes (∼350K vision-language-action pairs) to evaluate the effect of increased training data. • Data Augmentation.
- **p. 19 / A.3.2 ABLATION EXPERIMENTS - extractive body cue:** To investigate the impact of different vision encoders on task performance, we conduct comprehensive ablation experiments comparing four representative vision backbones: CLIP, DINO, SigLIP, and ...
- **p. 18 / A.2.4 DATASET REBALANCING - extractive body cue:** We apply stratified resampling as follows: Group sub-trajectories by phase into Dk = {τ (k) i }, compute sample sizes nk = round(wk · /Dk/), ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 5: Results (%) for depth projector ablations.
- **p. 10 / Figure/Table caption - extractive body cue:** Table 7: Results (%) for depth-vision- language alignment study. Variant SR CR PER (a) Siam 47.9

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES), p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), objective p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 4 (3 METHOD), p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 22 (A.5.4 PARALLEL INFERENCE ARCHITECTURE), p. 22 (A.5.4 PARALLEL INFERENCE ARCHITECTURE), temporal p. 22 (A.5.4 PARALLEL INFERENCE ARCHITECTURE), p. 22 (A.5.2 NETWORK COMMUNICATION PROTOCOL), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 8 (4 EXPERIMENTS), p. 19 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
