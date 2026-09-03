# Evaluation - Scalable Vision-Language-Action Model Pretraining for Robotic Dexterous Manipulation with Real-Life Human Activity Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2510.21571. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 15 (5 Experiments), p. 14 (5 Experiments), p. 15 (5 Experiments), p. 14 (5 Experiments), p. 10 (5 Experiments), p. 11 (5 Experiments)): By contrast, our approach achieves significantly better performance, benefiting from more explicit action supervision, which leads to a smaller pretraining-finetuning gap.

## Evaluation Body Digest

- **p. 9 / 5 Experiments - extractive body cue:** We compare our dataset with existing VLA datasets, including EgoDex [37], a human-hand VLA dataset of over 300K episodes collected in lab environments, and widely-used ...
- **p. 14 / 5 Experiments - extractive body cue:** Method Seen Object Average Pick & place Functional grasp Pour Sweep (40 trials) (24 trials) (8 trials) (8 trials) VPP 57.5 29.2 12.5 0.0 24.8 ...
- **p. 15 / 5 Experiments - extractive body cue:** The OXE dataset contains data from gripper-based robots and offers far less diversity in objects, tasks, and environments compared to our human hand VLA dataset, ...
- **p. 9 / 5 Experiments - extractive body cue:** Higher similarity values indicate that the dataset covers a larger portion of real-world scenes represented in OpenImages.
- **p. 10 / 5 Experiments - extractive body cue:** 5.2.1 Benchmark We construct a benchmark under unseen real-life environments, consisting of two task types defined below: Grasping We instruct the model to grasp objects ...
- **p. 10 / 5 Experiments - extractive body cue:** Moreover, our similarity increases more rapidly with the number of episodes (i.e., with a steeper slope), indicating a more uniform coverage of real-world scenes, in ...
- **p. 12 / 5 Experiments - extractive body cue:** We begin by describing the hardware system and the tasks defined for real-robot evaluation, followed by a detailed analysis of our model's performance and comparison ...
- **p. 12 / 5 Experiments - extractive body cue:** 5.3 Real-World Robot Dexterous Manipulation In this section, we evaluate the performance of our VLA model fine-tuned on a small set of real robot trajectories ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 Experiments (p. 8); A More Implementation Details (p. 24); B More Evaluation Details (p. 26); B.1 Hand Action Prediction Benchmark (p. 26); C More Results (p. 27); C.2 Hand Action Prediction Results (p. 27); C.3 Real-Robot Execution Results (p. 27).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | By contrast, our approach achieves significantly better performance, benefiting from more explicit action supervision, which leads to a smaller pretraining-finetuning gap. | p. 15 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For quantitative evaluation, we examine the model's performance in terms of task success rate and compare with prior methods. | p. 14 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Pretraining Hand-Prediction Accuracy Finally, we investigate the relationship between the fine-tuned robotic task success rates and the pretraining accuracy on human-hand prediction. | p. 15 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to the model without human VLA data pretraining, our approach achieves superior execution success and stronger generalization on unseen tasks. | p. 14 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our dataset achieves higher values on both metrics compared to the other datasets. | p. 10 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 5 Experiments - extractive body cue:** We compare our dataset with existing VLA datasets, including EgoDex [37], a human-hand VLA dataset of over 300K episodes collected in lab environments, and widely-used ...
- **p. 14 / 5 Experiments - extractive body cue:** Method Seen Object Average Pick & place Functional grasp Pour Sweep (40 trials) (24 trials) (8 trials) (8 trials) VPP 57.5 29.2 12.5 0.0 24.8 ...
- **p. 15 / 5 Experiments - extractive body cue:** The OXE dataset contains data from gripper-based robots and offers far less diversity in objects, tasks, and environments compared to our human hand VLA dataset, ...
- **p. 9 / 5 Experiments - extractive body cue:** Higher similarity values indicate that the dataset covers a larger portion of real-world scenes represented in OpenImages.
- **p. 10 / 5 Experiments - extractive body cue:** 5.2.1 Benchmark We construct a benchmark under unseen real-life environments, consisting of two task types defined below: Grasping We instruct the model to grasp objects ...
- **p. 10 / 5 Experiments - extractive body cue:** Moreover, our similarity increases more rapidly with the number of episodes (i.e., with a steeper slope), indicating a more uniform coverage of real-world scenes, in ...
- **p. 12 / 5 Experiments - extractive body cue:** We begin by describing the hardware system and the tasks defined for real-robot evaluation, followed by a detailed analysis of our model's performance and comparison ...
- **p. 12 / 5 Experiments - extractive body cue:** 5.3 Real-World Robot Dexterous Manipulation In this section, we evaluate the performance of our VLA model fine-tuned on a small set of real robot trajectories ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: We present a pretraining approach for robotic Vision-Language-Action (VLA) models by trans- forming unstructured real-life videos of human activity into structured V-L-A formats ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. 3.1 3D Motion Labeling The first stage of our approach extracts 3D motions from videos, including the motions of two hands and the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our holistic human activity analysis framework, which transforms unscripted real-life human videos into V-L-A episodes of human hands aligned with typical ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Our VLA model architecture. It consists of a VLM backbone and a diffusion action expert. The VLM receives visual and linguistic instructions, as ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Visual diversity across VLA datasets. (a) Image feature similarity with OpenImages [47] as the number of episodes varies. ⋆marks the full dataset's similarity. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Language instruction statistics across different VLA datasets. 5.1.1 Visual Diversity The diversity of visual observations and their coverage of natural scenes are crucial ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 6: Examples of environments used in hand action prediction evaluation. already surpasses that of the other datasets. In addition, the diversity of visual observations ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: Evaluation and ablation study of hand action prediction for the pretrained model. Note that Being-H0 [55] is a concurrent work to ours. See ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We compare our dataset with existing VLA datasets, including EgoDex [37], a human-hand VLA dataset of over 300K episodes collected in lab environments, and ... | embodiment, simulator version and control stack | p. 9 (5 Experiments), p. 14 (5 Experiments) |
| Task/environment | Method Seen Object Average Pick & place Functional grasp Pour Sweep (40 trials) (24 trials) (8 trials) (8 trials) VPP 57.5 29.2 12.5 0.0 ... | reset, timeout, object/scene variation | p. 14 (5 Experiments), p. 15 (5 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 6 (1 Introduction), p. 25 (A.3 Training Details) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 6 (1 Introduction), p. 7 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Pretraining Hand-Prediction Accuracy Finally, we investigate the relationship between the fine-tuned robotic task success rates and the pretraining accuracy on human-hand prediction. | definition/direction/unit from same section | p. 15 (5 Experiments) |
| Figure 10: Data scaling behavior on real-robot pick-and-place tasks. The circle size indicates the visual diversity of the pretraining data. (a) Task success rate ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| For quantitative evaluation, we examine the model's performance in terms of task success rate and compare with prior methods. | definition/direction/unit from same section | p. 14 (5 Experiments) |
| Method Seen Object Average Pick & place Functional grasp Pour Sweep (40 trials) (24 trials) (8 trials) (8 trials) VPP 57.5 29.2 12.5 0.0 ... | definition/direction/unit from same section | p. 14 (5 Experiments) |
| Method Grasp General action Avg./med. dhand-obj (cm) ↓ User Score ↑ Initial position 20.0 / 20.0 - Being-H0 (8B) 19.1 / 18.4 0.15 Ablations ... | definition/direction/unit from same section | p. 11 (5 Experiments) |
| These actions will be assigned 3, 2, and 1 scores while all others receive 0. | definition/direction/unit from same section | p. 11 (5 Experiments) |
| We examine how action prediction performance is influenced by key factors such as dataset composition, model architecture, training strategies, data construction strategies, and dataset ... | definition/direction/unit from same section | p. 10 (5 Experiments) |
| 5.3.2 Task Designs We collected 1.2K teleoperated trajectories for four tasks: i) General pick & place - moving an object into a box with ... | definition/direction/unit from same section | p. 13 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown, our method consistently outperforms all baselines. | comparison identity and matched condition | p. 11 (5 Experiments) |
| We compared with several baselines including a) Lab data, which replaces our VLA data with the EgoDex dataset captured in lab environments; b) Human ... | comparison identity and matched condition | p. 11 (5 Experiments) |
| Comparison of Pretraining Data To investigate the impact of different pretraining data on robot performance, we compare our method with several baselines: a) No ... | comparison identity and matched condition | p. 14 (5 Experiments) |
| We compare our method with two baselines that omit the use of 3D hand trajectory guidance during episode construction: a) Fixed-interval segmentation, which segments ... | comparison identity and matched condition | p. 12 (5 Experiments) |
| All baseline methods are fine-tuned using the same robot data collected in our study for a fair comparison. | comparison identity and matched condition | p. 14 (5 Experiments) |
| Our dataset achieves higher values on both metrics compared to the other datasets. | comparison identity and matched condition | p. 10 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also analyze the effect of different pretraining data and action representations, the data scaling behavior, and the relationship between robot performance and the ... | component/input/data sensitivity | p. 14 (5 Experiments) |
| Method Grasp General action Avg./med. dhand-obj (cm) ↓ User Score ↑ Initial position 20.0 / 20.0 - Being-H0 (8B) 19.1 / 18.4 0.15 Ablations ... | component/input/data sensitivity | p. 11 (5 Experiments) |
| Compared to the model without human VLA data pretraining, our approach achieves superior execution success and stronger generalization on unseen tasks. | component/input/data sensitivity | p. 14 (5 Experiments) |
| For this experiment, we compare with models pretrained on human-hand data using 50%, 20%, and 10% of the dataset (we do not include the ... | component/input/data sensitivity | p. 15 (5 Experiments) |
| Figure 1: We present a pretraining approach for robotic Vision-Language-Action (VLA) models by trans- forming unstructured real-life videos of human activity into structured V-L-A ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| 5.2.2 Performance Analysis Comparison of Pretraining Data We first compare the performance of models trained with different pretraining datasets to validate the effectiveness of ... | component/input/data sensitivity | p. 11 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Pretraining Unseen Object & BG Finetuning Pick up popcorn box Grasp whisk Grasp electric drill Pour into pot Sweep paper balls Pick up charger ... | By contrast, our approach achieves significantly better performance, benefiting from more explicit action supervision, which leads to a smaller pretraining-finetuning gap. | PDF body cue; verify exact table/figure and matched conditions | p. 15 (5 Experiments), p. 14 (5 Experiments), p. 15 (5 Experiments), p. 14 (5 Experiments), p. 10 (5 Experiments), p. 11 (5 Experiments) |
| Primary metric/result | For quantitative evaluation, we examine the model's performance in terms of task success rate and compare with prior methods. | numeric claim only at cited anchor | p. 14 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 5 Experiments - extractive body cue:** For fine-tuning on real robot data, we optimize the model for 20K steps with a batch size of 256 and a learning rate of 1e-5, ...
- **p. 10 / 5 Experiments - extractive body cue:** We capture RGB-D images from 47 unseen environments using Azure Kinect and annotate 396 objects with captions and segmented 3D point clouds.
- **p. 12 / 5 Experiments - extractive body cue:** 5.3.1 Robot Setup We use a Realman3 robot equipped with 12-DoF XHand4 dexterous hands and a RealSense head camera, as shown in Fig.
- **p. 13 / 5 Experiments - extractive body cue:** 5.3.2 Task Designs We collected 1.2K teleoperated trajectories for four tasks: i) General pick & place - moving an object into a box with 3-4 ...
- **p. 14 / 5 Experiments - extractive body cue:** Method Seen Object Average Pick & place Functional grasp Pour Sweep (40 trials) (24 trials) (8 trials) (8 trials) VPP 57.5 29.2 12.5 0.0 24.8 ...
- **p. 14 / 5 Experiments - extractive body cue:** Method Unseen Object & Background Unseen Category & Background Average Pick & place Functional grasp Pour Pick & place (16 trials) (16 trials) (8 trials) ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Moreover, it completely fails on unseen scenes, highlighting the importance of data diversity for generalization. | p. 15 (5 Experiments) |
| body limitation/failure cue | As shown, while latent action pretraining performs moderately on seen tasks, it fails completely in unseen environments. | p. 15 (5 Experiments) |
| body limitation/failure cue | While π0 is pretrained on large-scale robot data, its knowledge primarily targets gripper-based robots and does not transfer effectively to dexterous hands. | p. 14 (5 Experiments) |
| body limitation/failure cue | Figure 1: We present a pretraining approach for robotic Vision-Language-Action (VLA) models by trans- forming unstructured real-life videos of human activity into structured V-L-A ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 3: Our VLA model architecture. It consists of a VLM backbone and a diffusion action expert. The VLM receives visual and linguistic instructions, ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Using fixed-interval segmentation for constructing VLA episodes during pretraining results in degraded performance, as this approach can include multiple actions within a single clip, ... | p. 12 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For fine-tuning on real robot data, we optimize the model for 20K steps with a batch size of 256 and a learning rate of ... | p. 8 (5 Experiments) |
| The learning rates are 1e-4 and 1e-5 for the action expert and VLM, respectively, with a batch size of 512. | p. 8 (5 Experiments) |
| For other configurations, including ablations and prior methods, we select the best-performing checkpoint every 10K steps. | p. 25 (A.3 Training Details) |
| Specifically, we randomly sample 8K images from OpenImages as queries and extract their features using the DINOv2 [62] encoder. | p. 9 (5 Experiments) |
| For each query feature, we compute its maximum cosine similarity to our dataset, where the target features are extracted from the first frame of ... | p. 9 (5 Experiments) |
| We compute the minimum distance between predicted finger trajectories and target object points (i.e., dhand-obj) to evaluate movement plausibility. | p. 10 (5 Experiments) |
| Additionally, we compute the h-index and i100-index for the words, where the h-index represents the largest number h such that at least h words ... | p. 10 (5 Experiments) |
| We begin by describing the hardware system and the tasks defined for real-robot evaluation, followed by a detailed analysis of our model's performance and ... | p. 12 (5 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / 5 Experiments - extractive body cue:** Moreover, it completely fails on unseen scenes, highlighting the importance of data diversity for generalization.
- **p. 15 / 5 Experiments - extractive body cue:** As shown, while latent action pretraining performs moderately on seen tasks, it fails completely in unseen environments.
- **p. 14 / 5 Experiments - extractive body cue:** While π0 is pretrained on large-scale robot data, its knowledge primarily targets gripper-based robots and does not transfer effectively to dexterous hands.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: We present a pretraining approach for robotic Vision-Language-Action (VLA) models by trans- forming unstructured real-life videos of human activity into structured V-L-A formats ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Our VLA model architecture. It consists of a VLM backbone and a diffusion action expert. The VLM receives visual and linguistic instructions, as ...
- **p. 12 / 5 Experiments - extractive body cue:** Using fixed-interval segmentation for constructing VLA episodes during pretraining results in degraded performance, as this approach can include multiple actions within a single clip, thereby ...

- **Evidence anchors reviewed:** datasets p. 9 (5 Experiments), p. 14 (5 Experiments), p. 15 (5 Experiments), p. 9 (5 Experiments), p. 10 (5 Experiments), p. 10 (5 Experiments), metrics p. 15 (5 Experiments), p. 15 (Figure/Table caption), p. 14 (5 Experiments), p. 14 (5 Experiments), p. 11 (5 Experiments), p. 11 (5 Experiments), baselines p. 11 (5 Experiments), p. 11 (5 Experiments), p. 14 (5 Experiments), p. 12 (5 Experiments), p. 14 (5 Experiments), p. 10 (5 Experiments), results p. 15 (5 Experiments), p. 14 (5 Experiments), p. 15 (5 Experiments), p. 14 (5 Experiments), p. 10 (5 Experiments), p. 11 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
