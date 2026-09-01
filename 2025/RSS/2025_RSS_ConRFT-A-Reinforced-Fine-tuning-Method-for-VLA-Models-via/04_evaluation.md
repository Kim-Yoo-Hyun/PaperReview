# Evaluation - ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p019.html; PDF retrieval source: https://arxiv.org/pdf/2502.05450. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 8 (V. EXPERIMENT AND RESULTS), p. 8 (V. EXPERIMENT AND RESULTS), p. 6 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS)): Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, representing a 144% improvement over the ...

## Evaluation Body Digest

- **p. 6 / V. EXPERIMENT AND RESULTS - extractive body cue:** This figure presents the success rates, intervention rates, and episode lengths for HIL-SERL [20], HG-DAgger [19], PA-RL [14] and our method across five representative real-world ...
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** This enhanced sample efficiency and reduced episode length highlight the advantages of ConRFT for fine-tuning VLA models in real-world robotic applications.
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** This stability and performance highlight the effectiveness of our approach in overcoming the limitations of existing fine-tuning methods in real-world robotic applications.
- **p. 5 / V. EXPERIMENT AND RESULTS - extractive body cue:** To this end, we perform real-world experiments across eight diverse manipulation tasks, as illustrated in Figure 2.
- **p. 5 / V. EXPERIMENT AND RESULTS - extractive body cue:** Additionally, each task's initial state is randomized using either a scripted robot motion or manual resets by a human operator.
- **p. 6 / V. EXPERIMENT AND RESULTS - extractive body cue:** Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, representing a 144% ...
- **p. 8 / V. EXPERIMENT AND RESULTS - extractive body cue:** As shown in Table IV, the results indicate that ConRFT can effectively enhance the performance of various VLAs, improving the success rates across multiple robotic ...
- **p. 8 / V. EXPERIMENT AND RESULTS - extractive body cue:** As shown in Table III, even though DP and SFT benefit from a larger quantity of demonstrations, their success rates still fail to match the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** V. EXPERIMENT AND RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, ... | p. 6 (Figure/Table caption) |
| V. EXPERIMENT AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Meanwhile, RLDG achieves higher success rates using optimal data collected from RL policies, suggesting that the consistency of these RL-collected data can improve the ... | p. 8 (V. EXPERIMENT AND RESULTS) |
| V. EXPERIMENT AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This suggests that Cal-ConRFT enables quicker adaptation of the online learning process by leveraging the Q loss during the offline stage, allowing more effective ... | p. 8 (V. EXPERIMENT AND RESULTS) |
| V. EXPERIMENT AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | While HG-DAgger leverages human corrections to fine-tune the VLA model through supervised learning, it fails to achieve significant policy improvement and even experiences a ... | p. 6 (V. EXPERIMENT AND RESULTS) |
| V. EXPERIMENT AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Training Time (mins) Success Rate (%) Episode length Task HILSERL[20] HILConRFT HILSERL[20] HILConRFT Pick Banana 45 0 →15 50 →90 30.6 51.2 Put Spoon ... | p. 7 (V. EXPERIMENT AND RESULTS) |

## Dataset / Benchmark Role

- **p. 6 / V. EXPERIMENT AND RESULTS - extractive body cue:** This figure presents the success rates, intervention rates, and episode lengths for HIL-SERL [20], HG-DAgger [19], PA-RL [14] and our method across five representative real-world ...
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** This enhanced sample efficiency and reduced episode length highlight the advantages of ConRFT for fine-tuning VLA models in real-world robotic applications.
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** This stability and performance highlight the effectiveness of our approach in overcoming the limitations of existing fine-tuning methods in real-world robotic applications.
- **p. 5 / V. EXPERIMENT AND RESULTS - extractive body cue:** To this end, we perform real-world experiments across eight diverse manipulation tasks, as illustrated in Figure 2.
- **p. 5 / V. EXPERIMENT AND RESULTS - extractive body cue:** Additionally, each task's initial state is randomized using either a scripted robot motion or manual resets by a human operator.
- **p. 6 / V. EXPERIMENT AND RESULTS - extractive body cue:** Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, representing a 144% ...
- **p. 8 / V. EXPERIMENT AND RESULTS - extractive body cue:** As shown in Table IV, the results indicate that ConRFT can effectively enhance the performance of various VLAs, improving the success rates across multiple robotic ...
- **p. 8 / V. EXPERIMENT AND RESULTS - extractive body cue:** As shown in Table III, even though DP and SFT benefit from a larger quantity of demonstrations, their success rates still fail to match the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of ConRFT. This figure illustrates the architecture of our reinforced fine-tuning approach for a pre-trained VLA model, which comprises two stages: the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of all real-world experimental tasks. The real-world tasks include picking and placing (a) banana, (b) spoon, (d) and (f) bread, operating with ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Learning curves during online training. This figure presents the success rates, intervention rates, and episode lengths for HIL-SERL [20], HG-DAgger [19], PA-RL [14] ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, representing ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Learning curves for HIL-ConRFT online fine-tuning from SFT [47] and Cal-ConRFT baselines. This figure presents success and intervention rates across two represen- tative ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 5: Hardware setup and illustrations of camera views. We give the illustrations of hardware setup and the corresponding camera views for all real-world tasks ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 6: Learning curves during online training for all tasks. This figure presents the success rates, intervention rates, and episode lengths, displayed as a running ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This figure presents the success rates, intervention rates, and episode lengths for HIL-SERL [20], HG-DAgger [19], PA-RL [14] and our method across five representative ... | embodiment, simulator version and control stack | p. 6 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS) |
| Task/environment | This enhanced sample efficiency and reduced episode length highlight the advantages of ConRFT for fine-tuning VLA models in real-world robotic applications. | reset, timeout, object/scene variation | p. 7 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This suggests that Cal-ConRFT enables quicker adaptation of the online learning process by leveraging the Q loss during the offline stage, allowing more effective ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENT AND RESULTS) |
| As shown in Table IV, the results indicate that ConRFT can effectively enhance the performance of various VLAs, improving the success rates across multiple ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENT AND RESULTS) |
| It outperforms SOTA methods such as HG-DAgger and PA-RL, with average success rates of 65% and 71.3%. | definition/direction/unit from same section | p. 6 (V. EXPERIMENT AND RESULTS) |
| For each task, we report result metrics, including the success rate, episode length, and total training time in Table I. | definition/direction/unit from same section | p. 6 (V. EXPERIMENT AND RESULTS) |
| Moreover, in scenarios with a small set of demonstrations, we find that relying on Cal-QL alone is insufficient to train an effective policy, resulting ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENT AND RESULTS) |
| For instance, HIL-SERL [20], an approach that trains policies through RL from scratch with human interventions, fails to converge to an effective policy within ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENT AND RESULTS) |
| Fig. 6: Learning curves during online training for all tasks. This figure presents the success rates, intervention rates, and episode lengths, displayed as a ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| To this end, we perform real-world experiments across eight diverse manipulation tasks, as illustrated in Figure 2. | definition/direction/unit from same section | p. 5 (V. EXPERIMENT AND RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For the online stage, we compared HIL-ConRFT with multiple baselines, including HG-DAgger [19] that incorporates human corrections to fine-tune the policy through supervised learning, ... | comparison identity and matched condition | p. 6 (V. EXPERIMENT AND RESULTS) |
| Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| We first present the experimental setup and the results for various baselines and then discuss these results and their implications. | comparison identity and matched condition | p. 5 (V. EXPERIMENT AND RESULTS) |
| In contrast, HG-DAgger achieves an average episode length of 56.3 steps, which is only 1.1x shorter than the offline baseline. | comparison identity and matched condition | p. 7 (V. EXPERIMENT AND RESULTS) |
| As shown in Table I, the VLA model fine-tuned with HIL-ConRFT achieves an average episode length of 30.7 steps, demonstrating a 1.9x shorter than ... | comparison identity and matched condition | p. 7 (V. EXPERIMENT AND RESULTS) |
| 4: Learning curves for HIL-ConRFT online fine-tuning from SFT [47] and Cal-ConRFT baselines. | comparison identity and matched condition | p. 8 (V. EXPERIMENT AND RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This ability to fine-tune the action generation while leveraging the pretrained visual components underscores the broad applicability of ConRFT. | component/input/data sensitivity | p. 8 (V. EXPERIMENT AND RESULTS) |
| Overview of Experiments Our experiments aim to evaluate our approach's effectiveness and efficiency for fine-tuning VLA models in real-world scenarios. | component/input/data sensitivity | p. 5 (V. EXPERIMENT AND RESULTS) |
| PA-RL is implemented without human intervention. | component/input/data sensitivity | p. 6 (V. EXPERIMENT AND RESULTS) |
| This stability and performance highlight the effectiveness of our approach in overcoming the limitations of existing fine-tuning methods in real-world robotic applications. | component/input/data sensitivity | p. 7 (V. EXPERIMENT AND RESULTS) |
| In this section, we validate the proposed fine-tuning framework through real-world experiments. | component/input/data sensitivity | p. 5 (V. EXPERIMENT AND RESULTS) |
| For example, we observe that for contact-rich tasks that require precise, careful manipulation, such as Insert Wheel and Hang Chinese Knot, HG-DAgger has limited ... | component/input/data sensitivity | p. 6 (V. EXPERIMENT AND RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further ... | Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 8 (V. EXPERIMENT AND RESULTS), p. 8 (V. EXPERIMENT AND RESULTS), p. 6 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS) |
| Primary metric/result | Meanwhile, RLDG achieves higher success rates using optimal data collected from RL policies, suggesting that the consistency of these RL-collected data can improve the ... | numeric claim only at cited anchor | p. 8 (V. EXPERIMENT AND RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENT AND RESULTS - extractive body cue:** Data collection and policies command actions at 10Hz.
- **p. 6 / V. EXPERIMENT AND RESULTS - extractive body cue:** This figure presents the success rates, intervention rates, and episode lengths for HIL-SERL [20], HG-DAgger [19], PA-RL [14] and our method across five representative real-world ...
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** All metrics are reported over 20 trials per task. rect action optimization using a policy-agnostic Q-function trained through Cal-QL.
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** As shown in Table I, the VLA model fine-tuned with HIL-ConRFT achieves an average episode length of 30.7 steps, demonstrating a 1.9x shorter than the ...
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** In contrast, HG-DAgger achieves an average episode length of 56.3 steps, which is only 1.1x shorter than the offline baseline.
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** Similarly, PA-RL attains an average episode length of 51.1 steps.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain. | p. 8 (VI. LIMITATIONS) |
| body limitation/failure cue | While HG-DAgger leverages human corrections to fine-tune the VLA model through supervised learning, it fails to achieve significant policy improvement and even experiences a ... | p. 6 (V. EXPERIMENT AND RESULTS) |
| body limitation/failure cue | Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | They also show the limitations of supervised methods in handling sub-optimal data and efficient policy exploration. | p. 7 (V. EXPERIMENT AND RESULTS) |
| body limitation/failure cue | However, it fails to improve the policy performance in contact-rich tasks that require precise, careful manipulation, such as Insert Wheel. | p. 7 (V. EXPERIMENT AND RESULTS) |
| body limitation/failure cue | This indicates that simply adding more human-collected demonstrations with supervised learning does not necessarily guarantee higher performance due to the inconsistent and sub-optimal actions ... | p. 8 (V. EXPERIMENT AND RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The training time includes the duration of scripted motions, policy rollouts, and onboard computations, all of which are conducted using an NVIDIA RTX A6000 ... | p. 6 (V. EXPERIMENT AND RESULTS) |
| For each task, we report result metrics, including the success rate, episode length, and total training time in Table I. | p. 6 (V. EXPERIMENT AND RESULTS) |
| In contrast, starting from a pre-trained VLA model and performing offline fine-tuning reduces the online training time and improves sample efficiency. | p. 7 (V. EXPERIMENT AND RESULTS) |
| Training Time (mins) Success Rate (%) Episode length Task HILSERL[20] HILConRFT HILSERL[20] HILConRFT Pick Banana 45 0 →15 50 →90 30.6 51.2 Put Spoon ... | p. 7 (V. EXPERIMENT AND RESULTS) |
| All metrics are reported over 20 trials per task. | p. 8 (V. EXPERIMENT AND RESULTS) |
| Specifically, we fine-tune only the action head while keeping the visual encoders and transformer backbone frozen. | p. 8 (V. EXPERIMENT AND RESULTS) |
| We initialize the policy with the pre-trained VLA model for reinforcement learning, reducing both the exploration burden and the overall online training time. | p. 3 (IV. METHOD) |
| Specifically, the VLA model with a consistency policy as the action head is given by: πψ(a/s) = fψ(ak, k/Eϕ(s)) (2) where f denotes the ... | p. 4 (IV. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VI. LIMITATIONS - extractive body cue:** Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain.
- **p. 6 / V. EXPERIMENT AND RESULTS - extractive body cue:** While HG-DAgger leverages human corrections to fine-tune the VLA model through supervised learning, it fails to achieve significant policy improvement and even experiences a performance ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, representing ...
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** They also show the limitations of supervised methods in handling sub-optimal data and efficient policy exploration.
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** However, it fails to improve the policy performance in contact-rich tasks that require precise, careful manipulation, such as Insert Wheel.
- **p. 8 / V. EXPERIMENT AND RESULTS - extractive body cue:** This indicates that simply adding more human-collected demonstrations with supervised learning does not necessarily guarantee higher performance due to the inconsistent and sub-optimal actions inherent ...

- **PDF anchors reviewed:** datasets p. 6 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 5 (V. EXPERIMENT AND RESULTS), p. 5 (V. EXPERIMENT AND RESULTS), p. 6 (V. EXPERIMENT AND RESULTS), metrics p. 8 (V. EXPERIMENT AND RESULTS), p. 8 (V. EXPERIMENT AND RESULTS), p. 6 (V. EXPERIMENT AND RESULTS), p. 6 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), baselines p. 6 (V. EXPERIMENT AND RESULTS), p. 6 (Figure/Table caption), p. 5 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 8 (V. EXPERIMENT AND RESULTS), results p. 6 (Figure/Table caption), p. 8 (V. EXPERIMENT AND RESULTS), p. 8 (V. EXPERIMENT AND RESULTS), p. 6 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
