# MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

VLA의 end-effector waypoint와 base–arm bi-level trajectory optimization을 연결한다.

OVMM 및 실제 로봇 평가를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html) · [저자 project/code](https://gary3410.github.io/momanipVLA/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 waypoint frame, solver budget, controller, real-robot split은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

NaVILA·MoTo와 함께 VLA와 기하학적 실행 가능성의 경계를 비교하는 NEXT다.

### Dependency and Evolution

OpenVLA의 고정-base action interface → MoManipVLA의 base/arm 실행 가능성 → MoTo의 interaction-aware docking을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Base 고정과 이동 허용을 동일 waypoint·collision 조건에서 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Base 이동의 이득이 동일 waypoint와 motion planner를 맞춰도 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
