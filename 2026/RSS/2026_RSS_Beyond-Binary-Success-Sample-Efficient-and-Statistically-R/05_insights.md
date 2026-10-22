# Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Progress 등 bounded metric에 기반한 통계적 순차 비교를 제안한다.

Simulation과 실제 robot policy 비교를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p076.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 boundedness, anytime 보장, metric 편향, 반복 model selection은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C6의 progress-aware 선택을 신규 통계 방법으로 재주장하지 않도록 하는 최신 기준이다.

### Dependency and Evolution

STEP·progress reward → NSCORE.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Independent outcome과 progress judge를 분리해 같은 policy 쌍의 결론을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

학습에 사용한 judge를 평가에도 쓰면 순위가 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
