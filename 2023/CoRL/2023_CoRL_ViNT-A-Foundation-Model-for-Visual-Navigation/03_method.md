# Method - ViNT: A Foundation Model for Visual Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14846; PDF retrieval source: https://arxiv.org/pdf/2306.14846. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 18 (B.2 Subgoal Diffusion), p. 18 (B.2 Subgoal Diffusion), p. 21 (B.4 Fine-tuning ViNT), p. 21 (B.4 Fine-tuning ViNT), p. 19 (B.2 Subgoal Diffusion), p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs)): To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select osi to fall between 5 and 20 timesteps ...

## Method Body Digest

- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select osi to fall ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** [49], we use the unweighted training objective, called Lsimple in Ho et al.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** This architecture is illustrated in Figure 14. • Training: For our experiments, we use "left", "right", and "straight" as our discrete commands.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** We then pass this into a 2-layer MLP which outputs the prediction of the final token for the transformer.
- **p. 19 / B.2 Subgoal Diffusion - extractive body cue:** 2048 # Attention Layers nL 4 # Attention Heads nH 4 Temporal Context P 5 Prediction Horizon H 5 MLP layers (256, 128, 64, 32) ...
- **p. 20 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** We train a convolutional neural network on the overhead image to predict the probability that the subgoal s is included on a trajectory from ot ...
- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** Image Fine-tuning: • Architecture: We utilize the exact same architecture as ViNT with no changes. • Training: For fine-tuning the image-goal directed model, we utilize ...
- **p. 19 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** Nodes are visited according to a costing function f(s) that depends on the distance from the current state ot to the parent node s-(measured along ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We propose a novel exploration algorithm for the visual navigation paradigm using a diffusion model to propose short-horizon goals, and demonstrate that it enables ViNT ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose the Visual Navigation Transformer, or ViNT: a cross-embodiment foundation model for visual navigation with strong zero-shot generalization.
- **p. 20 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** Each ResNet consists of 2 residual blocks.

## Source Evidence Cues

- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select osi to fall ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** [49], we use the unweighted training objective, called Lsimple in Ho et al.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** This architecture is illustrated in Figure 14. • Training: For our experiments, we use "left", "right", and "straight" as our discrete commands.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** We then pass this into a 2-layer MLP which outputs the prediction of the final token for the transformer.
- **p. 19 / B.2 Subgoal Diffusion - extractive body cue:** 2048 # Attention Layers nL 4 # Attention Heads nH 4 Temporal Context P 5 Prediction Horizon H 5 MLP layers (256, 128, 64, 32) ...
- **p. 20 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** We train a convolutional neural network on the overhead image to predict the probability that the subgoal s is included on a trajectory from ot ...
- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** Image Fine-tuning: • Architecture: We utilize the exact same architecture as ViNT with no changes. • Training: For fine-tuning the image-goal directed model, we utilize ...
- **Detected method headings:** A ViNT Model Architecture (p. 17); A.1 Goal-Conditioning Architectures (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select ... | p. 18 (B.2 Subgoal Diffusion), p. 18 (B.2 Subgoal Diffusion) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | [49], we use the unweighted training objective, called Lsimple in Ho et al. | p. 18 (B.2 Subgoal Diffusion), p. 21 (B.4 Fine-tuning ViNT) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | This architecture is illustrated in Figure 14. • Training: For our experiments, we use "left", "right", and "straight" as our discrete commands. | p. 21 (B.4 Fine-tuning ViNT), p. 21 (B.4 Fine-tuning ViNT) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 20 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** We train a convolutional neural network on the overhead image to predict the probability that the subgoal s is included on a trajectory from ot ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** [49], we use the unweighted training objective, called Lsimple in Ho et al.
- **p. 19 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** Nodes are visited according to a costing function f(s) that depends on the distance from the current state ot to the parent node s-(measured along ...
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** Once we have a future goal coordinate for self-supervision, we convert to local coordinates and pass into our architecture, finetuning with the same objective as ...
- **p. 19 / B.2 Subgoal Diffusion - extractive body cue:** Head Dim 8 Channels (128, 128, 256, 512, 640) Diffusion Type continuous time Noise Schedule linear Hyperparameter Value Diffusion Training Dropout 0.1 Batch Size 128 ...
- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** Image Fine-tuning: • Architecture: We utilize the exact same architecture as ViNT with no changes. • Training: For fine-tuning the image-goal directed model, we utilize ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 18 (B.2 Subgoal Diffusion), p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs), p. 21 (B.4 Fine-tuning ViNT), p. 19 (B.2 Subgoal Diffusion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, image, input, produces, samples, where, candidate, subgoal, images, reachable, Algorithm, Long-Horizon, Navigation, Topological | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | takes, image, input, produces, samples, where, candidate, subgoal, images, reachable | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | novel, exploration, algorithm, visual, navigation, paradigm, diffusion, model, short-horizon, goals | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | train, convolutional, neural, network, overhead, image, predict, probability, subgoal, included | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** It takes an image ot as input and produces samples from g(osi / ot), where osi are candidate subgoal images reachable from ot.
- **p. 20 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** Algorithm 1: Long-Horizon Navigation via Topological Graph 1: while goal G not reached do 2: s ←minf(Ω); 3: P ←ShortestPath(M, ot, s-) 4: for (s, ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** [39], we implement image conditioning as simple channel-wise concatenation to the U-Net input.
- **p. 19 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** Nodes are visited according to a costing function f(s) that depends on the distance from the current state ot to the parent node s-(measured along ...
- **p. 2 / 1 Introduction - extractive body cue:** We specifically consider the problem of visual navigation, where the robot must navigate its environment solely using egocentric visual observations.
- **p. 2 / 1 Introduction - extractive body cue:** Such a model should provide a broadly capable navigation policy on top of which applications to specific domains can be constructed, giving a base level ...
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** We then pass this into a 2-layer MLP which outputs the prediction of the final token for the transformer.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | ViNT takes as input current and past visual observations ot-P :t and a subgoal image os, and predicts (i) the number of ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | 2048 # Attention Layers nL 4 # Attention Heads nH 4 Temporal Context P 5 Prediction Horizon H 5 MLP layers (256, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select osi to fall ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** [49], we use the unweighted training objective, called Lsimple in Ho et al.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** This architecture is illustrated in Figure 14. • Training: For our experiments, we use "left", "right", and "straight" as our discrete commands.
- **p. 19 / B.2 Subgoal Diffusion - extractive body cue:** 2048 # Attention Layers nL 4 # Attention Heads nH 4 Temporal Context P 5 Prediction Horizon H 5 MLP layers (256, 128, 64, 32) ...
- **p. 20 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** We train a convolutional neural network on the overhead image to predict the probability that the subgoal s is included on a trajectory from ot ...
- **p. 20 / B.4 Fine-tuning ViNT - extractive body cue:** Image Fine-tuning: • Architecture: We utilize the exact same architecture as ViNT with no changes. • Training: For fine-tuning the image-goal directed model, we utilize ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** produce, training, pairs, diffusion, model, first, select, uniformly, random, data, then, fall, between, timesteps, future, unweighted, objective, called, Lsimple, architecture.
- **Relevant PDF headings:** A ViNT Model Architecture (p. 17); A.1 Goal-Conditioning Architectures (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | [22], we further augment this dataset by allowing the rule-based agent to correct its position and re-center to the lane after a ... | p. 20 (B.4 Fine-tuning ViNT), p. 21 (B.4 Fine-tuning ViNT) |
| Global / local decision | Table 1: ViNT paired with our physical search algorithm consistently outperforms baselines for the task of undirected goal-reaching in indoor and outdoor ... | p. 7 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Motion execution / recovery | Figure 4: Adapting ViNT to different goals using a new tunable goal token. Full model fine-tuning: While ViNT demonstrates strong zero-shot generalization ... | p. 6 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: ViNT can effectively utilize goal-directed heuristics, such as 2D goal positions and satellite images, to explore novel kilometer-scale environments successfully and without interventions. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Left: ViNT can be fine-tuned end-to-end (Images) or adapted to downstream tasks (Positions and Routing), and outperforms training from scratch and other pre-training ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: In coverage tasks, ViNT drives dif- ferent robots for 100s of meters (reported maxi- mum displacement without intervention), beating lower-capacity models (GNM) and ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** We use the Flax U-Net implementation from the diffusers library [48] with textual cross-attention removed since we do not condition on text inputs.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Overview of the ViNT foundation model. ViNT generalizes zero-shot across environments and robot embodiments, and can be directly applied to tasks including exploration ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Adapting ViNT to different goals using a new tunable goal token. Full model fine-tuning: While ViNT demonstrates strong zero-shot generalization to new environments ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: ViNT accomplishes long-horizon navigation with a variety of objectives in indoor and outdoor environments; example trajectories between start (orange) and goal (green) visualized ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 18 (B.2 Subgoal Diffusion), p. 18 (B.2 Subgoal Diffusion), p. 21 (B.4 Fine-tuning ViNT), p. 21 (B.4 Fine-tuning ViNT), p. 19 (B.2 Subgoal Diffusion), p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs), objective p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs), p. 18 (B.2 Subgoal Diffusion), p. 19 (B.3 Long-Horizon Physical Search via Topological Graphs), p. 21 (B.4 Fine-tuning ViNT), p. 19 (B.2 Subgoal Diffusion), p. 20 (B.4 Fine-tuning ViNT), temporal p. 3 (7 Tokens), p. 18 (B.2 Subgoal Diffusion), p. 19 (B.2 Subgoal Diffusion), p. 19 (B.2 Subgoal Diffusion), p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs), p. 3 (7 Tokens).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
