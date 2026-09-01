# Insights — AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** In this paper, to address these issues and improve generalization performance, we propose an AlIgned 3D Open-Vocabulary S Emantic Segmentation framework, called A I D E, with two ...
- **Problem cue:** Due to the lack of large-scale 3D-vision-language segmentation data, instead of training models from scratch, the current solutions distill knowledge from pre-trained 2D vision-language models (VLMs) into 3D ...
- **Claim/result cue:** Extensive experiments show that A I D E outperforms previous methods by a large margin on three representative benchmarks, demonstrating its effectiveness.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation/language → task decision → action/control`.
- **Registry interface:** `open-vocabulary, semantic, alignment` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - 2D vision-language feature를 3D object/point/field/map에 정렬해 open-vocabulary querying과 semantic grounding에 사용할 수 있다.
  - 핵심은 language prior를 3D metric structure와 맞추면서 view inconsistency와 hallucination을 줄이는 것이다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Embodied Navigation and Mapping`; tags: `open-vocabulary, semantic, alignment`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: Extensive experiments show that A I D E outperforms previous methods by a large margin on three representative benchmarks, demonstrating its effectiveness.
  - open-vocabulary recognition이나 grounding을 보인 뒤에도 3D consistency, ambiguous reference resolution, robot-action relevance는 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: ImageNet, ScanNet, S3DIS, nuScenes / mIoU, IoU, mAP
  - 내 연구 확장 benchmark 후보: ScanNet, ScanRefer, ReferIt3D, SQA3D
  - 내 연구 확장 metric 후보: mIoU, Acc@0.25, Acc@0.5, Recall@K
  - 검증 초점: open-vocabulary segmentation/localization, 3D consistency, task-relevant grounding을 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

2D VLM feature를 3D로 lift할 때 multi-view consistency와 fine-grained object boundary를 동시에 유지할 수 있는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
