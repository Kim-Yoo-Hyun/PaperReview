# ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera Samplings and Diffusion Priors

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_ExploreGS-Explorable-3D-Scene-Reconstruction-with-Virtual/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This limitation stems from missing information, since optimization-based approaches cannot synthesize contents beyond the observed data.
- However, existing methods struggle with artifacts and missing regions when rendering from viewpoints that deviate from the training trajectory, limiting seamless scene exploration.
- Unfortunately, such an experience is yet to be fully realized, as existing methods suffer from severe degradations in rendering quality when viewpoints deviate signiﬁcantly from the input observations.

## Core Idea
- To evaluate our method, we present Wild-Explore, a benchmark designed for challenging scene exploration.
- To address this, we propose a 3DGS-based pipeline that generates additional training views to enhance reconstruction.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- demonstrate that our approach outperforms existing 3DGSbased methods, enabling high-quality, artifact-free rendering from arbitrary viewpoints.
- We introduce an information-gain-driven virtual camera placement strategy to maximize scene coverage, followed by video diffusion priors to reﬁne rendered results.
- Fine-tuning 3D Gaussians with these enhanced views signiﬁcantly improves reconstruction quality.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To evaluate our method, we present Wild-Explore, a benchmark designed for challenging scene exploration.
- demonstrate that our approach outperforms existing 3DGSbased methods, enabling high-quality, artifact-free rendering from arbitrary viewpoints.
- We introduce an information-gain-driven virtual camera placement strategy to maximize scene coverage, followed by video diffusion priors to reﬁne rendered results.

## Abstract Cue
- demonstrate that our approach outperforms existing 3DGSbased methods, enabling high-quality, artifact-free rendering from arbitrary viewpoints.
