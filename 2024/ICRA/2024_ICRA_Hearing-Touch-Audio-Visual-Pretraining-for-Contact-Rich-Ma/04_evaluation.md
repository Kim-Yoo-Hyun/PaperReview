# Evaluation - Hearing Touch: Audio-Visual Pretraining for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.08576; PDF retrieval source: https://arxiv.org/pdf/2405.08576. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (IV. EXPERIMENTS), p. 4 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS)): Flipping Scooping Zipping Success % Reward Success % Reward Success % Ours 50.0% 15.4 78.1% 8.9 88.9% BYOL-A 25.0% 2.3 25.0% 3.8 66.7% Scratch 15.4% 7.7 50.0% 6.9 72.2% Vision-Only ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** 2) Scaling Performance: We run evaluations on the scooping task for models trained with dataset sizes 50% (30 demos) and 150% (90 demos) of the ...
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** Tasks We present experiments on three real-world manipulation tasks, shown in Fig.
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** We address these questions through real-world experiments on our setup described in Section IV-A by evaluating across three tasks (Section IV-B) and four methods (Section ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Although BYOL-A includes an additional pre-training phase, the comparable performance with Scratch suggests that the augmentation techniques used by BYOL-A, while useful for learning audio ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For each method, we plot the projections of the embeddings from a sample trajectory over time for each variation of the flipping task, including both ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We evaluate the zero-shot transfer of frozen pre-trained audio representations (a), the effect of dataset size (b), the generalization ability of our method (c), and ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** 1) Qualitative Analysis: Many of the configurations of the task are difficult due to the noticeable visual differences between the train and test settings.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The selfattention mechanism for fusing audio and visual features is crucial to attaining good performance; both the success rate and the average reward drop by ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 3).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Flipping Scooping Zipping Success % Reward Success % Reward Success % Ours 50.0% 15.4 78.1% 8.9 88.9% BYOL-A 25.0% 2.3 25.0% 3.8 66.7% Scratch ... | p. 4 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 4: Success rates across methods and tasks. Our method, shown in blue, outperforms baselines in all but one setup of the zipping task. ... | p. 4 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that keeping the pre-trained audio encoder weights frozen during policy learning only slightly diminishes the performance of our method and still ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The selfattention mechanism for fusing audio and visual features is crucial to attaining good performance; both the success rate and the average reward drop ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | (a) Zero-Shot Transfer (b) Scaling Performance (c) Generalization (d) Architecture Ablation Fig. | p. 6 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** 2) Scaling Performance: We run evaluations on the scooping task for models trained with dataset sizes 50% (30 demos) and 150% (90 demos) of the ...
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** Tasks We present experiments on three real-world manipulation tasks, shown in Fig.
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** We address these questions through real-world experiments on our setup described in Section IV-A by evaluating across three tasks (Section IV-B) and four methods (Section ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Although BYOL-A includes an additional pre-training phase, the comparable performance with Scratch suggests that the augmentation techniques used by BYOL-A, while useful for learning audio ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For each method, we plot the projections of the embeddings from a sample trajectory over time for each variation of the flipping task, including both ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We evaluate the zero-shot transfer of frozen pre-trained audio representations (a), the effect of dataset size (b), the generalization ability of our method (c), and ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** 1) Qualitative Analysis: Many of the configurations of the task are difficult due to the noticeable visual differences between the train and test settings.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Hearing touch: We enable multisensory pretraining for manipulation by transferring audio-visual representations to manipulation tasks using vision and contact audio. over 2 million ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Two-stage model training. AVID and R3M pretraining leverages the large scale of internet video data (blue dashed box). We initialize the vision and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Hardware and task setup. We attach the Piezo contact microphones to our gripper to record vibrations in the form of audio and run ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Success rates across methods and tasks. Our method, shown in blue, outperforms baselines in all but one setup of the zipping task. Furthermore, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: t-SNE 2D projection. For comparative analysis of the learned embedding spaces, we visualize projections of the learned representations from each method in each ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Ablations. We evaluate the zero-shot transfer of frozen pre-trained audio representations (a), the effect of dataset size (b), the generalization ability of our ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 2) Scaling Performance: We run evaluations on the scooping task for models trained with dataset sizes 50% (30 demos) and 150% (90 demos) of ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS) |
| Task/environment | Tasks We present experiments on three real-world manipulation tasks, shown in Fig. | reset, timeout, object/scene variation | p. 3 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The selfattention mechanism for fusing audio and visual features is crucial to attaining good performance; both the success rate and the average reward drop ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Our TABLE I: Rewards and success rates across tasks. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Flipping Scooping Zipping Success % Reward Success % Reward Success % Ours 50.0% 15.4 78.1% 8.9 88.9% BYOL-A 25.0% 2.3 25.0% 3.8 66.7% Scratch ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| The success rate of both methods is closer under the train settings, with our method performing 10% better. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| We normalize the audio waveforms and generate mel spectrograms of the 2s audio segment following the audio preprocessing in [14]. | definition/direction/unit from same section | p. 3 (IV. EXPERIMENTS) |
| The zipping task demonstrates the contact microphone's abilities to directly record vibrations touching the gripper, while the flipping and scooping tasks show their ability ... | definition/direction/unit from same section | p. 3 (IV. EXPERIMENTS) |
| (a) Zero-Shot Transfer (b) Scaling Performance (c) Generalization (d) Architecture Ablation Fig. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method, shown in blue, outperforms baselines in all but one setup of the zipping task. | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| Further, our method outperforms or matches the performance of all baselines in 8/9 tasks, displaying a lower variation in performance between different configurations of ... | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| The results show that keeping the pre-trained audio encoder weights frozen during policy learning only slightly diminishes the performance of our method and still ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| 3) Generalization: To further investigate the poor performance of the Vision-Only baseline in comparison to our method on the flipping task, we compare the ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| (a) Zero-Shot Transfer (b) Scaling Performance (c) Generalization (d) Architecture Ablation Fig. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Fig. 6: Ablations. We evaluate the zero-shot transfer of frozen pre-trained audio representations (a), the effect of dataset size (b), the generalization ability of ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 6: Ablations. We evaluate the zero-shot transfer of frozen pre-trained audio representations (a), the effect of dataset size (b), the generalization ability of ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| We use different methods of pretraining in order to measure the effect of large-scale audio-visual pretraining on learning a useful contact audio representation for ... | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |
| 4) Architecture Ablation: We replace the transformer with an MLP including an added additional linear layer to ensure the resultant network has approximately the ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| This baseline compares the effect of large-scale audio-visual pre-training to in-domain audio pre-training, with an emphasis on the amount of pre-training data. | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |
| Ablation Studies 1) Zero-Shot Transfer: To get a better sense of how relevant pre-trained AVID weights are to downstream manipulation tasks, we train a ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| (a) Zero-Shot Transfer (b) Scaling Performance (c) Generalization (d) Architecture Ablation Fig. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset ... | Flipping Scooping Zipping Success % Reward Success % Reward Success % Ours 50.0% 15.4 78.1% 8.9 88.9% BYOL-A 25.0% 2.3 25.0% 3.8 66.7% Scratch ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (IV. EXPERIMENTS), p. 4 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Primary metric/result | Fig. 4: Success rates across methods and tasks. Our method, shown in blue, outperforms baselines in all but one setup of the zipping task. ... | numeric claim only at cited anchor | p. 4 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** The end effector actions are commanded at 30 Hz.
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** We use an Intel D435 RealSense camera with a fixed third-person view to collect image observations at 30 Hz. b) Data Collection: Demonstrations are collected ...
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** The visual data collected by the Intel D435 RealSense camera collects images with a resolution of 480×640.
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** We normalize the audio waveforms and generate mel spectrograms of the 2s audio segment following the audio preprocessing in [14].
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Further, our method outperforms or matches the performance of all baselines in 8/9 tasks, displaying a lower variation in performance between different configurations of each ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations for manipulation policies. | p. 6 (V. CONCLUSION) |
| body limitation/failure cue | As a result, the baselines suffer heavily from the domain shift and fail to generalize, often moving in jerk motions or away from the ... | p. 4 (IV. EXPERIMENTS) |
| body limitation/failure cue | Further, our method outperforms or matches the performance of all baselines in 8/9 tasks, displaying a lower variation in performance between different configurations of ... | p. 4 (IV. EXPERIMENTS) |
| body limitation/failure cue | Despite having access to the same information as our method, the BYOL-A and Scratch baselines fail to reason effectively over the audio and utilize ... | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | This is more like the behavior of the training data than the baselines, which often fail to begin digging the spoon into the material ... | p. 5 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| (a) Hardware Setup (b) Flipping task (c) Scooping task (d) Zipping task Fig. | p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Following [40], we keep both encoders unfrozen, continuing to update the weights during policy learning. | p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Baselines and Implementation Details We conduct experiments with our method and three other baselines. | p. 4 (IV. EXPERIMENTS) |
| This baseline tests whether the signal from contact microphones is beneficial in our setup. • Scratch: a baseline with randomly initialized weights for the ... | p. 4 (IV. EXPERIMENTS) |
| 2) Scaling Performance: We run evaluations on the scooping task for models trained with dataset sizes 50% (30 demos) and 150% (90 demos) of ... | p. 5 (IV. EXPERIMENTS) |
| The results show that keeping the pre-trained audio encoder weights frozen during policy learning only slightly diminishes the performance of our method and still ... | p. 5 (IV. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. CONCLUSION - extractive body cue:** Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations for manipulation policies.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** As a result, the baselines suffer heavily from the domain shift and fail to generalize, often moving in jerk motions or away from the object ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Further, our method outperforms or matches the performance of all baselines in 8/9 tasks, displaying a lower variation in performance between different configurations of each ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Despite having access to the same information as our method, the BYOL-A and Scratch baselines fail to reason effectively over the audio and utilize the ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** This is more like the behavior of the training data than the baselines, which often fail to begin digging the spoon into the material as ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), baselines p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), results p. 4 (IV. EXPERIMENTS), p. 4 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
