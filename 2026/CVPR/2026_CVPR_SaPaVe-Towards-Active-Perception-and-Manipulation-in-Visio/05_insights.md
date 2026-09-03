# Insights — SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy in ...
- **p. 2 / 1. Introduction - extractive body cue:** To address the limitations of fixed-viewpoint manipulation evaluation, we introduce the first simulated active manipulation benchmark, featuring 12 richly annotated tasks across 100 objects and ...
- **p. 4 / Model - extractive body cue:** To bridge this gap, we propose Universal Spatial Knowledge Injection, which efficiently leverages as much 3D information as possible to directly optimize the action output.
- **p. 4 / Model - extractive body cue:** Therefore, we propose Decoupled Action Heads and Camera Adapter to enable our model to acquire rich semantic active perception priors and retain general manipulation knowledge ...
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive body cue:** To fill this gap, we propose a large-scale, high-quality dataset, ActiveViewPose-200K, comprising 200k image-language and camera movement pairs (see Sec.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Given an observation Ot ∈O and a language instruction L ∈L, the policy predicts a joint action trajectory At = {Ahead,t, Aother,t} ∈A.
- **p. 3 / 3.2. Architecture - extractive body cue:** First, directly adding camera movement into the existing VLA action space would break the large-scale fixed-view manipulation priors learned from previous training.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (Model), p. 4 (Model), p. 5 (3.3. Two-Stage Training Strategy), p. 3 (3.1. Problem Formulation)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, this discretization hinders fine-grained camera control and manipulation, as it fails to connect high-level semantics with the continuous camera pose space.
- **p. 2 / 1. Introduction - extractive body cue:** To address the limitations of fixed-viewpoint manipulation evaluation, we introduce the first simulated active manipulation benchmark, featuring 12 richly annotated tasks across 100 objects and ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Unlike prior works that unify camera motion and manipulation into a single action space, we decouple them and propose a two-stage learning strategy for active ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At each timestep t, the observation Ot comprises the current RGB image It ∈RH×W ×3 and optional 3D geometric information Gt (e.g., depth maps and ...
- **p. 7 / 4.4. Comparison with existing VLA models - extractive body cue:** Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors.
- **p. 7 / 4.3. Fixed and Dynamic Cameras Evaluation - extractive body cue:** This result indicates that a fixed camera greatly limits the model's ability to explore the accessible space, leading to failures for active manipulation.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting viewpoints ...
- **Boundary to test:** Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy in a data-efficient way. • We introduce ActiveViewPose-200K, ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Table 3. Performance on active manipulation in real-world set- tings. We report the success rate (%) compared to the existing VLA models. Our approach achieves the best performance. | p. 7 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Failure/limitation | Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors. | p. 7 (4.4. Comparison with existing VLA models), p. 7 (4.3. Fixed and Dynamic Cameras Evaluation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Given an observation Ot ∈O and a language instruction L ∈L, the policy predicts a joint action trajectory At = {Ahead,t, Aother,t} ∈A.를 SaPaVe can process RGB images and task instructions and output camera movement and manipulation actions in a decoupled action space.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy in a data-efficient way. • We introduce ActiveViewPose-200K, ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, active perception, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Pick-and-Place Pick-and-Place Arti-Manip Arti-Manip π0 [6] 55 45 45 35 45.00 GR00T-N1 [5] 60 55 50 50 53.75 Ours 90 85 85 80 85.00 robot teleoperated dataset, including 4 task categories: Occluded/Out-of-View ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting viewpoints to reveal task-critical cues in cluttered ....
4. Report the body metric and its denominator/aggregation: For all experiments, we report the success rate..
5. Re-run the body-reported ablation/failure condition: We conduct a series of ablation experiments on 4 real-world tasks to evaluate the effectiveness of different components in our method..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (Model), p. 3 (3.1. Problem Formulation), p. 3 (3.2. Architecture); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.2. Semantic Active Perception Evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, threefold mechanism이 Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception ... 대비 For all experiments, we report the success rate.을 개선하고, Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
