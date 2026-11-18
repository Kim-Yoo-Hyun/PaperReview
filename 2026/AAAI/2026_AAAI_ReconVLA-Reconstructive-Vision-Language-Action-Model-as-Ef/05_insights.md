# ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시각 출력으로 target gaze 영역을 복원하는 diffusion transformer를 학습해 implicit grounding을 유도한다.

공개 로봇 데이터 기반 사전학습과 simulation·실세계 조작 평가를 보고한다.

근거: [공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/38921). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Gaze-region label 생성·data overlap·loss weighting·추론 경로은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

TASK-GEOMETRY의 이득이 단순 target attention/영역 supervision 때문인지 비교할 선행이다.

### Dependency and Evolution

OpenVLA/SpatialVLA의 시각 표현과 ReconVLA의 2D target reconstruction을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

ROI·학습 데이터·추가 parameter를 맞추고 2D/3D auxiliary target을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Task-local geometry supervision의 효과가 같은 ROI의 2D reconstruction만으로 설명되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
