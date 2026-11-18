# Universal Pose Pretraining for Generalizable Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Camera-centric pose token으로 공간·trajectory 사전학습을 한 뒤 로봇 action space에 적응한다.

공식 초록은 RoboTwin 2.0·LIBERO 및 실세계 물체 일반화 실험을 명시한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p145.html) · [저자 project/code](https://hetolin.github.io/PoseVLA/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 3D 데이터 규모·pose supervision·camera convention·test object 중복은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Pose 표현을 VLA에 넣는 것만으로 새 기여를 주장하지 않도록 하는 직접 선행이다.

### Dependency and Evolution

SpatialVLA의 spatial embedding과 Pose-VLA의 pose pretraining을 정보/학습 target별로 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 robot demonstrations에서 pose pretraining 유무와 성공 head 공유 여부를 분리한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Pose token이 정확도 외에 실제 필요한 관측 여부를 예측하는 데 도움이 되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
