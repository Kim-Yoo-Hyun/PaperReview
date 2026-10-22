# When would Vision-Proprioception Policies Fail in Robotic Manipulation?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Motion-transition phase에 따라 proprioception gradient를 조정하는 GAP을 제안한다.

Simulation·실제 single/dual-arm 및 Octo 적용을 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html) · [저자 project/code](https://gewu-lab.github.io/GAP/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 phase 추정 신호, task split, native Octo 코드·checkpoint은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D1에서 modality dominance를 새 발견으로 주장하지 않도록 추가한 직접 NEXT다.

### Dependency and Evolution

HPT·Octo의 vision/proprioception 결합 → GAP의 phase-guided training → ReViP의 inference-time progress feedback을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 데이터에서 GAP와 corruption augmentation을 hidden-fault holdout으로 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

학습 불균형 교정만으로 hidden fault 대응이 충분한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
