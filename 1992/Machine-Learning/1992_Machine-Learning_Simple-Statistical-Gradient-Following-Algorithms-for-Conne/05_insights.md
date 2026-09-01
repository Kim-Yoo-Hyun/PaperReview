# Insights — Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00992696; PDF retrieval source: https://doi.org/10.1007/BF00992696. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output ...
- **p. 2 / 1. Introduction - extractive body cue:** The results to be presented apply in general to any learner whose inputoutput mappings consists of a parameterized input-controlled distribution function from which outputs are ...
- **p. 8 / 5. Episodic REINFORCE algorithms - extractive body cue:** In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which the units may ...
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** For example, if the network consists of Bernoulli-logistic units an episodic REINFORCE algorithm would prescribe weight changes according to the rule k Awij = c~ij(r ...
- **p. 1 / 1. Introduction - extractive body cue:** While delayed reinforcement tasks are obviously important and are receiving much-deserved attention lately, a widely used approach to developing algorithms for such tasks is to ...
- **p. 8 / 4. REINFORCE algorithms - extractive body cue:** As a particular example, for a network of Bernoulli-logistic units one may use the learning rule Awij = a(r - ?)(Yi - Pi) xj, (9) ...
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** One way to create a statistical gradient-following algorithm for this case is to simply replace r in (11) by E~= 1 r(t), but it is ...
- **Contribution anchor:** p. 1 (1. Introduction), p. 2 (1. Introduction), p. 8 (5. Episodic REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms), p. 1 (1. Introduction), p. 8 (4. REINFORCE algorithms)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** While such algorithms are known to have a number of limitations, there are a number of reasons why their study can be useful.
- **p. 1 / 1. Introduction - extractive body cue:** The general framework of reinforcement learning encompasses a broad variety of problems ranging from various forms of function optimization at one extreme to learning control ...
- **p. 1 / 1. Introduction - extractive body cue:** Thus while it remains a useful research strategy to focus on limited forms of reinforcement learning problems simply to keep the problems tractable, it is ...
- **p. 2 / 1. Introduction - extractive body cue:** Also, to the extent that certain existing algorithms resemble the algorithms arising from such a gradient analysis, our understanding of them may be enhanced.
- **p. 15 / 8. Algorithm performance and other issues - extractive body cue:** 8.L Convergence properties A major limitation of the analysis performed here is that it does not immediately lead to prediction of the asymptotic properties of ...
- **p. 14 / 7.2. Backpropagating through random number generators - extractive body cue:** Unfortunately, even this property fails to hold in general.
- **p. 17 / 8. Algorithm performance and other issues - extractive body cue:** Choice of reinforcement baseline One important limitation of the analysis given here is that it offers no basis for choosing among various choices of reinforcement ...
- **Boundary to test:** 8.L Convergence properties A major limitation of the analysis performed here is that it does not immediately lead to prediction of the asymptotic properties of REINFORCE algorithms.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output mapping, and, with one limited exception, that ... | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | In those situations when it is known that unsatisfactory performance is being achieved it is reasonable to broaden this scale in order to take a coarsegrained view of the search space and ... | p. 17 (8. Algorithm performance and other issues), p. 15 (8. Algorithm performance and other issues) |
| Failure/limitation | 8.L Convergence properties A major limitation of the analysis performed here is that it does not immediately lead to prediction of the asymptotic properties of REINFORCE algorithms. | p. 15 (8. Algorithm performance and other issues), p. 14 (7.2. Backpropagating through random number generators) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 The results to be presented apply in general to any learner whose inputoutput mappings consists of a parameterized input-controlled distribution function from which outputs are randomly generated, and the corresponding algorithms modify ...를 In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output mapping, and, with one limited exception, that ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 8.L Convergence properties A major limitation of the analysis performed here is that it does not immediately lead to prediction of the asymptotic properties of REINFORCE algorithms.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output mapping, and, with one limited exception, that ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, Policy Gradient, REINFORCE`.
- **Reading predecessor in the generated track queue:** Q-Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Policy Gradient Methods for Reinforcement Learning with Function Approximation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 8.L Convergence properties A major limitation of the analysis performed here is that it does not immediately lead to prediction of the asymptotic properties of REINFORCE algorithms.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: A more general formulation of such an episodic learning task is also possible, where reinforcement is delivered to the network at each time step during the episode, not just at the end..
3. Compare against the body-reported baseline or a matched simpler baseline: In these studies, REINFORCE with reinforcement comparison was found to outperform all other algorithms investigated..
4. Report the body metric and its denominator/aggregation: One potentially useful feature of such a Gaussian unit is that the mean and variance of its output are individually controllable as long as separate weights (or perhaps inputs) are used to ....
5. Re-run the body-reported ablation/failure condition: WILLIAMS effect of connectivity between units is ignored; each unit in the network tries to determine the effect of changes of its output on changes in reinforcement independently of its effect on ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 9 (5. Episodic REINFORCE algorithms), p. 8 (5. Episodic REINFORCE algorithms), p. 8 (4. REINFORCE algorithms); the primary result is directionally consistent at p. 17 (8. Algorithm performance and other issues), p. 15 (8. Algorithm performance and other issues), p. 18 (8. Algorithm performance and other issues); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 article, present, analytical mechanism이 In these studies, REINFORCE with reinforcement comparison was found to outperform all other algorithms investigated. 대비 One potentially useful feature of such a Gaussian unit is that the mean and variance of its output ...을 개선하고, 8.L Convergence properties A major limitation of the analysis performed here is that it does not ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
