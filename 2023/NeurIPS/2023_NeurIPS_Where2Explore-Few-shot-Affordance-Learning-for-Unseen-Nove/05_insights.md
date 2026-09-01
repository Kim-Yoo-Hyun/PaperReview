# Insights — Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.07473; PDF retrieval source: https://arxiv.org/pdf/2309.07473. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our framework by training our model on constrained object categories and applying few-shot learning to novel categories with limited shapes.
- **p. 5 / 4 Method - extractive body cue:** As shown in the right part of figure 2, when faced with a novel category, our framework will first predict the similarity of the objects.
- **p. 3 / 4 Method - extractive body cue:** Next, we introduce the ‘similarity module' to form a representation that connects the geometries in the supporting set with geometries across category boundaries.
- **p. 3 / 4 Method - extractive body cue:** As shown in Figure 2, we propose the ‘Where2Explore' framework to explicitly leverage the similar semantics on local geometries shared across different categories for cross-category ...
- **p. 6 / 4 Method - extractive body cue:** 4.4 Network Architecture and Training Strategy Our network consists of two modules - the affordance module and the similarity module.
- **p. 6 / 4 Method - extractive body cue:** We use a PointNet++ segmentation network [29] encoder for extracting features from 3D partial point clouds.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (4 Method), p. 3 (4 Method), p. 3 (4 Method), p. 6 (4 Method)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** This limitation hinders the efficiency and safety of real-world applications of robots.
- **p. 1 / 1 Introduction - extractive body cue:** However, due to the significant variance in the objects' structure, 3D geometry, and articulation types across categories, developing efficient perception and manipulation systems that can ...
- **p. 2 / 1 Introduction - extractive body cue:** Considering the substantial semantic and geometric gap between known shapes and novel categories, forming an efficient exploration strategy for out-of-distribution objects is challenging.
- **p. 2 / 1 Introduction - extractive body cue:** Via fine-tuning our network with the interactions on novel objects, the model could generalize to unseen objects within this novel category (Bottom Right).
- **p. 3 / 1 Introduction - extractive body cue:** • Exploring the challenging task of cross-category few-shot learning for articulated object manipulation, requiring the model to capture fine-grained geometric information from an entirely new ...
- **p. 8 / 5 Experiments - extractive body cue:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.
- **p. 9 / 5 Experiments - extractive body cue:** Although Affordance fails to directly generalize to novel categories (Left) via interacting on low-similarity areas (Middle), our framework could learn the semantic information on them ...
- **Boundary to test:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | For both the F-score and sample success rate, we use the average score of the four different training category combinations. | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Failure/limitation | Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity. | p. 8 (5 Experiments), p. 9 (5 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 The similarity module is designed to take a partial point cloud of an object Oi ∈R3×N, a set of action directions and gripper orientations {Ri} on each point, and is required to ...를 Given a specific action Ri on a point pi of a partial point cloud Oi, the affordance module is required to predict whether the given action will result in a part motion.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, 3D Vision, active exploration, affordance, articulated objects, few-shot learning`.
- **Reading predecessor in the generated track queue:** Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Clio: Real-time Task-Driven Open-Set 3D Scene Graphs (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Similarity-guided Exploration 1 Part motion Franka Emika Panda Robot Similarity prediction Azure Kinect DK 2 No part motion 3 Fail to grasp Manipulation After Exploration Similarity prediction Adapted affordance Pulling Part motion ....
3. Compare against the body-reported baseline or a matched simpler baseline: Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately to match the real-world scenario. Table 2 presents ....
4. Report the body metric and its denominator/aggregation: For both the F-score and sample success rate, we use the average score of the four different training category combinations..
5. Re-run the body-reported ablation/failure condition: Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately to match the real-world scenario. Table 2 presents ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (4 Method), p. 6 (4 Method), p. 4 (4 Method); the primary result is directionally consistent at p. 7 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 demonstrate, framework, capability mechanism이 Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also ... 대비 For both the F-score and sample success rate, we use the average score of the four different training ...을 개선하고, Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
