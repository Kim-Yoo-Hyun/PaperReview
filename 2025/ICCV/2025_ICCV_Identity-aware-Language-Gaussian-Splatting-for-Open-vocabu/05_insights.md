# Insights — Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** To address this issue, we propose a simple yet powerful method that aligns language embeddings via the identity information.
- **Problem cue:** This limitation still makes the practical use of open-vocabulary 3D semantic segmentation challenging.
- **Claim/result cue:** Experimental results on benchmark datasets demonstrate that our method delivers state-of-the-art performance in open-vocabulary 3D semantic segmentation. https://github.com/DCVL-3D/ILGS release view2 Cosine similarity Others Sheep view2 view1 Gaussian field ...

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation/language → task decision → action/control`.
- **Registry interface:** `3D Vision, Gaussian Splatting, semantic` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Differentiable 3D scene representation을 semantic map, view synthesis, robot memory, planning cost field로 재사용할 수 있다.
  - Geometry와 appearance를 함께 담는 표현은 language feature, object identity, dynamic state를 붙이는 기반이 된다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Language-Grounded 3D Scene Representations`; tags: `3D Vision, Gaussian Splatting, semantic`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: Experimental results on benchmark datasets demonstrate that our method delivers state-of-the-art performance in open-vocabulary 3D semantic segmentation. https://github.com/DCVL-3D/ILGS release view2 Cosine similarity Others Sheep view2 view1 Gaussian field ...
  - reconstruction/view synthesis 품질을 보인 뒤에도 real-time update, semantic consistency, dynamic interaction, robot-safe planning은 후속 과제로 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: LERF / accuracy, mIoU, IoU, mAP, PSNR
  - 내 연구 확장 benchmark 후보: Replica, ScanNet, Mip-NeRF 360, Tanks and Temples
  - 내 연구 확장 metric 후보: PSNR, SSIM, LPIPS, mIoU
  - 검증 초점: view synthesis 품질뿐 아니라 semantic querying, map update, robot task success를 같이 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

Gaussian/NeRF field에 language feature를 붙일 때 3D consistency와 open-vocabulary retrieval을 동시에 유지할 수 있는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
