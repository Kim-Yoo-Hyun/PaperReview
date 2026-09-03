# Insights — ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION.
- **p. 2 / 1. Introduction - extractive body cue:** Instead, motivated by OmniDrive [61], which extracts features through Q-Former-styled architecture, we introduce QT-Former, a query-based temporal module.
- **p. 3 / 3.1. QT-Former - extractive body cue:** To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a querybased temporal module, ...
- **p. 4 / 3.3. Generative Planner - extractive body cue:** Inspired by the generative domain, we introduce a generative planner to bridge the gap between the reasoning and action space.
- **p. 4 / 3.2. Large Language Model - extractive body cue:** The LLM is pivotal to our framework because the highquality reasoning of the current driving scenario is necessary to instruct the generator to generate a ...
- **p. 4 / 3.3. Generative Planner - extractive body cue:** As there are essential differences in the distribution between the reasoning space of VLM and the action space of trajectory, we use the VAE [29] ...
- **p. 4 / 3.1. QT-Former - extractive body cue:** Then they interact with image features Fm with 3D positional encoding [38] Pm in the cross-attention (CA) module.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. QT-Former), p. 4 (3.3. Generative Planner), p. 4 (3.2. Large Language Model), p. 4 (3.3. Generative Planner)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Besides, limited by the intrinsic autoregressive mechanism of VLMs, the trajectories these method output lack diversity [54], which is inconsistent with the natural uncertainty of ...
- **p. 1 / 1. Introduction - extractive body cue:** Nevertheless, these methods lack the common sense to complete complex causal reasoning.
- **p. 2 / 1. Introduction - extractive body cue:** Other methods endeavor to bridge the gap via utilizing VLM output meta-action (e.g., turn left) to assist classic E2E methods [27, 41], as shown in ...
- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** For open-loop evaluation, we use the L2 distance error and the collision rate.
- **p. 6 / 25.00 71.11 78.33 30.00 69.15 54.72(+16.12) - extractive body cue:** On the other hand, our model falls behind DriveAdapter in Merging and Give Way, which shows that ORION is not good at making lane-changing decisions.
- **p. 6 / 4.5. Ablation Study - extractive body cue:** The plain text paradigm performs the worst (42.23 DS, 13.14% SR, and 15.39% mean ability), indicating the limitations of plain text output in closed-loop driving ...
- **p. 8 / 4.5. Ablation Study - extractive body cue:** The model cannot obtain both reasoning and planning capabilities with single-task training.
- **Boundary to test:** For open-loop evaluation, we use the L2 distance error and the collision rate.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] by a large margin and makes an improvement of +18.32 ... | p. 7 (4.5. Ablation Study), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |
| Failure/limitation | For open-loop evaluation, we use the L2 distance error and the collision rate. | p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 2, the user instruction Xq, including scene description, history information review, scene analysis, and action reasoning, is first encoded into language tokens xq ∈RL×C by the text tokenizer, where L is the ...를 The former only uses a single token encoded in the reasoning space from the perspective of the ego vehicle as input, aiming to bridge the gap between reasoning space and action space.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 For open-loop evaluation, we use the L2 distance error and the collision rate.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For open-loop evaluation, we use the L2 distance error and the collision rate.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Additionally, we compare our method with other baselines on nuScenes [7] open-loop evaluation (details in Appendix)..
3. Compare against the body-reported baseline or a matched simpler baseline: By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] by a large margin and makes an improvement of +18.32 ....
4. Report the body metric and its denominator/aggregation: Bench2drive includes five metrics for closed-loop evaluation: Driving Score (DS), Success Rate (SR), Efficiency, Comfortness, and Multi-Ability..
5. Re-run the body-reported ablation/failure condition: We then investigate the effect of employing different generative planners to bridge the reasoning-action space..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.1. QT-Former), p. 4 (3.3. Generative Planner), p. 4 (3.1. QT-Former); the primary result is directionally consistent at p. 7 (4.5. Ablation Study), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 tackle, problem, hOlistic mechanism이 By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already ... 대비 Bench2drive includes five metrics for closed-loop evaluation: Driving Score (DS), Success Rate (SR), Efficiency, Comfortness, and Multi-Ability.을 개선하고, For open-loop evaluation, we use the L2 distance error and the collision rate. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
