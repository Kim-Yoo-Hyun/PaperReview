# Searching in Space and Time: Unified Memory-Action Loops for Open-World Object Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

장기 기억과 작업 기억을 이용해 과거 기록 조회와 물리적 탐색 중 다음 행동을 선택한다.

저자는 STARBench와 Tiago 실기에서 비교했다. 프로젝트의 360개 과제는 3개 아파트와 3개 과제군을 포함한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11696368/) · [저자 project/code](https://amrl.cs.utexas.edu/STAR/) · [공식 code](https://github.com/ut-amrl/STARBench). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 실물과 시뮬레이션의 과제 수, 기억 관측 주체, 대상 이동 빈도은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

기억 조회와 로봇의 실제 이동을 구별하는 공개 탐색 프로토콜로 참조한다.

### Dependency and Evolution

PARTNR의 협업 기록과 달리 시간·속성으로 지칭한 대상을 찾는 요청을 통제한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 초기 위치와 후보 지도를 사용하고 이동·조회 비용과 최초 회수 성공을 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

이전 위치가 달라진 조건에서 기억 조회가 가까운 후보부터 방문하는 방법의 이동 비용을 줄이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
