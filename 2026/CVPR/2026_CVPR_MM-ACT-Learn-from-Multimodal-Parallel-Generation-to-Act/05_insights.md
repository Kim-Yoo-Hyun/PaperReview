# MM-ACT: Learn from Multimodal Parallel Generation to Act

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

텍스트·영상·행동을 공유 token 공간과 context로 학습하고 modality별 병렬 decoding을 사용한다.

LIBERO, 실제 Franka, RoboTwin2.0의 in-domain·out-of-domain 조작을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html) · [저자 project/code](https://github.com/HHYHRHY/MM-ACT). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 modality별 loss·compute 균형, 생성 token이 action에 주는 영향, RL 미검증 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

하나의 VLA 내부 통합을 설계할 architecture 선행이며 RL objective 통합 효과로 해석하지 않는다.

### Dependency and Evolution

RT-2·π0·GR-1의 shared representation 및 prediction/action 결합과 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 데이터에서 action-only와 multimodal pretraining을 비교한 뒤 동일 RL update를 적용한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

공유 생성 학습의 이득이 RL 후학습 후에도 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
