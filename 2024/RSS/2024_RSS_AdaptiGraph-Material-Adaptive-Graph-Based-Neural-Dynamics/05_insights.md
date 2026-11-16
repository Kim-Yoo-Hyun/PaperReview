# AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

물성 조건부 particle graph dynamics를 학습하고 online 상호작용으로 물성 변수를 조정한다.

로프·입자·상자·천 등 real-world 물체의 예측과 조작을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss20/p010.html) · [저자 project/code](https://robopil.github.io/adaptigraph/) · [공식 code](https://github.com/Boey-li/AdaptiGraph). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 particle extraction, 물성 식별 가능성, probe 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

물성 adaptation을 신규 방법으로 반복하지 않기 위한 GAP-DE의 모델 기반 대안이다.

### Dependency and Evolution

Graph dynamics → AdaptiGraph → task-oriented identification.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

물성 적응 유무와 단순 feedback baseline을 같은 조작 목표에서 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Prediction error 감소가 동일 probe 예산의 task 성공 개선으로 이어지는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
