# PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

초기·현재·목표 관측으로 progress를 추정하고 online refinement한다.

Human video와 실제 로봇 offline RL 평가를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Ayalew_PROGRESSOR_A_Perceptually_Guided_Reward_Estimator_with_Self-Supervised_Online_Refinement_ICCV_2025_paper.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 goal image 정보, refinement 데이터, train/test overlap, reward scale은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C4에서 progress reward 품질과 정책 효과를 분리할 비교군이다.

### Dependency and Evolution

Visual reward learning → PROGRESSOR → Robometer.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 rollout에서 progress score와 독립 success label의 불일치를 검수한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

보상 score 향상이 독립 task outcome도 개선하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
