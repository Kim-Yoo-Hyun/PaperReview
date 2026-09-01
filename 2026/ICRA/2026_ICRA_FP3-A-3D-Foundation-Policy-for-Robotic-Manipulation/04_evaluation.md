# Evaluation - FP3: A 3D Foundation Policy for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://2026.ieee-icra.org/awards/; PDF retrieval source: https://arxiv.org/pdf/2503.08950. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol), p. 7 (8 Training Scenes), p. 8 (8 Training Scenes), p. 4 (III. METHOD)): The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to the strong baselines.

## Evaluation Body Digest

- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** As we pre-train our FP3 model on the DROID dataset, we also build a real robot setup similar to DROID for evaluating downstream tasks.
- **p. 4 / III. METHOD - extractive PDF cue:** Different from the fine-tuning settings adopted in most existing robot foundation models in which they focus on either fine-tuning the model to adapt to new ...
- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** We further move the robot arm to novel environments and evaluate the policies with unseen objects.
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** More experiments on generalization Having demonstrated the efficient adaptation to new tasks and remarkable generalizability to novel objects and environments of FP3, we conduct more ...
- **p. 4 / III. METHOD - extractive PDF cue:** To build a 3D policy foundation model, we need to train our model on large-scale 3D robotic manipulation datasets.
- **p. 8 / V. LIMITATIONS - extractive PDF cue:** Future work can consider collecting larger 3D robotics datasets for pre-training.
- **p. 8 / V. LIMITATIONS - extractive PDF cue:** One possible reason is that the pre-training dataset DROID is still not large enough compared to other 2D robotics datasets like OXE.
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** We fine-tune FP3 and baseline methods on 80 demonstrations from 8 environments and evaluate them on four in-domain environments with seen objects and four in-the-wild ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4) Can FP3 correctly execute the corresponding tasks fol | EMPIRICAL / REAL-ROBOT OR HARDWARE | The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to the strong ... | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| 4) Can FP3 correctly execute the corresponding tasks fol | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results in Table I show that in in-domain experiments, with only 10 demonstrations per scene, DP and DP3 can somewhat handle easier tasks, even ... | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| 4) Can FP3 correctly execute the corresponding tasks fol | EMPIRICAL / REAL-ROBOT OR HARDWARE | FP3 significantly outperforms other policies both in domain and in the wild. | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| 8 Training Scenes | EMPIRICAL / REAL-ROBOT OR HARDWARE | FP3 achieves outstanding performance in all generalization evaluation settings. | p. 7 (8 Training Scenes) |
| 8 Training Scenes | EMPIRICAL / REAL-ROBOT OR HARDWARE | We achieve the best performance when using 3D point cloud input, a larger model, and largerscale pre-training data. | p. 8 (8 Training Scenes) |

## Dataset / Benchmark Role

- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** As we pre-train our FP3 model on the DROID dataset, we also build a real robot setup similar to DROID for evaluating downstream tasks.
- **p. 4 / III. METHOD - extractive PDF cue:** Different from the fine-tuning settings adopted in most existing robot foundation models in which they focus on either fine-tuning the model to adapt to new ...
- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** We further move the robot arm to novel environments and evaluate the policies with unseen objects.
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** More experiments on generalization Having demonstrated the efficient adaptation to new tasks and remarkable generalizability to novel objects and environments of FP3, we conduct more ...
- **p. 4 / III. METHOD - extractive PDF cue:** To build a 3D policy foundation model, we need to train our model on large-scale 3D robotic manipulation datasets.
- **p. 8 / V. LIMITATIONS - extractive PDF cue:** Future work can consider collecting larger 3D robotics datasets for pre-training.
- **p. 8 / V. LIMITATIONS - extractive PDF cue:** One possible reason is that the pre-training dataset DROID is still not large enough compared to other 2D robotics datasets like OXE.
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** We fine-tune FP3 and baseline methods on 80 demonstrations from 8 environments and evaluate them on four in-domain environments with seen objects and four in-the-wild ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of 3D Foundation Policy (FP3), a 1.3B 3D point cloud-based language-visuomotor policy pre-trained on 60k episodes from the DROID dataset [35]. FP3 ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: FP3 architecture. Each camera view's point cloud observation Pi t (with history length of two) is encoded with a Uni3D ViT-L [77] encoder. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: Task illustrations. We evaluate our model on four downstream tasks: Fold Towel, Clean Table, Stand up Cup, and Pour Water. Tasks. We choose ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visualizations of post-training environments and in-the-wild evaluations. The green boxes represent successful steps, while the red boxes represent failed ones. FP3 generalize well ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: Generalization evaluation. We evaluate FP3 and baseline policies on a diverse set of tasks, covering different axes of generalization, including lighting, camera view, ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 6: Instruction following evaluation. We evaluate FP3 and baseline policies in the same initial state with different language instructions. FP3 can perfectly follow the ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 8. We list the training hyperparameters for pre-training and fine-tuning in Table III and Table IV. We train all models on
- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 7: Scenes visualization of 8 post-training scenes and 4 unseen scenes for evaluation.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As we pre-train our FP3 model on the DROID dataset, we also build a real robot setup similar to DROID for evaluating downstream tasks. | embodiment, simulator version and control stack | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 4 (III. METHOD) |
| Task/environment | Different from the fine-tuning settings adopted in most existing robot foundation models in which they focus on either fine-tuning the model to adapt to ... | reset, timeout, object/scene variation | p. 4 (III. METHOD), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the success rate as our metric. | definition/direction/unit from same section | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| In contrast, thanks to pre-training and 3D representation, FP3 efficiently learns all tasks with a success rate exceeding 90%. | definition/direction/unit from same section | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| Once again, DP completely fails in this scenario, and DP3 is constrained by its in-domain performance, while FP3 maintains its high performance since the ... | definition/direction/unit from same section | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| FP3-Base and FP3-Base-30k demonstrate similar performance, both lower than our final FP3. | definition/direction/unit from same section | p. 8 (8 Training Scenes) |
| Fig. 1: Overview of 3D Foundation Policy (FP3), a 1.3B 3D point cloud-based language-visuomotor policy pre-trained on 60k episodes from the DROID dataset [35]. ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We use the AdamW optimizer [40] with a cosine learning rate schedule. | definition/direction/unit from same section | p. 4 (III. METHOD) |
| We then fine-tune the base model on this data using the parameter-efficient fine-tuning strategy LoRA [23]. | definition/direction/unit from same section | p. 4 (III. METHOD) |
| However, it is still limited by in-domain performance. | definition/direction/unit from same section | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to the strong ... | comparison identity and matched condition | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| In this challenging setting, we observe that all baseline policies without pre-training, including FP3-Scratch, often fail to recognize the target objects, resulting in near-zero ... | comparison identity and matched condition | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| FP3 significantly outperforms other policies both in domain and in the wild. | comparison identity and matched condition | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| With the benefits of pre-training initialization and 3D geometry understanding, FP3 surpasses the baselines. | comparison identity and matched condition | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| We evaluate FP3 and baseline policies on a diverse set of tasks, covering different axes of generalization, including lighting, camera view, distractor, object and ... | comparison identity and matched condition | p. 7 (8 Training Scenes) |
| We evaluate FP3 and baseline policies in the same initial state with different language instructions. | comparison identity and matched condition | p. 8 (8 Training Scenes) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first ... | component/input/data sensitivity | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| As we only care about the operated object, we cropped the points outside a 1-meter box to remove redundant points. | component/input/data sensitivity | p. 4 (III. METHOD) |
| Thanks to the effective initialization from pre-training, this small amount of fine-tuning data enables zero-shot deployment to novel environments and objects. | component/input/data sensitivity | p. 4 (III. METHOD) |
| In this challenging setting, we observe that all baseline policies without pre-training, including FP3-Scratch, often fail to recognize the target objects, resulting in near-zero ... | component/input/data sensitivity | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| Ablations We finally do ablation studies on the observation choice, model size, and pre-training data size. | component/input/data sensitivity | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| FP3 can perfectly follow the instructions to execute the correct tasks rather than simply memorize the training distribution. • FP3-Base-Image converts the point cloud ... | component/input/data sensitivity | p. 8 (8 Training Scenes) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong ... | The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to the strong ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol), p. 7 (8 Training Scenes), p. 8 (8 Training Scenes), p. 4 (III. METHOD) |
| Primary metric/result | Results in Table I show that in in-domain experiments, with only 10 demonstrations per scene, DP and DP3 can somewhat handle easier tasks, even ... | numeric claim only at cited anchor | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |

- Numeric sentences retained from the body:
- **p. 4 / III. METHOD - extractive PDF cue:** Pour the water in the bottle into the cup Language Instruction (𝑥, 𝑦, 𝑧, α, 𝛽, 𝛾, 𝑔) Proprioception States Uni3D ViT Uni3D ViT CLIP ...
- **p. 4 / III. METHOD - extractive PDF cue:** Thus, in this work, we pre-train FP3 with the DROID dataset [35], which includes 86 tasks and 76k demonstrations and provides depth observation data.
- **p. 4 / III. METHOD - extractive PDF cue:** Further, we downsample each point cloud by farthest point sampling (FPS, [48]) to 4000 points to facilitate model training while retaining sufficient information.
- **p. 4 / III. METHOD - extractive PDF cue:** The FP3 base model is pre-trained for 3M steps with a batch size of 128 using 8 NVIDIA A800 GPUs, which takes about 48 hours.
- **p. 4 / III. METHOD - extractive PDF cue:** Fine-tuning the same model on a single NVIDIA A800 GPU takes approximately 2 hours and can be further sped up with multi-GPU training.
- **p. 4 / III. METHOD - extractive PDF cue:** To handle the partial observation, we stack 2 frames as input, including 1 step observation history, to compensate for the missing dynamic information of the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first ... | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| body limitation/failure cue | While FP3 shows strong performance as a policy foundation model, it still has several limitations. | p. 8 (V. LIMITATIONS) |
| body limitation/failure cue | One limitation is that although FP3 enables efficient and generalizable downstream fine-tuning, the base model exhibits limited zero-shot performance. | p. 8 (V. LIMITATIONS) |
| body limitation/failure cue | Qualitatively, we find that the failures of all baseline algorithms are mainly due to issues in the details, such as not being precise enough ... | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| body limitation/failure cue | Another interesting issue is the policy's response after an initial failure attempt. | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |
| body limitation/failure cue | FP3 generalize well to all unseen environments and new objects, while Diffusion Policy often fails to recognize the target object or misses the target ... | p. 7 (8 Training Scenes) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The FP3 base model is pre-trained for 3M steps with a batch size of 128 using 8 NVIDIA A800 GPUs, which takes about 48 ... | p. 4 (III. METHOD) |
| The green boxes represent successful steps, while the red boxes represent failed ones. | p. 7 (8 Training Scenes) |
| FP3 can perfectly follow the instructions to execute the correct tasks rather than simply memorize the training distribution. • FP3-Base-Image converts the point cloud ... | p. 8 (8 Training Scenes) |
| We use the AdamW optimizer [40] with a cosine learning rate schedule. | p. 4 (III. METHOD) |
| FP3 is a 1.3B encoder-decoder transformer network following a two-stage pre-training and post-training recipe. | p. 3 (III. METHOD) |
| For the third-personview and the wrist-view point clouds, we use separate encoders since their point distributions might be greatly different. | p. 3 (III. METHOD) |
| Results in Table I are averaged over 20 evaluation trials. | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| In order to comprehensively evaluate FP3, we carefully select three baselines: • Diffusion Policy (DP) [12]: a classic diffusion-based imitation learning policy with 2D ... | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first failure, ...
- **p. 8 / V. LIMITATIONS - extractive PDF cue:** While FP3 shows strong performance as a policy foundation model, it still has several limitations.
- **p. 8 / V. LIMITATIONS - extractive PDF cue:** One limitation is that although FP3 enables efficient and generalizable downstream fine-tuning, the base model exhibits limited zero-shot performance.
- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** Qualitatively, we find that the failures of all baseline algorithms are mainly due to issues in the details, such as not being precise enough when ...
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive PDF cue:** Another interesting issue is the policy's response after an initial failure attempt.
- **p. 7 / 8 Training Scenes - extractive PDF cue:** FP3 generalize well to all unseen environments and new objects, while Diffusion Policy often fails to recognize the target object or misses the target position.

- **PDF anchors reviewed:** datasets p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 4 (III. METHOD), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol), p. 4 (III. METHOD), p. 8 (V. LIMITATIONS), metrics p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol), p. 8 (8 Training Scenes), p. 1 (Figure/Table caption), p. 4 (III. METHOD), baselines p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol), p. 7 (8 Training Scenes), p. 8 (8 Training Scenes), results p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol), p. 7 (8 Training Scenes), p. 8 (8 Training Scenes), p. 4 (III. METHOD).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
