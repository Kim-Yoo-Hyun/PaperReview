# ContextFlow: In-Context Flow Matching for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시연의 시각·proprioception·행동을 압축하는 perceiver와 in-context 조건부 flow matching을 결합한다.

LIBERO의 미관측 구성과 실제 단일팔·양팔 조작을 평가한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16) · [저자 project/code](https://dingjiansw101.github.io/contextflow-page/) · [공식 code](https://github.com/dingjiansw101/ContextFlow). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 context 길이·선정 비용, 미관측 task 정의, bimanual action 정규화은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

적응을 RL update 없이 해결하는 비교 대안으로 등록한다.

### Dependency and Evolution

ACT·Diffusion Policy·in-context imitation의 적응 interface를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 정책 규모와 새 시연으로 context-only·gradient adaptation을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 신규 시연 예산에서 context 적응이 RL fine-tuning과 어느 조건에서 갈리는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
