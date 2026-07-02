# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Large Multimodal Models
- Tags: Vision-Language, 3D spatial, grounding
- Paper link: ./2026/CVPR/2026_CVPR_Grounded-3D-Aware-Spatial-Vision-Language-Modeling/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present GR3D, a spatial vision language model equipped with three complementary grounding capabilities—explicit 2D grounding, implicit 2D grounding, and monocular 3D grounding—within a single framework.
- Our method surpasses prior Region-VLMs (*), which require manual annotated masks.
- To obtain them, we use Florence-2 to generate candidate 2D bounding boxes and class labels for each textual mention, producing dense but noisy region annotations.

## 원리적 동기
- Together, these grounding capabilities enable GR3D to decompose complex spatial understanding problems into grounded 2D perception followed by 3D inference.
- Two challenges, in particular, are under-addressed. (i) Implicit 2D grounding is scarce: most systems support explicit “point to X” grounding but
- We present GR3D, a spatial vision language model equipped with three complementary grounding capabilities—explicit 2D grounding, implicit 2D grounding, and monocular 3D grounding—within a single framework.

## 핵심 방법론
- Our method surpasses prior Region-VLMs (*), which require manual annotated masks.
- To obtain them, we use Florence-2 to generate candidate 2D bounding boxes and class labels for each textual mention, producing dense but noisy region annotations.
- Together, region-prompt grounding, structured 3D box representation, intrinsic normalization, and scalable training signals address both linguistic and geometric ambiguities of monocular 3D grounding.
