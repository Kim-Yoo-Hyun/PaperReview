# HALO : Human Preference Aligned Offline Reward Learning for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Expert 행동 주변 후보의 선호 순위를 학습해 시각 reward를 구성한다.

실제 Clearpath Husky 항법에서 성공·경로 특성을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/seneviratne25a.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 선호 query 생성·annotation 비용, 후보 sampling 분포, offline/online 데이터 경계은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

항법 VLA-RL에 인간 선호 보상을 붙일 때 참고할 구체적 reward-learning 대안이다.

### Dependency and Evolution

Preference-based RL·MPC와 언어 정책의 과제 성공 외 평가를 연결한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 환경에서 task success·path length·인간 경로 유사도를 분리해 선호 reward의 trade-off를 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

선호 정렬은 통행 성공을 높이는가, 인간 경로 모방만 강화하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
