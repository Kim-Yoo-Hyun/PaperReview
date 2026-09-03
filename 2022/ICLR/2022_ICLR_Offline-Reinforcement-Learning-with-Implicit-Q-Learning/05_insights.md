# Insights — Offline Reinforcement Learning with Implicit Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=68n2s9ZJWF8; PDF retrieval source: https://arxiv.org/pdf/2110.06169. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / ABSTRACT - extractive body cue:** We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method is easy to implement by making a small change to the loss function in a simple SARSA-like TD update and is computationally very ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The key idea in our method is to approximate an upper expectile of the distribution over values with respect to the distribution of dataset actions ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** In the following theorems, we show that under certain assumptions, our method indeed approximates the optimal state-action value Q∗and performs multi-step dynamical programming.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** 5 EXPERIMENTAL EVALUATION Our experiments aim to evaluate our method comparatively, in contrast to prior offline RL methods, and in particular to understand how our ...
- **p. 1 / ABSTRACT - extractive body cue:** The main insight in our work is that, instead of evaluating unseen actions from the latest policy, we can approximate the policy improvement step implicitly ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** Off-policy RL methods based on approximate dynamic programming typically utilize a state-action value function (Q-function), referred to as Q(s, a), which corresponds to the discounted ...
- **Contribution anchor:** p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 1 (ABSTRACT)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, this also carries with it major challenges: improving the policy beyond the level of the behavior policy that collected the data requires estimating values ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Offline reinforcement learning (RL) addresses the problem of learning effective policies entirely from previously collected data, without online interaction (Fujimoto et al., 2019; Lange et ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In particular, our approach significantly improves over the prior state-of-the-art on challenging Ant Maze tasks that require to "stitch" several sub-optimal trajectories.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we start from an observation that in-distribution constraints widely used in prior work might not be sufficient to avoid value function extrapolation, ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** The RL problem is formulated in the context of a Markov decision process (MDP) (S, A, p0(s), p(s′/s, a), r(s, a), γ), where S is ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy extraction ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** Note that the policy does not influence the value function in any way, and therefore extraction could be performed either concurrently or after TD learning.
- **Boundary to test:** TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy extraction (AWR): for each gradient step do φ ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve substantially over the best behavior in the ... | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Reported outcome | Table 2: Online finetuning results showing the initial perfor- mance after offline RL, and performance after 1M steps of on- line RL. In all tasks, IQL is able to finetune to a ... | p. 9 (Figure/Table caption), p. 9 (3 PRELIMINARIES) |
| Failure/limitation | TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy extraction (AWR): for each gradient step do φ ... | p. 5 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve substantially over the best behavior ... (p. 1, ABSTRACT).
- **Paper-specific mechanism:** Our method is easy to implement by making a small change to the loss function in a simple SARSA-like TD update and is computationally very efficient. (p. 2, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is Figure 2: Evaluation of our algorithm on a toy umaze environment (a). When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function ... (p. 7, Figure/Table caption); the relevant task/metric cue is The agent receives a reward of 10 for entering the goal state and zero reward for all other transitions. (p. 7, 3 PRELIMINARIES). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Our reproduced results offline are worse than the reported results, particularly on medium and large antmaze environments. (p. 13, C FINETUNING EXPERIMENTAL DETAILS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, offline reinforcement learning, implicit Q-learning, continuous control`.
- **Reading predecessor in the generated track queue:** Implicit Behavioral Cloning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Decision Transformer: Reinforcement Learning via Sequence Modeling (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy extraction (AWR): for each gradient step do φ ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve substantially over the best behavior ... (p. 1, ABSTRACT); preserve the objective/update rule: Note that we can optimize this objective with stochastic gradient descent. (p. 4, 3 PRELIMINARIES).
2. Use the paper-reported task/data/environment cue: The MuJoCo tasks in D4RL consist of the Gym locomotion tasks, the Ant Maze tasks, and the Adroit and Kitchen robotic manipulation environments. (p. 7, 3 PRELIMINARIES).
3. Compare against the reported or matched baseline: Figure 3: Estimating a larger expectile τ is crucial for antmaze tasks that require dynamical program- ming ('stitching'). Comparisons and baselines. We compare to methods that are representative of both ... (p. 8, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: The agent receives a reward of 10 for entering the goal state and zero reward for all other transitions. (p. 7, 3 PRELIMINARIES).
5. Re-run the reported ablation or stress/failure condition: Crucially, we will show that it is possible to do this without ever querying the learned Q-function on out-of-sample actions by utilizing expectile regression. (p. 4, 3 PRELIMINARIES); if none is reported, design one around: Our reproduced results offline are worse than the reported results, particularly on medium and large antmaze environments. (p. 13, C FINETUNING EXPERIMENTAL DETAILS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), match the reported outcome at p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (3 PRELIMINARIES), and measure the boundary at p. 13 (C FINETUNING EXPERIMENTAL DETAILS), p. 13 (C FINETUNING EXPERIMENTAL DETAILS).

## Falsifiable research question

Under the paper's stated interface (We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned ...), does the paper-specific mechanism (Our method is easy to implement by making a small change to the loss function in a simple SARSA-like TD update and ...) retain the reported evaluation outcome (The agent receives a reward of 10 for entering the goal state and zero reward for all other ...) when tested against the paper's strongest explicit boundary (Our reproduced results offline are worse than the reported results, particularly on medium and large antmaze environments.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The agent receives a reward of 10 for entering the goal state and zero reward for all other ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our method is easy to implement by making a small change to the loss function in a simple SARSA-like TD update and is computationally very efficient. (p. 2, 1 INTRODUCTION).
- **Paper-supported outcome:** Figure 2: Evaluation of our algorithm on a toy umaze environment (a). When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** Our reproduced results offline are worse than the reported results, particularly on medium and large antmaze environments. (p. 13, C FINETUNING EXPERIMENTAL DETAILS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
