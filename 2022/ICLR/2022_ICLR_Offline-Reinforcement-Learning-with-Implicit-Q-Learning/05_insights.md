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

- **Closed-loop position:** `dataset state/observation, action, reward와 return-to-go → Q/value 또는 sequence-policy state → dataset-supported action sequence`.
- 이 논문의 재사용 가능한 지점은 Off-policy RL methods based on approximate dynamic programming typically utilize a state-action value function (Q-function), referred to as Q(s, a), which corresponds to the discounted returns obtained by starting from the state ...를 When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function that degrades to zero far from the rewarding states too quickly (c).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 Q/value 또는 sequence-policy state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy extraction (AWR): for each gradient step do φ ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve substantially over the best behavior in the ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, offline reinforcement learning, implicit Q-learning, continuous control`.
- **Reading predecessor in the generated track queue:** Implicit Behavioral Cloning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Decision Transformer: Reinforcement Learning via Sequence Modeling (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy extraction (AWR): for each gradient step do φ ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the degree to which we can learn effective policies using only ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 3: Estimating a larger expectile τ is crucial for antmaze tasks that require dynamical program- ming ('stitching'). Comparisons and baselines. We compare to methods that are representative of both multi- step ....
4. Report the body metric and its denominator/aggregation: 1.0 0.5 0.0 0.5 1.0 u 0.0 0.2 0.4 0.6 0.8 1.0 / (u < 0)/u2 = 0.01 = 0.1 = 0.5 = 0.9 = 0.99 2 0 2 x 0.0 0.1 ....
5. Re-run the body-reported ablation/failure condition: Crucially, we will show that it is possible to do this without ever querying the learned Q-function on out-of-sample actions by utilizing expectile regression..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (ABSTRACT), p. 3 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 9 (3 PRELIMINARIES), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 offline, never, needs mechanism이 Figure 3: Estimating a larger expectile τ is crucial for antmaze tasks that require dynamical program- ... 대비 1.0 0.5 0.0 0.5 1.0 u 0.0 0.2 0.4 0.6 0.8 1.0 / (u < 0)/u2 = 0.01 ...을 개선하고, TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
