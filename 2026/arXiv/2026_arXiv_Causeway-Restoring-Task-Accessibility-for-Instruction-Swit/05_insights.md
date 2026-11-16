# Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

목표 작업의 re-entry pose를 조건으로 frozen decoder를 통한 gradient를 이용해 action-stream 표현을 수정하고, 정책 자체가 복귀 행동을 생성하는 inference-time 개입을 제안한다.

LIBERO-Goal, LIBERO-Object와 실제 xArm에서 instruction switching과 복구를 보고한다. 정확한 비교 수치·시행 수·특권 정보 조건은 신규 노트에서 본문 정독 완료로 표시하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.30913). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 re-entry pose 획득과 관측 접근, decoder별 개입 위치·계산 비용, 복귀/인계 조건, 실제 로봇 평가 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

전환 실패를 의미 기억 오류로 오인하지 않기 위한 직접 경쟁 설명이다. 새 목표의 물리적 실행 가능성과 언어 해석을 분리할 NEXT로 추가하며 preprint status를 유지한다.

### Dependency and Evolution

ReSteer의 상태별 steerability ↔ Causeway의 동결 정책 복구; Hi Robot의 지시 해석과 물리적 접근 가능성을 구별.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 시작·수정 상태에서 원자 목표와 oracle 복합 지시의 능력을 먼저 구분한다. Causeway 개입을 비교하려면 re-entry 정보와 추가 계산 비용을 별도로 맞추며 현재 P0에 자동 추가하지 않는다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

의미적으로 정확한 지시에서도 나타나는 continuation 실패를 분리한 뒤, 부분 수정 상태 관리의 행동 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
