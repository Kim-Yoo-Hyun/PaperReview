# Active 6D pose estimation for textureless objects using multi-view RGB frames

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Translation을 먼저 추정하고 canonical-scale template으로 orientation을 추정한 뒤 pose uncertainty를 줄일 다음 view를 선택한다.

ROBI·TOD·T-ROBI에서 같은 view의 추정 성능과 적은 view로 얻는 정확도를 비교한다. VLA 행동 효과 평가로 확장하지 않는다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649251411922) · [저자 project/code](https://trailab.github.io/ActiveODPE/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 CAD·calibration 요구·transparent dataset 조건·실제 이동 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Pose 정확도 중심 NBV와 task 성공 중심 관측 중단을 비교할 journal 기준이다.

### Dependency and Evolution

FoundationPose의 pose 기준과 ActiveODPE의 RGB NBV를 정보 조건별로 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 추정 후보와 카메라 budget에서 pose uncertainty 규칙과 task tolerance 규칙을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 view 비용에서 pose 정확도를 충분히 높이기 전에도 조작을 성공할 수 있는 조건은 무엇인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
