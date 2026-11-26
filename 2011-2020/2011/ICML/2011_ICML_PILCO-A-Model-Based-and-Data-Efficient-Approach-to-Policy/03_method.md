# Method - PILCO: A Model-Based and Data-Efficient Approach to Policy Search

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://icml.cc/2011/papers/323_icmlpaper.pdf; PDF retrieval source: https://www.deisenroth.cc/publication/deisenroth-2011-c/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

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

상태·행동·관측된 다음 상태 → 가우시안 과정 동역학과 미래 상태 분포 → 기대 장기 비용으로 갱신한 피드백 정책. [방법·평가의 원문 근거](./01_overview.md#observation-state-and-output-interface)

## Objective / Update Rule

- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** Analytic derivatives allow for standard gradient-based non-convex optimization methods, e.g., CG or LBFGS, which return optimized policy parameters θ∗.
- **p. 4 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** Hence, we can analytically compute the gradients of the expected return Jπ with respect to the policy parameters θ, which we sketch in the following.
- **p. 2 / 2. Model-based Indirect Policy Search - extractive body cue:** In the following, we detail the key components of the pilco policy-search framework: the dynamics model, analytic approximate policy evaluation, and gradientbased policy improvement.
- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** Given n training inputs ˜X = [˜x1, . . . , ˜xn] and corresponding training targets y = [∆1, . . . , ∆n]⊤, the ...
- **p. 4 / 2.2.2. Covariance Matrix of the Prediction - extractive body cue:** We assume that the cost c is chosen so that Eq.
- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** Analytic gradient computation of Jπ is much more efficient than estimating policy gradients through sampling: For the latter, the variance in the gradient estimate grows ...
- **Formal bridge:** 상태·행동·관측된 다음 상태 → 가우시안 과정 동역학과 미래 상태 분포 → 기대 장기 비용으로 갱신한 피드백 정책.
- **Equation/algorithm anchors:** p. 2 (2. Model-based Indirect Policy Search), p. 4 (2.3. Analytic Gradients for Policy Improvement), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 5 (2.3. Analytic Gradients for Policy Improvement).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Policy, evaluation, performed, closed, form, state-ofthe-art, approximate, inference, PILCO, Model-Based, Data-Efficient, Search, posterior, predictive | 상태·행동·관측된 다음 상태 | body cue; exact tensor/frame verify |
| State/latent | Policy, evaluation, performed, closed, form, state-ofthe-art, approximate, inference, PILCO, Model-Based | 가우시안 과정 동역학과 미래 상태 분포 | body cue; notation verify |
| Action/output | introduce, pilco, practical, data-efficient, model-based, policy, search, evaluation, performed, closed | 기대 장기 비용으로 갱신한 피드백 정책 | body cue; unit/decoder verify |
| Objective/constraint | Analytic, derivatives, allow, standard, gradient-based, non-convex, optimization, methods, LBFGS, return | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** Policy evaluation is performed in closed form using state-ofthe-art approximate inference.
- **p. 3 / 2.1. Dynamics Model Learning - extractive body cue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search The posterior predictive distribution p(∆∗/˜x∗) for an arbitrary, but known, test input ˜x∗is Gaussian with mean ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, policy gradients are computed analytically for policy improvement.
- **p. 2 / 2. Model-based Indirect Policy Search - extractive body cue:** In the following, we detail the key components of the pilco policy-search framework: the dynamics model, analytic approximate policy evaluation, and gradientbased policy improvement.
- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t = xt -xt-1 ...
- **p. 3 / 2.1. Dynamics Model Learning - extractive body cue:** For uncertain inputs, the target dimensions covary.
- **p. 4 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** (30), depend on the policy parametrization θ.
- **Normalized interface:** observation=상태·행동·관측된 다음 상태; state=가우시안 과정 동역학과 미래 상태 분포; output/action=기대 장기 비용으로 갱신한 피드백 정책.

## Temporal and Runtime Contract

| Contract | PDF body cue | Unresolved detail |
|---|---|---|
| Horizon | (27) is known from time step t -1 and ∂µt/∂p(xt-1) is computed by applying the chain-rule to Eqs. | episode/sequence/action-chunk boundary |
| Rate / latency | To obtain the state distributions p(x1), . . . , p(xT ), we cascade onestep predictions, see Eqs. | Hz/fps, inference time and control rate |
| Memory | not stated or recoverable in the selected PDF body | window and reset |
| Compute | To solve the swing-up plus balancing, pilco required only 17.5 s of interaction with the physical system. frame flywheel wheel (a) Robotic ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t = xt -xt-1 ...
- **p. 3 / 2.2.1. Mean Prediction - extractive body cue:** (16) is the difference between the training input ˜xi and the mean of the "test" input distribution p(xt-1, ut-1).

## Method-Specific Formal Details

- **Body-defined terms:** Pilco, probabilistic, dynamics, model, implemented, where, tuples, xt-1, ut-1, training, inputs, differences, diag, targets, Model-Based, Data-Efficient, Policy, Search, Algorithm, init.
- **Relevant PDF headings:** 2. Model-based Indirect Policy Search (p. 2); 2.1. Dynamics Model Learning (p. 2); 2.2. Policy Evaluation (p. 3); 2.3. Analytic Gradients for Policy Improvement (p. 4).

## Evaluation Link

| 평가 근거 | 원문에서 추출한 내용 | 원문 위치 |
|---|---|---|
| 원문 대조 | In this section, we report pilco's success in efficiently learning challenging control tasks, including both standard benchmark problems and high-dimensional control problems. | p. 5 (3. Experimental Results), p. 6 (3.3. Unicycle Riding) |
| 원문 대조 | In the following, we compare pilco's data efficiency (required interaction time) to other RL methods that learn previously discussed tasks from scratch, ... | p. 6 (3.4. Data Efficiency), p. 6 (3.4. Data Efficiency) |
| 원문 대조 | The success rate was approximately 93%; bringing the unicycle upright from extreme initial configurations was sometimes impossible due to the torque constraints. | p. 6 (3.3. Unicycle Riding), p. 2 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 3.4. Data Efficiency - extractive body cue:** In the following, we compare pilco's data efficiency (required interaction time) to other RL methods that learn previously discussed tasks from scratch, i.e., without informative ...
- **p. 7 / 4. Discussion and Conclusion - extractive body cue:** Hence, pilco's unprecedented data efficiency cannot solely be attributed to any kind of reward shaping.
- **p. 7 / 4. Discussion and Conclusion - extractive body cue:** Trial-and-error learning leads to some limitations in the discovered policy: Pilco is not an optimal control method; it merely finds a solution for the task.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** The goal was to ride the unicycle, i.e., to prevent it from falling.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** After 1.2 s, either the unicycle had fallen or the learned controller had managed to balance it very closely to the desired upright position.

## Reproduction Checklist

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (2.1. Dynamics Model Learning), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 2 (2. Model-based Indirect Policy Search), p. 3 (2.1. Dynamics Model Learning), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 3 (2.2.1. Mean Prediction), objective p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 4 (2.3. Analytic Gradients for Policy Improvement), p. 2 (2. Model-based Indirect Policy Search), p. 2 (2.1. Dynamics Model Learning), p. 4 (2.2.2. Covariance Matrix of the Prediction), p. 5 (2.3. Analytic Gradients for Policy Improvement), temporal p. 4 (2.3. Analytic Gradients for Policy Improvement), p. 3 (2.2. Policy Evaluation), p. 5 (3.1. Cart-Pole Swing-up), p. 5 (3.2. Cart-Double-Pendulum Swing-up), p. 6 (3.3. Unicycle Riding), p. 6 (3.3. Unicycle Riding).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t = xt -xt-1 + ε ∈RD, ε ∼N(0, ... (p. 2, 2.1. Dynamics Model Learning).
- **Objective/update evidence:** Analytic derivatives allow for standard gradient-based non-convex optimization methods, e.g., CG or LBFGS, which return optimized policy parameters θ∗. (p. 5, 2.3. Analytic Gradients for Policy Improvement).
- **Temporal/runtime evidence:** To obtain the state distributions p(x1), . . . , p(xT ), we cascade onestep predictions, see Eqs. (p. 3, 2.2. Policy Evaluation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
