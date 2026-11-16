# PROSPECT: Unified Streaming Vision-Language Navigation via Semantic–Spatial Fusion and Latent Predictive Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

CUT3R 공간 표현과 SigLIP 의미 표현을 융합하고 학습 중 미래 2D·3D latent prediction을 보조 목표로 사용한다.

VLN-CE와 실제 항법을 평가한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11673313/) · [저자 project/code](https://github.com/Debactor/PROSPECT). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 미래 target 접근, inference 비용 산정, map/history memory 조건은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

정책 내부 표현·미래 예측이 항법에 주는 효과를 RL 기여와 분리할 기준이다.

### Dependency and Evolution

DUSt3R/CUT3R·VLN foundation과 predictive representation의 action 연결을 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 navigation backbone에서 fusion·prediction·RL을 구분한 ablation을 수행한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

RL 이후에도 미래 표현 보조 학습이 관측 이력의 aliasing을 줄이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
