# Insights — SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** Due to the shared network architecture and training procedure with SpatialVLM, vanilla PaLM 2-E naturally serves as the baseline to study the effect of generated data.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation/language → task decision → action/control`.
- **Registry interface:** `Vision-Language Model, spatial reasoning, Robotics` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - 3D observation을 language model이 다룰 수 있는 token/memory/query interface로 바꾸는 방식을 spatial reasoning과 embodied planning에 사용할 수 있다.
  - LLM/VLM의 commonsense를 쓰되, 3D geometry가 제공하는 metric constraint로 hallucination을 제어하는 방향이 중요하다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `3D Vision-Language Understanding`; tags: `Vision-Language Model, spatial reasoning, Robotics`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 3D QA/reasoning 성능 이후에도 metric grounding, benchmark leakage, embodied action validation은 별도 검증이 필요하다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: COCO / accuracy, success rate
  - 내 연구 확장 benchmark 후보: ScanNet, SQA3D, EmbodiedScan, Matterport3D
  - 내 연구 확장 metric 후보: accuracy, mIoU, grounding accuracy, task success
  - 검증 초점: 3D spatial reasoning, answer grounding, embodied task transfer를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

LLM이 답한 spatial reasoning이 실제 3D metric relation과 일치하는지 어떻게 자동 검증할 수 있는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
