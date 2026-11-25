# Evaluation - Instant Neural Graphics Primitives with a Multiresolution Hash Encoding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.05989; PDF retrieval source: https://arxiv.org/pdf/2201.05989. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (24.2 M), p. 9 (24.2 M), p. 3 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 8 (24.2 M), p. 5 (Figure/Table caption)): It approaches NeRF's quality after training for just ∼5 min, yet is outperformed by our full method after training for 5 s-15 s, amounting to a 20-60× improvement that can ...

## Evaluation Body Digest

- **p. 9 / 24.2 M - extractive body cue:** At HD resolutions, synthetic and even real-world scenes can be trained in seconds and rendered at 60 FPS, without the need of caching of the ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5.1 Gigapixel Image Approximation Learning the 2D to RGB mapping of image coordinates to colors has become a popular benchmark for testing a model's ability ...
- **p. 9 / 24.2 M - extractive body cue:** Other scenes behave almost identically.
- **p. 10 / 24.2 M - extractive body cue:** On one hand, our method performs best on scenes with high geometric detail, such as Ficus, Drums, Ship and Lego, achieving the best PSNR of ...
- **p. 10 / 24.2 M - extractive body cue:** On the other hand, mip-NeRF and NSVF outperform our method on scenes with complex, view-dependent reflections, such as Materials; we attribute this to the much ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We target our multiresolution hash encoding at the same task and converge to high-fidelity images in seconds to minutes (Figure 4).
- **원문 대조:** Neural radiance caching의 MLP는 feature buffer에서 각 픽셀의 색을 예측한다. 인코딩 대상에는 world-space position이 포함되며, 렌더링 중 온라인으로 학습한다. ([PDF p. 8](https://arxiv.org/pdf/2201.05989#page=8), Figure 8).
- **p. 8 / 24.2 M - extractive body cue:** Our hash encoding exhibits similar numeric quality in terms of intersection over union (IoU) and can be evaluated anywhere in the scene.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); B IMPLEMENTATION DETAILS OF NGLOD (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 24.2 M | EMPIRICAL / REAL-ROBOT OR HARDWARE | It approaches NeRF's quality after training for just ∼5 min, yet is outperformed by our full method after training for 5 s-15 s, amounting ... | p. 10 (24.2 M) |
| 24.2 M | EMPIRICAL / REAL-ROBOT OR HARDWARE | Due to the small size and efficient implementation of the MLP, it is only 15% more expensive-well worth the significantly improved quality. function, which ... | p. 9 (24.2 M) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 2. A demonstration of the reconstruction quality of different encodings and parametric data structures for storing trainable feature embeddings. Each configuration was trained ... | p. 3 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2021], which achieves state-of-the-art results in both quality and speed by prefixing its small MLP with a lookup from an octree of trainable feature ... | p. 7 (5 EXPERIMENTS) |
| 24.2 M | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2021] gains much improved quality from the multiresolution hash encoding with only a mild performance penalty: 133 versus 147 frames per second at a ... | p. 8 (24.2 M) |

## Dataset / Benchmark Role

- **p. 9 / 24.2 M - extractive body cue:** At HD resolutions, synthetic and even real-world scenes can be trained in seconds and rendered at 60 FPS, without the need of caching of the ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5.1 Gigapixel Image Approximation Learning the 2D to RGB mapping of image coordinates to colors has become a popular benchmark for testing a model's ability ...
- **p. 9 / 24.2 M - extractive body cue:** Other scenes behave almost identically.
- **p. 10 / 24.2 M - extractive body cue:** On one hand, our method performs best on scenes with high geometric detail, such as Ficus, Drums, Ship and Lego, achieving the best PSNR of ...
- **p. 10 / 24.2 M - extractive body cue:** On the other hand, mip-NeRF and NSVF outperform our method on scenes with complex, view-dependent reflections, such as Materials; we attribute this to the much ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We target our multiresolution hash encoding at the same task and converge to high-fidelity images in seconds to minutes (Figure 4).
- **원문 대조:** Neural radiance caching의 MLP는 feature buffer에서 각 픽셀의 색을 예측한다. 인코딩 대상에는 world-space position이 포함되며, 렌더링 중 온라인으로 학습한다. ([PDF p. 8](https://arxiv.org/pdf/2201.05989#page=8), Figure 8).
- **p. 8 / 24.2 M - extractive body cue:** Our hash encoding exhibits similar numeric quality in terms of intersection over union (IoU) and can be evaluated anywhere in the scene.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. We demonstrate instant training of neural graphics primitives on a single GPU for multiple tasks. In Gigapixel image we represent a gigapixel image ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. A demonstration of the reconstruction quality of different encodings and parametric data structures for storing trainable feature embeddings. Each configuration was trained for ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Illustration of the multiresolution hash encoding in 2D. (1) for a given input coordinate x, we find the surrounding voxels at 𝐿resolution levels ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Hash encoding parameters and their ranges in our results. Only the hash table size𝑇and max. resolution 𝑁max need to be tuned to the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. The main curves plot test error over training time for varying hash table size 𝑇which determines the number of trainable encoding parameters. Increasing ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5. Test error over training time for fixed values of feature dimensionality 𝐹as the number of hash table levels 𝐿is varied. To maintain a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. This is explained by the 6 MB L2 cache of our NVIDIA RTX 3090 GPU, which becomes too small for individual levels when ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Approximating an RGB image of resolution 20 000 × 23 466 (469 M RGB pixels) with our multiresolution hash encoding. With hash table ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | At HD resolutions, synthetic and even real-world scenes can be trained in seconds and rendered at 60 FPS, without the need of caching of ... | embodiment, simulator version and control stack | p. 9 (24.2 M), p. 7 (5 EXPERIMENTS) |
| Task/environment | 5.1 Gigapixel Image Approximation Learning the 2D to RGB mapping of image coordinates to colors has become a popular benchmark for testing a model's ... | reset, timeout, object/scene variation | p. 7 (5 EXPERIMENTS), p. 9 (24.2 M) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 4. The main curves plot test error over training time for varying hash table size 𝑇which determines the number of trainable encoding parameters. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 5. Test error over training time for fixed values of feature dimensionality 𝐹as the number of hash table levels 𝐿is varied. To maintain ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 7. Neural signed distance functions trained for 11 000 steps. The frequency encoding [Mildenhall et al. 2020] struggles to capture the sharp details ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| IoU is always ≤1 with a perfect fit corresponding to = 1. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| We measure IoU by comparing the signs of the SDFs at 128 million points uniformly distributed within the bounding box of the scene. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| The effect of the MLP size on test error vs. training time (31 000 training steps) on the Lego scene. | definition/direction/unit from same section | p. 9 (24.2 M) |
| For photorealistic rendering, the neural radiance cache is typically queried only for indirect path contributions, which masks its reconstruction error behind the first reflection. | definition/direction/unit from same section | p. 9 (24.2 M) |
| For each scene, we mark the methods with least error using gold , silver , and bronze medals. | definition/direction/unit from same section | p. 10 (24.2 M) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As baseline, we compare with NGLOD [Takikawa et al. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| 2020] to provide a baseline, details of which are found in Appendix D. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| It approaches NeRF's quality after training for just ∼5 min, yet is outperformed by our full method after training for 5 s-15 s, amounting ... | comparison identity and matched condition | p. 10 (24.2 M) |
| On the other hand, mip-NeRF and NSVF outperform our method on scenes with complex, view-dependent reflections, such as Materials; we attribute this to the ... | comparison identity and matched condition | p. 10 (24.2 M) |
| Figure 4. This is explained by the 6 MB L2 cache of our NVIDIA RTX 3090 GPU, which becomes too small for individual levels ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| We experimentally verified that this does not lead to reduced quality, compared to looking up the entire hierarchy. | comparison identity and matched condition | p. 13 (B IMPLEMENTATION DETAILS OF NGLOD) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 12. NeRF reconstruction of a modular synthesizer and large natural 360 scene. The left image took 5 seconds to accumulate 128 samples at ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| The effect of the MLP size on test error vs. training time (31 000 training steps) on the Lego scene. | component/input/data sensitivity | p. 9 (24.2 M) |
| This sensitivity reveals undesired microstructure in our hash encoding on the scale 2IoU is the ratio of volumes of the interiors of the intersection ... | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| However, even without such a dedicated data structure, our encoding approaches a similar fidelity to NGLOD in terms of the intersectionover-union metric (IoU2) with ... | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| At HD resolutions, synthetic and even real-world scenes can be trained in seconds and rendered at 60 FPS, without the need of caching of ... | component/input/data sensitivity | p. 9 (24.2 M) |
| It could thus keep improving slightly if trained for extended periods of time, as in the offline NeRF variants that are often trained for ... | component/input/data sensitivity | p. 10 (24.2 M) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method-Figure 2 (e,f)-combines both ideas to reduce waste. | It approaches NeRF's quality after training for just ∼5 min, yet is outperformed by our full method after training for 5 s-15 s, amounting ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (24.2 M), p. 9 (24.2 M), p. 3 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 8 (24.2 M), p. 5 (Figure/Table caption) |
| Primary metric/result | Due to the small size and efficient implementation of the MLP, it is only 15% more expensive-well worth the significantly improved quality. function, which ... | numeric claim only at cited anchor | p. 9 (24.2 M) |

- Numeric sentences retained from the body:
- **p. 8 / 24.2 M - extractive body cue:** Neural signed distance functions trained for 11 000 steps.
- **p. 8 / 24.2 M - extractive body cue:** Multiresolution hash encoding (Ours), 𝑇= 15, 133 FPS Triangle wave encoding [Müller et al.
- **p. 8 / 24.2 M - extractive body cue:** 2021], 147 FPS Far view Medium view Close-by view Far view Medium view Close-by view Fig.
- **p. 8 / 24.2 M - extractive body cue:** 2021] gains much improved quality from the multiresolution hash encoding with only a mild performance penalty: 133 versus 147 frames per second at a resolution ...
- **p. 9 / 24.2 M - extractive body cue:** [2021]-our encoding results in sharper reconstruction while incurring only a mild performance overhead of 0.7 ms that reduces the frame rate from 147 to 133 ...
- **p. 9 / 24.2 M - extractive body cue:** Notably, the neural radiance cache is trained online-during rendering-from a path tracer that runs in the background, which means that the 0.7 ms overhead includes ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The MLP allows for resolving specular details and reduces the amount of background noise caused by hash collisions. | p. 9 (24.2 M) |
| body limitation/failure cue | Lookups along the hierarchy of this octree act similarly to our multiresolution cascade of grids: they are a collision-free analog to our technique, with ... | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | However, it also exhibits visually undesirable surface roughness that we attribute to randomly distributed hash collisions. | p. 8 (24.2 M) |
| body limitation/failure cue | Since NGLOD is essentially a collision-free analog to our hash encoding, we attribute this artifact to hash collisions. | p. 9 (24.2 M) |
| body limitation/failure cue | While the linear layer is capable of reproducing view-dependent effects, the quality is significantly compromised as compared to the MLP, which is better able ... | p. 10 (24.2 M) |
| body limitation/failure cue | Microstructure due to hash collisions. | p. 11 (24.2 M) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The effect of the MLP size on test error vs. training time (31 000 training steps) on the Lego scene. | p. 9 (24.2 M) |
| We decay the learning rate after 20 k steps by a factor of 0.33, which we repeat every further 10 k steps. | p. 10 (24.2 M) |
| In the code released alongside this paper, we have included a preliminary implementation that fits a radiance and density field directly from the noisy ... | p. 11 (24.2 M) |
| Informed by this analysis, we choose 𝑁layers = 2 and 𝑁neurons = 64. of the finest grid resolution, which is absent in NGLOD and ... | p. 9 (24.2 M) |
| To highlight the versatility and high quality of the encoding, we compare it with previous encodings in four distinct computer graphics primitives that benefit ... | p. 7 (5 EXPERIMENTS) |
| Neural signed distance functions trained for 11 000 steps. | p. 8 (24.2 M) |
| The feature buffers contain, among other variables, the world-space position x, which we propose to encode with our method. | p. 8 (24.2 M) |
| This amounts to 50 k steps after 5 min at which point the model is well converged. | p. 10 (24.2 M) |

## Limitations and Verification Questions

- **p. 9 / 24.2 M - extractive body cue:** The MLP allows for resolving specular details and reduces the amount of background noise caused by hash collisions.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Lookups along the hierarchy of this octree act similarly to our multiresolution cascade of grids: they are a collision-free analog to our technique, with a ...
- **p. 8 / 24.2 M - extractive body cue:** However, it also exhibits visually undesirable surface roughness that we attribute to randomly distributed hash collisions.
- **p. 9 / 24.2 M - extractive body cue:** Since NGLOD is essentially a collision-free analog to our hash encoding, we attribute this artifact to hash collisions.
- **p. 10 / 24.2 M - extractive body cue:** While the linear layer is capable of reproducing view-dependent effects, the quality is significantly compromised as compared to the MLP, which is better able to ...
- **p. 11 / 24.2 M - extractive body cue:** Microstructure due to hash collisions.

- **Evidence anchors reviewed:** datasets p. 9 (24.2 M), p. 7 (5 EXPERIMENTS), p. 9 (24.2 M), p. 10 (24.2 M), p. 10 (24.2 M), p. 7 (5 EXPERIMENTS), metrics p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (24.2 M), baselines p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 10 (24.2 M), p. 10 (24.2 M), p. 6 (Figure/Table caption), p. 13 (B IMPLEMENTATION DETAILS OF NGLOD), results p. 10 (24.2 M), p. 9 (24.2 M), p. 3 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 8 (24.2 M), p. 5 (Figure/Table caption).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
