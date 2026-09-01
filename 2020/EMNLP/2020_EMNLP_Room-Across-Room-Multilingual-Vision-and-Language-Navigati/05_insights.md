# Insights — Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** We introduce Room-Across-Room (RxR), a new Vision-and-Language Navigation (VLN) dataset.
- **Problem cue:** We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗ First two authors contributed equally. including more paths that (2) counter known ...
- **Claim/result cue:** In preliminary experiments, we found that pretraining the CNN in this way gave noticeable improvements over the same CNN pretrained for image classification on ImageNet (Russakovsky et al., ...

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation/language → task decision → action/control`.
- **Registry interface:** `Vision-Language Navigation, Navigation, grounding, Benchmark` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Language/semantic goal을 metric 3D map, BEV, scene graph, frontier/map memory와 연결해 navigation state representation으로 사용할 수 있다.
  - Navigation의 핵심 병목을 visual-language matching만이 아니라 spatial memory, localization, graph planning 문제로 재정의할 수 있다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Embodied Navigation and Mapping`; tags: `Vision-Language Navigation, Navigation, grounding, Benchmark`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: In preliminary experiments, we found that pretraining the CNN in this way gave noticeable improvements over the same CNN pretrained for image classification on ImageNet (Russakovsky et al., ...
  - navigation 성능을 보인 뒤에도 geometry-aware memory의 누적 오류, unseen scene transfer, semantic grounding failure는 후속 연구 지점으로 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: ImageNet, Matterport3D, R2R, RxR / SPL, SR, nDTW, success rate
  - 내 연구 확장 benchmark 후보: R2R, RxR, VLN-CE, Habitat
  - 내 연구 확장 metric 후보: SR, SPL, nDTW, collision
  - 검증 초점: instruction/semantic goal following, path efficiency, unseen environment generalization, online correction을 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

3D map/scene graph/gaussian map 중 어떤 representation이 language/semantic goal following에 가장 안정적인가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
