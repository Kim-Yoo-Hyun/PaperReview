# Problem

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_ExploreGS-Explorable-3D-Scene-Reconstruction-with-Virtual/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- This limitation stems from missing information, since optimization-based approaches cannot synthesize contents beyond the observed data.
- However, existing methods struggle with artifacts and missing regions when rendering from viewpoints that deviate from the training trajectory, limiting seamless scene exploration.
- Unfortunately, such an experience is yet to be fully realized, as existing methods suffer from severe degradations in rendering quality when viewpoints deviate signiﬁcantly from the input observations.

## 해결하려는 문제
- To evaluate our method, we present Wild-Explore, a benchmark designed for challenging scene exploration.
- demonstrate that our approach outperforms existing 3DGSbased methods, enabling high-quality, artifact-free rendering from arbitrary viewpoints.
- We introduce an information-gain-driven virtual camera placement strategy to maximize scene coverage, followed by video diffusion priors to reﬁne rendered results.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
