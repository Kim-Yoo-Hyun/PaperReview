# Evaluation - ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Mzz4BhdIFb; PDF retrieval source: https://openreview.net/pdf/06fee7a1122ea26338330e0d4ace4117ec6c3ca6.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.3. Evaluation on Real-world Tasks), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 5 (5.1. Generalization Evaluation on Mixed-quality Data), p. 5 (5. Experiments), p. 3 (Figure/Table caption)): (b) Generalization comparison on simple and unseen tasks. shot learning and OOD generalization performance in realistic scenarios, and significantly outperforms the baseline methods.

## Evaluation Body Digest

- **p. 8 / 5.3. Evaluation on Real-world Tasks - extractive PDF cue:** Specifically, we consider the picking and placing tasks of objects such as cups, bowls, and stuffed toys on a robotic arm UR5.
- **p. 8 / 5.3. Evaluation on Real-world Tasks - extractive PDF cue:** For OOD generalization evaluation, we consider scenes with unseen instructions, backgrounds, distractors and manipulated objects (Fig.
- **p. 5 / 5. Experiments - extractive PDF cue:** In this section, we explore how the proposed ReinboT model can effectively implement the RL principle of maximizing return to enhance robotic vision-language manipulation tasks.
- **p. 5 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** This dataset contains a small amount of data with language instructions in CALVIN ABC (about 50 trajectories per task) and a large amount of autonomous ...
- **p. 6 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning Table 1.
- **p. 6 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** Generalization performance comparison of models trained on CALVIN mixed-quality data to test environment D.
- **p. 5 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** 1 shows the success rate of each language instruction in the chain and the Average Length (AL) of the completed tasks.
- **p. 5 / 5. Experiments - extractive PDF cue:** To this end, our experiments aim to investigate the following questions: 1) Does ReinboT show better generalization ability and higher success rate when performing long-horizon ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Generalization Evaluation on Mixed-quality Data (p. 5); 5.3. Evaluation on Real-world Tasks (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Evaluation on Real-world Tasks | EMPIRICAL / SOURCE-REPORTED EVALUATION | (b) Generalization comparison on simple and unseen tasks. shot learning and OOD generalization performance in realistic scenarios, and significantly outperforms the baseline methods. | p. 8 (5.3. Evaluation on Real-world Tasks) |
| 5.1. Generalization Evaluation on Mixed-quality Data | EMPIRICAL / SOURCE-REPORTED EVALUATION | For ReinboT and RWR, our dense reward improves performance better than sparse rewards. | p. 6 (5.1. Generalization Evaluation on Mixed-quality Data) |
| 5.1. Generalization Evaluation on Mixed-quality Data | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1 shows that among the models trained only on data with text annotations, PIDM integrates vision and action into a closed loop and achieves ... | p. 6 (5.1. Generalization Evaluation on Mixed-quality Data) |
| 5.1. Generalization Evaluation on Mixed-quality Data | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1 shows the success rate of each language instruction in the chain and the Average Length (AL) of the completed tasks. | p. 5 (5.1. Generalization Evaluation on Mixed-quality Data) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | To this end, our experiments aim to investigate the following questions: 1) Does ReinboT show better generalization ability and higher success rate when performing ... | p. 5 (5. Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 5.3. Evaluation on Real-world Tasks - extractive PDF cue:** Specifically, we consider the picking and placing tasks of objects such as cups, bowls, and stuffed toys on a robotic arm UR5.
- **p. 8 / 5.3. Evaluation on Real-world Tasks - extractive PDF cue:** For OOD generalization evaluation, we consider scenes with unseen instructions, backgrounds, distractors and manipulated objects (Fig.
- **p. 5 / 5. Experiments - extractive PDF cue:** In this section, we explore how the proposed ReinboT model can effectively implement the RL principle of maximizing return to enhance robotic vision-language manipulation tasks.
- **p. 5 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** This dataset contains a small amount of data with language instructions in CALVIN ABC (about 50 trajectories per task) and a large amount of autonomous ...
- **p. 6 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning Table 1.
- **p. 6 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** Generalization performance comparison of models trained on CALVIN mixed-quality data to test environment D.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1. The proposed ReinboT model. We leverage CLIP (Radford et al., 2021) to encode robot language instructions, utilize ViT (Dosovitskiy et al., 2020; He ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Generalization performance comparison of models trained on CALVIN mixed-quality data to test environment D. Algorithms No. of Instructions Chained Avg. Length (↑) 1 ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation experiments are conducted to verify the necessity of the designed reward components. No. of Instructions Chained Avg. Length (↑) 1 2 3 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 2. (a) Impact of different values of ReturnToGo LRTG loss weight λ. (b) Impact of different values of the expectile regression parameter m in ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. (a) Distribution of ground-truth ReturnToGo of CALVIN mixed-quality training data and distribution of the maximized ReturnToGo predicted by the ReinboT when interacting with ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Few-shot learning and OOD generalization evaluation scenarios for real-world tasks. Few-shot learning evaluation scenarios include cup grasping (a), bowl grasping and placing (b), ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Distribution of successful realistic trajectories.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. (a) Comparison of few-shot learning performance. (b) Generalization comparison on simple and unseen tasks. shot learning and OOD generalization performance in real- istic ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Specifically, we consider the picking and placing tasks of objects such as cups, bowls, and stuffed toys on a robotic arm UR5. | embodiment, simulator version and control stack | p. 8 (5.3. Evaluation on Real-world Tasks), p. 8 (5.3. Evaluation on Real-world Tasks) |
| Task/environment | For OOD generalization evaluation, we consider scenes with unseen instructions, backgrounds, distractors and manipulated objects (Fig. | reset, timeout, object/scene variation | p. 8 (5.3. Evaluation on Real-world Tasks), p. 5 (5. Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (4.2. End-to-end Reinforced VLA model), p. 2 (3.1. Imitation Learning of VLA Model) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1. Introduction), p. 3 (3.2. Max-Return Sequence Modeling) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 1 shows the success rate of each language instruction in the chain and the Average Length (AL) of the completed tasks. | definition/direction/unit from same section | p. 5 (5.1. Generalization Evaluation on Mixed-quality Data) |
| To this end, our experiments aim to investigate the following questions: 1) Does ReinboT show better generalization ability and higher success rate when performing ... | definition/direction/unit from same section | p. 5 (5. Experiments) |
| For ReinboT and RWR, our dense reward improves performance better than sparse rewards. | definition/direction/unit from same section | p. 6 (5.1. Generalization Evaluation on Mixed-quality Data) |
| The sub-goal division and dense reward examples of successful training data on real-world UR5 are in Appendix Fig. | definition/direction/unit from same section | p. 8 (5.3. Evaluation on Real-world Tasks) |
| The result shows that even if the training data are all successful trajectories, their quality distribution is still uneven under the dense reward metric ... | definition/direction/unit from same section | p. 8 (5.3. Evaluation on Real-world Tasks) |
| Figure 1. The proposed ReinboT model. We leverage CLIP (Radford et al., 2021) to encode robot language instructions, utilize ViT (Dosovitskiy et al., 2020; ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Ablation experiments are conducted to verify the necessity of the designed reward components. | definition/direction/unit from same section | p. 6 (5.1. Generalization Evaluation on Mixed-quality Data) |
| Figure 13. The dense reward and reward component of long-horizon tasks with language instructions of "Pick up the green cup for me" in the ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (b) Generalization comparison on simple and unseen tasks. shot learning and OOD generalization performance in realistic scenarios, and significantly outperforms the baseline methods. | comparison identity and matched condition | p. 8 (5.3. Evaluation on Real-world Tasks) |
| To this end, our experiments aim to investigate the following questions: 1) Does ReinboT show better generalization ability and higher success rate when performing ... | comparison identity and matched condition | p. 5 (5. Experiments) |
| We first construct a mixed-quality dataset based on CALVIN (Mees et al., 2022), which contains long-horizon manipulation tasks, to examine the performance of the ... | comparison identity and matched condition | p. 5 (5.1. Generalization Evaluation on Mixed-quality Data) |
| The baseline details are introduced in Appendix Sec. | comparison identity and matched condition | p. 6 (5.1. Generalization Evaluation on Mixed-quality Data) |
| 1 shows that among the models trained only on data with text annotations, PIDM integrates vision and action into a closed loop and achieves ... | comparison identity and matched condition | p. 6 (5.1. Generalization Evaluation on Mixed-quality Data) |
| The quantitative performance comparison of real-world tasks is in Fig. | comparison identity and matched condition | p. 8 (5.3. Evaluation on Real-world Tasks) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation experiments are conducted to verify the necessity of the designed reward components. | component/input/data sensitivity | p. 6 (5.1. Generalization Evaluation on Mixed-quality Data) |
| This dataset contains a small amount of data with language instructions in CALVIN ABC (about 50 trajectories per task) and a large amount of ... | component/input/data sensitivity | p. 5 (5.1. Generalization Evaluation on Mixed-quality Data) |
| In addition to the original data collected by human teleoperation without language instructions in CALVIN (more than 20,000 trajectories), the autonomous data also contains ... | component/input/data sensitivity | p. 5 (5.1. Generalization Evaluation on Mixed-quality Data) |
| Predicting each component of ReturnToGo can further improve the generalization ability of ReinboT (AL increased from 1.90 to 2.26). | component/input/data sensitivity | p. 6 (5.1. Generalization Evaluation on Mixed-quality Data) |
| Each task contains only 30 successful trajectories, and the model is fine-tuned on these three tasks. | component/input/data sensitivity | p. 8 (5.3. Evaluation on Real-world Tasks) |
| Figure 9. The dense reward and reward component of long-horizon tasks with language instructions of "slide the door to the left" in CALVIN mixed-quality ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, the core contributions of this paper include: • We propose ReinboT, a novel end-to-end VLA model that integrates RL returns maximization to enhance ... | (b) Generalization comparison on simple and unseen tasks. shot learning and OOD generalization performance in realistic scenarios, and significantly outperforms the baseline methods. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.3. Evaluation on Real-world Tasks), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 5 (5.1. Generalization Evaluation on Mixed-quality Data), p. 5 (5. Experiments), p. 3 (Figure/Table caption) |
| Primary metric/result | For ReinboT and RWR, our dense reward improves performance better than sparse rewards. | numeric claim only at cited anchor | p. 6 (5.1. Generalization Evaluation on Mixed-quality Data) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** This dataset contains a small amount of data with language instructions in CALVIN ABC (about 50 trajectories per task) and a large amount of autonomous ...
- **p. 5 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** In addition to the original data collected by human teleoperation without language instructions in CALVIN (more than 20,000 trajectories), the autonomous data also contains failure ...
- **p. 4 / 4.1. Reward Densification - extractive PDF cue:** Based on these four main factors, the general dense reward captures the nature of the long-horizon visual-language manipulation tasks is: r = 4 X i=1 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In addition to the original data collected by human teleoperation without language instructions in CALVIN (more than 20,000 trajectories), the autonomous data also contains ... | p. 5 (5.1. Generalization Evaluation on Mixed-quality Data) |
| body limitation/failure cue | To promote data diversity, different degrees of Gaussian noise (0.05, 0.1, and 0.15) are added to the actions of the RoboFlamingo policy model during ... | p. 5 (5.1. Generalization Evaluation on Mixed-quality Data) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The last layer of hidden features in ReturnToGo decoder is further utilized to predict robot actions. | p. 3 (3.2. Max-Return Sequence Modeling) |
| The dense reward in ReturnToGo contains four aspects: sub-goal achievement, task progress, behavior smoothness and task completion. where 1(·) is a binary indicator function, ... | p. 3 (3.2. Max-Return Sequence Modeling) |
| (11) The feature hRTG t:t+k-1 is then input into the ReturnToGo decoder Pφ to obtain the last layer of hidden features ˆghidden t:t+k-1: ˆghidden ... | p. 4 (4.2. End-to-end Reinforced VLA model) |
| We introduce action and image token embeddings ([ACTION] and [IMAGE]) and predict robot actions and future image states through an action decoder Pω and ... | p. 4 (4.2. End-to-end Reinforced VLA model) |
| The implementation details are in Appendix Sec. | p. 5 (4.2. End-to-end Reinforced VLA model) |
| ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning The hidden features ˆghidden t:t+k-1 is concatenated with the action features haction t:t+k-1 and are further ... | p. 5 (4.2. End-to-end Reinforced VLA model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** In addition to the original data collected by human teleoperation without language instructions in CALVIN (more than 20,000 trajectories), the autonomous data also contains failure ...
- **p. 5 / 5.1. Generalization Evaluation on Mixed-quality Data - extractive PDF cue:** To promote data diversity, different degrees of Gaussian noise (0.05, 0.1, and 0.15) are added to the actions of the RoboFlamingo policy model during the ...

- **PDF anchors reviewed:** datasets p. 8 (5.3. Evaluation on Real-world Tasks), p. 8 (5.3. Evaluation on Real-world Tasks), p. 5 (5. Experiments), p. 5 (5.1. Generalization Evaluation on Mixed-quality Data), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), metrics p. 5 (5.1. Generalization Evaluation on Mixed-quality Data), p. 5 (5. Experiments), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 8 (5.3. Evaluation on Real-world Tasks), p. 8 (5.3. Evaluation on Real-world Tasks), p. 3 (Figure/Table caption), baselines p. 8 (5.3. Evaluation on Real-world Tasks), p. 5 (5. Experiments), p. 5 (5.1. Generalization Evaluation on Mixed-quality Data), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 8 (5.3. Evaluation on Real-world Tasks), results p. 8 (5.3. Evaluation on Real-world Tasks), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 6 (5.1. Generalization Evaluation on Mixed-quality Data), p. 5 (5.1. Generalization Evaluation on Mixed-quality Data), p. 5 (5. Experiments), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
