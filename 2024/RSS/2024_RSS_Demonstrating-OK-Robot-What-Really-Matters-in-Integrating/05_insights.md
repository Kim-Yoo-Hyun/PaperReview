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
- **p. 2 / I. INTRODUCTION - extractive body cue:** Hence, making progress on this problem requires a careful and nuanced framework that both integrates * Denotes.
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

- **Paper-specific interface:** Once collected, the RGB-D images, along with the camera pose and positions, are exported to our library for map-building. (p. 3, II. TECHNICAL COMPONENTS AND METHOD).
- **Paper-specific mechanism:** We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops. (p. 6, III. EXPERIMENTS); the relevant task/metric cue is Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and the error rates decrease from 25% to 16% and finally 13%. (p. 7, III. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image. (p. 7, III. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, mobile manipulation, open-vocabulary perception, home robotics`.
- **Reading predecessor in the generated track queue:** RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Once collected, the RGB-D images, along with the camera pose and positions, are exported to our library for map-building. (p. 3, II. TECHNICAL COMPONENTS AND METHOD); preserve the objective/update rule: Thus, our navigation method has to balance the following objectives: 1) The robot needs to be close enough to the object to manipulate it, 2) The robot needs some space ... (p. 3, II. TECHNICAL COMPONENTS AND METHOD).
2. Use the paper-reported task/data/environment cue: In Appendix Figure 12, we show the robot performing pick-and-drop in these two environments. (p. 6, III. EXPERIMENTS).
3. Compare against the reported or matched baseline: Both were larger compared to the average NY homes, requiring more robot motion to navigate to different goals. (p. 6, III. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and the error rates decrease from 25% to 16% and finally 13%. (p. 7, III. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: Ablations over system components Apart from the navigation and manipulation strategies used in OK-Robot, we also evaluated a number of alternative open (p. 6, III. EXPERIMENTS); if none is reported, design one around: Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image. (p. 7, III. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 7 (Figure/Table caption), and measure the boundary at p. 7 (III. EXPERIMENTS), p. 2 (I. INTRODUCTION).

## Falsifiable research question

Under the paper's stated interface (Once collected, the RGB-D images, along with the camera pose and positions, are exported to our library for map-building.), does the paper-specific mechanism (We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop.) retain the reported evaluation outcome (Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and ...) when tested against the paper's strongest explicit boundary (Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops. (p. 6, III. EXPERIMENTS).
- **Strongest explicit boundary:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image. (p. 7, III. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
