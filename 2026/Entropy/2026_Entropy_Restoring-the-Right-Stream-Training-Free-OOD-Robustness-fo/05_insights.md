# Restoring the Right Stream: Training-Free OOD Robustness for Vision–Language–Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Gated Per-Stream Manifold Restoration으로 visual/state 입력을 따로 복원한다.

OpenVLA-OFT와 LIBERO-Plus 평가를 보고한다.

근거: [공식 paper/abstract](https://www.mdpi.com/1099-4300/28/9/975) · [저자 project/code](https://www.mdpi.com/1099-4300/28/9/975). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 native state interface, gate oracle leakage, code·trial manifest 공개은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Top-tier 선정 논문은 아니지만 D1의 stream diagnosis·correction 주장과 직접 겹쳐 REFERENCE로 등록한다.

### Dependency and Evolution

OpenVLA-OFT·LIBERO-Plus → G-PSMR의 frozen-policy input restoration; ReViP·Self-Adaptive의 학습 기반 보정과 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

물리적 이동과 state reporting offset을 나누어 보정의 이득·손해를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

상태 이상이 실제 이동일 때 normalization이 필요한 변화까지 지우는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
