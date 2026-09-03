# Method - Data Scaling Laws in Imitation Learning for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=pISLZG7ktL; PDF retrieval source: https://arxiv.org/pdf/2410.18647. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 APPROACH), p. 4 (3 APPROACH), p. 5 (3 APPROACH), p. 8 (3 APPROACH), p. 6 (3 APPROACH), p. 3 (3 APPROACH)): There are several key observations: (1) As the number of training objects increases, the policy's performance on unseen objects consistently improves across all fractions of demonstrations.

## Method Body Digest

- **p. 5 / 3 APPROACH - extractive body cue:** There are several key observations: (1) As the number of training objects increases, the policy's performance on unseen objects consistently improves across all fractions of ...
- **p. 4 / 3 APPROACH - extractive body cue:** (2) Temporal ensemble: Diffusion Policy predicts a sequence of actions every T1 steps, with each sequence having a length of T2 (T2 > T1), and ...
- **p. 5 / 3 APPROACH - extractive body cue:** To explore the effect of the number of training environments on generalization, we use the same manipulation object across 32 distinct environments, collecting 120 demonstrations ...
- **p. 8 / 3 APPROACH - extractive body cue:** For each selected environment, we use all demonstrations of n objects (n = 1, 2, 3, 4) as the training data.
- **p. 6 / 3 APPROACH - extractive body cue:** 4 illustrates that (1) increasing the number of training environment-object pairs substantially enhances the policy's generalization performance, consistent with previous observations.
- **p. 3 / 3 APPROACH - extractive body cue:** Then, we demonstrate our data source and design choices for policy learning methods.
- **p. 4 / 3 APPROACH - extractive body cue:** First, to evaluate the generalization performance of the policy, we exclusively test it in unseen environments or with unseen objects.
- **p. 4 / 3 APPROACH - extractive body cue:** UMI's portability, intuitive design, and low cost make it an ideal tool for our data collection needs.

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To answer this, we present a comprehensive empirical study on data scaling in imitation learning, which is a predominant method for learning real-world manipulation skills ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, based on these data scaling laws, we propose an efficient data collection strategy to achieve the desired level of generalization (Sec.
- **p. 4 / 3 APPROACH - extractive body cue:** It enables highly efficient data collection and allows for seamless switching between different in-the-wild environments with minimal setup time.

## Source Evidence Cues

- **p. 5 / 3 APPROACH - extractive body cue:** There are several key observations: (1) As the number of training objects increases, the policy's performance on unseen objects consistently improves across all fractions of ...
- **p. 4 / 3 APPROACH - extractive body cue:** (2) Temporal ensemble: Diffusion Policy predicts a sequence of actions every T1 steps, with each sequence having a length of T2 (T2 > T1), and ...
- **p. 5 / 3 APPROACH - extractive body cue:** To explore the effect of the number of training environments on generalization, we use the same manipulation object across 32 distinct environments, collecting 120 demonstrations ...
- **p. 8 / 3 APPROACH - extractive body cue:** For each selected environment, we use all demonstrations of n objects (n = 1, 2, 3, 4) as the training data.
- **p. 6 / 3 APPROACH - extractive body cue:** 4 illustrates that (1) increasing the number of training environment-object pairs substantially enhances the policy's generalization performance, consistent with previous observations.
- **p. 3 / 3 APPROACH - extractive body cue:** Then, we demonstrate our data source and design choices for policy learning methods.
- **p. 4 / 3 APPROACH - extractive body cue:** First, to evaluate the generalization performance of the policy, we exclusively test it in unseen environments or with unseen objects.
- **Detected method headings:** 3 APPROACH (p. 3); C POLICY TRAINING (p. 23)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | There are several key observations: (1) As the number of training objects increases, the policy's performance on unseen objects consistently improves across ... | p. 5 (3 APPROACH), p. 4 (3 APPROACH) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | (2) Temporal ensemble: Diffusion Policy predicts a sequence of actions every T1 steps, with each sequence having a length of T2 (T2 ... | p. 4 (3 APPROACH), p. 5 (3 APPROACH) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | To explore the effect of the number of training environments on generalization, we use the same manipulation object across 32 distinct environments, ... | p. 5 (3 APPROACH), p. 8 (3 APPROACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 APPROACH - extractive body cue:** UMI's portability, intuitive design, and low cost make it an ideal tool for our data collection needs.
- **p. 5 / 3 APPROACH - extractive body cue:** Finally, to minimize the tester's subjective bias, we simultaneously evaluate multiple policies trained on datasets of different sizes; each rollout is randomly selected from these ...
- **p. 7 / 3 APPROACH - extractive body cue:** Dashed lines represent power-law fits, with the equations provided in the legend.
- **p. 8 / 3 APPROACH - extractive body cue:** For example, according to the equation in Fig.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 7 (3 APPROACH), p. 8 (3 APPROACH).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | There, several, observations, number, training, objects, increases, policy, performance, unseen, consistently, improves, across, fractions | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | There, several, observations, number, training, objects, increases, policy, performance, unseen | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | answer, present, comprehensive, empirical, study, data, scaling, imitation, learning, predominant | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | UMI, portability, intuitive, design, cost, make, ideal, tool, data, collection | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 APPROACH - extractive body cue:** There are several key observations: (1) As the number of training objects increases, the policy's performance on unseen objects consistently improves across all fractions of ...
- **p. 4 / 3 APPROACH - extractive body cue:** Specifically, the policy predicts at each timestep, resulting in overlapping action sequences.
- **p. 4 / 3 APPROACH - extractive body cue:** (2) Temporal ensemble: Diffusion Policy predicts a sequence of actions every T1 steps, with each sequence having a length of T2 (T2 > T1), and ...
- **p. 5 / 3 APPROACH - extractive body cue:** Furthermore, to examine how policy performance varies with the number of demonstrations, we randomly sample 2n fractions of valid demonstrations (n = 0, -1, -2, ...
- **p. 6 / 3 APPROACH - extractive body cue:** 4 illustrates that (1) increasing the number of training environment-object pairs substantially enhances the policy's generalization performance, consistent with previous observations.
- **p. 3 / 3 APPROACH - extractive body cue:** Then, we demonstrate our data source and design choices for policy learning methods.
- **p. 6 / 3 APPROACH - extractive body cue:** Each policy is evaluated in 8 unseen environments, using two unseen objects per environment, with 5 trials per environment.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Specifically, the policy predicts at each timestep, resulting in overlapping action sequences. | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | (2) Temporal ensemble: Diffusion Policy predicts a sequence of actions every T1 steps, with each sequence having a length of T2 (T2 ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | Each step can receive a maximum of 3 points, and we report a normalized score, defined as Normalized score = Total test ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 APPROACH - extractive body cue:** There are several key observations: (1) As the number of training objects increases, the policy's performance on unseen objects consistently improves across all fractions of ...
- **p. 5 / 3 APPROACH - extractive body cue:** To explore the effect of the number of training environments on generalization, we use the same manipulation object across 32 distinct environments, collecting 120 demonstrations ...
- **p. 8 / 3 APPROACH - extractive body cue:** For each selected environment, we use all demonstrations of n objects (n = 1, 2, 3, 4) as the training data.
- **p. 6 / 3 APPROACH - extractive body cue:** 4 illustrates that (1) increasing the number of training environment-object pairs substantially enhances the policy's generalization performance, consistent with previous observations.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** There, several, observations, number, training, objects, increases, policy, performance, unseen, consistently, improves, across, fractions, demonstrations, Temporal, ensemble, Diffusion, predicts, sequence.
- **Relevant PDF headings:** 3 APPROACH (p. 3); C POLICY TRAINING (p. 23).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | Existing robotic manipulation datasets do not provide enough environments and objects for a single task to meet our requirements. | p. 4 (3 APPROACH), p. 4 (3 APPROACH) |
| Policy fitting | To further enhance performance, we make two improvements: (1) DINOv2 visual encoder: In our experiments, fine-tuning the DINOv2 ViT (Oquab et al., ... | p. 4 (3 APPROACH), p. 6 (3 APPROACH) |
| Closed-loop rollout | To further enhance performance, we make two improvements: (1) DINOv2 visual encoder: In our experiments, fine-tuning the DINOv2 ViT (Oquab et al., ... | p. 4 (3 APPROACH), p. 1 (ABSTRACT) |

## Failure and Ablation Link

- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Model related experiments on Pour Water. The entries marked in gray are the same, which specify the default settings: the visual encoder is ...
- **p. 5 / 3 APPROACH - extractive body cue:** Throughout all experiments, we also analyze the effect of demonstration quantity (Sec.
- **p. 5 / 3 APPROACH - extractive body cue:** To explore the effect of the number of training environments on generalization, we use the same manipulation object across 32 distinct environments, collecting 120 demonstrations ...
- **p. 3 / 3 APPROACH - extractive body cue:** For instance, special lighting setups might be used to change only the color of illumination, or 3D-printed objects might be designed to vary only in ...
- **p. 8 / 3 APPROACH - extractive body cue:** The main question we seek to answer is: for a given manipulation task, how can we optimally select M, N, and K to ensure strong ...
- **p. 10 / 32 Env-Object Pairs - extractive body cue:** Both pretraining and full fine-tuning are indispensable.
- **p. 4 / 3 APPROACH - extractive body cue:** To further enhance performance, we make two improvements: (1) DINOv2 visual encoder: In our experiments, fine-tuning the DINOv2 ViT (Oquab et al., 2023) outperforms both ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 APPROACH), p. 4 (3 APPROACH), p. 5 (3 APPROACH), p. 8 (3 APPROACH), p. 6 (3 APPROACH), p. 3 (3 APPROACH), objective p. 4 (3 APPROACH), p. 5 (3 APPROACH), p. 7 (3 APPROACH), p. 8 (3 APPROACH), temporal p. 4 (3 APPROACH), p. 4 (3 APPROACH), p. 1 (ABSTRACT), p. 5 (3 APPROACH), p. 5 (3 APPROACH).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
