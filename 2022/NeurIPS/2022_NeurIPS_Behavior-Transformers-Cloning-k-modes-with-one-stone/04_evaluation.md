# Evaluation - Behavior Transformers: Cloning k modes with one stone

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Figure/Table caption), p. 6 (3 Experiments), p. 6 (3 Experiments), p. 8 (3 Experiments), p. 8 (3 Experiments), p. 5 (3 Experiments)): Figure 1: Unconditional rollouts from BeT models trained from multi-modal demonstartions on the CARLA, Block push, and Franka Kitchen environments. Due to the multi-modal architecture of BeT, even in the ...

## Evaluation Body Digest

- **p. 5 / 3 Experiments - extractive body cue:** 3.1 Environments and datasets We experiment with five broad environments.
- **p. 5 / 3 Experiments - extractive body cue:** While full descriptions of these environments, dataset creation procedure, and overall statistics are in Appendix A, a brief description of them are as follows.
- **p. 6 / 3 Experiments - extractive body cue:** We use the relay policy learning dataset with 566 demonstrations collected by human participants wearing VR headsets.
- **p. 6 / 3 Experiments - extractive body cue:** This dataset contains two different kinds of multi-modality: one from the inherent noise in human demonstrations, and another from the demonstrators' intent.
- **p. 7 / 3 Experiments - extractive body cue:** Next, we examine the question of whether, given a dataset where multi-modal behavior exists, our model learns behavior that is also multi-modal.
- **p. 9 / 3 Experiments - extractive body cue:** Our models contain on the order of 104-106 parameters, and even with a small batch size trains within an hour for our largest datasets (Block ...
- **p. 7 / 3 Experiments - extractive body cue:** In each of our environments, the demonstrations contain different types of multi-modality.
- **p. 8 / 3 Experiments - extractive body cue:** 4 that BeT visits certain strings of tasks more frequently than in the original demonstrations.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 3 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1: Unconditional rollouts from BeT models trained from multi-modal demonstartions on the CARLA, Block push, and Franka Kitchen environments. Due to the multi-modal ... | p. 2 (Figure/Table caption) |
| 3 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We see that BeT outperforms all other methods in all environments except CARLA, where it is narrowly outperformed by LWR. | p. 6 (3 Experiments) |
| 3 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | While IBC is slower than explicit BC models because of their sampling requirements, they have been shown to learn well on multi-modal data, and ... | p. 6 (3 Experiments) |
| 3 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | This result shows us that having discrete bins helps BeT achieve multi-modality. | p. 8 (3 Experiments) |
| 3 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Indeed, if there is no binning, we see from Table 3 that the performance of BeT drops significantly. | p. 8 (3 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 3 Experiments - extractive body cue:** 3.1 Environments and datasets We experiment with five broad environments.
- **p. 5 / 3 Experiments - extractive body cue:** While full descriptions of these environments, dataset creation procedure, and overall statistics are in Appendix A, a brief description of them are as follows.
- **p. 6 / 3 Experiments - extractive body cue:** We use the relay policy learning dataset with 566 demonstrations collected by human participants wearing VR headsets.
- **p. 6 / 3 Experiments - extractive body cue:** This dataset contains two different kinds of multi-modality: one from the inherent noise in human demonstrations, and another from the demonstrators' intent.
- **p. 7 / 3 Experiments - extractive body cue:** Next, we examine the question of whether, given a dataset where multi-modal behavior exists, our model learns behavior that is also multi-modal.
- **p. 9 / 3 Experiments - extractive body cue:** Our models contain on the order of 104-106 parameters, and even with a small batch size trains within an hour for our largest datasets (Block ...
- **p. 7 / 3 Experiments - extractive body cue:** In each of our environments, the demonstrations contain different types of multi-modality.
- **p. 8 / 3 Experiments - extractive body cue:** 4 that BeT visits certain strings of tasks more frequently than in the original demonstrations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Unconditional rollouts from BeT models trained from multi-modal demonstartions on the CARLA, Block push, and Franka Kitchen environments. Due to the multi-modal architecture ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Comparison between a regular MSE-based BC model and a BeT models that can capture multi-modal distributions. The MSE-BC model takes 0 action to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Architecture of Behavior Transformer. (A) The continuous action binning using k-means algorithm that lets BeT split every action into a discrete bin and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance of BeT compared with different baselines in learning from demonstrations. For CARLA, we measure the probability of the car reaching the goal ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Distribution of most frequent tasks completed in sequence in the Kitchen environment. Each task is colored differently, and frequency is shown out of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Multimodality learned from the multimodal demonstrations by different algorithms. In CARLA, we consider the probability of turning left vs. right at the intersection, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparison between an RBC model and two BeT models, trained with and without historical context on a dataset with three distinct modes. BeT ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Relative performance of ablated variants of BeT, normalized by average BeT successes at the task Ablations CARLA Block push Kitchen No offsets 0.94

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3.1 Environments and datasets We experiment with five broad environments. | embodiment, simulator version and control stack | p. 5 (3 Experiments), p. 5 (3 Experiments) |
| Task/environment | While full descriptions of these environments, dataset creation procedure, and overall statistics are in Appendix A, a brief description of them are as follows. | reset, timeout, object/scene variation | p. 5 (3 Experiments), p. 6 (3 Experiments) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 5 (1 Introduction) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 1 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Reward is normalized with respect to the best performing model. | definition/direction/unit from same section | p. 9 (3 Experiments) |
| Intuitively, we can understand how in higher dimension the loss of fidelity from discretizing would be higher, and the relative performance loss across three ... | definition/direction/unit from same section | p. 8 (3 Experiments) |
| We now study the empirical performance of BeT on a variety of behavior learning tasks. | definition/direction/unit from same section | p. 5 (3 Experiments) |
| The agent action space is 2D (accelerate/brake and left/right steer), while the observation space is (224,224,3)-dimensional RGB image from the car. | definition/direction/unit from same section | p. 5 (3 Experiments) |
| To examine that, we look at the performance of our model in CARLA, Block push, and Kitchen environments compared with our baselines in Table ... | definition/direction/unit from same section | p. 6 (3 Experiments) |
| While all baselines can somewhat successfully reach one block, they fail to complete the long-horizon, multi-modal task of pushing two blocks into two different ... | definition/direction/unit from same section | p. 6 (3 Experiments) |
| For CARLA, we measure the probability of the car reaching the goal successfully. | definition/direction/unit from same section | p. 7 (3 Experiments) |
| Here, we are interested in seeing the variance of the behavior of the model over different rollouts. | definition/direction/unit from same section | p. 7 (3 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5: Comparison between an RBC model and two BeT models, trained with and without historical context on a dataset with three distinct modes. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| To examine that, we look at the performance of our model in CARLA, Block push, and Kitchen environments compared with our baselines in Table ... | comparison identity and matched condition | p. 6 (3 Experiments) |
| We see that BeT outperforms all other methods in all environments except CARLA, where it is narrowly outperformed by LWR. | comparison identity and matched condition | p. 6 (3 Experiments) |
| CARLA Block: first block reached Push: red block target Push: green block target Kitchen Baselines Left Right Red Green Red Green Red Green Task ... | comparison identity and matched condition | p. 7 (3 Experiments) |
| CARLA Block push Kitchen Driving Reach Push # Tasks completed Baselines Success R1 R2 P1 P2 1 2 3 4 5 RBC 0.98 0.67 ... | comparison identity and matched condition | p. 7 (3 Experiments) |
| In contrast, for the same task, our strongest baseline IBC takes about 14 hours. | comparison identity and matched condition | p. 9 (3 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3: Relative performance of ablated variants of BeT, normalized by average BeT successes at the task Ablations CARLA Block push Kitchen No offsets ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 5: Comparison between an RBC model and two BeT models, trained with and without historical context on a dataset with three distinct modes. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| (c) How important are the individual components of BeT? | component/input/data sensitivity | p. 5 (3 Experiments) |
| For visual observations with BeT, we use a frozen ResNet-18 [36] pretrained on ImageNet [18] as an encoder. | component/input/data sensitivity | p. 5 (3 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we present Behavior Transformers (BeT), a new method for learning behaviors from rich, distributionally multi-modal data. | Figure 1: Unconditional rollouts from BeT models trained from multi-modal demonstartions on the CARLA, Block push, and Franka Kitchen environments. Due to the multi-modal ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Figure/Table caption), p. 6 (3 Experiments), p. 6 (3 Experiments), p. 8 (3 Experiments), p. 8 (3 Experiments), p. 5 (3 Experiments) |
| Primary metric/result | We see that BeT outperforms all other methods in all environments except CARLA, where it is narrowly outperformed by LWR. | numeric claim only at cited anchor | p. 6 (3 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 3 Experiments - extractive body cue:** Evaluations are over 100 rollouts in CARLA and 1,000 rollouts in Block push and Kitchen environments.
- **p. 9 / 3 Experiments - extractive body cue:** Our models contain on the order of 104-106 parameters, and even with a small batch size trains within an hour for our largest datasets (Block ...
- **p. 9 / 3 Experiments - extractive body cue:** In contrast, for the same task, our strongest baseline IBC takes about 14 hours.
- **p. 2 / 1 Introduction - extractive body cue:** Rollout 1 Start Reach red Push red to red Reach green Push green to green Start Push red to green Push green to red Reach ...
- **p. 4 / 1 Introduction - extractive body cue:** k means Continuous action dataset (/A/ x a) Clustering into k bins Action offset (1 x a) Continuous action (1 x a) Categorical action bin ...
- **p. 4 / 1 Introduction - extractive body cue:** Continuous action binning MinGPT Observation Sequence 0.4 0.1 0.0 0.5 0.0 Per-class action offsets (k x a) Bin probs (1 x k) Ground truth action ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Since the models are all behavioral cloning algorithms, they share the failure mode of failing once the observations go out of distribution (OOD). | p. 6 (3 Experiments) |
| body limitation/failure cue | On the other hand, we observe that BeT's primary failure mode is not realizing a block has not completely entered the target yet, while ... | p. 6 (3 Experiments) |
| body limitation/failure cue | Figure 2: Comparison between a regular MSE-based BC model and a BeT models that can capture multi-modal distributions. The MSE-BC model takes 0 action ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | We see that they may perform well sometimes but overall still fall short of our k-means binning approach. | p. 8 (3 Experiments) |
| body limitation/failure cue | BeT falls under the second category, as it is a behavior cloning model. | p. 9 (4 Related Work) |
| body limitation/failure cue | We see in Table 2 that in CARLA and Block push, BeT covers all the modes of the demonstration data, even in the few ... | p. 8 (3 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our models contain on the order of 104-106 parameters, and even with a small batch size trains within an hour for our largest datasets ... | p. 9 (3 Experiments) |
| For visual observations with BeT, we use a frozen ResNet-18 [36] pretrained on ImageNet [18] as an encoder. | p. 5 (3 Experiments) |
| (d) Variational auto-encoders (VAE): Inspired by SPiRL [66], where behavioral priors are learned through a VAE [42], we compare with continuous actions generated from ... | p. 6 (3 Experiments) |
| For Kitchen, we measure the probability of n tasks being completed by the model within the allotted 280 timesteps. | p. 7 (3 Experiments) |
| In our experiments, we also pick a k in the right neighborhood and only run a sweep at the very end to find out ... | p. 9 (3 Experiments) |
| While behavior learning has made impressive progress in recent times, it lags behind computer vision and natural language processing due to its inability to ... | p. 1 (Abstract) |
| All of our datasets, code, and trained models will be made publicly available. | p. 3 (1 Introduction) |
| We use a transformer decoder model, namely minGPT [11], with minor modifications, as our backbone. | p. 4 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 3 Experiments - extractive body cue:** Since the models are all behavioral cloning algorithms, they share the failure mode of failing once the observations go out of distribution (OOD).
- **p. 6 / 3 Experiments - extractive body cue:** On the other hand, we observe that BeT's primary failure mode is not realizing a block has not completely entered the target yet, while other ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Comparison between a regular MSE-based BC model and a BeT models that can capture multi-modal distributions. The MSE-BC model takes 0 action to ...
- **p. 8 / 3 Experiments - extractive body cue:** We see that they may perform well sometimes but overall still fall short of our k-means binning approach.
- **p. 9 / 4 Related Work - extractive body cue:** BeT falls under the second category, as it is a behavior cloning model.
- **p. 8 / 3 Experiments - extractive body cue:** We see in Table 2 that in CARLA and Block push, BeT covers all the modes of the demonstration data, even in the few cases ...

- **PDF anchors reviewed:** datasets p. 5 (3 Experiments), p. 5 (3 Experiments), p. 6 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments), p. 9 (3 Experiments), metrics p. 9 (3 Experiments), p. 8 (3 Experiments), p. 5 (3 Experiments), p. 5 (3 Experiments), p. 6 (3 Experiments), p. 6 (3 Experiments), baselines p. 8 (Figure/Table caption), p. 6 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments), p. 9 (3 Experiments), results p. 2 (Figure/Table caption), p. 6 (3 Experiments), p. 6 (3 Experiments), p. 8 (3 Experiments), p. 8 (3 Experiments), p. 5 (3 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
