# Insights — ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.
- **Problem cue:** In recent years, there has been tremendous progress in both semantic understanding and localization of objects in 2D images from natural language (also known as visual grounding).
- **Claim/result cue:** Results and analysis are conducted on the val split (except for results in Tab.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation/language → task decision → action/control`.
- **Registry interface:** `3D visual grounding, RGB-D, semantic` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - 2D vision-language feature를 3D object/point/field/map에 정렬해 open-vocabulary querying과 semantic grounding에 사용할 수 있다.
  - 핵심은 language prior를 3D metric structure와 맞추면서 view inconsistency와 hallucination을 줄이는 것이다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `3D Vision-Language Understanding`; tags: `3D visual grounding, RGB-D, semantic`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: Results and analysis are conducted on the val split (except for results in Tab.
  - 저자가 남긴 확장 방향: Overall, we hope that our new dataset and method will enable future research in the 3D visual language field.
  - open-vocabulary recognition이나 grounding을 보인 뒤에도 3D consistency, ambiguous reference resolution, robot-action relevance는 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: ScanNet, ShapeNet, ScanRefer / accuracy, IoU, mAP
  - 내 연구 확장 benchmark 후보: ScanNet, ScanRefer, ReferIt3D, SQA3D
  - 내 연구 확장 metric 후보: mIoU, Acc@0.25, Acc@0.5, Recall@K
  - 검증 초점: open-vocabulary segmentation/localization, 3D consistency, task-relevant grounding을 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

2D VLM feature를 3D로 lift할 때 multi-view consistency와 fine-grained object boundary를 동시에 유지할 수 있는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
