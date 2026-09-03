# ZeroKey: Point-Level Reasoning and Zero-Shot 3D Keypoint Detection from Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In general, we can observe an increased level of difficulty when going from complete objects to object parts and, finally, to specific points or small regions.를 문제로 두고, Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot keypoint detection.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose a novel zero-shot approach for keypoint detection on 3D shapes.
- **p. 1 / Abstract - extractive body cue:** Point-level reasoning on visual data is challenging as it requires precise localization capability, posing problems even for powerful models like DINO or CLIP.
- **p. 1 / Abstract - extractive body cue:** Traditional methods for 3D keypoint detection rely heavily on annotated 3D datasets and extensive supervised training, limiting their scalability and applicability to new categories or ...
- **p. 1 / Abstract - extractive body cue:** In contrast, our method utilizes the rich knowledge embedded within Multi-Modal Large Language Models (MLLMs).
- **p. 1 / Abstract - extractive body cue:** Specifically, we demonstrate, for the first time, that pixel-level annotations used to train recent MLLMs can be exploited for both extracting and naming salient keypoints ...
- **p. 2 / 1. Introduction - extractive body cue:** In general, we can observe an increased level of difficulty when going from complete objects to object parts and, finally, to specific points or small ...
- **p. 2 / 1. Introduction - extractive body cue:** Through this study, we characterize the strengths and limitations of the 3D awareness imparted to models through training with pixel-level annotations.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot keypoint ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we analyze the 3D understanding encoded in Molmo through our method by leveraging Schelling Points and evaluating the describability of keypoints.
- **p. 4 / 4.2. Prompting Molmo to Detect 2D Keypoints - extractive body cue:** The prompt to Molmo consists of the image Vj and the instruction to localize the keypoint ki.
- **p. 7 / Method - extractive body cue:** We then lift these 2D keypoints to 3D using the same backprojection technique described in our method.
- **p. 7 / Method - extractive body cue:** We lift the prediction of this method to 3D using the same lifting procedure used in our method to compare 3D Zero-shot keypoint detection.
- **p. 4 / 4. Method - extractive body cue:** Then, for each candidate, we ask the model to detect the precise coordinates of the point in a given image.
- **p. 4 / 4. Method - extractive body cue:** Our solution comprises three main components: first, we prompt a MLLM with the shape, asking the model to generate a list of names for possible ...
- **p. 7 / Method - extractive body cue:** The main idea is to identify text embeddings that guide the generative model to consistently focus on compact regions within images, which are then used ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It processes both images and text as input and generates text as output. | RGB-D, image set, point cloud, depth와 camera pose | p. 7 (Method), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints) |
| State/latent | processes, images, text, input, generates, output, example, Point, left, wing, image, leverages | geometry, map, object/relationship state | p. 7 (Method), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints) |
| Output/action | For example: "Point to the left wing tip in this image." This leverages Molmo's capability to understand natural language instructions and perform point-level localization. | point map, pose, scene graph, affordance 또는 query result | p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 7 (Method) |
| Objective/outcome | This method learns keypoints by optimizing text embeddings from latent diffusion models. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot keypoint ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we analyze the 3D understanding encoded in Molmo through our method by leveraging Schelling Points and evaluating the describability of keypoints.
- **p. 4 / 4.2. Prompting Molmo to Detect 2D Keypoints - extractive body cue:** The prompt to Molmo consists of the image Vj and the instruction to localize the keypoint ki.
- **p. 7 / Method - extractive body cue:** We then lift these 2D keypoints to 3D using the same backprojection technique described in our method.
- **p. 7 / Method - extractive body cue:** We lift the prediction of this method to 3D using the same lifting procedure used in our method to compare 3D Zero-shot keypoint detection.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Comparison of the performance across different config- urations: (blue) our original method; (red) results with a Global Text prompt; (orange, purple, brown) results ...
- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** Our KeypointNet evaluation shows (see Table.1) that our Zero-Shot method significantly outperforms MLLM-based baselines (PaliGemma 2[45], GPT-4o, CLIP-DINOiser [50]) across all distance thresholds.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to extract ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis) |
| Embodiment/environment | We evaluate our method using the KeypointNet dataset. | hardware/simulator version and reset protocol | p. 6 (6.1. Setup and Dataset), p. 6 (6.1. Setup and Dataset) |
| Dataset/benchmark | Furthermore, our method achieves IoU levels comparable to those of reference-based Few-Shot and fully supervised methods tailored for this dataset, such as B2-3D [49]. | role, split, size and leakage | p. 6 (6.1. Setup and Dataset), p. 6 (6.1. Setup and Dataset), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 8 (6.3. Quantitative and Qualitative Analysis) |
| Metric | [55], which computes the Intersection over Union (IoU) between predicted keypoints and ground-truth keypoints from the KeypointNet dataset, using varying distance thresholds. | definition, denominator, direction and uncertainty | p. 6 (6.1. Setup and Dataset), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Baseline/ablation | Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to extract and name salient keypoints on 3D models. ... | fair input/data/compute/action matching | p. 1 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 7 (6.3. Quantitative and Qualitative Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to ...
- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** Side-by-side comparisons between ground truth keypoints and our Zero-Shot predictions, a figure of GPT-4o fails to precisely locate the keypoint, and a comparison of our ...
- **p. 8 / 7. Conclusion and Future Work - extractive body cue:** Our evaluations demonstrate the efficacy of our approach and suggest that point-level reasoning is an effective way to endow MLLMs with a robust understanding of ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to extract ...
- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** Our KeypointNet evaluation shows (see Table.1) that our Zero-Shot method significantly outperforms MLLM-based baselines (PaliGemma 2[45], GPT-4o, CLIP-DINOiser [50]) across all distance thresholds.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In general, we can observe an increased level of difficulty when going from complete objects to object parts and, finally, to specific points or small regions.를 문제로 두고, Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot keypoint detection.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Motivation), p. 4 (3. Motivation), p. 3 (3. Motivation), p. 4 (4. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
