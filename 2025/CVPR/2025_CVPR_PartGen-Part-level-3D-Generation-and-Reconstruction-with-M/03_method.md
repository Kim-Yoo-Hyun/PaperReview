# Method

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_PartGen-Part-level-3D-Generation-and-Reconstruction-with-M/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our method leverages a multi-view diffusion model to extract plausible and view-consistent part segmentations from multiple views of a Work completed during Minghao Chen’s internship at Meta.
- To bridge this gap, we introduce PartGen, a novel approach for generating, from text, images, or unstructured 3D objects, 3D objects composed of meaningful parts.
- We then compare L̂ = k Ψ(Jˆk ) to the whole-object reconstruction L̂ = Ψ(I), i.e. without decomposing the object into parts, using the same protocol as for ...

## 원리적 동기
- Introduction view-consistent coloring problem, fine-tuning a multi-view image generator to produce several color-coded segmentation maps of the given 3D object.
- Text- or image-to-3D generators and 3D scanners can now produce 3D assets with high-quality shapes and textures, but as single, fused entities lacking meaningful structure.
- Our method leverages a multi-view diffusion model to extract plausible and view-consistent part segmentations from multiple views of a Work completed during Minghao Chen’s internship at Meta.

## 핵심 방법론
- We then compare L̂ = k Ψ(Jˆk ) to the whole-object reconstruction L̂ = Ψ(I), i.e. without decomposing the object into parts, using the same protocol as for ...
- 7, a variant of our method enables effective editing of the shape and texture of parts based on textual prompts.
- For illustration, we use the prompts from DreamFusion .
- Further training details are provided in the sup. mat.
- PartGen can reconstruct 3D parts that are minimally or even not visible, utilizing the guidance of a multi-view diffusion prior.
