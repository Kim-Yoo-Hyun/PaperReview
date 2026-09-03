# Insights — Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=meRCKuUpmc; PDF retrieval source: https://arxiv.org/pdf/2412.15109. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additionally, We evaluate our method on six challenging real-world tasks with over 900 trials.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce a foresight token to predict future RGB images and an action token to estimate intermediate actions between current and predicted future observations.
- **p. 3 / 3 METHOD - extractive body cue:** Therefore, we propose conditional visual foresight ffore to effectively anticipate future visual representations.
- **p. 4 / 3 METHOD - extractive body cue:** Seer consists of three parts: Multi-Modal Encoder, Conditional Visual Foresight and Inverse Dynamics Prediction.
- **p. 5 / 3 METHOD - extractive body cue:** Our aim is to answer: 1) How does our method perform on challenging simulation benchmarks?
- **p. 16 / A.2 NETWORK ARCHITECTURE - extractive body cue:** As presented in Figure A-1, Seer consists of the following modules: image encoder, perceiver resampler, robot state encoder, language encoder, transformer backbone, action decoder and ...
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 16 (A.2 NETWORK ARCHITECTURE)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** For example, R3M (Nair et al., 2022) and MVP (Xiao et al., 2022) learn discriminative representations from large-scale video datasets such as Ego4D (Grauman et ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our results further indicate superiority in long-horizon task completion, unseen scene generalization, and data efficiency.
- **p. 18 / A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS - extractive body cue:** The score will plus one (+1) when (1) pushing the button successfully with no collision, and (2) exceeding 3/4 of the scale.
- **p. 19 / A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS - extractive body cue:** The score will plus one (+1) when (1) grasping the camera model, and (2) inserting successfully with no collision.
- **p. 19 / A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS - extractive body cue:** Notably, both tasks require quite precise action predictions and collision-free interactions, showing our model's potential in high-precision and contact-rich tasks.
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Specifically, [FRS] tokens are appended to extract representations for two views, and three [INV ] tokens are appended to predict actions across three steps, ensuring ...
- **Boundary to test:** The score will plus one (+1) when (1) pushing the button successfully with no collision, and (2) exceeding 3/4 of the scale.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Additionally, We evaluate our method on six challenging real-world tasks with over 900 trials. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. Success" measures the average success rate across ten tasks. Seer ... | p. 6 (Figure/Table caption), p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS) |
| Failure/limitation | The score will plus one (+1) when (1) pushing the button successfully with no collision, and (2) exceeding 3/4 of the scale. | p. 18 (A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS), p. 19 (A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 Seer takes as input a goal g in the form of language instructions or robot states, along with historical observations ht, and predicts the RGB images at the time step t+n, denoted ...를 Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay Cosine decay Training Epochs 30 (LIBERO & ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The score will plus one (+1) when (1) pushing the button successfully with no collision, and (2) exceeding 3/4 of the scale.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Additionally, We evaluate our method on six challenging real-world tasks with over 900 trials.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, inverse dynamics, world model, manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The score will plus one (+1) when (1) pushing the button successfully with no collision, and (2) exceeding 3/4 of the scale.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: LIBERO (Liu et al., 2024) is a novel benchmark for lifelong learning in robot manipulation, comprising four task suites: LIBERO-SPATIAL, LIBERO-OBJECT, LIBERO-GOAL, and LIBERO100..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. Success" measures the average success rate across ten tasks. Seer ....
4. Report the body metric and its denominator/aggregation: Figure 4: Real-world Benchmark of four generalization-centric tasks. Left: We use a Franka Research 3 robot with a Robotiq-2f-85 gripper and two RealSense D435i cameras. Right: We design four real-world manipulation tasks: ....
5. Re-run the body-reported ablation/failure condition: We refer the subset mix-up recipe in Octo (Ghosh et al., 2024), remove all the subset that includes franka robots, filter subsets with odd action labels, and save the rest subsets as ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 16 (A.2 NETWORK ARCHITECTURE), p. 15 (A.1 IMPLEMENTATION DETAILS), p. 4 (3 METHOD); the primary result is directionally consistent at p. 6 (Figure/Table caption), p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS), p. 9 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Additionally, evaluate, challenging mechanism이 Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged ... 대비 Figure 4: Real-world Benchmark of four generalization-centric tasks. Left: We use a Franka Research 3 robot with a ...을 개선하고, The score will plus one (+1) when (1) pushing the button successfully with no collision, and ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
