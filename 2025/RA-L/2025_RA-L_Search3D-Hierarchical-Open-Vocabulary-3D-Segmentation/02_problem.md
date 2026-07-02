# Problem

- Year/Venue: 2025 / RA-L
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, semantic
- Paper link: ./2025/RA-L/2025_RA-L_Search3D-Hierarchical-Open-Vocabulary-3D-Segmentation/paper.pdf
- Code/Project: http://search3d-segmentation.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing methods for open-vocabulary 3D instance segmentation primarily focus on identifying object-level instances but struggle with finer-grained scene entities such as object parts, or regions described by generic ...
- Unlike prior methods, Search3D shifts towards a more flexible open-vocabulary 3D search paradigm, moving beyond explicit object-centric queries.

## 해결하려는 문제
- In this work, we introduce Search3D, an approach to construct hierarchical open-vocabulary 3D scene representations, enabling 3D search at multiple levels of granularity: fine-grained object parts, entire objects, ...
- Search3D outperforms baselines in scene-scale open-vocabulary 3D part segmentation, while maintaining strong performance in segmenting 3D objects and materials.
- For systematic evaluation, we further contribute a scene-scale open-vocabulary 3D part segmentation benchmark based on MultiScan, along with a set of open-vocabulary fine-grained part annotations on ScanNet++.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
