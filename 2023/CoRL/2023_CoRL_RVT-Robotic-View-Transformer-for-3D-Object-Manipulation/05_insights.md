# Insights — RVT: Robotic View Transformer for 3D Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14896; PDF retrieval source: https://arxiv.org/pdf/2306.14896. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose RVT (Robotic View Transformer) that significantly outperforms the SOTA voxel-based method both in terms of success rate and training time, ...
- **p. 3 / 3 Method - extractive body cue:** The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state ...
- **p. 1 / 1 Introduction - extractive body cue:** This hinders fast development and prototyping.
- **p. 5 / 3 Method - extractive body cue:** The training time and inference speed of PerAct and RVT are measured on the same GPU model. we use global features (G).
- **p. 4 / 3 Method - extractive body cue:** The model outputs an 8-dimensional action, including the 6-DoF target end effector pose (3-DoF for translation and 3-DoF for rotation), 1-DoF gripper state (open or ...
- **p. 4 / 3 Method - extractive body cue:** Our proposed method (RVT) is a transformer model [27] that processes images re-rendered around the robot workspace, produces an output for each view, and then ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Method), p. 1 (1 Introduction), p. 5 (3 Method), p. 4 (3 Method)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** C2FARM [5] represents the scene with multi-resolution voxels and achieves strong performance on difficult RLBench tasks.
- **p. 2 / 1 Introduction - extractive body cue:** Hence, a key question is - can we build a manipulation network that not only performs well but also inherits the scalability of view-based methods?
- **p. 2 / 1 Introduction - extractive body cue:** Another key innovation is that, unlike prior view-based methods, we decouple the camera images from the images fed to the transformer, by re-rendering the images ...
- **p. 8 / 4 Experiments - extractive body cue:** 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation.
- **p. 8 / 4 Experiments - extractive body cue:** Although we found RVT to achieve state-of-the-art results, we identify some limitations that present exciting directions for future research.
- **p. 15 / 6 Appendix - extractive body cue:** 6.2 RVT Overview Insert peg in the blue spoke Virtual Image 1 Virtual Image 2 Virtual Image 5 Patchify Projection Attention X 4 Attention X ...
- **p. 6 / 4 Experiments - extractive body cue:** Hence, the reported performance does not reflect a single multi-task model.
- **Boundary to test:** 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate various design choices for the multi-view transformer ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks. | p. 6 (4 Experiments), p. 8 (4 Experiments) |
| Failure/limitation | 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation. | p. 8 (4 Experiments), p. 8 (4 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Our proposed method (RVT) is a transformer model [27] that processes images re-rendered around the robot workspace, produces an output for each view, and then back-projects into 3D to predict ... (p. 4, 3 Method).
- **Paper-specific mechanism:** To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate various design choices for the ... (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Table 2: Left: Ablations on RLBench. A larger res., adding view correspondence, adding depth channel, separating initial attention layers, orthographic projection, using rotation aug., and re- rendered views around cube ... (p. 7, Figure/Table caption); the relevant task/metric cue is Our model overall achieves an 82.5% success rate on non-marker tasks. (p. 8, 4 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation. (p. 8, 4 Experiments).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Robotics-enabling 3D perception`; tags: `Robotics, 3D manipulation, Transformer`.
- **Reading predecessor in the generated track queue:** ConceptFusion: Open-set Multimodal 3D Mapping (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DUSt3R: Geometric 3D Vision Made Easy (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Our proposed method (RVT) is a transformer model [27] that processes images re-rendered around the robot workspace, produces an output for each view, and then back-projects into 3D to predict ... (p. 4, 3 Method); preserve the objective/update rule: We train RVT using a mixture of losses. (p. 5, 3 Method).
2. Use the paper-reported task/data/environment cue: A Franka Panda robot with a parallel gripper is controlled to complete the tasks. (p. 5, 4 Experiments).
3. Compare against the reported or matched baseline: Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks. (p. 6, 4 Experiments).
4. Report the body metric with its denominator and aggregation: Our model overall achieves an 82.5% success rate on non-marker tasks. (p. 8, 4 Experiments).
5. Re-run the reported ablation or stress/failure condition: We compare with two variants with CNN and ViT vision encoders respectively. (p. 5, 4 Experiments); if none is reported, design one around: 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation. (p. 8, 4 Experiments).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 7 (Figure/Table caption), p. 6 (4 Experiments), p. 6 (4 Experiments), and measure the boundary at p. 8 (4 Experiments), p. 8 (4 Experiments).

## Falsifiable research question

Under the paper's stated interface (Our proposed method (RVT) is a transformer model [27] that processes images re-rendered around the robot workspace, produces an output for each ...), does the paper-specific mechanism (To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; ...) retain the reported evaluation outcome (Our model overall achieves an 82.5% success rate on non-marker tasks.) when tested against the paper's strongest explicit boundary (5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Our model overall achieves an 82.5% success rate on non-marker tasks.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate various design choices for the ... (p. 2, 1 Introduction).
- **Paper-supported outcome:** Table 2: Left: Ablations on RLBench. A larger res., adding view correspondence, adding depth channel, separating initial attention layers, orthographic projection, using rotation aug., and re- rendered views around cube ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation. (p. 8, 4 Experiments).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
