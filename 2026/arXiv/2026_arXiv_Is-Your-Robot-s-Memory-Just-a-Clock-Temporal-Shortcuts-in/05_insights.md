# Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

무효 pause/fidget과 memory/timestamp 대조로 temporal shortcut을 진단하고 event-indexed memory를 비교한다.

RoboMME counting task에서 무효 사건·시간표식·memory 입력을 통제해 성공 변화를 측정한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2611.14488) · [저자 project/code](https://github.com/bennidict23/memory-clock). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 미확인 항목: event 기준의 관측 접근권·counting task 외 전이·제어 개입과 memory 효과의 분리.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

기억의 시간 편향 진단과 사건 기반 index가 이미 선행임을 반영할 직접 반대 근거다.

### Dependency and Evolution

RoboMME·FrameSamp 계열의 memory indexing과 기존 SET/FEEDBACK 질문을 연결한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

무효 사건·같은 관측의 memory withholding·event index를 먼저 대조하고 잔여 오류를 분리한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

무효 사건 제어 뒤에도 물리적 결과가 다른 사례에서 남는 memory 상태 오류가 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
