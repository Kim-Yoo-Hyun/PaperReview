# Insights — HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling strategy ...
- **p. 2 / 1. Introduction - extractive body cue:** We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination ...
- **p. 5 / 4.2.3. Multi-Sampling Strategy - extractive body cue:** To further enhance HAD, we propose a multi-sampling strategy that creates multiple versions of augmented views and fuses them to produce higher-quality novel views for ...
- **p. 5 / 4.2. Hallucination-Aware Diffusion Prior - extractive body cue:** To enhance novel view synthesis quality, we propose the hallucination-aware diffusion prior (HAD) to augment images rendered at novel views and optimize the 3DGS model ...
- **p. 1 / 1. Introduction - extractive body cue:** One approach to address data sparsity is to leverage generative diffusion priors to augment novel-view data by removing artifacts from rendered images through denoising conditioned ...
- **p. 5 / 4.2.2. Hallucination Score Estimation - extractive body cue:** Specifically, the hallucination score network consists of two components: a multi-view feature encoder V that processes multiple input views, and a score estimation branch S ...
- **p. 5 / 4.1. 3DGS training - extractive body cue:** Specifically, unlike Difix3D [41], which employs a two-phase training strategy that first fully trains a 3DGS model and then progressively updates it with diffusion priors ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2.3. Multi-Sampling Strategy), p. 5 (4.2. Hallucination-Aware Diffusion Prior), p. 1 (1. Introduction), p. 5 (4.2.2. Hallucination Score Estimation)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose incorporating hallucination awareness into the augmented views.
- **p. 1 / 1. Introduction - extractive body cue:** One approach to address data sparsity is to leverage generative diffusion priors to augment novel-view data by removing artifacts from rendered images through denoising conditioned ...
- **p. 3 / 3. Preliminary - extractive body cue:** Recent advances have demonstrated that diffusion-based priors are highly effective for improving 3D reconstruction and scene enhancement [8, 11, 26, 28, 41].
- **p. 3 / 3. Preliminary - extractive body cue:** We briefly describe the preliminaries for 3D Gaussian Splatting (3DGS) - the 3D pipeline that we use to validate our HAD, feedforward novel view synthesis ...
- **p. 8 / 6. Conclusion and Future Work - extractive body cue:** In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion priors effectively alleviate data sparsity, they introduce hallucinated content ...
- **p. 8 / 6. Conclusion and Future Work - extractive body cue:** An interesting direction for future work is to scale up the training of our model by removing the need for complex data requirementsfor instance, using ...
- **Boundary to test:** In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion priors effectively alleviate data sparsity, they introduce hallucinated content that compromises fidelity to input view ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling strategy into HAD that generates and fuses multiple ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | We select 3 views to achieve a trade-off between marginal improvement and computational overhead. | p. 8 (5.4. Ablation studies), p. 8 (5.4. Ablation studies) |
| Failure/limitation | In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion priors effectively alleviate data sparsity, they introduce hallucinated content that compromises fidelity to input view ... | p. 8 (6. Conclusion and Future Work), p. 8 (6. Conclusion and Future Work) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `conditioning observation와 noisy/intermediate sample → latent/noise variable와 conditional distribution → generated sample, action chunk 또는 trajectory`.
- 이 논문의 재사용 가능한 지점은 A feedforward NVS network is a generalizable network that takes multiple views as input and outputs a 3D feature, enabling the rendering of images from novel viewpoints.를 Thus, the multi-view encoder V outputs features aggregated at the novel view pose ˜c from the input views.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 latent/noise variable와 conditional distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion priors effectively alleviate data sparsity, they introduce hallucinated content that compromises fidelity to input view ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling strategy into HAD that generates and fuses multiple ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D reconstruction, Diffusion, Generation, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion priors effectively alleviate data sparsity, they introduce hallucinated content that compromises fidelity to input view ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We first curate training dataset of randomly selected 116 scenes from benchmark dataset for hallucination score network training..
3. Compare against the body-reported baseline or a matched simpler baseline: Our method outperforms the baselines by a large margin across all metrics..
4. Report the body metric and its denominator/aggregation: Table 6. Different hallucination score estimators. We use Mean Absolute Error (MAE) of the predicted hallucination score maps as our evaluation metric. We demonstrate that our hallucination score network, with the pretrained ....
5. Re-run the body-reported ablation/failure condition: Note that ours* denotes a variant following the twophase 3DGS optimization strategy of Difix3D, enabling a fair comparison between diffusion priors with and without hallucination awareness..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.1. 3DGS training), p. 4 (4. Methodology); the primary result is directionally consistent at p. 8 (5.4. Ablation studies), p. 8 (5.4. Ablation studies), p. 7 (5.3. Cross-domain evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 best, knowledge, first mechanism이 Our method outperforms the baselines by a large margin across all metrics. 대비 Table 6. Different hallucination score estimators. We use Mean Absolute Error (MAE) of the predicted hallucination score maps ...을 개선하고, In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
