# InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시뮬레이션에서 정렬과 삽입을 나누어 보상하고 손끝 힘을 이용해 접촉 뒤의 수정 동작을 학습한다.

저자는 실제 여러 형상에서 최소 공칭 간극 0.02 mm를 다뤘다. ManipulationNet의 20/20은 사람 개입을 허용한 프로토콜이며 다른 실험의 자율 지표와 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.24511) · [저자 project/code](https://mzhsoul.github.io/InsertAnything/) · [공식 code](https://github.com/mzhsoul/InsertAnything). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 형상별 시행 수, 목표 자세의 취득 방식과 사람 개입 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

위치 오차가 있는 삽입에서 강성 학습에 앞서 대조할 힘 기반 동작 정책이다.

### Dependency and Evolution

Factory와 IndustReal의 시뮬레이션 기반 조립, FORGE의 힘 탐색을 ContactBench의 정렬 오차와 연결한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일한 초기 오차에서 고정 하강과 힘 조건부 동작을 비교하며 최대 힘과 손을 뗀 뒤 안착을 함께 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 위치 오차와 하중 한도에서 손끝 힘을 이용한 동작 수정만으로 고정 경로의 실패가 줄어드는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
