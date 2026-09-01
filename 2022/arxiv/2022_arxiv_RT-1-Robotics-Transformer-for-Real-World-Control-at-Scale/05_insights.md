# Insights — RT-1: Robotics Transformer for Real-World Control at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.06817; PDF retrieval source: https://arxiv.org/pdf/2212.06817. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 3 Hz - extractive body cue:** We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 2 (a), consists of partial counters and is constructed for large scale data collection.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Our training data consists of human-provided demonstrations, and we annotate each episode with a textual description of the instruction that the robot just performed.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** Our primary dataset consists of ∼130k robot demonstrations, collected with a fleet of 13 robots over the course of 17 months.
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** The Transformer is a decoder-only sequence model with 8 self-attention layers and 19M total parameters that outputs action tokens.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 5 RT-1: ROBOTICS TRANSFORMER In this section, we describe how we tokenize the images, text, and actions, and then discuss the RT-1 model architecture.
- **Contribution anchor:** p. 2 (3 Hz), p. 1 (ABSTRACT), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects?
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Although recent years have seen several large multitask robot policies proposed in the literature (Reed et al., 2022; Jang et al., 2021), such models often ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** We evaluate the performance of our policies across these different environments, measuring the policy's performance and ability to generalize.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 4 SYSTEM OVERVIEW The goal of this work is to build and demonstrate a general robot learning system that can absorb large amounts of data ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** (2022), we do not patchify the images into visual tokens prior to feeding them to our Transformer backbone.
- **p. 30 / Figure/Table caption - extractive body cue:** Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness to distractors and backgrounds. for all the models, and ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Second, it does not use a pre-trained text embedding to encode the language string.
- **Boundary to test:** Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness to distractors and backgrounds. for all the models, and therefore we focus our evaluation on just ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations to be ... | p. 2 (3 Hz), p. 1 (ABSTRACT) |
| Reported outcome | Table 5: Experimental results for mixing data from two different robots. Incorporating Kuka bin- picking data from QT-Opt (Kalashnikov et al., 2018) in RT-1 minimally impacts the standard class- room evaluation performance ... | p. 13 (Figure/Table caption), p. 13 (6 EXPERIMENTS) |
| Failure/limitation | Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness to distractors and backgrounds. for all the models, and therefore we focus our evaluation on just ... | p. 30 (Figure/Table caption), p. 8 (6 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 RT-1 takes a short sequence of images and a natural language instruction as input and outputs an action for the robot at each time step.를 We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations to be ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness to distractors and backgrounds. for all the models, and therefore we focus our evaluation on just ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations to be ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `VLA and generalist robot policies`; tags: `VLA, Robotics, Imitation Learning`.
- **Reading predecessor in the generated track queue:** PaLM-E: An Embodied Multimodal Language Model (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness to distractors and backgrounds. for all the models, and therefore we focus our evaluation on just ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: It also improves real-world generalization on simulated objects used with skills seen only in the real world (+26%), e.g. "move X to Y" where X only appeared in simulated "pick X" task. ....
3. Compare against the body-reported baseline or a matched simpler baseline: (Appendix Section D.4) Throughout this section we will compare to two baseline state of the art architectures, Gato (Reed et al., 2022) and BC-Z (Jang et al., 2021)..
4. Report the body metric and its denominator/aggregation: We evaluate the success rate in experiments to measure performance on training instructions, generalization to unseen instructions, robustness to backgrounds and distractors, and performance in long-horizon scenarios, as detailed below..
5. Re-run the body-reported ablation/failure condition: Table 5: Experimental results for mixing data from two different robots. Incorporating Kuka bin- picking data from QT-Opt (Kalashnikov et al., 2018) in RT-1 minimally impacts the standard class- room evaluation performance ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (3 Hz), p. 6 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES); the primary result is directionally consistent at p. 13 (Figure/Table caption), p. 13 (6 EXPERIMENTS), p. 12 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 novel, architecture, call mechanism이 (Appendix Section D.4) Throughout this section we will compare to two baseline state of the art ... 대비 We evaluate the success rate in experiments to measure performance on training instructions, generalization to unseen instructions, robustness ...을 개선하고, Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
