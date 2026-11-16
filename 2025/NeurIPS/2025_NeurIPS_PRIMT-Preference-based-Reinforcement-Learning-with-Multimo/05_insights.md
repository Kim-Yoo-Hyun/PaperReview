# PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

VLM·LLM 피드백 결합, foresight trajectory 생성과 hindsight augmentation·causal auxiliary loss를 사용한다.

Locomotion과 manipulation benchmark에서 foundation-model 및 scripted 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html) · [저자 project/code](https://primt25.github.io/) · [공식 code](https://github.com/primt25/PRIMT). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 합성 trajectory 유효성, reward 누출, foundation model 호출 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Hindsight 재사용과 foundation reward 결합이 이미 연구되었음을 보여 주는 비교 선행이다.

### Dependency and Evolution

PEBBLE·RoboCLIP·HER와 합성 선호 및 재라벨의 역할을 구분해 읽는다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 feedback budget으로 원 trajectory만, 단순 증강, causal 증강을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

추가 생성 데이터량을 맞춰도 hindsight causal augmentation의 credit assignment 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
