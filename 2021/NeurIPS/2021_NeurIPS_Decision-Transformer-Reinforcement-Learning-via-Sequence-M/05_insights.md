# Insights — Decision Transformer: Reinforcement Learning via Sequence Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.01345; PDF retrieval source: https://arxiv.org/pdf/2106.01345. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** Training dataset consists of random walk trajectories and their per-node returns-to-go (middle).
- **p. 4 / 1 Introduction - extractive body cue:** Motivated by this observation, we propose Decision Transformer, where we use the GPT architecture to autoregressively model trajectories (shown in Figure 1).
- **p. 4 / 3 Method - extractive body cue:** In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure 1 and Algorithm ...
- **p. 5 / 3 Method - extractive body cue:** We did not find predicting the states or returns-to-go to improve performance, although it is easily permissible within our framework (as shown in Section 5.4) ...
- **p. 6 / 3 Method - extractive body cue:** We evaluate our method on 1% of all samples in the DQN-replay dataset as per Agarwal et al.
- **p. 4 / 3 Method - extractive body cue:** The key desiderata in our choice of trajectory representation are that it should enable transformers to learn meaningful patterns and we should be able to ...
- **p. 6 / 3 Method - extractive body cue:** In particular, our primary points of comparison are modelfree offline RL algorithms based on TD-learning, since our Decision Transformer architecture is fundamentally model-free in nature ...
- **Contribution anchor:** p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 4 (3 Method)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** To get an intuition for our proposal, consider the task of finding the shortest path on a directed graph, which can be posed as an ...
- **p. 3 / 1 Introduction - extractive body cue:** Finally, empirical evidence suggest that a transformer modeling approach can model a wide distribution of behaviors, enabling better generalization and transfer [3].
- **p. 9 / 5 Discussion - extractive body cue:** TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance.
- **p. 11 / Dataset - extractive body cue:** This act of optimizing a learned function can exacerbate and exploit any inaccuracies in the value function approximation, causing failures in policy improvement.
- **p. 12 / 7 Conclusion - extractive body cue:** Transformer models can also be used to model the state evolution of trajectory, potentially serving as an alternative to model-based RL, and we hope to ...
- **p. 10 / Dataset - extractive body cue:** Decision Transformer (DT) and imitation learning are minimally affected by the removal of dense rewards, while CQL fails.
- **p. 10 / Dataset - extractive body cue:** To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, and ...
- **Boundary to test:** TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Training dataset consists of random walk trajectories and their per-node returns-to-go (middle). | p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Reported outcome | Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such as Atari, where we use 1% of a replay buffer ... | p. 8 (Figure/Table caption), p. 21 (Figure/Table caption) |
| Failure/limitation | TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance. | p. 9 (5 Discussion), p. 11 (Dataset) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 By training an autoregressive model on sequences of states, actions, and returns, we reduce policy sampling to autoregressive generative modeling.를 We use st, at, and rt = R(st, at) to denote the state, action, and reward at timestep t, respectively.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Training dataset consists of random walk trajectories and their per-node returns-to-go (middle).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Reinforcement Learning, Transformer, policy`.
- **Reading predecessor in the generated track queue:** Offline Reinforcement Learning with Implicit Q-Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Denoising Diffusion Probabilistic Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, and instead receives the cumulative reward of the ....
3. Compare against the body-reported baseline or a matched simpler baseline: Table 2: Results for D4RL datasets3. We report the mean and variance for three seeds. Decision Transformer (DT) outperforms conventional RL algorithms on almost all tasks. 3Given that CQL is generally the ....
4. Report the body metric and its denominator/aggregation: Table 6: Success rate for Key-to-Door environment. Methods using hindsight (Decision Transformer, %BC) can learn successful policies, while TD learning struggles to perform credit assignment. 5.5 Can transformers be accurate critics in ....
5. Re-run the body-reported ablation/failure condition: Table 5: Ablation on context length. Decision Transformer (DT) performs better when using a longer context length (K = 50 for Pong, K = 30 for others). 5.4 Does Decision Transformer perform ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3 Method), p. 4 (3 Method), p. 6 (3 Method); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 21 (Figure/Table caption), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Training, dataset, consists mechanism이 Table 2: Results for D4RL datasets3. We report the mean and variance for three seeds. Decision ... 대비 Table 6: Success rate for Key-to-Door environment. Methods using hindsight (Decision Transformer, %BC) can learn successful policies, while ...을 개선하고, TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
