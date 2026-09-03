# Evaluation - Maximum Entropy Inverse Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.cmu.edu/~bziebart/publications/maximum-entropy-inverse-reinforcement-learning.html; PDF retrieval source: https://cdn.aaai.org/AAAI/2008/AAAI08-227.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Abstract), p. 3 (2. Recursively compute for N iterations), p. 5 (Figure/Table caption), p. 3 (2. Recursively compute for N iterations), p. 2 (Abstract), p. 6 (Figure/Table caption)): The authors propose a strategy of matching feature expectations (Equation 1) between an observed policy and a learner's behavior; they demonstrate that this matching is both necessary and sufficient to ...

## Evaluation Body Digest

- **p. 4 / 2. Recursively compute for N iterations - extractive body cue:** We discarded roughly 30% of the trips that were too short (fewer than 10 road segments), too cyclic, or too noisy, and split 20% of ...
- **p. 5 / A B - extractive body cue:** We use a training set to form a prior over destinations and evaluate our model on a withheld test set.
- **p. 4 / 2. Recursively compute for N iterations - extractive body cue:** This yielded a dataset of over 100,000 miles of travel collected during over 3,000 hours of driving and covering a large area surrounding Pittsburgh.
- **p. 5 / A B - extractive body cue:** The final metric measures the average log probability of paths in the training set under the given model.
- **p. 2 / Abstract - extractive body cue:** The authors propose a strategy of matching feature expectations (Equation 1) between an observed policy and a learner's behavior; they demonstrate that this matching is ...
- **p. 2 / Abstract - extractive body cue:** However, given demonstrated trajectories that are absorbed in a finite number of steps, the reward weights maximizing entropy must be convergent.
- **p. 3 / Abstract - extractive body cue:** The gradient is the difference between expected empirical feature counts and the learner's expected feature counts, which can be expressed in terms of expected state ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Example of probability distributions over paths. There are three obvious paths from A to B in Figure 2. As- suming each path provides ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | The authors propose a strategy of matching feature expectations (Equation 1) between an observed policy and a learner's behavior; they demonstrate that this matching ... | p. 2 (Abstract) |
| 2. Recursively compute for N iterations | SYSTEM / EVALUATION SCOPE UNRESOLVED | Space doesn't permit the full exposition of the incomplete (and non-convex) log-likelihood, but the intuitive expectation-maximization algorithm that results fits the maximumentropy model using ... | p. 3 (2. Recursively compute for N iterations) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: Comparison of different models' abilities to match most likely path predictions to withheld paths (average per- centage of distance matching and percentage ... | p. 5 (Figure/Table caption) |
| 2. Recursively compute for N iterations | SYSTEM / EVALUATION SCOPE UNRESOLVED | 2For stochastic MDPs we can achieve better usage of finite data by removing the variance in sample feature expectations due to the uncertainty in ... | p. 3 (2. Recursively compute for N iterations) |
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | Maximum Entropy IRL We take a different approach to matching feature counts that allows us to deal with this ambiguity in a principled way, ... | p. 2 (Abstract) |

## Dataset / Benchmark Role

- **p. 4 / 2. Recursively compute for N iterations - extractive body cue:** We discarded roughly 30% of the trips that were too short (fewer than 10 road segments), too cyclic, or too noisy, and split 20% of ...
- **p. 5 / A B - extractive body cue:** We use a training set to form a prior over destinations and evaluate our model on a withheld test set.
- **p. 4 / 2. Recursively compute for N iterations - extractive body cue:** This yielded a dataset of over 100,000 miles of travel collected during over 3,000 hours of driving and covering a large area surrounding Pittsburgh.
- **p. 5 / A B - extractive body cue:** The final metric measures the average log probability of paths in the training set under the given model.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: A deterministic MDP (a) and a single path from its path-space (b). A non-deterministic MDP (c) and a single path from its path-space ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Example of probability distributions over paths. There are three obvious paths from A to B in Figure 2. As- suming each path provides ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Comparison of different models' abilities to match most likely path predictions to withheld paths (average per- centage of distance matching and percentage of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Learned costs of turns (left) and miles of differ- ent road types (right) normalized to seconds (with interstate driving fixed to 65 miles ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Destination distribution (from 5 destinations) and remaining path distribution given partially traveled path. The partially traveled path is heading westward, which is a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Posterior prediction accuracy over five destina- tions given partial path.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We discarded roughly 30% of the trips that were too short (fewer than 10 road segments), too cyclic, or too noisy, and split 20% ... | embodiment, simulator version and control stack | p. 4 (2. Recursively compute for N iterations), p. 5 (A B) |
| Task/environment | We use a training set to form a prior over destinations and evaluate our model on a withheld test set. | reset, timeout, object/scene variation | p. 5 (A B), p. 4 (2. Recursively compute for N iterations) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 3 (Abstract), p. 4 (2. Recursively compute for N iterations) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 1 (Abstract), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The authors propose a strategy of matching feature expectations (Equation 1) between an observed policy and a learner's behavior; they demonstrate that this matching ... | definition/direction/unit from same section | p. 2 (Abstract) |
| However, given demonstrated trajectories that are absorbed in a finite number of steps, the reward weights maximizing entropy must be convergent. | definition/direction/unit from same section | p. 2 (Abstract) |
| The gradient is the difference between expected empirical feature counts and the learner's expected feature counts, which can be expressed in terms of expected ... | definition/direction/unit from same section | p. 3 (Abstract) |
| Figure 2: Example of probability distributions over paths. There are three obvious paths from A to B in Figure 2. As- suming each path ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Zai,j = X k P(sk/si, ai,j)ereward(si/θ)Zsk Zsi = X ai,j Zai,j Local action probability computation 3. | definition/direction/unit from same section | p. 3 (2. Recursively compute for N iterations) |
| We call this value a cost (i.e., a negative reward). | definition/direction/unit from same section | p. 4 (2. Recursively compute for N iterations) |
| For instance, the highest reward policy may not be the most probable policy in the model, and policies with the same expected reward can ... | definition/direction/unit from same section | p. 5 (A B) |
| Figure 5: Posterior prediction accuracy over five destina- tions given partial path. | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| They consider a class of loss functions that directly measure disagreement between an agent and a learned policy, and then efficiently learn a reward ... | comparison identity and matched condition | p. 2 (Abstract) |
| Compared to our maximum entropy distribution over paths, this model gives higher probability mass to paths with a smaller branching factor and lower probability ... | comparison identity and matched condition | p. 5 (A B) |
| Our algorithm is efficient (polynomial time) for both classes, but this reduction provides a significant speed up (without introducing optimization non-convexity) and limits consideration ... | comparison identity and matched condition | p. 4 (2. Recursively compute for N iterations) |
| Table 1: Comparison of different models' abilities to match most likely path predictions to withheld paths (average per- centage of distance matching and percentage ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our algorithm is efficient (polynomial time) for both classes, but this reduction provides a significant speed up (without introducing optimization non-convexity) and limits consideration ... | component/input/data sensitivity | p. 4 (2. Recursively compute for N iterations) |
| Further, by learning a probability distribution over driver preferences, destinations, and routes the MaxEntIRL model of driver behavior can go beyond route recommendation, to ... | component/input/data sensitivity | p. 5 (A B) |
| 2For stochastic MDPs we can achieve better usage of finite data by removing the variance in sample feature expectations due to the uncertainty in ... | component/input/data sensitivity | p. 3 (2. Recursively compute for N iterations) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our probabilistic approach enables modeling of route preferences as well as a powerful new approach to inferring destinations and routes based on partial trajectories. | The authors propose a strategy of matching feature expectations (Equation 1) between an observed policy and a learner's behavior; they demonstrate that this matching ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Abstract), p. 3 (2. Recursively compute for N iterations), p. 5 (Figure/Table caption), p. 3 (2. Recursively compute for N iterations), p. 2 (Abstract), p. 6 (Figure/Table caption) |
| Primary metric/result | Space doesn't permit the full exposition of the incomplete (and non-convex) log-likelihood, but the intuitive expectation-maximization algorithm that results fits the maximumentropy model using ... | numeric claim only at cited anchor | p. 3 (2. Recursively compute for N iterations) |

- Numeric sentences retained from the body:
- **p. 4 / 2. Recursively compute for N iterations - extractive body cue:** This yielded a dataset of over 100,000 miles of travel collected during over 3,000 hours of driving and covering a large area surrounding Pittsburgh.
- **p. 4 / 2. Recursively compute for N iterations - extractive body cue:** This yielded a dataset of over 100,000 miles of travel collected during over 3,000 hours of driving and covering a large area surrounding Pittsburgh.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This arises quite frequently when, for instance, the behavior demonstrated by the agent is imperfect, or the planning algorithm only captures a part of ... | p. 2 (Abstract) |
| body limitation/failure cue | We employ the principle of maximum entropy, which resolves this ambiguity by choosing the distribution that does not exhibit any additional preferences beyond matching ... | p. 2 (Abstract) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| These branching values yield local action probabilities (Step 3), from which state frequencies in each timestep can be computed (Steps 4 and 5) and ... | p. 4 (2. Recursively compute for N iterations) |
| However, given demonstrated trajectories that are absorbed in a finite number of steps, the reward weights maximizing entropy must be convergent. | p. 2 (Abstract) |
| Recursively compute for t = 1 to N Dsi,t+1 = X ai,j X k Dsk,tP(ai,j/si)P(sk/ai,j, si) Summing frequencies 6. | p. 3 (2. Recursively compute for N iterations) |
| 2 Efficient State Frequency Calculations Given the expected state frequencies, the gradient can easily be computed (Equation 6) for optimization. | p. 3 (Abstract) |
| It recursively "backs up" from each possible terminal state (Step 1) and computes the probability mass associated with each branch along the way (Step ... | p. 4 (2. Recursively compute for N iterations) |
| P(dest/˜ζA→B) ∝P(˜ζA→B/dest)P(dest) ∝ P ζB→dest eθ⊤fζ P ζA→dest eθ⊤fζ P(dest) These quantities can easily be computed using our inference algorithm (Algorithm 1). | p. 5 (A B) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Abstract - extractive body cue:** This arises quite frequently when, for instance, the behavior demonstrated by the agent is imperfect, or the planning algorithm only captures a part of the ...
- **p. 2 / Abstract - extractive body cue:** We employ the principle of maximum entropy, which resolves this ambiguity by choosing the distribution that does not exhibit any additional preferences beyond matching feature ...

- **Evidence anchors reviewed:** datasets p. 4 (2. Recursively compute for N iterations), p. 5 (A B), p. 4 (2. Recursively compute for N iterations), p. 5 (A B), metrics p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (Figure/Table caption), p. 3 (2. Recursively compute for N iterations), p. 4 (2. Recursively compute for N iterations), baselines p. 2 (Abstract), p. 5 (A B), p. 4 (2. Recursively compute for N iterations), p. 5 (Figure/Table caption), results p. 2 (Abstract), p. 3 (2. Recursively compute for N iterations), p. 5 (Figure/Table caption), p. 3 (2. Recursively compute for N iterations), p. 2 (Abstract), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
