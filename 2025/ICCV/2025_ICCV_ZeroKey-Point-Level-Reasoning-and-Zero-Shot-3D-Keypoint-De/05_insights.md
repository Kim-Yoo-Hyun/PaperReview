# Insights — ZeroKey: Point-Level Reasoning and Zero-Shot 3D Keypoint Detection from Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot keypoint ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we analyze the 3D understanding encoded in Molmo through our method by leveraging Schelling Points and evaluating the describability of keypoints.
- **p. 4 / 4.2. Prompting Molmo to Detect 2D Keypoints - extractive body cue:** The prompt to Molmo consists of the image Vj and the instruction to localize the keypoint ki.
- **p. 7 / Method - extractive body cue:** We then lift these 2D keypoints to 3D using the same backprojection technique described in our method.
- **p. 7 / Method - extractive body cue:** We lift the prediction of this method to 3D using the same lifting procedure used in our method to compare 3D Zero-shot keypoint detection.
- **p. 4 / 4. Method - extractive body cue:** Then, for each candidate, we ask the model to detect the precise coordinates of the point in a given image.
- **p. 4 / 4. Method - extractive body cue:** Our solution comprises three main components: first, we prompt a MLLM with the shape, asking the model to generate a list of names for possible ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 7 (Method), p. 7 (Method), p. 4 (4. Method)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** In general, we can observe an increased level of difficulty when going from complete objects to object parts and, finally, to specific points or small ...
- **p. 2 / 1. Introduction - extractive body cue:** Through this study, we characterize the strengths and limitations of the 3D awareness imparted to models through training with pixel-level annotations.
- **p. 4 / 3. Motivation - extractive body cue:** Furthermore, the recent MLLMs that incorporate 3D data [18, 51, 58] are typically trained with explicit alignment against pre-trained traditional vision-language models, and thus inherit ...
- **p. 4 / 3. Motivation - extractive body cue:** Existing methods for the 3D keypoint detection problem typically formulate the problem as either a supervised learning task, by exploiting the ground truth annotations, e.g., ...
- **p. 3 / 3. Motivation - extractive body cue:** Localization and naming of points in an image or a 3D shape is an extremely challenging problem.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to ...
- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** Side-by-side comparisons between ground truth keypoints and our Zero-Shot predictions, a figure of GPT-4o fails to precisely locate the keypoint, and a comparison of our ...
- **Boundary to test:** Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to the text prompt. In contrast, our method ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot keypoint detection. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Figure 7. Comparison of the performance across different config- urations: (blue) our original method; (red) results with a Global Text prompt; (orange, purple, brown) results using different ren- dering; (green) results without ... | p. 8 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis) |
| Failure/limitation | Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to the text prompt. In contrast, our method ... | p. 8 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 It processes both images and text as input and generates text as output.를 For example: "Point to the left wing tip in this image." This leverages Molmo's capability to understand natural language instructions and perform point-level localization.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to the text prompt. In contrast, our method ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot keypoint detection.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to the text prompt. In contrast, our method ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We evaluate our method using the KeypointNet dataset..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to extract and name salient keypoints on 3D models. ....
4. Report the body metric and its denominator/aggregation: [55], which computes the Intersection over Union (IoU) between predicted keypoints and ground-truth keypoints from the KeypointNet dataset, using varying distance thresholds..
5. Re-run the body-reported ablation/failure condition: This provides strong evidence for our claim that the pixel-level annotations used to train MLLMs can be leveraged to both extract and name salient keypoints on 3D models without requiring any ground ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4. Method), p. 4 (4. Method), p. 7 (Method); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 1 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Inspired, recent, developments mechanism이 Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method ... 대비 [55], which computes the Intersection over Union (IoU) between predicted keypoints and ground-truth keypoints from the KeypointNet dataset, ...을 개선하고, Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
