# Insights — Where2Act: From Pixels to Actions for Articulated 3D Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2101.02692; PDF retrieval source: https://arxiv.org/pdf/2101.02692. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...
- **p. 2 / 1. Introduction - extractive body cue:** We empirically show that our method successfully learns to predict possible actions for novel objects, and does so even for previously unseen categories.
- **p. 3 / 4. Method - extractive body cue:** We propose a learning-from-interaction approach to tackle this task.
- **p. 3 / 4.1. Network Modules - extractive body cue:** To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) an ...
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** Instead, we propose to let the agent learn by interacting with objects in simulation.
- **p. 3 / 4.1. Network Modules - extractive body cue:** For the 3D experiments, we use PointNet++ segmentation network [34] and implementation [47] with 4 set abstraction layers with single-scale grouping for the encoder and ...
- **p. 4 / 4.3. Training and Losses - extractive body cue:** We empirically find it beneficial to first train the action scoring module Ds and then train the three decoders jointly.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Method), p. 3 (4.1. Network Modules), p. 4 (4.2. Collecting Training Data), p. 3 (4.1. Network Modules)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** We therefore limit our work to considering the plausible short-term interactions that an agent can perform given the current state of the object.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...
- **p. 3 / 3. Problem Statement - extractive body cue:** We formulate a new challenging problem Where2Act - inferring per-pixel ‘actionable information' for manipulating 3D articulated objects.
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. We visualize (a) the actionability scoring and (b) the action proposal predictions on an example cabinet with a door that can be slipped ...
- **p. 8 / 6. Conclusion - extractive body cue:** Finally, our method does not explicitly model the part segmentation and part motion axis, which may be incorporated in the future works to further improve ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic manipulation ...
- **Boundary to test:** Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard for robot to figure out. For the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; • we propose an approach that can ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | We observe that 3D-ours achieves the best performance. validates that our network learns geometric features more than local normals and curvatures. | p. 7 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines) |
| Failure/limitation | Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard for robot to figure out. For the ... | p. 12 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Taking as input a single RGB image or a partial 3D point cloud, we employ an encoder-decoder backbone to extract per-pixel features and design three decoding branches to predict the 'actionable information'.를 Given as input an articulated 3D object, we learn to propose the actionable information for different robotic manipulation primitives (e.g. pushing, pulling): (a) the predicted actionability scores over pixels; (b) the proposed ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard for robot to figure out. For the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; • we propose an approach that can ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, 3D Vision, affordance, articulated objects, active perception, point cloud`.
- **Reading predecessor in the generated track queue:** DUSt3R: Geometric 3D Vision Made Easy (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard for robot to figure out. For the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Equipped with a large-scale PartNetMobility dataset, SAPIEN [49] provides a physics-rich simulation environment that supports robot actuators interacting with 2,346 3D CAD models from 46 object categories..
3. Compare against the body-reported baseline or a matched simpler baseline: We propose two quantitative metrics for evaluating performance of our proposed method, compared with three baseline methods and one ablated version of our method..
4. Report the body metric and its denominator/aggregation: Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic manipulation primitives (e.g. pushing, pulling): (a) the predicted ....
5. Re-run the body-reported ablation/failure condition: To validate the effectiveness of the proposed method and provide benchmarks for the proposed task, we compare to three baseline methods and one ablated version of our method: • B-Random: a random ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (4.1. Network Modules), p. 3 (4.1. Network Modules), p. 4 (4.3. Training and Losses); the primary result is directionally consistent at p. 7 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines), p. 1 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, formulate mechanism이 We propose two quantitative metrics for evaluating performance of our proposed method, compared with three baseline ... 대비 Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose ...을 개선하고, Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
