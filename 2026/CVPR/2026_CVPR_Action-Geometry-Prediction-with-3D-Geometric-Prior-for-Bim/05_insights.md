# Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

3D foundation latent·2D semantic feature·proprioception을 합쳐 action chunk와 미래 3D latent를 공동 예측한다.

RoboTwin simulation과 실세계 양팔 조작에서 성공·협응·공간 예측을 비교한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://github.com/Chongyang-99/GAP). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 미래 geometry target·3D foundation freeze 여부·양팔 action frame·data budget은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

관계 기반 탐색 후보에서 geometry representation 이득과 exploration 변경의 이득을 구별하는 직접 비교다.

### Dependency and Evolution

Diffusion Policy/DP3 → GAP의 action-geometry 예측 → 관계 조건 탐색을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 action-geometry backbone과 데이터에서 독립/관계 조건 noise만 바꾼다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Geometry 예측을 이미 학습한 actor에서도 관계별 exploration 분포 변경이 추가로 유효한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
