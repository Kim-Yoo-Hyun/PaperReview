# Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Contact point로 조건화한 modular utility policies와 EgoGym 반복 평가를 제안한다.

Pick/Open/Close와 새 환경·embodiment 평가를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p141.html) · [저자 project/code](https://cap-policy.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 anchor 획득 비용, embodiment split, 실제 checkpoint release은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA의 이득이 task specification 차이인지 가릴 강한 non-VLA baseline이므로 NEXT다.

### Dependency and Evolution

ACT/Diffusion Policy의 visuomotor 학습 → CAP의 contact-conditioned utility; OpenVLA의 language-conditioned goal 정보와 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

GT contact anchor와 추정 anchor를 분리하고 동일 정보의 VLA와 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 goal 정보에서 contact-conditioned 정책이 VLA보다 충분한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
