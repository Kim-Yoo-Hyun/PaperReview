# Insights — SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model.
- **p. 2 / 1. Introduction - extractive body cue:** Third, we present the first comprehensive search over the LMM design space for spatial reasoning tasks and propose a roadmap towards developing state-of-the-art models in ...
- **p. 3 / 3. Methods - extractive body cue:** We present the task of reasoning 3D spatial relationships and explain the challenges LMMs face when answering these questions in Sec.
- **p. 3 / 3.1. Preliminary of LMMs - extractive body cue:** A standard LMM [39, 41] consists of a visual encoder to process the image, a multimodal connector to transform the visual feature to visual token, ...
- **p. 5 / 3.3.1. Design space - extractive body cue:** 3.2.1, we propose new training setups that aim to improve 3D awareness and advance the 3D spatial reasoning capabilities.
- **p. 5 / 3.3.1. Design space - extractive body cue:** We introduce the design space considered in our work, i.e., choices of training data, model architecture, and training setup that advance the 3D spatial reasoning ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive body cue:** This step enables the model to learn rich visual features solely from visual signals. • Noisy image-text pairs: Large-scale image-text pairs [20, 37, 52] are ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methods), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space), p. 5 (3.3.1. Design space)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, a significant gap remains: previous works [2, 14, 16] have primarily focused on 3D distance relationships, overlooking the crucial role of 3D object orientation.
- **p. 1 / 1. Introduction - extractive body cue:** Collecting a small set of high-quality 3D-aware data to tackle the first challenge is feasible, albeit labor-intensive, using readily available tools.
- **p. 2 / 1. Introduction - extractive body cue:** This limitation suggests that a more holistic approach is necessary.
- **p. 2 / 1. Introduction - extractive body cue:** Addressing this gap, we aim to incorporate 3D orientation relationships-converted from ImageNet3D [17]-into our data engine, making us the first to enable complex spatial reasoning ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive body cue:** Prior works [39, 41, 46, 58] repurpose VQA benchmarks [22, 32] into instruction-tuning datasets.
- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive body cue:** Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different levels of 3D awareness and cannot be ...
- **p. 7 / 4.2. Results - extractive body cue:** Interestingly, although SpatialVLM [14] (implemented in SpaceLLaVA [2]) outperforms other open-source models in overall performance, it falls short in 3D orientation reasoning compared to LLaVA, ...
- **Boundary to test:** Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different levels of 3D awareness and cannot be answered from 2D spatial reasoning only.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary model by 8.7% and the best open-source model by 10.5%. | p. 7 (4.2. Results), p. 7 (4.2. Results) |
| Failure/limitation | Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different levels of 3D awareness and cannot be answered from 2D spatial reasoning only. | p. 4 (3.2.2. SpatialVQA for Evaluation), p. 7 (4.2. Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Existing pretraining and visual instruction tuning data for LMMs [41, 58] focused on detailed descriptions and conversations about scenes, appearances, and actions, while being vague about the 3D spatial relationships that build ...를 At this stage, the model is trained to describe images in details to align visual and language representations in the same space. • Visual instruction tuning.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different levels of 3D awareness and cannot be answered from 2D spatial reasoning only.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `LLM, spatial reasoning, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different levels of 3D awareness and cannot be answered from 2D spatial reasoning only.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We build our SpatialVQA on images from Omni3D [11], with 3D bounding box annotations on diverse objects from both urban [12, 21] and indoor scenes [9, 50, 54]..
3. Compare against the body-reported baseline or a matched simpler baseline: Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary model by 8.7% and the best open-source model by 10.5%..
4. Report the body metric and its denominator/aggregation: We follow [16, 58] and develop rule-based methods to generate visual question-answer pairs from the 3D groundtruths..
5. Re-run the body-reported ablation/failure condition: Table 2. Thorough exploration of the design space and roadmap progression. We systematically examine the 3D-informed design space from the aspects of data, architecture and training. The non-gray rows, listed from top ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.3.1. Design space), p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs); the primary result is directionally consistent at p. 7 (4.2. Results), p. 7 (4.2. Results), p. 6 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Second, novel, compound mechanism이 Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance ... 대비 We follow [16, 58] and develop rule-based methods to generate visual question-answer pairs from the 3D groundtruths.을 개선하고, Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
