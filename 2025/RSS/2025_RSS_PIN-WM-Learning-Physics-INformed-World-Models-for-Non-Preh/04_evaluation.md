# Evaluation - PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p153.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p153.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), p. 7 (A. Evaluations in Simulation), p. 6 (IV. RESULTS AND EVALUATIONS), p. 6 (IV. RESULTS AND EVALUATIONS)): All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, We also conduct an ablation study ...

## Evaluation Body Digest

- **p. 7 / A. Evaluations in Simulation - extractive body cue:** Experiment setup: n simulation, we collect a single task-agnostc trajectory thatthe target object is pushed forward along a straight line by the robot end-effector for ...
- **p. 8 / B. Evaluations in Real-World - extractive body cue:** Experiment setup: Our hardware setup consists of robot, an eye-in-hand camera, and an eye-to-hand camera, as shown in Figure 5.
- **p. 6 / IV. RESULTS AND EVALUATIONS - extractive body cue:** ‘We evaluate our method on rigid body motion control. ‘The robot's objective is to perform a sequence of non-prehensile actions to move an object into ...
- **p. 6 / IV. RESULTS AND EVALUATIONS - extractive body cue:** Simulators provide ground truth for evaluating system identification accuracy and hence offer comprehensive answers to the first three questions, while the real-world tests are used ...
- **p. 8 / B. Evaluations in Real-World - extractive body cue:** The robot then moves around the object and captures the time-lapse video sequence
- **p. 14 / A. Implementation Details for Baselines - extractive body cue:** The reward signal for policy learning is a handcrafted function to encourage the robot to push the object toward the target pose: r= -dy - ...
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** The initial object pose is randomized for each episode.
- **p. 14 / A. Implementation Details for Baselines - extractive body cue:** Diffusion Policy is trained with successful trajectories collected from ‘expert policies trained in the environment with GT physical parameters, without any randomization,

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** IV. RESULTS AND EVALUATIONS (p. 6); A. Evaluations in Simulation (p. 7); B. Evaluations in Real-World (p. 8); A. Implementation Details for Baselines (p. 14); B. More Experimental Results (p. 14); C. Further Real-World Evaluations (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A. Evaluations in Simulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, ... | p. 7 (A. Evaluations in Simulation) |
| A. Evaluations in Simulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Without PADC, our method still outperforms others, although with a performance decrease. | p. 8 (A. Evaluations in Simulation) |
| A. Evaluations in Simulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves the best performance for both non-prehensile manipulation tasks, thanks to the accurate system identification of PIN-WM and the meaningful digital cousins ... | p. 8 (A. Evaluations in Simulation) |
| A. Evaluations in Simulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We measure the success rate Suee % ‘of a policy if the task is completed within a threshold of 100 steps for push and ... | p. 7 (A. Evaluations in Simulation) |
| IV. RESULTS AND EVALUATIONS | EMPIRICAL / REAL-ROBOT OR HARDWARE | + Does our method outperform other Real2Sim2Real meth | p. 6 (IV. RESULTS AND EVALUATIONS) |

## Dataset / Benchmark Role

- **p. 7 / A. Evaluations in Simulation - extractive body cue:** Experiment setup: n simulation, we collect a single task-agnostc trajectory thatthe target object is pushed forward along a straight line by the robot end-effector for ...
- **p. 8 / B. Evaluations in Real-World - extractive body cue:** Experiment setup: Our hardware setup consists of robot, an eye-in-hand camera, and an eye-to-hand camera, as shown in Figure 5.
- **p. 6 / IV. RESULTS AND EVALUATIONS - extractive body cue:** ‘We evaluate our method on rigid body motion control. ‘The robot's objective is to perform a sequence of non-prehensile actions to move an object into ...
- **p. 6 / IV. RESULTS AND EVALUATIONS - extractive body cue:** Simulators provide ground truth for evaluating system identification accuracy and hence offer comprehensive answers to the first three questions, while the real-world tests are used ...
- **p. 8 / B. Evaluations in Real-World - extractive body cue:** The robot then moves around the object and captures the time-lapse video sequence
- **p. 14 / A. Implementation Details for Baselines - extractive body cue:** The reward signal for policy learning is a handcrafted function to encourage the robot to push the object toward the target pose: r= -dy - ...
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** The initial object pose is randomized for each episode.
- **p. 14 / A. Implementation Details for Baselines - extractive body cue:** Diffusion Policy is trained with successful trajectories collected from ‘expert policies trained in the environment with GT physical parameters, without any randomization,

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: PIN-WM is Jearned from few-shot and task-agnostic physical Interaction trajectories (random pushes of the blocks in this example), through end-to-end differentiable identification of ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Our Real2Sim2Real framework for learning non-prehensile manipulation policies. (a) The robot in the target domain moves around the object, capturing mul-view observations to ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: Manipulation trajectories in simulation obtained by our ‘method for both push and flip tasks.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Our real-world experiment setup.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: Real-world trajectories of different methods on the push task
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 8: Real-world trajectories of different methods on the flip task.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 10: Push cube object on a slippery plane.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 1: Flip a multicolored cube to change its top-surface color.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Experiment setup: n simulation, we collect a single task-agnostc trajectory thatthe target object is pushed forward along a straight line by the robot end-effector ... | embodiment, simulator version and control stack | p. 7 (A. Evaluations in Simulation), p. 8 (B. Evaluations in Real-World) |
| Task/environment | Experiment setup: Our hardware setup consists of robot, an eye-in-hand camera, and an eye-to-hand camera, as shown in Figure 5. | reset, timeout, object/scene variation | p. 8 (B. Evaluations in Real-World), p. 6 (IV. RESULTS AND EVALUATIONS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 5 (B. Physics-INformed World Model) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 14 (A. Implementation Details for Baselines), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| All RL-based policies are trained using PPO [66], with the same model architecture, reward function, hyperparameters, and stopping criterion based on the success rate. | definition/direction/unit from same section | p. 14 (A. Implementation Details for Baselines) |
| All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, ... | definition/direction/unit from same section | p. 7 (A. Evaluations in Simulation) |
| We evaluate the accuracy of a world model using ‘one-step error (44] which measures the distance between the final object states after applying one ... | definition/direction/unit from same section | p. 7 (A. Evaluations in Simulation) |
| Simulators provide ground truth for evaluating system identification accuracy and hence offer comprehensive answers to the first three questions, while the real-world tests are ... | definition/direction/unit from same section | p. 6 (IV. RESULTS AND EVALUATIONS) |
| Fig, 4: Transition and orientation errors of push task during training. | definition/direction/unit from same section | p. 8 (A. Evaluations in Simulation) |
| ASID [53] shows lower accuracy compared to PIN-WM in both push and flip tasks, since itis difficult for gradient-free optimization to | definition/direction/unit from same section | p. 8 (A. Evaluations in Simulation) |
| The reward signal for policy learning is a handcrafted function to encourage the robot to push the object toward the target pose: r= -dy ... | definition/direction/unit from same section | p. 14 (A. Implementation Details for Baselines) |
| + Does PIN-WM achieve more accurate system identifica | definition/direction/unit from same section | p. 6 (IV. RESULTS AND EVALUATIONS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Note that all physics-based methods being compared are trained with the same task-agnostic trajectories as PIN-WM, for fair comparison. | comparison identity and matched condition | p. 7 (A. Evaluations in Simulation) |
| Without PADC, our method still outperforms others, although with a performance decrease. | comparison identity and matched condition | p. 8 (A. Evaluations in Simulation) |
| tion compared to existing approaches? | comparison identity and matched condition | p. 6 (IV. RESULTS AND EVALUATIONS) |
| + Does our method outperform other Real2Sim2Real meth | comparison identity and matched condition | p. 6 (IV. RESULTS AND EVALUATIONS) |
| More implementation details of baseline methods are provided in Appendix A. | comparison identity and matched condition | p. 7 (A. Evaluations in Simulation) |
| ASID [53] shows lower accuracy compared to PIN-WM in both push and flip tasks, since itis difficult for gradient-free optimization to | comparison identity and matched condition | p. 8 (A. Evaluations in Simulation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, ... | component/input/data sensitivity | p. 7 (A. Evaluations in Simulation) |
| We set a variant with fixed, random physics and rendering parameters where no system identification or randomization is involved, denoted as Random. | component/input/data sensitivity | p. 7 (A. Evaluations in Simulation) |
| Without PADC, our method still outperforms others, although with a performance decrease. | component/input/data sensitivity | p. 8 (A. Evaluations in Simulation) |
| Diffusion Policy is trained with successful trajectories collected from ‘expert policies trained in the environment with GT physical parameters, without any randomization, | component/input/data sensitivity | p. 14 (A. Implementation Details for Baselines) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations. | All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), p. 7 (A. Evaluations in Simulation), p. 6 (IV. RESULTS AND EVALUATIONS), p. 6 (IV. RESULTS AND EVALUATIONS) |
| Primary metric/result | Without PADC, our method still outperforms others, although with a performance decrease. | numeric claim only at cited anchor | p. 8 (A. Evaluations in Simulation) |

- Numeric sentences retained from the body:
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** We measure the success rate Suee % ‘of a policy if the task is completed within a threshold of 100 steps for push and 25 ...
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** Dreamer V2 (27) 1 99 / o& 280 Difsion Policy (11) / 13% 9k / 10% 233 RolboGsim [4S] we 26 / 2m 205 Domain ...
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** Given their strong reliance oon data quantity, we provide 100 task-agnostic trajectories.
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** Comparisons on policy performance: We conduct 100 episodes of tests for each method and report the comparison results in Table I.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function ... | p. 7 (A. Evaluations in Simulation) |
| body limitation/failure cue | The purely data-driven world model Dreamer V2 [27], albeit having access to more task-agnostic data, fails to accurately approximate the dynamics of the target ... | p. 8 (A. Evaluations in Simulation) |
| body limitation/failure cue | Fig. 10: Push cube object on a slippery plane. | p. 14 (Figure/Table caption) |
| body limitation/failure cue | We can observe that Dreamer V2 quickly converges on the training dataset, but it does not generalize well on the test dataset. | p. 8 (A. Evaluations in Simulation) |
| body limitation/failure cue | ‘¢ Methods that rely purely on data. representative is the well-known Dreamer V2 [27], which is a latent-space dynamies model from data for handling ... | p. 7 (A. Evaluations in Simulation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Al the baselines are implemented carefully to ensure fair ‘comparison, We used the official implementations with default hyperparameters for Diffusion Policy [11], 2D Physics ... | p. 14 (A. Implementation Details for Baselines) |
| More implementation details of baseline methods are provided in Appendix A. | p. 7 (A. Evaluations in Simulation) |
| We also consider the required number of steps to complete a task, denoted as #Steps. | p. 7 (A. Evaluations in Simulation) |
| Experiment setup: Our hardware setup consists of robot, an eye-in-hand camera, and an eye-to-hand camera, as shown in Figure 5. | p. 8 (B. Evaluations in Real-World) |
| All RL-based policies are trained using PPO [66], with the same model architecture, reward function, hyperparameters, and stopping criterion based on the success rate. | p. 14 (A. Implementation Details for Baselines) |
| We propagate recursive derivatives of Equation 11 across H/h simulation time steps and optimize 8. | p. 6 (B. Physics-INformed World Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / A. Evaluations in Simulation - extractive body cue:** Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function Z ...
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** The purely data-driven world model Dreamer V2 [27], albeit having access to more task-agnostic data, fails to accurately approximate the dynamics of the target domain, ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 10: Push cube object on a slippery plane.
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** We can observe that Dreamer V2 quickly converges on the training dataset, but it does not generalize well on the test dataset.
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** ‘¢ Methods that rely purely on data. representative is the well-known Dreamer V2 [27], which is a latent-space dynamies model from data for handling high-dimensional ...

- **PDF anchors reviewed:** datasets p. 7 (A. Evaluations in Simulation), p. 8 (B. Evaluations in Real-World), p. 6 (IV. RESULTS AND EVALUATIONS), p. 6 (IV. RESULTS AND EVALUATIONS), p. 8 (B. Evaluations in Real-World), p. 14 (A. Implementation Details for Baselines), metrics p. 14 (A. Implementation Details for Baselines), p. 7 (A. Evaluations in Simulation), p. 7 (A. Evaluations in Simulation), p. 6 (IV. RESULTS AND EVALUATIONS), p. 8 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), baselines p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), p. 6 (IV. RESULTS AND EVALUATIONS), p. 6 (IV. RESULTS AND EVALUATIONS), p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), results p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), p. 7 (A. Evaluations in Simulation), p. 6 (IV. RESULTS AND EVALUATIONS), p. 6 (IV. RESULTS AND EVALUATIONS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
