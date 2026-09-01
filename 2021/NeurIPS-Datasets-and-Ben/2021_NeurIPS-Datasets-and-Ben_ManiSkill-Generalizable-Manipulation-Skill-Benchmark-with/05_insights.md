# Insights — ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`.
> Analysis basis: `ABSTRACT_CHECKED`; 01_overview의 source audit와 기존 insight cue를 이관했다: official proceedings abstract and project page checked; task statistics and baseline tables remain UNVERIFIED. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 확인 범위는 공식 abstract/project 수준이다. 상세 method, exact metric, failure는 full-text 확인 전까지 확정하지 않는다.

### What was actually new

- **Problem cue:** 다양한 objects와 tasks에 generalize하는 manipulation skill을 대규모·재현 가능하게 평가한다.
- **Method cue:** physics simulation, task suite, demonstration trajectories와 standardized learning tracks를 제공한다.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `policy/control → contact → feedback`.
- **Registry interface:** `Robotics, Benchmark, Dataset, manipulation, simulation` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - large-scale demonstrations와 object-level generalization을 결합한 manipulation benchmark로 modern GPU simulation/data generation 계보의 핵심이다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- SAPIEN simulation → ManiSkill → ManiSkill2/3와 large-scale GPU robot-learning benchmark로 이어진다.
- The recorded arrow is a reading dependency, not a confirmed citation relationship unless the references are checked.

### Minimal reproduction

1. Confirm the paper-reported input, output, task, metric, baseline, and split from the full text.
2. Implement the smallest paper-specific component and a simpler matched baseline.
3. Evaluate the primary paper metric plus failure rate, latency, and sensitivity to the assumption most central to the method.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

고정된 sensing/control rate에서 Robotics, Benchmark, Dataset, manipulation, simulation interface가 직접 joint-action baseline보다 contact loss와 force/pose error를 줄이는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
