# Measuring the Stability Assumption Behind Action Chunking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Open-loop/closed-loop branch의 finite-horizon divergence를 비교한다.

GR00T manipulation task에서 chunk 안정성 가정의 차이를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.01626) · [저자 project/code](https://aryangoyal7.github.io/publication/2026-stability-action-chunking). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 norm 단위, perturbation 크기, branch 동치, 전역 안정성과의 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E2 진단에서도 state-dependent 안정성을 새 발견으로 주장하지 않도록 하는 REFERENCE다.

### Dependency and Evolution

Action chunking → finite-horizon stability diagnosis.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Held-out perturbation·horizon에서 divergence와 success를 별도 검증한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

추정 slope가 별도 perturbation의 task outcome을 예측하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
