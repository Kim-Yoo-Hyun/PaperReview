# Method - SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2011.07215; PDF retrieval source: https://arxiv.org/pdf/2011.07215. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), p. 5 (1 Introduction)): Due to the large number of samples required by reinforcement learning, as well as the difficulty in specifying a reward function, all these works start by training the policy in ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Due to the large number of samples required by reinforcement learning, as well as the difficulty in specifying a reward function, all these works start ...
- **p. 2 / 1 Introduction - extractive body cue:** We benchmark a range of algorithms on these environments assuming different observation spaces for the policy, including full knowledge of the ground-truth state of the ...
- **p. 5 / 1 Introduction - extractive body cue:** 5.2 State Oracle Many robotic systems follow the paradigm of first performing state estimation and then using the estimated state as input to a policy.
- **p. 1 / Abstract - extractive body cue:** Further, we evaluate a variety of algorithms on these tasks and highlight challenges for reinforcement learning algorithms, including dealing with a state representation that has ...
- **p. 3 / 1 Introduction - extractive body cue:** 4 SoftGym To advance research in reinforcement learning in complex environments with an inherently high dimensional state, we propose SoftGym.
- **p. 5 / 1 Introduction - extractive body cue:** We use these positions as input to a policy trained using SAC [49]; we use the standard multi-layer perceptron (MLP) as the architecture for the ...
- **p. 6 / 1 Introduction - extractive body cue:** We also evaluate PlaNet [54], which learns a latent state space dynamics model for planning.
- **p. 5 / 1 Introduction - extractive body cue:** Given this information, we can use gradient free optimization to maximize the return.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface ...
- **p. 3 / 1 Introduction - extractive body cue:** SoftGym consists of three parts: SoftGym-Medium, SoftGym-Hard and SoftGym-Robot, visualized in Figure 1.
- **p. 3 / 1 Introduction - extractive body cue:** 4 SoftGym To advance research in reinforcement learning in complex environments with an inherently high dimensional state, we propose SoftGym.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** Due to the large number of samples required by reinforcement learning, as well as the difficulty in specifying a reward function, all these works start ...
- **p. 2 / 1 Introduction - extractive body cue:** We benchmark a range of algorithms on these environments assuming different observation spaces for the policy, including full knowledge of the ground-truth state of the ...
- **p. 5 / 1 Introduction - extractive body cue:** 5.2 State Oracle Many robotic systems follow the paradigm of first performing state estimation and then using the estimated state as input to a policy.
- **p. 1 / Abstract - extractive body cue:** Further, we evaluate a variety of algorithms on these tasks and highlight challenges for reinforcement learning algorithms, including dealing with a state representation that has ...
- **p. 3 / 1 Introduction - extractive body cue:** 4 SoftGym To advance research in reinforcement learning in complex environments with an inherently high dimensional state, we propose SoftGym.
- **p. 5 / 1 Introduction - extractive body cue:** We use these positions as input to a policy trained using SAC [49]; we use the standard multi-layer perceptron (MLP) as the architecture for the ...
- **p. 6 / 1 Introduction - extractive body cue:** We also evaluate PlaNet [54], which learns a latent state space dynamics model for planning.
- **Detected method headings:** B Algorithm Details (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Due to the large number of samples required by reinforcement learning, as well as the difficulty in specifying a reward function, all ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We benchmark a range of algorithms on these environments assuming different observation spaces for the policy, including full knowledge of the ground-truth ... | p. 2 (1 Introduction), p. 5 (1 Introduction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | 5.2 State Oracle Many robotic systems follow the paradigm of first performing state estimation and then using the estimated state as input ... | p. 5 (1 Introduction), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 1 Introduction - extractive body cue:** Given this information, we can use gradient free optimization to maximize the return.
- **p. 6 / 1 Introduction - extractive body cue:** Among these, we benchmark CURL-SAC [51], which uses a model-free approach with a contrastive loss among randomly cropped images, and DrQ [52], which applies data ...
- **p. 2 / 1 Introduction - extractive body cue:** Different physical properties of the objects are characterized by the constraints.
- **p. 2 / 1 Introduction - extractive body cue:** Each object is represented by a set of particles and the internal constraints among these particles.
- **p. 3 / 1 Introduction - extractive body cue:** Additional constraints for modeling self-collision are applied.
- **p. 3 / 1 Introduction - extractive body cue:** Each particle is connected to its eight neighbors by a spring, i.e. a stretching constraint.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | benchmark, range, algorithms, environments, assuming, different, observation, spaces, policy, including, full, knowledge, ground-truth, state | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | benchmark, range, algorithms, environments, assuming, different, observation, spaces, policy, including | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | present, SoftGym, open-source, simulated, benchmarks, manipulating, deformable, objects, standard, OpenAI | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Given, information, gradient, free, optimization, maximize, return, Among, benchmark, CURL-SAC | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** We benchmark a range of algorithms on these environments assuming different observation spaces for the policy, including full knowledge of the ground-truth state of the ...
- **p. 5 / 1 Introduction - extractive body cue:** 5.2 State Oracle Many robotic systems follow the paradigm of first performing state estimation and then using the estimated state as input to a policy.
- **p. 5 / 1 Introduction - extractive body cue:** Reduced State Oracle To avoid the challenges of RL from high-dimensional state spaces, this method uses a hand-defined reduced set of the full state as ...
- **p. 6 / 1 Introduction - extractive body cue:** It is important to evaluate methods that use high dimensional observations as input, since it cannot be assumed that a low dimensional state representation (such ...
- **p. 6 / 1 Introduction - extractive body cue:** 5.3 Image Based Observations We also evaluate state-of-the-art RL algorithms that directly operate on high dimensional observations.
- **p. 2 / 1 Introduction - extractive body cue:** Currently, SoftGym includes 10 challenging environments involving manipulation of rope, cloth and fluid of variable properties, with different options for the state and action spaces.
- **p. 4 / 1 Introduction - extractive body cue:** SoftGym-Hard contains four more tasks: PourWaterAmount This task is similar to PourWater but requires a specific amount of water poured into the target cup, indicated ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | All methods are trained for 106 time steps, except PlaNet, which is trained for 5 × 105 time steps due to computation ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | In Figure 2, we show the final performance of this method with 20 pick-and-place steps for each episode. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Given an initial set of five frames, PlaNet predicts the following 30 frames. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** Due to the large number of samples required by reinforcement learning, as well as the difficulty in specifying a reward function, all these works start ...
- **p. 5 / 1 Introduction - extractive body cue:** We use these positions as input to a policy trained using SAC [49]; we use the standard multi-layer perceptron (MLP) as the architecture for the ...
- **p. 6 / 1 Introduction - extractive body cue:** The x-axis shows the number of training time steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Due, large, number, samples, required, reinforcement, learning, well, difficulty, specifying, reward, function, works, start, training, policy, simulation, then, transfer, real.
- **Relevant PDF headings:** B Algorithm Details (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Thus, this evaluation points to a clear need for new methods development for image-based robot manipulation of deformable objects. | p. 7 (6 Experiments), p. 8 (6 Experiments) |
| Baseline harness | While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for ... | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Metric / failure reporting | While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for ... | p. 7 (6 Experiments), p. 7 (6 Experiments) |

## Failure and Ablation Link

- **p. 7 / 6 Experiments - extractive body cue:** from a policy that always does nothing.
- **p. 7 / 6 Experiments - extractive body cue:** On the other hand, this method does not perform very well on the FoldCloth task.
- **p. 17 / Figure/Table caption - extractive body cue:** Table 7: Architecture of the deconvolutional neural network (VAE decoder) in PlaNet. We use a GRU [56] with 200 hidden nodes as the deterministic path ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), p. 5 (1 Introduction), objective p. 5 (1 Introduction), p. 6 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), temporal p. 7 (6 Experiments), p. 7 (6 Experiments), p. 6 (1 Introduction), p. 8 (6 Experiments), p. 8 (6 Experiments), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
