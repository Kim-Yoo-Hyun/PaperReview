# Unifying 3D Vision-Language Understanding via Promptable Queries

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6043_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06043.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6043_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06043.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Recent advancements in embodied artificial intelligence have emphasized the importance of connecting 3D scene understanding with natural language [16,27, 29, 44, 71].를 문제로 두고, In this section, we present PQ3D, which consists of three main modules: Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning, as depicted in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Recent advancements in embodied artificial intelligence have emphasized the importance of connecting 3D scene understanding with natural language [16,27, 29, 44, 71].
- **p. 1 / 1 Introduction - extractive body cue:** This step is crucial for embodied agents to understand and execute human instructions in real-world scenarios [4,51].
- **p. 1 / 1 Introduction - extractive body cue:** In recent years, numerous tasks and datasets for benchmarking 3D scene understanding with languages have been proposed, including 3D semantic segmentation [52], 3D vision-language ⋆Work ...
- **p. 2 / 1 Introduction - extractive body cue:** Prompt: [Navigate to the door] Prompt: [Chair] Prompt: [Cabinet to the left of the TV] Prompt: [I want to watch Super Bowl] Prompt: [Describe this ...

## Core Idea

- **p. 5 / 3 Method - extractive body cue:** In this section, we present PQ3D, which consists of three main modules: Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning, as depicted in ...
- **p. 7 / 3 Method - extractive body cue:** 3.3 Prompt-guided Query Learning We propose a novel Transformer-like decoder to instruct the instance queries to assimilate scene and prompt information.
- **p. 6 / 3 Method - extractive body cue:** With such unification, we do not distinguish different prompt formats anymore and this design enables the model to transfer knowledge between different prompts.
- **p. 6 / 3 Method - extractive body cue:** Finally, each updated instance query is fed into three output heads to predict an instance mask, a task-relevance score, and a sentence. model [49], which ...
- **p. 7 / 3 Method - extractive body cue:** Within the decoder layer l, the instance queries Ql retrieve task-relevant information by first attending to the scene features {V, I, P} in parallel and ...
- **p. 8 / 3 Method - extractive body cue:** To support flexible inference when only some representations are available, we randomly drop out some scene features with rate 0.6 in masked-attention computation during training.
- **p. 7 / 3 Method - extractive body cue:** Then, we encode these scene representations by the corresponding encoders and pool the features to the segments in total of M.
- **p. 6 / 3 Method - extractive body cue:** In scene encoding, point clouds, voxel grids, and multi-view images of a scene are first encoded by corresponding encoders and then aligned into a shared ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Finally, each updated instance query is fed into three output heads to predict an instance mask, a task-relevance score, and a sentence. model [49], which allows us to train using a text ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3 Method), p. 8 (3 Method) |
| State/latent | Finally, updated, instance, query, three, output, heads, predict, mask, task-relevance, score, sentence | geometry, map, object/relationship state | p. 6 (3 Method), p. 8 (3 Method), p. 8 (3 Method) |
| Output/action | Generation head We choose the decoder of a pre-trained T5-small [12,50] as the generation head to generate a text response, using all instance queries as the encoded inputs. | point map, pose, scene graph, affordance 또는 query result | p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method) |
| Objective/outcome | During training, if text responses are provided as supervision for dense caption and QA task, we calculate the cross-entropy loss as the generation loss Lgen. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- **p. 5 / 3 Method - extractive body cue:** In this section, we present PQ3D, which consists of three main modules: Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning, as depicted in ...
- **p. 7 / 3 Method - extractive body cue:** 3.3 Prompt-guided Query Learning We propose a novel Transformer-like decoder to instruct the instance queries to assimilate scene and prompt information.
- **p. 6 / 3 Method - extractive body cue:** With such unification, we do not distinguish different prompt formats anymore and this design enables the model to transfer knowledge between different prompts.
- **p. 6 / 3 Method - extractive body cue:** Finally, each updated instance query is fed into three output heads to predict an instance mask, a task-relevance score, and a sentence. model [49], which ...
- **p. 10 / 4 Experiments - extractive body cue:** Furthermore, on the Multi3DRefer benchmark, our model outperforms others in the ST (single target) and MT (multiple targets) categories and achieves the highest average score ...
- **p. 11 / 4 Experiments - extractive body cue:** The proposed PQ3D provides global 3D features to the navigation agent that can improve the baseline VC-1 by a significant margin, achieving a 22.9% increase ...
- **p. 13 / 4 Experiments - extractive body cue:** When both image and point features are absent, the PQ3D outperforms the specific-tuned model, demonstrating the improved generalization ability through training with multiple representations.
- **p. 12 / 4 Experiments - extractive body cue:** The results suggest that a 4-layer decoder outperforms both 2-layer and 6-layer ones on all tasks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Embodiment/environment | To further demonstrate the capability of PQ3D, we also transfer it to an embodied agent for object navigation using the ObjNav task from CortexBench [42] and instruction-tune it with a large language ... | hardware/simulator version and reset protocol | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | Notably, we combine eight datasets for training, including about 662K training samples for various tasks. | role, split, size and leakage | p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Metric | The proposed PQ3D provides global 3D features to the navigation agent that can improve the baseline VC-1 by a significant margin, achieving a 22.9% increase in success rate. | definition, denominator, direction and uncertainty | p. 11 (4 Experiments), p. 11 (Figure/Table caption), p. 12 (4 Experiments) |
| Baseline/ablation | On the ScanRefer, Nr3D, and Sr3D benchmarks, our model outperforms SOTA by 5.4%, 2.3%, and 3.3%, respectively. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 4 (Figure/Table caption), p. 10 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 4 Experiments - extractive body cue:** However, our model trained only on the Multi3DRefer dataset "PQ3D (sg.)" exhibits better performance in the ZT and MT metric, but falls short of the ...
- **p. 11 / 4 Experiments - extractive body cue:** As our model utilizes the CLIP text encoder, it may face limitations in understanding long sentences.
- **p. 10 / 4 Experiments - extractive body cue:** Different from 3D-VisTA, our model does not use a classification head for QA, which causes a performance drop in EM metric.
- **p. 14 / 4. Adjust the temperature or settings of the heater - extractive body cue:** 5 Conclusions and Future Works In conclusion, our proposed PQ3D addresses the challenges in 3D vision-language learning (3D-VL) by offering a unified approach that integrates ...
- **p. 9 / 4 Experiments - extractive body cue:** However, our model's performance with tail classes is relatively less robust due to biases in the CLIP text encoder, which is analyzed in the appendix.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Recent advancements in embodied artificial intelligence have emphasized the importance of connecting 3D scene understanding with natural language [16,27, 29, 44, 71].를 문제로 두고, In this section, we present PQ3D, which consists of three main modules: Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning, as depicted in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 7 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 8 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
