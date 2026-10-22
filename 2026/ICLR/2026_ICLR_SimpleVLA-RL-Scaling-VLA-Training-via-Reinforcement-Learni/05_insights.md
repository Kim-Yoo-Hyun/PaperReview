# SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Outcome reward 기반 VLA RL에 trajectory sampling, parallel rollout/rendering 및 loss 계산 최적화를 결합한다.

ICLR abstract는 LIBERO, RoboTwin 1.0/2.0 및 real-world task 결과를 보고한다. Real-world 평가와 실제 online training은 구분해야 한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) · [저자 project/code](https://github.com/PRIME-RL/SimpleVLA-RL). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 실제 robot online training 범위, sparse reward 생성, data leakage 및 compute accounting은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend / system. OpenVLA-OFT에서 outcome reward와 scalable rollout/training을 다룬다. 현재 OFT → ConRFT 경로에 대규모 simulator RL의 비교 지점을 추가한다. Real-world 결과와 real-world online training의 범위는 구분해서 정독해야 한다.

### Dependency and Evolution

OpenVLA-OFT + PPO → SimpleVLA-RL; ConRFT/RLux-VLA와 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

OFT SFT와 SimpleVLA-RL을 동일 task에서 비교하고 rollout 수·reward access·성공률·기존 task retention을 함께 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 초기 OFT와 interaction budget에서 exploration 설계가 희소 reward의 long-horizon 학습을 개선하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
