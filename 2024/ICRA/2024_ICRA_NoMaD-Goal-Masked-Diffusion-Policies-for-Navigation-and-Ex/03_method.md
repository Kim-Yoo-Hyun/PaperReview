# Method - NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.07896; PDF retrieval source: https://arxiv.org/pdf/2310.07896. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD)): For the ViNT observation encoder, we use EfficientNet-B0 [39] to tokenize observations and goals into 256-dimensional embeddings, followed by a Transformer decoder with 4 layers and 4 heads.

## Method Body Digest

- **p. 4 / IV. METHOD - extractive body cue:** For the ViNT observation encoder, we use EfficientNet-B0 [39] to tokenize observations and goals into 256-dimensional embeddings, followed by a Transformer decoder with 4 layers ...
- **p. 3 / IV. METHOD - extractive body cue:** Training a shared policy across both behaviors allows the model to learn a more expressive prior over actions at, which can be used for both ...
- **p. 3 / IV. METHOD - extractive body cue:** To effectively model such complex distributions, we use a diffusion model [23] to approximate the conditional distribution p(at/ct), where ct is the observation context obtained ...
- **p. 4 / IV. METHOD - extractive body cue:** Note that we model the conditional (and not joint) action distribution, excluding ct from the output of the denoising process, which enables real-time control and ...
- **p. 4 / IV. METHOD - extractive body cue:** The predicted noise is compared to the actual noise through the mean squared error (MSE) loss.
- **p. 4 / IV. METHOD - extractive body cue:** The iterative denoising process follows the equation ak-1 t = α · (ak t -γϵθ(ct, ak t , k) + N(0, σ2I)) (1) where k ...
- **p. 3 / IV. METHOD - extractive body cue:** During training, the goal mask m is sampled from a Bernoulli distribution with probability pm.
- **p. 3 / IV. METHOD - extractive body cue:** For example, at a junction, the policy might need to assign high probabilities to left and right turns, but low probability to any action that ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a design for such a policy by combining a Transformer backbone for encoding the highdimensional stream of visual observations with ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The main contribution of our work is Navigation with Goal Masked Diffusion, or NoMaD, a novel architecture for robotic navigation in previously unseen environments.
- **p. 4 / IV. METHOD - extractive body cue:** The noise prediction network, ϵθ, consists of a 1D conditional U-Net [29, 31] with 15 convolutional layers.

## Source Evidence Cues

- **p. 4 / IV. METHOD - extractive body cue:** For the ViNT observation encoder, we use EfficientNet-B0 [39] to tokenize observations and goals into 256-dimensional embeddings, followed by a Transformer decoder with 4 layers ...
- **p. 3 / IV. METHOD - extractive body cue:** Training a shared policy across both behaviors allows the model to learn a more expressive prior over actions at, which can be used for both ...
- **p. 3 / IV. METHOD - extractive body cue:** To effectively model such complex distributions, we use a diffusion model [23] to approximate the conditional distribution p(at/ct), where ct is the observation context obtained ...
- **p. 4 / IV. METHOD - extractive body cue:** Note that we model the conditional (and not joint) action distribution, excluding ct from the output of the denoising process, which enables real-time control and ...
- **Detected method headings:** IV. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | For the ViNT observation encoder, we use EfficientNet-B0 [39] to tokenize observations and goals into 256-dimensional embeddings, followed by a Transformer decoder ... | p. 4 (IV. METHOD), p. 3 (IV. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Training a shared policy across both behaviors allows the model to learn a more expressive prior over actions at, which can be ... | p. 3 (IV. METHOD), p. 3 (IV. METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | To effectively model such complex distributions, we use a diffusion model [23] to approximate the conditional distribution p(at/ct), where ct is the ... | p. 3 (IV. METHOD), p. 4 (IV. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. METHOD - extractive body cue:** The predicted noise is compared to the actual noise through the mean squared error (MSE) loss.
- **p. 4 / IV. METHOD - extractive body cue:** The iterative denoising process follows the equation ak-1 t = α · (ak t -γϵθ(ct, ak t , k) + N(0, σ2I)) (1) where k ...
- **p. 3 / IV. METHOD - extractive body cue:** During training, the goal mask m is sampled from a Bernoulli distribution with probability pm.
- **p. 3 / IV. METHOD - extractive body cue:** For example, at a junction, the policy might need to assign high probabilities to left and right turns, but low probability to any action that ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (IV. METHOD), p. 4 (IV. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | objective, design, control, policy, visual, navigation, takes, robot, current, past, RGB, observations, input, ot-P | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | objective, design, control, policy, visual, navigation, takes, robot, current, past | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | present, design, policy, combining, Transformer, backbone, encoding, highdimensional, stream, visual | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | predicted, noise, compared, actual, through, mean, squared, error, MSE, loss | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. PRELIMINARIES - extractive body cue:** Our objective is to design a control policy π for visual navigation that takes the robot's current and past RGB observations as input ot := ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a design for such a policy by combining a Transformer backbone for encoding the highdimensional stream of visual observations with ...
- **p. 2 / III. PRELIMINARIES - extractive body cue:** ViNT uses an EfficientNet-B0 encoder [39] ψ(oi) to process each observation image i ∈{t -P, . . . , t} independently, as well as a ...
- **p. 3 / IV. METHOD - extractive body cue:** Diffusion Policy While goal masking allows for a convenient way to condition the policy on a goal image, the distribution over actions that results from ...
- **p. 3 / IV. METHOD - extractive body cue:** The NoMaD architecture has two key components: (i) attention-based goal-masking, which provides a flexible mechanism for conditioning the policy on (or masking out) an optional ...
- **p. 4 / IV. METHOD - extractive body cue:** Note that we model the conditional (and not joint) action distribution, excluding ct from the output of the denoising process, which enables real-time control and ...
- **p. 4 / IV. METHOD - extractive body cue:** We sample a sequence of future actions aK t from a Gaussian distribution and perform K iterations of denoising to produce a series of intermediate ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | x6 Goal Optional Transformer 4 Layers, 4 Heads 5M Parameters Observations Past 5 timesteps 96x96x3 RGB Context Average Pooled Temporal Distance Goal ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | To facilitate long-horizon exploration and goal-seeking, we follow the setup of ViKiNG [35] and pair π(ot) with a topological memory of the ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | To facilitate long-horizon exploration and goal-seeking, we follow the setup of ViKiNG [35] and pair π(ot) with a topological memory of the ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | x6 Goal Optional Transformer 4 Layers, 4 Heads 5M Parameters Observations Past 5 timesteps 96x96x3 RGB Context Average Pooled Temporal Distance Goal ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / IV. METHOD - extractive body cue:** Training a shared policy across both behaviors allows the model to learn a more expressive prior over actions at, which can be used for both ...
- **p. 4 / IV. METHOD - extractive body cue:** Note that we model the conditional (and not joint) action distribution, excluding ct from the output of the denoising process, which enables real-time control and ...
- **p. 4 / IV. METHOD - extractive body cue:** We use the AdamW optimizer [43] with a learning rate of 10-4 and train NoMaD for 30 epochs with a batch size of 256.
- **p. 5 / V. EVALUATION - extractive body cue:** Diffusion Policy: We train a diffusion policy [31] with the same visual encoder as NoMaD and m = 0.
- **p. 6 / V. EVALUATION - extractive body cue:** We find the choice of visual encoder to be crucial for training diffusion policies, as summarized in Table III.
- **p. 6 / V. EVALUATION - extractive body cue:** We use a straight-through estimator [44] for propagating gradients to the observation and goal encoders during training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ViNT, observation, encoder, EfficientNet-B0, tokenize, observations, goals, dimensional, embeddings, followed, Transformer, decoder, layers, heads, Training, shared, policy, across, behaviors, allows.
- **Relevant PDF headings:** IV. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Benchmarking Performance Towards understanding Q1, we compare NoMaD to six performant baselines for exploration and navigation in 6 challenging real-world environments. | p. 4 (V. EVALUATION), p. 4 (V. EVALUATION) |
| Global / local decision | Most notably, NoMaD outperforms the state-of-the-art (Subgoal Diffusion) by 25%, while also avoiding collisions and requiring 15× fewer parameters. mThese baselines that ... | p. 5 (V. EVALUATION), p. 5 (V. EVALUATION) |
| Motion execution / recovery | NoMaD consistently outperforms all baselines and results in smooth, reactive policies. | p. 5 (V. EVALUATION), p. 5 (V. EVALUATION) |

## Failure and Ablation Link

- **p. 5 / V. EVALUATION - extractive body cue:** Random Subgoals: A variation of the above ViNT system which replaces subgoal diffusion with randomly sampling the training data for a candidate subgoal, which is ...
- **p. 6 / VI. DISCUSSION - extractive body cue:** While our experiments provide a proof of concept that unified policies can provide more effective navigation in new environments, our system has a number of ...
- **p. 3 / 8 Future - extractive body cue:** Exploration with topological maps: While goalconditioned policies can exhibit useful affordances and collision-avoidance behavior, they may be insufficient for navigation in large environments that require ...
- **p. 4 / V. EVALUATION - extractive body cue:** We report the mean success rate for each baseline, as well as the mean number of collisions per experiment.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Visualizing the task-agnostic (yellow) and goal-directed pathways for two goal images (green, blue) learned by NoMaD. NoMaD predicts a bimodal distribution of collision-free ...
- **p. 5 / V. EVALUATION - extractive body cue:** VIB and Masked ViNT struggle in all the environments we tested and frequently end in collisions, likely due to challenges with effectively modeling multimodal action ...
- **p. 5 / V. EVALUATION - extractive body cue:** For exploratory goal discovery, NoMaD outperforms the best published baseline (Subgoal Diffusion) by over 25% in terms of both efficiency and collision avoidance, and succeeds ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD), objective p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), temporal p. 3 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (V. EVALUATION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** For the ViNT observation encoder, we use EfficientNet-B0 [39] to tokenize observations and goals into 256-dimensional embeddings, followed by a Transformer decoder with 4 layers and 4 heads. (p. 4, IV. METHOD).
- **Objective/update evidence:** The predicted noise is compared to the actual noise through the mean squared error (MSE) loss. (p. 4, IV. METHOD).
- **Temporal/runtime evidence:** Training a single policy to model such complex, multimodal distributions over action sequences is challenging. (p. 3, IV. METHOD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
