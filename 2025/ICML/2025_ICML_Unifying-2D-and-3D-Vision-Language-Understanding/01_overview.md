# Unifying 2D and 3D Vision-Language Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/jain25b.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/167696. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Ayush Jain, Alexander Swerdlow, Yuzhou Wang, Sergio Arnaud, Ada Martin, Alexander Sax, Franziska Meier, Katerina Fragkiadaki
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision
- Official paper: https://proceedings.mlr.press/v267/jain25b.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/jain25b/jain25b.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jain25b/jain25b.pdf)

## Why This Paper Is Here

UniVLG는 동일한 언어 조건부 마스크 디코더로 2D RGB 영상과 3D RGB-D 관측에서 지칭된 물체를 찾는다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jain25b/jain25b.pdf#page=1) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jain25b/jain25b.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Progress in 3D vision-language learning has been hindered by the scarcity of large-scale 3D datasets.
- **p. 1 / Abstract - extractive body cue:** We introduce UniVLG, a unified architecture for 2D and 3D vision-language understanding that bridges the gap between existing 2D-centric models and the rich 3D sensory ...
- **p. 1 / Abstract - extractive body cue:** Our approach initializes most model weights from pre-trained 2D models and trains on both 2D and 3D vision-language data.
- **p. 1 / Abstract - extractive body cue:** We propose a novel language-conditioned mask decoder shared across 2D and 3D modalities to ground objects effectively in both RGB and RGBD images, outperforming box-based ...
- **p. 1 / Abstract - extractive body cue:** To further reduce the domain gap between 2D and 3D, we incorporate 2D-to-3D lifting strategies, enabling UniVLG to utilize 2D data to enhance 3D performance.
- **p. 1 / 1. Introduction - extractive body cue:** Given these challenges, is scaling 3D training data the only viable path to bridging this gap, or are there alternative strategies for making 3D models ...
- **p. 1 / 1. Introduction - extractive body cue:** The key limitation, however, is dataset availability: while 2D datasets are vast and well-curated, 3D datasets remain scarce and expensive to annotate (Dai et al., ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • Unified 2D-3D Visual Grounding: We propose a model that can consume and benefit from both 2D and 3D vision-language ...
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we introduce UniVLG, a unified 2D-3D visionlanguage model designed to improve 3D understanding by leveraging large-scale 2D data and pre-trained 2D models.
- **p. 5 / 3.1. Supervision Objective - extractive body cue:** To address this, we introduce a novel box loss.
- **p. 3 / 3. Method - extractive body cue:** The output consists of segmentation masks for each object mentioned in the sentence, a corresponding text span that refers to each segmented object, and optionally, ...
- **p. 4 / 3. Method - extractive body cue:** Open-vocabulary mask decoders, such as those in ODIN (Jain et al., 2024) and X-Decoder (Zou et al., 2023), which extend Mask2Former's decoder to accept language ...
- **p. 3 / 3. Method - extractive body cue:** Language Conditioned Mask Decoder: The mask decoder head takes as input the encoded visual features, their corresponding (relative) 3D coordinates, and the encoded language utterance; ...
- **p. 4 / 3. Method - extractive body cue:** The proposed decoder then iteratively updates a set of learnable queries as well as the 3D feature tokens though token - language - query attentions ...
- **p. 4 / 3. Method - extractive body cue:** The refined queries after each decoder layer Q(i+1) = X(i+1) 1:M are then used for mask prediction with the updated visual features and for language ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (D) Example task inputs/outputs for UniVLG. on both visual features and language instructions to ground objects mentioned in the language input. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 3 (3. Method) |
| State/latent | Example, task, inputs/outputs, UniVLG, visual, features, language, instructions, ground, objects, mentioned, input | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction) |
| Output/action | Language Conditioned Mask Decoder: The mask decoder head takes as input the encoded visual features, their corresponding (relative) 3D coordinates, and the encoded language utterance; it outputs 3D segmentation masks of the ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Method), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | We incorporate this box loss as an additional cost in both Hungarian matching and the final loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.1. Supervision Objective), p. 5 (3.1. Supervision Objective), p. 3 (3. Method) |

## Main Claims and Actual Contribution

- 사전학습 2D 모델의 가중치를 활용하고 2D 특징을 3차원으로 올려 두 종류의 지도 신호로 함께 학습한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jain25b/jain25b.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jain25b/jain25b.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jain25b/jain25b.pdf#page=5)
- 3D 지시 표현의 장면 간 전이와 2D 지시 분할을 각각 평가하고 2D·3D 공동학습 및 마스크 출력의 영향을 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jain25b/jain25b.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jain25b/jain25b.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jain25b/jain25b.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (1. Lifting 2D datasets to 3D improves 3D performance), p. 7 (4.1. Evaluation on 3D Referential Grounding) |
| Embodiment/environment | For example, 3D-VisTA (Zhu et al., 2023b) trains on the previously mentioned 3D datasets that we use but also includes 3RScan (1500 scenes) (Wald et al., 2019), Objaverse (700k objects) (Deitke et ... | hardware/simulator version and reset protocol | p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding) |
| Dataset/benchmark | We show results in Table 3 on the validation sets of these benchmarks. | role, split, size and leakage | p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 7 (4.3. Evaluation on 3D Question Answering), p. 7 (4.3. Evaluation on 3D Question Answering) |
| Metric | It dramatically outperforms alternative single stage models, such as BUTDDETR, on the stricter IoU threshold of 0.75, thanks to predicting masks instead of bounding boxes-as we demonstrate later in Table 5c. | definition, denominator, direction and uncertainty | p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4. Experiments) |
| Baseline/ablation | UniVLG outperforms all prior baselines on both benchmarks. | fair input/data/compute/action matching | p. 7 (4.3. Evaluation on 3D Question Answering), p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4.7. Common failure modes of UniVLG - extractive body cue:** We identify three systematic failure modes in our model, illustrated in Figure-5 (see Appendix).
- **p. 9 / 4.7. Common failure modes of UniVLG - extractive body cue:** Classes UniVLG 72.6 53.8 UniVLG w/o 2D-to-3D lifting 71.4 0.0 UniVLG (Upper-Bound) 69.7 84.2 Grounding failures as seen in the third image of Figure-5.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 5. Systematic failure modes of UniVLG: Green boxes and masks are ground-truth, red masks and boxes are UniVLG's predictions. COCO/+/g datasets (Kazemzadeh et al., ...
- **p. 8 / 4.4. Evaluation on 2D Referential Grounding - extractive body cue:** Our results show that co-training with 3D data does not degrade the performance of the version trained solely on 2D data.
- **p. 7 / 4.3. Evaluation on 3D Question Answering - extractive body cue:** We found that using sensor point clouds vs mesh point clouds does not result in a significant difference in performance in these benchmarks, likely because ...
- **p. 7 / 4.2. Evaluation on Out-of-Domain 3D Referential - extractive body cue:** L3DD allows us to assess the robustness of our model on new scenes, camera capture systems, and language instructions.
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 6. We analyze the performance of UniVLG and BUTD-DETR on SR3D as the pose and depth error increases. We add gaussian noise to the ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3. Method)이다.
