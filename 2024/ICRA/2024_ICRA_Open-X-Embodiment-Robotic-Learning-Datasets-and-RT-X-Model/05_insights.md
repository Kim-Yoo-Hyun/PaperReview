# Insights — Open X-Embodiment: Robotic Learning Datasets and RT-X Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.08864; PDF retrieval source: https://arxiv.org/pdf/2310.08864. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive ...
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning research.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that the resulting models, which we call RT-X, can improve over policies trained only on data from the evaluation domain, exhibiting better generalization ...
- **p. 4 / 5 Hz - extractive body cue:** RT-1-X is an architecture designed for robotics, with a FiLM [116] conditioned EfficientNet [117] and a Transformer [118].
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Although both architectures are described in detail in their original papers [8, 9], we provide a short summary of each below: RT-1 [8] is a ...
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Policy architectures We consider two model architectures in our experiments: (1) RT-1 [8], an efficient Transformer-based architecture designed for robotic control, and (2) RT-2 [9] ...
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** These tokens are fed into a decoder-only Transformer, which outputs the tokenized actions.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 2 (I. INTRODUCTION), p. 4 (5 Hz), p. 4 (IV. RT-X DESIGN), p. 4 (IV. RT-X DESIGN)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these lessons are difficult to apply in robotics: any single robotic domain might be too narrow, and while computer vision and NLP can leverage ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** How can we overcome these challenges in robotics and move the field of robotic learning toward large data regime that has been so successful in ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** DISCUSSION, FUTURE WORK, AND OPEN PROBLEMS We presented a consolidated dataset that combines data from 22 robotic embodiments collected through a collaboration between 21 institutions, ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** 5: To assess transfer between embodiments, we evaluate the RT-2-X model on out-of-distribution skills.
- **Boundary to test:** In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive transfer. | p. 2 (I. INTRODUCTION), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY) |
| Reported outcome | Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the bigger vision-language-modelbased version (RT-2-X) demonst ... | p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Failure/limitation | In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class. | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 3: RT-1-X and RT-2-X both take images and a text instruction as input and output discretized end-effector actions.를 Both models take in a visual input and natural language instruction describing the task, and output a tokenized action.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive transfer.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `VLA and generalist robot policies`; tags: `Robotics, Dataset, Imitation Learning`.
- **Reading predecessor in the generated track queue:** VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Octo: An Open-Source Generalist Robot Policy (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Row Model Size History Length Dataset Co-Trained w/ Web Initial Checkpoint Emergent Skills Evaluation RT-2 Generalization Evaluation (1) RT-2 55B none Google Robot action Yes Web-pretrained 27.3% 62% (2) RT-2-X 55B none ....
3. Compare against the body-reported baseline or a matched simpler baseline: In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class..
4. Report the body metric and its denominator/aggregation: We also note that the 55B model has significantly higher success rate in the Emergent Skills compared to the 5B model (row (2) vs row (4)), demonstrating that higher model capacity enables ....
5. Re-run the body-reported ablation/failure condition: Our next ablation involves removing the Bridge dataset from RT-2-X training: Row (3) shows the results for RT-2X that includes all data used for RT-2-X except the Bridge dataset..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (IV. RT-X DESIGN), p. 4 (IV. RT-X DESIGN), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY); the primary result is directionally consistent at p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Addressing, goal, empirical mechanism이 In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only ... 대비 We also note that the 55B model has significantly higher success rate in the Emergent Skills compared to ...을 개선하고, In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
