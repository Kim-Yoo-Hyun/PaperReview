# Insights — LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity.
- **Problem cue:** This infrastructure drives a fivedimensional curriculum that decouples safety into semantic reasoning and physical constraints. – Keypose-Driven Data Generation Pipeline: To overcome the inefficiency and scalability bottlenecks of ...
- **Claim/result cue:** 4.1 Experimental Setup To systematically benchmark safety performance across both physical execution and cognitive reasoning, we evaluate a comprehensive suite of 10 representative architectures.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation → state/world model → decision/recovery`.
- **Registry interface:** `VLA, Vision-Language Model, Benchmark, semantic` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Language-conditioned perception을 바로 action/policy token으로 연결하는 방식을 3D object state, affordance, contact-aware manipulation으로 확장할 수 있다.
  - 2D image 중심 VLA가 놓치는 pose, metric distance, occlusion을 3D representation이나 scene memory로 보강하는 연구 질문으로 이어진다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Benchmarks and Datasets`; tags: `VLA, Vision-Language Model, Benchmark, semantic`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: 4.1 Experimental Setup To systematically benchmark safety performance across both physical execution and cognitive reasoning, we evaluate a comprehensive suite of 10 representative architectures.
  - 논문 내 한계/논의 단서: We therefore view LIBERO-Safety as a structured evaluation and data-generation foundation for future work on real-world validation, dense unsafe-event annotation, and intrinsically safety-aligned VLA models.
  - robot action까지 보인 경우에도 3D state grounding, closed-loop correction, force/tactile feedback, unseen embodiment generalization은 별도 검증이 필요하다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: RLBench, CALVIN, LIBERO, RoboTwin / SR, success rate, collision
  - 내 연구 확장 benchmark 후보: CALVIN, LIBERO, RLBench, Open X-Embodiment
  - 내 연구 확장 metric 후보: success rate, task completion, generalization gap, collision
  - 검증 초점: language-conditioned manipulation success, unseen object/task generalization, closed-loop recovery를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

3D geometry token을 VLA policy에 넣을 때 action success와 language following 중 어느 부분이 실제로 개선되는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
