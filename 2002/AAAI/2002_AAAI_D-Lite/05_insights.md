# Insights — D* Lite

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite.
- **Problem cue:** Heuristic search methods, such as A* (Nilsson 1971), on the other hand, use heuristic knowledge in form of approximations of the goal distances to focus the search and ...
- **Claim/result cue:** We believe that these results provide a strong foundation for further research on fast replanning methods in artificial intelligence and robotics.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `task & motion decision → policy/control`.
- **Registry interface:** `Robotics, path planning, incremental search, Navigation` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Language/semantic goal을 metric 3D map, BEV, scene graph, frontier/map memory와 연결해 navigation state representation으로 사용할 수 있다.
  - Navigation의 핵심 병목을 visual-language matching만이 아니라 spatial memory, localization, graph planning 문제로 재정의할 수 있다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Robotics Foundations: Planning and Control`; tags: `Robotics, path planning, incremental search, Navigation`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: We believe that these results provide a strong foundation for further research on fast replanning methods in artificial intelligence and robotics.
  - 논문 내 한계/논의 단서: D* Lite builds on our LPA*, that has a solid theoretical foundation, a strong similarity to A*, is efficient (since it does not expand any vertices whose gvalues ...
  - navigation 성능을 보인 뒤에도 geometry-aware memory의 누적 오류, unseen scene transfer, semantic grounding failure는 후속 연구 지점으로 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: 자동 추출에서 명확한 dataset 단서 없음 / 자동 추출에서 명확한 metric 단서 없음
  - 내 연구 확장 benchmark 후보: R2R, RxR, VLN-CE, Habitat
  - 내 연구 확장 metric 후보: SR, SPL, nDTW, collision
  - 검증 초점: instruction/semantic goal following, path efficiency, unseen environment generalization, online correction을 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

3D map/scene graph/gaussian map 중 어떤 representation이 language/semantic goal following에 가장 안정적인가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
