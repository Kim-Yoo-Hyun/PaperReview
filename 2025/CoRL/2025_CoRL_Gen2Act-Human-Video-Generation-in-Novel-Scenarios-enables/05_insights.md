# Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

고정된 생성 모델의 인간 영상을 조건으로 공통 robot policy를 실행한다.

새 물체 종류·동작을 포함한 실환경 manipulation을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/bharadhwaj25a.html) · [저자 project/code](https://homangab.github.io/gen2act/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 robot-data holdout, video 사전학습 중복, motion conditioning과 실행 latency은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA의 video prior가 action supervision을 어떻게 보완하는지 비교할 직접 선행이다.

### Dependency and Evolution

RT-2·video prediction → Gen2Act; VideoVLA와 video-to-action 경계 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 정책에서 생성 video·정지 keyframe·time-shuffled video를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

생성 영상의 semantic cue를 통제해도 motion 정보가 새로운 행동의 성공을 높이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
