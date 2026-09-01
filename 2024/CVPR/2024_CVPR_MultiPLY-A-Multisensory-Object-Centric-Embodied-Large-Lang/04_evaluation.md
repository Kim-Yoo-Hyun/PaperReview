# Evaluation - MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.1. Object Retrieval), p. 8 (5.4. Task Decomposition), p. 8 (5.4. Task Decomposition), p. 7 (5.1. Object Retrieval), p. 7 (5.1. Object Retrieval), p. 6 (5.1. Object Retrieval)): The select action could be achieved by calculating the similarity between the object embedding and the language embedding, and the object with the highest score will be retrieved.

## Evaluation Body Digest

- **p. 3 / 3. The Multisensory-Universe Dataset - extractive PDF cue:** As presented in Figure 2, we begin by explaining how we input interactive objects into the scene to construct object-centric 3D scenes for our dataset ...
- **p. 3 / 3.1. Inputting Interactive Objects into 3D Scenes - extractive PDF cue:** We build our scenes on top of the Habitat-Matterport 3D (HM3D) semantics dataset [45, 62], which has 216 3D Context (Bounding box, material, temperature, hardness……): ...
- **p. 6 / 5. Experiments - extractive PDF cue:** We ensure that no scenes and objects in the Multisensory Universe appear in the evaluation setup.
- **p. 6 / 5.1. Object Retrieval - extractive PDF cue:** The scene setup is different from the Multisensory Universe as we place more distracting objects to retrieve from (while in Multisensory Universe most scenes have ...
- **p. 4 / 3.3. Embodied Agents for Data Collection - extractive PDF cue:** Then we place an embodied agent to interact with the objects in 3D environments to perform the task and collect interaction data.
- **p. 7 / 5.2. Tool Use - extractive PDF cue:** Similar to the object retrieval task, we place some objects from different categories, and also objects from the same categories but with different materials/haptic/thermal information ...
- **p. 8 / 5.4. Task Decomposition - extractive PDF cue:** In our setting, we place several possible choice combinations in the environment, we also place object combinations unseen from the Multisensory Universe.
- **p. 4 / 3.3. Embodied Agents for Data Collection - extractive PDF cue:** Inspired by [58], we utilize LLM-powered embodied agents to collect the data in the constructed scenes.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3. The Multisensory-Universe Dataset (p. 3); 5. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Object Retrieval | SYSTEM / EVALUATION SCOPE UNRESOLVED | The select action could be achieved by calculating the similarity between the object embedding and the language embedding, and the object with the highest ... | p. 6 (5.1. Object Retrieval) |
| 5.4. Task Decomposition | SYSTEM / EVALUATION SCOPE UNRESOLVED | Note that there is a domain gap between the task decomposition data 3D-LLM was trained on and our setting, which yields almost zero success ... | p. 8 (5.4. Task Decomposition) |
| 5.4. Task Decomposition | SYSTEM / EVALUATION SCOPE UNRESOLVED | For each baseline we have two variants: 1) wo Interaction: generate all actions all at once, and execute the actions sequentially in the environment; ... | p. 8 (5.4. Task Decomposition) |
| 5.1. Object Retrieval | SYSTEM / EVALUATION SCOPE UNRESOLVED | Third, LLMs outperform similarity-based retrieval models. | p. 7 (5.1. Object Retrieval) |
| 5.1. Object Retrieval | SYSTEM / EVALUATION SCOPE UNRESOLVED | In general, our MultiPLY outperforms the baseline models a lot. | p. 7 (5.1. Object Retrieval) |

## Dataset / Benchmark Role

- **p. 3 / 3. The Multisensory-Universe Dataset - extractive PDF cue:** As presented in Figure 2, we begin by explaining how we input interactive objects into the scene to construct object-centric 3D scenes for our dataset ...
- **p. 3 / 3.1. Inputting Interactive Objects into 3D Scenes - extractive PDF cue:** We build our scenes on top of the Habitat-Matterport 3D (HM3D) semantics dataset [45, 62], which has 216 3D Context (Bounding box, material, temperature, hardness……): ...
- **p. 6 / 5. Experiments - extractive PDF cue:** We ensure that no scenes and objects in the Multisensory Universe appear in the evaluation setup.
- **p. 6 / 5.1. Object Retrieval - extractive PDF cue:** The scene setup is different from the Multisensory Universe as we place more distracting objects to retrieve from (while in Multisensory Universe most scenes have ...
- **p. 4 / 3.3. Embodied Agents for Data Collection - extractive PDF cue:** Then we place an embodied agent to interact with the objects in 3D environments to perform the task and collect interaction data.
- **p. 7 / 5.2. Tool Use - extractive PDF cue:** Similar to the object retrieval task, we place some objects from different categories, and also objects from the same categories but with different materials/haptic/thermal information ...
- **p. 8 / 5.4. Task Decomposition - extractive PDF cue:** In our setting, we place several possible choice combinations in the environment, we also place object combinations unseen from the Multisensory Universe.
- **p. 4 / 3.3. Embodied Agents for Data Collection - extractive PDF cue:** Inspired by [58], we utilize LLM-powered embodied agents to collect the data in the constructed scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We propose MultiPLY, a multisensory embodied LLM that encodes object-centric multisensory representations (e.g., visual, audio, tactile, and thermal), by deploying an embodied agent ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Multisensory-Universe Generation Pipelines. We first add a set of new interactive objects in the embodied environments, then prompt ChatGPT to generate diverse tasks ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of our MultiPLY. We first encode the scene as an abstracted object-centric representation, while multisensory details of objects can only be unveiled ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Experimental Results of Object Retrieval. -I denotes the models utilize oracle action tokens to interact with the environ- ment. (Finetuned) means finetuned on ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Experimental Results of Tool Use.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Experimental Results of Multisensory Captioning. Analysis Table 3 shows the result. From the table, we could see that 3D-based LLMs overall outshine 2D ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative Examples of our MultiPLY. MultiPLY could interact with the objects in the embodied environments and gather multisensory information. able foods in the ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Experimental Results of Task Decomposition. Analysis Table 4 shows the task decomposition results. From the table, we observe that models without interaction have ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As presented in Figure 2, we begin by explaining how we input interactive objects into the scene to construct object-centric 3D scenes for our ... | embodiment, simulator version and control stack | p. 3 (3. The Multisensory-Universe Dataset), p. 3 (3.1. Inputting Interactive Objects into 3D Scenes) |
| Task/environment | We build our scenes on top of the Habitat-Matterport 3D (HM3D) semantics dataset [45, 62], which has 216 3D Context (Bounding box, material, temperature, ... | reset, timeout, object/scene variation | p. 3 (3.1. Inputting Interactive Objects into 3D Scenes), p. 6 (5. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (4.4. Training & Inference), p. 5 (4.2. Action Tokens) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Note that there is a domain gap between the task decomposition data 3D-LLM was trained on and our setting, which yields almost zero success ... | definition/direction/unit from same section | p. 8 (5.4. Task Decomposition) |
| For each baseline we have two variants: 1) wo Interaction: generate all actions all at once, and execute the actions sequentially in the environment; ... | definition/direction/unit from same section | p. 8 (5.4. Task Decomposition) |
| The embeddings of all sensors are averaged and calculate the similarities with the language query, and the object with the highest score is retrieved. | definition/direction/unit from same section | p. 6 (5.1. Object Retrieval) |
| The select action could be achieved by calculating the similarity between the object embedding and the language embedding, and the object with the highest ... | definition/direction/unit from same section | p. 6 (5.1. Object Retrieval) |
| CLIP, CLAP, as well as models that use the initial visual embeddings have a very low score in object retrieval, emphasizing the importance of ... | definition/direction/unit from same section | p. 7 (5.1. Object Retrieval) |
| Model Accuracy ConceptGraph+CLIP 10.1 ConceptGraph+ImageBind 7.4 ConceptGraph+ImageBind-I 8.2 ConceptGraph+ImageBind-I (Finetuned) 16.4 MultiPLY-2D 36.3 ConceptGraph+PointBind 11.5 ConceptGraph+PointBind-I 13.2 ConceptGraph+PointBind-I ... | definition/direction/unit from same section | p. 7 (5.2. Tool Use) |
| You need to generate a task in the scene. | definition/direction/unit from same section | p. 3 (3.1. Inputting Interactive Objects into 3D Scenes) |
| Demonstration: For Room 1: [Few shot example] Generate similar responses for Room 2. | definition/direction/unit from same section | p. 3 (3.1. Inputting Interactive Objects into 3D Scenes) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In general, our MultiPLY outperforms the baseline models a lot. | comparison identity and matched condition | p. 7 (5.1. Object Retrieval) |
| Since the action tokens are pre-defined and not generated, this oracle setting makes it easier to compete with MultiPLY. | comparison identity and matched condition | p. 6 (5.1. Object Retrieval) |
| Experimental Results of Object Retrieval. -I denotes the models utilize oracle action tokens to interact with the environment. | comparison identity and matched condition | p. 6 (5.1. Object Retrieval) |
| Third, LLMs outperform similarity-based retrieval models. | comparison identity and matched condition | p. 7 (5.1. Object Retrieval) |
| Therefore, we finetune all models as baselines. | comparison identity and matched condition | p. 8 (5.4. Task Decomposition) |
| Baselines We include LLaVA, a minimal 2D image version of our model. | comparison identity and matched condition | p. 8 (5.4. Task Decomposition) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also experiment with MultiPLY-2D, a 2D variant of our model, where we replace 3D features with 2D single-view features. | component/input/data sensitivity | p. 6 (5.1. Object Retrieval) |
| Due to space limits, we attach more ablative studies in the Supplementary Material, where we experiment with each possible combination of sensory inputs from ... | component/input/data sensitivity | p. 6 (5. Experiments) |
| From the table, we observe that models without interaction have very poor results, probably because vision-language models have hallucination to a great extent. | component/input/data sensitivity | p. 8 (5.4. Task Decomposition) |
| Note that there is a domain gap between the task decomposition data 3D-LLM was trained on and our setting, which yields almost zero success ... | component/input/data sensitivity | p. 8 (5.4. Task Decomposition) |
| For example, we could use a steel spoon to replace the can opener, but we can't use a plastic spoon. | component/input/data sensitivity | p. 7 (5.2. Tool Use) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected by an ... | The select action could be achieved by calculating the similarity between the object embedding and the language embedding, and the object with the highest ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.1. Object Retrieval), p. 8 (5.4. Task Decomposition), p. 8 (5.4. Task Decomposition), p. 7 (5.1. Object Retrieval), p. 7 (5.1. Object Retrieval), p. 6 (5.1. Object Retrieval) |
| Primary metric/result | Note that there is a domain gap between the task decomposition data 3D-LLM was trained on and our setting, which yields almost zero success ... | numeric claim only at cited anchor | p. 8 (5.4. Task Decomposition) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One limitation of our model is that currently MultiPLY does not involve detailed navigation and control policy, but utilizes pre-defined policies for carrying out ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | As these models cannot interact with the environment to get the tactile, impact sound, and temperature data, we refine three setups for the baselines: ... | p. 6 (5.1. Object Retrieval) |
| body limitation/failure cue | Second, 3Dbased models surpass 2D models, mainly because singleview images sometimes fail to provide enough information to reason about the objects due to view ... | p. 7 (5.1. Object Retrieval) |
| body limitation/failure cue | LLaVA and 3D-LLM take the holistic representation as inputs, and thus fail to compete with models that could interact with the models to switch ... | p. 7 (5.3. Multisensory Captioning) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Inference At the inference time, our MultiPLY first takes the task prompt and abstracted scene representation as inputs and generates subsequent tokens. | p. 6 (4.4. Training & Inference) |
| We freeze the weight of the image encoder and the LLM for faster convergence and maintenance of language reasoning abilities. | p. 5 (4.4. Training & Inference) |
| From one interaction, we could incrementally construct several input-output data, denoting the interaction at different steps, as shown in Figure 2. | p. 4 (3.3. Embodied Agents for Data Collection) |
| We first encode the scene as an abstracted object-centric representation, while multisensory details of objects can only be unveiled when the agent executes an ... | p. 5 (4.2. Action Tokens) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive PDF cue:** One limitation of our model is that currently MultiPLY does not involve detailed navigation and control policy, but utilizes pre-defined policies for carrying out the ...
- **p. 6 / 5.1. Object Retrieval - extractive PDF cue:** As these models cannot interact with the environment to get the tactile, impact sound, and temperature data, we refine three setups for the baselines: 1) ...
- **p. 7 / 5.1. Object Retrieval - extractive PDF cue:** Second, 3Dbased models surpass 2D models, mainly because singleview images sometimes fail to provide enough information to reason about the objects due to view inconsistency ...
- **p. 7 / 5.3. Multisensory Captioning - extractive PDF cue:** LLaVA and 3D-LLM take the holistic representation as inputs, and thus fail to compete with models that could interact with the models to switch between ...

- **PDF anchors reviewed:** datasets p. 3 (3. The Multisensory-Universe Dataset), p. 3 (3.1. Inputting Interactive Objects into 3D Scenes), p. 6 (5. Experiments), p. 6 (5.1. Object Retrieval), p. 4 (3.3. Embodied Agents for Data Collection), p. 7 (5.2. Tool Use), metrics p. 8 (5.4. Task Decomposition), p. 8 (5.4. Task Decomposition), p. 6 (5.1. Object Retrieval), p. 6 (5.1. Object Retrieval), p. 7 (5.1. Object Retrieval), p. 7 (5.2. Tool Use), baselines p. 7 (5.1. Object Retrieval), p. 6 (5.1. Object Retrieval), p. 6 (5.1. Object Retrieval), p. 7 (5.1. Object Retrieval), p. 8 (5.4. Task Decomposition), p. 8 (5.4. Task Decomposition), results p. 6 (5.1. Object Retrieval), p. 8 (5.4. Task Decomposition), p. 8 (5.4. Task Decomposition), p. 7 (5.1. Object Retrieval), p. 7 (5.1. Object Retrieval), p. 6 (5.1. Object Retrieval).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
