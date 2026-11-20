# Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

여러 sensor를 처리하는 encoder와 학습 중 modality dropout으로 결손에 대비한다.

Locomotion과 manipulation, simulation과 실로봇의 sensor failure를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/skand25a.html) · [저자 project/code](https://pvskand.github.io/projects/RME). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 결손 종류·지속 시간·학습 노출, proprio와 image mask 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

새 multimodal VLA adaptation 전에 대조할 단순 sensor-dropout 기준이다.

### Dependency and Evolution

Multimodal encoder → masked training → FuSe 및 sensor-aware VLA.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 센서와 dropout 예산에서 masked training과 추가 adaptive fusion을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

결손 대비 학습으로 제거되지 않는 action-relevant sensing 이득이 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
