# What Matters in Learning from Large-Scale Datasets for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

통제 가능한 데이터 생성으로 카메라·물체·배치 다양성과 retrieval 정렬을 비교한다.

시뮬레이션 구성 실험과 DROID를 이용한 실로봇 학습을 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 camera와 task 분할, retrieval의 target 접근, 동일 학습 예산은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

단순 시각·공간 정렬로 설명되는 이득을 제거하기 위한 DataMIL·GAP-N1의 비교 기준이다.

### Dependency and Evolution

robomimic/DROID → 구성 다양성 → DataMIL의 성능 기반 선택.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 camera/scene 분포의 random·정렬 retrieval·policy-aware subset으로 target을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 target 관측과 시연 수에서 spatial alignment 이후에도 selector 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
