# DEAS: DEtached value learning with Action Sequence for Scalable Offline RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

행동 sequence 기반 가치 학습에 detached value learning을 적용하여 데이터 안의 고수익 행동으로 추정을 유도한다.

OGBench, RoboCasa Kitchen과 실세계 조작의 VLA 확장을 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html) · [저자 project/code](https://changyeon.site/deas/) · [공식 code](https://github.com/csmile-1006/DEAS-Isaac-GR00T). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 value target gradient 경계, OOD action 처리, 실로봇 데이터·환경 예산은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Chunk-aware actor-critic과 공유 표현 연구에서 반드시 넘어야 하는 직접 offline RL 선행이다.

### Dependency and Evolution

IQL·Diffusion Policy·OpenVLA-OFT와 sequence 단위 value의 차이를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 chunk·데이터에서 single-step critic, sequence critic, detached sequence critic을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

개선이 chunk 길이에서 오는가, detached value target에서 오는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
