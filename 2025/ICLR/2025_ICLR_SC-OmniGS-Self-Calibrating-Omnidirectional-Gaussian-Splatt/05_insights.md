# Insights — SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7idCpuEAiR; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/113436. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose SC-OmniGS, a novel system that self-calibrates the omnidirectional camera model and poses along with omnidirectional radiance field reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** It can also facilitate other applications such as GS-based omnidirectional SLAM. • We introduced a novel differentiable omnidirectional camera model that effectively tackles the complex ...
- **p. 1 / ABSTRACT - extractive body cue:** We present SC-OmniGS, a novel self-calibrating omnidirectional Gaussian splatting system for fast and accurate omnidirectional radiance field reconstruction using 360-degree images.
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Moreover, considering omnidirectional images in the equirectangular projection have an unbalanced spatial resolution, we introduce weighted spherical photometric loss to ensure the spatially equivalent optimization.
- **p. 1 / ABSTRACT - extractive body cue:** Overall, the omnidirectional camera intrinsic model, extrinsic poses, and 3D Gaussians are jointly optimized by minimizing weighted spherical photometric loss.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given the lack of camera models accounting for the distortion of 360-degree images and the limitations of existing self-calibration approaches, there is an urgent need ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing methods for recovering 3D information from 360-degree images, including structure-from-motion (SfM) systems (Moulon et al., 2013; Huang & Yeung, 2022), rely on an idealized ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** It can achieve rapid radiance field reconstruction with no pose prior and render high-fidelity novel views. on SfM, some approaches (Lin et al., 2021; Jeong ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** However, we cannot apply a similar modification to 3D-GS based methods.
- **p. 10 / 6 CONCLUSION - extractive body cue:** With the differentiable omnidirectional camera model and Gaussian splatting procedure, our approach jointly optimizes 3D Gaussians, omnidirectional camera poses and camera model, leading to robust ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** OmniBlender dataset provides noise-free camera poses and depth maps.
- **Boundary to test:** However, we cannot apply a similar modification to 3D-GS based methods.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, omnidirectional camera poses, and camera models. • ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | When trained with pose perturbation, our full model, incorporating both camera model and pose optimization, consistently achieves improvement in both training and test view synthesis. | p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Failure/limitation | However, we cannot apply a similar modification to 3D-GS based methods. | p. 8 (5 EXPERIMENTS), p. 10 (6 CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 To rectify distortion patterns in the input image, we propose a differentiable omnidirectional camera model comprising a learnable 3D spherical grid to regress the camera distortion.를 (2023b), have demonstrated the feasibility and efficiency of reconstructing omnidirectional radiance fields in large scenes using sparse and wide-baseline 360-degree image inputs.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 However, we cannot apply a similar modification to 3D-GS based methods.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, omnidirectional camera poses, and camera models. • ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, we cannot apply a similar modification to 3D-GS based methods.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We evaluated SG-OmniGS against several SOTA models on datasets of 360-degree images, including eight real-world multi-room scenes from 360Roam dataset (Huang et al., 2022) each with on average 110 training views and ....
3. Compare against the body-reported baseline or a matched simpler baseline: Furthermore, when compared to other calibration baselines (see Barbershop in Table 1), SC-OmniGS consistently outperforms them with most increased rotation noise scales..
4. Report the body metric and its denominator/aggregation: Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors..
5. Re-run the body-reported ablation/failure condition: To validate the effectiveness of our camera calibration, we conducted ablation studies on a real scene Center, with and without perturbation to training cameras..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT); the primary result is directionally consistent at p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, main, contributions mechanism이 Furthermore, when compared to other calibration baselines (see Barbershop in Table 1), SC-OmniGS consistently outperforms them ... 대비 Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors.을 개선하고, However, we cannot apply a similar modification to 3D-GS based methods. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
