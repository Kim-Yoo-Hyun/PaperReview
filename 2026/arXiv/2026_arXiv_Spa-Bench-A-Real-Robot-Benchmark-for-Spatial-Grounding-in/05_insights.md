# Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

SO-101의 공간 지시 과제에서 익숙한 객체·개념·행동을 유지한 배치 변화와 직접 지시·표현·무행동 진단을 비교한다.

저자는 여섯 tabletop task와 여러 VLA의 실제 rollout을 보고한다. 전체 protocol을 수행한 모델과 부분 baseline이 다르므로 분모를 섞지 않는다. 공개 project의 model/data 링크는 확인했으나 독립 실행 code URL은 확인하지 못했다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.12696) · [저자 project/code](https://justintiensmith.github.io/Spa-Bench/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 ID/OOD support, 모델별 완료 범위와 trial 분모, 직접 지시의 정보량, 최종 수량·무행동 채점, 공개 data/코드의 실제 가용 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

집합·수량 후보의 가장 직접적인 counting/직접 지시 비교 선행이다. 알려진 공간 grounding 실패를 새 공백으로 과장하지 않도록 NEXT에 등록하며 preprint 경계를 유지한다.

### Dependency and Evolution

OpenVLA·π0 계열의 일반 정책을 VLABench·RoboMME와 다른 공간 grounding 축에서 비교할 자료다. 모델별 세부 설정은 본문 확인 대상이다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

현재 SET의 D/R 설계와 Counting 평가 정의를 먼저 맞춘다. SO-101 결과를 VLABench simulator의 결과로 대체하지 않으며 실제 실행은 별도 조건을 따른다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

기존 matched 지시 진단 이후, 익숙한 범주의 EXACTLY-k를 단순 k회 반복으로 바꾸는 비교가 어떤 추가 판단을 제공하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
