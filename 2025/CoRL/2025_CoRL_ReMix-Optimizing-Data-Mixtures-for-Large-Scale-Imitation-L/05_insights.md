# ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

DRO 기반 domain 가중치 학습에 action 정규화·이산화와 early stopping을 적용한다.

Bridge·Open X-Embodiment 기반 데이터 혼합과 후속 정책 성능을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/hejna25a.html) · [저자 project/code](https://github.com/jhejna/remix). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 domain 정의, proxy/target 접근, normalization, selection 계산 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

DataMIL의 subset 선택과 domain-level mixture 최적화를 구분하는 필수 비교군이다.

### Dependency and Evolution

OXE/RT-X → ReMix → DataMIL; 동일한 selection objective인지는 별도 확인.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 데이터·학습 budget에서 uniform·ReMix·target subset을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

target-aware subset 이득이 domain mixture와 action scale 보정 이후에도 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
