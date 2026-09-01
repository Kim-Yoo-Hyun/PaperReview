# Evaluation - Learning Humanoid Standing-up Control across Diverse Postures

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p064.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p064.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (B. Main Results), p. 6 (B. Main Results), p. 8 (A. Main Results), p. 8 (A. Main Results)): key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same reward functions, the performance of the single critic version of HOST deteriorates ...

## Evaluation Body Digest

- **p. 8 / A. Main Results - extractive PDF cue:** this conclusion, with our approach achieving a 100% success rate and high motion smoothness across all scenes.' Generalization to outdoor environments (Viz.
- **p. 9 / B. Sim-to-real Analysis - extractive PDF cue:** Phase plot. ‘To further investigate the sources of this gap, we ‘examine the phase plots of the knee and hip roll joints. ‘These joints are ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** During real-world deployment, we observe a significant torque gap between simulation and reality (see Fig.
- **p. 13 / B. More Implementation Details - extractive PDF cue:** During the hardware deployment, the stiffness of hip and knee joints are amplified to 1.5 times than the simulation ones, similar to G1, We present ...
- **p. 6 / B. Main Results - extractive PDF cue:** While the robot can learn to stand up without action bounds (HOST-w/o-Bound), its movements are excessively violent, as indicated by three performance metrics.
- **p. 6 / B. Main Results - extractive PDF cue:** Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a ...
- **p. 8 / A. Main Results - extractive PDF cue:** Additionally, our controllers successfully handle more complex scenarios, including stone platforms and tree-leaning postures, demonstrating their adaptability to diverse real-world conditions.
- **p. 12 / B. More Implementation Details - extractive PDF cue:** In simulation, the stiffness values are set as 100 for the upper body, 40 for the ankle, 150 for the hip, and

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** B. Main Results (p. 6); VI. REAL ROBOT EXPERIMENTS (p. 8); A. Main Results (p. 8); A. More Experimental Details (p. 12); B. More Implementation Details (p. 12).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B. Main Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same reward functions, the performance of the ... | p. 6 (B. Main Results) |
| B. Main Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | HOST with short history length underperforms in contact-rich scenarios, such as the Wall terrain, In contrast, a longer history length improves performance, though it ... | p. 6 (B. Main Results) |
| A. Main Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | this conclusion, with our approach achieving a 100% success rate and high motion smoothness across all scenes.' Generalization to outdoor environments (Viz. | p. 8 (A. Main Results) |
| A. Main Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Smooth regularization improves motions (Fig. | p. 8 (A. Main Results) |

## Dataset / Benchmark Role

- **p. 8 / A. Main Results - extractive PDF cue:** this conclusion, with our approach achieving a 100% success rate and high motion smoothness across all scenes.' Generalization to outdoor environments (Viz.
- **p. 9 / B. Sim-to-real Analysis - extractive PDF cue:** Phase plot. ‘To further investigate the sources of this gap, we ‘examine the phase plots of the knee and hip roll joints. ‘These joints are ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** During real-world deployment, we observe a significant torque gap between simulation and reality (see Fig.
- **p. 13 / B. More Implementation Details - extractive PDF cue:** During the hardware deployment, the stiffness of hip and knee joints are amplified to 1.5 times than the simulation ones, similar to G1, We present ...
- **p. 6 / B. Main Results - extractive PDF cue:** While the robot can learn to stand up without action bounds (HOST-w/o-Bound), its movements are excessively violent, as indicated by three performance metrics.
- **p. 6 / B. Main Results - extractive PDF cue:** Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a ...
- **p. 8 / A. Main Results - extractive PDF cue:** Additionally, our controllers successfully handle more complex scenarios, including stone platforms and tree-leaning postures, demonstrating their adaptability to diverse real-world conditions.
- **p. 12 / B. More Implementation Details - extractive PDF cue:** In simulation, the stiffness values are set as 100 for the upper body, 40 for the ankle, 150 for the hip, and

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview. (a) Our propose framework HOST
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Framework overview. (2) We train policies in simulation from scratch vwith multiple cris. and motion consrsnts operationalized by rewards, Smoothness regularization, and action ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5: Robustness analysis in simulation. Evaluation of contol policies under four environmental disturbances demonstrates the robustness of our contol
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: Trade-off analysis in simulation, Trad-offs between motion sped, smoothness, and energy across trains. Resulis show the inverse speed Smoothness relationship, indicating the importance ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Snapshot of rea robot motion. We dretly transfer our policies from simulation to fou real-world scenes that correspond to fou simulation teas
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 10: Emergent properties in real robot experiments (a) our controllers show great robusiness (0 th ground, and payload mass upto [2kg (2x mass of ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 9. Our results demonstrate that the introduction of these randomization terms significantly reduces the sim-to-real gap, particularly with respect to the Center of Mass ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 12: More diverse postures. HoST can learn across prone postures 02 the ground. The lara policies can also handle side-ying postr

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | this conclusion, with our approach achieving a 100% success rate and high motion smoothness across all scenes.' Generalization to outdoor environments (Viz. | embodiment, simulator version and control stack | p. 8 (A. Main Results), p. 9 (B. Sim-to-real Analysis) |
| Task/environment | Phase plot. ‘To further investigate the sources of this gap, we ‘examine the phase plots of the knee and hip roll joints. ‘These joints ... | reset, timeout, object/scene variation | p. 9 (B. Sim-to-real Analysis), p. 13 (B. More Implementation Details) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same reward functions, the performance of the ... | definition/direction/unit from same section | p. 6 (B. Main Results) |
| With action bounds, HOST demonstrates smoother motions and higher success rates. | definition/direction/unit from same section | p. 6 (B. Main Results) |
| this conclusion, with our approach achieving a 100% success rate and high motion smoothness across all scenes.' Generalization to outdoor environments (Viz. | definition/direction/unit from same section | p. 8 (A. Main Results) |
| Outside this region, the reward smoothly decreases according to a Gaussian function, reaching the value v ata distance determined by the margin m. | definition/direction/unit from same section | p. 12 (B. More Implementation Details) |
| We present the complete set of ward functions and their detailed descriptions in Tulble V1 Several regularization reward terms are adapted from prior work ... | definition/direction/unit from same section | p. 12 (B. More Implementation Details) |
| Our control - Jes demonstrate great stability bance after successful standing up. | definition/direction/unit from same section | p. 8 (A. Main Results) |
| Fig. 2: Framework overview. (2) We train policies in simulation from scratch vwith multiple cris. and motion consrsnts operationalized by rewards, Smoothness regularization, and ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Reward functions within the same group are independently normalized, Whose assovited advantaged functions are eaimated via disinet criti. | definition/direction/unit from same section | p. 13 (B. More Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| HOST with short history length underperforms in contact-rich scenarios, such as the Wall terrain, In contrast, a longer history length improves performance, though it ... | comparison identity and matched condition | p. 6 (B. Main Results) |
| We evaluate our method in both I vironments corresponding to simulation terrains, using HOST: ww/o-L2C2 as the baseline to examine the effect of smoothness ... | comparison identity and matched condition | p. 8 (A. Main Results) |
| HoST-w/o-MuC represents a baseline with a single value network, essentially a standard RL implementation, HOST-w/o-Force-RND removes the vertical force curriculum and introduces an RND ... | comparison identity and matched condition | p. 12 (B. More Implementation Details) |
| While the robot can learn to stand up without action bounds (HOST-w/o-Bound), its movements are excessively violent, as indicated by three performance metrics. | comparison identity and matched condition | p. 6 (B. Main Results) |
| Motion oscillations are observed in all scenes without smoothness regularization, often leading to standing-up failures, In contrast, our method produces smooth and stable motions, ... | comparison identity and matched condition | p. 8 (A. Main Results) |
| We present the complete set of ward functions and their detailed descriptions in Tulble V1 Several regularization reward terms are adapted from prior work ... | comparison identity and matched condition | p. 12 (B. More Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| ‘We select the successful episode to compute smocthaess to reflect the effect of L2C2 regularization tier. | component/input/data sensitivity | p. 8 (B. Sim-to-real Analysis) |
| In this analysis, we investigate the effect of various domain randomization terms on the sim-to-real gap, as shown in Fig. | component/input/data sensitivity | p. 8 (B. Sim-to-real Analysis) |
| While the robot can learn to stand up without action bounds (HOST-w/o-Bound), its movements are excessively violent, as indicated by three performance metrics. | component/input/data sensitivity | p. 6 (B. Main Results) |
| Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from ... | component/input/data sensitivity | p. 6 (B. Main Results) |
| are handcrafted without collision models. | component/input/data sensitivity | p. 12 (B. More Implementation Details) |
| HOST-Bound0.25 uses a fixed action bound of $ ~ 0.25 without a curriculum, HOST-wip-r*"* eliminates all style-telated reward functions. | component/input/data sensitivity | p. 12 (B. More Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate ... | key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same reward functions, the performance of the ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (B. Main Results), p. 6 (B. Main Results), p. 8 (A. Main Results), p. 8 (A. Main Results) |
| Primary metric/result | HOST with short history length underperforms in contact-rich scenarios, such as the Wall terrain, In contrast, a longer history length improves performance, though it ... | numeric claim only at cited anchor | p. 6 (B. Main Results) |

- Numeric sentences retained from the body:
- **p. 12 / B. More Implementation Details - extractive PDF cue:** Each iteration includes 50 steps per environment, with 5 learning epochs and 4 mini-batches per epoch, The discount factor + is set to 0.99, the ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** Tom a Hi i Kp__kd Kp Kd Hip ry 30 30 Knee 6 308 04 Ankle 2 m0 2 mo 2 Shoulder 4 304 3504 ...
- **p. 12 / B. More Implementation Details - extractive PDF cue:** Each iteration includes 50 steps per environment, with 5 learning epochs and 4 mini-batches per epoch, The discount factor + is set to 0.99, the ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** Tom a Hi i Kp__kd Kp Kd Hip ry 30 30 Knee 6 308 04 Ankle 2 m0 2 mo 2 Shoulder 4 304 3504 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from ... | p. 6 (B. Main Results) |
| body limitation/failure cue | We further tested our controllers on a 15° slippery slope, simulating challenging real-world conditions such as unstable surfaces. | p. 9 (C. Emergent Properties) |
| body limitation/failure cue | Motion oscillations are observed in all scenes without smoothness regularization, often leading to standing-up failures, In contrast, our method produces smooth and stable motions, ... | p. 8 (A. Main Results) |
| body limitation/failure cue | Our proposed framework, HOST, advances humanoid standing-up control by addressing the limitations of existing methods, which either neglect hardware constraints or rely on predefined ... | p. 9 (VII. CoxcLusion) |
| body limitation/failure cue | are handcrafted without collision models. | p. 12 (B. More Implementation Details) |
| body limitation/failure cue | Fig. 5: Robustness analysis in simulation. Evaluation of contol policies under four environmental disturbances demonstrates the robustness of our contol | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each iteration includes 50 steps per environment, with 5 learning epochs and 4 mini-batches per epoch, The discount factor + is set to 0.99, ... | p. 12 (B. More Implementation Details) |
| During the hardware deployment, the stiffness of hip and knee joints are amplified to 1.5 times than the simulation ones, similar to G1, We ... | p. 13 (B. More Implementation Details) |
| Lastly, HOSTHistory modifies the history length of states while keeping other implementations unchanged, | p. 12 (B. More Implementation Details) |
| In our implementations, HI has 19 actuators and H1-2 has 27 actuators. | p. 13 (B. More Implementation Details) |
| This highlights the importance of ‘multiple critics in learning and integrating motor skills while also reducing the hyperparameter tuning burden. | p. 6 (B. Main Results) |
| Due to the unaailabity of the height ‘we compute the smoothness Fan Within two Seconds after staring Up. | p. 8 (B. Sim-to-real Analysis) |
| ‘We select the successful episode to compute smocthaess to reflect the effect of L2C2 regularization tier. | p. 8 (B. Sim-to-real Analysis) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / B. Main Results - extractive PDF cue:** Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a ...
- **p. 9 / C. Emergent Properties - extractive PDF cue:** We further tested our controllers on a 15° slippery slope, simulating challenging real-world conditions such as unstable surfaces.
- **p. 8 / A. Main Results - extractive PDF cue:** Motion oscillations are observed in all scenes without smoothness regularization, often leading to standing-up failures, In contrast, our method produces smooth and stable motions, especially ...
- **p. 9 / VII. CoxcLusion - extractive PDF cue:** Our proposed framework, HOST, advances humanoid standing-up control by addressing the limitations of existing methods, which either neglect hardware constraints or rely on predefined motion ...
- **p. 12 / B. More Implementation Details - extractive PDF cue:** are handcrafted without collision models.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5: Robustness analysis in simulation. Evaluation of contol policies under four environmental disturbances demonstrates the robustness of our contol

- **PDF anchors reviewed:** datasets p. 8 (A. Main Results), p. 9 (B. Sim-to-real Analysis), p. 13 (B. More Implementation Details), p. 13 (B. More Implementation Details), p. 6 (B. Main Results), p. 6 (B. Main Results), metrics p. 6 (B. Main Results), p. 6 (B. Main Results), p. 8 (A. Main Results), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 8 (A. Main Results), baselines p. 6 (B. Main Results), p. 8 (A. Main Results), p. 12 (B. More Implementation Details), p. 6 (B. Main Results), p. 8 (A. Main Results), p. 12 (B. More Implementation Details), results p. 6 (B. Main Results), p. 6 (B. Main Results), p. 8 (A. Main Results), p. 8 (A. Main Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
