# SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

같은 batch의 성공 궤적을 기준으로 world-model latent에서 실패의 진행 보상을 만든다.

LIBERO와 LIBERO-Plus에서 학습 효율·견고성을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 성공 없는 batch 처리, world-model 사전학습 비용, 진행 측정 오류, reward scale은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

HINDSIGHT의 실패 재사용이 이미 존재하는 self-reference reward shaping과 다른지 검토할 직접 선행이다.

### Dependency and Evolution

SimpleVLA-RL·LfH·Dopamine-Reward와 목표 relabeling 및 진행 보상 차이를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 실패 pool·성공 참조·원 목표 평가에서 relabeling, self-reference shaping, 둘의 결합을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

실패 재라벨 선택의 이득이 같은 성공 참조를 이용한 dense reward로 설명되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
