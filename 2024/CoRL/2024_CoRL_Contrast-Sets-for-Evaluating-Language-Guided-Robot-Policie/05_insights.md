# Contrast Sets for Evaluating Language-Guided Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

기존 test instance에 작고 구체적인 변화를 주는 contrast set으로 성능과 평가 노력의 관계를 분석한다.

시뮬레이션 조작과 물리 로봇의 vision-and-language navigation을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/anwar25a.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 대조쌍 난이도·유효성 검수, 평가자 노력의 정의, 물리 reset 재현성은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA+RL 개선이 언어 민감도까지 바꾸는지 적은 실행으로 진단할 평가 설계의 선행이다.

### Dependency and Evolution

RT-2·OpenVLA의 언어 행동 연결과 LIBERO의 task variation 평가를 대조한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 scene의 지시 대조쌍을 구성하고 학습 전후 paired success와 instruction-consistency를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

평균 성공이 오른 RL 정책이 최소 언어 대조쌍에서도 목표 변경에 맞춰 행동하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
