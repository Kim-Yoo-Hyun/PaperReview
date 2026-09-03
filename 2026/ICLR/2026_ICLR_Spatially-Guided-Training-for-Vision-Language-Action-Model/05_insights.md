# Insights — Spatially Guided Training for Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eKhOrQWAVJ; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247957. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 METHODS We propose ST4VLA, a spatially guided training framework that bridges spatial understanding with embodied control through a novel two-stage training recipe 2.2.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address the fundamental gap between multimodal understanding and embodied control, we propose ST4VLA, a dual-system vision-language-action framework that explicitly integrates spatial priors into robot ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** (2025) showing that direct gradient flow between action and VLM modules may distort multimodal knowledge, we introduce a gradient decay factor within the querying transformer.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new a dual-system, end-to-end VLA framework based on Qwen2.5-VL, which can foster alignment between the optimization dynamics of the spatial grounding objective ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given a task instruction, the VLM planner produces latent plans through explicit spatial prompting, which then effectively guides the action expert to generate control signals. ...
- **Contribution anchor:** p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, a critical gap remains when transferring these capabilities to the physical domain, because robots must not only understand what an instruction means but also ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Prior work has approached this challenge through hierarchical robotic systems Huang et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address the fundamental gap between multimodal understanding and embodied control, we propose ST4VLA, a dual-system vision-language-action framework that explicitly integrates spatial priors into robot ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** ST4VLA substantially improves generalization to unseen objects, novel instructions, and out-of-distribution environments, outperforming strong baselines such as π0 Black et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The rigid separation between symbolic task structures and low-level motor control makes it difficult to scale automatically to complex and diverse tasks, and particularly limits ...
- **p. 36 / Figure/Table caption - extractive body cue:** Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure cases during real-world instruction-following pick-and-place tasks. As shown in ...
- **p. 38 / Figure/Table caption - extractive body cue:** Figure 25: Simulation data synthesis pipeline. The pipeline generates diverse robotic manipulation data from a large asset library, converts intermediate representations into VQA data, and ...
- **Boundary to test:** Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure cases during real-world instruction-following pick-and-place tasks. As shown in Figure 23. In some cases, the robot ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization with spatial grounding objectives, preserving ... | p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Reported outcome | Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et al. (2024) and GR00T N1.5 Bjorck et al. ... | p. 7 (Figure/Table caption), p. 20 (Figure/Table caption) |
| Failure/limitation | Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure cases during real-world instruction-following pick-and-place tasks. As shown in Figure 23. In some cases, the robot ... | p. 36 (Figure/Table caption), p. 38 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Noisy Actions Actions DiT - Actor Conditioned State (opt) Your task is to {instruction}.를 Spatial Planning Prompt VL-Input Sub-Task Planning Action Action VLM Planner DiT Actor Latent Planning Data Model Deployment Point Grounding A: The image shows a person standing in a bathroom, facing away from ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure cases during real-world instruction-following pick-and-place tasks. As shown in Figure 23. In some cases, the robot ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization with spatial grounding objectives, preserving ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure cases during real-world instruction-following pick-and-place tasks. As shown in Figure 23. In some cases, the robot ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 3.4 EVALUATION IN REAL-WORLD CLUTTERED-SCENE PICK-AND-PLACE We use the Franka Research 3 robot to evaluate the generalization performance of our model and baselines on the real-world pick-and-place tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et al. (2024) and GR00T N1.5 Bjorck et al. ....
4. Report the body metric and its denominator/aggregation: Figure 3: Ablation study on the effect of auxiliary spatial prompting during co-training. From left to right: (a) perception performance (IoU@0.5 on RefCOCO-g); (b) manipulation performance (Average Success Rate on WidowX); (c) ....
5. Re-run the body-reported ablation/failure condition: Figure 3: Ablation study on the effect of auxiliary spatial prompting during co-training. From left to right: (a) perception performance (IoU@0.5 on RefCOCO-g); (b) manipulation performance (Average Success Rate on WidowX); (c) ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 6 (3 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contrast, simple, spatial mechanism이 Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. ... 대비 Figure 3: Ablation study on the effect of auxiliary spatial prompting during co-training. From left to right: (a) ...을 개선하고, Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
