# Insights — Hierarchical Task and Motion Planning in the Now

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`.
> Analysis basis: `ABSTRACT_CHECKED`; 01_overview의 source audit와 기존 insight cue를 이관했다: publisher metadata and abstract checked; algorithmic details remain UNVERIFIED. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 확인 범위는 공식 abstract/project 수준이다. 상세 method, exact metric, failure는 full-text 확인 전까지 확정하지 않는다.

### What was actually new

- **Problem cue:** 긴 symbolic plan 전체를 미리 확정하면 geometric infeasibility와 실행 중 변화에 취약한 문제를 다룬다.
- **Method cue:** 현재 필요한 action을 중심으로 task planning과 motion planning을 interleave하는 hierarchical approach를 제안한다.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `task & motion decision → policy/control`.
- **Registry interface:** `Robotics, Planning, task and motion planning, manipulation` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - symbolic task choice와 geometric motion feasibility를 계층적으로 연결한 초기 TAMP 대표작이다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- hierarchical TAMP → FFRob/LGP/PDDLStream → language-guided long-horizon robot planning으로 이어진다.
- The recorded arrow is a reading dependency, not a confirmed citation relationship unless the references are checked.

### Minimal reproduction

1. Confirm the paper-reported input, output, task, metric, baseline, and split from the full text.
2. Implement the smallest paper-specific component and a simpler matched baseline.
3. Evaluate the primary paper metric plus failure rate, latency, and sensitivity to the assumption most central to the method.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

고정된 state, action, compute budget에서 Robotics, Planning, task and motion planning, manipulation formulation이 task cost 또는 success를 유지하면서 perturbation 이후 recovery를 개선하는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
