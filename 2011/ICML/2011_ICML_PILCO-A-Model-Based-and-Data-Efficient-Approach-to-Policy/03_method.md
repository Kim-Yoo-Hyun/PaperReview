# Method - PILCO: A Model-Based and Data-Efficient Approach to Policy Search

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.deisenroth.cc/publication/deisenroth-2011-c/; PDF retrieval source: https://www.deisenroth.cc/publication/deisenroth-2011-c/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (2.1. Dynamics Model Learning), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 2 (2. Model-based Indirect Policy Search), p. 3 (2.1. Dynamics Model Learning), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 3 (2.2.1. Mean Prediction)): Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t = xt -xt-1 + ε ∈RD, ε ∼N(0, ...

## Method Body Digest

- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t = xt -xt-1 ...
- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search Algorithm 1 pilco 1: init: Sample controller parameters θ ∼N(0, I).
- **p. 2 / 2. Model-based Indirect Policy Search - extractive body cue:** In the following, we detail the key components of the pilco policy-search framework: the dynamics model, analytic approximate policy evaluation, and gradientbased policy improvement.
- **p. 3 / 2.1. Dynamics Model Learning - extractive body cue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search The posterior predictive distribution p(∆∗/˜x∗) for an arbitrary, but known, test input ˜x∗is Gaussian with mean ...
- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** 2: repeat 3: Learn probabilistic (GP) dynamics model, see Sec.
- **p. 3 / 2.2.1. Mean Prediction - extractive body cue:** (16) is the difference between the training input ˜xi and the mean of the "test" input distribution p(xt-1, ut-1).
- **p. 4 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** (30), depend on the policy parametrization θ.
- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** Analytic derivatives allow for standard gradient-based non-convex optimization methods, e.g., CG or LBFGS, which return optimized policy parameters θ∗.

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce pilco, a practical, data-efficient model-based policy search method.

## Source Evidence Cues

- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t = xt -xt-1 ...
- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search Algorithm 1 pilco 1: init: Sample controller parameters θ ∼N(0, I).
- **p. 2 / 2. Model-based Indirect Policy Search - extractive body cue:** In the following, we detail the key components of the pilco policy-search framework: the dynamics model, analytic approximate policy evaluation, and gradientbased policy improvement.
- **p. 3 / 2.1. Dynamics Model Learning - extractive body cue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search The posterior predictive distribution p(∆∗/˜x∗) for an arbitrary, but known, test input ˜x∗is Gaussian with mean ...
- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** 2: repeat 3: Learn probabilistic (GP) dynamics model, see Sec.
- **p. 3 / 2.2.1. Mean Prediction - extractive body cue:** (16) is the difference between the training input ˜xi and the mean of the "test" input distribution p(xt-1, ut-1).
- **p. 4 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** (30), depend on the policy parametrization θ.
- **Detected method headings:** 2. Model-based Indirect Policy Search (p. 2); 2.1. Dynamics Model Learning (p. 2); 2.2. Policy Evaluation (p. 3); 2.3. Analytic Gradients for Policy Improvement (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t ... | p. 2 (2.1. Dynamics Model Learning), p. 5 (2.3. Analytic Gradients for Policy Improvement) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | PILCO: A Model-Based and Data-Efficient Approach to Policy Search Algorithm 1 pilco 1: init: Sample controller parameters θ ∼N(0, I). | p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 2 (2. Model-based Indirect Policy Search) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | In the following, we detail the key components of the pilco policy-search framework: the dynamics model, analytic approximate policy evaluation, and gradientbased ... | p. 2 (2. Model-based Indirect Policy Search), p. 3 (2.1. Dynamics Model Learning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** Analytic derivatives allow for standard gradient-based non-convex optimization methods, e.g., CG or LBFGS, which return optimized policy parameters θ∗.
- **p. 4 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** Hence, we can analytically compute the gradients of the expected return Jπ with respect to the policy parameters θ, which we sketch in the following.
- **p. 2 / 2. Model-based Indirect Policy Search - extractive body cue:** In the following, we detail the key components of the pilco policy-search framework: the dynamics model, analytic approximate policy evaluation, and gradientbased policy improvement.
- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** Given n training inputs ˜X = [˜x1, . . . , ˜xn] and corresponding training targets y = [∆1, . . . , ∆n]⊤, the ...
- **p. 4 / 2.2.2. Covariance Matrix of the Prediction - extractive body cue:** We assume that the cost c is chosen so that Eq.
- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** Analytic gradient computation of Jπ is much more efficient than estimating policy gradients through sampling: For the latter, the variance in the gradient estimate grows ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 2 (2. Model-based Indirect Policy Search), p. 4 (2.3. Analytic Gradients for Policy Improvement), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 5 (2.3. Analytic Gradients for Policy Improvement).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Policy, evaluation, performed, closed, form, state-ofthe-art, approximate, inference, PILCO, Model-Based, Data-Efficient, Search, posterior, predictive | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Policy, evaluation, performed, closed, form, state-ofthe-art, approximate, inference, PILCO, Model-Based | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | introduce, pilco, practical, data-efficient, model-based, policy, search, evaluation, performed, closed | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Analytic, derivatives, allow, standard, gradient-based, non-convex, optimization, methods, LBFGS, return | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** Policy evaluation is performed in closed form using state-ofthe-art approximate inference.
- **p. 3 / 2.1. Dynamics Model Learning - extractive body cue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search The posterior predictive distribution p(∆∗/˜x∗) for an arbitrary, but known, test input ˜x∗is Gaussian with mean ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, policy gradients are computed analytically for policy improvement.
- **p. 2 / 2. Model-based Indirect Policy Search - extractive body cue:** In the following, we detail the key components of the pilco policy-search framework: the dynamics model, analytic approximate policy evaluation, and gradientbased policy improvement.
- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t = xt -xt-1 ...
- **p. 3 / 2.1. Dynamics Model Learning - extractive body cue:** For uncertain inputs, the target dimensions covary.
- **p. 4 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** (30), depend on the policy parametrization θ.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | (27) is known from time step t -1 and ∂µt/∂p(xt-1) is computed by applying the chain-rule to Eqs. | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | To obtain the state distributions p(x1), . . . , p(xT ), we cascade onestep predictions, see Eqs. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | To solve the swing-up plus balancing, pilco required only 17.5 s of interaction with the physical system. frame flywheel wheel (a) Robotic ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t = xt -xt-1 ...
- **p. 3 / 2.2.1. Mean Prediction - extractive body cue:** (16) is the difference between the training input ˜xi and the mean of the "test" input distribution p(xt-1, ut-1).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Pilco, probabilistic, dynamics, model, implemented, where, tuples, xt-1, ut-1, training, inputs, differences, diag, targets, Model-Based, Data-Efficient, Policy, Search, Algorithm, init.
- **Relevant PDF headings:** 2. Model-based Indirect Policy Search (p. 2); 2.1. Dynamics Model Learning (p. 2); 2.2. Policy Evaluation (p. 3); 2.3. Analytic Gradients for Policy Improvement (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | In this section, we report pilco's success in efficiently learning challenging control tasks, including both standard benchmark problems and high-dimensional control problems. | p. 5 (3. Experimental Results), p. 6 (3.3. Unicycle Riding) |
| Coverage / augmentation | In the following, we compare pilco's data efficiency (required interaction time) to other RL methods that learn previously discussed tasks from scratch, ... | p. 6 (3.4. Data Efficiency), p. 6 (3.4. Data Efficiency) |
| Downstream learning interface | The success rate was approximately 93%; bringing the unicycle upright from extreme initial configurations was sometimes impossible due to the torque constraints. | p. 6 (3.3. Unicycle Riding), p. 2 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 3.4. Data Efficiency - extractive body cue:** In the following, we compare pilco's data efficiency (required interaction time) to other RL methods that learn previously discussed tasks from scratch, i.e., without informative ...
- **p. 7 / 4. Discussion and Conclusion - extractive body cue:** Hence, pilco's unprecedented data efficiency cannot solely be attributed to any kind of reward shaping.
- **p. 7 / 4. Discussion and Conclusion - extractive body cue:** Trial-and-error learning leads to some limitations in the discovered policy: Pilco is not an optimal control method; it merely finds a solution for the task.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** The goal was to ride the unicycle, i.e., to prevent it from falling.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** After 1.2 s, either the unicycle had fallen or the learned controller had managed to balance it very closely to the desired upright position.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (2.1. Dynamics Model Learning), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 2 (2. Model-based Indirect Policy Search), p. 3 (2.1. Dynamics Model Learning), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 3 (2.2.1. Mean Prediction), objective p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 4 (2.3. Analytic Gradients for Policy Improvement), p. 2 (2. Model-based Indirect Policy Search), p. 2 (2.1. Dynamics Model Learning), p. 4 (2.2.2. Covariance Matrix of the Prediction), p. 5 (2.3. Analytic Gradients for Policy Improvement), temporal p. 4 (2.3. Analytic Gradients for Policy Improvement), p. 3 (2.2. Policy Evaluation), p. 5 (3.1. Cart-Pole Swing-up), p. 5 (3.2. Cart-Double-Pendulum Swing-up), p. 6 (3.3. Unicycle Riding), p. 6 (3.3. Unicycle Riding).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
