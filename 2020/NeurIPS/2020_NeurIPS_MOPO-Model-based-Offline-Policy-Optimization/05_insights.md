# Insights — MOPO: Model-based Offline Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2005.13239; PDF retrieval source: https://arxiv.org/pdf/2005.13239. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** Specifically, these methods estimate error with respect to out-of-distribution actions, but only consider states that lie within the offline dataset and do not ∗equal contribution. ...
- **p. 2 / 1 Introduction - extractive body cue:** The primary contribution of this work is an offline model-based RL algorithm that optimizes a policy in an uncertainty-penalized MDP, where the reward function is ...
- **p. 1 / Abstract - extractive body cue:** Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- **p. 5 / 3 Preliminaries - extractive body cue:** We will analyze our framework under the assumption that we have access to an oracle uncertainty quantification module that provides an upper bound on the ...
- **p. 2 / 1 Introduction - extractive body cue:** Although neither method is designed for the batch setting, we find that the model-based method and its variant without ensembles show surprisingly large gains.
- **p. 4 / 3 Preliminaries - extractive body cue:** 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that ...
- **p. 4 / 3 Preliminaries - extractive body cue:** Then we maximize the conservative estimation of the return by an off-the-shelf reinforcement learning algorithm, which gives MOPO, a generic model-based off-policy algorithm (Section 4.2).
- **Contribution anchor:** p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 5 (3 Preliminaries), p. 2 (1 Introduction), p. 4 (3 Preliminaries)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Our results suggest that MOPO substantially outperforms these prior methods on the offline RL benchmark D4RL [18] as well as on offline RL problems where ...
- **p. 1 / 1 Introduction - extractive body cue:** These failures are generally caused by large extrapolation error when the Q-function is evaluated on out-of-distribution actions [19, 36], which can lead to unstable learning ...
- **p. 2 / 1 Introduction - extractive body cue:** In particular, because offline model-based algorithms cannot improve the dynamics model using additional experience, we expect that such algorithms require careful use of the model ...
- **p. 3 / 3 Preliminaries - extractive body cue:** In the offline RL problem, the algorithm only has access to a static dataset Denv = {(s, a, r, s′)} collected by one or a ...
- **p. 7 / 3 Preliminaries - extractive body cue:** While this estimator lacks theoretical guarantees, we find that it is sufficiently accurate to achieve good performance in practice.4 Hence the practical uncertainty-penalized reward of ...
- **p. 9 / 6 Conclusion - extractive body cue:** However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation.
- **p. 9 / 6 Conclusion - extractive body cue:** Our work opens up a number of questions and directions for future work.
- **Boundary to test:** However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Specifically, these methods estimate error with respect to out-of-distribution actions, but only consider states that lie within the offline dataset and do not ∗equal contribution. † equal advising. | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Table 2: Average returns halfcheetah-jump and ant-angle that require out-of-distribution policy. The MOPO results are averaged over 6 random seeds, ± standard deviation, while the results of other methods are averaged over ... | p. 9 (Figure/Table caption), p. 18 (Figure/Table caption) |
| Failure/limitation | However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation. | p. 9 (6 Conclusion), p. 9 (6 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `dataset state/observation, action, reward와 return-to-go → Q/value 또는 sequence-policy state → dataset-supported action sequence`.
- 이 논문의 재사용 가능한 지점은 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that are not strictly within the support of ...를 We argue that it is important for an offline RL algorithm to be equipped with the ability to leave the data support to learn a better policy for two reasons: (1) the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 Q/value 또는 sequence-policy state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Specifically, these methods estimate error with respect to out-of-distribution actions, but only consider states that lie within the offline dataset and do not ∗equal contribution. † equal advising.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, offline reinforcement learning, model-based RL, distribution shift`.
- **Reading predecessor in the generated track queue:** Conservative Q-Learning for Offline Reinforcement Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** A Minimalist Approach to Offline Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 5.1 Evaluation on the D4RL benchmark To answer question (1), we evaluate our method on a large subset of datasets in the D4RL benchmark [18] based on the MuJoCo simulator [69], including ....
3. Compare against the body-reported baseline or a matched simpler baseline: We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms..
4. Report the body metric and its denominator/aggregation: To extend the theory to an unknown reward function, we can consider the reward as being concatenated onto the state, so that the admissible error estimator bounds the error on (s′, r), ....
5. Re-run the body-reported ablation/failure condition: To answer question (3), we conduct a complete ablation study to analyze the effect of each module in MOPO in Appendix D..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 7 (3 Preliminaries); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (5 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Specifically, methods, estimate mechanism이 We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms. 대비 To extend the theory to an unknown reward function, we can consider the reward as being concatenated onto ...을 개선하고, However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
