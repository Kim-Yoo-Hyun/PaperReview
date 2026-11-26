# Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1007/BF00992696.
> PDF retrieval source: https://doi.org/10.1007/BF00992696. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1992 / Machine Learning
- Authors: Ronald J. Williams
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Reinforcement Learning, Policy Gradient, REINFORCE
- Official paper: https://doi.org/10.1007/BF00992696
- Full-text retrieval: https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf) 기준이다.

## Why This Paper Is Here

Williams의 REINFORCE는 확률적 출력을 갖는 신경망에서 표집한 강화 신호로 기대 보상을 높이는 방향의 매개변수 갱신을 유도한다. [PDF 1쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=1)

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** The general framework of reinforcement learning encompasses a broad variety of problems ranging from various forms of function optimization at one extreme to learning control ...
- **p. 1 / 1. Introduction - extractive body cue:** While research in these individual areas tends to emphasize different sets of issues in isolation, it is likely that effective reinforcement learning techniques for autonomous ...
- **p. 1 / 1. Introduction - extractive body cue:** Thus while it remains a useful research strategy to focus on limited forms of reinforcement learning problems simply to keep the problems tractable, it is ...
- **p. 1 / 1. Introduction - extractive body cue:** In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output ...
- **p. 1 / 1. Introduction - extractive body cue:** While delayed reinforcement tasks are obviously important and are receiving much-deserved attention lately, a widely used approach to developing algorithms for such tasks is to ...
- **p. 2 / 1. Introduction - extractive body cue:** While such algorithms are known to have a number of limitations, there are a number of reasons why their study can be useful.
- **p. 2 / 1. Introduction - extractive body cue:** Also, to the extent that certain existing algorithms resemble the algorithms arising from such a gradient analysis, our understanding of them may be enhanced.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output ...
- **p. 2 / 1. Introduction - extractive body cue:** The results to be presented apply in general to any learner whose inputoutput mappings consists of a parameterized input-controlled distribution function from which outputs are ...
- **p. 8 / 5. Episodic REINFORCE algorithms - extractive body cue:** In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which the units may ...
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** For example, if the network consists of Bernoulli-logistic units an episodic REINFORCE algorithm would prescribe weight changes according to the rule k Awij = c~ij(r ...
- **p. 1 / 1. Introduction - extractive body cue:** While delayed reinforcement tasks are obviously important and are receiving much-deserved attention lately, a widely used approach to developing algorithms for such tasks is to ...
- **p. 8 / 4. REINFORCE algorithms - extractive body cue:** As a particular example, for a network of Bernoulli-logistic units one may use the learning rule Awij = a(r - ?)(Yi - Pi) xj, (9) ...
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** One way to create a statistical gradient-following algorithm for this case is to simply replace r in (11) by E~= 1 r(t), but it is ...
- **p. 7 / 4. REINFORCE algorithms - extractive body cue:** Thus AR-b when applied to a network of Bernoulli-logistic units, is a REINFORCE algorithm.

## Observation, State, and Output Interface

확률적 뉴런에서 행동 로그확률의 도함수와 기준값을 뺀 강화 신호로 기대 보상의 기울기를 추정한다. 이진 및 가우시안 출력과 지연 보상을 다룬다. [PDF 5쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=5) · [PDF 7쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=7)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The results to be presented apply in general to any learner whose inputoutput mappings consists of a parameterized input-controlled distribution function from which outputs are randomly generated, and the corresponding algorithms modify ... | 네트워크 입력·표집한 출력·강화 신호 | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | presented, apply, general, learner, whose, inputoutput, mappings, consists, parameterized, input-controlled, distribution, function | 출력 확률의 점수함수와 기준값 | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output mapping, and, with one limited exception, that ... | 가중치에 대한 확률적 기울기 갱신 | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 8 (5. Episodic REINFORCE algorithms) |
| Objective/outcome | If k = 0, this is called the associative reward-inaction (AR_I) algorithm, and we see that the learning rule reduces to equation (8) in this case. | 기대 강화 신호와 기대 갱신 방향의 관계 | p. 7 (4. REINFORCE algorithms), p. 6 (4. REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms) |

## Main Claims and Actual Contribution

- 출력 확률의 로그 도함수와 기준값을 뺀 강화 신호를 결합하고 갱신의 기댓값이 기울기와 갖는 관계를 보인다. [PDF 4쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=4) · [PDF 5쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=5) · [PDF 6쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=6)
- 이진 및 가우시안 확률 단위에 적용하는 예와 지연된 보상을 다루기 위한 적격도 누적 방식을 제시한다. [PDF 7쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=7) · [PDF 8쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=8) · [PDF 9쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=9) · [PDF 10쪽](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 17 (8. Algorithm performance and other issues), p. 15 (8. Algorithm performance and other issues) |
| Embodiment/environment | A more general formulation of such an episodic learning task is also possible, where reinforcement is delivered to the network at each time step during the episode, not just at the end. | hardware/simulator version and reset protocol | p. 9 (5. Episodic REINFORCE algorithms), p. 15 (8. Algorithm performance and other issues) |
| Dataset/benchmark | Roughly, the idea is to treat this learning problem over the k-time-step interval as k different but overlapping episodic learning problems, all starting at the beginning of the episode. | role, split, size and leakage | p. 9 (5. Episodic REINFORCE algorithms), p. 15 (8. Algorithm performance and other issues), p. 9 (5. Episodic REINFORCE algorithms), p. 15 (8. Algorithm performance and other issues) |
| Metric | One potentially useful feature of such a Gaussian unit is that the mean and variance of its output are individually controllable as long as separate weights (or perhaps inputs) are used to ... | definition, denominator, direction and uncertainty | p. 10 (6. REINFORCE with multiparameter distributions), p. 17 (8. Algorithm performance and other issues), p. 10 (6. REINFORCE with multiparameter distributions) |
| Baseline/ablation | In these studies, REINFORCE with reinforcement comparison was found to outperform all other algorithms investigated. | fair input/data/compute/action matching | p. 15 (8. Algorithm performance and other issues), p. 17 (8. Algorithm performance and other issues), p. 9 (5. Episodic REINFORCE algorithms) |

## Explicit Limitations and Failure Boundary

- **p. 15 / 8. Algorithm performance and other issues - extractive body cue:** 8.L Convergence properties A major limitation of the analysis performed here is that it does not immediately lead to prediction of the asymptotic properties of ...
- **p. 14 / 7.2. Backpropagating through random number generators - extractive body cue:** Unfortunately, even this property fails to hold in general.
- **p. 17 / 8. Algorithm performance and other issues - extractive body cue:** Choice of reinforcement baseline One important limitation of the analysis given here is that it offers no basis for choosing among various choices of reinforcement ...
- **p. 19 / 8.5. Use of other local gradient estimates - extractive body cue:** REINFORCE fails to be model-based even in this local sense, but it may be worthwhile to consider algorithms that do attempt to generate more explicit ...
- **p. 22 / 1 Og i - extractive body cue:** OWij gi OWij Although this fails to be defined when gi = 0, it will still be the case that Awij is welldefined for any ...
- **p. 22 / 1 Og i - extractive body cue:** Then E{Awij I W, x i} = Z E{Awijl W, x i, Yi = ~} Pr{yi = ~ I W, x i} ~Y~ --- ~i ...
- **p. 23 / 1 Og i - extractive body cue:** This means that Pr {x z = x ] W} does not depend on w6, so the result follows by differentiating both sides of this ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 9 (5. Episodic REINFORCE algorithms), p. 8 (5. Episodic REINFORCE algorithms)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** The general framework of reinforcement learning encompasses a broad variety of problems ranging from various forms of function optimization at one extreme to learning control at the other. (p. 1, 1. Introduction).
- **Actual contribution:** In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output mapping, and, with one limited ... (p. 1, 1. Introduction).
- **Evaluation boundary:** Dayan's simulation results seem to suggest that use of such a reinforcement baseline offers 21 (p. 17, 8. Algorithm performance and other issues).
- **Explicit failure boundary:** 8.L Convergence properties A major limitation of the analysis performed here is that it does not immediately lead to prediction of the asymptotic properties of REINFORCE algorithms. (p. 15, 8. Algorithm performance and other issues).
