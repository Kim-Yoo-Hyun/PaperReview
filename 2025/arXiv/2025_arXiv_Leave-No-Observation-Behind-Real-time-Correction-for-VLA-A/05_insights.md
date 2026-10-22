# Leave No Observation Behind: Real-time Correction for VLA Action Chunks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

새 관측과 base action 등에 조건화한 residual head로 chunk action을 수정한다.

Kinetix와 LIBERO Spatial 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2509.23224) · [저자 project/code](https://github.com/k1000dai/a2c2-libero). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 residual target, 추가 feature, checkpoint 공개, 관측 latency은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E2의 fresh feedback correction·delay/horizon 분리가 이미 존재함을 보여준다.

### Dependency and Evolution

RTC → learned residual correction → E2.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Base 고정 후 residual 유무와 delay/horizon을 교차 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 관측·학습 예산에서 다른 feedback 분배의 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
