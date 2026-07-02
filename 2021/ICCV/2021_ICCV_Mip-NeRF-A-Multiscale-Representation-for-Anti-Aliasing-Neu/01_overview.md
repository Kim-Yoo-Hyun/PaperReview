# Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields

- Year/Venue: 2021 / ICCV
- Category: Foundations: 3D Scene Representations
- Tags: NeRF, 3D Vision, representation, geometry
- Paper link: ./2021/ICCV/2021_ICCV_Mip-NeRF-A-Multiscale-Representation-for-Anti-Aliasing-Neu/paper.pdf
- Code/Project: https://jonbarron.info/mipnerf/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The rendering procedure used by neural radiance fields (NeRF) samples a scene with a single ray per pixel and may therefore produce renderings that are excessively blurred or ...
- The straightforward solution of supersampling by rendering with multiple rays per pixel is impractical for NeRF, because rendering each ray requires querying a multilayer perceptron hundreds of times.
- Our solution, which we call “mip-NeRF” (à la “mipmap”), extends NeRF to represent the scene at a continuously-valued scale.

## Core Idea
- Compared to NeRF, mip-NeRF reduces average error rates by 17% on the dataset presented with NeRF and by 60% on a challenging multiscale variant of that dataset that ...
- The rendering procedure used by neural radiance fields (NeRF) samples a scene with a single ray per pixel and may therefore produce renderings that are excessively blurred or ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Although NeRF and its variants have demonstrated impressive results across a range of view synthesis tasks, NeRF’s rendering model is flawed in a manner that can cause excessive ...
- By efficiently rendering anti-aliased conical frustums instead of rays, mip-NeRF reduces objectionable aliasing artifacts and significantly improves NeRF’s ability to represent fine details, while also being 7% faster ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Compared to NeRF, mip-NeRF reduces average error rates by 17% on the dataset presented with NeRF and by 60% on a challenging multiscale variant of that dataset that ...
- Although NeRF and its variants have demonstrated impressive results across a range of view synthesis tasks, NeRF’s rendering model is flawed in a manner that can cause excessive ...
- The rendering procedure used by neural radiance fields (NeRF) samples a scene with a single ray per pixel and may therefore produce renderings that are excessively blurred or ...

## Abstract Cue
- The rendering procedure used by neural radiance fields (NeRF) samples a scene with a single ray per pixel and may therefore produce renderings that are excessively blurred or aliased when training or testing images observe scene content at different resolutions.
