# Insights — CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose Chain-of-Affordance, namely CoA-VLA, a novel perspective on generalizing model reasoning at test-time, and leverage such generated reasoning to facilitate the ...
- **p. 2 / 1. Introduction - extractive body cue:** Our method leverages visual affordance in robot learning, conceptualizing various actions and interactions with objects or the environment that a robot can perform based on ...
- **p. 3 / 4. Methodology - extractive body cue:** In Section 4.2, we present two formats for representing the chain of affordances: a text format and an image format.
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive body cue:** In our framework, spatial affordance is operationalized as actionable destinations-discrete 2D coordinates representing feasible interaction zones.
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive body cue:** By employing a dynamic affordance selection mechanism, our method avoids generating redundant affordances at every timestep. object to interact with and where it is located, ...
- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive body cue:** This module bridges the gap between abstract language-based reasoning and pixel-level visual context, enabling the policy model to synergistically leverage both modalities for robust, context-aware ...
- **p. 3 / 4. Methodology - extractive body cue:** We then discuss how these representations can be integrated into the policy learning process.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Methodology), p. 4 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, current approaches often rely heavily on high-level planning or task decomposition by off-the-shelf Large language models(LLMs) or Vision language models (VLMs), limiting models from ...
- **p. 8 / 5.3. More Experiments - extractive body cue:** Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability.
- **p. 8 / 5.3. More Experiments - extractive body cue:** Collision avoidance is essential for safe and effective physical interactions, as improper maneuvers can lead to significant damage or even catastrophic outcomes.
- **Boundary to test:** Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we propose Chain-of-Affordance, namely CoA-VLA, a novel perspective on generalizing model reasoning at test-time, and leverage such generated reasoning to facilitate the policy learning process. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Specifically, CoA-VLA achieves an overall success rate of 79.8%, outperforming OpenVLA, the previous best-performing method, by a margin of 3.3%. | p. 7 (5.2. Evaluation on Simulation), p. 7 (5.2. Evaluation on Simulation) |
| Failure/limitation | Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability. | p. 8 (5.3. More Experiments), p. 8 (5.3. More Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Our objective is to learn an intermediate language output z : O ↑G ↓Z that maps observations and task descriptions to affordance reasoning in natural language.를 This module bridges the gap between abstract language-based reasoning and pixel-level visual context, enabling the policy model to synergistically leverage both modalities for robust, context-aware action generation.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we propose Chain-of-Affordance, namely CoA-VLA, a novel perspective on generalizing model reasoning at test-time, and leverage such generated reasoning to facilitate the policy learning process.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: LIBERO is a robot learning benchmark comprising over 130 language-conditioned manipulation tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: Compared to our baseline model, which employs vanilla reasoning, our method achieves a 14.29% increase in accuracy..
4. Report the body metric and its denominator/aggregation: We report the success rate and standard error for four task suites..
5. Re-run the body-reported ablation/failure condition: Detailed descriptions of each task and the experimental setup, and our ablation experiments are provided in the Appendix..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (4.1. Definition of Chain-of-Affordance), p. 3 (4. Methodology), p. 5 (4.1. Definition of Chain-of-Affordance); the primary result is directionally consistent at p. 7 (5.2. Evaluation on Simulation), p. 7 (5.2. Evaluation on Simulation), p. 6 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Chain-of-Affordance, namely, CoA-VLA mechanism이 Compared to our baseline model, which employs vanilla reasoning, our method achieves a 14.29% increase in ... 대비 We report the success rate and standard error for four task suites.을 개선하고, Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
