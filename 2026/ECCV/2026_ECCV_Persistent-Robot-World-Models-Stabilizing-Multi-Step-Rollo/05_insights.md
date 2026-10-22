# Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

자신이 생성한 history에 conditioning하며 여러 미래 rollout을 비교하는 RL post-training과 multi-view visual fidelity reward를 제안한다.

공식 abstract/project는 DROID에서 LPIPS/SSIM/PSNR 기반 rollout fidelity와 human preference 평가를 설명한다. Downstream policy improvement는 별도 검증 대상이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.25685) · [저자 project/code](https://jaibardhan.com/persistworld/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Reward metric의 geometry/contact 민감도, rollout horizon, 실제 robot policy evidence 유무은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend. RL로 개선하는 대상은 world model의 autoregressive prediction이다. DROID rollout fidelity 근거를 policy success 개선으로 간주하지 않는다. Ctrl-World/WMPO 기반 learned simulator를 직접 고도화할 때 NEXT 검토.

### Dependency and Evolution

Ctrl-World → PersistWorld; VLAW/WMPO와 prediction-quality vs policy-improvement 구분.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 Ctrl-World backbone의 전후 checkpoint에서 video fidelity와 action-outcome ranking을 함께 평가하고 두 지표의 상관을 확인한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Visual fidelity 개선이 같은 MPC/정책 평가 예산에서 실제 action ranking 정확도로 이어지는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
