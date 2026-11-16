# MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

다양한 실내 환경·상호작용 객체·grasp 자산과 통합 benchmark를 제공한다.

조작·항법을 포함한 8개 benchmark task와 sim-to-real 상관을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p091.html) · [저자 project/code](https://github.com/allenai/molmospaces). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 asset license, 실제 지원 simulator별 기능, 장면 split, 정책별 co-training 여부은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

현재 후보의 한 benchmark 의존을 줄일 추가 환경·데이터 자원이다.

### Dependency and Evolution

BEHAVIOR·RoboCasa·ManiSkill과 장면 다양성 및 평가 task 정의를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

학습 장면을 고정하고 세 변이를 독립적으로 바꾼 held-out 평가를 설계한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 VLA의 RL 개선이 초기 자세·가림·지시 표현 변화에서도 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
