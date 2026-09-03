# Insights — GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 3 Method - extractive body cue:** In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose GS-LRM, a novel transformer-based large reconstruction model that predicts 3D Gaussian primitives [30] from sparse input images, enabling fast and ...
- **p. 5 / 3 Method - extractive body cue:** 2) and consists of Pre-LayerNorm [3], multi-head Self-Attention [60] and MLP.
- **p. 2 / 1 Introduction - extractive body cue:** The core of our approach is a simple and scalable transformer-based network architecture that predicts per-pixel Gaussians.
- **p. 6 / 3 Method - extractive body cue:** This property allows us to better handle high-frequency details in the inputs and large-scale scene captures.
- **p. 6 / 3 Method - extractive body cue:** We empirically find that the perceptual loss in [14] based on VGG-19 network [53] provides a more stable training than LPIPS [73] used in [27,32,61,66], ...
- **p. 4 / 3 Method - extractive body cue:** Multi-view image tokens are then concatenated and passed through a sequence of transformer blocks consisting of self-attention and MLP layers.
- **Contribution anchor:** p. 4 (3 Method), p. 2 (1 Introduction), p. 5 (3 Method), p. 2 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.
- **p. 1 / 1 Introduction - extractive body cue:** This leads to challenges in training and rendering speeds, preserving fine details, and scaling to large scenes beyond object-centric inputs. *
- **p. 13 / 4 Experiments - extractive body cue:** 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future work.
- **p. 14 / 5 Conclusion - extractive body cue:** We hope that our work can inspire more future work in the space of data-driven feed-forward 3D reconstruction.
- **p. 8 / 4 Experiments - extractive body cue:** The Triplane-LRM cannot reconstruct high-frequency details (top left and top right) and thin structures (bottom left) well.
- **p. 14 / 4 Experiments - extractive body cue:** Please refer to our project page for the video and interactive rendering results. the view frustum, which means that unseen regions cannot be reconstructed.
- **p. 9 / 4 Experiments - extractive body cue:** We also tried to compare against another baseline SparseNeuS [36]; however, we found that it failed to produce plausible reconstructions given 4 highly sparse inputs; ...
- **Boundary to test:** 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future work.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec. | p. 4 (3 Method), p. 2 (1 Introduction) |
| Reported outcome | Fig. 5: We compare scene-level GS-LRM with the best-performing baseline pixel- Splat [8]. We can observe that our model is better in sharpness (leftmost column), has fewer floaters (mid-right and rightmost), and ... | p. 10 (Figure/Table caption), p. 10 (4 Experiments) |
| Failure/limitation | 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future work. | p. 13 (4 Experiments), p. 14 (5 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Unlike previous LRMs that require careful designs of additional (triplane) NeRF tokens for reconstruction, we align input (2D images) and output (3D Gaussians) in the same pixel space, predicting one Gaussian per ...를 The final output of our model is simply the merge of 3D Gaussians from all N input views.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future work.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future work.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We follow the standard training/testing split for the dataset, which is also used in pixelSplat [8]..
3. Compare against the body-reported baseline or a matched simpler baseline: We outperform relevant baselines by a large margin in both scenarios..
4. Report the body metric and its denominator/aggregation: The dataset contains 80K video clips curated from 10K YouTube videos..
5. Re-run the body-reported ablation/failure condition: We only leverage the multi-view renderings of the objects without accessing explicit 3D information (such as depths)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (3 Method), p. 4 (3 Method), p. 5 (3 Method); the primary result is directionally consistent at p. 10 (Figure/Table caption), p. 10 (4 Experiments), p. 7 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 section, present, technical mechanism이 We outperform relevant baselines by a large margin in both scenarios. 대비 The dataset contains 80K video clips curated from 10K YouTube videos.을 개선하고, 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
