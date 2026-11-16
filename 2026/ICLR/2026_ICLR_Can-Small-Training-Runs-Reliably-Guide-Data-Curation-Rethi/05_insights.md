# Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Data-dependent tuning에 따라 순위가 바뀌는 문제를 분석하고 작은 learning rate를 쓰는 평가 보정을 제안한다.

LLM pretraining recipe와 random-feature model 이론을 다룬다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 이론 적용 범위, loss와 task success 차이, tuning 총비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

GAP-N1에서 관측 정보 효과와 optimizer 설정 효과를 분리하는 필수 방법론 참조다.

### Dependency and Evolution

Proxy ranking → tuning 조건 통제 → VLA 전이 진단.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 정보의 proxy에서 LR 민감도를 먼저 확인하고 이후 cue 조건을 바꾼다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Learning-rate 보정 뒤에도 history cue 유무에 따른 subset 순위 차이가 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
