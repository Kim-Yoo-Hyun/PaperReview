# Insights — EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 FPS ...
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** To this end, we propose EmbodiedSplat, a novel online framework to endow pretrained feed-forward 3DGS [44] with open-vocabulary capability.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, our objective is to develop an embodied perception model that meets the above five conditions by leveraging 3D Gaussian Splatting (3DGS) [20].
- **p. 1 / 1. Introduction - extractive body cue:** 3DGS is the recent 3D representation that supports real-time novel view synthesis with explicit structure which existing repreThis CVPR paper is the Open Access version, ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since FreeSplat++ is designed for offline use, we modify its inference pipeline to enable online perception from streaming images: 1) Input selection.
- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** Prior works compress CLIP with encoder-decoder networks [19, 35, 56] or Product Quantization (PQ) [18].
- **p. 4 / 4.1. EmbodiedSplat - extractive body cue:** Local st l(i) is then fused with paired global CLIP feature st-1 g (mi) by following the confidenceweighted average from Eq.
- **Contribution anchor:** p. 2 (1) They require per-scene optimization that cannot be gen), p. 2 (1) They require per-scene optimization that cannot be gen), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Preliminaries), p. 4 (4.1. EmbodiedSplat)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Nevertheless, all of them share two limitations in embodied scenarios:
- **p. 1 / 1. Introduction - extractive body cue:** 3DGS is the recent 3D representation that supports real-time novel view synthesis with explicit structure which existing repreThis CVPR paper is the Open Access version, ...
- **p. 2 / 1. Introduction - extractive body cue:** Its distinct competency motivates the current research to explore the open-vocabulary scene understanding with 3DGS.
- **p. 3 / 3. Preliminaries - extractive body cue:** Given the current frame It ∈RH×W ×3, we select N past frames from time steps t-N to t-1 to reflect the online setting.
- **p. 7 / 5.1. Experimental Results - extractive body cue:** Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** Splat [18] shares the same limitations.
- **p. 7 / 5.1. Experimental Results - extractive body cue:** Our model shows strong semantics generalizability in ScanNet++ →ScanNet transfer with performance degradation remaining below 1 mIoU compared to ScanNet →ScanNet setting in Tab.
- **Boundary to test:** Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization methods.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 FPS inference speed. • Combination of 2D CLIP ... | p. 2 (1) They require per-scene optimization that cannot be gen), p. 2 (1) They require per-scene optimization that cannot be gen) |
| Reported outcome | Table 1. Quantitative comparisons on 3D Semantic Segmentation across ScanNet [6], ScanNet200 [38] and ScanNet++ [53]. We compare the performance of our EmbodiedSplat with existing semantic 3DGS methods on 3D semantic segmentation. ... | p. 6 (Figure/Table caption), p. 8 (5.2. Ablation Studies) |
| Failure/limitation | Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization methods. | p. 7 (5.1. Experimental Results), p. 8 (5.2. Ablation Studies) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Specifically, the embodied agent equipped with a precise SLAM system collects posed RGB or RGB-D images to understand the 3D scene, follow human instructions, and make autonomous decisions based on its own ...를 With It and the N reference views as input, the CNN encoder E predicts pixelwise local Gaussian triplets Θt l = {µt l, ωt l, f t l } and a depth ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization methods.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 FPS inference speed. • Combination of 2D CLIP ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, open-vocabulary, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization methods.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization methods..
3. Compare against the body-reported baseline or a matched simpler baseline: Our EmbodiedSplat demonstrates better segmentation quality compared to the baselines, while combining the ground-truth depths (EmbodiedSplat-D) further enhances the quality of the visualization..
4. Report the body metric and its denominator/aggregation: For each time step, we prune top L -1 indices by the confidence scores as described in Algorithm..
5. Re-run the body-reported ablation/failure condition: Figure 5. Online 3D reasoning for class "Bed". tures to each Gaussian, but incurs heavy memory overhead (2295 MB) due to the high dimensionality of CLIP. In con- trast, our EmbodiedSplat preserves ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat), p. 5 (4.1. EmbodiedSplat); the primary result is directionally consistent at p. 6 (Figure/Table caption), p. 8 (5.2. Ablation Studies), p. 7 (5.1. Experimental Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, follows, Novel mechanism이 Our EmbodiedSplat demonstrates better segmentation quality compared to the baselines, while combining the ground-truth depths (EmbodiedSplat-D) ... 대비 For each time step, we prune top L -1 indices by the confidence scores as described in Algorithm.을 개선하고, Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
