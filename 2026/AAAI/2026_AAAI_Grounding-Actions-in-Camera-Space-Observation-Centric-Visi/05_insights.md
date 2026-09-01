# Insights — Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38947; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38947. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Notably, our method exhibits markedly improved adaptability to previously unseen camera viewarXiv:2508.13103v1 [cs.RO] 18 Aug 2025
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

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 OC-VLA transforms the end effector pose whether defined in a discrete or continuous action space from the robot base coordinate to the third-person camera coordinate, unifying the observation and prediction targets across ...를 This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view inputs are available.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially compensate for the limited pretraining data and model ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly in the third-person camera coordinate system, named ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Robotics, action representation, camera space, cross-view generalization, real-world manipulation`.
- **Reading predecessor in the generated track queue:** GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially compensate for the limited pretraining data and model ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms..
3. Compare against the body-reported baseline or a matched simpler baseline: These models serve as baselines in our evaluation..
4. Report the body metric and its denominator/aggregation: For each task, we conduct 10 trials and measure performance by computing the task success rate..
5. Re-run the body-reported ablation/failure condition: For model finetuning, we fine-tune the model pretrained on the Droid dataset, using either end effector actions defined in the third-person camera coordinate or those in the robot base coordinate as prediction ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, issues, novel mechanism이 These models serve as baselines in our evaluation. 대비 For each task, we conduct 10 trials and measure performance by computing the task success rate.을 개선하고, Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
