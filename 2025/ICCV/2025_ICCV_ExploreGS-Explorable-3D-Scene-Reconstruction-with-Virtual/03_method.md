# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_ExploreGS-Explorable-3D-Scene-Reconstruction-with-Virtual/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To evaluate our method, we present Wild-Explore, a benchmark designed for challenging scene exploration.
- To address this, we propose a 3DGS-based pipeline that generates additional training views to enhance reconstruction.
- We introduce an information-gain-driven virtual camera placement strategy to maximize scene coverage, followed by video diffusion priors to reﬁne rendered results.

## 원리적 동기
- This limitation stems from missing information, since optimization-based approaches cannot synthesize contents beyond the observed data.
- However, existing methods struggle with artifacts and missing regions when rendering from viewpoints that deviate from the training trajectory, limiting seamless scene exploration.
- To evaluate our method, we present Wild-Explore, a benchmark designed for challenging scene exploration.

## 핵심 방법론
- Although both our image-level conﬁdence map and scale based one are effective, our method leads to slight better performance.
- For uncertainty-based method, we observe that it is sensitive to 3D Gaussians with large scales,
