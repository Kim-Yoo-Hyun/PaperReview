# Evaluation - Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00992696; PDF retrieval source: https://doi.org/10.1007/BF00992696. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 17 (8. Algorithm performance and other issues), p. 15 (8. Algorithm performance and other issues), p. 18 (8. Algorithm performance and other issues), p. 17 (8. Algorithm performance and other issues), p. 9 (5. Episodic REINFORCE algorithms), p. 11 (7. Compatibility with backpropagation)): In those situations when it is known that unsatisfactory performance is being achieved it is reasonable to broaden this scale in order to take a coarsegrained view of the search ...

## Evaluation Body Digest

- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** A more general formulation of such an episodic learning task is also possible, where reinforcement is delivered to the network at each time step during ...
- **p. 15 / 8. Algorithm performance and other issues - extractive body cue:** In the case of the recurrent networks, the objective was to learn a trajectory and episodic REINFORCE was used.
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** Roughly, the idea is to treat this learning problem over the k-time-step interval as k different but overlapping episodic learning problems, all starting at the ...
- **p. 15 / 8. Algorithm performance and other issues - extractive body cue:** The network studies involved multilayer or recurrent networks facing supervised learning tasks but receiving only reinforcement feedback.
- **p. 16 / 8. Algorithm performance and other issues - extractive body cue:** One REINFORCE algorithm whose asymptotic behavior is reasonably well understood analytically is 2-action LR-~, and simulation experience obtained to date with a number of other ...
- **p. 16 / 8. Algorithm performance and other issues - extractive body cue:** In general, a reasonable conjecture consistent with what is known analytically about simple REINFORCE algorithms like LR-~ and what has been found in simulations of ...
- **p. 17 / 8. Algorithm performance and other issues - extractive body cue:** Simulation studies using both deterministic and noisy reinforcement confirm this behavior.
- **p. 17 / 8. Algorithm performance and other issues - extractive body cue:** Dayan's simulation results seem to suggest that use of such a reinforcement baseline offers 21

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 8. Algorithm performance and other issues | EMPIRICAL / SIMULATION | In those situations when it is known that unsatisfactory performance is being achieved it is reasonable to broaden this scale in order to take ... | p. 17 (8. Algorithm performance and other issues) |
| 8. Algorithm performance and other issues | EMPIRICAL / SIMULATION | In these studies, REINFORCE with reinforcement comparison was found to outperform all other algorithms investigated. | p. 15 (8. Algorithm performance and other issues) |
| 8. Algorithm performance and other issues | EMPIRICAL / SIMULATION | WILLIAMS a slight improvement in convergence speed over the use of mean reinforcement, but a more convincing advantage remains to be demonstrated. &4. | p. 18 (8. Algorithm performance and other issues) |
| 8. Algorithm performance and other issues | EMPIRICAL / SIMULATION | Also relevant here is the work of Schmidhuber and Huber (1990), who have reported successful results using networks having Gaussian output units in control ... | p. 17 (8. Algorithm performance and other issues) |
| 5. Episodic REINFORCE algorithms | EMPIRICAL / SIMULATION | In this case the appropriate performance measure is E {~=1 r(t) ] W}. | p. 9 (5. Episodic REINFORCE algorithms) |

## Dataset / Benchmark Role

- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** A more general formulation of such an episodic learning task is also possible, where reinforcement is delivered to the network at each time step during ...
- **p. 15 / 8. Algorithm performance and other issues - extractive body cue:** In the case of the recurrent networks, the objective was to learn a trajectory and episodic REINFORCE was used.
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** Roughly, the idea is to treat this learning problem over the k-time-step interval as k different but overlapping episodic learning problems, all starting at the ...
- **p. 15 / 8. Algorithm performance and other issues - extractive body cue:** The network studies involved multilayer or recurrent networks facing supervised learning tasks but receiving only reinforcement feedback.
- **p. 16 / 8. Algorithm performance and other issues - extractive body cue:** One REINFORCE algorithm whose asymptotic behavior is reasonably well understood analytically is 2-action LR-~, and simulation experience obtained to date with a number of other ...
- **p. 16 / 8. Algorithm performance and other issues - extractive body cue:** In general, a reasonable conjecture consistent with what is known analytically about simple REINFORCE algorithms like LR-~ and what has been found in simulations of ...
- **p. 17 / 8. Algorithm performance and other issues - extractive body cue:** Simulation studies using both deterministic and noisy reinforcement confirm this behavior.
- **p. 17 / 8. Algorithm performance and other issues - extractive body cue:** Dayan's simulation results seem to suggest that use of such a reinforcement baseline offers 21

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | A more general formulation of such an episodic learning task is also possible, where reinforcement is delivered to the network at each time step ... | embodiment, simulator version and control stack | p. 9 (5. Episodic REINFORCE algorithms), p. 15 (8. Algorithm performance and other issues) |
| Task/environment | In the case of the recurrent networks, the objective was to learn a trajectory and episodic REINFORCE was used. | reset, timeout, object/scene variation | p. 15 (8. Algorithm performance and other issues), p. 9 (5. Episodic REINFORCE algorithms) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 8 (5. Episodic REINFORCE algorithms) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| One potentially useful feature of such a Gaussian unit is that the mean and variance of its output are individually controllable as long as ... | definition/direction/unit from same section | p. 10 (6. REINFORCE with multiparameter distributions) |
| In this work, backpropagation through random number generators was used to allow learning of a model and learning of performance to proceed simultaneously rather ... | definition/direction/unit from same section | p. 17 (8. Algorithm performance and other issues) |
| As a particular example, the normal distribution has two parameters, the mean/z and the standard deviation a. | definition/direction/unit from same section | p. 10 (6. REINFORCE with multiparameter distributions) |
| It is worth noting that these particular results in no way depend on the fact that/~ is the mean and o the standard deviation; ... | definition/direction/unit from same section | p. 14 (7.2. Backpropagating through random number generators) |
| Since the sampled points y are roughly twice as likely to lie within one standard deviation of the mean, it follows that whenever/z sits ... | definition/direction/unit from same section | p. 16 (8. Algorithm performance and other issues) |
| In this case the appropriate performance measure is E {~=1 r(t) ] W}. | definition/direction/unit from same section | p. 9 (5. Episodic REINFORCE algorithms) |
| All quantities are assumed to satisfy the same conditions required for the REINFORCE algorithm, where, in particular, for each i and j, the reinforcement ... | definition/direction/unit from same section | p. 9 (5. Episodic REINFORCE algorithms) |
| Then 01n g _ y - # &z 02 where 02 is the variance of the distribution. | definition/direction/unit from same section | p. 11 (6. REINFORCE with multiparameter distributions) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In these studies, REINFORCE with reinforcement comparison was found to outperform all other algorithms investigated. | comparison identity and matched condition | p. 15 (8. Algorithm performance and other issues) |
| While Theorem 1 applies equally well to any such choice, extensive empirical investigation of such algorithms leads to the inescapable conclusion that use of ... | comparison identity and matched condition | p. 17 (8. Algorithm performance and other issues) |
| All quantities are assumed to satisfy the same conditions required for the REINFORCE algorithm, where, in particular, for each i and j, the reinforcement ... | comparison identity and matched condition | p. 9 (5. Episodic REINFORCE algorithms) |
| For further discussion of the role of the reinforcement baseline, see below. &2. | comparison identity and matched condition | p. 16 (8. Algorithm performance and other issues) |
| In general, a reasonable conjecture consistent with what is known analytically about simple REINFORCE algorithms like LR-~ and what has been found in simulations ... | comparison identity and matched condition | p. 16 (8. Algorithm performance and other issues) |
| Dayan's simulation results seem to suggest that use of such a reinforcement baseline offers 21 | comparison identity and matched condition | p. 17 (8. Algorithm performance and other issues) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| WILLIAMS effect of connectivity between units is ignored; each unit in the network tries to determine the effect of changes of its output on ... | component/input/data sensitivity | p. 12 (7. Compatibility with backpropagation) |
| Some of the variants examined incorporated modifications designed to help defeat this often undesirable behavior. | component/input/data sensitivity | p. 15 (8. Algorithm performance and other issues) |
| Williams and Peng (1991) have also investigated a number of variants of REINFORCE in nonassociative function-optimization tasks, using networks of Bernoulli units. | component/input/data sensitivity | p. 15 (8. Algorithm performance and other issues) |
| A straightforward way to obtain a number of variants of REINFORCE is to vary the form of either of these factors. | component/input/data sensitivity | p. 18 (8. Algorithm performance and other issues) |
| Furthermore, the corresponding strategy can be used to generate variants of REINFORCE in a number of other cases. | component/input/data sensitivity | p. 18 (8. Algorithm performance and other issues) |
| But perhaps most significant of all is the fact that, in the sense given by Theorems 1 and 2, they climb an appropriate gradient ... | component/input/data sensitivity | p. 19 (8.5. Use of other local gradient estimates) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an ... | In those situations when it is known that unsatisfactory performance is being achieved it is reasonable to broaden this scale in order to take ... | PDF body cue; verify exact table/figure and matched conditions | p. 17 (8. Algorithm performance and other issues), p. 15 (8. Algorithm performance and other issues), p. 18 (8. Algorithm performance and other issues), p. 17 (8. Algorithm performance and other issues), p. 9 (5. Episodic REINFORCE algorithms), p. 11 (7. Compatibility with backpropagation) |
| Primary metric/result | In these studies, REINFORCE with reinforcement comparison was found to outperform all other algorithms investigated. | numeric claim only at cited anchor | p. 15 (8. Algorithm performance and other issues) |

- Numeric sentences retained from the body:
- **p. 20 / 8.5. Use of other local gradient estimates - extractive body cue:** WILLIAMS using the y - 3S form of eligibility described above may be related to such an approach but this has not been fully analyzed ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 8.L Convergence properties A major limitation of the analysis performed here is that it does not immediately lead to prediction of the asymptotic properties ... | p. 15 (8. Algorithm performance and other issues) |
| body limitation/failure cue | Unfortunately, even this property fails to hold in general. | p. 14 (7.2. Backpropagating through random number generators) |
| body limitation/failure cue | Choice of reinforcement baseline One important limitation of the analysis given here is that it offers no basis for choosing among various choices of ... | p. 17 (8. Algorithm performance and other issues) |
| body limitation/failure cue | REINFORCE fails to be model-based even in this local sense, but it may be worthwhile to consider algorithms that do attempt to generate more ... | p. 19 (8.5. Use of other local gradient estimates) |
| body limitation/failure cue | OWij gi OWij Although this fails to be defined when gi = 0, it will still be the case that Awij is welldefined for ... | p. 22 (1 Og i) |
| body limitation/failure cue | Then E{Awij I W, x i} = Z E{Awijl W, x i, Yi = ~} Pr{yi = ~ I W, x i} ~Y~ --- ... | p. 22 (1 Og i) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which the units ... | p. 8 (5. Episodic REINFORCE algorithms) |
| WILLIAMS Awij = ~ij(r - bij)eij, where c~/j is a learning rate factor, bij is a reinforcement baseline, and eij = 0In gi/3wij is ... | p. 6 (4. REINFORCE algorithms) |
| A "network" consisting of more than one such unit constitutes a team of such learning automata, each using its own individual learning rate. | p. 7 (4. REINFORCE algorithms) |
| It is interesting to compare this with the associative rewardpenalty (An_e) algorithm (Barto, 1985; Barto & Anandan, 1985; Barto & Anderson, 1985; Barto & ... | p. 7 (4. REINFORCE algorithms) |
| Recall that weights are adjusted in this network following receipt of the reinforcement value r at each trial. | p. 5 (4. REINFORCE algorithms) |
| Suppose that the learning algorithm for this network is such that at the end of each trial each parameter wij in the network is ... | p. 5 (4. REINFORCE algorithms) |
| What is noteworthy about this algorithm is that it has a plausible on-line implementation using a single accumulator for each parameter w/j in the ... | p. 9 (5. Episodic REINFORCE algorithms) |
| A unit determining its output according to such a distribution would first compute values of/z and a determinisfically and then draw its output from ... | p. 10 (6. REINFORCE with multiparameter distributions) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / 8. Algorithm performance and other issues - extractive body cue:** 8.L Convergence properties A major limitation of the analysis performed here is that it does not immediately lead to prediction of the asymptotic properties of ...
- **p. 14 / 7.2. Backpropagating through random number generators - extractive body cue:** Unfortunately, even this property fails to hold in general.
- **p. 17 / 8. Algorithm performance and other issues - extractive body cue:** Choice of reinforcement baseline One important limitation of the analysis given here is that it offers no basis for choosing among various choices of reinforcement ...
- **p. 19 / 8.5. Use of other local gradient estimates - extractive body cue:** REINFORCE fails to be model-based even in this local sense, but it may be worthwhile to consider algorithms that do attempt to generate more explicit ...
- **p. 22 / 1 Og i - extractive body cue:** OWij gi OWij Although this fails to be defined when gi = 0, it will still be the case that Awij is welldefined for any ...
- **p. 22 / 1 Og i - extractive body cue:** Then E{Awij I W, x i} = Z E{Awijl W, x i, Yi = ~} Pr{yi = ~ I W, x i} ~Y~ --- ~i ...

- **PDF anchors reviewed:** datasets p. 9 (5. Episodic REINFORCE algorithms), p. 15 (8. Algorithm performance and other issues), p. 9 (5. Episodic REINFORCE algorithms), p. 15 (8. Algorithm performance and other issues), p. 16 (8. Algorithm performance and other issues), p. 16 (8. Algorithm performance and other issues), metrics p. 10 (6. REINFORCE with multiparameter distributions), p. 17 (8. Algorithm performance and other issues), p. 10 (6. REINFORCE with multiparameter distributions), p. 14 (7.2. Backpropagating through random number generators), p. 16 (8. Algorithm performance and other issues), p. 9 (5. Episodic REINFORCE algorithms), baselines p. 15 (8. Algorithm performance and other issues), p. 17 (8. Algorithm performance and other issues), p. 9 (5. Episodic REINFORCE algorithms), p. 16 (8. Algorithm performance and other issues), p. 16 (8. Algorithm performance and other issues), p. 17 (8. Algorithm performance and other issues), results p. 17 (8. Algorithm performance and other issues), p. 15 (8. Algorithm performance and other issues), p. 18 (8. Algorithm performance and other issues), p. 17 (8. Algorithm performance and other issues), p. 9 (5. Episodic REINFORCE algorithms), p. 11 (7. Compatibility with backpropagation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
