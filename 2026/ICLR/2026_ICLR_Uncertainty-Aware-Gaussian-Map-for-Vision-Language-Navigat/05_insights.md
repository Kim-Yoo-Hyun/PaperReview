# Insights — Uncertainty-Aware Gaussian Map for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=LPv59noPAy; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/246583. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 3 METHOD - extractive body cue:** To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Extensive ablation studies confirm the contribution of each component (§4.4).
- **p. 6 / 3 METHOD - extractive body cue:** This fusion enables the agent to jointly reason about geometric structure and perceptual confidence, thereby promoting reliable and uncertainty-aware decision-making.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In the same manner, semantic uncertainty is estimated by perturbing the semantic attributes of Gaussians, which reveals ambiguous interpretations and allows the agent to down-weight ...
- **p. 6 / 3 METHOD - extractive body cue:** Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling ...
- **p. 6 / 3 METHOD - extractive body cue:** To supervise SGM construction, we apply a pixel-wise rendering loss between the rendered outputs and ground-truth observations.
- **p. 3 / 3 METHOD - extractive body cue:** Based on these observations, the agent learns a navigation policy π(at/X, It, Dt) that predicts actions at ∈At, which includes navigable neighbor nodes, previously observed ...
- **Contribution anchor:** p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 6 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Despite these advances, existing agents typically ignore uncertainty in perception when making decisions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Their training recipes discourage expressing uncertainty or recognizing unreliable situations, instead incentivizing them to predict actions regardless of confidence [17].
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Brighter colors indicate higher uncertainty.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** High uncertainty in the distance; safer to detour right.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation already provides sufficient evidence of the target, ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** 5 illustrates our diverse perceptual forms. i) SGM preserves detailed geometric structures while maintaining high-fidelity rendering of the scene. ii) Geometric uncertainty reveals structural reliability, ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 12: Robustness to observation noise on R2R val unseen split. We evaluate an epistemic only variant (geometric + semantic), an aleatoric only variant (appearance), ...
- **Boundary to test:** Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation already provides sufficient evidence of the target, creating confusion about whether further steps are ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing the Kullback-Leibler (KL) divergence to true posterior ... | p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Reported outcome | On the val unseen split, it achieves an SR of 78% compared to 76% from VER [17] and improves SPL from 65% to 66%, corresponding to gains of 2% in SR and ... | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Failure/limitation | Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation already provides sufficient evidence of the target, creating confusion about whether further steps are ... | p. 22 (Figure/Table caption), p. 9 (4 EXPERIMENT) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Based on these observations, the agent learns a navigation policy π(at/X, It, Dt) that predicts actions at ∈At, which includes navigable neighbor nodes, previously observed nodes accessible via backtracking, and a [STOP] ...를 Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling and single-step action prediction to strengthen multimoda ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation already provides sufficient evidence of the target, creating confusion about whether further steps are ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing the Kullback-Leibler (KL) divergence to true posterior ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Vision-Language Model, 3D Vision, Navigation, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation already provides sufficient evidence of the target, creating confusion about whether further steps are ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: All datasets are built upon the Matterport3D simulator [80], and are split into train, val-seen, val-unseen, and test sets according to scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by Path Length (SPL)..
4. Report the body metric and its denominator/aggregation: For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by Path Length (SPL)..
5. Re-run the body-reported ablation/failure condition: Components R2R [1] REVERIE [28] # SGM 3DVM SR ↑ SPL ↑ SR ↑ RGS ↑ RGSPL ↑ 1 - - 72.22 60.41 46.98 32.15 23.03 2 ✓ - 76.21 64.57 50.20 ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (3 METHOD), p. 6 (3 METHOD), p. 3 (3 METHOD); the primary result is directionally consistent at p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 7 (4 EXPERIMENT); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 approximate, like, introduce mechanism이 For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success ... 대비 For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), ...을 개선하고, Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
