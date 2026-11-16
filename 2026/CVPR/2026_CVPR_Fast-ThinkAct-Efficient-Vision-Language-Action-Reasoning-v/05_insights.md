# Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Teacher의 언어·시각 계획을 preference-guided distillation으로 압축하여 verbalizable latent reasoning을 학습한다.

Embodied manipulation·reasoning benchmark의 latency와 장기 계획·적응·복구를 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.html) · [저자 project/code](https://jasper0314-huang.github.io/fast-thinkact/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 teacher 감독 비용, action model 별도 학습 여부, end-to-end latency은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

RL reasoning의 이득을 긴 텍스트 출력 없이 행동에 전달하는 대안으로 비교한다.

### Dependency and Evolution

RT-2·OpenVLA와 ThinkAct의 reasoning/action 경계를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 teacher 데이터로 reasoning 제거·latent reasoning·명시 reasoning을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 제어 latency에서 latent reasoning이 단순 action distillation보다 복구를 개선하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
