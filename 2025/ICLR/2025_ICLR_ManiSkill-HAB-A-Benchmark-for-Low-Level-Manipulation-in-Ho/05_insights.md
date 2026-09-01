# Insights — ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- Available source material does not yet establish a paper-specific contribution; verify the abstract/full text before treating this as a conclusion.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `policy/control → contact → feedback`.
- **Registry interface:** `Robotics, Benchmark, home rearrangement, Reinforcement Learning` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Dataset/benchmark 설계 방식을 연구 아이디어의 evaluation protocol과 failure taxonomy를 잡는 기준으로 사용할 수 있다.
  - 새 방법을 제안하기 전, 이 benchmark가 어떤 input, annotation, split, metric을 표준화했는지 확인해야 한다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Robot Learning and Data`; tags: `Robotics, Benchmark, home rearrangement, Reinforcement Learning`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - benchmark는 task를 정의하지만, 실제 robot deployment나 open-world generalization을 완전히 대변하지 못할 수 있다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: Habitat, ManiSkill / success rate, collision
  - 내 연구 확장 benchmark 후보: paper-defined benchmark
  - 내 연구 확장 metric 후보: paper-defined metrics, generalization gap, failure rate
  - 검증 초점: benchmark coverage, split validity, metric-task alignment를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

현재 benchmark metric이 3D CV 성능과 robotics task success 사이의 차이를 충분히 드러내는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
