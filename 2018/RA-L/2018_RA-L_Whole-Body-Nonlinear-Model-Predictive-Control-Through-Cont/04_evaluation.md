# Evaluation - Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1712.02889; PDF retrieval source: https://arxiv.org/pdf/1712.02889. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 5 (VI. RESULTS), p. 7 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 5 (VI. RESULTS), p. 6 (VI. RESULTS)): Fig. 8. MPC update rate as recorded during two trotting experiments on ANYmal. While iLQR achieves update rates of around 80 Hz, GNMS reaches almost 190 Hz. While the higher ...

## Evaluation Body Digest

- **p. 6 / VI. RESULTS - extractive body cue:** While the robot does not always land perfectly, the MPC controller optimizes a trajectory from the current state and tries to get back as close ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Structure of the estimation and control approach for hardware execution of the NMPC controller.
- **p. 5 / VI. RESULTS - extractive body cue:** We test a periodic trotting gait on both robots and disturb them during the tests.
- **p. 5 / VI. RESULTS - extractive body cue:** Cost function weights for the different hardware experiments plotted on a logarithmic scale.
- **p. 6 / VI. RESULTS - extractive body cue:** The robot is executing a periodic trot motion in place.
- **p. 7 / VI. RESULTS - extractive body cue:** However, we notice that below 30 Hz update rate, the performance on hardware starts to degrade significantly.
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** However, using a multiple-shooting approach allows us to parallelize the forward simulation over the individual multiple-shooting intervals.
- **p. 7 / VI. RESULTS - extractive body cue:** This is illustrated in Figure 9 which compares the costs of the trajectories obtained from both algorithms during a trot task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** IV. SOFTWARE IMPLEMENTATION (p. 3); VI. RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 8. MPC update rate as recorded during two trotting experiments on ANYmal. While iLQR achieves update rates of around 80 Hz, GNMS reaches ... | p. 7 (Figure/Table caption) |
| VI. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Also, we add a strong cost penalty on the base orientation to improve stability. | p. 5 (VI. RESULTS) |
| VI. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As a result, the controller achieves a constant apex height but drifts slightly in x and y directions. | p. 7 (VI. RESULTS) |
| IV. SOFTWARE IMPLEMENTATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | The linearization of our dynamic system is performed with Auto-Diff and code-generation described in detail in [22], which provides the same accuracy as analytic ... | p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| VI. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Note that running only a single solver iteration before updating the state measurement results in better overall performance than running multiple iterations and letting ... | p. 5 (VI. RESULTS) |

## Dataset / Benchmark Role

- **p. 6 / VI. RESULTS - extractive body cue:** While the robot does not always land perfectly, the MPC controller optimizes a trajectory from the current state and tries to get back as close ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Structure of the estimation and control approach for hardware execution of the NMPC controller.
- **p. 5 / VI. RESULTS - extractive body cue:** We test a periodic trotting gait on both robots and disturb them during the tests.
- **p. 5 / VI. RESULTS - extractive body cue:** Cost function weights for the different hardware experiments plotted on a logarithmic scale.
- **p. 6 / VI. RESULTS - extractive body cue:** The robot is executing a periodic trot motion in place.
- **p. 7 / VI. RESULTS - extractive body cue:** However, we notice that below 30 Hz update rate, the performance on hardware starts to degrade significantly.
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** However, using a multiple-shooting approach allows us to parallelize the forward simulation over the individual multiple-shooting intervals.
- **p. 7 / VI. RESULTS - extractive body cue:** This is illustrated in Figure 9 which compares the costs of the trajectories obtained from both algorithms during a trot task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. The quadrupeds HyQ-blue (left front) and ANYmal (right), which served as test platforms for our MPC experiments. In recent years, there has been ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Structure of the estimation and control approach for hardware execution of the NMPC controller. Estimators estimate ground height and base state information. The ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Cost function weights for the different hardware experiments plotted on a logarithmic scale. All weighting matrices are diagonal and thus the weights illustrated ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Plots of the deviation of the orientation and position offset during trotting experiments on HyQ. In the cost function, we penalize orientation stronger ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Base orientation (top) and position (bottom) of ANYmal during a trot. At t = 2.8s we placed a wooden stick below one foot ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6. Joint torques of ANYmal during a repeated squat jump. The torques stay well below the physical torque limit of 40 Nm. Furthermore, the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Base position and linear velocity of ANYmal during a repeated squat jump. We mostly penalize base orientation and linear velocities to obtain straight ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8. MPC update rate as recorded during two trotting experiments on ANYmal. While iLQR achieves update rates of around 80 Hz, GNMS reaches almost ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | While the robot does not always land perfectly, the MPC controller optimizes a trajectory from the current state and tries to get back as ... | embodiment, simulator version and control stack | p. 6 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Task/environment | Structure of the estimation and control approach for hardware execution of the NMPC controller. | reset, timeout, object/scene variation | p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 5 (VI. RESULTS) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Even placing planks under single feet does not deteriorate performance. | definition/direction/unit from same section | p. 5 (VI. RESULTS) |
| However, we notice that below 30 Hz update rate, the performance on hardware starts to degrade significantly. | definition/direction/unit from same section | p. 7 (VI. RESULTS) |
| While GNMS offers a higher update rate, it is not very noticeable in performance such that iLQR performs similarly well. | definition/direction/unit from same section | p. 7 (VI. RESULTS) |
| The linearization of our dynamic system is performed with Auto-Diff and code-generation described in detail in [22], which provides the same accuracy as analytic ... | definition/direction/unit from same section | p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| The performance of our algorithms is assessed on both quadrupeds. | definition/direction/unit from same section | p. 5 (VI. RESULTS) |
| These plots illustrate how the MPC controller deals with disturbances. | definition/direction/unit from same section | p. 6 (VI. RESULTS) |
| We measured the rate of incoming trajectories that the tracking controller received. | definition/direction/unit from same section | p. 6 (VI. RESULTS) |
| Multithreading and Vectorization Another important factor for obtaining best performance is multi-threading. | definition/direction/unit from same section | p. 4 (IV. SOFTWARE IMPLEMENTATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to ANYmal the magnitude of the deviations is slightly larger. | comparison identity and matched condition | p. 6 (VI. RESULTS) |
| Compared to HyQ the deviations of the base orientation and position are much smaller. | comparison identity and matched condition | p. 6 (VI. RESULTS) |
| Compared to [15], which is using the same algorithm but requires around 50 ms per iteration, our solver is about 300% faster for the ... | comparison identity and matched condition | p. 7 (VI. RESULTS) |
| framework is lean compared to sophisticated physics engines and produces fast to evaluate, hard realtime capable code. | comparison identity and matched condition | p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| The symplectic integrator allows us to increase the integration step size by a factor of four compared to explicit schemes [17]. | comparison identity and matched condition | p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| HyQ can be perturbed significantly both on the base and the legs without reacting stiffly. | comparison identity and matched condition | p. 5 (VI. RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The cost and sensitivity computation, which can be distributed among all available cores, is parallelizable for all our algorithm variants. | component/input/data sensitivity | p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Therefore, we compute them exactly by integrating a corresponding sensitivity ODE. | component/input/data sensitivity | p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| HyQ can be perturbed significantly both on the base and the legs without reacting stiffly. | component/input/data sensitivity | p. 5 (VI. RESULTS) |
| In previous work [17], we have demonstrated that our approach can also discover a trotting gait without swing leg costs. | component/input/data sensitivity | p. 5 (VI. RESULTS) |
| The controller is able to return to a periodic motion after the disturbance is removed. | component/input/data sensitivity | p. 6 (VI. RESULTS) |
| On the torque level the robot stayed well below the admissible torque level of ANYmal (40 Nm) without imposing additional constraints. | component/input/data sensitivity | p. 6 (VI. RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts. | Fig. 8. MPC update rate as recorded during two trotting experiments on ANYmal. While iLQR achieves update rates of around 80 Hz, GNMS reaches ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 5 (VI. RESULTS), p. 7 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 5 (VI. RESULTS), p. 6 (VI. RESULTS) |
| Primary metric/result | Also, we add a strong cost penalty on the base orientation to improve stability. | numeric claim only at cited anchor | p. 5 (VI. RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / VI. RESULTS - extractive body cue:** In all experiments, we employ a time horizon of 500 ms, a control discretization of 4 ms and an integration rate of 1 ms for ...
- **p. 6 / VI. RESULTS - extractive body cue:** At t = 2.8s we placed a wooden stick below one foot which acted as heavy disturbance on the system.
- **p. 6 / VI. RESULTS - extractive body cue:** At t = 2.8s we placed a wooden plank below one of ANYmal's feet.
- **p. 6 / VI. RESULTS - extractive body cue:** We enforce jumps every 2 seconds, starting at t = 1s.
- **p. 6 / VI. RESULTS - extractive body cue:** It can be seen that our solver runs at around 80 Hz for when using the iLQRalgorithm and at 175 Hz when using Gauss-Newton MultipleShooting.
- **p. 7 / VI. RESULTS - extractive body cue:** While iLQR achieves update rates of around 80 Hz, GNMS reaches almost 190 Hz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers. | p. 3 (IV. SOFTWARE IMPLEMENTATION) |
| body limitation/failure cue | Also, many computational routines such as integrating a differential equation over time, are naturally sequential operations that cannot be parallelized easily. | p. 3 (IV. SOFTWARE IMPLEMENTATION) |
| body limitation/failure cue | Furthermore, while most tasks by design stayed within the physical limitations of the platforms, GNMS would allow us to handle constraints such as torque ... | p. 7 (VII. SUMMARY AND OUTLOOK) |
| body limitation/failure cue | The resulting overall controller is stable and can robustly handle aforementioned disturbances. | p. 5 (VI. RESULTS) |
| body limitation/failure cue | Also here we observe that the controller is robust to disturbances. | p. 6 (VI. RESULTS) |
| body limitation/failure cue | We expect that a longer time horizon could show more elaborate disturbance rejection and recovery behavior since it offers more flexibility and predictive capabilities ... | p. 7 (VII. SUMMARY AND OUTLOOK) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Therefore, we use RobCoGen [30], an efficient code generation framework for modelling Rigid Body Dynamics. | p. 3 (IV. SOFTWARE IMPLEMENTATION) |
| In this implementation, we switched to AVX [34] instructions. | p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| In a previous implementation [17], we had already used SSE [34] Fig. | p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| This results from a more efficient solver implementation, optimized vectorization, faster computation of the dynamics due to a simpler contact model as well as ... | p. 7 (VI. RESULTS) |
| It shows two forward integration steps during the algorithm. | p. 3 (III. NMPC APPROACH) |
| Cost function weights for the different hardware experiments plotted on a logarithmic scale. | p. 5 (VI. RESULTS) |
| We run a so called "real-time iteration scheme" [23], where we apply the optimized trajectory after a single iteration. | p. 5 (VI. RESULTS) |
| For all timings and experiments, the NMPC solver is run on an Intel Core i7 4790 quadcore PC with 3.6 GHz. | p. 6 (VI. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Also, many computational routines such as integrating a differential equation over time, are naturally sequential operations that cannot be parallelized easily.
- **p. 7 / VII. SUMMARY AND OUTLOOK - extractive body cue:** Furthermore, while most tasks by design stayed within the physical limitations of the platforms, GNMS would allow us to handle constraints such as torque limitations ...
- **p. 5 / VI. RESULTS - extractive body cue:** The resulting overall controller is stable and can robustly handle aforementioned disturbances.
- **p. 6 / VI. RESULTS - extractive body cue:** Also here we observe that the controller is robust to disturbances.
- **p. 7 / VII. SUMMARY AND OUTLOOK - extractive body cue:** We expect that a longer time horizon could show more elaborate disturbance rejection and recovery behavior since it offers more flexibility and predictive capabilities to ...

- **PDF anchors reviewed:** datasets p. 6 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 5 (VI. RESULTS), p. 5 (VI. RESULTS), p. 6 (VI. RESULTS), p. 7 (VI. RESULTS), metrics p. 5 (VI. RESULTS), p. 7 (VI. RESULTS), p. 7 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 5 (VI. RESULTS), p. 6 (VI. RESULTS), baselines p. 6 (VI. RESULTS), p. 6 (VI. RESULTS), p. 7 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 5 (VI. RESULTS), results p. 7 (Figure/Table caption), p. 5 (VI. RESULTS), p. 7 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 5 (VI. RESULTS), p. 6 (VI. RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
