# Method - Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (Method), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 5 (3.4. Vision-Language-Exploration Training)): Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that ...

## Method Body Digest

- **p. 3 / Method - extractive body cue:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We ...
- **p. 3 / Method - extractive body cue:** When combined with a large vision-language model, serving as its trajectory generator, our approach improves the embodied question answering for LM-SR by 2.4% and LLM-SPL ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** The unified decision scores SU t are optimized with binary cross-entropy loss, teaching the model to assign higher scores to appropriate query locations based on ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** We utilize RGBD trajectories from ScanNet and HM3D to train query representation with instance segmentation loss.
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** Lbox is the 3D box IoU loss; Lmask and Lscore are binary cross-entropy losses; Lvocab is cosine similarity loss.
- **p. 3 / Method - extractive body cue:** MTU3D uniquely integrates advantages from both sides, supporting online exploration and lifelong visual grounding. time decision-making.
- **p. 2 / 1. Introduction - extractive body cue:** (a) 3D-VL Model (b) End-to-End RL (c) MTU3D (Ours) Full RGB-D Video Time World Visual Grounding Model Explicit Mesh Open loop Single RGB-D image World ...
- **p. 3 / Method - extractive body cue:** Specifically, MTU3D improves the state-of-the-art results by 13.7%, 23.0%, and 9.1% in SR, and 2.4%, 13.0%, and 6.3% in SPL on HM3D-OVON [79], GOAT-Bench [37], ...

## Design Rationale

- **p. 3 / Method - extractive body cue:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Move to Understand (MTU3D), a unified framework that bridges visual grounding and exploration for versatile embodied navigation as shown ...
- **p. 2 / 1. Introduction - extractive body cue:** Our approach introduces three key innovations:

## Source Evidence Cues

- **p. 3 / Method - extractive body cue:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We ...
- **p. 3 / Method - extractive body cue:** When combined with a large vision-language model, serving as its trajectory generator, our approach improves the embodied question answering for LM-SR by 2.4% and LLM-SPL ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** The unified decision scores SU t are optimized with binary cross-entropy loss, teaching the model to assign higher scores to appropriate query locations based on ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** We utilize RGBD trajectories from ScanNet and HM3D to train query representation with instance segmentation loss.
- **Detected method headings:** Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied ... | p. 3 (Method), p. 3 (Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | When combined with a large vision-language model, serving as its trajectory generator, our approach improves the embodied question answering for LM-SR by ... | p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The unified decision scores SU t are optimized with binary cross-entropy loss, teaching the model to assign higher scores to appropriate query ... | p. 5 (3.4. Vision-Language-Exploration Training), p. 5 (3.4. Vision-Language-Exploration Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** The unified decision scores SU t are optimized with binary cross-entropy loss, teaching the model to assign higher scores to appropriate query locations based on ...
- **p. 3 / Method - extractive body cue:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** Lbox is the 3D box IoU loss; Lmask and Lscore are binary cross-entropy losses; Lvocab is cosine similarity loss.
- **p. 3 / Method - extractive body cue:** MTU3D uniquely integrates advantages from both sides, supporting online exploration and lifelong visual grounding. time decision-making.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 5 (3.4. Vision-Language-Exploration Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | D-VL, Model, End-to-End, MTU3D, Ours, Full, RGB-D, Video, Time, World, Visual, Grounding, Explicit, Mesh | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | D-VL, Model, End-to-End, MTU3D, Ours, Full, RGB-D, Video, Time, World | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, present, MTU3D, bridging, visual, grounding, exploration | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | unified, decision, scores, optimized, binary, cross-entropy, loss, teaching, model, assign | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** (a) 3D-VL Model (b) End-to-End RL (c) MTU3D (Ours) Full RGB-D Video Time World Visual Grounding Model Explicit Mesh Open loop Single RGB-D image World ...
- **p. 3 / Method - extractive body cue:** Specifically, MTU3D improves the state-of-the-art results by 13.7%, 23.0%, and 9.1% in SR, and 2.4%, 13.0%, and 6.3% in SPL on HM3D-OVON [79], GOAT-Bench [37], ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** The unified decision scores SU t are optimized with binary cross-entropy loss, teaching the model to assign higher scores to appropriate query locations based on ...
- **p. 3 / Method - extractive body cue:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We ...
- **p. 2 / 1. Introduction - extractive body cue:** Similarly, an embodied agent navigating a new environment must operate in a continuous closed-loop cycle of exploration, perception, reasoning, and action [31, 64, 73].
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** In VLE pre-training, we utilize stage 1 output queries to jointly train exploration and grounding.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | This is achieved by three key innovations: 1) Online query-based representation learning, enabling direct spatial memory construction from RGB-D frames, eliminating the ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We reset spatial memory in w/o mem for each sub-episode in GOAT-Bench, and the experimental results in Fig. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | This is achieved by three key innovations: 1) Online query-based representation learning, enabling direct spatial memory construction from RGB-D frames, eliminating the ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | In Stage 1, we train for 50 epochs using AdamW (learning rate 1e-4, β1 = 0.9, β2 = 0.98) with loss weights ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / Method - extractive body cue:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** We utilize RGBD trajectories from ScanNet and HM3D to train query representation with instance segmentation loss.
- **p. 6 / 4.1. Experimental setting - extractive body cue:** In Stage 1, we train for 50 epochs using AdamW (learning rate 1e-4, β1 = 0.9, β2 = 0.98) with loss weights λb = 1.0, ...
- **p. 6 / 4.1. Experimental setting - extractive body cue:** All training runs on four NVIDIA A100 GPUs around 164 GPU hours.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** main, contributions, summarized, follows, present, MTU3D, bridging, visual, grounding, exploration, efficient, versatile, embodied, navigation, unified, objective, jointly, optimizes, leveraging, complementary.
- **Relevant PDF headings:** Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Unlike other benchmarks, SG3D emphasizes task consistency across multiple steps, making it more complex. | p. 6 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results) |
| Global / local decision | 3 demonstrate that our proposed MTU3D significantly outperforms all baselines in terms of SR across both Val Seen and Val Unseen settings. | p. 6 (4.2. Quantitative Results), p. 7 (4.2. Quantitative Results) |
| Motion execution / recovery | While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and ... | p. 6 (4.2. Quantitative Results), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 4.4. Qualitative results - extractive body cue:** Ablation studies showing (a) the impact of vision-language-exploration pretraining, (b) exploration efficiency on seen environments, and (c) the contribution of spatial memory to navigation performance.
- **p. 8 / 4.4. Qualitative results - extractive body cue:** OVON GOAT SG3D Dataset 15 20 25 30 35 40 SR (%) 27.8 22.2 22.9 33.3 36.1 27.9 VLE w/o vle w/ vle (a) Effect ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (Method), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 5 (3.4. Vision-Language-Exploration Training), objective p. 5 (3.4. Vision-Language-Exploration Training), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 3 (Method), temporal p. 1 (Abstract), p. 7 (4.3. Discussions), p. 7 (4.3. Discussions), p. 3 (2. Related work), p. 4 (3.1. Online Query Representation Learning), p. 4 (3.1. Online Query Representation Learning).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
