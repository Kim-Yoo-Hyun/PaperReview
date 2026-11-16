# LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

구조화된 시각 latent에서 dynamics·policy·forecasting을 공동 학습하고 이질적 데이터를 통합한다.

Simulation과 실제 contact-rich·dexterous·long-horizon 조작을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p210.html) · [저자 project/code](https://github.com/jiangranlv/LDA-1B). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 저품질 데이터 정의, 데이터 역할별 objective, action/vision rate, 학습 데이터 중복은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

단일 모델의 행동·세계 예측 공유를 새 기여로 제안하기 전에 비교할 핵심 구조다.

### Dependency and Evolution

Unified World Model·π0 계열을 대규모 이질적 데이터 공동 학습과 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 데이터·backbone·compute에서 action-only와 dynamics 공동 학습 후 동일 RL budget으로 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

공유 dynamics 학습이 단순 데이터 증가보다 RL 적응에 유리한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
