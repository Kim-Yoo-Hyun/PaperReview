# Insights — SSCNet: Semantic Scene Completion from a Single Depth Image

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1611.08974; PDF retrieval source: https://arxiv.org/pdf/1611.08974. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and semantic ...
- **p. 1 / 1. Introduction - extractive body cue:** Similarly, for a robot, the ability to infer complete 3D shape from partial observations is necessary for low-level tasks such as grasping and obstacle avoidance ...
- **p. 2 / 1. Introduction - extractive body cue:** In support of that goal, we design a dilation-based 3D context module that enables efficient context learning with large receptive fields.
- **p. 5 / 4. Synthesizing training data - extractive body cue:** In this paper, we present a new large-scale synthetic 3D scene dataset, from which we obtain a large amount of training data with synthetically rendered ...
- **p. 5 / 4. Synthesizing training data - extractive body cue:** During the task, we show a set of top view renderings of each floor and ask turkers to vote whether this is a valid apartment ...
- **p. 4 / 3.2. Network architecture - extractive body cue:** Then, we use a dilation-based 3D context module to capture higher-level inter-object contextual information.
- **p. 4 / 3.2. Network architecture - extractive body cue:** Taking a high-resolution 3D volume as input, the network first uses several 3D convolution layers to learn a local geometry representation.
- **Contribution anchor:** p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (4. Synthesizing training data), p. 5 (4. Synthesizing training data), p. 4 (3.2. Network architecture)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, if we consider the context due to surrounding objects, such as the table and floor, the problem is much easier.
- **p. 2 / 1. Introduction - extractive body cue:** First, how do we effectively capture contextual information from 3D volumetric data, where the signal is sparse and lacks high frequency detail?
- **p. 1 / 1. Introduction - extractive body cue:** Prior work is limited to address only part of this problem as shown in FigFigure 1.
- **p. 1 / 1. Introduction - extractive body cue:** Therefore, the two problems of predicting voxel occupancy and identifying object semantics are strongly coupled.
- **p. 7 / 5.1. Experimental results - extractive body cue:** While Firman et al. produces good results for many cases, their approach fails when the scene becomes complex.
- **p. 7 / 5.1. Experimental results - extractive body cue:** For instance, their algorithm fails to complete half of the bed in the first row of Figure 7, and also fails to complete the chairs ...
- **p. 6 / 5.1. Experimental results - extractive body cue:** In contrast, our algorithm is based on only depth and does not use additional mesh model at test time.
- **Boundary to test:** While Firman et al. produces good results for many cases, their approach fails when the scene becomes complex.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and semantic annotations. | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | Increasing the receptive field gives the network a opportunity to capture richer contextual information and significantly improve the network performance from 38.0% to 44.3%. | p. 8 (5.1. Experimental results), p. 8 (5.1. Experimental results) |
| Failure/limitation | While Firman et al. produces good results for many cases, their approach fails when the scene becomes complex. | p. 7 (5.1. Experimental results), p. 7 (5.1. Experimental results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 (a) Input single-view depth map (b) Visible surface from the depth map; color is for visualization only.를 With this motivation, our goal is to have a model that predicts both volumetric occupancy (i.e., scene completion) and object category (i.e., scene labeling) from a single depth image of a 3D ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 While Firman et al. produces good results for many cases, their approach fails when the scene becomes complex.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and semantic annotations.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, semantic, occupancy, geometry`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** While Firman et al. produces good results for many cases, their approach fails when the scene becomes complex.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 4. Comparison of receptive fields and voxel sizes between SSCNet and prior work. (a) Object centric networks such as [34] and [20] scale objects into the same 3D voxel grid thus ....
4. Report the body metric and its denominator/aggregation: We see a performance gain by using additional synthetic data especially for the semantic scene completion task having an 10.3% improvement in IoU..
5. Re-run the body-reported ablation/failure condition: Figure 8. What 3D context does the network learn? The first fig- ure shows the input depth map (a desk) and the following figures show the predictions for other objects. Without observing ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. Network architecture), p. 4 (3.2. Network architecture), p. 5 (3.2. Network architecture); the primary result is directionally consistent at p. 8 (5.1. Experimental results), p. 8 (5.1. Experimental results), p. 6 (5.1. Experimental results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 provide, training, data mechanism이 Figure 4. Comparison of receptive fields and voxel sizes between SSCNet and prior work. (a) Object ... 대비 We see a performance gain by using additional synthetic data especially for the semantic scene completion task having ...을 개선하고, While Firman et al. produces good results for many cases, their approach fails when the scene ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
