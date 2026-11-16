# EvoVLA: Self-evolving Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Counterfactual hard negative 기반 stage reward, relative pose 탐색, 선택적 장기 memory를 결합한다.

Discoverse-L 장기 조작과 실제 로봇의 성공·stage hallucination을 평가한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14) · [저자 project/code](https://aigeeksgroup.github.io/EvoVLA/) · [공식 code](https://github.com/AIGeeksGroup/EvoVLA). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 pose·stage annotation의 특권 정보, hard-negative 생성 비용, 세 모듈별 기여은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA+RL 보상 개선에서 이미 다룬 near-miss 구분과 실제 물리 완료의 선행이다.

### Dependency and Evolution

ConRFT·OpenVLA-OFT·RoboCLIP과 reward validity 및 장기 credit assignment를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 rollout에서 기본 보상·near-miss 보정·새 방법을 비교하고 독립 물리 완료 지표를 둔다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

성공/near-miss를 구별하는 보상만으로 새 실패 재사용 방법의 이득이 설명되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
