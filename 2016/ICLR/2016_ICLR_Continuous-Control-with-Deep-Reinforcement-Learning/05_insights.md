# Insights — Continuous Control with Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1509.02971; PDF retrieval source: https://arxiv.org/pdf/1509.02971. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In order to evaluate our method we constructed a variety of challenging physical control problems that involve complex multi-joint movements, unstable and rich contact dynamics, ...
- **p. 1 / ABSTRACT - extractive body cue:** We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, as we show below, a naive application of this actor-critic method with neural function approximators is unstable for challenging problems.
- **p. 3 / 2 BACKGROUND - extractive body cue:** Our contribution here is to provide modifications to DPG, inspired by the success of DQN, which allow it to use neural network function approximators to ...
- **p. 4 / 2 BACKGROUND - extractive body cue:** In the low-dimensional case, we used batch normalization on the state input and all layers of the µ network and all layers of the Q ...
- **p. 2 / 2 BACKGROUND - extractive body cue:** We model it as a Markov decision process with a state space S, action space A = IRN, an initial state distribution p(s1), transition dynamics ...
- **Contribution anchor:** p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, this has many limitations, most notably the curse of dimensionality: the number of actions increases exponentially with the number of degrees of freedom.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Such large action spaces are difficult to explore efficiently, and thus successfully training DQN-like networks in this context is likely intractable.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Prior to DQN, it was generally believed that learning value functions using large, non-linear function approximators was difficult and unstable.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A key feature of the approach is its simplicity: it requires only a straightforward actor-critic architecture and learning algorithm with very few "moving parts", making ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** However, such approximators appear essential in order to learn and generalize on large state spaces.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task ...
- **p. 8 / 6 CONCLUSION - extractive body cue:** The work combines insights from recent advances in deep learning and reinforcement learning, resulting in an algorithm that robustly solves challenging problems across a variety ...
- **Boundary to test:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task name Brief Description blockworld1 Agent is required ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces. | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). All scores, except Torcs, are normalized so ... | p. 7 (Figure/Table caption), p. 5 (4 RESULTS) |
| Failure/limitation | Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task name Brief Description blockworld1 Agent is required ... | p. 12 (Figure/Table caption), p. 8 (6 CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 A long-standing challenge of robotic control is to learn an action policy directly from raw sensory input such as video.를 An agent's behavior is defined by a policy, π, which maps states to a probability distribution over the actions π: S →P(A).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task name Brief Description blockworld1 Agent is required ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, continuous control, actor-critic`.
- **Reading predecessor in the generated track queue:** DrEureka: Language Model Guided Sim-To-Real Transfer (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Addressing Function Approximation Error in Actor-Critic Methods (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task name Brief Description blockworld1 Agent is required ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We examined DDPG's estimates empirically by comparing the values estimated by Q after training with the true returns seen on test episodes..
3. Compare against the body-reported baseline or a matched simpler baseline: We normalized the scores using two baselines..
4. Report the body metric and its denominator/aggregation: Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). All scores, except Torcs, are normalized so ....
5. Re-run the body-reported ablation/failure condition: We also report results with components of our algorithm (i.e. the target network or batch normalization) removed..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (2 BACKGROUND), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 5 (4 RESULTS), p. 5 (4 RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, model-free, off-policy mechanism이 We normalized the scores using two baselines. 대비 Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the ...을 개선하고, Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
