# Insights — DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=VdwdU81Uzy; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/166841. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 3. Methodology - extractive body cue:** In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose a unified model, named DiffusionVLA (DiVLA in short), that integrates autoregression with a diffusion model.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, we propose a reasoning injection module, which reuses reasoning outputs and embeds them directly into the policy head, thus enriching the ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** We illustrate the training strategy and other techniques that we used to improve the efficiency and effectiveness of our method.
- **p. 5 / 3.1. Architecture - extractive body cue:** Unlike most autoregressive VLAs, which require a recursive setup - converting reasoning outputs into inputs for subsequent model runs - our method proposes a more ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** Because larger models typically needs more data for training, we use OXE and Droid together for pre-training DiVLA-72B.
- **p. 3 / 3. Methodology - extractive body cue:** Developing such an integrated model presents substantial challenges, with key issues centered on: (i) designing an architecture that seamlessly and efficiently integrates both autoregressive and ...
- **Contribution anchor:** p. 3 (3. Methodology), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.2. Model Design Choices), p. 5 (3.1. Architecture), p. 5 (3.2. Model Design Choices)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, simply combining these elements does not fully exploit the reasoning potential, as there is often an implicit gap between logical reasoning and actionable robot ...
- **p. 2 / 1. Introduction - extractive body cue:** However, despite the advantages of diffusion models for policy learning, they lack the reasoning capabilities crucial for VLA models to solve complex tasks effectively, a ...
- **p. 7 / 4.4. Behavior Analysis of Robot Foundation Model - extractive body cue:** Failure case analysis via self-generated reasoning.
- **p. 8 / 5. Conclusion - extractive body cue:** Additionally, we show that DiVLA has robust generalization capabilities, adapting effectively to new instructions, tasks, and environments.
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Experimental Results for Multi-Task Learning on Real Robot. We report the count of pre-trained trajectories. We also report the average success rate for ...
- **p. 5 / 4. Experiments - extractive body cue:** In Section 4.2, we compare DiVLA against other state-of-the-art models within a standard multi-task setting, assessing its performance in both in-distribution and out-of-distribution scenarios.
- **p. 6 / 4. Experiments - extractive body cue:** DiVLA is robust to visual changes in different scenarios.
- **Boundary to test:** Failure case analysis via self-generated reasoning.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in Section 3.2. | p. 3 (3. Methodology), p. 2 (1. Introduction) |
| Reported outcome | Figure 3: Experimental Results for Factory Sorting. We compared our DiVLA with Diffusion Policy, Octo, TinyVLA, and OpenVLA. DiVLA achieves the highest average success rate, outperforming the runner-up OpenVLA by 20.9%. lies ... | p. 5 (Figure/Table caption), p. 8 (4.6. Adapt to Real-World Bimanual Robot) |
| Failure/limitation | Failure case analysis via self-generated reasoning. | p. 7 (4.4. Behavior Analysis of Robot Foundation Model), p. 8 (5. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 These data contain only robotic actions, paired partially with observations and language instructions.를 By embedding reasoning directly within the policy model, we avoid the computational and operational complexities of iterative input-output cycles, enabling faster and more seamless reasoning incorporation.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Failure case analysis via self-generated reasoning.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in Section 3.2.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, Diffusion`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Failure case analysis via self-generated reasoning.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: (c) Seen Tableware (d) Unseen Tableware (a) Bimanual Robot Setup (b) Setup for Table Bussing (e) Seen Trash (f) Unseen Trash Figure 9: (a) Environmental setup for the bimanual robot, (b) Table ....
3. Compare against the body-reported baseline or a matched simpler baseline: Our method outperforms the state-of-the-art robot foundation models by a large margin..
4. Report the body metric and its denominator/aggregation: Our evaluation of these scenarios reveals that while all methods experience a decline in performance due to these visual changes, our method consistently maintains the highest average success rate across five different ....
5. Re-run the body-reported ablation/failure condition: Table 8: Ablation study on reasoning injection module. In-Distribution Model \ Tasks Task 1 Task 2 Task 3 Task 4 Task 5.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3. Methodology), p. 5 (3.2. Model Design Choices), p. 3 (3. Methodology); the primary result is directionally consistent at p. 5 (Figure/Table caption), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 8 (4.6. Adapt to Real-World Bimanual Robot); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 section, introduce, overall mechanism이 Our method outperforms the state-of-the-art robot foundation models by a large margin. 대비 Our evaluation of these scenarios reveals that while all methods experience a decline in performance due to these ...을 개선하고, Failure case analysis via self-generated reasoning. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
