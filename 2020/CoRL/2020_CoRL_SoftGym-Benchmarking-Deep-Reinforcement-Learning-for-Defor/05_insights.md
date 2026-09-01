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

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 We benchmark a range of algorithms on these environments assuming different observation spaces for the policy, including full knowledge of the ground-truth state of the deformable object, a lowdimension state representation, and ...를 5.2 State Oracle Many robotic systems follow the paradigm of first performing state estimation and then using the estimated state as input to a policy.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 from a policy that always does nothing.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface for creating new environments.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, deformable object, Benchmark, Reinforcement Learning, simulation`.
- **Reading predecessor in the generated track queue:** Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** from a policy that always does nothing.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Thus, this evaluation points to a clear need for new methods development for image-based robot manipulation of deformable objects..
3. Compare against the body-reported baseline or a matched simpler baseline: While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for exploration, the result shows that there still exists a large ....
4. Report the body metric and its denominator/aggregation: Table 3: Task specific planning horizon for CEM B.2 SAC and CURL-SAC We use the CURL-SAC implementation from the released code3. Both Q-value network and the policy network are MLPs with 2 ....
5. Re-run the body-reported ablation/failure condition: from a policy that always does nothing..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction); the primary result is directionally consistent at p. 7 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, SoftGym, open-source mechanism이 While it outperforms the rest of the baselines due to the use of the segmentation map ... 대비 Table 3: Task specific planning horizon for CEM B.2 SAC and CURL-SAC We use the CURL-SAC implementation from ...을 개선하고, from a policy that always does nothing. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
