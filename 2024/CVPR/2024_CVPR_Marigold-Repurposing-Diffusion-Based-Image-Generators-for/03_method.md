# Method

- Year/Venue: 2024 / CVPR
- Category: Foundations: Monocular Geometry
- Tags: Diffusion, Generation, depth, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Marigold-Repurposing-Diffusion-Based-Image-Generators-for/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce Marigold, a method for affine-invariant 1.
- The impressive progress of monocular depth estimators has mirrored the growth in model capacity, from relatively modest CNNs to large Transformer architectures.
- The estimator can be fine-tuned in a couple of days on a single GPU using only synthetic training data.

## 원리적 동기
- Clearly, undoing the projection from the 3D world to a 2D image is a geometrically ill-posed problem and can only be solved with the help of prior knowledge, ...
- Still, monocular depth estimators tend to struggle when presented with images with unfamiliar content and layout, since their knowledge of the visual world is restricted by the data ...
- We introduce Marigold, a method for affine-invariant 1.

## 핵심 방법론
- # Training samples Real Synthetic DiverseDepth MiDaS LeReS Omnidata HDN DPT 320K 2M 300K 11.9M 300K 1.2M Ours (w/o ensemble) Ours (w/ ensemble) — † ∗ ∗ NYUv2 ...
