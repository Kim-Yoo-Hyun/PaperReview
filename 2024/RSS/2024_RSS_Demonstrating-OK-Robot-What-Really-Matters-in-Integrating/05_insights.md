# Insights — Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p091.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p091.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** The system we introduce is a combination of three primary subsystems combined on a Hello Robot: Stretch.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** This manual scan simply consists of taking a video of the home using the Record3D app on the iPhone, which results in a sequence of ...
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** If -→p is the grasp point and -→a is the approach vector given by the grasping model, our robot gripper follows the following trajectory: ⟨-→p ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Hence, making progress on this problem requires a careful and nuanced framework that both integrates * Denotes equal contribution and † denotes equal advising.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Open-home, open-vocabulary object navigation The first component of our method is an open-home, openvocabulary object navigation model that we use to map a home and ...
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Navigating to objects in the real world: Once our navigation model gives us a 3D location coordinate in the real world, we use that as ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 2 (I. INTRODUCTION), p. 3 (II. TECHNICAL COMPONENTS AND METHOD)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** We also find that using heuristics to counteract the robot's physical limitations can lead to a better success rate in the real world (see Section ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To highlight the difficulty of this problem, the recent NeurIPS 2023 challenge for open-vocabulary mobile manipulation (OVMM) [22] registered a success rate of 33% for ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D ...
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety of objects, certain hardware limitations also dictate ...
- **p. 6 / III. EXPERIMENTS - extractive body cue:** 4) What are the failure modes of such a system and its individual components in real home environments?
- **p. 6 / III. EXPERIMENTS - extractive body cue:** As a result, each success and failure of the robot tells us something interesting about applying open-knowledge models in robotics, which we analyze over the ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** However, at a closer look, we notice a long tail of failure causes presented in Figure 4.
- **Boundary to test:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop. | p. 2 (I. INTRODUCTION), p. 3 (II. TECHNICAL COMPONENTS AND METHOD) |
| Reported outcome | Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops. | p. 6 (III. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Failure/limitation | Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image. | p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 Overall, through our experiments, we make the following observations: • Pre-trained VLMs are highly effective for openvocabulary navigation: Current open-vocabulary visionlanguage models such as CLIP [9] or OWL-ViT [8] offer strong perf ...를 Since we do not implement error detection or correction, our state machine model is a simple linear chain of steps leading from navigating to object, to grasping, to navigating to goal, and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, mobile manipulation, open-vocabulary perception, home robotics`.
- **Reading predecessor in the generated track queue:** RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The three leading causes of failures are failing to retrieve the right object to navigate to from the semantic memory (9.3%), getting a difficult pose from the manipulation module (8.0%), and robot ....
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 5: Ablation experiment using different semantic memory and grasping modules, with the bars showing average performance and the error bars showing standard deviation over the environments. vocabulary navigation and grasping modules. ....
4. Report the body metric and its denominator/aggregation: Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and the error rates decrease from 25% to 16% and finally 13%..
5. Re-run the body-reported ablation/failure condition: Ablations over system components Apart from the navigation and manipulation strategies used in OK-Robot, we also evaluated a number of alternative open.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD); the primary result is directionally consistent at p. 6 (III. EXPERIMENTS), p. 1 (Figure/Table caption), p. 7 (III. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, OK-Robot, Open mechanism이 Fig. 5: Ablation experiment using different semantic memory and grasping modules, with the bars showing average ... 대비 Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and ...을 개선하고, Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
