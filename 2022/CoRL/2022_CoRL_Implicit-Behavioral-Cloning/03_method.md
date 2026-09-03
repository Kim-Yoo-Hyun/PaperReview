# Method - Implicit Behavioral Cloning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v164/florence22a.html; PDF retrieval source: https://arxiv.org/pdf/2109.00137. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 6 (1 Introduction), p. 4 (1 Introduction)): We use either a) a derivative-free (sampling-based) optimization procedure, b) an auto-regressive variant of the derivative-free optimizer which performs coordinate descent, or c) gradient-based Langevin sampling [11, 12] with gradient ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** We use either a) a derivative-free (sampling-based) optimization procedure, b) an auto-regressive variant of the derivative-free optimizer which performs coordinate descent, or c) gradient-based Langevin ...
- **p. 2 / 1 Introduction - extractive body cue:** Given a dataset of samples {xi,yi}, and regression bounds ymin,ymax ∈Rm, training consists of generating a set of negative counter-examples {˜yj i}Nneg. j=1 for each ...
- **p. 1 / 1 Introduction - extractive body cue:** Like many other supervised learning methods, BC policies are often represented by explicit continuous feed-forward models (e.g., deep networks) of the form ˆa=Fθ(o) that map ...
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose to reformulate BC using implicit models - specifically, the composition of argmin with a continuous energy function Eθ (see Sec.
- **p. 6 / 1 Introduction - extractive body cue:** The action space is 12DoF (6DoF Cartesian per arm), and each episode consists of 700 steps recorded at 10Hz.
- **p. 4 / 1 Introduction - extractive body cue:** 4 shows how on a simple visual coordinate regression task, which is a notoriously hard problem for convolutional networks [23], an MSE-trained Conv-MLP model [24] ...
- **p. 5 / 1 Introduction - extractive body cue:** N-D Particle Integrator is a simple environment with linear dynamics but where a discontinuous oracle policy is used to generate training demonstrations: once within the ...
- **p. 2 / 1 Introduction - extractive body cue:** This loss equates to the negative log likelihood of pθ(y/x)= exp(-Eθ(x,y)) Z(x,θ) , and the counter-examples are used to estimate Z(xi,θ): LInfoNCE= N X i=1 ...

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose to reformulate BC using implicit models - specifically, the composition of argmin with a continuous energy function Eθ (see Sec.
- **p. 2 / 1 Introduction - extractive body cue:** 2), to build intuition on the nature of implicit models, we present their empirical properties (Sec.
- **p. 2 / 1 Introduction - extractive body cue:** Given a dataset of samples {xi,yi}, and regression bounds ymin,ymax ∈Rm, training consists of generating a set of negative counter-examples {˜yj i}Nneg. j=1 for each ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** We use either a) a derivative-free (sampling-based) optimization procedure, b) an auto-regressive variant of the derivative-free optimizer which performs coordinate descent, or c) gradient-based Langevin ...
- **p. 2 / 1 Introduction - extractive body cue:** Given a dataset of samples {xi,yi}, and regression bounds ymin,ymax ∈Rm, training consists of generating a set of negative counter-examples {˜yj i}Nneg. j=1 for each ...
- **p. 1 / 1 Introduction - extractive body cue:** Like many other supervised learning methods, BC policies are often represented by explicit continuous feed-forward models (e.g., deep networks) of the form ˆa=Fθ(o) that map ...
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose to reformulate BC using implicit models - specifically, the composition of argmin with a continuous energy function Eθ (see Sec.
- **p. 6 / 1 Introduction - extractive body cue:** The action space is 12DoF (6DoF Cartesian per arm), and each episode consists of 700 steps recorded at 10Hz.
- **p. 4 / 1 Introduction - extractive body cue:** 4 shows how on a simple visual coordinate regression task, which is a notoriously hard problem for convolutional networks [23], an MSE-trained Conv-MLP model [24] ...
- **p. 5 / 1 Introduction - extractive body cue:** N-D Particle Integrator is a simple environment with linear dynamics but where a discontinuous oracle policy is used to generate training demonstrations: once within the ...
- **Detected method headings:** B Energy-Based Model Training and Implicit Inference Details (p. 13); B.1 Method with Derivative-Free Optimization (p. 13); B.2 Method with Autoregressive Derivative-Free Optimization (p. 13); C.3.2 Robot Policy and Controller (p. 13); B Energy-Based Model Training and Implicit Inference Details (p. 14); B.1 Method with Derivative-Free Optimization (p. 14); B.2 Method with Autoregressive Derivative-Free Optimization (p. 15); C.3.2 Robot Policy and Controller (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | We use either a) a derivative-free (sampling-based) optimization procedure, b) an auto-regressive variant of the derivative-free optimizer which performs coordinate descent, or ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | Given a dataset of samples {xi,yi}, and regression bounds ymin,ymax ∈Rm, training consists of generating a set of negative counter-examples {˜yj i}Nneg. ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | Like many other supervised learning methods, BC policies are often represented by explicit continuous feed-forward models (e.g., deep networks) of the form ... | p. 1 (1 Introduction), p. 1 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** We use either a) a derivative-free (sampling-based) optimization procedure, b) an auto-regressive variant of the derivative-free optimizer which performs coordinate descent, or c) gradient-based Langevin ...
- **p. 2 / 1 Introduction - extractive body cue:** This loss equates to the negative log likelihood of pθ(y/x)= exp(-Eθ(x,y)) Z(x,θ) , and the counter-examples are used to estimate Z(xi,θ): LInfoNCE= N X i=1 ...
- **p. 3 / 1 Introduction - extractive body cue:** Instead of using argmin to identify a single optimal value, argmin may return a set of values, which may either be interpreted probabilistically as sampling ...
- **p. 1 / 1 Introduction - extractive body cue:** 1), and at inference time (given o) performs implicit regression by optimizing for the optimal action ˆa via sampling or gradient descent [11, 12].
- **p. 5 / 1 Introduction - extractive body cue:** By adding perhaps the simplest way to use reward information, if we prioritize sampling to be only the top 50% of demonstrations sorted by their ...
- **p. 1 / Abstract - extractive body cue:** We find these policies provide competitive results or outperform state-of-the-art offline reinforcement learning methods on the challenging human-expert tasks from the D4RL benchmark suite, despite ...
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Like, many, other, supervised, learning, methods, policies, often, represented, explicit, continuous, feed-forward, models, deep | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | Like, many, other, supervised, learning, methods, policies, often, represented, explicit | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | reformulate, implicit, models, specifically, composition, argmin, continuous, energy, function, Sec | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | either, derivative-free, sampling-based, optimization, procedure, auto-regressive, variant, optimizer, performs, coordinate | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive body cue:** Like many other supervised learning methods, BC policies are often represented by explicit continuous feed-forward models (e.g., deep networks) of the form ˆa=Fθ(o) that map ...
- **p. 1 / Abstract - extractive body cue:** On robotic policy learning tasks we show that implicit behavioral cloning policies with energy-based models (EBM) often outperform common explicit (Mean Square Error, or Mixture ...
- **p. 2 / 1 Introduction - extractive body cue:** (a) In contrast to explicit policies, implicit policies leverage parameterized energy functions that take both observations (e.g. images) and actions as inputs, and optimize for ...
- **p. 6 / 1 Introduction - extractive body cue:** In both cases, state observations as inputs do not perform well compared with image pixel inputs.
- **p. 6 / 1 Introduction - extractive body cue:** Perspective RGB images from a simulated camera are used as visual input, along with current end effector poses as state input.
- **p. 4 / 1 Introduction - extractive body cue:** Visual Generalization Of particular relevance to learning visuomotor policies, we also find striking differences in extrapolation ability with converting high-dimensional image inputs into continuous outputs.
- **p. 4 / 1 Introduction - extractive body cue:** Standard deviations are shown in Tables 2, 3, 4, 5, 6. image human unknown multimodal Benchmark input demos cardinality solutions D4RL Human-Experts    ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value was not selected from the PDF body. | The action space is 12DoF (6DoF Cartesian per arm), and each episode consists of 700 steps recorded at 10Hz. | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Results show that implicit models for BC exhibit the capacity to learn long-horizon, closed-loop visuomotor tasks better than their explicit counterparts - ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | The action space is 12DoF (6DoF Cartesian per arm), and each episode consists of 700 steps recorded at 10Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** We use either a) a derivative-free (sampling-based) optimization procedure, b) an auto-regressive variant of the derivative-free optimizer which performs coordinate descent, or c) gradient-based Langevin ...
- **p. 2 / 1 Introduction - extractive body cue:** Given a dataset of samples {xi,yi}, and regression bounds ymin,ymax ∈Rm, training consists of generating a set of negative counter-examples {˜yj i}Nneg. j=1 for each ...
- **p. 4 / 1 Introduction - extractive body cue:** 4 shows how on a simple visual coordinate regression task, which is a notoriously hard problem for convolutional networks [23], an MSE-trained Conv-MLP model [24] ...
- **p. 5 / 1 Introduction - extractive body cue:** N-D Particle Integrator is a simple environment with linear dynamics but where a discontinuous oracle policy is used to generate training demonstrations: once within the ...
- **p. 6 / 1 Introduction - extractive body cue:** Real-world robot results, success % shown is mean +/- std.dev (20 rollouts per seed, 3 seeds = 60 trials per method per task).
- **p. 1 / 1 Introduction - extractive body cue:** 1), and at inference time (given o) performs implicit regression by optimizing for the optimal action ˆa via sampling or gradient descent [11, 12].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** either, derivative-free, sampling-based, optimization, procedure, auto-regressive, variant, optimizer, performs, coordinate, descent, gradient-based, Langevin, sampling, gradient, penalty, loss, during, training, Appendix.
- **Relevant PDF headings:** B Energy-Based Model Training and Implicit Inference Details (p. 13); B.1 Method with Derivative-Free Optimization (p. 13); B.2 Method with Autoregressive Derivative-Free Optimization (p. 13); C.3.2 Robot Policy and Controller (p. 13); B Energy-Based Model Training and Implicit Inference Details (p. 14); B.1 Method with Derivative-Free Optimization (p. 14); B.2 Method with Autoregressive Derivative-Free Optimization (p. 15); C.3.2 Robot Policy and Controller (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | Real-world robot results, success % shown is mean +/- std.dev (20 rollouts per seed, 3 seeds = 60 trials per method per ... | p. 6 (1 Introduction), p. 7 (1 Introduction) |
| Policy fitting | Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations ... | p. 5 (Figure/Table caption), p. 1 (Abstract) |
| Closed-loop rollout | Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations ... | p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 1 Introduction - extractive body cue:** We evaluate implicit (EBM) and explicit (MSE and MDN [30, 31]) policies on both variants, trained from a dataset of 2,000 demonstrations using a scripted ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 3. Results on simulated xArm6 pushing tasks, average of 3 random seeds, 100 evaluations each, with ± std. dev. Simulated Pushing consists of a ...
- **p. 2 / 1 Introduction - extractive body cue:** Implicit models are able to approximate discontinuities sharply without introducing intermediate artifacts (Fig.
- **p. 2 / 1 Introduction - extractive body cue:** To demonstrate a breadth of approaches, we present results with three different EBM training and inference methods discussed below, however a comprehensive comparison of all ...
- **p. 3 / 1 Introduction - extractive body cue:** Once the training data is uncorrelated (i.e. random noise) and without regularization (Fig.
- **p. 7 / 1 Introduction - extractive body cue:** The red/green pushing tasks, including multi-modal variant (Fig.
- **p. 7 / 1 Introduction - extractive body cue:** This means that implicit functions can approximate steep or discontinuous explicit functions without large gradients in the function approximator that may cause generalization issues.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 6 (1 Introduction), p. 4 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 5 (1 Introduction), p. 1 (Abstract), temporal p. 6 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Like many other supervised learning methods, BC policies are often represented by explicit continuous feed-forward models (e.g., deep networks) of the form ˆa=Fθ(o) that map directly from input observations o ... (p. 1, 1 Introduction).
- **Objective/update evidence:** We use either a) a derivative-free (sampling-based) optimization procedure, b) an auto-regressive variant of the derivative-free optimizer which performs coordinate descent, or c) gradient-based Langevin sampling [11, 12] with gradient ... (p. 2, 1 Introduction).
- **Temporal/runtime evidence:** The action space is 12DoF (6DoF Cartesian per arm), and each episode consists of 700 steps recorded at 10Hz. (p. 6, 1 Introduction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
