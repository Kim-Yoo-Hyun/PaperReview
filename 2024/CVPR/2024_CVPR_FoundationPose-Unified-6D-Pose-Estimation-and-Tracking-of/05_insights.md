# FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Neural implicit 표현으로 두 입력 조건을 연결해 동일 pose 모듈을 재사용한다. 새 물체별 fine-tuning 없이 적용하는 설정이다.

공식 project는 미지 물체 pose estimation/tracking의 일반화를 제시한다. 이번 등록에서는 세부 trial·로봇 성공률을 확정하지 않는다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html) · [저자 project/code](https://nvlabs.github.io/FoundationPose/) · [공식 code](https://github.com/NVlabs/FoundationPose). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Model-free reference 요구·대칭 처리·ranking score와 보정 확률의 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

현재 능동 관측 후보의 pose baseline이며 CAD/reference·score·좌표 가정을 판단하는 직접 NEXT다.

### Dependency and Evolution

기하학적 pose/registration → FoundationPose → ActivePose의 시점 선택과 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 CAD·깊이·카메라 조건에서 pose coverage와 실제 배치 성공을 따로 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 pose 오차에서도 task별 허용 오차에 따라 필요한 추가 관측이 달라지는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
