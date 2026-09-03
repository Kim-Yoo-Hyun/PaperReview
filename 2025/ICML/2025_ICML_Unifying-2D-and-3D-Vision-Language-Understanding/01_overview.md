# Unifying 2D and 3D Vision-Language Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=FcTeo26AfZ.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/167696. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision
- Official paper: https://openreview.net/forum?id=FcTeo26AfZ
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/167696
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Given these challenges, is scaling 3D training data the only viable path to bridging this gap, or are there alternative strategies for making 3D models more effective?를 문제로 두고, In summary, our contributions are: • Unified 2D-3D Visual Grounding: We propose a model that can consume and benefit from both 2D and 3D vision-language data. • State-of-the-Art Performance: UniVLG achieves state-of-the-art ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • Unified 2D-3D Visual Grounding: We propose a model that can consume and benefit from both 2D and 3D vision-language ...
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we introduce UniVLG, a unified 2D-3D visionlanguage model designed to improve 3D understanding by leveraging large-scale 2D data and pre-trained 2D models.
- **p. 5 / 3.1. Supervision Objective - extractive body cue:** To address this, we introduce a novel box loss.
- **p. 3 / 3. Method - extractive body cue:** The output consists of segmentation masks for each object mentioned in the sentence, a corresponding text span that refers to each segmented object, and optionally, ...
- **p. 4 / 3. Method - extractive body cue:** Open-vocabulary mask decoders, such as those in ODIN (Jain et al., 2024) and X-Decoder (Zou et al., 2023), which extend Mask2Former's decoder to accept language ...
- **p. 8 / 1. Lifting 2D datasets to 3D improves 3D performance - extractive body cue:** We observe that incorporating 2D data improves performance in both scenarios, but our approach of lifting 2D images to 3D achieves the best results.
- **p. 7 / 4.1. Evaluation on 3D Referential Grounding - extractive body cue:** In the GT setup as well, UniVLG significantly outperforms 3D-VisTA and closely matches the performance of the recent work of PQ3D in the setup where ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. (A) UniVLG achieves state-of-the-art performance performance across a range of referential grounding, question answering, and instance segmentation benchmarks. (B) UniVLG is a unified ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Given these challenges, is scaling 3D training data the only viable path to bridging this gap, or are there alternative strategies for making 3D models more effective?를 문제로 두고, In summary, our contributions are: • Unified 2D-3D Visual Grounding: We propose a model that can consume and benefit from both 2D and 3D vision-language data. • State-of-the-Art Performance: UniVLG achieves state-of-the-art ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
