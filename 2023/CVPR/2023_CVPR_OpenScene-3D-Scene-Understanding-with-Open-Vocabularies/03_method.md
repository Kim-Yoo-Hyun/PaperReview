# Method

- Year/Venue: 2023 / CVPR
- Category: Open-Vocabulary 3D Mapping
- Tags: open-vocabulary, 3D semantic, CLIP
- Paper link: ./2023/CVPR/2023_CVPR_OpenScene-3D-Scene-Understanding-with-Open-Vocabularies/paper.pdf
- Code/Project: https://pengsongyou.github.io/openscene
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose OpenScene, an alternative approach where a model predicts dense features for 3D scene points that are co-embedded with text and image pixels in CLIP feature space.
- Our approach is effective at identifying objects, materials, affordances, activities, and room types in complex 3D scenes, all using a single model trained without any labeled 3D data.
- This zero-shot approach enables taskagnostic training and open-vocabulary queries.

## 원리적 동기
- posed RGB images, the goal is to infer the semantics, affordances, functions, and physical properties of every 3D point.
- For example, given the house shown in Figure 1, we would like to predict which surfaces are part of a fan (semantics), made of metal (materials), within a ...
- We propose OpenScene, an alternative approach where a model predicts dense features for 3D scene points that are co-embedded with text and image pixels in CLIP feature space.

## 핵심 방법론
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
