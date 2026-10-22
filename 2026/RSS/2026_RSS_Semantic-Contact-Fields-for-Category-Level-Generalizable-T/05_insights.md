# Semantic Contact Fields for Category-Level Generalizable Tool Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

3D semantic-contact field를 sim pretraining과 real pseudo-label 조정으로 학습한다.

서로 다른 도구를 사용하는 contact-rich 작업 평가를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p004.html) · [저자 project/code](https://github.com/Kevinskwk/SCFields). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 촉각 입력 종류, pseudo-label 정확도, unseen-tool split은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D2의 도구·접촉 표현을 비교할 REFERENCE다. End-to-end VLA로 분류하지 않는다.

### Dependency and Evolution

Diffusion Policy와 접촉 표현을 출발점으로 SCFields의 tool generalization을 읽고 ForceVLA2의 force-feedback interface와 구별한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 demonstration에서 semantic-only와 contact 추가 조건을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

접촉 표현이 형상 표현만으로 얻는 이득을 넘는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
