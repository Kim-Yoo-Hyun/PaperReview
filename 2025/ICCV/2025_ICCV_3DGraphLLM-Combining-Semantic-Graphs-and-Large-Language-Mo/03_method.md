# Method - 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Model Architecture), p. 4 (3.1. Model Architecture), p. 3 (3.1. Model Architecture), p. 3 (3.1. Model Architecture), p. 5 (3.3. Training Strategy), p. 5 (3.3. Training Strategy)): To adapt the extracted features for the language model, we use three trainable projection modules: the 2D Object Projection f2d(·), which maps the 2D image features of objects, the 3D ...

## Method Body Digest

- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** To adapt the extracted features for the language model, we use three trainable projection modules: the 2D Object Projection f2d(·), which maps the 2D image ...
- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** Therefore, we use latent features to capture possible combinations of these semantic relationships.
- **p. 3 / 3.1. Model Architecture - extractive PDF cue:** These learned identifiers, with the features from object subgraphs composed of nearest neighbors for each object, are used to create a flat representation of the ...
- **p. 3 / 3.1. Model Architecture - extractive PDF cue:** The model architecture includes pre-trained encoders for 2D images, 3D point clouds, and point clouds semantic relationships, alongside a pre-trained LLM.
- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** We use the semantic relationships encoder [52] pretrained using ground-truth (GT) point cloud scene segmentation data.
- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** We use the following loss function: L(θ) = - ℓ X i=1 log P(sres i /sres [1,...,i-1], sprefix), (2) where ℓis the length of the ...
- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** During training, we aim to optimize the trainable parameters θ of both the language model and the projection layers to minimize the negative log-likelihood of ...
- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** One of its key advantages is that it only requires 3D point cloud coordinates as input during prediction while leveraging knowledge transfer from the pretrained ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, our contributions are as follows: • We introduce 3DGraphLLM, the first method for creating a learnable 3D scene graph representation specifically designed for ...
- **p. 2 / 1. Introduction - extractive PDF cue:** It enables semantic relationships between objects in a scene to be mapped directly into the LLM's token embedding space. • We propose an algorithm that ...
- **p. 3 / 3.1. Model Architecture - extractive PDF cue:** Thus, the set V of vertices of the graph consists of n point clouds {Pi}n i=1, where Pi ∈Rmi×6.

## Source Evidence Cues

- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** To adapt the extracted features for the language model, we use three trainable projection modules: the 2D Object Projection f2d(·), which maps the 2D image ...
- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** Therefore, we use latent features to capture possible combinations of these semantic relationships.
- **p. 3 / 3.1. Model Architecture - extractive PDF cue:** These learned identifiers, with the features from object subgraphs composed of nearest neighbors for each object, are used to create a flat representation of the ...
- **p. 3 / 3.1. Model Architecture - extractive PDF cue:** The model architecture includes pre-trained encoders for 2D images, 3D point clouds, and point clouds semantic relationships, alongside a pre-trained LLM.
- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** We use the semantic relationships encoder [52] pretrained using ground-truth (GT) point cloud scene segmentation data.
- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** We use the following loss function: L(θ) = - ℓ X i=1 log P(sres i /sres [1,...,i-1], sprefix), (2) where ℓis the length of the ...
- **Detected method headings:** 3. Method (p. 3); 3.1. Model Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To adapt the extracted features for the language model, we use three trainable projection modules: the 2D Object Projection f2d(·), which maps ... | p. 4 (3.1. Model Architecture), p. 4 (3.1. Model Architecture) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Therefore, we use latent features to capture possible combinations of these semantic relationships. | p. 4 (3.1. Model Architecture), p. 3 (3.1. Model Architecture) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | These learned identifiers, with the features from object subgraphs composed of nearest neighbors for each object, are used to create a flat ... | p. 3 (3.1. Model Architecture), p. 3 (3.1. Model Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** During training, we aim to optimize the trainable parameters θ of both the language model and the projection layers to minimize the negative log-likelihood of ...
- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** We use the following loss function: L(θ) = - ℓ X i=1 log P(sres i /sres [1,...,i-1], sprefix), (2) where ℓis the length of the ...
- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** One of its key advantages is that it only requires 3D point cloud coordinates as input during prediction while leveraging knowledge transfer from the pretrained ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.3. Training Strategy).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | uses, point, clouds, scene, objects, input, obtained, either, ground-truth, annotations, through, state-of-the-art, cloud, instance | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | uses, point, clouds, scene, objects, input, obtained, either, ground-truth, annotations | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summarize, contributions, follows, introduce, DGraphLLM, first, creating, learnable, scene, graph | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | During, training, optimize, trainable, parameters, language, model, projection, layers, minimize | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive PDF cue:** Our approach uses a set of point clouds of scene objects as input.
- **p. 3 / 3. Method - extractive PDF cue:** The objects' point clouds can be obtained either from ground-truth annotations or through state-of-the-art point cloud instance segmentation methods.
- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** One of its key advantages is that it only requires 3D point cloud coordinates as input during prediction while leveraging knowledge transfer from the pretrained ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The proposed 3DGraphLLM approach leverages 3D semantic scene graph learnable representation supplied as input to an LLM to perform various 3D vision-language tasks.
- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** To adapt the extracted features for the language model, we use three trainable projection modules: the 2D Object Projection f2d(·), which maps the 2D image ...
- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** This adaptation of the tasks is designed for user-assistant interactions, as proposed by the authors of Chat-Scene.
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we introduce 3DGraphLLM, a novel learnable representation of a 3D scene graph designed for use as input to an LLM (see Fig.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | To convert the scene graph into a token sequence, we represent each object by an identifier, its 2D object feature, and a ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Such a graph contains n · (n -1) edges between objects, and using the complete graph as a sequence for the LLM ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | We vary the number of nearest neighbors in powers of two, capping it at 4 due to GPU memory constraints during training. | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | We use a batch size of 8 and train 3DGraphLLM for 3 epochs with an initial learning rate of 5 · 10-6, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** To adapt the extracted features for the language model, we use three trainable projection modules: the 2D Object Projection f2d(·), which maps the 2D image ...
- **p. 3 / 3.1. Model Architecture - extractive PDF cue:** The model architecture includes pre-trained encoders for 2D images, 3D point clouds, and point clouds semantic relationships, alongside a pre-trained LLM.
- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** We use the semantic relationships encoder [52] pretrained using ground-truth (GT) point cloud scene segmentation data.
- **p. 6 / 4. Experiments - extractive PDF cue:** We use a batch size of 8 and train 3DGraphLLM for 3 epochs with an initial learning rate of 5 · 10-6, following a cosine ...
- **p. 8 / 4.2. Ablation Studies - extractive PDF cue:** 4, increasing the number of nearest neighbors enhances visual grounding quality with a slight increase in inference time.
- **p. 5 / 3.3. Training Strategy - extractive PDF cue:** We use the semantic relationships encoder [52] pretrained using ground-truth (GT) point cloud scene segmentation data.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** adapt, extracted, features, language, model, three, trainable, projection, modules, Object, maps, image, objects, point, cloud, Semantic, Relation, relationships, between, Therefore.
- **Relevant PDF headings:** 3. Method (p. 3); 3.1. Model Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | For 3RScan scenes, we use data from the RioRefer dataset [36] for object grounding, and the 3RQA dataset [26] for question answering. | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Global / local decision | 2, our method significantly outperforms the baseline approach Chat-Scene [25] on the two ScanNet 3D referred object grounding benchmarks, ScanRefer [5] and ... | p. 6 (4.1. Experimental Results), p. 6 (4.1. Experimental Results) |
| Motion execution / recovery | 4, incorporating a scene graph representation significantly improves the performance of the LLMs across all three 3D Vision-Language tasks: visual grounding, scene ... | p. 7 (4.2. Ablation Studies), p. 6 (4.1. Experimental Results) |

## Failure and Ablation Link

- **p. 6 / 4. Experiments - extractive PDF cue:** In our experiments, we use LLAMA3-8BInstruct [2], a state-of-the-art large language model, as well as Vicuna-1.5-7B [62] for ablation.
- **p. 7 / 4.1. Experimental Results - extractive PDF cue:** Ablation study on semantic edges role and training pipeline.
- **p. 8 / 4.2. Ablation Studies - extractive PDF cue:** Ablation study on subgraph representation.
- **p. 8 / 4.2. Ablation Studies - extractive PDF cue:** Ablation study on semantic edges role depending on quality of instance segmentation.
- **p. 5 / 4. Experiments - extractive PDF cue:** For pretraining 3DGraphLLM using GT instance segmentation, we employ a combined 3D VisionLanguage dataset for ScanNet [11] and 3RScan [50] scenes.
- **p. 5 / 4. Experiments - extractive PDF cue:** To assess 3DGraphLLM performance under realistic conditions, we perform fine-tuning on predicted instance segmentation using 3D vision-language benchmarks 8889
- **p. 6 / 4. Experiments - extractive PDF cue:** For fine-tuning the language model, we apply LoRA [23] with a rank of 16.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1. Model Architecture), p. 4 (3.1. Model Architecture), p. 3 (3.1. Model Architecture), p. 3 (3.1. Model Architecture), p. 5 (3.3. Training Strategy), p. 5 (3.3. Training Strategy), objective p. 5 (3.3. Training Strategy), p. 5 (3.3. Training Strategy), p. 4 (3.1. Model Architecture), temporal p. 3 (3. Method), p. 4 (3.2. Flat Graph Representation), p. 7 (4.2. Ablation Studies), p. 8 (4.2. Ablation Studies), p. 8 (4.2. Ablation Studies), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
