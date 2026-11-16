# DataMIL: Selecting Data for Robot Imitation Learning with Datamodels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Datamodel로 policy 성능에 기여하는 데이터를 선택하며 task-specific surrogate로 선택 중 rollout 비용을 줄인다.

OXE 선택을 포함한 simulation 및 실로봇 manipulation 평가를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) · [저자 project/code](https://github.com/UT-Austin-RobIn/datamil). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 surrogate 정의, target 데이터 누설, policy family 및 selector 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

현재 proxy→target 데이터 전이 질문에서 반드시 대조할 performance-aware 선택 방법이다.

### Dependency and Evolution

DROID/OXE → DataMIL → proxy와 target의 정보 조건 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 target·budget에서 random, similarity, DataMIL 계열 선택을 먼저 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Proxy의 숨은 관측 차이가 target surrogate를 맞춘 뒤에도 선택 순위와 성공을 바꾸는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
