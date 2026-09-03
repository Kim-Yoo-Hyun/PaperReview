# 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Scene Graph, LLM, Graph Reasoning
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing methods [7, 8, 22, 24] that use learnable 3D scene representations for vision-language tasks typically rely only on spatial coordinates and fail to incorporate semantic relationships between objects - limiting ...를 문제로 두고, To summarize, our contributions are as follows: • We introduce 3DGraphLLM, the first method for creating a learnable 3D scene graph representation specifically designed for LLMs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A 3D scene graph represents a compact scene model by capturing both the objects present and the semantic relationships between them, making it a promising ...
- **p. 1 / Abstract - extractive body cue:** To effectively interact with users, an embodied intelligent agent should be able to answer a wide range of natural language queries about the surrounding 3D ...
- **p. 1 / Abstract - extractive body cue:** Large Language Models (LLMs) are beneficial solutions for user-robot interaction due to their natural language understanding and reasoning abilities.
- **p. 1 / Abstract - extractive body cue:** Recent methods for learning scene representations have shown that adapting these representations to the 3D world can significantly improve the quality of LLM responses.
- **p. 1 / Abstract - extractive body cue:** However, existing methods typically rely only on geometric information, such as object coordinates, and overlook the rich semantic relationships between objects.
- **p. 2 / 1. Introduction - extractive body cue:** However, existing methods [7, 8, 22, 24] that use learnable 3D scene representations for vision-language tasks typically rely only on spatial coordinates and fail to ...
- **p. 1 / 1. Introduction - extractive body cue:** A common setup of this problem assumes access to a 3D reconstruction of the scene, such as a point cloud, mesh, or NeRF.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: • We introduce 3DGraphLLM, the first method for creating a learnable 3D scene graph representation specifically designed for ...
- **p. 2 / 1. Introduction - extractive body cue:** It enables semantic relationships between objects in a scene to be mapped directly into the LLM's token embedding space. • We propose an algorithm that ...
- **p. 3 / 3.1. Model Architecture - extractive body cue:** Thus, the set V of vertices of the graph consists of n point clouds {Pi}n i=1, where Pi ∈Rmi×6.
- **p. 3 / 3. Method - extractive body cue:** A scene graph consists of nodes representing the objects and edges corresponding to semantic relationships between them.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** We introduce trainable layers to map the extracted graph node and edge features into the token embedding space of a pre-trained LLM.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** To adapt the extracted features for the language model, we use three trainable projection modules: the 2D Object Projection f2d(·), which maps the 2D image ...
- **p. 4 / 3.1. Model Architecture - extractive body cue:** Therefore, we use latent features to capture possible combinations of these semantic relationships.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** These learned identifiers, with the features from object subgraphs composed of nearest neighbors for each object, are used to create a flat representation of the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our approach uses a set of point clouds of scene objects as input. | camera/depth stream, pose, map와 language goal | p. 3 (3. Method), p. 3 (3. Method) |
| State/latent | uses, point, clouds, scene, objects, input, obtained, either, ground-truth, annotations, through, state-of-the-art | robot pose, free-space/semantic map와 local goal | p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Model Architecture) |
| Output/action | The objects' point clouds can be obtained either from ground-truth annotations or through state-of-the-art point cloud instance segmentation methods. | collision-free trajectory 또는 velocity command | p. 3 (3. Method), p. 4 (3.1. Model Architecture), p. 1 (1. Introduction) |
| Objective/outcome | During training, we aim to optimize the trainable parameters θ of both the language model and the projection layers to minimize the negative log-likelihood of the target response sres compared to the ... | goal reach, safety, localization error와 replanning latency | p. 5 (3.3. Training Strategy), p. 5 (3.3. Training Strategy), p. 4 (3.1. Model Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: • We introduce 3DGraphLLM, the first method for creating a learnable 3D scene graph representation specifically designed for ...
- **p. 2 / 1. Introduction - extractive body cue:** It enables semantic relationships between objects in a scene to be mapped directly into the LLM's token embedding space. • We propose an algorithm that ...
- **p. 3 / 3.1. Model Architecture - extractive body cue:** Thus, the set V of vertices of the graph consists of n point clouds {Pi}n i=1, where Pi ∈Rmi×6.
- **p. 3 / 3. Method - extractive body cue:** A scene graph consists of nodes representing the objects and edges corresponding to semantic relationships between them.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** We introduce trainable layers to map the extracted graph node and edge features into the token embedding space of a pre-trained LLM.
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** 4, incorporating a scene graph representation significantly improves the performance of the LLMs across all three 3D Vision-Language tasks: visual grounding, scene description, and question ...
- **p. 6 / 4.1. Experimental Results - extractive body cue:** 2, our method significantly outperforms the baseline approach Chat-Scene [25] on the two ScanNet 3D referred object grounding benchmarks, ScanRefer [5] and Multi3DRefer [60], as ...
- **p. 6 / 4.1. Experimental Results - extractive body cue:** 3DGraphLLM achieves results comparable to the state-of-the-art method GPT4Scene8890

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.2. Ablation Studies), p. 6 (4.1. Experimental Results) |
| Embodiment/environment | For 3RScan scenes, we use data from the RioRefer dataset [36] for object grounding, and the 3RQA dataset [26] for question answering. | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Dataset/benchmark | 2, our method significantly outperforms the baseline approach Chat-Scene [25] on the two ScanNet 3D referred object grounding benchmarks, ScanRefer [5] and Multi3DRefer [60], as well as on the scene captioning benchmark ... | role, split, size and leakage | p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.1. Experimental Results), p. 6 (4. Experiments) |
| Metric | Therefore, we use the benchmark-standard F1 score at IoU thresholds of 0.25 and 0.5. | definition, denominator, direction and uncertainty | p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.2. Ablation Studies) |
| Baseline/ablation | 2, our method significantly outperforms the baseline approach Chat-Scene [25] on the two ScanNet 3D referred object grounding benchmarks, ScanRefer [5] and Multi3DRefer [60], as well as on the scene captioning benchmark ... | fair input/data/compute/action matching | p. 6 (4.1. Experimental Results), p. 6 (4.1. Experimental Results), p. 7 (4.2. Ablation Studies) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** A limitation of the method is a significant increase in resource consumption with an increase in the edge number for each graph node.
- **p. 6 / 4. Experiments - extractive body cue:** Our approach falls into the category of "LLM-based models" that consider different tasks as different user queries to a generative model.
- **p. 8 / 5. Conclusion - extractive body cue:** Another important aspect for further work is the creation of methods for generating semantic relations between objects that are robust to imperfections in the instance ...
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** It is worth noting that the n-gram-based evaluation metrics used in scene captioning and question answering benchmarks are not adequate for assessing the quality of ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing methods [7, 8, 22, 24] that use learnable 3D scene representations for vision-language tasks typically rely only on spatial coordinates and fail to incorporate semantic relationships between objects - limiting ...를 문제로 두고, To summarize, our contributions are as follows: • We introduce 3DGraphLLM, the first method for creating a learnable 3D scene graph representation specifically designed for LLMs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.1. Model Architecture), p. 4 (3.1. Model Architecture), p. 3 (3.1. Model Architecture), p. 3 (3.1. Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
