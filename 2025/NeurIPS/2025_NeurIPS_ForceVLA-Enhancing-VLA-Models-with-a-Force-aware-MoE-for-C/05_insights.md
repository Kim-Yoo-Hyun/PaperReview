# Insights — ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=2845H8Ua5D; PDF retrieval source: https://arxiv.org/pdf/2505.22159. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions are: • We present a novel framework that integrates force, vision, language, and action for improved precision and stability on contact-rich manipulation ...
- **p. 2 / 1 Introduction - extractive body cue:** Key to our approach is a force-aware Mixture-of-Experts-based fusion module, which enables dynamic processing and deep integration of force, visual, and language features during action ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems.
- **p. 3 / 1 Introduction - extractive body cue:** The robot's observation at timestep t consists of base and hand visual inputs V b t and V h t , the proprioceptive state st ...
- **p. 3 / 1 Introduction - extractive body cue:** TCP position is represented by Cartesian coordinates (x, y, z) and orientation is represented by Euler angles (α, β, γ). ft is the estimated external ...
- **p. 2 / 1 Introduction - extractive body cue:** To address these limitations, we introduce ForceVLA, a novel framework that augments VLA models with a force-aware Mixture-of-Experts (MoE) module, enabling effective reasoning and context-sensitive, ...
- **p. 3 / 1 Introduction - extractive body cue:** Flow-based architectures such as π0 [10, 21] integrate pretrained vision-language encoders with fast action decoders to achieve high-frequency outputs.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** However, these methods largely omit explicit modeling of the force/tactile modalities, and lack mechanisms for dynamically routing across multimodal signals in contact-intensive tasks.
- **p. 2 / 1 Introduction - extractive body cue:** Current methods lack mechanisms to perceive and adapt to these dynamic variations, limiting their ability to reason over time about physical interactions.
- **p. 3 / 1 Introduction - extractive body cue:** Multimodal fusion methods [38, 39] show promise in complex environments, though current approaches are often limited to static modality fusion and lack dynamic routing or ...
- **p. 5 / 1 Introduction - extractive body cue:** Existing datasets often lack the comprehensive force interactions or the diversity of contact-driven scenarios necessary to develop robust force-aware policies.
- **p. 2 / 1 Introduction - extractive body cue:** Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Trajectory visualizations across tasks and conditions. (a) USB insertion, (b) bottle pumping, and (c) plug insertion under stable and unstable socket conditions. Each ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; (e) ...
- **Boundary to test:** Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. In contrast, ForceVLA leverages external force signals to ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions are: • We present a novel framework that integrates force, vision, language, and action for improved precision and stability on contact-rich manipulation tasks. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback improves performance for π0-base model, while our method achi ... | p. 7 (Figure/Table caption), p. 6 (5 Experiments) |
| Failure/limitation | Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. In contrast, ForceVLA leverages external force signals to ... | p. 2 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 Given a language instruction L, the objective is to learn an end-to-end policy π(At/Ot, L) that outputs low-level, executable action chunk At = {at, at+1, ..., at+H-1}[10] maximizing the likelihood of completing ...를 The robot's observation at timestep t consists of base and hand visual inputs V b t and V h t , the proprioceptive state st ∈R7, and external forcetorque readings ft ∈ ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. In contrast, ForceVLA leverages external force signals to ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions are: • We present a novel framework that integrates force, vision, language, and action for improved precision and stability on contact-rich manipulation tasks.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. In contrast, ForceVLA leverages external force signals to ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized fusion mechanism; (2) the model's ability to generalize ....
3. Compare against the body-reported baseline or a matched simpler baseline: The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized fusion mechanism; (2) the model's ability to generalize ....
4. Report the body metric and its denominator/aggregation: Model performance is primarily evaluated using the task success rate across all five challenging contact-rich manipulation tasks..
5. Re-run the body-reported ablation/failure condition: The specific variants include π0-base[10] w/o F (standard π0 without force input), π0-base[10] w/ F (π0 with force signals directly concatenated to state inputs), and corresponding π0-fast[25] configurations ( w/o F and ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 6 (5 Experiments), p. 8 (5 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, present mechanism이 The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared ... 대비 Model performance is primarily evaluated using the task success rate across all five challenging contact-rich manipulation tasks.을 개선하고, Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
