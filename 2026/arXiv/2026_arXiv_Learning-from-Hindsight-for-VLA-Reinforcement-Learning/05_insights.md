# Learning from Hindsight for VLA Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

VLM으로 실패에서 달성한 행동을 보조 언어 목표로 붙이고 원 과제와 함께 정책을 학습한다.

v2 abstract는 LIBERO-PRO의 분포 이동 조작과 실제 Franka 학습을 보고한다. 샘플 효율 개선은 해당 비교 조건의 저자 주장이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.09042) · [저자 project/code](https://iamxjy.github.io/lfh-website/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 v2의 importance correction·label filtering·모방 대조와 우리 selector의 정확한 차이, VLM 감독 비용과 rollout 분모, 원 지시 평가 독립성은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

실패 재사용 자체가 새 기여가 아님을 보여 주는 HINDSIGHT의 가장 가까운 선행. 참인 보조 목표들 사이의 원 과제 전이를 연구하려면 먼저 비교해야 한다.

### Dependency and Evolution

HER의 사후 목표 재라벨 → 언어 기반 relabeling → OpenVLA/OFT·GRPO 후학습의 개념 연결. 직접 citation edge로 등록하지 않는다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

먼저 자연적으로 참인 관련/비관련 목표가 같은 실패에서 발생하는지 확인한다. 이후 고정 pool에서 균등·객체 일치·원 목표만 학습을 대조한다. 현재 주제의 P0/P1/P2 계약은 별도이며 이 노트는 실험 결과가 아니다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 실패 pool·원 보상·후보 목표·계산량에서 원 목표 객체를 우선하는 선택이 균등 선택보다 원 지시 성공을 높이며, 동일 라벨 모방으로 설명되지 않는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
