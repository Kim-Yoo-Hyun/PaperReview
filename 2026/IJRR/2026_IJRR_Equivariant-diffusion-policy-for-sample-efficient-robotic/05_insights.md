# Equivariant diffusion policy for sample-efficient robotic manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

조작의 기하학적 대칭성을 denoising에 반영해 데이터 효율을 높인다.

MimicGen simulation과 실로봇 manipulation에서 소량 시연 학습을 비교한다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649261424445) · [저자 project/code](https://equidiff.github.io/) · [공식 code](https://github.com/pointW/equidiff). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 적용 가능한 symmetry, 절대/상대 action, RGB/point-cloud 정보량, checkpoint 선택은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

일반화 이득이 더 큰 VLA보다 대칭성 같은 inductive bias로 설명되는지 대조할 기준이다.

### Dependency and Evolution

Diffusion Policy → Equivariant Diffusion Policy(CoRL 2024) → IJRR 확장; DP3와 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 입력·시연·action 좌표계에서 augmentation과 equivariant denoising을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

관측/제어 좌표계를 맞춘 후에도 equivariance가 단순 augmentation보다 데이터 효율적인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
