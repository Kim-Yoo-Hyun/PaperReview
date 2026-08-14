# Problem

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2024 / CVPR
- Category: 3D Geometry, Reconstruction, and SLAM
- Tags: 3D reconstruction, calibration, geometry
- Paper link: ./2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/paper.pdf
- Code/Project: https://github.com/naver/dust3r
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We cast the pairwise reconstruction problem as a regression of pointmaps, relaxing the hard constraints of usual projective camera models.
- This is possible because our network jointly processes the input images and the resulting 3D pointmaps, thus learning to associate 2D structures with 3D shapes, and having the ...

## 해결하려는 문제
- We base our network architecture on standard Transformer encoders and decoders, allowing us to leverage powerful pretrained models.
- Exhaustive experiments on all these tasks showcase that the proposed DUSt3R can unify various 3D vision tasks and set new SoTAs on monocular/multi-view depth estimation as well as ...
- We drift away from the trend of integrating task-specific modules , and instead adopt a fully data-driven strategy based on a generic transformer a

## 선행 연구 / 배경 단서
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.
