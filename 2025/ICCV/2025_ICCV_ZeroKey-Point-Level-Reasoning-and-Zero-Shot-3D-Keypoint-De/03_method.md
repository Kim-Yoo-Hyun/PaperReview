# Method - ZeroKey: Point-Level Reasoning and Zero-Shot 3D Keypoint Detection from Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4. Method), p. 4 (4. Method), p. 7 (Method), p. 7 (Method), p. 5 (4.3. Zero-Shot 3D Keypoint Detection), p. 5 (4.3. Zero-Shot 3D Keypoint Detection)): Then, for each candidate, we ask the model to detect the precise coordinates of the point in a given image.

## Method Body Digest

- **p. 4 / 4. Method - extractive PDF cue:** Then, for each candidate, we ask the model to detect the precise coordinates of the point in a given image.
- **p. 4 / 4. Method - extractive PDF cue:** Our solution comprises three main components: first, we prompt a MLLM with the shape, asking the model to generate a list of names for possible ...
- **p. 7 / Method - extractive PDF cue:** The main idea is to identify text embeddings that guide the generative model to consistently focus on compact regions within images, which are then used ...
- **p. 7 / Method - extractive PDF cue:** This method learns keypoints by optimizing text embeddings from latent diffusion models.
- **p. 5 / 4.3. Zero-Shot 3D Keypoint Detection - extractive PDF cue:** One can also extract the confidence weighting from Molmo's feature map and apply it to the predictions.
- **p. 5 / 4.3. Zero-Shot 3D Keypoint Detection - extractive PDF cue:** Assuming a pinhole camera model, each camera projection matrix Cj maps 3D points P ∈R3 to 2D points p ∈R2: \m a thbf {p } ...
- **p. 7 / Method - extractive PDF cue:** It processes both images and text as input and generates text as output.
- **p. 4 / 4.2. Prompting Molmo to Detect 2D Keypoints - extractive PDF cue:** For example: "Point to the left wing tip in this image." This leverages Molmo's capability to understand natural language instructions and perform point-level localization.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot keypoint ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Furthermore, we analyze the 3D understanding encoded in Molmo through our method by leveraging Schelling Points and evaluating the describability of keypoints.
- **p. 4 / 4.2. Prompting Molmo to Detect 2D Keypoints - extractive PDF cue:** The prompt to Molmo consists of the image Vj and the instruction to localize the keypoint ki.

## Source Evidence Cues

- **p. 4 / 4. Method - extractive PDF cue:** Then, for each candidate, we ask the model to detect the precise coordinates of the point in a given image.
- **p. 4 / 4. Method - extractive PDF cue:** Our solution comprises three main components: first, we prompt a MLLM with the shape, asking the model to generate a list of names for possible ...
- **p. 7 / Method - extractive PDF cue:** The main idea is to identify text embeddings that guide the generative model to consistently focus on compact regions within images, which are then used ...
- **p. 7 / Method - extractive PDF cue:** This method learns keypoints by optimizing text embeddings from latent diffusion models.
- **p. 5 / 4.3. Zero-Shot 3D Keypoint Detection - extractive PDF cue:** One can also extract the confidence weighting from Molmo's feature map and apply it to the predictions.
- **p. 5 / 4.3. Zero-Shot 3D Keypoint Detection - extractive PDF cue:** Assuming a pinhole camera model, each camera projection matrix Cj maps 3D points P ∈R3 to 2D points p ∈R2: \m a thbf {p } ...
- **Detected method headings:** 2.1. Multimodal Large Language Models (p. 2); 4. Method (p. 4); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, for each candidate, we ask the model to detect the precise coordinates of the point in a given image. | p. 4 (4. Method), p. 4 (4. Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Our solution comprises three main components: first, we prompt a MLLM with the shape, asking the model to generate a list of ... | p. 4 (4. Method), p. 7 (Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The main idea is to identify text embeddings that guide the generative model to consistently focus on compact regions within images, which ... | p. 7 (Method), p. 7 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / Method - extractive PDF cue:** This method learns keypoints by optimizing text embeddings from latent diffusion models.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.3. Zero-Shot 3D Keypoint Detection).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | processes, images, text, input, generates, output, example, Point, left, wing, image, leverages, Molmo, capability | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | processes, images, text, input, generates, output, example, Point, left, wing | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Inspired, recent, developments, investigating, MLLMs, endowed, point-level, reasoning, context, shape | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | learns, keypoints, optimizing, text, embeddings, latent, diffusion, models | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / Method - extractive PDF cue:** It processes both images and text as input and generates text as output.
- **p. 4 / 4.2. Prompting Molmo to Detect 2D Keypoints - extractive PDF cue:** For example: "Point to the left wing tip in this image." This leverages Molmo's capability to understand natural language instructions and perform point-level localization.
- **p. 4 / 4.2. Prompting Molmo to Detect 2D Keypoints - extractive PDF cue:** To detect the precise 2D coordinates of each candidate keypoint, we utilize Molmo [12], a state-of-the-art MLLM capable of localizing points in images based on ...
- **p. 7 / Method - extractive PDF cue:** Given an image and a text prompt, PaliGemma outputs a segmentation mask around the relevant region.
- **p. 2 / 1. Introduction - extractive PDF cue:** This type of reasoning focuses on understanding and interpreting visual input at a fine-grained level using text.
- **p. 5 / 4.3. Zero-Shot 3D Keypoint Detection - extractive PDF cue:** Subsequently, we apply hierarchical densitybased spatial clustering to this aggregated point cloud.
- **p. 5 / 4.3. Zero-Shot 3D Keypoint Detection - extractive PDF cue:** We aggregate all the points into a single point cloud, which contains an unknown number of key points.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For example, for the class "airplane," the MLLM might generate keypoint names such as "nose," "wing tip," and "tail." In our experiments, ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | VointNet [15] operates within the Voint cloud framework, retaining the original point cloud's compactness and descriptive 3D properties. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, candidate, model, detect, precise, coordinates, point, given, image, solution, comprises, three, main, components, first, prompt, MLLM, shape, asking, generate.
- **Relevant PDF headings:** 2.1. Multimodal Large Language Models (p. 2); 4. Method (p. 4); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate our method using the KeypointNet dataset. | p. 6 (6.1. Setup and Dataset), p. 6 (6.1. Setup and Dataset) |
| Semantic / temporal fusion | Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within ... | p. 1 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis) |
| Robot query / planning handoff | Figure 7. Comparison of the performance across different config- urations: (blue) our original method; (red) results with a Global Text prompt; (orange, ... | p. 8 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis) |

## Failure and Ablation Link

- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive PDF cue:** This provides strong evidence for our claim that the pixel-level annotations used to train MLLMs can be leveraged to both extract and name salient keypoints ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to extract ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 7. Comparison of the performance across different config- urations: (blue) our original method; (red) results with a Global Text prompt; (orange, purple, brown) results ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to ...
- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive PDF cue:** Side-by-side comparisons between ground truth keypoints and our Zero-Shot predictions, a figure of GPT-4o fails to precisely locate the keypoint, and a comparison of our ...
- **p. 8 / 7. Conclusion and Future Work - extractive PDF cue:** Our evaluations demonstrate the efficacy of our approach and suggest that point-level reasoning is an effective way to endow MLLMs with a robust understanding of ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to extract ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4. Method), p. 4 (4. Method), p. 7 (Method), p. 7 (Method), p. 5 (4.3. Zero-Shot 3D Keypoint Detection), p. 5 (4.3. Zero-Shot 3D Keypoint Detection), objective p. 7 (Method), temporal p. 4 (4.1. Generating Text Candidates for Salient Points), p. 3 (2.3. Lifting from 2D to 3D).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
