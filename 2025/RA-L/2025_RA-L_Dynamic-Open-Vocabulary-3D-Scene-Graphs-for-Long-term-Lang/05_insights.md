# Insights — Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.11989; PDF retrieval source: https://arxiv.org/pdf/2410.11989. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate ...
- **p. 4 / III. METHOD - extractive body cue:** We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly.
- **p. 2 / III. METHOD - extractive body cue:** DovSG enables mobile robots to perform long-term tasks in indoor environments by constructing dynamic 3D scene graphs and using large language models for task planning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we enhance robotic capabilities by introducing a novel and practical robotic framework, the DovSG system.
- **p. 4 / III. METHOD - extractive body cue:** To address this issue, we have designed a simple memory update module that can quickly perform local updates to the memory based on new RGB-D ...
- **p. 4 / III. METHOD - extractive body cue:** Then, we apply an advanced Open-Vocal segmentation model to segment regions in the RGB images, extract semantic feature vectors for each region, and project them ...
- **p. 5 / III. METHOD - extractive body cue:** 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start point ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** This limitation restricts their applicability in real-world scenarios where adaptability is crucial.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address the challenge of scene perception, our perception module integrates advanced tools such as RecognizeAnything [6], Grounding DINO [7], Segment Anything-2 [8], and CLIP ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing ...
- **p. 5 / III. METHOD - extractive body cue:** 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start point ...
- **p. 6 / III. METHOD - extractive body cue:** A buffer of 0.1 is added to account for potential collisions.
- **p. 6 / III. METHOD - extractive body cue:** In the first row, we cropped the point cloud input into anyGrasp within a certain range around the target object, allowing anyGrasp to focus more ...
- **Boundary to test:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing navigation failure.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate long-term task execution in dynamic and interactive ... | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD) |
| Reported outcome | This makes it highly likely for the robot to navigate near the target, resulting in a significantly higher success rate compared to "Appearance" and "Positional Shift" (in 80 trials, it achieved 5 ... | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Failure/limitation | In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing navigation failure. | p. 7 (IV. EXPERIMENTS), p. 5 (III. METHOD) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** YAN et al.: DYNAMIC OPEN-VOCABULARY 3D SCENE GRAPHS FOR LONG-TERM LANGUAGE-GUIDED MOBILE MANIPULATION 5 and color information, we process each new observation Ik as follows: (1) We transform the all ... (p. 5, III. METHOD).
- **Paper-specific mechanism:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate long-term task execution in dynamic ... (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is This results in a 10.7% higher pick-up success rate than Ok-Robot, which relies solely on AnyGrasp. (p. 7, IV. EXPERIMENTS); the relevant task/metric cue is (3) Task Success Rate: This metric represents the overall task completion success rate. (p. 7, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** These changes are often invisible to previous approaches [3], [21], [14], and in such environments, if the robot cannot dynamically update its memory, it will soon face failure. (p. 4, III. METHOD).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, 3D Vision, Graph Reasoning, semantic`.
- **Reading predecessor in the generated track queue:** Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing navigation failure.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: YAN et al.: DYNAMIC OPEN-VOCABULARY 3D SCENE GRAPHS FOR LONG-TERM LANGUAGE-GUIDED MOBILE MANIPULATION 5 and color information, we process each new observation Ik as follows: (1) We transform the all ... (p. 5, III. METHOD); preserve the objective/update rule: From these, a 3D scene graph is generated, capturing object relationships and continuously updated when the environment changes. (p. 2, III. METHOD).
2. Use the paper-reported task/data/environment cue: 2) Environment and Task Setups: To verify our method's ability to enable robots to perform long-term tasks in dynamic environments, we designed an experiment in 4 real-world rooms. (p. 6, IV. EXPERIMENTS).
3. Compare against the reported or matched baseline: In contrast, DovSG, supported by precise relocalization, can accurately identify the voxel index where changes have occurred in the scene, significantly outperforming the baseline. (p. 7, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: (3) Task Success Rate: This metric represents the overall task completion success rate. (p. 7, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: (2) How effectively does this facilitate the completion of consecutive tasks without manual resets? (p. 6, IV. EXPERIMENTS); if none is reported, design one around: These changes are often invisible to previous approaches [3], [21], [14], and in such environments, if the robot cannot dynamically update its memory, it will soon face failure. (p. 4, III. METHOD).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), and measure the boundary at p. 4 (III. METHOD), p. 7 (IV. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (YAN et al.: DYNAMIC OPEN-VOCABULARY 3D SCENE GRAPHS FOR LONG-TERM LANGUAGE-GUIDED MOBILE MANIPULATION 5 and color information, we process each new observation ...), does the paper-specific mechanism (Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task ...) retain the reported evaluation outcome ((3) Task Success Rate: This metric represents the overall task completion success rate.) when tested against the paper's strongest explicit boundary (These changes are often invisible to previous approaches [3], [21], [14], and in such environments, if the robot ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric ((3) Task Success Rate: This metric represents the overall task completion success rate.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate long-term task execution in dynamic ... (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** This results in a 10.7% higher pick-up success rate than Ok-Robot, which relies solely on AnyGrasp. (p. 7, IV. EXPERIMENTS).
- **Strongest explicit boundary:** These changes are often invisible to previous approaches [3], [21], [14], and in such environments, if the robot cannot dynamically update its memory, it will soon face failure. (p. 4, III. METHOD).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
