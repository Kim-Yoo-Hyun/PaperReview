# Insights — GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/fce176458ff542940fa3ed16e6f9c852-Abstract-Conference.html; PDF retrieval source: https://openreview.net/pdf/ecd829e279f0682dcfeefecc82736686079eb078.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, inspired by the approach of introducing task sub-goals to achieve efficient execution in robotic manipulation (Black et al., 2024; Kang et al., ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3) We propose a new action diffusion framework, GravMAD, guided by GravMaps.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Our method combines the learning power of diffusion architectures with the generalization of VLMs.
- **p. 4 / 3 METHOD - extractive body cue:** In this section, we introduce GravMAD, a multi-task, sub-goal-driven, language-conditioned diffusion framework for 3D manipulation, as shown in Fig.
- **원문 대조:** 세 번째 prediction head는 gripper의 open/close 상태를 예측하며 ground-truth openness에 대한 binary cross-entropy로 학습한다. Position·rotation noise head의 L1 loss 및 subgoal auxiliary head와 구분된다. ([PDF p. 7](https://arxiv.org/pdf/2409.20154#page=7), §3, Eq. (3)).
- **p. 7 / 3 METHOD - extractive body cue:** A self-attention layer then refines this representation to produce end-effector contextual features.
- **Contribution anchor:** p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (3 METHOD), p. 7 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, these policies often lack the language understanding and generalization abilities of foundation models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, this decoupling often leads to a limited understanding of scenes and manipulation tasks (Huang et al., 2024), allowing robots to conceptually grasp tasks but ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these policies often overfit to specific tasks (Xie et al., 2024; Zhang et al., 2024), leading to significant performance degradation or even failure when ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Recent works have combined the reasoning capabilities of foundation models with fine-grained control in 3D manipulation to overcome this limitation (Huang et al., 2024; Sharan ...
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected labels. identify ideal areas, leading to imprecise ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** During testing, except for the novel task "push buttons light", which must be completed in 3 time steps, all other tasks must be completed in ...
- **Boundary to test:** Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected labels. identify ideal areas, leading to imprecise contextual information from the Detector module for ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies. | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | GravMAD (Manual) outperforms Act3D and Voxposer across all tasks and exceeds the best baseline, 3D Diffuser Actor, in 9 out of 12 tasks, with an average success rate improvement of 13.36%. | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Failure/limitation | Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected labels. identify ideal areas, leading to imprecise contextual information from the Detector module for ... | p. 26 (Figure/Table caption), p. 8 (4 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Our goal is to learn a policy π : (O, L, G) 7→A, which maps observations ot, sub-goals gt, and instructions ℓto actions at.를 For each keypose, the corresponding observation-action pair (oKip, aKip) is passed to the function SK, which outputs a Boolean value to determine whether the given keypose should be discovered as a sub-goal ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected labels. identify ideal areas, leading to imprecise contextual information from the Detector module for ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, 3D Vision, Diffusion, Imitation Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected labels. identify ideal areas, leading to imprecise contextual information from the Detector module for ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Additionally, we further validate GravMAD on 10 real-world robotic tasks, with details provided in Appendix D.6..
3. Compare against the body-reported baseline or a matched simpler baseline: Performance gains are compared to the best-performing baselines, indicated by underlines..
4. Report the body metric and its denominator/aggregation: Despite the Detector's coarse SoM positioning affecting GravMAD (VLM)'s performance, it still outperforms Act3D and Voxposer on all tasks, with a 0.91% higher average success rate than 3D Diffuser Actor..
5. Re-run the body-reported ablation/failure condition: Figure 4: Ablation Studies. We evaluate the impact of key design elements by reporting the average success rates across 12 base tasks and 8 novel tasks. In the results, "→" denotes replacement, ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (3 METHOD), p. 7 (3 METHOD), p. 18 (A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD); the primary result is directionally consistent at p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, leveraging mechanism이 Performance gains are compared to the best-performing baselines, indicated by underlines. 대비 Despite the Detector's coarse SoM positioning affecting GravMAD (VLM)'s performance, it still outperforms Act3D and Voxposer on all ...을 개선하고, Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
