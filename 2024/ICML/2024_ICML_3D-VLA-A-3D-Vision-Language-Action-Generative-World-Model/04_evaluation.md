# Evaluation - 3D-VLA: A 3D Vision-Language-Action Generative World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://icml.cc/virtual/2024/poster/34575; PDF retrieval source: https://arxiv.org/pdf/2403.09631.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (5.1. 3D Reasoning and Localization), p. 3 (Figure/Table caption), p. 6 (5.1. 3D Reasoning and Localization), p. 7 (5.1. 3D Reasoning and Localization), p. 6 (Figure/Table caption)): Table 6. Evaluation of action planning on CALVIN dataset. matches the baseline performance in most tasks within the RLBench action prediction, showing its planning capability. It's worth noting that the ...

## Evaluation Body Digest

- **p. 6 / 5.1. 3D Reasoning and Localization - extractive body cue:** The tasks include 1) embodied QA on RoboVQA dataset (Sermanet et al., 2023); 2) task captioning on 11 Open-X datasets (Padalkar et al., 2023), where ...
- **p. 4 / 3.1. Dataset Collection - extractive body cue:** Human Object Interaction Datasets: Human/hand-object interactions could provide demonstrations that benefit robot decision-making and imitation.
- **p. 6 / 5.1. 3D Reasoning and Localization - extractive body cue:** We build several tasks on 3D embodied instruction tuning datasets for learning these abilities in the robotics domain.
- **p. 7 / 5.1. 3D Reasoning and Localization - extractive body cue:** Moreover, we find that 3D-LLM performs poorly on these robotic reasoning tasks, which demonstrates the necessity of collecting and training on a robotics-related 3D dataset.
- **p. 3 / 3. 3D Embodied Instruction Tuning Dataset - extractive body cue:** Similarly, million-level datasets comprising video-action pairs lay the foundation for embodied VLMs for robot control.
- **p. 4 / 3.2. Visual Annotations - extractive body cue:** The embodied datasets that serve as sources provide text instructions to describe the commands executed by the robots.
- **p. 7 / 5.2. Multi-modal Goal Generation - extractive body cue:** We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training process.
- **p. 3 / 3. 3D Embodied Instruction Tuning Dataset - extractive body cue:** Recently, benefiting from billion-scale datasets on the internet, VLMs have demonstrated exceptional proficiency in various tasks.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 3. 3D Embodied Instruction Tuning Dataset (p. 3); 3.1. Dataset Collection (p. 4); 5. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 6. Evaluation of action planning on CALVIN dataset. matches the baseline performance in most tasks within the RLBench action prediction, showing its planning ... | p. 8 (Figure/Table caption) |
| 5.1. 3D Reasoning and Localization | SYSTEM / EVALUATION SCOPE UNRESOLVED | In Tables 1, 3D-VLA outperforms all 2D VLM methods on language reasoning tasks. | p. 7 (5.1. 3D Reasoning and Localization) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2. Overview of our 3D-VLA pipeline. The left part shows our goal-generation capability. Our model can imagine the final state image and point ... | p. 3 (Figure/Table caption) |
| 5.1. 3D Reasoning and Localization | SYSTEM / EVALUATION SCOPE UNRESOLVED | Localization results on held-in robotics datasets. of interaction, which require a greater level of reasoning and localization abilities. | p. 6 (5.1. 3D Reasoning and Localization) |
| 5.1. 3D Reasoning and Localization | SYSTEM / EVALUATION SCOPE UNRESOLVED | RGB image goal generation results. ∗denotes the model is trained on our pretrained dataset. | p. 7 (5.1. 3D Reasoning and Localization) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. 3D Reasoning and Localization - extractive body cue:** The tasks include 1) embodied QA on RoboVQA dataset (Sermanet et al., 2023); 2) task captioning on 11 Open-X datasets (Padalkar et al., 2023), where ...
- **p. 4 / 3.1. Dataset Collection - extractive body cue:** Human Object Interaction Datasets: Human/hand-object interactions could provide demonstrations that benefit robot decision-making and imitation.
- **p. 6 / 5.1. 3D Reasoning and Localization - extractive body cue:** We build several tasks on 3D embodied instruction tuning datasets for learning these abilities in the robotics domain.
- **p. 7 / 5.1. 3D Reasoning and Localization - extractive body cue:** Moreover, we find that 3D-LLM performs poorly on these robotic reasoning tasks, which demonstrates the necessity of collecting and training on a robotics-related 3D dataset.
- **p. 3 / 3. 3D Embodied Instruction Tuning Dataset - extractive body cue:** Similarly, million-level datasets comprising video-action pairs lay the foundation for embodied VLMs for robot control.
- **p. 4 / 3.2. Visual Annotations - extractive body cue:** The embodied datasets that serve as sources provide text instructions to describe the commands executed by the robots.
- **p. 7 / 5.2. Multi-modal Goal Generation - extractive body cue:** We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training process.
- **p. 3 / 3. 3D Embodied Instruction Tuning Dataset - extractive body cue:** Recently, benefiting from billion-scale datasets on the internet, VLMs have demonstrated exceptional proficiency in various tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Examples from our 3D Embodied Instruction Tuning Dataset. added tokens enable our model to perform a wider range of embodied tasks and support ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of our 3D-VLA pipeline. The left part shows our goal-generation capability. Our model can imagine the final state image and point cloud ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Evaluation on reasoning ability using held-in data. ∗denotes zero-shot transfer results without training on our pre-train datasets. modal content to output. Between the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Localization results on held-in robotics datasets. of interaction, which require a greater level of reasoning and localization abilities. We build several tasks on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. RGB image goal generation results. ∗denotes the model is trained on our pretrained dataset. Models P-FID ↓ Chamfer-L1 ↓ Point-E∗ 5.241 0.159
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Point Cloud goal generation results. ∗denotes the model is trained on our pretrained dataset. X and RoboVQA dataset). For the localization task, we ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Visualization of generated RGB-D goal images. The results in the first row are sampled from the test set of held-in training data while ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Evaluation of action planning on RLBench dataset. we evaluate our model under the long-horizon multi-task language control setting, where the agent is required ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The tasks include 1) embodied QA on RoboVQA dataset (Sermanet et al., 2023); 2) task captioning on 11 Open-X datasets (Padalkar et al., 2023), ... | embodiment, simulator version and control stack | p. 6 (5.1. 3D Reasoning and Localization), p. 4 (3.1. Dataset Collection) |
| Task/environment | Human Object Interaction Datasets: Human/hand-object interactions could provide demonstrations that benefit robot decision-making and imitation. | reset, timeout, object/scene variation | p. 4 (3.1. Dataset Collection), p. 6 (5.1. 3D Reasoning and Localization) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (1. Introduction), p. 3 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS), p. 8 (5.3. Embodied Action Planning) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Table 2, 3D-VLA demonstrates a marked superiority over the 2D baseline methods in terms of localization performance. | definition/direction/unit from same section | p. 7 (5.1. 3D Reasoning and Localization) |
| 3D-VLA is a versatile 3D-based generative world model that can perform reasoning and grounding in the 3D world, imagine multi-modal goal content, and generate ... | definition/direction/unit from same section | p. 6 (5. Experiments) |
| We attribute it to the leverage of 3D information, which provides more accurate spatial information for reasoning. | definition/direction/unit from same section | p. 7 (5.1. 3D Reasoning and Localization) |
| Recently, benefiting from billion-scale datasets on the internet, VLMs have demonstrated exceptional proficiency in various tasks. | definition/direction/unit from same section | p. 3 (3. 3D Embodied Instruction Tuning Dataset) |
| Figure 2. Overview of our 3D-VLA pipeline. The left part shows our goal-generation capability. Our model can imagine the final state image and point ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Our data are curated from various sources. | definition/direction/unit from same section | p. 4 (3.1. Dataset Collection) |
| Optical flow aids in refining the data we generate. | definition/direction/unit from same section | p. 4 (3.2. Visual Annotations) |
| Figure 3. Visualization of generated RGB-D goal images. The results in the first row are sampled from the test set of held-in training data ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 2. Overview of our 3D-VLA pipeline. The left part shows our goal-generation capability. Our model can imagine the final state image and point ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| We implement these baselines in two ways: 1) zero-shot transfer where we test the released trained model on these new tasks; 2) held-in evaluation ... | comparison identity and matched condition | p. 6 (5.1. 3D Reasoning and Localization) |
| In Tables 1, 3D-VLA outperforms all 2D VLM methods on language reasoning tasks. | comparison identity and matched condition | p. 7 (5.1. 3D Reasoning and Localization) |
| In Table 2, 3D-VLA demonstrates a marked superiority over the 2D baseline methods in terms of localization performance. | comparison identity and matched condition | p. 7 (5.1. 3D Reasoning and Localization) |
| Table 5. Evaluation of action planning on RLBench dataset. we evaluate our model under the long-horizon multi-task language control setting, where the agent is ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 6. Evaluation of action planning on CALVIN dataset. matches the baseline performance in most tasks within the RLBench action prediction, showing its planning ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without 3D information, it is challenging for a robot to comprehend and execute the commands that require 3D spatial reasoning, such as "place the ... | component/input/data sensitivity | p. 3 (3. 3D Embodied Instruction Tuning Dataset) |
| For tasks without pre-defined templates, ChatGPT is also asked to generate prompts and answers as language inputs and outputs of these tasks by itself. | component/input/data sensitivity | p. 4 (3.3. Language Annotations) |
| Therefore, we utilize several human-object interaction datasets, including datasets without depth information, such as Epic-Kitchens (Damen et al., 2018), and datasets with better 3D ... | component/input/data sensitivity | p. 4 (3.1. Dataset Collection) |
| Table 1. Evaluation on reasoning ability using held-in data. ∗denotes zero-shot transfer results without training on our pre-train datasets. modal content to output. Between ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| RGB image goal generation results. ∗denotes the model is trained on our pretrained dataset. | component/input/data sensitivity | p. 7 (5.1. 3D Reasoning and Localization) |
| Figure 1. Examples from our 3D Embodied Instruction Tuning Dataset. added tokens enable our model to perform a wider range of embodied tasks and ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene. | Table 6. Evaluation of action planning on CALVIN dataset. matches the baseline performance in most tasks within the RLBench action prediction, showing its planning ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (5.1. 3D Reasoning and Localization), p. 3 (Figure/Table caption), p. 6 (5.1. 3D Reasoning and Localization), p. 7 (5.1. 3D Reasoning and Localization), p. 6 (Figure/Table caption) |
| Primary metric/result | In Tables 1, 3D-VLA outperforms all 2D VLM methods on language reasoning tasks. | numeric claim only at cited anchor | p. 7 (5.1. 3D Reasoning and Localization) |

- Numeric sentences retained from the body:
- **p. 7 / 5.2. Multi-modal Goal Generation - extractive body cue:** We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training process.
- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** The robot's actions, with 7 degrees of freedom, are represented by discrete tokens such as <aloc0-255>, <arot0-255>, and <gripper0/1> to denote the arm's intended absolute ...
- **p. 8 / 5.3. Embodied Action Planning - extractive body cue:** Evaluation of action planning on RLBench dataset. we evaluate our model under the long-horizon multi-task language control setting, where the agent is required to execute ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | FOR GOAL GENERATION To address the limitations of current diffusion models for goal generation in an embodied environment, we train RGBD to RGB-D and ... | p. 5 (4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS) |
| body limitation/failure cue | Thus, for video segments where the camera pose does not change, we use optical flow to estimate which pixels are the unmoved background. | p. 4 (3.2. Visual Annotations) |
| body limitation/failure cue | We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training process. | p. 7 (5.2. Multi-modal Goal Generation) |
| body limitation/failure cue | In these diverse and uncontrolled environments, our 3D-VLA model consistently and robustly demonstrated its efficacy. | p. 7 (3) LLMs with image generation ability NeXT-GPT (Wu) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| These tokens are intricately designed to inform the decoder about the type of 5 | p. 5 (4.3.2. BRIDGING LLM AND GOAL GENERATION) |
| Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene. | p. 5 (4.2.2. INTERACTION TOKENS) |
| Based on this, we can apply a transformer-based projector, which is capable of mapping the decoder features and embeddings from the Large Language Model ... | p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION) |
| For CALVIN, we compare with MCIL (Lynch & Sermanet, 2020), which is a conditional sequence-to-sequence variational autoencoder. | p. 8 (5.3. Embodied Action Planning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS - extractive body cue:** FOR GOAL GENERATION To address the limitations of current diffusion models for goal generation in an embodied environment, we train RGBD to RGB-D and point-cloud ...
- **p. 4 / 3.2. Visual Annotations - extractive body cue:** Thus, for video segments where the camera pose does not change, we use optical flow to estimate which pixels are the unmoved background.
- **p. 7 / 5.2. Multi-modal Goal Generation - extractive body cue:** We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training process.
- **p. 7 / 3) LLMs with image generation ability NeXT-GPT (Wu - extractive body cue:** In these diverse and uncontrolled environments, our 3D-VLA model consistently and robustly demonstrated its efficacy.

- **Evidence anchors reviewed:** datasets p. 6 (5.1. 3D Reasoning and Localization), p. 4 (3.1. Dataset Collection), p. 6 (5.1. 3D Reasoning and Localization), p. 7 (5.1. 3D Reasoning and Localization), p. 3 (3. 3D Embodied Instruction Tuning Dataset), p. 4 (3.2. Visual Annotations), metrics p. 7 (5.1. 3D Reasoning and Localization), p. 6 (5. Experiments), p. 7 (5.1. 3D Reasoning and Localization), p. 3 (3. 3D Embodied Instruction Tuning Dataset), p. 3 (Figure/Table caption), p. 4 (3.1. Dataset Collection), baselines p. 3 (Figure/Table caption), p. 6 (5.1. 3D Reasoning and Localization), p. 7 (5.1. 3D Reasoning and Localization), p. 7 (5.1. 3D Reasoning and Localization), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 7 (5.1. 3D Reasoning and Localization), p. 3 (Figure/Table caption), p. 6 (5.1. 3D Reasoning and Localization), p. 7 (5.1. 3D Reasoning and Localization), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
