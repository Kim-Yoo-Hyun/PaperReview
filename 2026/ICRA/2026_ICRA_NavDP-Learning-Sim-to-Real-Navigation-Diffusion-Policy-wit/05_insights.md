# NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Privileged information guidance를 이용한 simulation training과 end-to-end local navigation diffusion policy를 제안한다.

저자 project는 no-goal exploration, point-goal/image-goal navigation과 cross-embodiment real-world transfer를 설명한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2505.08712) · [저자 project/code](https://github.com/InternRobotics/NavDP). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Training oracle, depth/pose 입력, trajectory selector, robot footprint와 controller 한계은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend. Simulation training에서 real-world cross-embodiment local navigation으로 이어지는 경로를 보충한다. NoMaD/ViNT의 local policy와 비교할 대상이며, 논문 자체를 language-conditioned VLA RL로 부르지는 않는다.

### Dependency and Evolution

ViNT/NoMaD → NavDP → LoGoPlanner; X-NavDP는 미등록 watchlist.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

NoMaD/NavDP의 goal·sensor·controller 조건을 맞춘 local navigation task에서 collision·success·latency를 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Privileged guidance의 이득이 onboard observation과 collision constraints를 동일하게 맞춰도 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
