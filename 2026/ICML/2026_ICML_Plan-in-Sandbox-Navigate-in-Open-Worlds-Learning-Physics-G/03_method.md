# Method - Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=W5e8c9nwNo; PDF retrieval source: https://openreview.net/pdf/27299763732e881621b2b6f37e47e47722f2e575.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (2.3. Navigation Task), p. 3 (2.1. Physics-Grounded Interaction Sandbox)): To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O.

## Method Body Digest

- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O.
- **p. 3 / 2.1. Physics-Grounded Interaction Sandbox - extractive PDF cue:** P(s′/s, a) denotes the state transition dynamics.
- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** 3 within the abstracted sandbox, the agent progressively acquires robust priors, ultimately allowing transfer to minimize the realworld objective JN (θ).
- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** Intuitively, the core objective is to optimize the policy against the synthesized experiences: Jϕ(θ) = E o∼O, at∼πθ(·/st,o), st+1∼P(·/st,at) "X t=0 γtrϕ(st, at, o) # ...
- **p. 3 / 2.1. Physics-Grounded Interaction Sandbox - extractive PDF cue:** A represents the agent's action space, which we decompose into the selection of discrete intermediate observations and their corresponding navigable waypoints.
- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** For any specific task n ∼N, the agent aims to reach the target state via a policy πθ(a/s, n), which maximizes the expected cumulative reward ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Physics-Grounded Sandbox Optimized Policy Hybrid Sampling w/o exp Observations Augmented Samples Task Task Task Task Experience Hybrid Samples ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Simulator Env Frontier Node Memory Node Sandbox Open-world Experience Question Observation w/ exp Optimized Policy 1 2 1 2 3 Frontier 2 3 2 Memory ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Instead of relying on difficult exploration in the real world, we propose operating the VLM within a physics-grounded sandbox to synthesize diverse tasks and proactively ...
- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O.

## Source Evidence Cues

- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O.
- **p. 3 / 2.1. Physics-Grounded Interaction Sandbox - extractive PDF cue:** P(s′/s, a) denotes the state transition dynamics.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O. | p. 3 (2.3. Navigation Task), p. 3 (2.1. Physics-Grounded Interaction Sandbox) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | P(s′/s, a) denotes the state transition dynamics. | p. 3 (2.1. Physics-Grounded Interaction Sandbox) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O. | p. 3 (2.3. Navigation Task) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** 3 within the abstracted sandbox, the agent progressively acquires robust priors, ultimately allowing transfer to minimize the realworld objective JN (θ).
- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** Intuitively, the core objective is to optimize the policy against the synthesized experiences: Jϕ(θ) = E o∼O, at∼πθ(·/st,o), st+1∼P(·/st,at) "X t=0 γtrϕ(st, at, o) # ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (2.3. Navigation Task), p. 3 (2. Problem Formulation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | represents, agent, action, space, decompose, selection, discrete, intermediate, observations, corresponding, navigable, waypoints, specific, task | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | represents, agent, action, space, decompose, selection, discrete, intermediate, observations, corresponding | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, contributions, introduce, novel, Generative, Experience-Driven, Learning, paradigm, address, severe | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | within, abstracted, sandbox, agent, progressively, acquires, robust, priors, ultimately, allowing | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2.1. Physics-Grounded Interaction Sandbox - extractive PDF cue:** A represents the agent's action space, which we decompose into the selection of discrete intermediate observations and their corresponding navigable waypoints.
- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** For any specific task n ∼N, the agent aims to reach the target state via a policy πθ(a/s, n), which maximizes the expected cumulative reward ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Physics-Grounded Sandbox Optimized Policy Hybrid Sampling w/o exp Observations Augmented Samples Task Task Task Task Experience Hybrid Samples ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Simulator Env Frontier Node Memory Node Sandbox Open-world Experience Question Observation w/ exp Optimized Policy 1 2 1 2 3 Frontier 2 3 2 Memory ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Although the research community has turned to Reinforcement Learning (RL) to facilitate policy adaptation (Zeng et al., 2024; Choi et al., 2024; Wang & Huang, ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The first is goal-based navigation (Chang et al., 2023; Ziliotto et al., 2025; Yin et al., 2025), which requires the embodied agent to navigate to ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Ultimately, the full SAGE framework achieves peak performance by equipping this optimized policy with Cret, demonstrating a synergistic effect where the policy ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | At time step t, the robot receives RGB-D observations from the environment. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Conversely, aggressive updates (ϵexp = 1.2) lead to instability and performance degradation after 100 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.2. Main Navigation Results - extractive PDF cue:** Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation 0 50 100 150 200 Training Steps 42 44 46 48 ...
- **p. 8 / 4.4. Analysis on Evolution - extractive PDF cue:** An optimally relaxed bound (ϵexp = 1.0) balances this, enabling rapid experience absorption without policy collapse, achieving a peak SR† of 53.21% and SPL† of ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, approximating, optimal, behavior, maximizing, surrogate, objective, within, sandbox, task, distribution, denotes, state, transition, dynamics, abstracted, agent, progressively, acquires, robust.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | GOAT-Bench: This benchmark challenges robots to sequentially execute 5 to 10 subtasks within unseen real-world scenes. | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Global / local decision | SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin. | p. 6 (4.2. Main Navigation Results), p. 6 (4.2. Main Navigation Results) |
| Motion execution / recovery | SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin. | p. 6 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation) |

## Failure and Ablation Link

- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** We benchmark SAGE against a diverse set of state-of-the-art (SOTA) methods categorized into two paradigms: (1) RL Paradigm, including SenseAct-NN variants (Khanna et al., 2024); ...
- **p. 8 / 4.5. Analysis and Ablation - extractive PDF cue:** Effects of Main Components. "Task" denotes synthesized tasks; "Exp" denotes experience rules; "AAC" denotes Asymmetric Adaptive Clipping.
- **p. 8 / 4.4. Analysis on Evolution - extractive PDF cue:** An optimally relaxed bound (ϵexp = 1.0) balances this, enabling rapid experience absorption without policy collapse, achieving a peak SR† of 53.21% and SPL† of ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 8. Effect of mismatched experience injection. All values are in percent (%).
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 9. Sensitivity to ϵexp schedules. All values are in percent (%). Schedule A-EQA GOAT-Bench SR† SPL† SR SPL
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 7. Visualization of the word cloud. rules using regular expressions. The entire trajectory is discarded if the generated output fails to match the required ...
- **p. 23 / Figure/Table caption - extractive PDF cue:** Table 14. Computational Cost per Navigation Step (Real-World) Component Hardware / Spec Metric Value VLM Inference NVIDIA RTX 4090 (24GB) Latency

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (2.3. Navigation Task), p. 3 (2.1. Physics-Grounded Interaction Sandbox), objective p. 3 (2.3. Navigation Task), p. 3 (2.3. Navigation Task), temporal p. 8 (4.5. Analysis and Ablation), p. 5 (3.3. Navigation), p. 6 (3.3. Navigation), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Main Navigation Results), p. 8 (4.4. Analysis on Evolution).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
