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

- **Paper-specific interface:** Intuitively, since Equation 2 maximizes Q-values under the behavior policy ˆπβ, Q-values for actions that are likely under ˆπβ might be overestimated, and hence ˆQπ may not lower-bound Qπ pointwise. (p. 3, 2 Preliminaries).
- **Paper-specific mechanism:** We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Table 6: Average return obtained by CQL(H) and CQL(H) without the dataset average Q-value maximization term. The latter formulation corresponds to Equation 1, which is void of the dataset Q-value ... (p. 31, Figure/Table caption); the relevant task/metric cue is Table 2: Normalized scores of all methods on AntMaze, Adroit, and kitchen domains from D4RL, averaged across 4 seeds. On the harder mazes, CQL is the only method that attains ... (p. 8, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Of course, policy constraints should prevent the policy from choosing OOD actions, however, as we will show that in certain cases, policy constraint methods might also fail to prevent the ... (p. 15, B Discussion of Gap-Expanding Behavior of CQL Backups).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, offline reinforcement learning, conservative learning, Q-learning`.
- **Reading predecessor in the generated track queue:** Constrained Policy Optimization (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MOPO: Model-based Offline Policy Optimization (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This has made current results fall short of the full promise of such methods.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Intuitively, since Equation 2 maximizes Q-values under the behavior policy ˆπβ, Q-values for actions that are likely under ˆπβ might be overestimated, and hence ˆQπ may not lower-bound Qπ pointwise. (p. 3, 2 Preliminaries); preserve the objective/update rule: In Theorem 3.5, we first show that CQL (Equation 2) optimizes a well-defined penalized RL empirical objective. (p. 5, 2 Preliminaries).
2. Use the paper-reported task/data/environment cue: CQL outperforms prior methods by as much as 2-5x on many benchmark tasks, and is the only method that can outperform simple behavioral cloning on a number of realistic datasets ... (p. 2, 1 Introduction).
3. Compare against the reported or matched baseline: Table 5: Average return obtained by CQL(H), and CQL(ρ) on three D4RL MuJoCo environments. Observe that on these environments, CQL(H) generally outperforms CQL(ρ). Next, we evaluate the answer to question ... (p. 30, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: Table 2: Normalized scores of all methods on AntMaze, Adroit, and kitchen domains from D4RL, averaged across 4 seeds. On the harder mazes, CQL is the only method that attains ... (p. 8, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: Table 4: Difference between policy values predicted by each algorithm and the true policy value for CQL, a variant of CQL that uses Equation 1, the minimum of an ensemble ... (p. 9, Figure/Table caption); if none is reported, design one around: Of course, policy constraints should prevent the policy from choosing OOD actions, however, as we will show that in certain cases, policy constraint methods might also fail to prevent the ... (p. 15, B Discussion of Gap-Expanding Behavior of CQL Backups).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 31 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), and measure the boundary at p. 15 (B Discussion of Gap-Expanding Behavior of CQL Backups), p. 16 (B Discussion of Gap-Expanding Behavior of CQL Backups).

## Falsifiable research question

Under the paper's stated interface (Intuitively, since Equation 2 maximizes Q-values under the behavior policy ˆπβ, Q-values for actions that are likely under ˆπβ might be overestimated, ...), does the paper-specific mechanism (We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.) retain the reported evaluation outcome (Table 2: Normalized scores of all methods on AntMaze, Adroit, and kitchen domains from D4RL, averaged across 4 ...) when tested against the paper's strongest explicit boundary (Of course, policy constraints should prevent the policy from choosing OOD actions, however, as we will show that ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Table 2: Normalized scores of all methods on AntMaze, Adroit, and kitchen domains from D4RL, averaged across 4 ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms. (p. 2, 1 Introduction).
- **Paper-supported outcome:** Table 6: Average return obtained by CQL(H) and CQL(H) without the dataset average Q-value maximization term. The latter formulation corresponds to Equation 1, which is void of the dataset Q-value ... (p. 31, Figure/Table caption).
- **Strongest explicit boundary:** Of course, policy constraints should prevent the policy from choosing OOD actions, however, as we will show that in certain cases, policy constraint methods might also fail to prevent the ... (p. 15, B Discussion of Gap-Expanding Behavior of CQL Backups).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
