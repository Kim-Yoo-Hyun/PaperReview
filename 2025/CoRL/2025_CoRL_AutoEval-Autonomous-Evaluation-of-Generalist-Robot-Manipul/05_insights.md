# AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

평가 job scheduling·자동 success 검출·scene reset을 결합한다.

WidowX/BridgeData 계열 실제 평가와 수동 판정을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/zhou25a.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 target start distribution, 자동 judge 오류, 제외 trial, human 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C5/C6의 reset ledger와 반복 평가를 설계할 핵심 system 기준이다.

### Dependency and Evolution

Robot policy evaluation → AutoEval → STEP/NSCORE.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Policy를 고정하고 reset 실패·retry·human rescue까지 포함한 ledger를 작성한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

자동 reset 성공 조건이 정책 비교 분포를 편향시키는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
