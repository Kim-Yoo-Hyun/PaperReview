# Evaluation - AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=88RKxlFUNY; PDF retrieval source: https://openreview.net/pdf/1a99a8c26a0bf879894a517257af43defc03d88a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 19 (A.3.2 ABLATION EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES)): Results demonstrate clear performance differences: SigLIP achieves the highest success rate among single encoders (46.6%), outperforming CLIP (43.1%) by 3.5% and DINO (45.2%) by 1.4%.

## Evaluation Body Digest

- **p. 16 / A.2.2 DATASET SPLIT - extractive PDF cue:** Our training set comprises 10 scenes with 50 object instances, totaling over 13K episodes and 2.5M image-language-action triplets.
- **p. 15 / A.2.1 DATASET CONSTRUCTION - extractive PDF cue:** Simulation data is collected using 12 custom 70m × 70m scenes constructed in AirSim (Shah et al., 2018), while real-world data is acquired through manual ...
- **p. 15 / A.2.1 DATASET CONSTRUCTION - extractive PDF cue:** Data Collection Framework: We employ a dual-source approach for dataset construction, combining simulation and real-world data acquisition.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Scene Sim : Real SR CR PER indoor 0K : 1K 10 40 61.1 indoor 5K : 1K 25 65 71.3 indoor 10K : 1K ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We adopt success rate (SR) as the primary evaluation metric following standard robotics benchmarks.
- **p. 16 / A.2.2 DATASET SPLIT - extractive PDF cue:** Evaluation uses 4 testing scenes (2 from training environments plus 2 completely unseen scenes) with 60 targets (50 previously seen, 10 unseen).
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** All evaluations follow the dataset split protocol detailed in Section 3.3 and threshold specifications summarized in Appendix A.2.1.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Results show progressive performance gains with increased simulation data, confirming that substantial simulation exposure enhances real-world deployment even with limited real-world fine-tuning.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 8); A.2 DETAILS OF AUTONOMOUS NAVIGATION DATASET (p. 15); A.2.1 DATASET CONSTRUCTION (p. 15); A.2.2 DATASET SPLIT (p. 16); A.2.4 DATASET REBALANCING (p. 17); A.3 EXPERIMENTS (p. 18); A.3.2 ABLATION EXPERIMENTS (p. 19); A.3.3 EVALUATION ON CHALLENGING SCENARIOS (p. 19); A.6.1 SIMULATION ENVIRONMENT RESULTS (p. 24).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A.3.2 ABLATION EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results demonstrate clear performance differences: SigLIP achieves the highest success rate among single encoders (46.6%), outperforming CLIP (43.1%) by 3.5% and DINO (45.2%) by ... | p. 19 (A.3.2 ABLATION EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results in Table 4 demonstrate that the method with the pseudo-depth encoder (47.9%, 21.9%) in success rate and collision rate significantly outperforms the ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table refsim-to-real, AutoFly achieves comparable performance across both environments: 60% success rate indoors versus 55% outdoors, with collision rates of 30% ... | p. 9 (4 EXPERIMENTS) |
| A.3.3 EVALUATION ON CHALLENGING SCENARIOS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The pseudo-depth encoder consistently delivers substantial improvements in both success rates (SR) and collision rates (CR) across diverse environmental conditions, with the most pronounced ... | p. 19 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |
| A.3.3 EVALUATION ON CHALLENGING SCENARIOS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This spatial reasoning capability translates to a 7.9 % improvement in success rate and a 7.6 % reduction in collision rate. | p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |

## Dataset / Benchmark Role

- **p. 16 / A.2.2 DATASET SPLIT - extractive PDF cue:** Our training set comprises 10 scenes with 50 object instances, totaling over 13K episodes and 2.5M image-language-action triplets.
- **p. 15 / A.2.1 DATASET CONSTRUCTION - extractive PDF cue:** Simulation data is collected using 12 custom 70m × 70m scenes constructed in AirSim (Shah et al., 2018), while real-world data is acquired through manual ...
- **p. 15 / A.2.1 DATASET CONSTRUCTION - extractive PDF cue:** Data Collection Framework: We employ a dual-source approach for dataset construction, combining simulation and real-world data acquisition.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Scene Sim : Real SR CR PER indoor 0K : 1K 10 40 61.1 indoor 5K : 1K 25 65 71.3 indoor 10K : 1K ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We adopt success rate (SR) as the primary evaluation metric following standard robotics benchmarks.
- **p. 16 / A.2.2 DATASET SPLIT - extractive PDF cue:** Evaluation uses 4 testing scenes (2 from training environments plus 2 completely unseen scenes) with 60 targets (50 previously seen, 10 unseen).
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** All evaluations follow the dataset split protocol detailed in Section 3.3 and threshold specifications summarized in Appendix A.2.1.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Results show progressive performance gains with increased simulation data, confirming that substantial simulation exposure enhances real-world deployment even with limited real-world fine-tuning.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Analysis of previous methods and our AutoFly. Left: Previous methods (Lee et al., 2024; Liu et al., 2023b) rely on dedicated, step-by-step instructions ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Framework of AutoFly. AutoFly takes RGB observations and linguistic instructions as inputs and directly outputs high-level actions. These actions, combined with initial actions ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of autonomous navigation dataset statistical analysis.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of VLN datasets. Datasets for ground robots are shown above the dividing line; aerial-robot datasets are shown below. Ntraj: total number of ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Comparison of three paradigms for integrating depth information during fine-tuning: (a) Siamese MLP projector, (b) Non-Siamese MLP projector, (c) Direct depth integration. instructions ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Visualization of AutoFly in the real indoor environment. The experimental arena is a structured indoor environment designed for autonomous navigation and mapping tasks. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Visualization of AutoFly in the real outdoor environment. The experimental arena is a unstructured outdoor environment with trees. We have achieved a 55% ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Overall performance metrics for quadrotor (all values in %). Here, we report three metrics: Success Rate (SR↑), Collision Rate (CR↓), and Path Efficiency ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our training set comprises 10 scenes with 50 object instances, totaling over 13K episodes and 2.5M image-language-action triplets. | embodiment, simulator version and control stack | p. 16 (A.2.2 DATASET SPLIT), p. 15 (A.2.1 DATASET CONSTRUCTION) |
| Task/environment | Simulation data is collected using 12 custom 70m × 70m scenes constructed in AirSim (Shah et al., 2018), while real-world data is acquired through ... | reset, timeout, object/scene variation | p. 15 (A.2.1 DATASET CONSTRUCTION), p. 15 (A.2.1 DATASET CONSTRUCTION) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3 METHOD), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 4 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As shown in Table refsim-to-real, AutoFly achieves comparable performance across both environments: 60% success rate indoors versus 55% outdoors, with collision rates of 30% ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| 4.3 REAL-WORLD PERFORMANCE Table 3: Success rate (%) for sim-to-real transferring. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Results demonstrate clear performance differences: SigLIP achieves the highest success rate among single encoders (46.6%), outperforming CLIP (43.1%) by 3.5% and DINO (45.2%) by ... | definition/direction/unit from same section | p. 19 (A.3.2 ABLATION EXPERIMENTS) |
| The pseudo-depth encoder consistently delivers substantial improvements in both success rates (SR) and collision rates (CR) across diverse environmental conditions, with the most pronounced ... | definition/direction/unit from same section | p. 19 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |
| Here, we report three metrics: Success Rate (SR↑), Collision Rate (CR↓), and Path Efficiency Rate (PER↑). | definition/direction/unit from same section | p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |
| This spatial reasoning capability translates to a 7.9 % improvement in success rate and a 7.6 % reduction in collision rate. | definition/direction/unit from same section | p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |
| We adopt success rate (SR) as the primary evaluation metric following standard robotics benchmarks. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Figure 6: Visualization of AutoFly in the real outdoor environment. The experimental arena is a unstructured outdoor environment with trees. We have achieved a ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The results in Table 4 demonstrate that the method with the pseudo-depth encoder (47.9%, 21.9%) in success rate and collision rate significantly outperforms the ... | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Both AutoFly and OpenVLA outperform RT-2 across all scenarios, achieving success rates of 47.9% and 44% respectively versus RT-2's 41.9%; this stems from OpenVLA's ... | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Results demonstrate clear performance differences: SigLIP achieves the highest success rate among single encoders (46.6%), outperforming CLIP (43.1%) by 3.5% and DINO (45.2%) by ... | comparison identity and matched condition | p. 19 (A.3.2 ABLATION EXPERIMENTS) |
| The baseline model's collision rate reaches 37.7%, frequently failing to maintain safe distances from moving obstacles or predict their trajectories. | comparison identity and matched condition | p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |
| Dense Forest Scene: In this visually complex environment, the baseline model demonstrates hesitant navigation behavior, struggling to parse irregular obstacle geometries. | comparison identity and matched condition | p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |
| Figure 4: Comparison of three paradigms for integrating depth information during fine-tuning: (a) Siamese MLP projector, (b) Non-Siamese MLP projector, (c) Direct depth integration. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To validate the effectiveness of our pseudo-depth encoder, we conduct ablation studies comparing models with and without the depth encoder. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| 4.4 ABLATION EXPERIMENTS We conduct comprehensive ablation studies to validate our model's effectiveness, systematically evaluating five key components: pseudo-depth encoder ablation, specialized depth projector ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| We collect an additional 1,000 episodes (∼350K vision-language-action pairs) to evaluate the effect of increased training data. • Data Augmentation. | component/input/data sensitivity | p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES) |
| To investigate the impact of different vision encoders on task performance, we conduct comprehensive ablation experiments comparing four representative vision backbones: CLIP, DINO, SigLIP, ... | component/input/data sensitivity | p. 19 (A.3.2 ABLATION EXPERIMENTS) |
| We apply stratified resampling as follows: Group sub-trajectories by phase into Dk = {τ (k) i }, compute sample sizes nk = round(wk · ... | component/input/data sensitivity | p. 18 (A.2.4 DATASET REBALANCING) |
| Table 5: Results (%) for depth projector ablations. | component/input/data sensitivity | p. 10 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework. | Results demonstrate clear performance differences: SigLIP achieves the highest success rate among single encoders (46.6%), outperforming CLIP (43.1%) by 3.5% and DINO (45.2%) by ... | PDF body cue; verify exact table/figure and matched conditions | p. 19 (A.3.2 ABLATION EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES) |
| Primary metric/result | The results in Table 4 demonstrate that the method with the pseudo-depth encoder (47.9%, 21.9%) in success rate and collision rate significantly outperforms the ... | numeric claim only at cited anchor | p. 9 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We evaluated the system on 10 object instances, conducting 20 independent trials per target in each setting.
- **p. 15 / A.2.1 DATASET CONSTRUCTION - extractive PDF cue:** Success Metrics: A navigation episode is considered successful when the robot achieves: (1) proximity within 5 meters of the target, and (2) target orientation with ...
- **p. 16 / A.2.2 DATASET SPLIT - extractive PDF cue:** Our training set comprises 10 scenes with 50 object instances, totaling over 13K episodes and 2.5M image-language-action triplets.
- **p. 16 / A.2.2 DATASET SPLIT - extractive PDF cue:** This setup creates 4 evaluation conditions, with 30 trials per condition, yielding 7,200 evaluation episodes in total.
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive PDF cue:** We collect an additional 1,000 episodes (∼350K vision-language-action pairs) to evaluate the effect of increased training data. • Data Augmentation.
- **p. 4 / 3 METHOD - extractive PDF cue:** 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language instruction L, and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER SR CR PER w/ 57.2 21.1 78.3 53.6 ... | p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |
| body limitation/failure cue | To address these limitations, we plan to enhance AutoFly's sensing capabilities through LiDAR integration, which will provide comprehensive 360◦environmental perception and improve robustness in ... | p. 24 (A.7 LIMITATIONS AND FUTURE WORK) |
| body limitation/failure cue | Future work will integrate Reinforcement Learning to enable active interaction with dynamic environments, allowing the system to learn more robust reactive behaviors through trial-and-error ... | p. 24 (A.7 LIMITATIONS AND FUTURE WORK) |
| body limitation/failure cue | The baseline model's collision rate reaches 37.7%, frequently failing to maintain safe distances from moving obstacles or predict their trajectories. | p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |
| body limitation/failure cue | Figure 1: Analysis of previous methods and our AutoFly. Left: Previous methods (Lee et al., 2024; Liu et al., 2023b) rely on dedicated, step-by-step ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | SR = /S//N, CR = /C//N, PER = /E///S/, (4) where S = {i : di ≤dτ, θi ≤θτ} denotes the set of successful ... | p. 8 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We maintain the default cross-entropy loss function from the base language model and employ a learning rate of 2e-5 for the VLM backbone and ... | p. 8 (4 EXPERIMENTS) |
| The optimized pipeline achieves near-optimal throughput where total inference time approaches the LLM inference duration plus inter-process communication overhead (approximately 15-20ms). | p. 22 (A.5.4 PARALLEL INFERENCE ARCHITECTURE) |
| 4.1 IMPLEMENTATION DETAILS This section presents implementation details across three components: training details, evaluation details, and robot setup. | p. 8 (4 EXPERIMENTS) |
| Analysis of vision encoder variations is detailed in the Appendix A.3.2. | p. 9 (4 EXPERIMENTS) |
| Method SR CR PER w/ 47.9 21.9 77.3 w/o 44 24.5 75.1 Pseudo-Depth Encoder Ablation. | p. 9 (4 EXPERIMENTS) |
| Different Vision Encoders Analysis. | p. 19 (A.3.2 ABLATION EXPERIMENTS) |
| While our main experiments demonstrate the effectiveness of the pseudo-depth encoder across diverse navigation tasks. | p. 19 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |
| Cross-Scenario Insights: The depth encoder's performance gains scale with scenario difficulty. | p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 20 / A.3.3 EVALUATION ON CHALLENGING SCENARIOS - extractive PDF cue:** Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER SR CR PER w/ 57.2 21.1 78.3 53.6 23.7 ...
- **p. 24 / A.7 LIMITATIONS AND FUTURE WORK - extractive PDF cue:** To address these limitations, we plan to enhance AutoFly's sensing capabilities through LiDAR integration, which will provide comprehensive 360◦environmental perception and improve robustness in complex ...
- **p. 24 / A.7 LIMITATIONS AND FUTURE WORK - extractive PDF cue:** Future work will integrate Reinforcement Learning to enable active interaction with dynamic environments, allowing the system to learn more robust reactive behaviors through trial-and-error exploration.
- **p. 20 / A.3.3 EVALUATION ON CHALLENGING SCENARIOS - extractive PDF cue:** The baseline model's collision rate reaches 37.7%, frequently failing to maintain safe distances from moving obstacles or predict their trajectories.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Analysis of previous methods and our AutoFly. Left: Previous methods (Lee et al., 2024; Liu et al., 2023b) rely on dedicated, step-by-step instructions ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** SR = /S//N, CR = /C//N, PER = /E///S/, (4) where S = {i : di ≤dτ, θi ≤θτ} denotes the set of successful trials, ...

- **PDF anchors reviewed:** datasets p. 16 (A.2.2 DATASET SPLIT), p. 15 (A.2.1 DATASET CONSTRUCTION), p. 15 (A.2.1 DATASET CONSTRUCTION), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 16 (A.2.2 DATASET SPLIT), metrics p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3.2 ABLATION EXPERIMENTS), p. 19 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), baselines p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3.2 ABLATION EXPERIMENTS), p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 7 (Figure/Table caption), results p. 19 (A.3.2 ABLATION EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
