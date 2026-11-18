# GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

로봇 keypoint trajectory와 3D Gaussian geometry 예측을 학습 supervision으로 사용한다.

RoboCasa Human-50·LIBERO·실세계 조작에서 geometry 관련 이득을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html) · [저자 project/code](https://github.com/jingjingqian75/GeoPredict). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Depth supervision·keypoint target·배포 추가 token 비용·baseline data fairness은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

3D reconstruction auxiliary loss 자체가 새 기여가 아님을 보여 주는 직접 VLA 비교다.

### Dependency and Evolution

SpatialVLA의 입력 geometry와 GeoPredict의 학습 시 미래 geometry supervision을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 policy/data에서 global geometry와 task-local geometry loss를 compute-matched 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

접촉 ROI의 예측 오차를 줄이는 supervision이 전체 scene reconstruction보다 행동에 유리한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
