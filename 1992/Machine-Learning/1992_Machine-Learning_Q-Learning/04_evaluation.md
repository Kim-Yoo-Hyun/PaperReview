# Evaluation - Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00992698; PDF retrieval source: https://doi.org/10.1007/BF00992698. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem), p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem)): Given e > O, choose s such that .ys__ < 1-3` T By B.3, with probability 1, it is possible to choose l sufficiently large such that for n > ...

## Evaluation Body Digest

- **p. 4 / 3. The convergence proof - extractive body cue:** First, all the cards for episodes later than n are eliminated, leaving just a finite deck.
- **p. 5 / 3.1. Lemmas - extractive body cue:** The proof proceeds by backwards induction, following the AFIP down through the stack of past episodes.
- **p. 6 / 3.1. Lemmas - extractive body cue:** The AFIP effectively estimates the mean rewards and transitions of the real process over all the episodes.
- **p. 4 / 3. The convergence proof - extractive body cue:** Imagine each episode (xt, at, Yt, rt, °~t) written on a card.
- **p. 5 / 3. The convergence proof - extractive body cue:** 2 Note that during such a sequence, episode cards are only removed from the deck, and are never replaced.
- **p. 4 / 2. The task for ~-learning - extractive body cue:** DAYAN Theorem Given bounded rewards I rn [ -< (R, learning rates 0 < c~ n < 1, and ~ Otni(x,a ) : 0o, ~11 ...
- **p. 4 / 3. The convergence proof - extractive body cue:** The above completely specifies how state transitions and rewards are determined in the AFIP.
- **p. 5 / 3.1. Lemmas - extractive body cue:** B.1 Consider a discounted, bounded-reward, finite Markov process.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 3.2. The theorem | SYSTEM / EVALUATION SCOPE UNRESOLVED | Given e > O, choose s such that .ys__ < 1-3` T By B.3, with probability 1, it is possible to choose l sufficiently ... | p. 6 (3.2. The theorem) |
| 3.2. The theorem | SYSTEM / EVALUATION SCOPE UNRESOLVED | (~-LEARNING 285 2e 2e i,,,~ , ,ir#)taj _ ,~ Irxyl < 3s(s + 1)(R' and 16~'(n)(a) - (Rx(a)[ < 3s(s + 1)' where the ... | p. 7 (3.2. The theorem) |
| 3.2. The theorem | SYSTEM / EVALUATION SCOPE UNRESOLVED | Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state ... | p. 7 (3.2. The theorem) |
| 3.2. The theorem | SYSTEM / EVALUATION SCOPE UNRESOLVED | Given e > O, choose s such that .ys__ < 1-3` T By B.3, with probability 1, it is possible to choose l sufficiently ... | p. 6 (3.2. The theorem) |
| 3.2. The theorem | SYSTEM / EVALUATION SCOPE UNRESOLVED | (~-LEARNING 285 2e 2e i,,,~ , ,ir#)taj _ ,~ Irxyl < 3s(s + 1)(R' and 16~'(n)(a) - (Rx(a)[ < 3s(s + 1)' where the ... | p. 7 (3.2. The theorem) |

## Dataset / Benchmark Role

- **p. 4 / 3. The convergence proof - extractive body cue:** First, all the cards for episodes later than n are eliminated, leaving just a finite deck.
- **p. 5 / 3.1. Lemmas - extractive body cue:** The proof proceeds by backwards induction, following the AFIP down through the stack of past episodes.
- **p. 6 / 3.1. Lemmas - extractive body cue:** The AFIP effectively estimates the mean rewards and transitions of the real process over all the episodes.
- **p. 4 / 3. The convergence proof - extractive body cue:** Imagine each episode (xt, at, Yt, rt, °~t) written on a card.
- **p. 5 / 3. The convergence proof - extractive body cue:** 2 Note that during such a sequence, episode cards are only removed from the deck, and are never replaced.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | First, all the cards for episodes later than n are eliminated, leaving just a finite deck. | embodiment, simulator version and control stack | p. 4 (3. The convergence proof), p. 5 (3.1. Lemmas) |
| Task/environment | The proof proceeds by backwards induction, following the AFIP down through the stack of past episodes. | reset, timeout, object/scene variation | p. 5 (3.1. Lemmas), p. 6 (3.1. Lemmas) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 2 (2. The task for ~-learning), p. 2 (2. The task for ~-learning) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 3 (2. The task for ~-learning), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| DAYAN Theorem Given bounded rewards I rn [ -< (R, learning rates 0 < c~ n < 1, and ~ Otni(x,a ) : 0o, ... | definition/direction/unit from same section | p. 4 (2. The task for ~-learning) |
| The above completely specifies how state transitions and rewards are determined in the AFIP. | definition/direction/unit from same section | p. 4 (3. The convergence proof) |
| B.1 Consider a discounted, bounded-reward, finite Markov process. | definition/direction/unit from same section | p. 5 (3.1. Lemmas) |
| The AFIP effectively estimates the mean rewards and transitions of the real process over all the episodes. | definition/direction/unit from same section | p. 6 (3.1. Lemmas) |
| So, if the transition probabilities and rewards are close, then the values of the actions must be close too. | definition/direction/unit from same section | p. 6 (3.1. Lemmas) |
| The second term is the cost, from B.4, of the incorrect rewards and transition probabilities. | definition/direction/unit from same section | p. 7 (3.2. The theorem) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Assume, without loss of generality, that O~0(x, a) < 61/(1 - 3') and that 61 __. | comparison identity and matched condition | p. 6 (3.2. The theorem) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 2 Note that during such a sequence, episode cards are only removed from the deck, and are never replaced. | component/input/data sensitivity | p. 5 (3. The convergence proof) |
| However, by B.1, the effect of taking only s actions makes a difference of less than e/6 for both the ARP and the real ... | component/input/data sensitivity | p. 7 (3.2. The theorem) |
| Cards are then removed one at a time from top of this deck and examined until one is found whose starting state and action ... | component/input/data sensitivity | p. 4 (3. The convergence proof) |
| Assume, without loss of generality, that O~0(x, a) < 61/(1 - 3') and that 61 __. | component/input/data sensitivity | p. 6 (3.2. The theorem) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes. | Given e > O, choose s such that .ys__ < 1-3` T By B.3, with probability 1, it is possible to choose l sufficiently ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem), p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem) |
| Primary metric/result | (~-LEARNING 285 2e 2e i,,,~ , ,ir#)taj _ ,~ Irxyl < 3s(s + 1)(R' and 16~'(n)(a) - (Rx(a)[ < 3s(s + 1)' where the ... | numeric claim only at cited anchor | p. 7 (3.2. The theorem) |

- Numeric sentences retained from the body:
- **p. 6 / 3.2. The theorem - extractive body cue:** Given e > O, choose s such that .ys__ < 1-3` T By B.3, with probability 1, it is possible to choose l sufficiently large ...
- **p. 7 / 3.2. The theorem - extractive body cue:** (~-LEARNING 285 2e 2e i,,,~ , ,ir#)taj _ ,~ Irxyl < 3s(s + 1)(R' and 16~'(n)(a) - (Rx(a)[ < 3s(s + 1)' where the primes ...
- **p. 7 / 3.2. The theorem - extractive body cue:** Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x ...
- **p. 6 / 3.2. The theorem - extractive body cue:** Given e > O, choose s such that .ys__ < 1-3` T By B.3, with probability 1, it is possible to choose l sufficiently large ...
- **p. 7 / 3.2. The theorem - extractive body cue:** (~-LEARNING 285 2e 2e i,,,~ , ,ir#)taj _ ,~ Irxyl < 3s(s + 1)(R' and 16~'(n)(a) - (Rx(a)[ < 3s(s + 1)' where the primes ...
- **p. 7 / 3.2. The theorem - extractive body cue:** Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be ... | p. 8 (4. Discussions and conclusions) |
| body limitation/failure cue | The theorem above only proves the convergence of a restricted version of Watkins' (1989) comprehensive Q-learning algorithm, since it does not permit updates based ... | p. 8 (4. Discussions and conclusions) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| DAYAN Theorem Given bounded rewards I rn [ -< (R, learning rates 0 < c~ n < 1, and ~ Otni(x,a ) : 0o, ... | p. 4 (2. The task for ~-learning) |
| The key to the convergence proof is an artificial controlled Markov process called the actionreplay process AF1P, which is constructed from the episode sequence ... | p. 4 (3. The convergence proof) |
| Since its raw data are unbiased, the conditions on the sums and sums of squares of the learning rates O/ni(x,a ) ensure the convergence ... | p. 6 (3.1. Lemmas) |
| There are also various industrial applications. | p. 1 (1. Introduction) |
| By discounted reward, we mean that rewards received s steps hence are worth less than rewards received now, by a factor of 3"~ (0 ... | p. 2 (2. The task for ~-learning) |
| The first two steps are preparatory; the next two specify the form of the convergence and provide foundations for proving that it occurs. | p. 5 (3.1. Lemmas) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4. Discussions and conclusions - extractive body cue:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required.
- **p. 8 / 4. Discussions and conclusions - extractive body cue:** The theorem above only proves the convergence of a restricted version of Watkins' (1989) comprehensive Q-learning algorithm, since it does not permit updates based on ...

- **PDF anchors reviewed:** datasets p. 4 (3. The convergence proof), p. 5 (3.1. Lemmas), p. 6 (3.1. Lemmas), p. 4 (3. The convergence proof), p. 5 (3. The convergence proof), metrics p. 4 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 5 (3.1. Lemmas), p. 6 (3.1. Lemmas), p. 6 (3.1. Lemmas), p. 7 (3.2. The theorem), baselines p. 6 (3.2. The theorem), results p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem), p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
