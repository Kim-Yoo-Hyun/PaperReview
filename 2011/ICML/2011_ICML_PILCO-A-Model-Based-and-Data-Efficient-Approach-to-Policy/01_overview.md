# PILCO: A Model-Based and Data-Efficient Approach to Policy Search

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/2011/papers/323_icmlpaper.pdf.
> PDF retrieval source: https://www.deisenroth.cc/publication/deisenroth-2011-c/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2011 / ICML
- Authors: Marc Peter Deisenroth, Carl Edward Rasmussen
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning, model-based RL, Gaussian Process
- Official paper: https://icml.cc/2011/papers/323_icmlpaper.pdf
- Full-text retrieval: https://icml.cc/2011/papers/323_icmlpaper.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://icml.cc/2011/papers/323_icmlpaper.pdf) 기준이다.

## Why This Paper Is Here

PILCO는 적은 상호작용으로 제어를 학습하도록 확률적 동역학 모형의 불확실성을 장기 정책 평가에 전파한다. [PDF 1쪽](https://icml.cc/2011/papers/323_icmlpaper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce pilco, a practical, data-efficient model-based policy search method.
- **p. 1 / Abstract - extractive body cue:** Pilco reduces model bias, one of the key problems of model-based reinforcement learning, in a principled way.
- **p. 1 / Abstract - extractive body cue:** By learning a probabilistic dynamics model and explicitly incorporating model uncertainty into long-term planning, pilco can cope with very little data and facilitates learning from ...
- **p. 1 / Abstract - extractive body cue:** Policy evaluation is performed in closed form using state-ofthe-art approximate inference.
- **p. 1 / Abstract - extractive body cue:** Furthermore, policy gradients are computed analytically for policy improvement.
- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** (5) Throughout this paper, we consider a prior mean function m ≡0 and the squared exponential (SE) kernel k with automatic relevance determination.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce pilco, a practical, data-efficient model-based policy search method.
- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** Pilco's probabilistic dynamics model is implemented as a GP, where we use tuples (xt-1, ut-1) ∈RD+F as training inputs and differences ∆t = xt -xt-1 ...
- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search Algorithm 1 pilco 1: init: Sample controller parameters θ ∼N(0, I).
- **p. 2 / 2. Model-based Indirect Policy Search - extractive body cue:** In the following, we detail the key components of the pilco policy-search framework: the dynamics model, analytic approximate policy evaluation, and gradientbased policy improvement.
- **p. 3 / 2.1. Dynamics Model Learning - extractive body cue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search The posterior predictive distribution p(∆∗/˜x∗) for an arbitrary, but known, test input ˜x∗is Gaussian with mean ...
- **p. 5 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** 2: repeat 3: Learn probabilistic (GP) dynamics model, see Sec.
- **p. 3 / 2.2.1. Mean Prediction - extractive body cue:** (16) is the difference between the training input ˜xi and the mean of the "test" input distribution p(xt-1, ut-1).
- **p. 4 / 2.3. Analytic Gradients for Policy Improvement - extractive body cue:** (30), depend on the policy parametrization θ.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Policy evaluation is performed in closed form using state-ofthe-art approximate inference. | multi-view observation, language/task label과 action trajectory | p. 1 (Abstract), p. 3 (2.1. Dynamics Model Learning) |
| State/latent | Policy, evaluation, performed, closed, form, state-ofthe-art, approximate, inference, PILCO, Model-Based, Data-Efficient, Search | shared representation, embodiment/task identity와 data distribution | p. 1 (Abstract), p. 3 (2.1. Dynamics Model Learning), p. 1 (Abstract) |
| Output/action | PILCO: A Model-Based and Data-Efficient Approach to Policy Search The posterior predictive distribution p(∆∗/˜x∗) for an arbitrary, but known, test input ˜x∗is Gaussian with mean and variance mf(˜x∗) = Ef[∆∗] = k⊤ ... | dataset sample 또는 learned policy action | p. 3 (2.1. Dynamics Model Learning), p. 1 (Abstract), p. 2 (2. Model-based Indirect Policy Search) |
| Objective/outcome | Analytic derivatives allow for standard gradient-based non-convex optimization methods, e.g., CG or LBFGS, which return optimized policy parameters θ∗. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 4 (2.3. Analytic Gradients for Policy Improvement), p. 2 (2. Model-based Indirect Policy Search) |

## Main Claims and Actual Contribution

- 가우시안 과정으로 상태 전이를 학습하고 예측 상태 분포의 모멘트로 장기 비용과 정책 기울기를 근사 계산한다. [PDF 2쪽](https://icml.cc/2011/papers/323_icmlpaper.pdf#page=2) · [PDF 3쪽](https://icml.cc/2011/papers/323_icmlpaper.pdf#page=3) · [PDF 4쪽](https://icml.cc/2011/papers/323_icmlpaper.pdf#page=4)
- 카트폴 등 제어 과제에서 제한된 자료로 정책을 갱신하고 실제 장치에서 학습에 필요한 상호작용을 측정했다. [PDF 5쪽](https://icml.cc/2011/papers/323_icmlpaper.pdf#page=5) · [PDF 6쪽](https://icml.cc/2011/papers/323_icmlpaper.pdf#page=6) · [PDF 7쪽](https://icml.cc/2011/papers/323_icmlpaper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (3.3. Unicycle Riding), p. 2 (Figure/Table caption) |
| Embodiment/environment | In this section, we report pilco's success in efficiently learning challenging control tasks, including both standard benchmark problems and high-dimensional control problems. | hardware/simulator version and reset protocol | p. 5 (3. Experimental Results), p. 6 (3.3. Unicycle Riding) |
| Dataset/benchmark | Pilco successfully learned a sufficiently good dynamics model and a good controller for this standard benchmark problem fully automatically in only a handful of trials and a total experience of 17.5 s. | role, split, size and leakage | p. 5 (3. Experimental Results), p. 6 (3.3. Unicycle Riding), p. 5 (3.1. Cart-Pole Swing-up), p. 6 (3.3. Unicycle Riding) |
| Metric | The success rate was approximately 93%; bringing the unicycle upright from extreme initial configurations was sometimes impossible due to the torque constraints. | definition, denominator, direction and uncertainty | p. 6 (3.3. Unicycle Riding), p. 6 (3.3. Unicycle Riding), p. 3 (2.2. Policy Evaluation) |
| Baseline/ablation | In the following, we compare pilco's data efficiency (required interaction time) to other RL methods that learn previously discussed tasks from scratch, i.e., without informative prior knowledge. | fair input/data/compute/action matching | p. 6 (3.4. Data Efficiency), p. 6 (3.4. Data Efficiency) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4. Discussion and Conclusion - extractive body cue:** Hence, pilco's unprecedented data efficiency cannot solely be attributed to any kind of reward shaping.
- **p. 7 / 4. Discussion and Conclusion - extractive body cue:** Trial-and-error learning leads to some limitations in the discovered policy: Pilco is not an optimal control method; it merely finds a solution for the task.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** The goal was to ride the unicycle, i.e., to prevent it from falling.
- **p. 6 / 3.3. Unicycle Riding - extractive body cue:** After 1.2 s, either the unicycle had fallen or the learned controller had managed to balance it very closely to the desired upright position.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Abstract), p. 2 (2.1. Dynamics Model Learning), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 2 (2. Model-based Indirect Policy Search)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Pilco reduces model bias, one of the key problems of model-based reinforcement learning, in a principled way. (p. 1, Abstract).
- **Actual contribution:** In this paper, we introduce pilco, a practical, data-efficient model-based policy search method. (p. 1, Abstract).
- **Evaluation boundary:** Robotic unicycle system and simulation results. (p. 6, 3.3. Unicycle Riding).
- **Explicit failure boundary:** Trial-and-error learning leads to some limitations in the discovered policy: Pilco is not an optimal control method; it merely finds a solution for the task. (p. 7, 4. Discussion and Conclusion).
