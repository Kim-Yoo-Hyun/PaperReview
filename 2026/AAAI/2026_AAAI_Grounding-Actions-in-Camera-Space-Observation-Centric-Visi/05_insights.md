# Insights — Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38947; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38947. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Notably, our method exhibits markedly improved adaptability to previously unseen camera view.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We introduce the Observation-Centric VLA (OC-VLA) framework.
- **p. 3 / III. METHOD - extractive body cue:** Different from previous end-effector action prediction, the predicted action in our method is in the camera space.
- **p. 3 / III. METHOD - extractive body cue:** Based on the baseline architecture, we implement a variant specifically designed for discrete action prediction or continuous action prediction.
- **p. 3 / III. METHOD - extractive body cue:** While these representations are widely used as supervision signals for Vision-Language-Action (VLA) models, they are tightly coupled with specific robot embodiment configurations, rather than being ...
- **p. 3 / III. METHOD - extractive body cue:** Consequently, it is difficult for the model to achieve a reasonable projection from image observation to corresponding actions, and thus the model generalization is limited, ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although this paradigm has achieved impressive performance across a variety of benchmarks, it remains fundamentally constrained by the intrinsic limitations of the robotics domain-namely, the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** By transforming end-effector actions from the robot base coordinate to the third-person camera coordinate, OC-VLA aligns action predictions with visual observations across diverse viewpoints, enabling ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially compensate ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** This diversity makes it an ideal choice for evaluating the generalizability and robustness of our observationcentric action prediction framework.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In addition to language and image tokens, we concatenate the current timestep and the noise-perturbed action as inputs to the causal transformer.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this setting, the camera viewpoint remains fixed and identical throughout both the finetuning and evaluation phases. • Slight Camera Perturbations To further validate the ...
- **Boundary to test:** Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially compensate for the limited pretraining data and model ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly in the third-person camera coordinate system, named ... | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | However, when the prediction target is switched from robot-base coordinate actions to camera-base coordinate actions, the model achieves a further 10% improvement in the metric of success rate, surpassing the best-performing baseline, ... | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Failure/limitation | Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially compensate for the limited pretraining data and model ... | p. 7 (Figure/Table caption), p. 2 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** OC-VLA transforms the end effector pose whether defined in a discrete or continuous action space from the robot base coordinate to the third-person camera coordinate, unifying the observation and prediction ... (p. 3, III. METHOD).
- **Paper-specific mechanism:** To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly in the third-person camera coordinate ... (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms. (p. 4, IV. EXPERIMENTS); the relevant task/metric cue is For each task, we conduct 10 trials and measure performance by computing the task success rate. (p. 5, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Failures are highlighted with red circles. the same data. (p. 7, IV. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Robotics, action representation, camera space, cross-view generalization, real-world manipulation`.
- **Reading predecessor in the generated track queue:** GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially compensate for the limited pretraining data and model ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: OC-VLA transforms the end effector pose whether defined in a discrete or continuous action space from the robot base coordinate to the third-person camera coordinate, unifying the observation and prediction ... (p. 3, III. METHOD); preserve the objective/update rule: We then analyze the differences between camera-coordinate and robotcoordinate optimization. (p. 2, III. METHOD).
2. Use the paper-reported task/data/environment cue: Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms. (p. 4, IV. EXPERIMENTS).
3. Compare against the reported or matched baseline: These models serve as baselines in our evaluation. (p. 5, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: For each task, we conduct 10 trials and measure performance by computing the task success rate. (p. 5, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: METHODS ANNOTATED WITH "(VAR)" INDICATE RESULTS OBTAINED UNDER ZERO-SHOT CAMERA EVALUATION, WHILE THOSE WITHOUT THE ANNOTATION CORRESPOND TO EVALUATIONS CONDUCTED USING THE TRAINING CAM 1. (p. 6, IV. EXPERIMENTS); if none is reported, design one around: Failures are highlighted with red circles. the same data. (p. 7, IV. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), and measure the boundary at p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (OC-VLA transforms the end effector pose whether defined in a discrete or continuous action space from the robot base coordinate to the ...), does the paper-specific mechanism (To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead ...) retain the reported evaluation outcome (For each task, we conduct 10 trials and measure performance by computing the task success rate.) when tested against the paper's strongest explicit boundary (Failures are highlighted with red circles. the same data.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (For each task, we conduct 10 trials and measure performance by computing the task success rate.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly in the third-person camera coordinate ... (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms. (p. 4, IV. EXPERIMENTS).
- **Strongest explicit boundary:** Failures are highlighted with red circles. the same data. (p. 7, IV. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
