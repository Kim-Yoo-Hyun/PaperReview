# Evaluation - Any-point Trajectory Modeling for Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p092.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p092.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 2 (2) Through extensive experiments on simulated bench), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption)): Fig. 6: We implement ATM Diffusion Policy by adding the predicted future trajectories as additional conditioning and show consistent improvement over the base diffusion policies across the benchmark suites. TABLE ...

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTS - extractive body cue:** All methods are trained on 10 action-labeled demonstration trajectories and 50 action-free video demonstration trajectories of the robot for each task, amounting to 500 videos ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We compare with baselines on over one hundred language-conditioned manipulation tasks in the LIBERO benchmark [27].
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Success rate of our policy trained with 4%, 10% and 20% action-labeled demos. Our policy trained with only 4% demos performs comparably to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 10: We plot the success rates of the policies learned with predicted trajectories of different lengths. Generally, longer trajectory length improves the performance, but ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: We implement ATM Diffusion Policy by adding the predicted future trajectories as additional conditioning and show consistent improvement over the base diffusion policies ...
- **p. 2 / 2) Through extensive experiments on simulated bench - extractive body cue:** marks and in the real world, we demonstrate that our method can effectively utilize video data in pre-training and significantly outperform various video pre-training baselines ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We compare with baselines on each suite separately.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Learning robotic skills from human videos for three tasks. We collect 100 videos of a human performing the tasks directly and 10 teleoperation ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 2) Through extensive experiments on simulated bench (p. 2); V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6: We implement ATM Diffusion Policy by adding the predicted future trajectories as additional conditioning and show consistent improvement over the base diffusion ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 10: We plot the success rates of the policies learned with predicted trajectories of different lengths. Generally, longer trajectory length improves the performance, ... | p. 9 (Figure/Table caption) |
| 2) Through extensive experiments on simulated bench | EMPIRICAL / REAL-ROBOT OR HARDWARE | marks and in the real world, we demonstrate that our method can effectively utilize video data in pre-training and significantly outperform various video pre-training ... | p. 2 (2) Through extensive experiments on simulated bench) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 9: Success rate of our policy trained with 4%, 10% and 20% action-labeled demos. Our policy trained with only 4% demos performs comparably ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Real robot experiments on a dining table setup consisting of five tasks. The left figure shows our real-world setup and the tasks. ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTS - extractive body cue:** All methods are trained on 10 action-labeled demonstration trajectories and 50 action-free video demonstration trajectories of the robot for each task, amounting to 500 videos ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We compare with baselines on over one hundred language-conditioned manipulation tasks in the LIBERO benchmark [27].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Given a task instruction and the initial positions of any set of points in an image frame, our Any-point Trajectory Model (ATM) can ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of our framework. (a) In the first stage, given an action-free video dataset, we first sample 2D points on one video frame ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: A visual illustration of the architecture of the track- guided policy. Given the current observation and the predicted tracks from the frozen pre-trained ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: We compare with state-of-the-art video pre-training methods on language-conditioned manipulation tasks in the LIBERO benchmark [27]. (a) Visualization of the LIBERO tasks separated ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Real robot experiments on a dining table setup consisting of five tasks. The left figure shows our real-world setup and the tasks. The ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: We implement ATM Diffusion Policy by adding the predicted future trajectories as additional conditioning and show consistent improvement over the base diffusion policies ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Learning robotic skills from human videos for three tasks. We collect 100 videos of a human performing the tasks directly and 10 teleoperation ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Cross-morphology skill transfer for a pick-and-place task. Here, we collect 160 action-free videos of a Franka arm and 10 action-labeled demonstrations from a ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | All methods are trained on 10 action-labeled demonstration trajectories and 50 action-free video demonstration trajectories of the robot for each task, amounting to 500 ... | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Task/environment | We compare with baselines on over one hundred language-conditioned manipulation tasks in the LIBERO benchmark [27]. | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTS) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 3 (III. PRELIMINARY), p. 4 (IV. METHOD) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 4 (IV. METHOD), p. 3 (IV. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 9: Success rate of our policy trained with 4%, 10% and 20% action-labeled demos. Our policy trained with only 4% demos performs comparably ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 10: We plot the success rates of the policies learned with predicted trajectories of different lengths. Generally, longer trajectory length improves the performance, ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 6: We implement ATM Diffusion Policy by adding the predicted future trajectories as additional conditioning and show consistent improvement over the base diffusion ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| marks and in the real world, we demonstrate that our method can effectively utilize video data in pre-training and significantly outperform various video pre-training ... | definition/direction/unit from same section | p. 2 (2) Through extensive experiments on simulated bench) |
| We compare with baselines on each suite separately. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Fig. 7: Learning robotic skills from human videos for three tasks. We collect 100 videos of a human performing the tasks directly and 10 ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 3: A visual illustration of the architecture of the track- guided policy. Given the current observation and the predicted tracks from the frozen ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 4: We compare with state-of-the-art video pre-training methods on language-conditioned manipulation tasks in the LIBERO benchmark [27]. (a) Visualization of the LIBERO tasks ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 4: We compare with state-of-the-art video pre-training methods on language-conditioned manipulation tasks in the LIBERO benchmark [27]. (a) Visualization of the LIBERO tasks ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| marks and in the real world, we demonstrate that our method can effectively utilize video data in pre-training and significantly outperform various video pre-training ... | comparison identity and matched condition | p. 2 (2) Through extensive experiments on simulated bench) |
| We perform experiments to answer the following questions: • How does ATM compare with state-of-the-art video pretraining and behaviour cloning baselines for learning from ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| Fig. 5: Real robot experiments on a dining table setup consisting of five tasks. The left figure shows our real-world setup and the tasks. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We compare with baselines on each suite separately. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| Fig. 8: Cross-morphology skill transfer for a pick-and-place task. Here, we collect 160 action-free videos of a Franka arm and 10 action-labeled demonstrations from ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Finally, we present ablation results in Sec. | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| Fig. 9: Success rate of our policy trained with 4%, 10% and 20% action-labeled demos. Our policy trained with only 4% demos performs comparably ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Fig. 7: Learning robotic skills from human videos for three tasks. We collect 100 videos of a human performing the tasks directly and 10 ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Fig. 8: Cross-morphology skill transfer for a pick-and-place task. Here, we collect 160 action-free videos of a Franka arm and 10 action-labeled demonstrations from ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We perform experiments to answer the following questions: • How does ATM compare with state-of-the-art video pretraining and behaviour cloning baselines for learning from ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| Fig. 2: Overview of our framework. (a) In the first stage, given an action-free video dataset, we first sample 2D points on one video ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our main contributions below: 1) We propose an Any-point Trajectory Model, a simple and novel framework that bridges video pre-training to policy ... | Fig. 6: We implement ATM Diffusion Policy by adding the predicted future trajectories as additional conditioning and show consistent improvement over the base diffusion ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 2 (2) Through extensive experiments on simulated bench), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Fig. 10: We plot the success rates of the policies learned with predicted trajectories of different lengths. Generally, longer trajectory length improves the performance, ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Each suite has 10 tasks, except LIBERO-90 which contains 90 tasks.
- **p. 4 / IV. METHOD - extractive body cue:** Instead, we find it sufficient to simply use a fixed set of 32 points on a grid for the policy.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Please see our video for failure cases of a video prediction model. | p. 7 (1) BC denotes the vanilla behavioral cloning which trains) |
| body limitation/failure cue | Fig. 2: Overview of our framework. (a) In the first stage, given an action-free video dataset, we first sample 2D points on one video ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | On the other hand, as the number of action-labeled trajectories is small, BC baselines that only use action-labeled trajectories fail. | p. 8 (160 Franka Videos) |
| body limitation/failure cue | Experiments show that training the trajectory model on additional cross-embodiment videos makes the trajectory prediction more robust and accurate, significantly improving policy learning. | p. 8 (160 Franka Videos) |
| body limitation/failure cue | The subgoal prediction is more robust as it is trained on a larger video dataset. | p. 9 (160 Franka Videos) |
| body limitation/failure cue | We hypothesize that the longer tracks might interfere with the learning of inverse dynamics due to noise. | p. 9 (160 Franka Videos) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| More formally, given an image observation ot at timestep t, any set of 2D query points on the image frame pt = {pt,k}K k=1, ... | p. 3 (IV. METHOD) |
| For the language instruction, we use a pre-trained BERT [9] encoder. | p. 4 (IV. METHOD) |
| Finally, we decode the track tokens into future trajectories of the corresponding points. | p. 4 (IV. METHOD) |
| A detailed architecture diagram and hyperparameters are available in the appendix. | p. 5 (IV. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 1) BC denotes the vanilla behavioral cloning which trains - extractive body cue:** Please see our video for failure cases of a video prediction model.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of our framework. (a) In the first stage, given an action-free video dataset, we first sample 2D points on one video frame ...
- **p. 8 / 160 Franka Videos - extractive body cue:** On the other hand, as the number of action-labeled trajectories is small, BC baselines that only use action-labeled trajectories fail.
- **p. 8 / 160 Franka Videos - extractive body cue:** Experiments show that training the trajectory model on additional cross-embodiment videos makes the trajectory prediction more robust and accurate, significantly improving policy learning.
- **p. 9 / 160 Franka Videos - extractive body cue:** The subgoal prediction is more robust as it is trained on a larger video dataset.
- **p. 9 / 160 Franka Videos - extractive body cue:** We hypothesize that the longer tracks might interfere with the learning of inverse dynamics due to noise.

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), metrics p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (2) Through extensive experiments on simulated bench), p. 5 (V. EXPERIMENTS), p. 8 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 2 (2) Through extensive experiments on simulated bench), p. 5 (V. EXPERIMENTS), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 8 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 2 (2) Through extensive experiments on simulated bench), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
