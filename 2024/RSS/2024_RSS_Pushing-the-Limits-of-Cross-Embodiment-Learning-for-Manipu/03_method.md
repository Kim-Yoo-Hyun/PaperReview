# Method - Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p093.html; PDF retrieval source: https://arxiv.org/pdf/2402.19432.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 2 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING)): Our heterogeneous cross-embodiment model consists of five different components: two observation encoders, a transformer, a diffusion policy action head [81], and an MLP distance prediction head for navigation with topological ...

## Method Body Digest

- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Our heterogeneous cross-embodiment model consists of five different components: two observation encoders, a transformer, a diffusion policy action head [81], and an MLP distance prediction ...
- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** At a high level, we want our model to process its observations using some encoder, feed its embeddings into a transformer, and then output both ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating for ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** Each trajectory τ ∈Dem consists of a sequence of observations (images) and actions.
- **p. 3 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** While we could simply train a single policy across all of the navigation and manipulation datasets to output action labels that match each specific dataset ...
- **p. 4 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** We use separate observation and goal convolutional encoders to tokenize visual observations, which are passed through a Transformer block.
- **p. 4 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Under these assumptions, training our policy to predict action ai would allow us to learn from Dem,1 ∪Dem,2 ∪. . . ∪Den,1 ∪Den,2 with a ...
- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Our overall objective is the weighted combination of these two losses: L(θ, ϕ, ψ) = Ldiffusion(θ, ψ) + λLdistance(θ, ψ).

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating for ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present, to our knowledge, the first results demonstrating a large-scale policy trained jointly on navigation and manipulation data from many different robots, showing that ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** Each trajectory τ ∈Dem consists of a sequence of observations (images) and actions.

## Source Evidence Cues

- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Our heterogeneous cross-embodiment model consists of five different components: two observation encoders, a transformer, a diffusion policy action head [81], and an MLP distance prediction ...
- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** At a high level, we want our model to process its observations using some encoder, feed its embeddings into a transformer, and then output both ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating for ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** Each trajectory τ ∈Dem consists of a sequence of observations (images) and actions.
- **p. 3 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** While we could simply train a single policy across all of the navigation and manipulation datasets to output action labels that match each specific dataset ...
- **p. 4 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** We use separate observation and goal convolutional encoders to tokenize visual observations, which are passed through a Transformer block.
- **p. 4 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Under these assumptions, training our policy to predict action ai would allow us to learn from Dem,1 ∪Dem,2 ∪. . . ∪Den,1 ∪Den,2 with a ...
- **Detected method headings:** 1) Can a single goal-conditioned policy successfully control (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | Our heterogeneous cross-embodiment model consists of five different components: two observation encoders, a transformer, a diffusion policy action head [81], and an ... | p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | At a high level, we want our model to process its observations using some encoder, feed its embeddings into a transformer, and ... | p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 2 (I. INTRODUCTION) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our ... | p. 2 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Our overall objective is the weighted combination of these two losses: L(θ, ϕ, ψ) = Ldiffusion(θ, ψ) + λLdistance(θ, ψ).
- **p. 3 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Note that a∗is agnostic to embodiment, meaning that optimizing an action prediction loss L(f(oi, oj), a∗), where f(oi, oj) tries to prediction a∗given its current ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** The objective of visual robotic navigation is to direct a robotic agent to move to a goal g ∈G while avoiding obstacles.
- **p. 4 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** This allows the policy to handle different action magnitudes across datasets, which otherwise would cause instability in the action loss.
- **p. 4 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Under these assumptions, training our policy to predict action ai would allow us to learn from Dem,1 ∪Dem,2 ∪. . . ∪Den,1 ∪Den,2 with a ...
- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** We train our policy with diffusion denoising loss Ldiffusion(θ, ψ) = //ϵk -ϵϕ(fθ(ot-k:t, og), a0 t + ϵk, k)//2 2, and a distance prediction loss ...
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | objective, goal-conditioned, imitation, learning, train, policy, output, actions, control, particular, embodiment, given, current, goal | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | objective, goal-conditioned, imitation, learning, train, policy, output, actions, control, particular | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | While, particular, training, methodology, model, architecture, prior, techniques, empirical, findings | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | overall, objective, weighted, combination, losses, Ldiffusion, Ldistance, Note, agnostic, embodiment | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PRELIMINARIES - extractive body cue:** The objective of goal-conditioned imitation learning is to train a policy π(a/o, og) to output actions that control a particular embodiment given the current and ...
- **p. 3 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** To solve this problem, we train a goal-conditioned policy π(a/o, og) that outputs k actions into the future given a context of c observations.
- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** For our action output head, we chose to use a diffusion policy [81] to account for noise in human demonstrations as well as different strategies ...
- **p. 7 / VI. ANALYSIS - extractive body cue:** In addition, our policy can identify and output an action for the appropriate embodiment given its current and goal observations.
- **p. 4 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Goal MLP Temporal Distance Head Diffusion Policy Action Head EfficientNet-b5 EfficientNet-b5 Context Observations Egocentric Goal Fig.
- **p. 5 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** At a high level, we want our model to process its observations using some encoder, feed its embeddings into a transformer, and then output both ...
- **p. 7 / VI. ANALYSIS - extractive body cue:** These scenarios involve spatial reasoning in novel environments (e.g., in Shelf Manipulation, the policy must learn which actions don't collide with the shelf), requiring the ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | In addition, dt denotes the distance in timesteps from the current observation and goal observation. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | The goal image is sampled uniformly at random 20 to 40 timesteps into the future from the current observation. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | For navigation, we create a topological map M by recording the robot's observations with a frequency of 4 Hz while moving the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / I. INTRODUCTION - extractive body cue:** While the particular training methodology and model architecture are based on prior techniques, the empirical findings are a novel contribution of our work, demonstrating for ...
- **p. 3 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** While we could simply train a single policy across all of the navigation and manipulation datasets to output action labels that match each specific dataset ...
- **p. 4 / IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING - extractive body cue:** Under these assumptions, training our policy to predict action ai would allow us to learn from Dem,1 ∪Dem,2 ∪. . . ∪Den,1 ∪Den,2 with a ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** heterogeneous, cross-embodiment, model, consists, five, different, components, observation, encoders, transformer, diffusion, policy, action, head, MLP, distance, prediction, navigation, topological, graphs.
- **Relevant PDF headings:** 1) Can a single goal-conditioned policy successfully control (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 -7% improvement in navigation performance (success ... | p. 8 (VI. ANALYSIS), p. 7 (VI. ANALYSIS) |
| Base-arm task decision | Training our policy on a manipulation and navigation data split had a 20% greater success rate over 5 tasks compared to training ... | p. 7 (VI. ANALYSIS), p. 9 (VI. ANALYSIS) |
| Execution / correction | Fig. 6: Does manipulation help navigation? Across three different robots in challenging indoor and outdoor environments, adding manipulation datasets leads to 5 ... | p. 8 (Figure/Table caption), p. 9 (VI. ANALYSIS) |

## Failure and Ablation Link

- **p. 8 / VI. ANALYSIS - extractive body cue:** To further examine whether information from the goal image is essential to transferring navigation data to manipulation, we ran an ablation of our method without ...
- **p. 7 / VI. ANALYSIS - extractive body cue:** Due to a difference in the camera lens used by the DJI tello, we noticed that the performance of the drone degraded significantly in environments ...
- **p. 7 / VI. ANALYSIS - extractive body cue:** For the Cluttered Grasp tasks, the gap in performance between the joint navigation-manipulation policy is larger in the out-of-distribution variant than the in-distribution variant.
- **p. 8 / VI. ANALYSIS - extractive body cue:** Operating under the assumption that the diffusion policy is powerful enough to model the different possible tasks from the current observation without conditioning on the ...
- **p. 7 / VI. ANALYSIS - extractive body cue:** Gauging object distance is analogous to testing the robustness to a change in table height in tabletop manipulation, which previous works have identified as a ...
- **p. 7 / VI. ANALYSIS - extractive body cue:** This requires the robot to avoid colliding with the shelf as well as gauge its distance to the object, which is fundamentally similar to the ...
- **p. 8 / VI. ANALYSIS - extractive body cue:** While we qualitatively observed that these policies had better estimates for the closest node and had less collision with the environment, we acknowledge that the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 2 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), objective p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 3 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 3 (III. PRELIMINARIES), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), temporal p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 5 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING), p. 6 (4) Toy Kitchen. A more semantically meaningful environ), p. 3 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), p. 4 (IV. HETEROGENEOUS CROSS-EMBODIMENT LEARNING).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
