# Insights — A Minimalist Approach to Offline Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.06860; PDF retrieval source: https://arxiv.org/pdf/2106.06860. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated ...
- **p. 2 / 1 Introduction - extractive body cue:** The surprising effectiveness of our minimalist approach suggests that in the context of offline RL, simpler approaches have been left underexplored in favor of more ...
- **p. 3 / 3 Background - extractive body cue:** We believe these challenges highlight the importance of minimalist approaches, where performance can be easily attributed to algorithmic contributions, rather than entangled with the specifics ...
- **p. 4 / 3 Background - extractive body cue:** If additional changes are necessary, then it suggests the algorithmic contributions alone are insufficient.
- **p. 6 / 3 Background - extractive body cue:** As discussed in Section 4 a minimalist approach has a variety of benefits, such as reducing the number of hyperparameters to tune, increasing scalability by ...
- **p. 4 / 3 Background - extractive body cue:** Most offline RL algorithms are built explicitly on top of an existing off-policy deep RL algorithm, such as TD3 [Fujimoto et al., 2018] or SAC ...
- **p. 4 / 3 Background - extractive body cue:** CQL Fisher-BRC TD3+BC [Kumar et al., 2020] [Kostrikov et al., 2021] (Ours) Algorithmic Adjustments Add regularizer to critic† Train a generative model†‡ Add a BC ...
- **Contribution anchor:** p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Background), p. 4 (3 Background), p. 6 (3 Background), p. 4 (3 Background)

### Strongest assumption and failure boundary

- **p. 3 / 3 Background - extractive body cue:** One challenge for offline RL is the problem of extrapolation error [Fujimoto et al., 2019b], which is generalization error in the approximate value function, induced ...
- **p. 4 / 3 Background - extractive body cue:** However, in the offline setting, where we cannot interact with the environment, making additional adjustments to the underlying algorithm should be considered as more costly ...
- **p. 3 / 3 Background - extractive body cue:** 4 Challenges in Offline RL In this section, we identify key open challenges in offline RL through analyzing and evaluating prior algorithms.
- **p. 5 / 3 Background - extractive body cue:** In analyzing the final trained policies of prior offline algorithms, we learned of a tangential, and open, challenge in the form of instability.
- **p. 6 / 3 Background - extractive body cue:** While we could not solve this challenge sufficiently within the scope of this work, the fact that this is reproducible even in the minimalistic variant ...
- **p. 9 / 7 Conclusion - extractive body cue:** Finally, we believe the sheer simplicity of our approach highlights a possible overemphasis on algorithmic complexity made by the community, and we hope to inspire ...
- **p. 9 / 7 Conclusion - extractive body cue:** Additionally, we highlight existing open challenges in offline RL research, including not only the extra implementation, computation, and hyperparameter-tuning complexities that we successfully address in ...
- **Boundary to test:** Finally, we believe the sheer simplicity of our approach highlights a possible overemphasis on algorithmic complexity made by the community, and we hope to inspire future work to revisit simpler alternatives which ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated with an untrained RL agent. | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added implementation details (mainly architecture changes) and the algorithmic ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Failure/limitation | Finally, we believe the sheer simplicity of our approach highlights a possible overemphasis on algorithmic complexity made by the community, and we hope to inspire future work to revisit simpler alternatives which ... | p. 9 (7 Conclusion), p. 9 (7 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** This in turn affects policy improvement, where agents learn to prefer out-of-distribution actions whose value has been overestimated, resulting in poor performance [Fujimoto et al., 2019b]. (p. 1, 1 Introduction).
- **Paper-specific mechanism:** Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated with an untrained RL agent. (p. 1, 1 Introduction).
- **Evidence boundary:** the reported outcome is Table 9: Average normalized score using the D4RL -v2 datasets. The highest performing scores are highlighted. ± captures the standard deviation over seeds. Total (DT) sums scores over the subset ... (p. 18, Figure/Table caption); the relevant task/metric cue is BC CQL Fisher-BRC TD3+BC 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 80 100 120 Normalized Score HalfCheetah-Random 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 ... (p. 8, 6 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We use the hyperparameters defined in the CQL paper rather than the default settings in the CQL GitHub as we found those settings performed poorly. † denotes hyperparameters which deviate ... (p. 15, B Experimental Details).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, offline reinforcement learning, behavior cloning, continuous control`.
- **Reading predecessor in the generated track queue:** MOPO: Model-based Offline Policy Optimization (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Finally, we believe the sheer simplicity of our approach highlights a possible overemphasis on algorithmic complexity made by the community, and we hope to inspire future work to revisit simpler alternatives which ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: This in turn affects policy improvement, where agents learn to prefer out-of-distribution actions whose value has been overestimated, resulting in poor performance [Fujimoto et al., 2019b]. (p. 1, 1 Introduction); preserve the objective/update rule: TD3's policy π is updated with the deterministic policy gradient [Silver et al., 2014]: π = argmax π E(s,a)∼D[Q(s, π(s))]. (p. 2, 1 Introduction).
2. Use the paper-reported task/data/environment cue: We evaluate our proposed approach on the D4RL benchmark of OpenAI gym MuJoCo tasks [Todorov et al., 2012, Brockman et al., 2016, Fu et al., 2020], which encompasses a variety ... (p. 7, 6 Experiments).
3. Compare against the reported or matched baseline: Our offline RL baselines include two state-of-the-art algorithms, CQL [Kumar et al., 2020] and Fisher-BRC [Kostrikov et al., 2021], as well as BRAC [Wu et al., 2019] and AWAC [Nair ... (p. 7, 6 Experiments).
4. Report the body metric with its denominator and aggregation: BC CQL Fisher-BRC TD3+BC 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 80 100 120 Normalized Score HalfCheetah-Random 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 ... (p. 8, 6 Experiments).
5. Re-run the reported ablation or stress/failure condition: BC CQL Fisher-BRC TD3+BC 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 80 100 120 Normalized Score HalfCheetah-Random 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 ... (p. 8, 6 Experiments); if none is reported, design one around: We use the hyperparameters defined in the CQL paper rather than the default settings in the CQL GitHub as we found those settings performed poorly. † denotes hyperparameters which deviate ... (p. 15, B Experimental Details).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (6 Experiments), and measure the boundary at p. 15 (B Experimental Details), p. 18 (C.3 Benchmarking against the Decision Transformer).

## Falsifiable research question

Under the paper's stated interface (This in turn affects policy improvement, where agents learn to prefer out-of-distribution actions whose value has been overestimated, resulting in poor performance ...), does the paper-specific mechanism (Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of ...) retain the reported evaluation outcome (BC CQL Fisher-BRC TD3+BC 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 80 100 120 Normalized ...) when tested against the paper's strongest explicit boundary (We use the hyperparameters defined in the CQL paper rather than the default settings in the CQL GitHub ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (BC CQL Fisher-BRC TD3+BC 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 80 100 120 Normalized ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated with an untrained RL agent. (p. 1, 1 Introduction).
- **Paper-supported outcome:** Table 9: Average normalized score using the D4RL -v2 datasets. The highest performing scores are highlighted. ± captures the standard deviation over seeds. Total (DT) sums scores over the subset ... (p. 18, Figure/Table caption).
- **Strongest explicit boundary:** We use the hyperparameters defined in the CQL paper rather than the default settings in the CQL GitHub as we found those settings performed poorly. † denotes hyperparameters which deviate ... (p. 15, B Experimental Details).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
