# ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Flow 경로에 학습 가능한 잡음을 넣어 이산 시간 확률 과정으로 바꾸고 정책 likelihood를 사용해 online RL 후학습한다.

공식 abstract는 locomotion과 state/visual manipulation에서 Rectified Flow·Shortcut 정책 후학습을 보고한다. 최신 저장소의 VLA 지원을 원 논문 실험으로 소급하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html) · [저자 project/code](https://reinflow.github.io/) · [공식 code](https://github.com/ReinFlow/ReinFlow). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 생성 경로 likelihood와 action likelihood의 차이, DPPO 비교의 모델/자료/시간 통제, noise 학습과 step 축소 효과, 실제 로봇 평가 여부은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

PPO·Flow Matching·DPPO를 로봇 flow-policy online RL로 연결하는 비교 방법. 단순 noise 학습을 새 VLA RL 기여로 주장하기 전에 읽어야 한다.

### Dependency and Evolution

Flow Matching·policy gradient·Diffusion Policy/DPPO → ReinFlow → 후속 flow VLA RL. 후속 repository 기능은 별도 version이다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

하나의 공개 task에서 같은 초기 flow 정책과 생성 step 수로 고정/학습 noise를 비교하고 성공률·return·전체 rollout/학습 wall time을 함께 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 interaction·초기 정책·전체 계산 예산에서 학습 noise의 이득이 생성 step 수와 보상 희소성에 따라 어떻게 달라지는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
