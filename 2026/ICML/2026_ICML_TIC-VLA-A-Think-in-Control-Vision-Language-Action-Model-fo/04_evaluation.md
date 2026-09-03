# Evaluation - TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=9wYjjPydfe; PDF retrieval source: https://openreview.net/pdf/111f8ac3ef90d847bb2191b2bd71a573458c6810.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Simulation Testing), p. 8 (4.2. Simulation Testing), p. 8 (4.2. Simulation Testing), p. 9 (4.4. Ablation Study), p. 7 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study)): After RL fine-tuning, TICVLA achieves the highest success rate and the lowest collision rate, indicating improved closed-loop robustness in dynamic scenes.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We train the model using three datasets featuring dynamic human-robot interactions: (1) SCAND (Karnan et al., 2022), which contains 8.7 hours of robot-driven trajectories across ...
- **p. 9 / 4.4. Ablation Study - extractive body cue:** Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments Depth Camera RGB Camera LiDAR Onboard Computer w/ Jetson Orin NX Laptop w/ RTX 4060 Desktop ...
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** The navigation policy is executed on a Unitree Go2 quadruped robot in real-world navigation tasks.
- **p. 8 / 4.3. Real-world Testing - extractive body cue:** We evaluate TIC-VLA on a Unitree Go2 robot across four real-world navigation tasks: (1) an indoor hallway with dynamic human and static obstacles, (2) a ...
- **p. 8 / 4.3. Real-world Testing - extractive body cue:** Overall, TIC-VLA transfers zero-shot to real-world robot navigation and remains robust under asynchronous high-latency VLM inference, demonstrating the practical value of explicit latency modeling.
- **p. 9 / 4.4. Ablation Study - extractive body cue:** (a) Hardware configuration, including the robot platform and computation setup.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The primary language-guided navigation baselines are listed below: (1) NaVILA (Cheng et al., 2024), a hierarchical VLA model that translates language instructions into mid-level commands; ...
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments t=2.6s t=6.4s t=13.3s t=27.9s t=32.3s t=2.3s t=7.7s t=18.3s t=54.3s t=57.3s t=69.1s I am at the end ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Simulation Testing | EMPIRICAL / REAL-ROBOT OR HARDWARE | After RL fine-tuning, TICVLA achieves the highest success rate and the lowest collision rate, indicating improved closed-loop robustness in dynamic scenes. | p. 7 (4.2. Simulation Testing) |
| 4.2. Simulation Testing | EMPIRICAL / REAL-ROBOT OR HARDWARE | The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all latency settings, ... | p. 8 (4.2. Simulation Testing) |
| 4.2. Simulation Testing | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, using KV-cache features significantly improves navigation success, and latencyawareness enhances performance under asynchronous inference. | p. 8 (4.2. Simulation Testing) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results indicate that test-time reasoning improves task success, while TIC-VLA mitigates its latency through explicit latency-aware control. | p. 9 (4.4. Ablation Study) |
| 4.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Performance is measured by the average success rate. | p. 7 (4.1. Experimental Setup) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We train the model using three datasets featuring dynamic human-robot interactions: (1) SCAND (Karnan et al., 2022), which contains 8.7 hours of robot-driven trajectories across ...
- **p. 9 / 4.4. Ablation Study - extractive body cue:** Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments Depth Camera RGB Camera LiDAR Onboard Computer w/ Jetson Orin NX Laptop w/ RTX 4060 Desktop ...
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** The navigation policy is executed on a Unitree Go2 quadruped robot in real-world navigation tasks.
- **p. 8 / 4.3. Real-world Testing - extractive body cue:** We evaluate TIC-VLA on a Unitree Go2 robot across four real-world navigation tasks: (1) an indoor hallway with dynamic human and static obstacles, (2) a ...
- **p. 8 / 4.3. Real-world Testing - extractive body cue:** Overall, TIC-VLA transfers zero-shot to real-world robot navigation and remains robust under asynchronous high-latency VLM inference, demonstrating the practical value of explicit latency modeling.
- **p. 9 / 4.4. Ablation Study - extractive body cue:** (a) Hardware configuration, including the robot platform and computation setup.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The primary language-guided navigation baselines are listed below: (1) NaVILA (Cheng et al., 2024), a hierarchical VLA model that translates language instructions into mid-level commands; ...
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments t=2.6s t=6.4s t=13.3s t=27.9s t=32.3s t=2.3s t=7.7s t=18.3s t=54.3s t=57.3s t=69.1s I am at the end ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. TIC-VLA enables real-time, language-conditioned nav- igation by decoupling slow vision-language reasoning from fast reactive control via a delayed semantic-control interface. A latency- consistent ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of TIC-VLA. The architecture adopts a decoupled dual-system design with a fast action expert and a slow reasoning VLM. A shared vision ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Details of TIC-VLA action policy structure, training, and asynchronous execution. (a) Latency-aware action policy that predicts action chunks from multimodal inputs. (b) Value ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative closed-loop results of TIC-VLA in DynaNav hospital (top) and office (bottom) environments. TIC-VLA demonstrates effective semantic reasoning while producing reactive navigation actions ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Performance of TIC-VLA and baseline methods on the DynaNav benchmark. BC, RL, and NavDP are point-goal-based.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all latency ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Influence of semantic interface and latency training. Interface Latency NE (↓) SR (↑) SPL (↑) CR (↓) Waypoint
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Real-world testing results. Runtimes for dual-system methods are reported as action policy / VLM reasoning latency.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We train the model using three datasets featuring dynamic human-robot interactions: (1) SCAND (Karnan et al., 2022), which contains 8.7 hours of robot-driven trajectories ... | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study) |
| Task/environment | Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments Depth Camera RGB Camera LiDAR Onboard Computer w/ Jetson Orin NX Laptop w/ RTX 4060 ... | reset, timeout, object/scene variation | p. 9 (4.4. Ablation Study), p. 7 (4.1. Experimental Setup) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| TIC-VLA demonstrates effective semantic reasoning while producing reactive navigation actions in dynamic scenarios. the agent and the goal; (2) Success Rate (SR): the percentage ... | definition/direction/unit from same section | p. 7 (4.1. Experimental Setup) |
| The 1-second horizon obtains the lowest collision rate, suggesting stronger shortterm reactivity, but yields a lower success rate and SPL. | definition/direction/unit from same section | p. 9 (4.4. Ablation Study) |
| As a result, stale VLM features may be treated as temporally aligned with the current observation, leading to degraded navigation accuracy, lower success rates, ... | definition/direction/unit from same section | p. 9 (4.4. Ablation Study) |
| After RL fine-tuning, TICVLA achieves the highest success rate and the lowest collision rate, indicating improved closed-loop robustness in dynamic scenes. | definition/direction/unit from same section | p. 7 (4.2. Simulation Testing) |
| The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all latency settings, ... | definition/direction/unit from same section | p. 8 (4.2. Simulation Testing) |
| For each task, we conduct five trials and report the average success rate. | definition/direction/unit from same section | p. 8 (4.3. Real-world Testing) |
| Figure 10. Online reinforcement learning tasks used to train TIC-VLA across three environments and tasks. The weights for the reward function (Equation (5)) are ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| We adopt the following evaluation metrics: (1) Navigation Error (NE): the final distance between 6 | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Without RL finetuning, TIC-VLA is competitive with NavDP, a point-goal method with privileged state access, and outperforms the vanilla BC and RL baselines. | comparison identity and matched condition | p. 7 (4.2. Simulation Testing) |
| Moreover, TIC-VLA outperforms stronger VLA baselines, including OmniVLA and MobileVLA. | comparison identity and matched condition | p. 7 (4.2. Simulation Testing) |
| All language-guided baselines are fine-tuned on the same training datasets and evaluated under the same settings for a fair comparison. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Point-goal navigation policies are included as reference baselines to contextualize task difficulty: (1) a vanilla Behavior Cloning (BC) policy that maps RGB observations and ... | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Figure 10. Online reinforcement learning tasks used to train TIC-VLA across three environments and tasks. The weights for the reward function (Equation (5)) are ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| All evaluations are conducted zero-shot, without task-specific training data. | comparison identity and matched condition | p. 8 (4.3. Real-world Testing) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| As shown in Table 5, the 3-second horizon achieves the best overall performance among TICVLA variants without RL fine-tuning. | component/input/data sensitivity | p. 9 (4.4. Ablation Study) |
| Table 5. Effect of action prediction horizon. Results are reported without RL fine-tuning. Horizon NE (↓) SR (↑) SPL (↑) CR (↓) 1s | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Specifically, we compare interface variants that use waypoint-based guidance and KV-cache-based features, each trained with and without explicit latency-aware modeling and training. | component/input/data sensitivity | p. 8 (4.2. Simulation Testing) |
| The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all latency settings, ... | component/input/data sensitivity | p. 8 (4.2. Simulation Testing) |
| In contrast, TIC-VLA uses only egocentric observations and language instructions, without access to privileged goals or maps. | component/input/data sensitivity | p. 7 (4.2. Simulation Testing) |
| The synchronous TIC-VLA variant also degrades substantially, confirming that blocking control on slow VLM inference harms real-time navigation. | component/input/data sensitivity | p. 7 (4.2. Simulation Testing) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly exposes inference delay to the control policy. | After RL fine-tuning, TICVLA achieves the highest success rate and the lowest collision rate, indicating improved closed-loop robustness in dynamic scenes. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Simulation Testing), p. 8 (4.2. Simulation Testing), p. 8 (4.2. Simulation Testing), p. 9 (4.4. Ablation Study), p. 7 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study) |
| Primary metric/result | The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all latency settings, ... | numeric claim only at cited anchor | p. 8 (4.2. Simulation Testing) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We train the model using three datasets featuring dynamic human-robot interactions: (1) SCAND (Karnan et al., 2022), which contains 8.7 hours of robot-driven trajectories across ...
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments t=2.6s t=6.4s t=13.3s t=27.9s t=32.3s t=2.3s t=7.7s t=18.3s t=54.3s t=57.3s t=69.1s I am at the end ...
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Enter the room with the reception desk. t=41.1s Exit the room and turn right to enter the hallway.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** TIC-VLA demonstrates effective semantic reasoning while producing reactive navigation actions in dynamic scenarios. the agent and the goal; (2) Success Rate (SR): the percentage of ...
- **p. 7 / 4.2. Simulation Testing - extractive body cue:** All experiments are conducted on an NVIDIA L40S GPU, with the action policy running at 10 Hz and asynchronous VLM reasoning running at 0.5 Hz.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Disabling reasoning reduces VLM overhead and increases the forward rate from 0.5 Hz to 4 Hz, but leads to weaker goal completion and navigation progress.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | An episode is considered a failure if manual intervention is required to prevent collisions. | p. 7 (4.1. Experimental Setup) |
| body limitation/failure cue | Although the non-reasoning variant has a lower collision rate, this mainly reflects reduced activity and more frequent failure rather than safer navigation. | p. 8 (4.4. Ablation Study) |
| body limitation/failure cue | Figure 5. The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | TIC-VLA has three main limitations. | p. 9 (5. Conclusions) |
| body limitation/failure cue | After RL fine-tuning, TICVLA achieves the highest success rate and the lowest collision rate, indicating improved closed-loop robustness in dynamic scenes. | p. 7 (4.2. Simulation Testing) |
| body limitation/failure cue | Third, extending beyond navigation to domains such as robotic manipulation remains future work. | p. 9 (5. Conclusions) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For training the action expert, we increase the batch size to 16 per GPU and set the initial learning rate to 2 × 10-4. | p. 6 (4.1. Experimental Setup) |
| Training is performed using Distributed Data Parallel on eight NVIDIA L40S GPUs, with a batch size of 2 per GPU. | p. 6 (4.1. Experimental Setup) |
| An RTX A6000 GPU is used only when the baselines cannot run on these devices. | p. 7 (4.1. Experimental Setup) |
| Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments Depth Camera RGB Camera LiDAR Onboard Computer w/ Jetson Orin NX Laptop w/ RTX 4060 ... | p. 9 (4.4. Ablation Study) |
| We mix waypoint-only and scene-reasoningaugmented targets during training for flexible prompting at inference time. | p. 5 (3.3. Latency-Consistent Training Pipeline) |
| Pooling Concatenate Value State + Goal MLP MLP (a) (b) +++ Asynchronous Inference in Closed-loop Multi-stage Training IL with Delayed Inference VLM SFT (d) ... | p. 5 (3.3. Latency-Consistent Training Pipeline) |
| All experiments are conducted on an NVIDIA L40S GPU, with the action policy running at 10 Hz and asynchronous VLM reasoning running at 0.5 ... | p. 7 (4.2. Simulation Testing) |
| Task descriptions and hardware configurations are shown in Figure 6. | p. 8 (4.3. Real-world Testing) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.1. Experimental Setup - extractive body cue:** An episode is considered a failure if manual intervention is required to prevent collisions.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Although the non-reasoning variant has a lower collision rate, this mainly reflects reduced activity and more frequent failure rather than safer navigation.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains consistently higher success rates across all latency ...
- **p. 9 / 5. Conclusions - extractive body cue:** TIC-VLA has three main limitations.
- **p. 7 / 4.2. Simulation Testing - extractive body cue:** After RL fine-tuning, TICVLA achieves the highest success rate and the lowest collision rate, indicating improved closed-loop robustness in dynamic scenes.
- **p. 9 / 5. Conclusions - extractive body cue:** Third, extending beyond navigation to domains such as robotic manipulation remains future work.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study), p. 7 (4.1. Experimental Setup), p. 8 (4.3. Real-world Testing), p. 8 (4.3. Real-world Testing), p. 9 (4.4. Ablation Study), metrics p. 7 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study), p. 9 (4.4. Ablation Study), p. 7 (4.2. Simulation Testing), p. 8 (4.2. Simulation Testing), p. 8 (4.3. Real-world Testing), baselines p. 7 (4.2. Simulation Testing), p. 7 (4.2. Simulation Testing), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 19 (Figure/Table caption), p. 8 (4.3. Real-world Testing), results p. 7 (4.2. Simulation Testing), p. 8 (4.2. Simulation Testing), p. 8 (4.2. Simulation Testing), p. 9 (4.4. Ablation Study), p. 7 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
