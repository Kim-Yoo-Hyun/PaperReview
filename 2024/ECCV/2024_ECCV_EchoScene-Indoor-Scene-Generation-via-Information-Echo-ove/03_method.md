# Method - EchoScene: Indoor Scene Generation via Information Echo over Scene Graph Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3146_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03146.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 8 (4 Method), p. 6 (4 Method), p. 10 (4 Method), p. 6 (4 Method), p. 7 (4 Method), p. 7 (4 Method)): In this form, one sending and one receiving step constitute an ‘ information echo.' Note that the Langevin dynamics here are different from the ones in a normal diffusion model, ...

## Method Body Digest

- **p. 8 / 4 Method - extractive body cue:** In this form, one sending and one receiving step constitute an ‘ information echo.' Note that the Langevin dynamics here are different from the ones ...
- **p. 6 / 4 Method - extractive body cue:** After the encoding, node features evolve to VZ = {vz i / i = 1, . . . , N}, where vz i consists of ...
- **p. 10 / 4 Method - extractive body cue:** The objective of the training is to minimize the noise prediction errors: Lshape = EX,"⇠N (0,1),t ⇥ //" -"✓(Xt, ⇡(t), Us(GSt)//2 2 ⇤ , GSt ...
- **p. 6 / 4 Method - extractive body cue:** To make the layout and shape branches aware of the semantic and spatial information among the objects, we first encode the contextual graph to have ...
- **p. 7 / 4 Method - extractive body cue:** To achieve both highly controllable and consistent generation at the same time, we propose to couple the inverse iterative conditional diffusion mechanism on graph node ...
- **p. 7 / 4 Method - extractive body cue:** EchoScene 7 B.2 Shape Branch Denoiser εθ Shape Encoder S Xt Xt-1 S' X0 XT ··· ··· ··· ··· Shape Decoder Noise A.2 Latent Contextual ...
- **p. 8 / 4 Method - extractive body cue:** Then, the process sends VDt to U, which comprehensively understands group dynamics according to graph edges E, by subscribing and aggregating information from all processes.
- **p. 9 / 4 Method - extractive body cue:** For each time step, we encourage the layout (left) and shape (right) branches to exchange information within each branch for all objects in the same ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** We introduce an information echo scheme inside each branch of EchoScene that allows multiple denoising processes to exchange their denoising status among each other at ...
- **p. 3 / 1 Introduction - extractive body cue:** We present EchoScene, a scene generation method with a dual-branch diffusion model on dynamic scene graphs, to simultaneously generate layouts and shapes with more controllability.
- **p. 5 / 4 Method - extractive body cue:** We present EchoScene, a method that accomplishes scene generation through layout and shape generation from scene graphs.

## Source Evidence Cues

- **p. 8 / 4 Method - extractive body cue:** In this form, one sending and one receiving step constitute an ‘ information echo.' Note that the Langevin dynamics here are different from the ones ...
- **p. 6 / 4 Method - extractive body cue:** After the encoding, node features evolve to VZ = {vz i / i = 1, . . . , N}, where vz i consists of ...
- **p. 10 / 4 Method - extractive body cue:** The objective of the training is to minimize the noise prediction errors: Lshape = EX,"⇠N (0,1),t ⇥ //" -"✓(Xt, ⇡(t), Us(GSt)//2 2 ⇤ , GSt ...
- **p. 6 / 4 Method - extractive body cue:** To make the layout and shape branches aware of the semantic and spatial information among the objects, we first encode the contextual graph to have ...
- **p. 7 / 4 Method - extractive body cue:** To achieve both highly controllable and consistent generation at the same time, we propose to couple the inverse iterative conditional diffusion mechanism on graph node ...
- **p. 7 / 4 Method - extractive body cue:** EchoScene 7 B.2 Shape Branch Denoiser εθ Shape Encoder S Xt Xt-1 S' X0 XT ··· ··· ··· ··· Shape Decoder Noise A.2 Latent Contextual ...
- **p. 8 / 4 Method - extractive body cue:** Then, the process sends VDt to U, which comprehensively understands group dynamics according to graph edges E, by subscribing and aggregating information from all processes.
- **Detected method headings:** 4 Method (p. 5); 11 Method (p. 11); 13 Method (p. 13)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | In this form, one sending and one receiving step constitute an ‘ information echo.' Note that the Langevin dynamics here are different ... | p. 8 (4 Method), p. 6 (4 Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | After the encoding, node features evolve to VZ = {vz i / i = 1, . . . , N}, where vz ... | p. 6 (4 Method), p. 10 (4 Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The objective of the training is to minimize the noise prediction errors: Lshape = EX,"⇠N (0,1),t ⇥ //" -"✓(Xt, ⇡(t), Us(GSt)//2 2 ... | p. 10 (4 Method), p. 6 (4 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 10 / 4 Method - extractive body cue:** The objective of the training is to minimize the noise prediction errors: Lshape = EX,"⇠N (0,1),t ⇥ //" -"✓(Xt, ⇡(t), Us(GSt)//2 2 ⇤ , GSt ...
- **p. 9 / 4 Method - extractive body cue:** For each time step, we encourage the layout (left) and shape (right) branches to exchange information within each branch for all objects in the same ...
- **p. 7 / 4 Method - extractive body cue:** As each generation proceeds individually, there is no awareness of scene content during the denoising steps, which makes the generation inconsistent with global constraints in ...
- **p. 8 / 4 Method - extractive body cue:** Since the bounding box generation needs to be compliant with the spatial constraints described in the scene graph, state observation from other nodes is needed ...
- **p. 8 / 4 Method - extractive body cue:** In this form, one sending and one receiving step constitute an ‘ information echo.' Note that the Langevin dynamics here are different from the ones ...
- **p. 12 / 11 Method - extractive body cue:** 5.2 Graph Constraints In this part, we evaluate the layout generation performance with respect to scene graph constraints.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 10 (4 Method), p. 7 (4 Method), p. 8 (4 Method), p. 8 (4 Method), p. 9 (4 Method), p. 12 (11 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Since, bounding, generation, needs, compliant, spatial, constraints, described, scene, graph, state, observation, other, nodes | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Since, bounding, generation, needs, compliant, spatial, constraints, described, scene, graph | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | introduce, information, echo, scheme, inside, branch, EchoScene, allows, multiple, denoising | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | objective, training, minimize, noise, prediction, errors, Lshape, GSt, VSt, Dual-Branch | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / 4 Method - extractive body cue:** Since the bounding box generation needs to be compliant with the spatial constraints described in the scene graph, state observation from other nodes is needed ...
- **p. 2 / 1 Introduction - extractive body cue:** First, due to varying numbers of graph nodes and manipulator-induced node-edge operations, the input scene graphs dynamically describe global scene states, thus demanding adaptability from ...
- **p. 2 / 1 Introduction - extractive body cue:** In an attempt to flexibly encapsulate information from an indefinite number of nodes without losing global graph constraints, it can be helpful to allocate an ...
- **p. 6 / 4 Method - extractive body cue:** The manipulation includes node addition and relation change, mimicking the user interaction.
- **p. 6 / 4 Method - extractive body cue:** In this case, we initialize the input embeddings of layer 0 with the features from the contextual graph, thus, (β(0) vi , β(0) ei!j, β(0) ...
- **p. 8 / 4 Method - extractive body cue:** 1, with input (β(0) vi , β(0) ei!j, β(0) vj ) = (vdt i , ei!j, vdt j ), where vdt i and vdt j ...
- **p. 9 / 4 Method - extractive body cue:** We solve the problem by introducing shape observation of other processes for each process, which is achieved by shape echoes.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Ul to achieve global awareness at each time step. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Thus, layout echoes happen at each time step by using Eq. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4 Method - extractive body cue:** In this form, one sending and one receiving step constitute an ‘ information echo.' Note that the Langevin dynamics here are different from the ones ...
- **p. 10 / 4 Method - extractive body cue:** The objective of the training is to minimize the noise prediction errors: Lshape = EX,"⇠N (0,1),t ⇥ //" -"✓(Xt, ⇡(t), Us(GSt)//2 2 ⇤ , GSt ...
- **p. 10 / 5 Experiments - extractive body cue:** Training is optimized with AdamW with an initial learning rate of 1e-4.
- **p. 10 / 5 Experiments - extractive body cue:** The training, evaluation, and visualization are carried out on a single NVIDIA A40 GPU with 40 GB of memory.
- **p. 7 / 4 Method - extractive body cue:** As each generation proceeds individually, there is no awareness of scene content during the denoising steps, which makes the generation inconsistent with global constraints in ...
- **p. 8 / 4 Method - extractive body cue:** We follow a normal DDPM training routine, in which we set 1000 time steps for all diffusion processes with weight-shared γ✓.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** form, sending, receiving, step, constitute, information, echo, Note, Langevin, dynamics, here, different, ones, normal, diffusion, model, where, introduce, relationship, group.
- **Relevant PDF headings:** 4 Method (p. 5); 11 Method (p. 11); 13 Method (p. 13).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We conduct our experiments on SG-FRONT dataset [58], which provides scene-graph annotations for the high-quality 3D-FRONT [16] with household environments. | p. 10 (5 Experiments), p. 10 (5 Experiments) |
| Global / local decision | Table 2: Scene graph constraints (higher is better). Top: Relationship change mode. Middle: Node addition mode. Bottom: No manipulation (i.e., generation only). ... | p. 13 (Figure/Table caption), p. 14 (Figure/Table caption) |
| Motion execution / recovery | Fig. 4: Comparisons with other generative methods. Input scene graphs have more edges between two nodes than the ones visualized here. Red ... | p. 12 (Figure/Table caption), p. 10 (5 Experiments) |

## Failure and Ablation Link

- **p. 14 / Figure/Table caption - extractive body cue:** Table 4: Ablations under three cir- cumstances. mSG means average graph constraints. observe a marginal decrease, indicating even without ⇡(t), the model still learns temporal ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Inter-object Consistency. The consistent object shapes within a scene are indicated by low CD values (⇥0.001). Ablation FID FIDCLIP KID mSG Ours w/o ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of EchoScene. Our pipeline consists of graph preprocessing and two collaborative branches Layout Branch and Shape Branch. The details of two branches ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 3: One Step of Dual-Branch Information Echo. For each time step, we encourage the layout (left) and shape (right) branches to exchange information within ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 4: Ablations under three cir- cumstances. mSG means average graph constraints. observe a marginal decrease, indicating even without ⇡(t), the model still learns temporal ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 8 (4 Method), p. 6 (4 Method), p. 10 (4 Method), p. 6 (4 Method), p. 7 (4 Method), p. 7 (4 Method), objective p. 10 (4 Method), p. 9 (4 Method), p. 7 (4 Method), p. 8 (4 Method), p. 8 (4 Method), p. 12 (11 Method), temporal p. 8 (4 Method), p. 8 (4 Method), p. 9 (4 Method), p. 10 (4 Method), p. 10 (4 Method), p. 14 (13 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
