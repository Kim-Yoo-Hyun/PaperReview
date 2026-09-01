# Insights — RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (71 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OGxalNUHbJ; PDF retrieval source: https://openreview.net/pdf/81387e1e7f5169279b63c293ca88b1e4a8bc7e35.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions ...
- **p. 2 / 1 Introduction - extractive body cue:** To advance spatial referring, we introduce RefSpatial, a large-scale dataset of 2.5M high-quality examples with 20M QA pairs (2× prior [3]).
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose RoboRefer, a 3D-aware VLM that not only acquires precise spatial understanding via SFT but also exhibits generalized strong reasoning capabilities ...
- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.
- **p. 4 / 3 Method - extractive body cue:** To address this, we propose a simple yet effective approach: a dedicated depth encoder and projector, initialized from their RGB counterparts.
- **p. 3 / 3 Method - extractive body cue:** Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec.
- **p. 4 / 3 Method - extractive body cue:** 2, RoboRefer employs separate RGB and depth encoders to extract features, which are then aligned via projectors with the LLM for VQA or point prediction.
- **Contribution anchor:** p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Method), p. 3 (3 Method)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Thus, this work attempts to address this gap by integrating both levels for comprehensive spatial referring.
- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.
- **p. 3 / 1 Introduction - extractive body cue:** (2) We construct RefSpatial, a well-annotated dataset tailored for spatial referring, facilitating both SFT and RFT training, and introduce RefSpatial-Bench, a benchmark that fills the ...
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, current VLMs depend heavily on supervised fine-tuning (SFT) for implicit reasoning, risking memorizing answers over explicit reasoning and thereby hindering generalization and accuracy in ...
- **p. 52 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion ...
- **p. 21 / B.3.5 Question-Answer Pair Generation - extractive body cue:** 53 F More Demonstrations 54 G More Discussion on Limitations and Future Work 54 H Broader Impacts 54 I Licenses 54
- **p. 54 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** G More Discussion on Limitations and Future Work Despite achieving promising results, our model still has limitations.
- **Boundary to test:** Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion planning errors such as IK failures or ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions to achieve spatial referring. | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | By using a single target point predicted by RoboRefer, the system can generate more accurate masks and corresponding grasp poses than those from 2D boxes under occlusion in cluttered scenes, yielding a ... | p. 9 (4 Experiments), p. 8 (Figure/Table caption) |
| Failure/limitation | Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion planning errors such as IK failures or ... | p. 52 (C Implementation Details and Samples of RefSpatial-Bench), p. 21 (B.3.5 Question-Answer Pair Generation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 D.4.1 Sampling Action Groups Given an input state s = (O, Q), where O denotes the visual encoding of the RGB or RGB-D observation and Q the textual encoding of the question, ...를 3.1 Problem Formulation We formulate spatial referring as predicting a single 2D point (x, y) in image space to specify a target location or destination, given visual inputs O (e.g., RGB or ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion planning errors such as IK failures or ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions to achieve spatial referring.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion planning errors such as IK failures or ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To evaluate more complex multi-step spatial referring, we propose RefSpatial-Bench, a challenging benchmark based on real-world cluttered scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: 2, the 2B-RFT variant outperforms all baselines, exceeding the prior SOTA (Gemini-2.5-Pro [9]) by 17.4% (absolute) on RefSpatial-Bench..
4. Report the body metric and its denominator/aggregation: Method CV-Bench [15] BLINKval [16] RoboSpatial [2] SAT [4] EmbSpatial [22] 2D-Relation 3D-Depth 3D-Distance 2D-Relation 3D-Depth Qwen-2.5-VL-7B (base) 82.15 60.17 69.00 64.34 60.98 49.59 30.00 40.20 Qwen-2.5-VL-7B (finetuned) 95.85 95.0 ....
5. Re-run the body-reported ablation/failure condition: To assess this, we fine-tune NVILA-2B [38] on RefSpatial without the depth encoder, followed by continued RFT..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method); the primary result is directionally consistent at p. 9 (4 Experiments), p. 8 (Figure/Table caption), p. 9 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 2, the 2B-RFT variant outperforms all baselines, exceeding the prior SOTA (Gemini-2.5-Pro [9]) by 17.4% (absolute) ... 대비 Method CV-Bench [15] BLINKval [16] RoboSpatial [2] SAT [4] EmbSpatial [22] 2D-Relation 3D-Depth 3D-Distance 2D-Relation 3D-Depth Qwen-2.5-VL-7B (base) ...을 개선하고, Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
