# Evaluation - WMPO: World Model-based Policy Optimization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007263; PDF retrieval source: https://arxiv.org/pdf/2511.09515. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments)): We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline RL in simulation environments; (2) how does the ...

## Evaluation Body Digest

- **p. 6 / 4 Experiments - extractive body cue:** We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline RL in simulation ...
- **p. 9 / 4 Experiments - extractive body cue:** Real World Trajectory Imagined Trajectory Figure 7 Real-world experiments on the fine-grained manipulation task "Insert the square into the stick" where the clearance between the ...
- **p. 9 / 4 Experiments - extractive body cue:** The top row shows the real-world trajectory of the base policy executed in the real world, while the bottom row depicts the corresponding imagined trajectory ...
- **p. 10 / 4 Experiments - extractive body cue:** 4.6 Real-world Experiments In this section, we evaluate the challenging real-world manipulation task, "Insert the square into the stick" (see Fig.
- **p. 7 / 4 Experiments - extractive body cue:** For simplicity, we omit the robot proprioceptive state and wrist camera inputs, and set the action chunk length K to 8.
- **p. 8 / 4 Experiments - extractive body cue:** These results highlight the effectiveness and scalability of WMPO for policy optimization in robotic manipulation.
- **p. 10 / 4 Experiments - extractive body cue:** For comparison, we also train an offline DPO policy using the same dataset.
- **p. 7 / 4 Experiments - extractive body cue:** Simulation Environment Details We conduct experiments in the Mimicgen simulation [23].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 4 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline RL in ... | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that the base policy, DPO, and WMPO achieve success rates of 53%, 60%, and 70%, respectively, demonstrating the effectiveness of WMPO ... | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | DPO attains modest improvements in the in-distribution setting compared to the base policy, but its performance degrades significantly under background and texture changes, suggesting ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 6, demonstrate that WMPO achieves stable and substantial improvements over both baselines, whereas DPO fails to improve iteratively due to unstable training. | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, we evaluate the reward model and find that it achieves an F1 score above 0.95 across all tasks, reliably distinguishing success from failure ... | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiments - extractive body cue:** We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline RL in simulation ...
- **p. 9 / 4 Experiments - extractive body cue:** Real World Trajectory Imagined Trajectory Figure 7 Real-world experiments on the fine-grained manipulation task "Insert the square into the stick" where the clearance between the ...
- **p. 9 / 4 Experiments - extractive body cue:** The top row shows the real-world trajectory of the base policy executed in the real world, while the bottom row depicts the corresponding imagined trajectory ...
- **p. 10 / 4 Experiments - extractive body cue:** 4.6 Real-world Experiments In this section, we evaluate the challenging real-world manipulation task, "Insert the square into the stick" (see Fig.
- **p. 7 / 4 Experiments - extractive body cue:** For simplicity, we omit the robot proprioceptive state and wrist camera inputs, and set the action chunk length K to 8.
- **p. 8 / 4 Experiments - extractive body cue:** These results highlight the effectiveness and scalability of WMPO for policy optimization in robotic manipulation.
- **p. 10 / 4 Experiments - extractive body cue:** For comparison, we also train an offline DPO policy using the same dataset.
- **p. 7 / 4 Experiments - extractive body cue:** Simulation Environment Details We conduct experiments in the Mimicgen simulation [23].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline RL in ... | embodiment, simulator version and control stack | p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | Real World Trajectory Imagined Trajectory Figure 7 Real-world experiments on the fine-grained manipulation task "Insert the square into the stick" where the clearance between ... | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 5 (1. Imagined Trajectory Generation), p. 4 (3. Policy Update) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 5 (1. Imagined Trajectory Generation), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Furthermore, we evaluate the reward model and find that it achieves an F1 score above 0.95 across all tasks, reliably distinguishing success from failure ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Performance is reported as the task success rate (%). | definition/direction/unit from same section | p. 7 (4 Experiments) |
| For evaluation, we test 128 different initial states for each task and report the average success rate. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| 0 128 256 Rollout Budget 45 50 55 60 65 Success Rate (%) Base Policy DPO WMPO Figure 6 Lifelong learning results of WMPO ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| All models are evaluated under identical experimental conditions, and we report the average success rate over 30 trials. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| The results show that the base policy, DPO, and WMPO achieve success rates of 53%, 60%, and 70%, respectively, demonstrating the effectiveness of WMPO ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| 3), we observe that when both the base policy and WMPO deviate from the correct trajectory due to error accumulation and encounter a collision, ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| 4.5 Lifelong Learning In this section, we demonstrate that WMPO can continuously improve the performance of VLA by iteratively collecting real trajectories from the ... | definition/direction/unit from same section | p. 9 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Results show that WMPO consistently outperforms both GRPO and DPO baselines under different budgets. | comparison identity and matched condition | p. 7 (4 Experiments) |
| 1, WMPO consistently outperforms all baselines across all tasks. | comparison identity and matched condition | p. 8 (4 Experiments) |
| We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline RL in ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| Collision Self-correction Continue moving down WMPO Base Policy … … Figure 3 Behavior analysis of the Square task (inserting the square into the stick) ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| With a small rollout budget of P=128, it already surpasses the strongest baseline by +9.8 points, demonstrating strong data efficiency. | comparison identity and matched condition | p. 8 (4 Experiments) |
| 0 128 256 Rollout Budget 45 50 55 60 65 Success Rate (%) Base Policy DPO WMPO Figure 6 Lifelong learning results of WMPO ... | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| These trajectories are further used to fine-tune a world model, which predicts the next K = 8 frames given c = 4 conditioning frames ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| 4.1 Experiment Settings Implementation Details In this work, we fine-tune OpenVLA-OFT [24] via imitation learning on target manipulation tasks as our base policy. | component/input/data sensitivity | p. 7 (4 Experiments) |
| Using the Cobot Mobile ALOHA platform, we collect 200 high-quality expert demonstrations to fine-tune the OpenVLA-OFT model as the base policy. | component/input/data sensitivity | p. 10 (4 Experiments) |
| We then deploy this policy to collect an additional 128 trajectories, which are used to further fine-tune the world model and optimize the policy ... | component/input/data sensitivity | p. 10 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig. | We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline RL in ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Primary metric/result | The results show that the base policy, DPO, and WMPO achieve success rates of 53%, 60%, and 70%, respectively, demonstrating the effectiveness of WMPO ... | numeric claim only at cited anchor | p. 10 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** These trajectories are further used to fine-tune a world model, which predicts the next K = 8 frames given c = 4 conditioning frames and ...
- **p. 8 / 4 Experiments - extractive body cue:** With a small rollout budget of P=128, it already surpasses the strongest baseline by +9.8 points, demonstrating strong data efficiency.
- **p. 8 / 4 Experiments - extractive body cue:** When the budget increases to P=1280, the margin further expands to +15.2 points on average, indicating that WMPO leverages additional trajectories more effectively than existing ...
- **p. 9 / 4 Experiments - extractive body cue:** 0 128 256 Rollout Budget 45 50 55 60 65 Success Rate (%) Base Policy DPO WMPO Figure 6 Lifelong learning results of WMPO and ...
- **p. 10 / 4 Experiments - extractive body cue:** We then deploy this policy to collect an additional 128 trajectories, which are used to further fine-tune the world model and optimize the policy within ...
- **p. 10 / 4 Experiments - extractive body cue:** All models are evaluated under identical experimental conditions, and we report the average success rate over 30 trials.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The baseline policy, trained only on expert demonstrations, has never observed collisions during training; it continues to push the square against the stick until ... | p. 8 (4 Experiments) |
| body limitation/failure cue | 6, demonstrate that WMPO achieves stable and substantial improvements over both baselines, whereas DPO fails to improve iteratively due to unstable training. | p. 10 (4 Experiments) |
| body limitation/failure cue | This is because WMPO discourages stuck behaviors, which often result in failures due to timeouts. | p. 8 (4 Experiments) |
| body limitation/failure cue | 7, more cases including failure could be found in Appendix C), to validate the effectiveness of WMPO. | p. 10 (4 Experiments) |
| body limitation/failure cue | Collision Self-correction Continue moving down WMPO Base Policy … … Figure 3 Behavior analysis of the Square task (inserting the square into the stick) ... | p. 7 (4 Experiments) |
| body limitation/failure cue | DPO attains modest improvements in the in-distribution setting compared to the base policy, but its performance degrades significantly under background and texture changes, suggesting ... | p. 9 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.1 Experiment Settings Implementation Details In this work, we fine-tune OpenVLA-OFT [24] via imitation learning on target manipulation tasks as our base policy. | p. 7 (4 Experiments) |
| More implementation details are provided in Appendix B. | p. 8 (4 Experiments) |
| Coffee StackThree ThreePieceAssembly Square 94 96 98 100 102 104 Relative Length (%) Base Policy DPO GRPO WMPO Figure 5 Relative average trajectory length ... | p. 9 (4 Experiments) |
| All models are evaluated under identical experimental conditions, and we report the average success rate over 30 trials. | p. 10 (4 Experiments) |
| To address this, WMPO generates complete trials through clip-level autoregressive video generation, enabling more reliable outcome-based reward assignment. | p. 2 (1 Introduction) |
| When applying the imagined trajectory to VLA optimization, we decode the images back into pixel space to better leverage the pretrained knowledge, rather than ... | p. 5 (1. Imagined Trajectory Generation) |
| To mitigate this issue, we introduce a noisy-frame conditioning technique: during training, conditional frames Ii-m:i are perturbed with diffusion noise at 50/1000 steps rather ... | p. 5 (1. Imagined Trajectory Generation) |
| At inference, the model applies a sliding window with stride s over τ to compute the success probability of each clip. | p. 6 (1. Imagined Trajectory Generation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 Experiments - extractive body cue:** The baseline policy, trained only on expert demonstrations, has never observed collisions during training; it continues to push the square against the stick until the ...
- **p. 10 / 4 Experiments - extractive body cue:** 6, demonstrate that WMPO achieves stable and substantial improvements over both baselines, whereas DPO fails to improve iteratively due to unstable training.
- **p. 8 / 4 Experiments - extractive body cue:** This is because WMPO discourages stuck behaviors, which often result in failures due to timeouts.
- **p. 10 / 4 Experiments - extractive body cue:** 7, more cases including failure could be found in Appendix C), to validate the effectiveness of WMPO.
- **p. 7 / 4 Experiments - extractive body cue:** Collision Self-correction Continue moving down WMPO Base Policy … … Figure 3 Behavior analysis of the Square task (inserting the square into the stick) shows ...
- **p. 9 / 4 Experiments - extractive body cue:** DPO attains modest improvements in the in-distribution setting compared to the base policy, but its performance degrades significantly under background and texture changes, suggesting reliance ...

- **PDF anchors reviewed:** datasets p. 6 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), metrics p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), baselines p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), results p. 6 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
