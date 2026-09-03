# Insights — Scaffolding Dexterous Manipulation with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PdRf0O7baQ; PDF retrieval source: https://arxiv.org/pdf/2506.19212.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.
- **p. 2 / 1 Introduction - extractive body cue:** Building upon this insight, we introduce a framework for learning manipulation policies for dexterous robot hands with VLM-generated motion plans and residual RL.
- **p. 2 / 1 Introduction - extractive body cue:** Across 8 tasks, our method achieves close performance in both success rate and generalization to handcrafted, oracle plans despite requiring no manual reward engineering.
- **p. 1 / Abstract - extractive body cue:** Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies.
- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. 𝑥1:𝑇 1 𝑥1:𝑇 ...
- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** In this section, we describe how we use the plan τ to further guide the learning and exploration of πl through the reward function, policy ...
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** Instead, we use ˜w1:T in the policy parameterization itself.
- **Contribution anchor:** p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** To avoid both data scarcity and the embodiment gap, a combination of reinforcement learning (RL) and sim-to-real transfer has emerged as a promising approach by ...
- **p. 1 / 1 Introduction - extractive body cue:** The prevailing approach for training generalist policies - imitation learning from demonstrations [5, 49] - has achieved limited success with robot hands, primarily due to ...
- **p. 2 / 1 Introduction - extractive body cue:** Though demonstration tracking overcomes the design challenges associated with RL, it paradoxically re-introduces the same dependence on demonstrations we sought to avoid in the first ...
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our method across a suite of challenging dexterous manipulation tasks in simulation requiring semantic understanding, human knowledge about concepts like "hammering", and precise ...
- **p. 8 / 4 Experiments - extractive body cue:** To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in Fig.
- **p. 8 / 4 Experiments - extractive body cue:** Our analysis reveals that the most significant failure mode is incomplete trajectory tracking, occurring in 26% of the rollouts.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty reflects the standard error. Our method performs ...
- **Boundary to test:** To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in Fig.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards. | p. 1 (Abstract), p. 2 (1 Introduction) |
| Reported outcome | Figure 5: (Left) The performance of our method as we iteratively refine the high-level policy πh by providing successful plans τ in-context. (Right) The projected 3D plans on the evaluation set for ... | p. 8 (Figure/Table caption), p. 23 (Figure/Table caption) |
| Failure/limitation | To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in Fig. | p. 8 (4 Experiments), p. 8 (4 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. 𝑥1:𝑇 1 𝑥1:𝑇 2 ෥𝑤1:𝑇 Action (𝑤𝑡+ Δ𝑤𝑡, 𝑞𝑡) Residual ...를 We learn πl using residual reinforcement learning [16, 26], which we formalize through a "plan" conditioned MDP on top of the low-level observation space Ol and action space A with horizon T.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in Fig.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Vision-Language Model, Robotics, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in Fig.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The low-level policy is trained entirely in simulation using a digital twin of the real-world environment, and then executed in the real-world, conditioned on the generated trajectories..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 3: A depiction of the eight tasks used for evaluation. Each task belongs to one of four overarching categories. Methods Given the novelty of our problem setting, there are few applicable ....
4. Report the body metric and its denominator/aggregation: Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty reflects the standard error. Our method performs comparably to the oracle with perfectly scripted ....
5. Re-run the body-reported ablation/failure condition: Figure 11: Effect of Gaussian noise on VLM predictions in the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty indicates the standard error. The performance of our ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 23 (Figure/Table caption), p. 9 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Moreover, showcase, transfers mechanism이 Figure 3: A depiction of the eight tasks used for evaluation. Each task belongs to one ... 대비 Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty ...을 개선하고, To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
