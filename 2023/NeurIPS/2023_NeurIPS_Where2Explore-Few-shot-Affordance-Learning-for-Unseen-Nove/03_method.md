# Method - Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.07473; PDF retrieval source: https://arxiv.org/pdf/2309.07473. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (4 Method), p. 6 (4 Method), p. 4 (4 Method), p. 5 (4 Method), p. 3 (4 Method), p. 5 (4 Method)): 4.4 Network Architecture and Training Strategy Our network consists of two modules - the affordance module and the similarity module.

## Method Body Digest

- **p. 6 / 4 Method - extractive body cue:** 4.4 Network Architecture and Training Strategy Our network consists of two modules - the affordance module and the similarity module.
- **p. 6 / 4 Method - extractive body cue:** We use a PointNet++ segmentation network [29] encoder for extracting features from 3D partial point clouds.
- **p. 4 / 4 Method - extractive body cue:** To achieve the first property, as shown in the middle of Figure 3, we propose a ‘similarity module' to predict the semantic similarity.
- **p. 5 / 4 Method - extractive body cue:** Then, by choosing the action with the lowest similarity prediction, the model performs a short-term manipulation trajectory and observes the result of the interaction as ...
- **p. 3 / 4 Method - extractive body cue:** Next, we introduce the ‘similarity module' to form a representation that connects the geometries in the supporting set with geometries across category boundaries.
- **p. 5 / 4 Method - extractive body cue:** We use a similarity module to predict the similarity conditioned on specific actions (Middle).
- **p. 3 / 4 Method - extractive body cue:** Then, to expand the supporting set along the similarity representation we built, we perform few-shot learning on novel categories with the guidance of the similarity ...
- **p. 6 / 4 Method - extractive body cue:** To train the similarity module, we use an L1 loss to measure the distance between Similarity prediction and the ground truth accuracy.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our framework by training our model on constrained object categories and applying few-shot learning to novel categories with limited shapes.
- **p. 5 / 4 Method - extractive body cue:** As shown in the right part of figure 2, when faced with a novel category, our framework will first predict the similarity of the objects.

## Source Evidence Cues

- **p. 6 / 4 Method - extractive body cue:** 4.4 Network Architecture and Training Strategy Our network consists of two modules - the affordance module and the similarity module.
- **p. 6 / 4 Method - extractive body cue:** We use a PointNet++ segmentation network [29] encoder for extracting features from 3D partial point clouds.
- **p. 4 / 4 Method - extractive body cue:** To achieve the first property, as shown in the middle of Figure 3, we propose a ‘similarity module' to predict the semantic similarity.
- **p. 5 / 4 Method - extractive body cue:** Then, by choosing the action with the lowest similarity prediction, the model performs a short-term manipulation trajectory and observes the result of the interaction as ...
- **p. 3 / 4 Method - extractive body cue:** Next, we introduce the ‘similarity module' to form a representation that connects the geometries in the supporting set with geometries across category boundaries.
- **p. 5 / 4 Method - extractive body cue:** We use a similarity module to predict the similarity conditioned on specific actions (Middle).
- **p. 3 / 4 Method - extractive body cue:** Then, to expand the supporting set along the similarity representation we built, we perform few-shot learning on novel categories with the guidance of the similarity ...
- **Detected method headings:** 4 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 4.4 Network Architecture and Training Strategy Our network consists of two modules - the affordance module and the similarity module. | p. 6 (4 Method), p. 6 (4 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We use a PointNet++ segmentation network [29] encoder for extracting features from 3D partial point clouds. | p. 6 (4 Method), p. 4 (4 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To achieve the first property, as shown in the middle of Figure 3, we propose a ‘similarity module' to predict the semantic ... | p. 4 (4 Method), p. 5 (4 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4 Method - extractive body cue:** To train the similarity module, we use an L1 loss to measure the distance between Similarity prediction and the ground truth accuracy.
- **p. 6 / 4 Method - extractive body cue:** To supervise the learning of the affordance network, We deploy a binary crossentropy loss, which measures the error between the affordance prediction of a given ...
- **p. 5 / 4 Method - extractive body cue:** Finally, both the affordance module and the similarity module will be updated by this interaction (Oi, pi, Ri, mi) and be ready for the next ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (4 Method), p. 6 (4 Method), p. 5 (4 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | similarity, module, designed, take, partial, point, cloud, object, action, directions, gripper, orientations, required, predict | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | similarity, module, designed, take, partial, point, cloud, object, action, directions | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | demonstrate, framework, capability, efficiently, explore, novel, categories, exploiting, geometric, similarity | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | train, similarity, module, loss, measure, distance, between, prediction, ground, truth | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4 Method - extractive body cue:** The similarity module is designed to take a partial point cloud of an object Oi ∈R3×N, a set of action directions and gripper orientations {Ri} ...
- **p. 4 / 4 Method - extractive body cue:** Given a specific action Ri on a point pi of a partial point cloud Oi, the affordance module is required to predict whether the given ...
- **p. 5 / 4 Method - extractive body cue:** Thanks to the property that similarity is conditioned on action directions and gripper orientations, we could sample interactions in diverse directions and poses Ri to ...
- **p. 5 / 4 Method - extractive body cue:** "##$%&'()* +$&,-* ./0/-'%/12 +$&,-* Similarity Affordance Gripper Pose Training categories Similarity Categories GT Interaction Action Direction 0 1 Affordance Category Split Affordance learning Similarity learning ...
- **p. 1 / 1 Introduction - extractive body cue:** Since encountering novel objects is inevitable in real-world applications, few-shot learning, which allows robots to propose interactions with novel objects and adapt their understanding to ...
- **p. 2 / 1 Introduction - extractive body cue:** Different from instance-level few-shot learning that focuses on discovering kinematic and dynamic information of a specific object, cross-category few-shot learning proposes a more demanding requirement ...
- **p. 6 / 4 Method - extractive body cue:** The encoder will output a per-point feature of 128 dimensions.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | As shown in Figure 2, we propose the ‘Where2Explore' framework to explicitly leverage the similar semantics on local geometries shared across different ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For example, handles are significant in pulling whereas less important in pushing, and a horizontal handle could not be grasped by a ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The encoder will output a per-point feature of 128 dimensions. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4 Method - extractive body cue:** 4.4 Network Architecture and Training Strategy Our network consists of two modules - the affordance module and the similarity module.
- **p. 7 / 5 Experiments - extractive body cue:** We select PointEncoder to compare our framework with a network pre-trained on large-scale datasets.
- **p. 7 / 5 Experiments - extractive body cue:** This baseline uses the pre-trained transformer encoder to extract features for few-shot affordance learning.
- **p. 5 / 4 Method - extractive body cue:** The Accu is computed using the accuracy in predicting the affordance score of an action during training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Network, Architecture, Training, Strategy, consists, modules, affordance, module, similarity, PointNet, segmentation, encoder, extracting, features, partial, point, clouds, achieve, first, property.
- **Relevant PDF headings:** 4 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Similarity-guided Exploration 1 Part motion Franka Emika Panda Robot Similarity prediction Azure Kinect DK 2 No part motion 3 Fail to grasp ... | p. 9 (5 Experiments), p. 7 (5 Experiments) |
| Semantic / temporal fusion | Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | For both the F-score and sample success rate, we use the average score of the four different training category combinations. | p. 7 (5 Experiments), p. 8 (5 Experiments) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately to ...
- **p. 7 / 5 Experiments - extractive body cue:** Besides, we compare to ablated versions of our method to verify our exploration strategy: • No-explore (lower bound): our affordance model directly evaluated on novel ...
- **p. 6 / 5 Experiments - extractive body cue:** We also conduct ablation studies to prove the efficiency of our exploration strategy.
- **p. 7 / 5 Experiments - extractive body cue:** 5.2 Baselines, Ablations, and Metrics Baselines and Ablations.
- **p. 6 / 5 Experiments - extractive body cue:** Finally, we test our fine-tuned model on unseen instances in novel categories to demonstrate that our model learns the general semantic and geometric information.
- **p. 8 / 5 Experiments - extractive body cue:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.
- **p. 9 / 5 Experiments - extractive body cue:** Although Affordance fails to directly generalize to novel categories (Left) via interacting on low-similarity areas (Middle), our framework could learn the semantic information on them ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (4 Method), p. 6 (4 Method), p. 4 (4 Method), p. 5 (4 Method), p. 3 (4 Method), p. 5 (4 Method), objective p. 6 (4 Method), p. 6 (4 Method), p. 5 (4 Method), temporal p. 3 (4 Method), p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method), p. 6 (5 Experiments), p. 6 (5 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
