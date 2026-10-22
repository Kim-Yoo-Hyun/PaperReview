# EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Stereo fixation 기반 표현과 gaze/행동 제어를 연결한다.

Simulation 및 실제 bimanual manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.03710) · [저자 project/code](https://eyerobot2.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 물리/가상 gaze 경계, stereo calibration, RL/BC supervision, robot 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C1의 시선 조절과 action-relevant 관측에 대한 직접 REFERENCE다.

### Dependency and Evolution

Active perception·3D policy → EyeRobot 2.0.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Fixed gaze와 adaptive gaze를 같은 실행기·시야 예산으로 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 시각 정보·행동 비용에서 gaze 선택이 정밀도를 높이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
