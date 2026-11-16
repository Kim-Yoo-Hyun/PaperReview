# CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

VLM 기반 counterfactual 라벨과 대응 행동 자료로 기존 robot dataset의 지시·행동 다양성을 늘려 언어 추종을 학습한다.

v2 abstract는 실내외 3개 navigation 환경과 distractor가 있는 manipulation의 instruction following을 평가한다고 보고한다. 정확한 trial·split·수치는 본문 확인 필요다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2508.13446) · [저자 project/code](https://cast-vla.github.io/) · [공식 code](https://github.com/catglossop/CAST). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 합성 행동의 물리적 유효성, 원 데이터/평가 중복, language와 action 증강 기여 분리, 공개 모델/자료의 논문 version 대응은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

목표 의미를 바꾸는 학습 자료의 직접 대조. 사실인 실패 라벨 선택과 실행되지 않은 counterfactual augmentation의 차이를 명확히 하는 데 필요하다.

### Dependency and Evolution

언어 조건 VLA·데이터 증강 → CAST → hindsight label 선택과 의미 grounding의 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 관측별 원 지시·단순 paraphrase·counterfactual 지시/행동을 구분하고 계산량을 맞춰 새 명령 성공과 distractor 오선택을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 원 자료·VLM 호출·합성 행동 수를 맞췄을 때 개선은 지시의 의미적 다양성인가, 행동 coverage나 추가 학습량 때문인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
