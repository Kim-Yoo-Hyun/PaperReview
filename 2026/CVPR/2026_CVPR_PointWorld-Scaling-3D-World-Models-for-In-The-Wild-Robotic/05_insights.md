# PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

State와 robot action을 3D point flow 공간에서 연결하고 action-conditioned scene dynamics를 학습한다.

CVF abstract/저자 project는 real/sim training data와 Franka의 pushing·deformable/articulated manipulation·tool use 평가를 설명한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://point-world.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 RGB-D calibration, point-flow action 변환, partial observability와 MPC cost 정의은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend / action-relevant 3D. State와 action을 3D point flow로 표현하고 예측을 manipulation MPC에 연결한다. DP3/3D-VLA 이후 explicit geometry와 world model을 비교할 직접적인 연결이다. 본문 평가의 보장 범위와 calibration 의존성은 추가 확인 대상이다.

### Dependency and Evolution

DP3/3D-VLA + TD-MPC2 → PointWorld; 일반 reconstruction과 downstream control 구분.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

간단한 pushing task에서 3D model과 visual model의 action ranking을 비교하고 prediction error와 실제 goal error를 함께 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 action 후보와 compute budget에서 3D point-flow dynamics가 video-prediction MPC보다 contact outcome을 더 잘 구분하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
