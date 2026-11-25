# LADDER: A Long-Horizon Robot Manipulation Benchmark

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

같은 환경에서 하위 목표 수를 1–10개로 바꾸고 직접 지시, 하위 지시, 도구 선택을 비교한다.

저자는 3개 시뮬레이션 평가군, 145과제, 시스템당 2,024회와 두 로봇 구성의 실물 실험을 보고했다. 시스템별 제어·추론 예산을 함께 봐야 한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.18053) · [저자 project/code](https://ladder.insait.ai/) · [공식 code](https://github.com/insait-institute/ladder). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 시스템별 사용 가능한 성공 판정, 재시도 권한과 평가 예산은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

긴 조작의 계획 오류와 실행 오류를 추적할 수 있는 공개 실행 기록이 있어 일반 정책 비교에 직접 필요하다.

### Dependency and Evolution

RoboMME가 기억 의존성을 평가하는 축에 하위 목표 수와 실행 구조를 통제하는 축을 추가한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 과제·정책·남은 시간을 맞춘 실행 쌍에서 단계별 완료와 다음 물체의 실제 접촉을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

첫 목표 뒤 과제가 실패할 때 다음 목표를 선택하기 이전과 실제 조작 이후의 실패 비율은 어떻게 다른가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
