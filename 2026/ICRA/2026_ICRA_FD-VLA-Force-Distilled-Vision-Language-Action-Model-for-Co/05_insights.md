# Insights — FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2602.02142. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the main contributions of this work are summarized as follows: • We propose the FD-VLA framework that injects a distilled force token into ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a novel FD-VLA framework that incorporates a distilled force token, rather than raw sensor signals, into the VLA model to ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual force signals during ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** The realization of FDM consists of two parallel branches, i.e., the prediction branch and actual force branch.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Rather than directly incorporating the raw force measurements into the VLM, we introduce the Force Distillation Module (FDM) that can predict a latent force representation ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Force Distillation Module (FDM) Our FDM generates a compact, state-aware force representation that can be seamlessly integrated into the VLA pipeline without requiring specialized tactile ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Overall Training Objective The overall objective of our FD-VLA framework combines two complementary components, i.e., a standard policy learning loss and a force-distillation loss, which ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables practical deployment on a wide range of robot platforms that lack force sensors, reducing hardware cost and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Moreover, the late-fusion mechanism limits fine-grained forcevision-state interactions, reducing tight perception-action coupling and generalization.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** This architecture allows our system to leverage the semantic richness of pretrained VLM while introducing stable, taskrelevant physical reasoning through force distillation, achieving both robustness ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Finally, FDM mitigates the noise and instability of raw sensor signals by learning a supervised latent embedding that serves as a denoised, taskrelevant proxy for ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Our model achieves consistently higher performance, which highlights the benefit of force distillation for accurate and robust manipulation.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For evaluation, each task was trained using a set of 50 demonstrations and subsequently evaluated over 30 independent test trials to ensure statistical robustness.
- **Boundary to test:** Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM and action expert. (Right) Our FD-VLA using ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, the main contributions of this work are summarized as follows: • We propose the FD-VLA framework that injects a distilled force token into the VLA model to improve contact-rich manipulation. ... | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, substantially outperforming both SmolVLA without force encoding (23.3%), DP3 (11.1%) and even π0 without ... | p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption) |
| Failure/limitation | Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM and action expert. (Right) Our FD-VLA using ... | p. 2 (Figure/Table caption), p. 4 (III. METHODOLOGY) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 The multimodal inputs of VLA include language instruction L, visual observation Vt, robot state St, and force Ft, where t denotes the timestamp.를 This allows them to map RGB inputs and natural-language instructions directly to low-level robot commands, while benefiting from strong This research is supported by National Robotics Programme (NRP) 2.0 funding initiative "Domain-speci ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM and action expert. (Right) Our FD-VLA using ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, the main contributions of this work are summarized as follows: • We propose the FD-VLA framework that injects a distilled force token into the VLA model to improve contact-rich manipulation. ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM and action expert. (Right) Our FD-VLA using ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Results are averaged over 30 evaluation episodes per task..
3. Compare against the body-reported baseline or a matched simpler baseline: DP3 is selected as a strong diffusion-based control framework with a parameter scale comparable to ours, which provides a capacity-matched baseline that excels at generating precise motion trajectories. π0 represents the state-of-the-ar ....
4. Report the body metric and its denominator/aggregation: Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, substantially outperforming both SmolVLA without force encoding (23.3%), DP3 (11.1%) and even π0 without ....
5. Re-run the body-reported ablation/failure condition: We compare FD-VLA (ours) with SmolVLA, π0 and DP3, SmolVLA and π0 are evaluated with and without force inputs..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY); the primary result is directionally consistent at p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, main, contributions mechanism이 DP3 is selected as a strong diffusion-based control framework with a parameter scale comparable to ours, ... 대비 Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, ...을 개선하고, Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
