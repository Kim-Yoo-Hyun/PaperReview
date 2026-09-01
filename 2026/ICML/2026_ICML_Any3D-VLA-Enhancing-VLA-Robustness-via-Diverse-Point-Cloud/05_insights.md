# Insights — Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=zyMvoKYWMZ; PDF retrieval source: https://openreview.net/pdf/01fd7931fc7be08bf369b6a34264822e6d1de9b9.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA.
- **p. 2 / 1. Introduction - extractive body cue:** We propose ANY3D-VLA, a plug-in pipeline for existing VLA backbones (Figure 1).
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** The VLM comprises a trainable large language model InternLM2 1.8B (Cai et al., 2024), a visual observation module (§5.2), and a trainable projector that maps ...
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** We use a conditional flow-matching action expert (Lipman et al., 2023) to generate fine-grained end-effector actions.
- **p. 5 / 5.3. Training Strategy - extractive body cue:** The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data.
- **p. 5 / 5.3. Training Strategy - extractive body cue:** We do not incorporate any explicit reconstruction losses for depth or point clouds, aiming to demonstrate that the performance gains stem primarily from superior spatial ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (5.1. Overall Architecture), p. 4 (5.1. Overall Architecture), p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** (2) To address the scaling bottlenecks of 3D VLA training and the cross-environment domain gap, we introduce a hybrid point-cloud training strategy and construct a ...
- **p. 2 / 1. Introduction - extractive body cue:** However, 3D VLAs still face bottlenecks in scalable training and real deployment: (1) compared to the massive amount of 2D image data, 3D data is ...
- **p. 1 / 1. Introduction - extractive body cue:** Vision-Language-Action (VLA) models, trained on massive collections of action trajectories paired with language instructions, hold great promise for achieving general-purpose embodied intelligence (Kim et al., ...
- **p. 8 / 7. Limitations and Future Work - extractive body cue:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single ...
- **p. 7 / 6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD - extractive body cue:** We also conduct a qualitative analysis to highlight the robustness of our method compared to baselines and to discuss shared limitations (Appendix J).
- **p. 8 / 7. Limitations and Future Work - extractive body cue:** Future work could extend to additional robot platforms and environments, and evaluate more complex, long-horizon tasks.
- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** Expert trajectories are produced by generating candidate grasp poses with BoDex (Chen et al., 2025b), performing oneshot collision-avoidance trajectory planning with CuRobo (Sundaralingam et al., ...
- **Boundary to test:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited set of ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | In particular, the overall average success rate for (Setting 2, DA3) reaches 62.5%, representing a 29.2% improvement over the strongest baseline SpatialVLA, which achieves 33.3%. | p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 8 (6.5. LIBERO and CALVIN Benchmarks) |
| Failure/limitation | Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited set of ... | p. 8 (7. Limitations and Future Work), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data.를 Vision-Language-Action (VLA) models, trained on massive collections of action trajectories paired with language instructions, hold great promise for achieving general-purpose embodied intelligence (Kim et al., 2025b; Deng et al., 2025; ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited set of ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, 3D Vision`.
- **Reading predecessor in the generated track queue:** Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited set of ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This dataset includes 15 object categories that appeared in the pre-training data, while the layouts and backgrounds are randomly generated and unseen during pre-training, resulting in 95 distinct scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: ANY3DVLA outperforms the baselines on both tasks..
4. Report the body metric and its denominator/aggregation: We evaluate the models in simulation, training until the success rate converges, and then select the best-performing checkpoint for real-world testing..
5. Re-run the body-reported ablation/failure condition: Ablation study on the effect of 2D-3D fusion..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (5.1. Overall Architecture), p. 4 (5.1. Overall Architecture), p. 5 (5.3. Training Strategy); the primary result is directionally consistent at p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 8 (6.5. LIBERO and CALVIN Benchmarks), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 ANY3DVLA outperforms the baselines on both tasks. 대비 We evaluate the models in simulation, training until the success rate converges, and then select the best-performing checkpoint ...을 개선하고, Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
