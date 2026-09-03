# Insights — Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ULTWUuGhC3; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245105. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The interleaved format enables robust zeroshot generalization to novel objects and user-provided sketches unseen during training.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (1) We introduce Interleave-VLA: a lightweight, transferable paradigm that enhances the generalization capability of current text input VLA models with interleaved image-text instructions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This enables training Interleave-VLA with real-world interaction data and diverse visual instruction types.
- **p. 1 / ABSTRACT - extractive body cue:** Building on this insight, we introduce Interleave-VLA, a robot learning paradigm extending interleaved image-text instructions from digital world to directly generating continuous action sequences in ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this limitation, we first build a high-quality interleaved image-text datasets, crucial for training multimodal models.
- **p. 1 / ABSTRACT - extractive body cue:** It offers a natural, flexible, and model-agnostic paradigm that extends state-of-the-art vision-language-action (VLA) models with minimal modifications while achieving strong zero-shot generalization.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In order to bridge the gap of the lack of image-text interleaved datasets in robotic manipulation, we develop a pipeline to automatically construct interleaved instructions ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, current VLA models (Brohan et al., 2023; Kim et al., 2024; Black et al., 2024) remain predominantly trained on text-only instructions-a setting we refer ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We summarize our key takeaways below: • Generalization failures in VLAs often stem from attentional hallucinations, which we summarized as attentional bias, diffused attention, and ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (1) We introduce Interleave-VLA: a lightweight, transferable paradigm that enhances the generalization capability of current text input VLA models with interleaved image-text instructions.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - 2, it is typically the cost of Text-VLA model. ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** (2) What are the common failure modes of Text-VLA, and how does Interleave-VLA address them?
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For quantitative breakdown of failure modes, please refer to Figure 11.
- **Boundary to test:** Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - 2, it is typically the cost of Text-VLA model. Interleave-VLA takes in more images because of ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling existing VLAs to process interleaved inputs without ... | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Reported outcome | Table 13: Detailed evaluation results on 9 Out-of-Domain generalization tasks based on SimplerEnv. Success rates (%) are reported for π0, Interleave-VLA (adapted from π0), and Interleave-VLA co- trained with our Open Interleaved ... | p. 27 (Figure/Table caption), p. 10 (4 EXPERIMENTS) |
| Failure/limitation | Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - 2, it is typically the cost of Text-VLA model. Interleave-VLA takes in more images because of ... | p. 22 (Figure/Table caption), p. 6 (4 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 To develop a general and practical robot policy capable of acting on interleaved image-text instructions in the real world, a straightforward solution is to build upon VLA (Kim et al., 2024; O'Neill ...를 (c) It enables flexible, zero-shot instruction following with cropped images, web photos, and hand-drawn sketches for practical and intuitive human-robot interaction.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - 2, it is typically the cost of Text-VLA model. Interleave-VLA takes in more images because of ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling existing VLAs to process interleaved inputs without ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Robotics, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - 2, it is typically the cost of Text-VLA model. Interleave-VLA takes in more images because of ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Notably, although the pretraining dataset does not include FANUC robot arm data, it still enables strong cross-embodiment transfer to FANUC..
3. Compare against the body-reported baseline or a matched simpler baseline: In contrast, Interleave-VLA outperforms Text-VLA baselines by leveraging in-context visual grounding and cross-modality training to reduce attentional hallucinations..
4. Report the body metric and its denominator/aggregation: Table 8: Performance across sketch styles. Success Rate and Intention Accuracy (in %) of Interleave-VLA when the target object is specified by sketches with different levels of clarity and ambiguity. subsequently corrects ....
5. Re-run the body-reported ablation/failure condition: Pretraining on the Interleaved X-Embodiment dataset significantly boosts performance through effective crossembodiment transfer, reducing the need for laborious data collection..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT); the primary result is directionally consistent at p. 27 (Figure/Table caption), p. 10 (4 EXPERIMENTS), p. 24 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 illustrated, Figure, Interleave-VLA mechanism이 In contrast, Interleave-VLA outperforms Text-VLA baselines by leveraging in-context visual grounding and cross-modality training to reduce ... 대비 Table 8: Performance across sketch styles. Success Rate and Intention Accuracy (in %) of Interleave-VLA when the target ...을 개선하고, Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
