# Insights — WaterSplatting: Fast Underwater 3D Scene Reconstruction using Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://arxiv.org/pdf/2408.08206.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Splatting with Medium: We introduce a novel approach that combines the strengths of Gaussian Splatting (GS) and volume rendering.
- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** We illustrate the pipeline of our method in Fig.
- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ...
- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** Under the occlusion of both primitives and medium, our model acquires the transmittance along the ray and is capable of synthesizing medium component and object ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** For scene rendering in scattering media we use the revised underwater image formation model from [1] where the final image I is separated into a ...
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** Integrating regularization into the LReg-DSSIM formulation becomes particularly critical for 3DGS optimization due to the discrete nature of its primitives, necessitating structural regularization to maintain ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Splatting with Medium), p. 4 (3.3. Loss Function Alignment), p. 3 (3.2. Splatting with Medium), p. 3 (3.1. Preliminaries)

### Strongest assumption and failure boundary

- **p. 1 / Abstract - extractive body cue:** The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences.
- **p. 1 / Abstract - extractive body cue:** The problem was successfully tackled by fully volumetric NeRF-based methods which can model both the geometry and the medium (water).
- **p. 7 / 5. Limitations - extractive body cue:** Although our method achieves good reconstruction quality, there are some limitations to consider.
- **p. 7 / 5. Limitations - extractive body cue:** However, in the foreground, our method prunes medium-role primitives well while SeaThru-NeRF cannot prevent the geometrical field from fitting the medium, resulting in wave-like artifacts.
- **p. 8 / 5. Limitations - extractive body cue:** Limitation: insufficient supervision.
- **p. 8 / 5. Limitations - extractive body cue:** Limitation: simulating distant medium with Gaussians.
- **p. 6 / 4.1. Results - extractive body cue:** Both traditional 3DGS and NeRF with a proposal sampler cannot handle semitransparent medium well.
- **Boundary to test:** Although our method achieves good reconstruction quality, there are some limitations to consider.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera. | p. 7 (4.1. Results), p. 6 (4.1. Results) |
| Failure/limitation | Although our method achieves good reconstruction quality, there are some limitations to consider. | p. 7 (5. Limitations), p. 7 (5. Limitations) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 The input to our model is a set of images with scattering medium and corresponding camera poses.를 In the meantime, 3DGS prunes primitives with low opacity for acceleration and periodically set αi close to zero for all Gaussians to moderate the increase of floaters close to the input cameras.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Although our method achieves good reconstruction quality, there are some limitations to consider.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although our method achieves good reconstruction quality, there are some limitations to consider.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: SeaThru-NeRF Dataset: SeaThru-NeRF Dataset released by [18] contains real-world scenes acquired from four different scenes in sea: IUI3 Red Sea, Curac¸ao, Japanese Gardens Red Sea, and Panama..
3. Compare against the body-reported baseline or a matched simpler baseline: Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera..
4. Report the body metric and its denominator/aggregation: We present the alpha blending of depth as the depth map and the rendering without medium to demonstrate the ability to decouple the medium and the object for SeaThru-NeRF and our method..
5. Re-run the body-reported ablation/failure condition: We conduct a quantitative analysis on different combination of loss functions, between pixel-wise component {L1, L2, LReg-L1, LReg-L2} and frame-wise {LDSSIM, LReg-DSSIM}, as well as removing the medium effect and removing both ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.3. Loss Function Alignment), p. 3 (3.1. Preliminaries), p. 5 (3.3. Loss Function Alignment); the primary result is directionally consistent at p. 7 (4.1. Results), p. 6 (4.1. Results), p. 7 (4.1. Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Loss, Function, Alignment mechanism이 Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes ... 대비 We present the alpha blending of depth as the depth map and the rendering without medium to demonstrate ...을 개선하고, Although our method achieves good reconstruction quality, there are some limitations to consider. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
