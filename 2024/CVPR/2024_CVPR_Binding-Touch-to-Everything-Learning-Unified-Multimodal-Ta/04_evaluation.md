# Evaluation - Binding Touch to Everything: Learning Unified Multimodal Tactile Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Binding_Touch_to_Everything_Learning_Unified_Multimodal_Tactile_Representations_CVPR_2024_paper.html; PDF retrieval source: https://arxiv.org/pdf/2401.18084. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Cross-modal retrieval with touch), p. 9 (Figure/Table caption), p. 6 (4.1. UniTouch representation), p. 8 (4.7. Ablation study), p. 8 (4.6. X-to-touch generation), p. 5 (4.1. UniTouch representation)): UniTouch achieves state-of-the-art performance on all three modalities and outperforms those supervised methods that are trained with paired modalities by a large Method LLM Eval GPT-4 Rating (↑) BLIP-2 [70] ...

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive body cue:** These include the real-world dataset Touch and Go [111], the robotic dataset Feeling of Success [6], the YCB-Slide [94] dataset featuring DIGIT sensor interactions, and ...
- **p. 5 / 4. Experiments - extractive body cue:** To test the generalization ability of our model, we also evaluate it with three out-of-domain datasets with two unseen sensors, including ObjectFolder Real [33], ObjectFolder ...
- **p. 6 / 4.1. UniTouch representation - extractive body cue:** We evaluate UniTouch on three datasets: Feeling of Success, ObjectFolder 2.0, and ObjectFolder 1.0, where ObjectFolder 1.0 is an out-of-domain dataset.
- **p. 6 / 4.2. Zero-shot touch understanding - extractive body cue:** This may come from the fact that we link the touch of the successful grasps to the robot's action of lifting objects while failed grasps ...
- **p. 7 / 4.3. Cross-modal retrieval with touch - extractive body cue:** We evaluate on ObjectFolder 2.0 cross-sensory retrieval benchmark [33].
- **p. 7 / 4.2. Zero-shot touch understanding - extractive body cue:** Our Touch-LLM can conduct a series of tactile question-answer tasks such as robot grasping stability prediction, contact localization, and touch image captioning.
- **p. 8 / 4.4. Image synthesis with touch - extractive body cue:** We evaluate our prompt designs for zero-shot material classification on Touch and Go and ObjectFolder 2.0 datasets. set.
- **p. 8 / 4.7. Ablation study - extractive body cue:** 8 ablates the importance of each module design on the zero-shot material classification task with the Touch and Go dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** 4. Experiments (p. 5); A.1. Datasets and Metrics (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Cross-modal retrieval with touch | EMPIRICAL / REAL-ROBOT OR HARDWARE | UniTouch achieves state-of-the-art performance on all three modalities and outperforms those supervised methods that are trained with paired modalities by a large Method LLM ... | p. 7 (4.3. Cross-modal retrieval with touch) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 8. Ablation study. We ablate the effectiveness of each of our proposed contributions via the zero-shot material classification. can significantly improve the performance, ... | p. 9 (Figure/Table caption) |
| 4.1. UniTouch representation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our performance consistently outperforms existing baselines by a large margin. | p. 6 (4.1. UniTouch representation) |
| 4.7. Ablation study | EMPIRICAL / REAL-ROBOT OR HARDWARE | We improve the performance by 17% by adding the sensor-specific tokens to it. | p. 8 (4.7. Ablation study) |
| 4.6. X-to-touch generation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our model achieves 55.3% consistency, illustrating the reliability of the generated results. | p. 8 (4.6. X-to-touch generation) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive body cue:** These include the real-world dataset Touch and Go [111], the robotic dataset Feeling of Success [6], the YCB-Slide [94] dataset featuring DIGIT sensor interactions, and ...
- **p. 5 / 4. Experiments - extractive body cue:** To test the generalization ability of our model, we also evaluate it with three out-of-domain datasets with two unseen sensors, including ObjectFolder Real [33], ObjectFolder ...
- **p. 6 / 4.1. UniTouch representation - extractive body cue:** We evaluate UniTouch on three datasets: Feeling of Success, ObjectFolder 2.0, and ObjectFolder 1.0, where ObjectFolder 1.0 is an out-of-domain dataset.
- **p. 6 / 4.2. Zero-shot touch understanding - extractive body cue:** This may come from the fact that we link the touch of the successful grasps to the robot's action of lifting objects while failed grasps ...
- **p. 7 / 4.3. Cross-modal retrieval with touch - extractive body cue:** We evaluate on ObjectFolder 2.0 cross-sensory retrieval benchmark [33].
- **p. 7 / 4.2. Zero-shot touch understanding - extractive body cue:** Our Touch-LLM can conduct a series of tactile question-answer tasks such as robot grasping stability prediction, contact localization, and touch image captioning.
- **p. 8 / 4.4. Image synthesis with touch - extractive body cue:** We evaluate our prompt designs for zero-shot material classification on Touch and Go and ObjectFolder 2.0 datasets. set.
- **p. 8 / 4.7. Ablation study - extractive body cue:** 8 ablates the importance of each module design on the zero-shot material classification task with the Touch and Go dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Putting touch "in touch" with other modalities. We show that a variety of tactile sensing tasks, ranging from touch image understanding to image ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Tactile images of different sensors and datasets. In contrast to many other modalities, signals from different touch sensing hardware exhibit large amounts of ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Method overview. We align our touch embedding with a pre-trained image embedding derived from large-scale vision lan- guage data, using sensor-specific tokens for ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Datasets for training and evaluation. nearest neighbor sensor-specific tokens from the learned sen- sor set {sk}N k=1. Specifically, we first compute a prototype ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Tactile material classification. We compare our touch features with other methods and ImageNet pretraining. We also report our zero-shot classification performance. The metric ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 3. Robotics grasping stability prediction. We compare our touch features with other methods and ImageNet pretraining on grasping stability prediction task. We report our ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Zero-shot image synthesis with touch. (Left) We generate an image of a scene given a tactile signal. (Right) We perform tactile-driven image stylization ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Cross-modal retrieval from touch. We evaluate the performance using mean Average Precision (mAP) on ObjectFolder 2.0. † denotes results from [33]. and sensors ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These include the real-world dataset Touch and Go [111], the robotic dataset Feeling of Success [6], the YCB-Slide [94] dataset featuring DIGIT sensor interactions, ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Task/environment | To test the generalization ability of our model, we also evaluate it with three out-of-domain datasets with two unseen sensors, including ObjectFolder Real [33], ... | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 6 (4.1. UniTouch representation) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 2 (1. Introduction) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate the performance using mean Average Precision (mAP) on ObjectFolder 2.0. † denotes results from [33]. and sensors validate our proposed sensor-specific tokens ... | definition/direction/unit from same section | p. 6 (4.1. UniTouch representation) |
| Following [6, 33, 111], we evaluate models' performance via accuracy metric for both downstream tasks. | definition/direction/unit from same section | p. 5 (4.1. UniTouch representation) |
| Class predictions are chosen based on highest scores, without training on labeled data. | definition/direction/unit from same section | p. 6 (4.2. Zero-shot touch understanding) |
| Despite a slightly lower FID score compared to [112], our method outperforms on the CVTP and material consistency metrics. | definition/direction/unit from same section | p. 8 (4.4. Image synthesis with touch) |
| Table 2. Tactile material classification. We compare our touch features with other methods and ImageNet pretraining. We also report our zero-shot classification performance. The ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| With our proposed batch sampling strategy and sensor-specific tokens, our model can achieve strong performance, surpassing the model trained on a single dataset, which ... | definition/direction/unit from same section | p. 8 (4.7. Ablation study) |
| Figure 6. Effect of σ for in-batch sampling. We compare the average zero-shot material classification accuracy from six datasets using different σ of 0, ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| We aim to generate images solely from touch. | definition/direction/unit from same section | p. 7 (4.4. Image synthesis with touch) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| UniTouch outperforms all the baselines by a large margin, implying that our tactile representations benefit from the alignment to a wellstructured embedding space trained ... | comparison identity and matched condition | p. 5 (4.1. UniTouch representation) |
| Our performance consistently outperforms existing baselines by a large margin. | comparison identity and matched condition | p. 6 (4.1. UniTouch representation) |
| UniTouch achieves state-of-the-art performance on all three modalities and outperforms those supervised methods that are trained with paired modalities by a large Method LLM ... | comparison identity and matched condition | p. 7 (4.3. Cross-modal retrieval with touch) |
| Despite a slightly lower FID score compared to [112], our method outperforms on the CVTP and material consistency metrics. | comparison identity and matched condition | p. 8 (4.4. Image synthesis with touch) |
| We compare our method to the state-of-the-art supervised diffusion method [112] trained on Touch and Go. | comparison identity and matched condition | p. 6 (4.1. UniTouch representation) |
| We evaluate our TouchLLM and three baselines on our test cases from Touch and Go [111]. | comparison identity and matched condition | p. 7 (4.3. Cross-modal retrieval with touch) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 8. Ablation study. We ablate the effectiveness of each of our proposed contributions via the zero-shot material classification. can significantly improve the performance, ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Figure 6. Effect of σ for in-batch sampling. We compare the average zero-shot material classification accuracy from six datasets using different σ of 0, ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Class predictions are chosen based on highest scores, without training on labeled data. | component/input/data sensitivity | p. 6 (4.2. Zero-shot touch understanding) |
| This demonstrates our strong cross-modal ability to align touch with other modalities without the need for explicit paired training data or additional supervision. | component/input/data sensitivity | p. 7 (4.3. Cross-modal retrieval with touch) |
| We use L = 5 learnable tokens for each sensor type in our pretraining datasets with K = 3 different sensors. | component/input/data sensitivity | p. 5 (4. Experiments) |
| We freeze the learned touch embeddings and train a linear classifier on the downstream tasks for specific datasets. | component/input/data sensitivity | p. 5 (4.1. UniTouch representation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| First, we present our contrastive visuo-tactile pretraining, inspired by [35], that can emerge interconnections of touch and other modalities. | UniTouch achieves state-of-the-art performance on all three modalities and outperforms those supervised methods that are trained with paired modalities by a large Method LLM ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Cross-modal retrieval with touch), p. 9 (Figure/Table caption), p. 6 (4.1. UniTouch representation), p. 8 (4.7. Ablation study), p. 8 (4.6. X-to-touch generation), p. 5 (4.1. UniTouch representation) |
| Primary metric/result | Table 8. Ablation study. We ablate the effectiveness of each of our proposed contributions via the zero-shot material classification. can significantly improve the performance, ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive body cue:** We train our model with a batch size of 48 on each of the 4 NVIDIA A40 GPUs for 150 epochs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Failures occur when the grasped object slips by more than 3cm. | p. 6 (4.1. UniTouch representation) |
| body limitation/failure cue | This may come from the fact that we link the touch of the successful grasps to the robot's action of lifting objects while failed ... | p. 6 (4.2. Zero-shot touch understanding) |
| body limitation/failure cue | Figure 8. More examples of zero-shot image synthesis with touch. (Left) We generate an image of a scene given a tactile signal. (Right) We ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | No, the object cannot be grasped into the air as the gripper is touching the object at the edge. | p. 7 (4.2. Zero-shot touch understanding) |
| body limitation/failure cue | Interpreting vision-based touch images, crucial for delicate tasks in fields like robotics, is challenging due to human perceptual limitations. | p. 8 (4.5. Touch-LLM) |
| body limitation/failure cue | We observe the supervised state-of-the-art method [112] fails to change the visual style according to the touch images even though these are seen during ... | p. 8 (4.4. Image synthesis with touch) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train our model with a batch size of 48 on each of the 4 NVIDIA A40 GPUs for 150 epochs. | p. 5 (4. Experiments) |
| We use the AdamW optimizer [58, 76] with the base learning rate of 1 × 10-5 and cosine decay learning rate scheduler. | p. 5 (4. Experiments) |
| Thus, we further demonstrate that our model design and training paradigm are useful not only in computer vision but also can be generalized to ... | p. 6 (4.1. UniTouch representation) |
| The baseline, a vanilla transformer model aligning touch embedding to a fixed vision encoder, drops performance significantly when applied to multiple sensors and datasets, ... | p. 8 (4.7. Ablation study) |
| We then introduce our touch encoder design and data sampling strategy that can be used for different tactile sensors at once. | p. 3 (3. Method) |
| Image Encoder Touch Encoder Contrastive loss Binding space L Sensor token Image Touch Frozen Trainable < GelSight > Figure 3. | p. 3 (3. Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. UniTouch representation - extractive body cue:** Failures occur when the grasped object slips by more than 3cm.
- **p. 6 / 4.2. Zero-shot touch understanding - extractive body cue:** This may come from the fact that we link the touch of the successful grasps to the robot's action of lifting objects while failed grasps ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 8. More examples of zero-shot image synthesis with touch. (Left) We generate an image of a scene given a tactile signal. (Right) We perform ...
- **p. 7 / 4.2. Zero-shot touch understanding - extractive body cue:** No, the object cannot be grasped into the air as the gripper is touching the object at the edge.
- **p. 8 / 4.5. Touch-LLM - extractive body cue:** Interpreting vision-based touch images, crucial for delicate tasks in fields like robotics, is challenging due to human perceptual limitations.
- **p. 8 / 4.4. Image synthesis with touch - extractive body cue:** We observe the supervised state-of-the-art method [112] fails to change the visual style according to the touch images even though these are seen during the ...

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.1. UniTouch representation), p. 6 (4.2. Zero-shot touch understanding), p. 7 (4.3. Cross-modal retrieval with touch), p. 7 (4.2. Zero-shot touch understanding), metrics p. 6 (4.1. UniTouch representation), p. 5 (4.1. UniTouch representation), p. 6 (4.2. Zero-shot touch understanding), p. 8 (4.4. Image synthesis with touch), p. 5 (Figure/Table caption), p. 8 (4.7. Ablation study), baselines p. 5 (4.1. UniTouch representation), p. 6 (4.1. UniTouch representation), p. 7 (4.3. Cross-modal retrieval with touch), p. 8 (4.4. Image synthesis with touch), p. 6 (4.1. UniTouch representation), p. 7 (4.3. Cross-modal retrieval with touch), results p. 7 (4.3. Cross-modal retrieval with touch), p. 9 (Figure/Table caption), p. 6 (4.1. UniTouch representation), p. 8 (4.7. Ablation study), p. 8 (4.6. X-to-touch generation), p. 5 (4.1. UniTouch representation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
