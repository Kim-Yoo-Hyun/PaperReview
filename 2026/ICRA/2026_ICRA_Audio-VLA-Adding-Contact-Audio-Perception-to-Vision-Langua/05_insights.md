# Insights — Audio-VLA: Adding Contact Audio Perception to Vision-Language-Action Model for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2511.09958v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / III. METHOD - extractive body cue:** 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this paper, we propose Audio-VLA, a multimodal manipulation policy that combines acoustic and visual perception.
- **p. 3 / III. METHOD - extractive body cue:** It consists of two powerful vision transformers, DINOv2 [23] and SigLIP [24], pre-trained on Internet-scale image data to capture rich visual features and comprehensive spatial ...
- **p. 3 / III. METHOD - extractive body cue:** The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a unified representation space, a 7B-parameter ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Large-scale vision-language pretraining [4] enables VLA models to achieve generalizable manipulation capabilities across diverse scenarios.
- **p. 2 / III. METHOD - extractive body cue:** This section first details the Audio-VLA architecture, then presents our training objective and audio-enhanced simulation environments for LIBERO [8] and RLBench [9].
- **p. 4 / III. METHOD - extractive body cue:** This enables Faud to capture high-frequency acoustic features and temporal dynamics of contact events, providing physical interaction information unavailable through visual perception alone.
- **Contribution anchor:** p. 2 (III. METHOD), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Despite these promising capabilities, integrating acoustic information into existing VLA frameworks presents technical challenges, such as extracting contact event information from high-frequency contact audio, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, current VLA methods exhibit a fundamental limitation as they rely exclusively on visual perception [6]- [10].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Prior works [15], [16], [19] have attempted to use tactile signals to compensate for VLA's limited perception of dynamic information such as contact events and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furthermore, recognizing the limitations of existing evaluation metrics that focus primarily on final task outcomes, the Task Completion Rate (TCR) evaluation metric is proposed to ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable information particularly when visual perception fails to ...
- **p. 7 / V. CONCLUSION - extractive body cue:** This paper presents Audio-VLA, a multimodal manipulation policy that integrates acoustic perception into VLA models to overcome vision-only limitations.
- **p. 7 / V. CONCLUSION - extractive body cue:** Experimental results demonstrate that Audio-VLA achieves superior performance in both simulation environments and real-world tasks, proving the contribution of contact audio perception in overcoming visual ...
- **Boundary to test:** Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable information particularly when visual perception fails to capture con ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi | p. 2 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Reported outcome | I, AudioVLA achieves 97.6% average success rate on LIBERO and 55.1% on RLBench, outperforming all comparative methods. | p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Failure/limitation | Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable information particularly when visual perception fails to capture con ... | p. 6 (IV. EXPERIMENT), p. 7 (V. CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Furthermore, recognizing the limitations of existing evaluation metrics that focus primarily on final task outcomes, the Task Completion Rate (TCR) evaluation metric is proposed to quantify dynamic process perceptual feedback capabiliti ...를 Subsequently, we extract the action hidden states Hact from Hdec, where each vector h(m) ∈Rdllm for m = 1, . . . , K · D encodes contextual information from all input ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable information particularly when visual perception fails to capture con ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable information particularly when visual perception fails to capture con ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The performance gap reveals that in tasks requiring precise force control and continuous state monitoring, visual modality nearly loses its ability to perceive contact states under domain shift, whereas contact audio provide ....
3. Compare against the body-reported baseline or a matched simpler baseline: The inferior performance of the vision-only configuration compared to the full configuration demonstrates that audio provides critical information for TABLE IV: Ablation study results on Real-world Configuration EAWS S5GO Success rate T ....
4. Report the body metric and its denominator/aggregation: AudioVLA preserves 30% and 20% success rates on EAWM and S5GO respectively, whereas vision-only methods approach near-zero performance..
5. Re-run the body-reported ablation/failure condition: Additionally, we conduct ablation studies in both simulation and real-world settings to investigate the effectiveness of incorporating contact audio signals into VLA. a) Simulation Experiments Results: Simulation experiments are conduct ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD); the primary result is directionally consistent at p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Audio-VLA, consists, four mechanism이 The inferior performance of the vision-only configuration compared to the full configuration demonstrates that audio provides ... 대비 AudioVLA preserves 30% and 20% success rates on EAWM and S5GO respectively, whereas vision-only methods approach near-zero performance.을 개선하고, Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
