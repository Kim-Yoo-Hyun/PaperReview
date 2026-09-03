# Insights — From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yngvAamNQi; PDF retrieval source: https://openreview.net/pdf/bf1367fb5cae44ded2c3d2914a515610024c5414.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose FSD (From Seeing to Doing), a novel framework that generates these visual intermediate representations through structured spatial reasoning (Fig.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions include: 1) A novel paradigm where VLM reasoning generates versatile visual aids, enabling either direct open-loop control or serving as the high-level planner ...
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** Based on these considerations, we introduce Spatial Relationship-Focused Visual Chain-of-thought (SrCoT).
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** While VLMs struggle to directly map future actions to image coordinates, our method leverages known object relationships as reference points for multi-hop analysis, simplifying the ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** Therefore, we propose a self-consistency mechanism to further align FSD capabilities in 5
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** The training process unfolds in two stages: General Spatial Reasoning Enhancement: In the first stage, we use our Level 1-3 data to cultivate the model's ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** For visual trace generation (Level 5 Dataset), we employ a two-stage approach: first applying self-supervised keypoint extraction (Huang et al., 2024) to identify grasp points ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (4. How to avoid collisions?), p. 4 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?), p. 6 (4. How to avoid collisions?)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** FSD unlocks visual aids reasoning and generation through Spatial RelationshipFocused CoT, demonstrating exceptional generalization capabilities that enable zero-shot robot manipulation and achieving remarkable performance across ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We attribute the limited generalization in existing VLA-based systems to two fundamental challenges: data scarcity and heterogeneity.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this generalization gap, the community has explored several paradigms.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** FSD is an enhanced affordance-based VLA that generalizes effectively to new instructions and scenes through its reasoning abilities.
- **p. 10 / 7 CONCLUSION - extractive body cue:** More limitations and future works are in App.J.
- **p. 34 / Figure/Table caption - extractive body cue:** Figure 17: Visual comparison demonstrating the effectiveness of Self-Consistency Alignment. It is worth noting that without self-consistent alignment, the model's textual reasoning process is logically ...
- **p. 10 / 7 CONCLUSION - extractive body cue:** We acknowledge limitations, such as the reliance on 2D trajectory generation and constraints from training data quality.
- **Boundary to test:** More limitations and future works are in App.J.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To this end, we propose FSD (From Seeing to Doing), a novel framework that generates these visual intermediate representations through structured spatial reasoning (Fig. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Type Model Put Spoon on Towel Put Carrot on Plate Stack Green Block on Yellow Block Put Eggplant in Yellow Basket Avg End-to-end VLA Octo (Team et al., 2024) 41.7 8.2 0.0 ... | p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Failure/limitation | More limitations and future works are in App.J. | p. 10 (7 CONCLUSION), p. 34 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 A driving force behind robotics research is the pursuit of generalization: creating agents capable of versatile action across diverse robotic platforms, extending beyond familiar tasks, objects, and environments while adapting to dynami ...를 End-to-end VLAs (Black et al., 2024; Brohan et al., 2023) attempt a direct mapping from multimodal inputs to low-level actions, but the disconnect between pre-trained cyberspace data and physical action modalities can ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 More limitations and future works are in App.J.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To this end, we propose FSD (From Seeing to Doing), a novel framework that generates these visual intermediate representations through structured spatial reasoning (Fig.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Vision-Language Model, Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** More limitations and future works are in App.J.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For Doing, we conducted zero-shot manipulation experiments in both SimplerEnv (Li et al., 2024c) simulation and real-world xArm robotic platforms to assess its practical generalization performance..
3. Compare against the body-reported baseline or a matched simpler baseline: 3, FSD significantly outperforms all baselines in generating precise spatial affordances and visual traces..
4. Report the body metric and its denominator/aggregation: Specifically, FSD achieves 61.82% accuracy on VABench-P, over 3x higher than RoboPoint (19.09%) and attains significantly lower error rates with a better LLM Score on VABench-V..
5. Re-run the body-reported ablation/failure condition: Table 8: Ablation study on the impact of Stage 1 training. We compare the full FSD model against a variant trained without the foundational spatial understanding stage (Levels 1-3)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?), p. 1 (ABSTRACT); the primary result is directionally consistent at p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 FSD, Seeing, Doing mechanism이 3, FSD significantly outperforms all baselines in generating precise spatial affordances and visual traces. 대비 Specifically, FSD achieves 61.82% accuracy on VABench-P, over 3x higher than RoboPoint (19.09%) and attains significantly lower error ...을 개선하고, More limitations and future works are in App.J. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
