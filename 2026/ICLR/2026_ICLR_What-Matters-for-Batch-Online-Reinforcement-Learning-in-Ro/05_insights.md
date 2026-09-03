# Insights — What Matters for Batch Online Reinforcement Learning in Robotics?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10006859; PDF retrieval source: https://arxiv.org/pdf/2505.08078. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** On top of the recipe, we propose a simple practical addition to induce even more diversity and achieve better sample efficiency: applying a small amount ...
- **p. 2 / 1 Introduction - extractive body cue:** Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function ...
- **p. 5 / 3 Preliminaries - extractive body cue:** In Figure 3, we present the average normalized returns over iterations of batch online RL for each algorithm class on our six tasks.
- **p. 5 / 3 Preliminaries - extractive body cue:** Based on our results, in Section 5 we present a recipe for batch online RL, and demonstrate the practicality of the recipe on a challenging ...
- **p. 6 / 3 Preliminaries - extractive body cue:** We present the results of data scaling in Figure 5.
- **p. 8 / 3 Preliminaries - extractive body cue:** This is in contrast to batch online RL, where to leverage diversity of the online data, the initial model needs to have captured enough of ...
- **p. 5 / 3 Preliminaries - extractive body cue:** For all of the algorithm classes, we use a diffusion-based policy as the default.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 8 (3 Preliminaries)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Learning from autonomously collected data for policy improvement, however, remains a significant challenge in robot learning as current algorithms struggle to fully leverage this autonomous ...
- **p. 1 / 1 Introduction - extractive body cue:** Although recent works have focused on mitigating this gap by proposing large robotic datasets [1, 2], robot learning continues to operate under a substantially smaller ...
- **p. 2 / 1 Introduction - extractive body cue:** IL methods have inherent limitations in their ability to leverage suboptimal demonstrations within autonomously collected datasets, while methods based on weighted or filtered IL often ...
- **p. 3 / 3 Preliminaries - extractive body cue:** Robotics operates under a smaller data regime than other fields due to the difficulty in obtaining data.
- **p. 4 / 3 Preliminaries - extractive body cue:** The size of D0 varies from 5 to 100 demonstrations depending on the task difficulty; we choose this size such that the base policy π0 ...
- **p. 9 / 6 Discussion - extractive body cue:** Our work presents a general recipe on batch online RL, though it does have a number of limitations.
- **p. 9 / 6 Discussion - extractive body cue:** 7 Limitations In this work, we empirically analyze the key axes that affect performance in batch online RL, demonstrating that the general recipe of value-based ...
- **Boundary to test:** Our work presents a general recipe on batch online RL, though it does have a number of limitations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | On top of the recipe, we propose a simple practical addition to induce even more diversity and achieve better sample efficiency: applying a small amount of temporally correlated noise modeled by the ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 3: Normalized returns of different algorithm classes over multiple iterations of improvement. Value-based RL significantly outperforms IL and filtered-IL. Runs are 3 seeds, 100 evaluations. Based on our results, in Section ... | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Failure/limitation | Our work presents a general recipe on batch online RL, though it does have a number of limitations. | p. 9 (6 Discussion), p. 9 (6 Discussion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function on the autonomous data, and perform implicit ...를 Intuitively, this makes sense because value-based RL methods can use the Q-function to determine which states and actions are desirable even in failure trajectories, thus allowing the policy to learn from a ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Our work presents a general recipe on batch online RL, though it does have a number of limitations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: On top of the recipe, we propose a simple practical addition to induce even more diversity and achieve better sample efficiency: applying a small amount of temporally correlated noise modeled by the ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, batch online RL, real robot`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Our work presents a general recipe on batch online RL, though it does have a number of limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Based on our results, in Section 5 we present a recipe for batch online RL, and demonstrate the practicality of the recipe on a challenging real-world robotic task of hanging tape on ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 11: Normalized returns of value-based RL compared with IL, filtered-IL, and temporally- correlated noise at different data scales, shown for each task. From Figure 11, we see that value-based RL scales ....
4. Report the body metric and its denominator/aggregation: However, directly adding noise may not be applicable in some deployment settings, though we find empirically that adding a small amount of noise only changes the success rate of the policy marginally..
5. Re-run the body-reported ablation/failure condition: We separate policy extraction into two distinct categories, explicit policy extraction and implicit policy extraction, to analyze the effect of extraction method on performance..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 8 (3 Preliminaries), p. 5 (3 Preliminaries); the primary result is directionally consistent at p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (3 Preliminaries); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 recipe, simple, practical mechanism이 Figure 11: Normalized returns of value-based RL compared with IL, filtered-IL, and temporally- correlated noise at ... 대비 However, directly adding noise may not be applicable in some deployment settings, though we find empirically that adding ...을 개선하고, Our work presents a general recipe on batch online RL, though it does have a number ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
