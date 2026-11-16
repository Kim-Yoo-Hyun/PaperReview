# EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Embodiment-centric flow와 goal alignment를 학습하고 URDF 제약으로 행동에 변환한다.

Meta-World와 실제 가림·변형·비변위 조작을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html) · [저자 project/code](https://ec-flow1.github.io/) · [공식 code](https://github.com/YixiangChen515/EC-Flow). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 URDF만으로 해결되는 변환 범위, calibration, 동역학·접촉 정보 의존성은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

행동 표현을 통합하는 연구에서 object motion과 robot motion의 차이를 보존할 대안이다.

### Dependency and Evolution

General Flow·FlowBot·PointVLA와 embodiment 제약의 주입 위치를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 task의 object-centric와 embodiment-centric 표현을 비교하고 URDF·제어 오차를 따로 바꾼다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 영상 supervision에서 embodiment flow가 target robot 동역학 변화에도 유효한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
