# Method - Continuous 3D Perception Model with Persistent State

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.12387; PDF retrieval source: https://arxiv.org/pdf/2501.12387. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Training Strategy), p. 4 (3.2. Querying the State with Unseen Views), p. 3 (3. Method), p. 3 (3.1. State-Input Interaction Mechanism), p. 4 (3.2. Querying the State with Unseen Views), p. 5 (3.4. Training Strategy)): We use a ViT-Large model [22] for the image encoder Encoderi, initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders.

## Method Body Digest

- **p. 5 / 3.4. Training Strategy - extractive body cue:** We use a ViT-Large model [22] for the image encoder Encoderi, initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders.
- **p. 4 / 3.2. Querying the State with Unseen Views - extractive body cue:** Given a query raymap R, we first encode it into token representations Fr using a separate transformer Encoderr: Fr = Encoderr(R).
- **p. 3 / 3. Method - extractive body cue:** As a new image comes in through the model, it interacts with the latent state representation, which encodes the understanding of the current 3D scene.
- **p. 3 / 3.1. State-Input Interaction Mechanism - extractive body cue:** This bidirectional interaction is implemented using two interconnected transformer decoders [107, 110], which jointly operate on both image and state tokens: [z′ t, F ′ ...
- **p. 4 / 3.2. Querying the State with Unseen Views - extractive body cue:** Specifically, we use a virtual camera as a query to extract information from the state.
- **p. 5 / 3.4. Training Strategy - extractive body cue:** The state consists of 768 tokens, each with a dimensionality of 768.
- **p. 5 / 3.4. Training Strategy - extractive body cue:** These two stages are trained on 224×224 images to reduce computational costs, following DUSt3R [107].
- **p. 5 / 3.3. Training Objective - extractive body cue:** Following MASt3R [51], we apply a confidence-aware regression loss to the pointmaps: Lconf = X (ˆx,c)∈( ˆ X,C)  c ·

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to ...
- **p. 2 / 1. Introduction - extractive body cue:** Our framework is designed to be general and flexible, making it well-suited for training on an extensive collection of datasets and adaptable to diverse inference ...
- **p. 1 / 1. Introduction - extractive body cue:** Building on these insights, we introduce an online 3D perception framework that unifies three key capabilities: 1) reconstructing 3D scenes from few observations, 2) continuously ...

## Source Evidence Cues

- **p. 5 / 3.4. Training Strategy - extractive body cue:** We use a ViT-Large model [22] for the image encoder Encoderi, initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders.
- **p. 4 / 3.2. Querying the State with Unseen Views - extractive body cue:** Given a query raymap R, we first encode it into token representations Fr using a separate transformer Encoderr: Fr = Encoderr(R).
- **p. 3 / 3. Method - extractive body cue:** As a new image comes in through the model, it interacts with the latent state representation, which encodes the understanding of the current 3D scene.
- **p. 3 / 3.1. State-Input Interaction Mechanism - extractive body cue:** This bidirectional interaction is implemented using two interconnected transformer decoders [107, 110], which jointly operate on both image and state tokens: [z′ t, F ′ ...
- **p. 4 / 3.2. Querying the State with Unseen Views - extractive body cue:** Specifically, we use a virtual camera as a query to extract information from the state.
- **p. 5 / 3.4. Training Strategy - extractive body cue:** The state consists of 768 tokens, each with a dimensionality of 768.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We use a ViT-Large model [22] for the image encoder Encoderi, initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders. | p. 5 (3.4. Training Strategy), p. 4 (3.2. Querying the State with Unseen Views) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Given a query raymap R, we first encode it into token representations Fr using a separate transformer Encoderr: Fr = Encoderr(R). | p. 4 (3.2. Querying the State with Unseen Views), p. 3 (3. Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | As a new image comes in through the model, it interacts with the latent state representation, which encodes the understanding of the ... | p. 3 (3. Method), p. 3 (3.1. State-Input Interaction Mechanism) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Training Strategy - extractive body cue:** These two stages are trained on 224×224 images to reduce computational costs, following DUSt3R [107].
- **p. 5 / 3.3. Training Objective - extractive body cue:** Following MASt3R [51], we apply a confidence-aware regression loss to the pointmaps: Lconf = X (ˆx,c)∈( ˆ X,C)  c ·
- **p. 3 / 3.1. State-Input Interaction Mechanism - extractive body cue:** We refer to these interactions as state-update and state-readout, respectively.
- **p. 3 / 3. Method - extractive body cue:** Specifically, the image simultaneously updates the state with new information and retrieves information stored in the state.
- **p. 4 / 3.3. Training Objective - extractive body cue:** In these cases, we randomly replace each image with its corresponding raymap at a certain probability, excluding the first view.
- **p. 4 / 3.2. Querying the State with Unseen Views - extractive body cue:** Note that, unlike in the state-image interaction, the state is not updated here, as the raymap serves solely as a query without introducing new scene ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective), p. 3 (3.1. State-Input Interaction Mechanism), p. 3 (3. Method), p. 4 (3.2. Querying the State with Unseen Views), p. 4 (3.1. State-Input Interaction Mechanism).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Following, state-image, interaction, explicit, pointmaps, camera, poses, extracted, view, denotes, image, tokens, enriched, state | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Following, state-image, interaction, explicit, pointmaps, camera, poses, extracted, view, denotes | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | learned, prior, enables, address, challenges, encountered, traditional, methods, dynamic, objects | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | stages, trained, images, reduce, computational, costs, following, DUSt3R, MASt3R, apply | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive body cue:** Following the state-image interaction, explicit 3D pointmaps and camera poses are extracted for each view.
- **p. 3 / 3.1. State-Input Interaction Mechanism - extractive body cue:** F ′ t denotes the image tokens enriched with state information. z is a learnable "pose token" prepended to the image tokens, whose output z′ ...
- **p. 4 / 3.1. State-Input Interaction Mechanism - extractive body cue:** State 0 State 1 State 2 State 3 Image 1 Image 2 Image 3 … Pointmaps & Cameras Scene reconstruction at each time Input images ...
- **p. 4 / 3.2. Querying the State with Unseen Views - extractive body cue:** Note that, unlike in the state-image interaction, the state is not updated here, as the raymap serves solely as a query without introducing new scene ...
- **p. 2 / 1. Introduction - extractive body cue:** We evaluate our method on various 3D tasks: monocular and consistent video depth estimation, camera pose estimation, and 3D reconstruction, achieving competitive or state-of-the-art performance ...
- **p. 2 / 1. Introduction - extractive body cue:** With each new observation, the model simultaneously updates this state and reads from it to predict the current view's 3D properties, including an estimate of ...
- **p. 5 / 3.3. Training Objective - extractive body cue:** When the input is raymap, besides the 3D regression loss, we also apply an MSE loss to enforce the predicted pixel colors ˆIr to match ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Our method performs online dense 3D reconstruction from a stream of images (video frames or a photo collection) by using a persistent ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Video depth estimation evaluates per-frame depth quality and inter-frame depth consistency by aligning predicted depth maps to ground truth using a persequence ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | MonST3R finetunes DUSt3R on dynamic datasets to handle dynamic scenes, while Spann3R extends DUSt3R to support varying number of images via additional ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | While operating online, our method achieves competitive performance, on par with and even surpassing offline methods that employ global alignment. the 7-Scenes ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Training Strategy - extractive body cue:** We use a ViT-Large model [22] for the image encoder Encoderi, initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders.
- **p. 7 / 4.4. Analysis - extractive body cue:** 4.3, we introduce an additional version of our approach called "revisiting": we first run our method online to obtain the final state that has seen ...
- **p. 8 / 4.4. Analysis - extractive body cue:** This setup differs from the online setup by allowing the state to see the full context of the scene during the first run.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ViT-Large, model, image, encoder, Encoderi, initialized, DUSt3R, pretrained, weights, ViT-Base, decoders, Given, query, raymap, first, encode, token, representations, separate, transformer.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | For this experiment, we use the validation set of the MapFree [3] and ARKitScenes datasets, both with metric camera pose annotations. | p. 8 (4.4. Analysis), p. 5 (4.1. Monocular and Video Depth Estimation) |
| Global / local decision | We present a subset of baselines here; please refer to the supplementary material for full comparisons. | p. 6 (4.1. Monocular and Video Depth Estimation), p. 5 (4.1. Monocular and Video Depth Estimation) |
| Motion execution / recovery | Our method significantly outperforms the other online approach Spann3R [101], and achieves comparable or sometimes better results than the top optimization-based method, ... | p. 7 (4.3. 3D Reconstruction), p. 6 (4.1. Monocular and Video Depth Estimation) |

## Failure and Ablation Link

- **p. 5 / 4.1. Monocular and Video Depth Estimation - extractive body cue:** For metric pointmap methods like ours and MASt3R, we also report results without alignment.
- **p. 6 / 4.1. Monocular and Video Depth Estimation - extractive body cue:** We report scale-invariant depth and metric depth accuracy on Sintel, Bonn, and KITTI datasets.
- **p. 6 / 4.2. Camera Pose Estimation - extractive body cue:** For the online category, we additionally include DUSt3R [107] where we align all video frames with first frame, without using GA.
- **p. 7 / 4.4. Analysis - extractive body cue:** Our model continuously updates its state representation as new data arrives, relying solely on past and current observations without knowledge of future inputs.
- **p. 8 / 4.4. Analysis - extractive body cue:** To the best of our knowledge, our method is the first to enable the inference of unseen structures in metric scale for general scenes, supporting ...
- **p. 7 / 4.4. Analysis - extractive body cue:** 4.3, we introduce an additional version of our approach called "revisiting": we first run our method online to obtain the final state that has seen ...
- **p. 6 / 4.2. Camera Pose Estimation - extractive body cue:** Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.4. Training Strategy), p. 4 (3.2. Querying the State with Unseen Views), p. 3 (3. Method), p. 3 (3.1. State-Input Interaction Mechanism), p. 4 (3.2. Querying the State with Unseen Views), p. 5 (3.4. Training Strategy), objective p. 5 (3.4. Training Strategy), p. 5 (3.3. Training Objective), p. 3 (3.1. State-Input Interaction Mechanism), p. 3 (3. Method), p. 4 (3.3. Training Objective), p. 4 (3.2. Querying the State with Unseen Views), temporal p. 4 (3.1. State-Input Interaction Mechanism), p. 5 (4.1. Monocular and Video Depth Estimation), p. 5 (4. Experiments), p. 6 (4.2. Camera Pose Estimation), p. 6 (4.1. Monocular and Video Depth Estimation), p. 7 (4.3. 3D Reconstruction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
