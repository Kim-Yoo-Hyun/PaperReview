# Insights — SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2011.07215; PDF retrieval source: https://arxiv.org/pdf/2011.07215. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface ...
- **p. 3 / 1 Introduction - extractive body cue:** SoftGym consists of three parts: SoftGym-Medium, SoftGym-Hard and SoftGym-Robot, visualized in Figure 1.
- **p. 3 / 1 Introduction - extractive body cue:** 4 SoftGym To advance research in reinforcement learning in complex environments with an inherently high dimensional state, we propose SoftGym.
- **p. 2 / 1 Introduction - extractive body cue:** As such, we believe that SoftGym would be a unique and valuable contribution to the reinforcement learning and robotics communities, by enabling new methods to ...
- **p. 4 / 1 Introduction - extractive body cue:** This action space is designed to enable the user to focus on the challenges of high-level planning and to abstract away the low-level manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Due to the large number of samples required by reinforcement learning, as well as the difficulty in specifying a reward function, all these works start ...
- **p. 2 / 1 Introduction - extractive body cue:** We benchmark a range of algorithms on these environments assuming different observation spaces for the policy, including full knowledge of the ground-truth state of the ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, programming a robot to perform these tasks has long been a challenge in robotics due to the high dimensional state representation and complex dynamics ...
- **p. 1 / 1 Introduction - extractive body cue:** However, such low-dimensional sufficient state representations are difficult to perceive (or sometimes even define) for many deformable object tasks, such as laundry folding or dough ...
- **p. 2 / 1 Introduction - extractive body cue:** These environments highlight the difficulty in performing robot manipulation tasks in environments that have complex visual observations with partial observability and an inherently high dimensional ...
- **p. 2 / 1 Introduction - extractive body cue:** Due to the large number of samples required by reinforcement learning, as well as the difficulty in specifying a reward function, all these works start ...
- **p. 3 / 1 Introduction - extractive body cue:** 4.1 Action Space We aim to decouple the challenges in learning low-level grasping skills from high-level planning.
- **p. 7 / 6 Experiments - extractive body cue:** from a policy that always does nothing.
- **p. 7 / 6 Experiments - extractive body cue:** On the other hand, this method does not perform very well on the FoldCloth task.
- **Boundary to test:** from a policy that always does nothing.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface for creating new environments. | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Reported outcome | While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for exploration, the result shows that there still exists a large ... | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Failure/limitation | from a policy that always does nothing. | p. 7 (6 Experiments), p. 7 (6 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 4 SoftGym To advance research in reinforcement learning in complex environments with an inherently high dimensional state, we propose SoftGym. (p. 3, 1 Introduction).
- **Paper-specific mechanism:** In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface for creating new environments. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is 6.2 Benchmarking results on SoftGym-Medium A summary of the final normalized performance of all baselines on the evaluation set is shown in Figure 2. (p. 7, 6 Experiments); the relevant task/metric cue is 6.1 Experimental Setup For each task, we compute a lower bound and upper bound on performance so that we can more easily analyze the performance of each method (see Appendix ... (p. 6, 6 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We do not include the latent over-shooting in our experiment as it does not improve much over the one-step case. (p. 17, B.4 PlaNet).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, deformable object, Benchmark, Reinforcement Learning, simulation`.
- **Reading predecessor in the generated track queue:** Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** from a policy that always does nothing.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 4 SoftGym To advance research in reinforcement learning in complex environments with an inherently high dimensional state, we propose SoftGym. (p. 3, 1 Introduction); preserve the objective/update rule: Given this information, we can use gradient free optimization to maximize the return. (p. 5, 1 Introduction).
2. Use the paper-reported task/data/environment cue: In this section, we perform experiments with an aim to answer the following questions: • Are SoftGym tasks challenging for current reinforcement learning algorithms? • Is learning with state as ... (p. 6, 6 Experiments).
3. Compare against the reported or matched baseline: While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for exploration, the result shows that there still exists ... (p. 7, 6 Experiments).
4. Report the body metric with its denominator and aggregation: 6.1 Experimental Setup For each task, we compute a lower bound and upper bound on performance so that we can more easily analyze the performance of each method (see Appendix ... (p. 6, 6 Experiments).
5. Re-run the reported ablation or stress/failure condition: 6.1 Experimental Setup For each task, we compute a lower bound and upper bound on performance so that we can more easily analyze the performance of each method (see Appendix ... (p. 6, 6 Experiments); if none is reported, design one around: We do not include the latent over-shooting in our experiment as it does not improve much over the one-step case. (p. 17, B.4 PlaNet).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 3 (1 Introduction), match the reported outcome at p. 7 (6 Experiments), p. 7 (6 Experiments), p. 6 (6 Experiments), and measure the boundary at p. 17 (B.4 PlaNet), p. 7 (6 Experiments).

## Falsifiable research question

Under the paper's stated interface (4 SoftGym To advance research in reinforcement learning in complex environments with an inherently high dimensional state, we propose SoftGym.), does the paper-specific mechanism (In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API ...) retain the reported evaluation outcome (6.1 Experimental Setup For each task, we compute a lower bound and upper bound on performance so that ...) when tested against the paper's strongest explicit boundary (We do not include the latent over-shooting in our experiment as it does not improve much over the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (6.1 Experimental Setup For each task, we compute a lower bound and upper bound on performance so that ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface for creating new environments. (p. 2, 1 Introduction).
- **Paper-supported outcome:** 6.2 Benchmarking results on SoftGym-Medium A summary of the final normalized performance of all baselines on the evaluation set is shown in Figure 2. (p. 7, 6 Experiments).
- **Strongest explicit boundary:** We do not include the latent over-shooting in our experiment as it does not improve much over the one-step case. (p. 17, B.4 PlaNet).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
