# Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시연에서 interaction frame을 복원해 전역 시각 정책과 국소 hybrid force-position 제어를 구성한다.

실제 contact-rich 조작과 새로운 형상·물성 객체를 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p128.html) · [저자 project/code](https://force-policy.github.io/) · [공식 code](https://github.com/force-policy/ForcePolicy). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 frame label 생성과 수동 조정, 접촉 전환 조건, 정책·controller 주기은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Unified VLA의 접촉 기여가 분리된 고주파 힘 제어보다 나은지 판단할 비교 기준이다.

### Dependency and Evolution

Hybrid force-position control·Diffusion Policy와 ForceVLA2의 action interface를 대조한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

관측과 controller를 맞춘 후 접촉 검출, frame 추정, force regulation의 실패를 각각 계측한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 센서·제어주기에서 통합 정책이 interaction-frame 분해보다 견고한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
