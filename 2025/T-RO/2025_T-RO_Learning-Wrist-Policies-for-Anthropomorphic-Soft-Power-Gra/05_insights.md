# Learning Wrist Policies for Anthropomorphic Soft Power Grasping in Handle and Door Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

손·팔을 하나의 임피던스 제어기로 다루며, 손목 임피던스와 손바닥·손가락 힘을 함께 조절하는 정책을 학습한다.

시뮬레이션에서 학습하고 완전 구동 손과 부족 구동 손을 장착한 서비스 휴머노이드에서 손잡이·문 조작을 검증했다.

근거: [공식 paper/abstract](https://portal.fis.tum.de/en/publications/learning-wrist-policies-for-anthropomorphic-soft-power-grasping-i/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 손의 구동 형태와 문 유형별 시험 조건 및 힘·속도 제어 기준선은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

걸쇠와 손잡이 실험에서 재학습 없는 순응 제어 기준을 제공한다.

### Dependency and Evolution

손목 임피던스 학습과 휴머노이드 접촉 제어를 연결하는 비교 문헌이다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

손잡이 초기 자세 오류를 독립적으로 바꿔 일정 손목 강성과 순응 정책의 손잡이 파지 유지율을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

손잡이의 기하 오차 강건성과 저항 해제 직후의 몸통 균형을 서로 다른 지표로 다룬다.

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
