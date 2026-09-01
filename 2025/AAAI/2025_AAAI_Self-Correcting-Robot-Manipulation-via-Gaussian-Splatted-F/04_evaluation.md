# Evaluation - Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/34866; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/34866. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme), p. 7 (2. By incorporating the proposed self-correction scheme), p. 3 (2. By incorporating the proposed self-correction scheme), p. 1 (Figure/Table caption)): Comprehensive experiments across ten tasks with 166 variations demonstrate that our method significantly outperforms stateof-the-art techniques, achieving a 12.0% higher success rate.

## Evaluation Body Digest

- **p. 5 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** 2023), we collected 20 episodes of demonstrations for each of 10 challenging language-conditioned manipulation tasks in the dataset collected PerAct (Shridhar, Manuelli, and Fox 2023b), ...
- **p. 6 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** To differentiate the testing focus across various tasks on PerAct dataset, we compute the average success rate for the following categories: • The ‘Planning' group ...
- **p. 4 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** Future scene prediction In robotic manipulation, all objects are treated as rigid bodies with intrinsic properties such as color, scale, opacity, and semantic features.
- **p. 5 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** To further validate the performance of the proposed method, we collected 20 episodes of demonstrations for each of 6 tasks from the HiveFormer (Guhur et ...
- **p. 7 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** The evaluation protocol comprised 25 demonstration episodes for two manipulation tasks: open drawer and reach and drag.
- **p. 3 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** The training of diffusion models requires a substantial amount of expert trajectories and is limited to single-task robotic manipulation.
- **p. 3 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** In scenarios where environmental changes or unforeseen obstacles arise during locomotion, it is imperative for robots to dynamically modify their pre-determined trajectories.
- **p. 6 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** We evaluate 25 episodes per task at the final checkpoint utilizing 3 random seeds across 10 challenging tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 2. By incorporating the proposed self-correction scheme | EMPIRICAL / SIMULATION | Comprehensive experiments across ten tasks with 166 variations demonstrate that our method significantly outperforms stateof-the-art techniques, achieving a 12.0% higher success rate. | p. 7 (2. By incorporating the proposed self-correction scheme) |
| 2. By incorporating the proposed self-correction scheme | EMPIRICAL / SIMULATION | As presented in table 2, our method achieves the highest success rate in 5 out of 6 tasks and the average success rate across ... | p. 6 (2. By incorporating the proposed self-correction scheme) |
| 2. By incorporating the proposed self-correction scheme | EMPIRICAL / SIMULATION | The mean and standard value of the success rates are reported as (mean ± std), and the highest average performance is also reported. | p. 6 (2. By incorporating the proposed self-correction scheme) |
| 2. By incorporating the proposed self-correction scheme | EMPIRICAL / SIMULATION | The success rates (SR) on the PerAct's dataset with different τ are reported. bustness compared to other methods (GNFactor and PerAct) under all investigated ... | p. 7 (2. By incorporating the proposed self-correction scheme) |
| 2. By incorporating the proposed self-correction scheme | EMPIRICAL / SIMULATION | 2023) optimized a generalizable NeRF with a reconstruction loss besides behavior cloning and showed effective improvement in both simulated and real scenarios. | p. 3 (2. By incorporating the proposed self-correction scheme) |

## Dataset / Benchmark Role

- **p. 5 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** 2023), we collected 20 episodes of demonstrations for each of 10 challenging language-conditioned manipulation tasks in the dataset collected PerAct (Shridhar, Manuelli, and Fox 2023b), ...
- **p. 6 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** To differentiate the testing focus across various tasks on PerAct dataset, we compute the average success rate for the following categories: • The ‘Planning' group ...
- **p. 4 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** Future scene prediction In robotic manipulation, all objects are treated as rigid bodies with intrinsic properties such as color, scale, opacity, and semantic features.
- **p. 5 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** To further validate the performance of the proposed method, we collected 20 episodes of demonstrations for each of 6 tasks from the HiveFormer (Guhur et ...
- **p. 7 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** The evaluation protocol comprised 25 demonstration episodes for two manipulation tasks: open drawer and reach and drag.
- **p. 3 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** The training of diffusion models requires a substantial amount of expert trajectories and is limited to single-task robotic manipulation.
- **p. 3 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** In scenarios where environmental changes or unforeseen obstacles arise during locomotion, it is imperative for robots to dynamically modify their pre-determined trajectories.
- **p. 6 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** We evaluate 25 episodes per task at the final checkpoint utilizing 3 random seeds across 10 challenging tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Illustration of the proposed self-correcting policy. was successful. Moreover, since existing policies are typi- cally learned from successful expert trajectories, they may fall ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of the proposed foresight-driven self-correction module. estimated using α-blending as follows: ˜Im(p) = N X i=1 ωici Y
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Illustration of the self-correcting robot manipula- tion framework. consistency between the prediction and observation, which is defined as d = D({µ+ i }N ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Success rates on Peract's dataset. Bold indicates the best results while Underline denotes the second-ranked per- formance. The ‘Average' metric represents the mean ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Success rates on HiveFormer's dataset. Bold indicates the best performance , while underline denotes the second- ranked performance. The ‘Average' metric represents the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Ablation study. The comparison between the models without and with self-correction on PerAct's dataset.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: The visualization of rendered images generated by our method, ManiGaussian, and GNFActor.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: The visualization of the predicted point cloud. clouds for the tasks open drawer and turn tap. The visual results reveal that the proposed ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 2023), we collected 20 episodes of demonstrations for each of 10 challenging language-conditioned manipulation tasks in the dataset collected PerAct (Shridhar, Manuelli, and Fox ... | embodiment, simulator version and control stack | p. 5 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme) |
| Task/environment | To differentiate the testing focus across various tasks on PerAct dataset, we compute the average success rate for the following categories: • The ‘Planning' ... | reset, timeout, object/scene variation | p. 6 (2. By incorporating the proposed self-correction scheme), p. 4 (2. By incorporating the proposed self-correction scheme) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (2. By incorporating the proposed self-correction scheme), p. 2 (2. By incorporating the proposed self-correction scheme) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (2. By incorporating the proposed self-correction scheme), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Success rates on HiveFormer's dataset. Bold indicates the best performance , while underline denotes the second- ranked performance. The ‘Average' metric represents ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| The success rates indicate that our approach exhibits enhanced roMethod / Perturb. light color object color object texture table color PerAct A 20.0 20.0 ... | definition/direction/unit from same section | p. 7 (2. By incorporating the proposed self-correction scheme) |
| The mean and standard value of the success rates are reported as (mean ± std), and the highest average performance is also reported. | definition/direction/unit from same section | p. 6 (2. By incorporating the proposed self-correction scheme) |
| Table 5: Comparative analysis on the distance threshold. The success rates (SR) on the PerAct's dataset with different τ are reported. bustness compared to ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| If the distance d exceeds a predefined threshold τ, it indicates that there may be significant errors in the action execution. | definition/direction/unit from same section | p. 5 (2. By incorporating the proposed self-correction scheme) |
| Figure 1: Illustration of the proposed self-correcting policy. was successful. Moreover, since existing policies are typi- cally learned from successful expert trajectories, they may ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| 2023) optimized a generalizable NeRF with a reconstruction loss besides behavior cloning and showed effective improvement in both simulated and real scenarios. | definition/direction/unit from same section | p. 3 (2. By incorporating the proposed self-correction scheme) |
| These technologies generally necessitate little to no fine-tuning to attain effective performance, predominantly leveraging the inherent inferential capabilities of open-source large models. | definition/direction/unit from same section | p. 3 (2. By incorporating the proposed self-correction scheme) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Analysis and discussion Ablation study To evaluate the efficacy of the proposed self-correction scheme, we conducted a comparative analysis between the baseline framework, designated ... | comparison identity and matched condition | p. 7 (2. By incorporating the proposed self-correction scheme) |
| Table 3: Ablation study. The comparison between the models without and with self-correction on PerAct's dataset. | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Performance evaluation Quantitative analysis In this section, we compare the proposed model with several state-of-the-art multi-task approaches on Peract's and HiveFormer's datasets. | comparison identity and matched condition | p. 6 (2. By incorporating the proposed self-correction scheme) |
| Qualitative analysis Figure 4 illustrates the qualitative results obtained from our method and state-of-the-art approaches for novel view synthesis on two tasks, namely stack ... | comparison identity and matched condition | p. 6 (2. By incorporating the proposed self-correction scheme) |
| Lu et al.'s method uses dynamic Gaussian Splatting to generate semantic features and feeds them into the PercevieIO module, while the proposed method uses ... | comparison identity and matched condition | p. 3 (2. By incorporating the proposed self-correction scheme) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3: Ablation study. The comparison between the models without and with self-correction on PerAct's dataset. | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| These technologies generally necessitate little to no fine-tuning to attain effective performance, predominantly leveraging the inherent inferential capabilities of open-source large models. | component/input/data sensitivity | p. 3 (2. By incorporating the proposed self-correction scheme) |
| Sensitivity analysis of threshold τ To investigate the impact of the Chamfer distance threshold τ, we evaluated performance across 10 representative tasks from the ... | component/input/data sensitivity | p. 7 (2. By incorporating the proposed self-correction scheme) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose a novel approach to ascertain the necessity of replanning by predicting the environmental structural information of future keyframes, thereby ... | Comprehensive experiments across ten tasks with 166 variations demonstrate that our method significantly outperforms stateof-the-art techniques, achieving a 12.0% higher success rate. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme), p. 7 (2. By incorporating the proposed self-correction scheme), p. 3 (2. By incorporating the proposed self-correction scheme), p. 1 (Figure/Table caption) |
| Primary metric/result | As presented in table 2, our method achieves the highest success rate in 5 out of 6 tasks and the average success rate across ... | numeric claim only at cited anchor | p. 6 (2. By incorporating the proposed self-correction scheme) |

- Numeric sentences retained from the body:
- **p. 5 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** 2023), we collected 20 episodes of demonstrations for each of 10 challenging language-conditioned manipulation tasks in the dataset collected PerAct (Shridhar, Manuelli, and Fox 2023b), ...
- **p. 5 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** To further validate the performance of the proposed method, we collected 20 episodes of demonstrations for each of 6 tasks from the HiveFormer (Guhur et ...
- **p. 6 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** Method / Task close jar open drawer sweep to dustpan meat off grill turn tap slide block put in drawer PerAct 12.0 36.0 12.0 48.0 ...
- **p. 6 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** The ‘Average' metric represents the mean success rate across all 10 tasks.
- **p. 6 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** Method / Task basketball hoop change clock phone on base put rubbish stack wine turn oven on Average PerAct 32.0 24.0 36.0 48.0 28.0 28.0 ...
- **p. 6 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** The ‘Average' metric represents the mean success rate across all 6 tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: Illustration of the proposed self-correcting policy. was successful. Moreover, since existing policies are typi- cally learned from successful expert trajectories, they may ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Incorpoarating this scheme with the PerAct pipeline, we develop a robust selfcorrecting policy capable of failure self-correction. | p. 7 (2. By incorporating the proposed self-correction scheme) |
| body limitation/failure cue | Conclusion In this paper, we introduce a novel self-correcting scheme for robot manipulation that addresses the critical challenge of failure detection and recovery in ... | p. 7 (2. By incorporating the proposed self-correction scheme) |
| body limitation/failure cue | To mitigate this issue, we propose a foresight-driven self-correction scheme, where a foresight with Gaussian splatting-based representation is adopted for failure detection. | p. 3 (2. By incorporating the proposed self-correction scheme) |
| body limitation/failure cue | Additionally, Lu et al.'s method is not capable of self-correction, while our proposed method includes failure detection and self-correction, which can be incorporated with ... | p. 3 (2. By incorporating the proposed self-correction scheme) |
| body limitation/failure cue | Once the observation is not consistent with the predicted scene, it can be viewed as a failure. | p. 4 (2. By incorporating the proposed self-correction scheme) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We evaluate 25 episodes per task at the final checkpoint utilizing 3 random seeds across 10 challenging tasks. | p. 6 (2. By incorporating the proposed self-correction scheme) |
| To differentiate the testing focus across various tasks on PerAct dataset, we compute the average success rate for the following categories: • The ‘Planning' ... | p. 6 (2. By incorporating the proposed self-correction scheme) |
| The visual results reveal that the proposed method effectively predicts the spatial state information of the robotic arm at future time steps, providing a ... | p. 7 (2. By incorporating the proposed self-correction scheme) |
| 2019) was used with an initial learning rate of ( 5 × 10-4 ) with a cosine scheduler. | p. 5 (2. By incorporating the proposed self-correction scheme) |
| All comparative methods were trained on PerAct's dataset for 300000 iterations, while the HiveFormer dataset for 100000 iterations, both with a batch size of ... | p. 5 (2. By incorporating the proposed self-correction scheme) |
| 2020) and ResNet18 image encoder (He et al. | p. 2 (2. By incorporating the proposed self-correction scheme) |
| 2022) uses the USE language encoder (Yang et al. | p. 2 (2. By incorporating the proposed self-correction scheme) |
| 2025) for visual representation, which relates the semantic features with 3D Gaussian and fed them into action decoder. | p. 3 (2. By incorporating the proposed self-correction scheme) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Illustration of the proposed self-correcting policy. was successful. Moreover, since existing policies are typi- cally learned from successful expert trajectories, they may fall ...
- **p. 7 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** Incorpoarating this scheme with the PerAct pipeline, we develop a robust selfcorrecting policy capable of failure self-correction.
- **p. 7 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** Conclusion In this paper, we introduce a novel self-correcting scheme for robot manipulation that addresses the critical challenge of failure detection and recovery in language-conditioned ...
- **p. 3 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** To mitigate this issue, we propose a foresight-driven self-correction scheme, where a foresight with Gaussian splatting-based representation is adopted for failure detection.
- **p. 3 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** Additionally, Lu et al.'s method is not capable of self-correction, while our proposed method includes failure detection and self-correction, which can be incorporated with other ...
- **p. 4 / 2. By incorporating the proposed self-correction scheme - extractive body cue:** Once the observation is not consistent with the predicted scene, it can be viewed as a failure.

- **PDF anchors reviewed:** datasets p. 5 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme), p. 4 (2. By incorporating the proposed self-correction scheme), p. 5 (2. By incorporating the proposed self-correction scheme), p. 7 (2. By incorporating the proposed self-correction scheme), p. 3 (2. By incorporating the proposed self-correction scheme), metrics p. 6 (Figure/Table caption), p. 7 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme), p. 7 (Figure/Table caption), p. 5 (2. By incorporating the proposed self-correction scheme), p. 1 (Figure/Table caption), baselines p. 7 (2. By incorporating the proposed self-correction scheme), p. 7 (Figure/Table caption), p. 6 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme), p. 3 (2. By incorporating the proposed self-correction scheme), results p. 7 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme), p. 6 (2. By incorporating the proposed self-correction scheme), p. 7 (2. By incorporating the proposed self-correction scheme), p. 3 (2. By incorporating the proposed self-correction scheme), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
