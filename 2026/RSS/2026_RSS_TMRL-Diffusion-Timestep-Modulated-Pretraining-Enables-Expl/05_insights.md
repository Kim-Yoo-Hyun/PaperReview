# TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

입력에 diffusion noise를 넣어 사전학습하고 RL이 조건화 noise 수준을 선택한다.

항법·조작 평가를 보고하며 project는 실제 VLA 후학습도 설명한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p208.html) · [저자 project/code](https://weirdlabuw.github.io/tmrl/) · [공식 code](https://github.com/matthewh6/tmrl). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 pretraining 추가 비용, high-level action 주기, baseline 탐색 분산, 로봇별 학습 시간은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA 내부 학습을 제안할 때 비교해야 할 사전학습 coverage·탐색 조절 대안이다.

### Dependency and Evolution

Diffusion Policy·π0·RL fine-tuning을 잇지만 high-level timestep 선택 구조임을 구별한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 CSP checkpoint에서 고정 noise, 무작위 noise, 학습된 noise 선택을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

이득이 context-smoothed pretraining에서 오는가, 적응적 timestep 선택에서 오는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
