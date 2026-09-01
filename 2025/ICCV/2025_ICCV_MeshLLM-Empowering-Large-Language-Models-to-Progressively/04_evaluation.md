# Evaluation - MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Performance Evaluation), p. 7 (4.3. Performance Evaluation), p. 8 (4.4. Ablation Studies), p. 6 (4.2. Dialogue Ability), p. 6 (4.1. Implementation Details), p. 8 (4.4. Ablation Studies)): 1, reveal that our method surpasses LLaMA-Mesh on multiple metrics and achieves a performance comparable to that of MeshXL, thereby validating the effectiveness of our Primitive-Mesh construction strategy and training ...

## Evaluation Body Digest

- **p. 5 / 4.1. Implementation Details - extractive PDF cue:** We follow dataset split configurations from previous works [8, 49], extracting 10% of the 4 subsets (chair, table, bench, lamp) from ShapeNet and 1K samples ...
- **p. 5 / 4.1. Implementation Details - extractive PDF cue:** We train for 2 epochs on the KNN-based Primitive-Mesh dataset, 3 epochs on the se14065
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** Additionally, to mitigate catastrophic forgetting and retain the LLM's conversational capabilities, we randomly sample the data from the previous phase and ultra-chat dataset [17] with ...
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** This expansion enables MeshLLM to understand and generate 3D meshes through natural and intuitive language interactions, further solidifying LLMs as versatile and powerful tools. mantic ...
- **p. 8 / 4.4. Ablation Studies - extractive PDF cue:** The primary ablation settings include: 1) KNN-based Primitive-Mesh: This design is critical for constructing a large-scale usable dataset.
- **p. 7 / 4.3. Performance Evaluation - extractive PDF cue:** The improvement primarily stems from the finer-grained semantic information embedded in Primitive-Meshes, as well as the mesh assembly task, which reinforces the connection between local ...
- **p. 7 / 4.3. Performance Evaluation - extractive PDF cue:** It is worth noting that while MeshXL and PolyGen excel in mesh generation tasks, neither possesses mesh understanding or interactive dialogue capabilities, which are unique ...
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** For the mesh understanding task, we use the BLEU-1 [51], CIDEr [63], METEOR [16], and ROUGE [40] metrics to evaluate the accuracy of the generated ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experimental Results (p. 5); 4.1. Implementation Details (p. 5); 4.3. Performance Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Performance Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, reveal that our method surpasses LLaMA-Mesh on multiple metrics and achieves a performance comparable to that of MeshXL, thereby validating the effectiveness of ... | p. 7 (4.3. Performance Evaluation) |
| 4.3. Performance Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | MeshLLM generates 3D meshes with clean geometric details, outperforming the LLMbased LLaMA-Mesh and achieving performance comparable to Polygen and MeshXL, which are specifically designed ... | p. 7 (4.3. Performance Evaluation) |
| 4.4. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Excluding it results in a slight reduction in mesh generation quality and a marked degradation in mesh understanding performance. | p. 8 (4.4. Ablation Studies) |
| 4.2. Dialogue Ability | EMPIRICAL / SOURCE-REPORTED EVALUATION | These findings demonstrate that our approach successfully integrates text-serialized 3D information into LLMs. | p. 6 (4.2. Dialogue Ability) |
| 4.1. Implementation Details | EMPIRICAL / SOURCE-REPORTED EVALUATION | For the mesh understanding task, we use the BLEU-1 [51], CIDEr [63], METEOR [16], and ROUGE [40] metrics to evaluate the accuracy of the ... | p. 6 (4.1. Implementation Details) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Implementation Details - extractive PDF cue:** We follow dataset split configurations from previous works [8, 49], extracting 10% of the 4 subsets (chair, table, bench, lamp) from ShapeNet and 1K samples ...
- **p. 5 / 4.1. Implementation Details - extractive PDF cue:** We train for 2 epochs on the KNN-based Primitive-Mesh dataset, 3 epochs on the se14065
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** Additionally, to mitigate catastrophic forgetting and retain the LLM's conversational capabilities, we randomly sample the data from the previous phase and ultra-chat dataset [17] with ...
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** This expansion enables MeshLLM to understand and generate 3D meshes through natural and intuitive language interactions, further solidifying LLMs as versatile and powerful tools. mantic ...
- **p. 8 / 4.4. Ablation Studies - extractive PDF cue:** The primary ablation settings include: 1) KNN-based Primitive-Mesh: This design is critical for constructing a large-scale usable dataset.
- **p. 7 / 4.3. Performance Evaluation - extractive PDF cue:** The improvement primarily stems from the finer-grained semantic information embedded in Primitive-Meshes, as well as the mesh assembly task, which reinforces the connection between local ...
- **p. 7 / 4.3. Performance Evaluation - extractive PDF cue:** It is worth noting that while MeshXL and PolyGen excel in mesh generation tasks, neither possesses mesh understanding or interactive dialogue capabilities, which are unique ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We propose MeshLLM, a method for effectively injecting text-serialized meshes into large language models, enabling the understanding and generation of 3D mesh through ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Differences between LLaMA-Mesh and MeshLLM. LLaMA-Mesh applies a single text-mesh alignment optimization strategy on only 31k available meshes. In contrast, our proposed MeshLLM ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Illustration of Primitive-Mesh. We utilize both KNN clustering and semantic segmentation to partition meshes into Primitive-Meshes that retain local structural information. This strategy ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Illustration of the MeshLLM framework. We adopt a progressive training process: Stage 1: Training on Primitive-Meshes obtained through KNN clustering, where two tasks ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 5. Example of the constructed SFT data for training LLM. then apply farthest point sampling (FPS) and KNN to iden- tify central points and ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Gallery results. MeshLLM demonstrates an ability to generate diverse and high-quality meshes. Mesh Understanding. Given a mesh M and its textual de- scription ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7. Dialogue results. MeshLLM extends the capabilities of LLMs to the domain of 3D mesh while retaining their advanced dialogue abilities, such as question-answering ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 8. Comparisons on the mesh generation. MeshLLM generates 3D meshes with clean geometric details, outperforming the LLM- based LLaMA-Mesh and achieving performance comparable to ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We follow dataset split configurations from previous works [8, 49], extracting 10% of the 4 subsets (chair, table, bench, lamp) from ShapeNet and 1K ... | embodiment, simulator version and control stack | p. 5 (4.1. Implementation Details), p. 5 (4.1. Implementation Details) |
| Task/environment | We train for 2 epochs on the KNN-based Primitive-Mesh dataset, 3 epochs on the se14065 | reset, timeout, object/scene variation | p. 5 (4.1. Implementation Details), p. 6 (4.1. Implementation Details) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Primitive-Mesh), p. 5 (3.4. SFT Data Curation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.2. Primitive-Mesh), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For the mesh understanding task, we use the BLEU-1 [51], CIDEr [63], METEOR [16], and ROUGE [40] metrics to evaluate the accuracy of the ... | definition/direction/unit from same section | p. 6 (4.1. Implementation Details) |
| These metrics include Minimum Matching Distance (MMD, lower is better), Coverage (COV, higher is better), and 1-Nearest Neighbor Accuracy (1-NNA, the optimal value is ... | definition/direction/unit from same section | p. 6 (4.1. Implementation Details) |
| 1, reveal that our method surpasses LLaMA-Mesh on multiple metrics and achieves a performance comparable to that of MeshXL, thereby validating the effectiveness of ... | definition/direction/unit from same section | p. 7 (4.3. Performance Evaluation) |
| MeshLLM generates 3D meshes with clean geometric details, outperforming the LLMbased LLaMA-Mesh and achieving performance comparable to Polygen and MeshXL, which are specifically designed ... | definition/direction/unit from same section | p. 7 (4.3. Performance Evaluation) |
| Figure 2. Differences between LLaMA-Mesh and MeshLLM. LLaMA-Mesh applies a single text-mesh alignment optimization strategy on only 31k available meshes. In contrast, our proposed ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We employ the AdamW optimizer with a learning rate of 2e-5 and set the maximum context length to 8192. | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |
| We then generate semantic-level Primitive-Meshes on this subset using the SamPart3D method [70], yielding over 100k+ semantic-level Primitive-Meshes. | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |
| Ablating this component also leads to a pronounced performance decrease. | definition/direction/unit from same section | p. 8 (4.4. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We further compare it with state-of-the-art methods in Fig. | comparison identity and matched condition | p. 6 (4.3. Performance Evaluation) |
| The most directly related baseline to our approach is LLaMAMesh [64]. | comparison identity and matched condition | p. 6 (4.1. Implementation Details) |
| Moreover, when compared with methods specifically designed for mesh generation like PolyGen and MeshXL, the overall performance of MeshLLM is comparable. | comparison identity and matched condition | p. 7 (4.3. Performance Evaluation) |
| The generated descriptions are fluent and accurate and effectively reflect the structural characteristics of the meshes, which significantly surpass the LLaMA-Mesh baseline. | comparison identity and matched condition | p. 7 (4.3. Performance Evaluation) |
| Quantitative comparisons of mesh quality. | comparison identity and matched condition | p. 8 (4.3. Performance Evaluation) |
| Ablation studies of MeshLLM. "PM" denotes PrimitiveMesh. | comparison identity and matched condition | p. 8 (4.3. Performance Evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In particular, the constructed data sets and training pipeline are fully compatible with any existing LLM without necessitating additional complex encoder-decoder designs. | component/input/data sensitivity | p. 6 (4.2. Dialogue Ability) |
| Ablation studies of MeshLLM. "PM" denotes PrimitiveMesh. | component/input/data sensitivity | p. 8 (4.3. Performance Evaluation) |
| We conduct a series of ablation experiments, the results of which are summarized in Tab. | component/input/data sensitivity | p. 8 (4.4. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of our work are as follows: • We introduce a mesh decomposition strategy to create 1500k+ Primitive-Meshes, expanding the scale of ... | 1, reveal that our method surpasses LLaMA-Mesh on multiple metrics and achieves a performance comparable to that of MeshXL, thereby validating the effectiveness of ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Performance Evaluation), p. 7 (4.3. Performance Evaluation), p. 8 (4.4. Ablation Studies), p. 6 (4.2. Dialogue Ability), p. 6 (4.1. Implementation Details), p. 8 (4.4. Ablation Studies) |
| Primary metric/result | MeshLLM generates 3D meshes with clean geometric details, outperforming the LLMbased LLaMA-Mesh and achieving performance comparable to Polygen and MeshXL, which are specifically designed ... | numeric claim only at cited anchor | p. 7 (4.3. Performance Evaluation) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Implementation Details - extractive PDF cue:** We train for 2 epochs on the KNN-based Primitive-Mesh dataset, 3 epochs on the se14065
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** Could you tell me what x is when 2x=4?
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** So, 2x divided by 2 is equal to 4 divided by 2.
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** You can subtract 1 from both sides of the equation, which gives you 2x=3.
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** This expansion enables MeshLLM to understand and generate 3D meshes through natural and intuitive language interactions, further solidifying LLMs as versatile and powerful tools. mantic ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, highlighting future research areas: 1) The scale of ... | p. 8 (5. Limitation and Future Work) |
| body limitation/failure cue | In this paper, we propose MeshLLM, a novel approach that rethinks the paradigm of generating text-serialized meshes using Large Language Models, which addresses two ... | p. 8 (6. Conclusions) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We employ the AdamW optimizer with a learning rate of 2e-5 and set the maximum context length to 8192. | p. 5 (4.1. Implementation Details) |
| We train for 2 epochs on the KNN-based Primitive-Mesh dataset, 3 epochs on the se14065 | p. 5 (4.1. Implementation Details) |
| In particular, the constructed data sets and training pipeline are fully compatible with any existing LLM without necessitating additional complex encoder-decoder designs. | p. 6 (4.2. Dialogue Ability) |
| In addition, we render 8 different images of the meshes and compute the CLIP similarity [55] between these images and the text to assess ... | p. 6 (4.1. Implementation Details) |
| MeshLLM surpasses the same-type method LLaMA-Mesh and is comparable to encoder-based MeshXL. | p. 8 (4.3. Performance Evaluation) |
| The mesh is textualized through the following steps: 1) Quantization: The coordinate values of the mesh vertices are mapped to the integer values in ... | p. 3 (3. Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Limitation and Future Work - extractive PDF cue:** While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, highlighting future research areas: 1) The scale of available ...
- **p. 8 / 6. Conclusions - extractive PDF cue:** In this paper, we propose MeshLLM, a novel approach that rethinks the paradigm of generating text-serialized meshes using Large Language Models, which addresses two key ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Implementation Details), p. 5 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 8 (4.4. Ablation Studies), p. 7 (4.3. Performance Evaluation), metrics p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 7 (4.3. Performance Evaluation), p. 7 (4.3. Performance Evaluation), p. 2 (Figure/Table caption), p. 5 (4.1. Implementation Details), baselines p. 6 (4.3. Performance Evaluation), p. 6 (4.1. Implementation Details), p. 7 (4.3. Performance Evaluation), p. 7 (4.3. Performance Evaluation), p. 8 (4.3. Performance Evaluation), p. 8 (4.3. Performance Evaluation), results p. 7 (4.3. Performance Evaluation), p. 7 (4.3. Performance Evaluation), p. 8 (4.4. Ablation Studies), p. 6 (4.2. Dialogue Ability), p. 6 (4.1. Implementation Details), p. 8 (4.4. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
