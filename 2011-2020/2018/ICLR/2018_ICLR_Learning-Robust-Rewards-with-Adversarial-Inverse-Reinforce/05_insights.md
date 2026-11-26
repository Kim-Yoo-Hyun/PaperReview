# Insights — Learning Robust Rewards with Adversarial Inverse Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1710.11248; PDF retrieval source: https://arxiv.org/pdf/1710.11248. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** When compared to GAIL (Ho & Ermon, 2016), which does not attempt to directly recover rewards, our method achieves comparable results on tasks that do ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** In order to decouple the reward function from the advantage, we propose to modify the discriminator of Sec.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** There are many scenarios where IRL may be preferred over direct imitation learning, such as re-optimizing a reward in novel environments (Finn et al., 2017) ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** If the ground truth reward is also only a function of state, this allows us to recover the true reward up to a constant.
- **p. 3 / 3 BACKGROUND - extractive body cue:** The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** Suppose IRL recovers a state-only reward r′(s) such that it produces an optimal policy in T: Q∗ r′,T (s, a) = Q∗ r,T (s, a) ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 5 (3 BACKGROUND), p. 3 (3 BACKGROUND)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithm provides for simultaneous learning of the reward function and value function, which enables us to both make use of the efficient adversarial formulation ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, adversarial IRL methods (Finn et al., 2016b;a) hold promise for tackling difficult tasks due to the ability to adapt training samples to improve learning ...
- **p. 4 / 3 BACKGROUND - extractive body cue:** Because IRL methods only infer rewards from demonstrations given from an optimal agent, they cannot in general disambiguate between reward functions within this class of ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Part of the challenge is that IRL is an ill-defined problem, since there are many optimal policies that can explain a set of demonstrations, and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (2008) handles the former ambiguity, but the latter ambiguity means that IRL algorithms have difficulty distinguishing the true reward functions from those shaped by the ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we cannot ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** At test time, the agent cannot simply mimic the actions learned during training, and instead must successfully infer that the goal in the maze is ...
- **Boundary to test:** 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we cannot guarantee that learned rewards will not be ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | We also show that in the transfer learning setup, under a new transition matrix T ′, the optimal policy under the state-only reward achieves optimal performance (it is identical to the ground ... | p. 6 (7 EXPERIMENTS), p. 7 (Figure/Table caption) |
| Failure/limitation | 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we cannot guarantee that learned rewards will not be ... | p. 5 (3 BACKGROUND), p. 7 (7 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation history와 expert trajectory/action → behavior policy와 temporal action context → predicted action 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: π∗= arg maxπ Eτ∼π " T X ...를 4 ADVERSARIAL INVERSE REINFORCEMENT LEARNING (AIRL) In practice, using full trajectories as proposed by GAN-GCL can result in high variance estimates as compared to using single state, action pairs, and our experimental ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 behavior policy와 temporal action context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we cannot guarantee that learned rewards will not be ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, inverse reinforcement learning, adversarial learning, reward learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we cannot guarantee that learned rewards will not be ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: (2016a), which we refer to as GAN-GCL, on standard benchmark tasks that do not evaluate transfer..
3. Compare against the body-reported baseline or a matched simpler baseline: We find that AIRL performs on par with GAIL in a traditional imitation learning setup while vastly outperforming it in transfer learning setups, and outperforms GAN-GCL in both settings..
4. Report the body metric and its denominator/aggregation: Table 1: Results on transfer learning tasks. Mean scores (higher is better) are reported over 5 runs. We also include results for TRPO optimizing the ground truth reward, and the performance of ....
5. Re-run the body-reported ablation/failure condition: 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we cannot guarantee that learned rewards will not be ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 1 (ABSTRACT); the primary result is directionally consistent at p. 6 (7 EXPERIMENTS), p. 7 (Figure/Table caption), p. 6 (7 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 adversarial, inverse, reinforcement mechanism이 We find that AIRL performs on par with GAIL in a traditional imitation learning setup while ... 대비 Table 1: Results on transfer learning tasks. Mean scores (higher is better) are reported over 5 runs. We ...을 개선하고, 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
