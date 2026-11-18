# RFMPose: Generative Category-level Object Pose Estimation via Riemannian Flow Matching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Riemannian flow와 geodesic 경로·optimal transport를 사용하며 likelihood 추정 경로를 제안한다.

Omni6DPose의 pose metric과 sim-to-real/추적 확장을 보고한다. 이번 등록에서는 정책 제어 trial을 추정하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html) · [저자 project/code](https://github.com/shabiouyang/RMFPose). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Likelihood 구현·symmetry convention·공개 checkpoint·tracking 평가 조건은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

유한 pose 가설 생성과 score 해석을 비교하는 직접 NEXT다.

### Dependency and Evolution

Flow Matching의 생성 표현 → RFMPose → pose 가설별 행동 양립성 평가로 연결한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 K에서 top-score와 diversity-preserving 후보의 task-relevant coverage를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Pose 후보의 likelihood 순위가 조작에 필요한 가설 coverage를 보장하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
