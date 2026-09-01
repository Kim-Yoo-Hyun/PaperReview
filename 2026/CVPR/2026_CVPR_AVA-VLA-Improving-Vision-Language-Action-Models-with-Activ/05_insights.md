# Insights — AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.
- **p. 2 / 1. Introduction - extractive body cue:** To our knowledge, it is the first VLA framework to explicitly address this limitation via a POMDP-inspired approach. • We introduce an Active Visual Attention ...
- **p. 3 / 3. Methods - extractive body cue:** In this section, we present our proposed VLA method.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** A typical VLA model Pθ, parameterized by θ, consists of four main components: a Large-Language-Model (LLM) backbone M, a vision encoder E, a language tokenizer ...
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** For simplicity, our framework is built upon the OpenVLA-OFT foundation model.
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** Then the AVA module combines this recurrent state with textconditioned visual features from the current observation to generate soft importance scores, which modulate the visual ...
- **p. 3 / 3.2. AVA-VLA Framework - extractive body cue:** To utilize the recurrent state, we introduce the active visual attention module by quantifying the importance of visual tokens and dynamically modulating the processing of ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methods), p. 3 (3.1. Preliminaries), p. 4 (3.2. AVA-VLA Framework), p. 4 (3.2. AVA-VLA Framework)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.
- **p. 1 / 1. Introduction - extractive body cue:** (b) Qualitative comparison of visual focus from two viewpoints while executing the task "turn on the stove and put the moka pot on it." The ...
- **p. 2 / 1. Introduction - extractive body cue:** In fact, the inability to anticipate perceptual intent a priori makes active visual modules difficult to realize in computer vision.
- **p. 1 / 1. Introduction - extractive body cue:** This implicitly formulates robot manipulation as a Markov Decision Process (MDP) [16, 31], where actions are generated from the current visual observation, assumed to represent ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** (2) Regardless of whether AR or parallel decoding is used, these VLA models learn to predict the action ¯ At only from the current observation ...
- **p. 8 / 4.4. Analysis - extractive body cue:** Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains a ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Due to space limitations, implementation details are provided in Appendix A.
- **Boundary to test:** Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains a robust and spatially consistent focus by effectively ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Each component alone improves over OpenVLA-OFT, and their combination achieves the best overall performance. | p. 7 (4.3. Ablation Studies), p. 7 (4.2. Evaluation Results) |
| Failure/limitation | Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains a robust and spatially consistent focus by effectively ... | p. 8 (4.4. Analysis), p. 1 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 In a POMDP framework, the optimal policy at timestep t should be conditioned not only on the current observation xt but also on a belief state bt-1, which captures all relevant historical ...를 (1) Recent representative VLA models, such as OpenVLAOFT [20] and its variant [23], map the output hidden states into an executable action chunk At = [at 0, at 1, ..., at Lc-1] ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains a robust and spatially consistent focus by effectively ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, active perception, visual attention, POMDP, recurrent state, long horizon`.
- **Reading predecessor in the generated track queue:** MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains a robust and spatially consistent focus by effectively ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We conduct experiments on three challenging settings: the LIBERO [28] and CALVIN [31] benchmarks for evaluation in simulation environments, and a real-world tablemounted Mobile ALOHA robot with four test tasks, to validate ....
3. Compare against the body-reported baseline or a matched simpler baseline: The results show that the proposed AVA-VLA framework comprehensively outperforms baseline methods across all tasks..
4. Report the body metric and its denominator/aggregation: We use widely adopted performance evaluation metrics "Success Rate (SR)" (the same 13458.
5. Re-run the body-reported ablation/failure condition: Additionally, we conduct a comprehensive ablation study and analysis to validate the effectiveness of our approach..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries), p. 3 (3.2. AVA-VLA Framework); the primary result is directionally consistent at p. 7 (4.3. Ablation Studies), p. 7 (4.2. Evaluation Results), p. 6 (4.1. Experimental Setup); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, threefold, novel mechanism이 The results show that the proposed AVA-VLA framework comprehensively outperforms baseline methods across all tasks. 대비 We use widely adopted performance evaluation metrics "Success Rate (SR)" (the same 13458을 개선하고, Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
