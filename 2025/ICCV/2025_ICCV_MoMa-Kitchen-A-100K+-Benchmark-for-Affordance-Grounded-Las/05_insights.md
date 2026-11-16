# MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

조작 가능 최종 base 위치를 라벨링한 주방 데이터와 affordance baseline을 제공한다.

여러 팔·platform 높이를 포함한 simulated kitchen affordance 평가를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html) · [저자 project/code](https://momakitchen.github.io/) · [공식 code](https://github.com/MoMaKitchen/MoMaKitchen). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 형상별 split, oracle grasp label 생성, navigability와 reachability 정의, 실환경 전이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA+RL을 manipulation과 navigation에 통합할 때 성공 조건을 구체화하는 benchmark다.

### Dependency and Evolution

Mobile manipulation·RoboCasa·BEHAVIOR의 목표 도달과 조작 가능성 차이를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 장면·목표에서 proximity와 affordance 종료를 비교하고 실제 grasp 시도 성공을 따로 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

거리 기반 항법 reward보다 manipulation feasibility reward가 후속 grasp 성공을 높이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
