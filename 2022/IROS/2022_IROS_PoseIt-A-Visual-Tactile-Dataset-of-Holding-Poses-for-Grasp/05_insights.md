# PoseIt: A Visual-Tactile Dataset of Holding Poses for Grasp Stability Analysis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

집기·자세 이동·흔들기 전 과정의 시각과 촉각 관측을 수집하고 다중 모달 시계열 분류기를 비교한다.

저자 자료는 26개 물체의 실물 기록을 제공하며 초록은 미관측 물체와 자세에 대한 예측을 평가한다. 자세 이동 중 실패와 마지막 흔들기 결과는 별개다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/9981562/) · [저자 project/code](https://publish.illinois.edu/robotouch/poseit-a-visual-tactile-dataset-of-holding-poses-for-grasp-stability-analysis/) · [공식 code](https://github.com/Robo-Touch/PoseIt). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 물체 분할, 파지 명령이 변경된 시점과 단계별 실패 라벨의 의미은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

들기 이후 실패가 발생한 단계를 공개 기록으로 재확인할 때 쓰는 데이터 기준이다.

### Dependency and Evolution

정적 grasp 판정에서 작업 자세를 바꾼 후의 안정성 평가로 연결한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

물체를 분리한 검증에서 이동 중 실패와 흔들기 실패를 나누고 같은 힘 예산의 단순 대조를 포함한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

들기에서 안정했던 관측만 골랐을 때 이동 자세가 이후 실패를 추가로 예측하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
