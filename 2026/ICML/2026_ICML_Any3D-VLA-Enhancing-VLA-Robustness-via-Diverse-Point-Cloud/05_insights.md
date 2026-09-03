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

- **Paper-specific interface:** The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data. (p. 5, 5.3. Training Strategy).
- **Paper-specific mechanism:** The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA. (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 RGBD image-plane 56.8 76.8 87.4 Point ... (p. 4, 3. Dataset and Benchmark); the relevant task/metric cue is Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 RGBD image-plane 56.8 76.8 87.4 Point ... (p. 4, 3. Dataset and Benchmark). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited ... (p. 8, 7. Limitations and Future Work).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, 3D Vision`.
- **Reading predecessor in the generated track queue:** Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited set of ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data. (p. 5, 5.3. Training Strategy); preserve the objective/update rule: The full form of the loss function is provided in Appendix F.1. (p. 5, 5.3. Training Strategy).
2. Use the paper-reported task/data/environment cue: To validate the effectiveness of pre-training in simulation, we constructed an RGBD evaluation dataset as a benchmark using the same procedure. (p. 3, 3. Dataset and Benchmark).
3. Compare against the reported or matched baseline: ANY3DVLA outperforms the baselines on both tasks. (p. 7, 6.1.3. REAL-WORLD POST-TRAINING).
4. Report the body metric with its denominator and aggregation: Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 RGBD image-plane 56.8 76.8 87.4 Point ... (p. 4, 3. Dataset and Benchmark).
5. Re-run the reported ablation or stress/failure condition: Ablation study on the effect of 2D-3D fusion. (p. 8, 6.4. Ablation Study); if none is reported, design one around: Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited ... (p. 8, 7. Limitations and Future Work).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 2 (1. Introduction), match the reported outcome at p. 4 (3. Dataset and Benchmark), p. 8 (6.5. LIBERO and CALVIN Benchmarks), p. 6 (6.1.1. REAL-WORLD SETUP), and measure the boundary at p. 8 (7. Limitations and Future Work), p. 9 (7. Limitations and Future Work).

## Falsifiable research question

Under the paper's stated interface (The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data.), does the paper-specific mechanism (The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA.) retain the reported evaluation outcome (Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 ...) when tested against the paper's strongest explicit boundary (Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA. (p. 2, 1. Introduction).
- **Paper-supported outcome:** Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 RGBD image-plane 56.8 76.8 87.4 Point ... (p. 4, 3. Dataset and Benchmark).
- **Strongest explicit boundary:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited ... (p. 8, 7. Limitations and Future Work).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
