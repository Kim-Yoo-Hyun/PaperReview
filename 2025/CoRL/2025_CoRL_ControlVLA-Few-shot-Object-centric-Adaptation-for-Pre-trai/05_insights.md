# ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Zero-initialized projection을 가진 ControlNet 형태로 object-centric 조건을 주입한다.

실제 조작과 새 객체·배경 및 long-horizon 확장을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/li25c.html) · [저자 project/code](https://controlvla.github.io/) · [공식 code](https://github.com/ControlVLA/ControlVLA). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 객체 mask 감독 비용, base model 학습 데이터, 표준·장기 task 구분은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

RL이 반드시 필요한지를 판단할 저데이터 SFT·표현 적응 비교다.

### Dependency and Evolution

Generalist VLA·ControlNet식 조건 주입과 object-centric manipulation을 연결한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

기본 SFT와 object-centric SFT를 먼저 맞춘 뒤 동일한 online RL budget을 적용한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 시연 수에서 RL 이득이 객체 조건화만으로 재현되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
