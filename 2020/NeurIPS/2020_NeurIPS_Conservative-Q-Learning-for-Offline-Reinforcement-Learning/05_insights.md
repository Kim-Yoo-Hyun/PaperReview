# Insights — Conservative Q-Learning for Offline Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html; PDF retrieval source: https://arxiv.org/pdf/2006.04779. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.
- **p. 2 / 1 Introduction - extractive body cue:** The key idea behind our method is to minimize values under an appropriately chosen distribution over state-action tuples, and then further tighten this bound by ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a policy under the ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Due to space constraints, we present these results in Theorem D.1 and Theorem D.2 in Appendix D.1.
- **p. 6 / 2 Preliminaries - extractive body cue:** (6) The expression of ζ in Theorem 3.6 consists of two terms: the first term captures the decrease in policy performance in M, that occurs ...
- **p. 2 / 2 Preliminaries - extractive body cue:** S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) represents the discount ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (2 Preliminaries), p. 1 (Abstract), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning ...
- **p. 1 / 1 Introduction - extractive body cue:** This in principle can make it possible to leverage large datasets, but in practice fully offline RL methods pose major technical difficulties, stemming from the ...
- **p. 5 / 2 Preliminaries - extractive body cue:** We also showed that the Q-function is gap-expanding, meaning that it should only ever over-estimate the gap between in-distribution and out-of-distribution actions, preventing OOD actions.
- **p. 5 / 2 Preliminaries - extractive body cue:** Our final result shows that CQL Q-function update is "gap-expanding", by which we mean that the difference in Q-values at in-distribution actions and over-optimistically erroneous ...
- **p. 6 / 2 Preliminaries - extractive body cue:** Note that this penalty is implicitly introduced by virtue by the gap-expanding (Theorem 3.4) behavior of CQL.
- **p. 1 / 1 Introduction - extractive body cue:** This has made current results fall short of the full promise of such methods.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of ...
- **Boundary to test:** This has made current results fall short of the full promise of such methods.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Table 2: Normalized scores of all methods on AntMaze, Adroit, and kitchen domains from D4RL, averaged across 4 seeds. On the harder mazes, CQL is the only method that attains non-zero returns, ... | p. 8 (Figure/Table caption), p. 31 (Figure/Table caption) |
| Failure/limitation | This has made current results fall short of the full promise of such methods. | p. 1 (1 Introduction), p. 1 (Abstract) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `dataset state/observation, action, reward와 return-to-go → Q/value 또는 sequence-policy state → dataset-supported action sequence`.
- 이 논문의 재사용 가능한 지점은 S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) represents the discount factor. πβ(a/s) represents the behavior policy, D ...를 However, the policy may suffer from state distribution shift at test time.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 Q/value 또는 sequence-policy state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 This has made current results fall short of the full promise of such methods.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, offline reinforcement learning, conservative learning, Q-learning`.
- **Reading predecessor in the generated track queue:** Constrained Policy Optimization (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MOPO: Model-based Offline Policy Optimization (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This has made current results fall short of the full promise of such methods.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: CQL outperforms prior methods by as much as 2-5x on many benchmark tasks, and is the only method that can outperform simple behavioral cloning on a number of realistic datasets collected from ....
3. Compare against the body-reported baseline or a matched simpler baseline: Table 5: Average return obtained by CQL(H), and CQL(ρ) on three D4RL MuJoCo environments. Observe that on these environments, CQL(H) generally outperforms CQL(ρ). Next, we evaluate the answer to question (2). On ....
4. Report the body metric and its denominator/aggregation: We also empirically demonstrate the robustness of our approach to Q-function estimation error..
5. Re-run the body-reported ablation/failure condition: Table 4: Difference between policy values predicted by each algorithm and the true policy value for CQL, a variant of CQL that uses Equation 1, the minimum of an ensemble of varying ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), p. 2 (2 Preliminaries); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 31 (Figure/Table caption), p. 5 (2 Preliminaries); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 novel, learning, conservative mechanism이 Table 5: Average return obtained by CQL(H), and CQL(ρ) on three D4RL MuJoCo environments. Observe that ... 대비 We also empirically demonstrate the robustness of our approach to Q-function estimation error.을 개선하고, This has made current results fall short of the full promise of such methods. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
