# A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ri.cmu.edu/publications/a-reduction-of-imitation-learning-and-structured-prediction-to-no-regret-online-learning/.
> PDF retrieval source: https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2011 / AISTATS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Imitation Learning, policy learning
- Official paper: https://www.ri.cmu.edu/publications/a-reduction-of-imitation-learning-and-structured-prediction-to-no-regret-online-learning/
- Full-text retrieval: https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 The interaction between policy and the resulting distribution makes optimization difficult as it results in a non-convex objective even if the loss ℓ(s, ·) is convex in π for all states s.를 문제로 두고, We propose a new meta-algorithm for imitation learning which learns a stationary deterministic policy guaranteed to perform well under its induced distribution of states (number of mistakes/costs that grows linearly in T ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), violate the common i.i.d. assumptions made in statistical learning.
- **p. 1 / Abstract - extractive body cue:** This leads to poor performance in theory and often in practice.
- **p. 1 / Abstract - extractive body cue:** Some recent approaches (Daumé III et al., 2009; Ross and Bagnell, 2010) provide stronger guarantees in this setting, but remain somewhat unsatisfactory as they train ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in ...
- **p. 1 / Abstract - extractive body cue:** We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations ...
- **p. 2 / 2 PRELIMINARIES - extractive body cue:** The interaction between policy and the resulting distribution makes optimization difficult as it results in a non-convex objective even if the loss ℓ(s, ·) is ...
- **p. 2 / 2 PRELIMINARIES - extractive body cue:** Our goal is to find a policy ˆπ which minimizes the observed surrogate loss under its induced distribution of states, i.e.: ˆπ = arg min ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose a new meta-algorithm for imitation learning which learns a stationary deterministic policy guaranteed to perform well under its induced distribution of states (number ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We take a reduction-based approach (Beygelzimer et al., 2005) that enables reusing existing supervised learning algorithms.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in ...
- **p. 1 / Abstract - extractive body cue:** We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations ...
- **p. 4 / 2 PRELIMINARIES - extractive body cue:** We show below the only requirement is that {βi} be a sequence such that βN = 1 N PN i=1 βi →0 as N →∞.
- **p. 2 / 2 PRELIMINARIES - extractive body cue:** The interaction between policy and the resulting distribution makes optimization difficult as it results in a non-convex objective even if the loss ℓ(s, ·) is ...
- **p. 3 / 2 PRELIMINARIES - extractive body cue:** Hence the forward algorithm guarantees that the expected loss under the distribution of states induced by the learned policy matches the average loss during training, ...
- **p. 3 / 2 PRELIMINARIES - extractive body cue:** Let Qπ′ t (s, π) denote the t-step cost of executing π in initial state s and then following policy π′ and assume ℓ(s, π) ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | However since the learner's prediction affects future input observations/states during execution of the learned policy, this violate the crucial i.i.d. assumption made by most statistical learning approaches. | observation history와 expert trajectory/action | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| State/latent | However, since, learner, prediction, affects, future, input, observations/states, during, execution, learned, policy | behavior policy와 temporal action context | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (2 PRELIMINARIES) |
| Output/action | A typical approach to imitation learning is to train a classifier or regressor to predict an expert's behavior given training data of the encountered observations (input) and actions (output) performed by the ... | predicted action 또는 action chunk | p. 1 (1 INTRODUCTION), p. 2 (2 PRELIMINARIES), p. 5 (2 PRELIMINARIES) |
| Objective/outcome | It finds the policy ˆπsup: ˆπsup = arg min π∈Π Es∼dπ∗[ℓ(s, π)] (2) Assuming ℓ(s, π) is the 0-1 loss (or upper bound on the 01 loss) implies the following performance guarantee ... | imitation error, task success, robustness와 compounding error | p. 2 (2 PRELIMINARIES), p. 2 (2 PRELIMINARIES), p. 4 (2 PRELIMINARIES) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose a new meta-algorithm for imitation learning which learns a stationary deterministic policy guaranteed to perform well under its induced distribution of states (number ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We take a reduction-based approach (Beygelzimer et al., 2005) that enables reusing existing supervised learning algorithms.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in ...
- **p. 1 / Abstract - extractive body cue:** We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations ...
- **p. 4 / 2 PRELIMINARIES - extractive body cue:** We show below the only requirement is that {βi} be a sequence such that βN = 1 N PN i=1 βi →0 as N →∞.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Though even after 5 iterations, the policy we obtain almost never falls off the track and is significantly outperforming both SMILe and the baseline supervised ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** DAgger (βi = I(i=1)) SMILe (α = 0.1) Supervised Figure 2: Average falls/lap as a function of training data. supervised approach where training always occurs ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The baseline result without structure achieves 82% character accuracy by just using an SVM that predicts each character independently.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Embodiment/environment | We use the dataset of Taskar et al. | hardware/simulator version and reset protocol | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Dataset/benchmark | A human expert is used to provide demonstrations of the correct steering (analog joystick value in [-1,1]) for each of the observed game images. | role, split, size and leakage | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Metric | Figure 4: Average distance/stage as a function of data. approach, performance stagnates as we collect more data from the expert demonstrations, as this does not help the particular errors the learned controller ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Baseline/ablation | Though even after 5 iterations, the policy we obtain almost never falls off the track and is significantly outperforming both SMILe and the baseline supervised approach. | fair input/data/compute/action matching | p. 6 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5 EXPERIMENTS - extractive body cue:** DAgger (βi = I(i=1)) SMILe (α = 0.1) Supervised Figure 2: Average falls/lap as a function of training data. supervised approach where training always occurs ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** We measure performance in terms of the average number of falls per lap.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Andrew Bagnell ing being hit by enemies and falling into gaps, and before running out of time.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** DAgger (βi=I(i=1)) SEARN (α=1) SEARN (α=0.8) SEARN (α=0.1) SMILe (α=0.1) Supervised No Structure Figure 5: Character accuracy as a function of iteration. predicted character feature) ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** D0 D0.5 D0.9 Se1 Se0.4 Sm0.1 Sup Figure 4: Average distance/stage as a function of data. approach, performance stagnates as we collect more data from ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 6 FUTURE WORK We show that by batching over iterations of interaction with a system, no-regret methods, including the presented DAGGER approach can provide a ...

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 The interaction between policy and the resulting distribution makes optimization difficult as it results in a non-convex objective even if the loss ℓ(s, ·) is convex in π for all states s.를 문제로 두고, We propose a new meta-algorithm for imitation learning which learns a stationary deterministic policy guaranteed to perform well under its induced distribution of states (number of mistakes/costs that grows linearly in T ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (2 PRELIMINARIES), p. 2 (2 PRELIMINARIES), p. 3 (2 PRELIMINARIES), p. 1 (1 INTRODUCTION), p. 3 (2 PRELIMINARIES), p. 2 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Sequence Prediction problems arise commonly in practice. (p. 1, 1 INTRODUCTION).
- **Actual contribution:** We take a reduction-based approach (Beygelzimer et al., 2005) that enables reusing existing supervised learning algorithms. (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** The baseline result without structure achieves 82% character accuracy by just using an SVM that predicts each character independently. (p. 8, 5 EXPERIMENTS).
- **Explicit failure boundary:** We measure performance in terms of the average number of falls per lap. (p. 6, 5 EXPERIMENTS).
