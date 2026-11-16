# RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

VLA/RL/simulator 공통 interface와 rendering·inference·training 자원 할당 구조를 제공한다.

RSS abstract는 LIBERO, ManiSkill, RoboTwin simulation에서 training efficiency와 policy 성능을 비교한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p089.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Model별 action interface, GPU utilization 산정, asynchronous policy lag은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend / system. 여러 VLA·RL 알고리즘·시뮬레이터를 비교할 공통 interface와 resource allocation을 제공한다. SimpleVLA-RL 및 ConRFT 실험을 설계할 때 algorithm 효과와 시스템 throughput을 분리하는 데 유용하다. 공식 RSS title은 RLinf-VLA다.

### Dependency and Evolution

OFT/π0 + SimpleVLA-RL → RLinf-VLA; USER는 real-world system 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 policy/algorithm/task에서 scheduling만 바꾸고 samples/sec·wall-clock time·고정 step 성공률을 보고한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

GPU·environment step budget을 고정하면 resource scheduling의 이득이 algorithm 성능 차이와 분리되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
