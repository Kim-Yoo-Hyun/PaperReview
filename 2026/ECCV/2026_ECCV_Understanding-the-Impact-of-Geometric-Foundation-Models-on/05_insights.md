# Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

GR00T-N1.5와 VGGT를 고정한 비교에서 geometry를 읽어내는 probe와 세 가지 geometry 결합 구조를 분석한다.

공식 초록은 특정 VLA/GFM 조합의 표현 probing, 결합 구조 세 가지, 데이터·카메라 수·재구성 품질의 영향을 비교한다. 모든 VLA에 대한 보편 결론이나 동일 상태 오류 개입 실험을 뜻하지 않는다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Probe 용량 차이·architecture별 파라미터/학습량·재구성 품질의 측정 단위·task/data split·real-robot 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

단순 geometry 오차–성공률 상관도 이미 분석됐음을 확인할 직접 NEXT다. 신규 후보는 동일 상태 개입·단순 대안 이후의 차이를 보여야 한다.

### Dependency and Evolution

VGGT·GR00T·SpatialVLA·geometry alignment → 통제된 geometry 결합 비교 → 작업 조건별 오류 개입. 개념 계보이며 citation graph가 아니다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 checkpoint·RGB·K를 고정하고 geometry 입력 오차만 바꿔 원래 오차–성공 관계와 비교한다. Action/policy 변경은 별도 비교다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

관측 상관을 넘어 같은 state·policy의 geometry 오류를 개입해도 작업별 차이가 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
