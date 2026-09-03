# Insights — LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lwOoBzJykL; PDF retrieval source: https://arxiv.org/pdf/2601.05248.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose LaST0, a unified VLA model that enables efficient reason-before-act behavior through a Latent SpatioTemporal CoT, performing ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose LaST0, a dual-system VLA model that enables efficient reason-before-act behavior through a Latent Spatio-Temporal Chain-of-Thought (CoT).
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Specifically, this control vector consists of 3-DoF for relative positional offsets ([∆x, ∆y, ∆z] ∈R3), 3-DoF for rotation (represented as Euler angles [roll, pitch, yaw] ...
- **p. 3 / 3.2. LaST0 Architecture - extractive body cue:** In our framework, these encoded features fimg serve a dual purpose: the current frame acts as real-time contextual input to the MoT experts, while future ...
- **p. 4 / 3.2. LaST0 Architecture - extractive body cue:** Framework. a) We propose LaST0, a unified VLA model with a dual-system architecture.
- **p. 4 / 3.2. LaST0 Architecture - extractive body cue:** LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception Latent LaST CoT ...
- **p. 4 / 3.2. LaST0 Architecture - extractive body cue:** The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated latent representations. b) ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminaries), p. 3 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** 1, unlike prior explicit CoT-based VLA methods, LaST0 performs reasoning in a compact latent space, enabling the capture of fine-grained physical and robotic dynamics that ...
- **p. 2 / 1. Introduction - extractive body cue:** Despite their demonstrated benefits, explicit CoT VLA methods remain constrained by two fundamental challenges in robotics manipulation.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** We formulate the robot manipulation task as a probabilistic sequence decision-making problem (Kim et al., 2024).
- **p. 3 / 3.1. Preliminaries - extractive body cue:** At each timestep t, the policy receives a natural language instruction lt and visual observations It ∈RH×W ×3 that capture the current environment.
- **p. 9 / 4.3. Real-World Experiment - extractive body cue:** We show more comprehensive visualizations in Appendix G and supplementary video, and failure cases in Appendix H.
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 11. Visualization of failure cases on different robot platforms, the task progresses from left to right, and red box highlights the failure positions. H. ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 12. Visualization of complete task execution processes by real-world tasks (from left to right). 3) The failure in the third case in the dexterous ...
- **Boundary to test:** We show more comprehensive visualizations in Appendix G and supplementary video, and failure cases in Appendix H.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are summarized as follows: • We propose LaST0, a unified VLA model that enables efficient reason-before-act behavior through a Latent SpatioTemporal CoT, performing reasoning in a compact latent space to ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | As shown in Table 3, LaST0 achieves the best overall performance on realworld manipulation tasks, with a mean success rate of 72% (±3) on Franka platform (not including the long-horizon task), substantially ... | p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz) |
| Failure/limitation | We show more comprehensive visualizations in Appendix G and supplementary video, and failure cases in Appendix H. | p. 9 (4.3. Real-World Experiment), p. 21 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated latent representations. b) We design a spatio-temporal latent space, wher ...를 LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception Latent LaST CoT t𝒕"𝑯 "Scoop the egg out of the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We show more comprehensive visualizations in Appendix G and supplementary video, and failure cases in Appendix H.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are summarized as follows: • We propose LaST0, a unified VLA model that enables efficient reason-before-act behavior through a Latent SpatioTemporal CoT, performing reasoning in a compact latent space to ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We show more comprehensive visualizations in Appendix G and supplementary video, and failure cases in Appendix H.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For the LIBERO (Liu et al., 2024) benchmark, our evaluation leverages its four specialized dataset suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long..
3. Compare against the body-reported baseline or a matched simpler baseline: In this suite, LaST0 achieves a 95.6% success rate, outperforming strong baselines such as OpenVLA-OFT (94.5%) and π0.5 (92.4%)..
4. Report the body metric and its denominator/aggregation: Beyond the overall average, LaST0 attains the highest success rate on 7 out of 10 tasks, indicating consistent performance gains across diverse manipulation skills..
5. Re-run the body-reported ablation/failure condition: Table 10. Ablation on Latent Modalities. The effect of removing individual modalities on the action inter-class distance. Latent Modality Configuration Action Inter-class Distance w/o 2D (3D + State only) 1.22 w/o 3D ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought); the primary result is directionally consistent at p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz), p. 7 (15.4 Hz); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 In this suite, LaST0 achieves a 95.6% success rate, outperforming strong baselines such as OpenVLA-OFT (94.5%) ... 대비 Beyond the overall average, LaST0 attains the highest success rate on 7 out of 10 tasks, indicating consistent ...을 개선하고, We show more comprehensive visualizations in Appendix G and supplementary video, and failure cases in Appendix ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
