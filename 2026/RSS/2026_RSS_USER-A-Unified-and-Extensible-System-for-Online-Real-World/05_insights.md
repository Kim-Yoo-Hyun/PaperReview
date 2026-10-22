# USER: A Unified and Extensible System for Online Real-World Policy Learning in Embodied AI

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Robot/GPU 추상화, adaptive communication 및 persistent buffer를 갖춘 asynchronous learning system을 제안한다.

RSS abstract는 simulation과 실제 multi-robot·heterogeneous manipulator·edge-cloud·장기 비동기 학습 사례를 명시한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p037.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Weight version tagging, replay consistency, crash recovery와 실제 robot 시간 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current system. 실제 robot online RL에서 edge/cloud·buffer·weight synchronization을 구현할 때 SERL/HIL-SERL의 시스템 확장으로 읽는다. Simulator 중심 RLux-VLA와 역할이 다르다.

### Dependency and Evolution

SERL/HIL-SERL → USER; RLux-VLA는 simulator 기반 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 policy와 robot task에서 sync/async 학습을 비교하고 policy lag·중단 복구·wall-clock learning·success를 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

통신 지연과 policy lag가 증가할 때 asynchronous throughput 이득이 task 안정성을 유지하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
