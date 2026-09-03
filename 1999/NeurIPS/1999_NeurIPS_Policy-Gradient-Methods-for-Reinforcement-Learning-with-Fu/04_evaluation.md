# Evaluation - Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html; PDF retrieval source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Abstract), p. 4 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract), p. 5 (Abstract)): If the above can be achieved, then 0 can usually be assured to converge to a locally optimal policy in the performance measure p.

## Evaluation Body Digest

- **p. 2 / Abstract - extractive body cue:** The environment's dynamics are characterized by state transition probabilities, P:SI = Pr { St+ 1 = Sf I St = s, at = a}, and ...
- **p. 3 / Abstract - extractive body cue:** Policy Gradient Methods for RL with Function Approximation 1059 With function approximation, two ways of formulating the agent's objective are useful.
- **p. 3 / Abstract - extractive body cue:** We will give our results only once, but they will apply to this formulation as well under the definitions p(1I") = E{t. "(t-lrt I 80 ...
- **p. 2 / Abstract - extractive body cue:** However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy.
- **p. 2 / Abstract - extractive body cue:** Let 0 denote the vector of policy parameters and p the performance of the corresponding policy (e.g., the average reward per step).
- **p. 3 / Abstract - extractive body cue:** For any MDP, in either the average-reward or start-state formulations, ap = "'.ftr( )'" a1l"(s,a)Q1r( ) ao ~ u s ~ ao s, a .
- **p. 3 / Abstract - extractive body cue:** (2) This way of expressing the gradient was first rtiscussed for the average-reward formulation by Marbach and Tsitsiklis (1998), based on a related expression in ...
- **p. 4 / Abstract - extractive body cue:** (5) II a Proof: Combining (3) and (4) gives Ld7f(s) L 87r1~a) [Q7f(s,a) - fw(s,a)] = 0 (6) II a which tells us that the ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | If the above can be achieved, then 0 can usually be assured to converge to a locally optimal policy in the performance measure p. | p. 2 (Abstract) |
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | For example, Jaakkola, Singh, and Jordan (1995) proved that for the special case of function approximation arising in a tabular POMDP one could assure ... | p. 4 (Abstract) |
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. | p. 2 (Abstract) |
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | We extend their results to the start-state formulation and provide simpler and more direct proofs. | p. 3 (Abstract) |
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our first result concerns the gradient of the performance metric with respect to the policy parameter: Theorem 1 (Policy Gradient). | p. 3 (Abstract) |

## Dataset / Benchmark Role

- **p. 2 / Abstract - extractive body cue:** The environment's dynamics are characterized by state transition probabilities, P:SI = Pr { St+ 1 = Sf I St = s, at = a}, and ...
- **p. 3 / Abstract - extractive body cue:** Policy Gradient Methods for RL with Function Approximation 1059 With function approximation, two ways of formulating the agent's objective are useful.
- **p. 3 / Abstract - extractive body cue:** We will give our results only once, but they will apply to this formulation as well under the definitions p(1I") = E{t. "(t-lrt I 80 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption PDF body cue not selected; no claim inferred

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The environment's dynamics are characterized by state transition probabilities, P:SI = Pr { St+ 1 = Sf I St = s, at = a}, ... | embodiment, simulator version and control stack | p. 2 (Abstract), p. 3 (Abstract) |
| Task/environment | Policy Gradient Methods for RL with Function Approximation 1059 With function approximation, two ways of formulating the agent's objective are useful. | reset, timeout, object/scene variation | p. 3 (Abstract), p. 3 (Abstract) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 2 (Abstract), p. 1 (Abstract) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 3 (Abstract), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. | definition/direction/unit from same section | p. 2 (Abstract) |
| Let 0 denote the vector of policy parameters and p the performance of the corresponding policy (e.g., the average reward per step). | definition/direction/unit from same section | p. 2 (Abstract) |
| For any MDP, in either the average-reward or start-state formulations, ap = "'.ftr( )'" a1l"(s,a)Q1r( ) ao ~ u s ~ ao s, a ... | definition/direction/unit from same section | p. 3 (Abstract) |
| (2) This way of expressing the gradient was first rtiscussed for the average-reward formulation by Marbach and Tsitsiklis (1998), based on a related expression ... | definition/direction/unit from same section | p. 3 (Abstract) |
| (5) II a Proof: Combining (3) and (4) gives Ld7f(s) L 87r1~a) [Q7f(s,a) - fw(s,a)] = 0 (6) II a which tells us that ... | definition/direction/unit from same section | p. 4 (Abstract) |
| 8 2 7r(s a) ....£..£....- The bounds on 89;89j and on the MDP's rewards together assure us that 89i89j | definition/direction/unit from same section | p. 5 (Abstract) |
| Then, for any MDP with bounded rewards, the sequence {p(1rk)}r=o, defined by any 00, 1rk = 1r(.,., Ok), and '"' '"' [ ]ofw(s,a) Wk ... | definition/direction/unit from same section | p. 5 (Abstract) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The issues here are entirely analogous to those in the use of reinforcement baselines in earlier work (e.g., Williams, 1992; Dayan, 1991; Sutton, 1984). | comparison identity and matched condition | p. 5 (Abstract) |
| Williams's (1988, 1992) REINFORCE algorithm also finds an unbiased estimate of the gradient, but without the assistance of a learned value function. | comparison identity and matched condition | p. 2 (Abstract) |
| Our results establish that that approximation process can proceed without affecting the expected evolution of fw and 1r. | comparison identity and matched condition | p. 5 (Abstract) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In any event, the key aspect of both expressions for the gradient is that their are no terms of the form adiJII): the effect ... | component/input/data sensitivity | p. 3 (Abstract) |
| Williams's (1988, 1992) REINFORCE algorithm also finds an unbiased estimate of the gradient, but without the assistance of a learned value function. | component/input/data sensitivity | p. 2 (Abstract) |
| Our results establish that that approximation process can proceed without affecting the expected evolution of fw and 1r. | component/input/data sensitivity | p. 5 (Abstract) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours. | If the above can be achieved, then 0 can usually be assured to converge to a locally optimal policy in the performance measure p. | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Abstract), p. 4 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract), p. 5 (Abstract) |
| Primary metric/result | For example, Jaakkola, Singh, and Jordan (1995) proved that for the special case of function approximation arising in a tabular POMDP one could assure ... | numeric claim only at cited anchor | p. 4 (Abstract) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy. | p. 2 (Abstract) |
| body limitation/failure cue | As a result, VAPS does not converge to a locally optimal policy, except in the case that no weight is put upon value-function accuracy, ... | p. 2 (Abstract) |
| body limitation/failure cue | In any event, the key aspect of both expressions for the gradient is that their are no terms of the form adiJII): the effect ... | p. 3 (Abstract) |
| body limitation/failure cue | (This follows immediately because l:a 87r~~a) = 0, Vs E S.) The choice of v does not affect any of our theorems, but can ... | p. 5 (Abstract) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Mansour Rather than approximating a value function and using that to compute a deterministic policy, we approximate a stochastic policy directly using an independent ... | p. 2 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Abstract - extractive body cue:** Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy.
- **p. 2 / Abstract - extractive body cue:** As a result, VAPS does not converge to a locally optimal policy, except in the case that no weight is put upon value-function accuracy, in ...
- **p. 3 / Abstract - extractive body cue:** In any event, the key aspect of both expressions for the gradient is that their are no terms of the form adiJII): the effect of ...
- **p. 5 / Abstract - extractive body cue:** (This follows immediately because l:a 87r~~a) = 0, Vs E S.) The choice of v does not affect any of our theorems, but can substantially ...

- **Evidence anchors reviewed:** datasets p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract), metrics p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 5 (Abstract), baselines p. 5 (Abstract), p. 2 (Abstract), p. 5 (Abstract), results p. 2 (Abstract), p. 4 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract), p. 5 (Abstract).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. (p. 2, Abstract).
- **Metric evidence:** However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. (p. 2, Abstract).
- **Baseline/ablation evidence:** Williams's (1988, 1992) REINFORCE algorithm also finds an unbiased estimate of the gradient, but without the assistance of a learned value function. (p. 2, Abstract).
- **Failure/negative evidence:** The value-function approach has worked well in many applications, but has several limitations. (p. 1, Abstract).
