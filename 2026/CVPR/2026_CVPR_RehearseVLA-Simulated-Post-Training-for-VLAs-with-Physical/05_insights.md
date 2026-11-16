# RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

물리 일관성을 지향한 world simulator와 보상·종료를 판단하는 VLM reflector를 구성한다.

소수 시연 조건의 복잡한 로봇 조작 개선을 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html) · [저자 project/code](https://github.com/iSEE-Laboratory/RehearseVLA). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 실제/가상 rollout 분모, 물리 일관성 검증, reflector의 감독 비용, 종료 오탐은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLAW 등과 함께 imagined rollout으로 실제 interaction을 대체하는 직접 비교 기준이다.

### Dependency and Evolution

World-model RL·VLAW·실패 recovery를 simulator 편향과 종료 판단 관점에서 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 시연으로 world-model RL·추가 모방·종료 모듈만 적용한 정책을 각각 실제 환경에서 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

개선이 virtual exploration에서 오는가, 더 나은 종료 판정에서 오는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
