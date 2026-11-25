# Tactile-Guided In-Contact Robotic Insertion via Physically Consistent Force-Array Representation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

접촉 후 시연에서 힘 분포 표현을 관측하는 diffusion policy를 학습하고 합력·모멘트만 쓰는 경우와 대조한다.

IEEE 초록은 학습 분포 안에서 합력·모멘트만 쓴 변형이 약간 우세했고, 새 2·3핀과 USB·HDMI 커넥터 전이에서는 분포 표현이 유리했다고 보고한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11692602/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 센서 교정, 커넥터별 시행 수, 실물 분포 신호를 재현할 수 있는 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

순합력과 국소 접촉 정보가 다른 판단을 주는 현재 삽입 연구의 실물 비교 논문이다.

### Dependency and Evolution

ContactBench의 하중 계측과 비교할 수 있다. 센서 측정값과 시뮬레이터 접촉점 배열에는 서로 다른 관측 권한이 있다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

커넥터별로 하중을 맞춘 뒤 합력·분포 입력의 성공과 최대 하중을 분리해 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 합력에서도 접촉 위치가 다른 사례에서 분포 표현이 정렬 수정에 추가 정보를 주는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
