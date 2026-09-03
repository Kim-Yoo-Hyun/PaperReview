# Insights — World Action Models are Zero-shot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.15922; PDF retrieval source: https://arxiv.org/pdf/2602.15922. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1. Introduction - extractive body cue:** Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present DreamZero, a 14B robot foundation model built upon a pretrained image-tovideo diffusion backbone (Team Wan, 2025).
- **p. 3 / 1. Introduction - extractive body cue:** To address the computational overhead inherent to video diffusion models, we introduce a suite of optimizations spanning three categories: (1) algorithmic improvements, including decoupled video ...
- **p. 2 / 1. Introduction - extractive body cue:** Consequently, we observe that this enables (1) effective learning from robot data that are heterogeneous trajectories collected during the execution of useful behaviors in real-world ...
- **p. 7 / 3.1. Model Architecture - extractive body cue:** We introduce autoregressive modeling only for the video modality to avoid error propagation coming from closed-loop action prediction.
- **p. 7 / 3.1. Model Architecture - extractive body cue:** To retain the generalization capability of video models, we introduce minimal additional parameters: state encoders, action encoders, and decoders.
- **p. 7 / 3.1. Model Architecture - extractive body cue:** Autoregressive generation possesses the following advantages: (1) it enables faster inference speed by utilizing KV-cache, (2) the policy model can leverage the visual observation history ...
- **Contribution anchor:** p. 3 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned ...
- **p. 2 / 1. Introduction - extractive body cue:** While VLAs successfully inherit linguistic priors to generalize across diverse language instructions, especially manipulating diverse objects (Brohan et al., 2023), their generalization to novel environments ...
- **p. 3 / 1. Introduction - extractive body cue:** We further find that diverse distribution of the training data is essential for generalization, outperforming multi-task repetitive data with the same amount of hours.
- **p. 3 / 1. Introduction - extractive body cue:** Moreover, the environment generalization of DreamZero is retained even after task-specific post-training, outperforming state-of-the-art VLAs by 10% on average task progress.
- **p. 19 / 6. Discussion and Future Work - extractive body cue:** While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion or ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 9: Zero-shot Generalization to Unseen Tasks. DreamZero achieves non-trivial task progress on 10 tasks absent from training, while VLAs struggle across both embodiments. alignment ...
- **p. 18 / 6. Discussion and Future Work - extractive body cue:** We leave this direction as future work.
- **Boundary to test:** While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion or fine assembly.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) with only 30 minutes of play data, ... | p. 3 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Figure 10: Posttraining Results. WAMs enable stronger post-training results across three tasks, indicating that environment generalization of DreamZero is retained after post-training. Q3. Do WAMs improve post-training performance? We i ... | p. 15 (Figure/Table caption), p. 16 (Figure/Table caption) |
| Failure/limitation | While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion or fine assembly. | p. 19 (6. Discussion and Future Work), p. 14 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 DreamZero jointly predicts video o𝑙:𝑙+𝐻and actions a𝑙:𝑙+𝐻conditioned on language instruction c, proprioceptive state q𝑙and visual observation including the current and the past history o0:𝑙 where 𝐻> 0 is a fixed horizon and ...를 Initialized from video diffusion models trained on web-scale video data, WAMs leverage rich spatiotemporal priors to jointly generate future frames and actions conditioned on language instructions and observations.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion or fine assembly.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) with only 30 minutes of play data, ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, VLA, world model, zero-shot policy, action representation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion or fine assembly.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: As shown in Figure 6, each episode averages around 4.4 minutes and encompasses approximately 42 subtasks-significantly longer-horizon than typical robotic manipulation datasets (Khazatsky et al., 2024; Walke et al., 2023)..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 2: Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that the predicted actions closely align with the generated video. The examples are from totally unseen tasks. ....
4. Report the body metric and its denominator/aggregation: Table 2: Cross-Embodiment Transfer Results. Average task progress on unseen tasks (± standard error). Both transfer settings improve over baseline (result from Table 9) using only 10-20 minutes of video-only demonstration data. ....
5. Re-run the body-reported ablation/failure condition: We also conduct some ablations (Section 5.2) where we initialize from Wan2.1-I2V-5B-480P to see the effect of model size (5B vs..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture), p. 6 (3.1. Model Architecture); the primary result is directionally consistent at p. 15 (Figure/Table caption), p. 16 (Figure/Table caption), p. 3 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Second, more, surprisingly mechanism이 Figure 2: Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that ... 대비 Table 2: Cross-Embodiment Transfer Results. Average task progress on unseen tasks (± standard error). Both transfer settings improve ...을 개선하고, While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
