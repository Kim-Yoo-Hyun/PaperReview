# Evaluation - ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results), p. 8 (4.2. Ablation Study), p. 8 (4.2. Ablation Study), p. 1 (Figure/Table caption), p. 6 (4.1. Experimental Results)): Results in Table 2 show that ActiveVLA achieves a new state of the art on COLOSSEUM, with an average success rate of 65.9% and an average rank of 1.07, outperforming ...

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive body cue:** Real-world experiments are conducted on a KINOVA GEN2 robot with a RealSense D455 camera in an eye-to-hand setup, covering occlusion-rich manipulation tasks.
- **p. 7 / 4.1. Experimental Results - extractive body cue:** Right of the dotted line (fine stage): using these regions, perform (c) active view selection and (d) active 3D zoom-in for fine-grained manipulation in complex ...
- **p. 6 / 4. Experiments - extractive body cue:** RLBench [23] features 18 tasks using a Franka Panda robot with RGB-D inputs from four calibrated cameras and 100 demonstrations per task.
- **p. 8 / 4.1. Experimental Results - extractive body cue:** The tasks involve diverse spatial configurations, such as picking objects from cluttered scenes, retrieving partially hidden items, and manipulating objects with intricate occlusion relationships.
- **p. 7 / 4.1. Experimental Results - extractive body cue:** Results on the COLOSSEUM Benchmark.
- **p. 8 / 4.1. Experimental Results - extractive body cue:** To evaluate the real-world performance of ActiveVLA, we conduct a series of real-world manipulation experiments under complex and highly occluded scenarios.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Component Performance A-VS A-3Z RLBench COLOSSEUM GemBench 87.6/0.26 63.6/0.33 48.9/0.21 " 89.4/0.45 64.5/0.51 49.4/0.48 " " 91.8/0.53 65.9/0.62 51.3/0.59 1 2 3 4 5 6 ...
- **p. 7 / 4.1. Experimental Results - extractive body cue:** Results are reported as mean success rates without confidence intervals.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results in Table 2 show that ActiveVLA achieves a new state of the art on COLOSSEUM, with an average success rate of 65.9% and ... | p. 7 (4.1. Experimental Results) |
| 4.1. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 3, ActiveVLA achieves the best performance across core levels L1-L3, with success rates of 92.4%, 66.3%, and 45.1%, surpassing 8147 | p. 7 (4.1. Experimental Results) |
| 4.2. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 5, increasing the number of views improves the success rate from 82.2% (one view) to 91.8% (three views), confirming that ... | p. 8 (4.2. Ablation Study) |
| 4.2. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Component Performance A-VS A-3Z RLBench COLOSSEUM GemBench 87.6/0.26 63.6/0.33 48.9/0.21 " 89.4/0.45 64.5/0.51 49.4/0.48 " " 91.8/0.53 65.9/0.62 51.3/0.59 1 2 3 4 5 ... | p. 8 (4.2. Ablation Study) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive body cue:** Real-world experiments are conducted on a KINOVA GEN2 robot with a RealSense D455 camera in an eye-to-hand setup, covering occlusion-rich manipulation tasks.
- **p. 7 / 4.1. Experimental Results - extractive body cue:** Right of the dotted line (fine stage): using these regions, perform (c) active view selection and (d) active 3D zoom-in for fine-grained manipulation in complex ...
- **p. 6 / 4. Experiments - extractive body cue:** RLBench [23] features 18 tasks using a Franka Panda robot with RGB-D inputs from four calibrated cameras and 100 demonstrations per task.
- **p. 8 / 4.1. Experimental Results - extractive body cue:** The tasks involve diverse spatial configurations, such as picking objects from cluttered scenes, retrieving partially hidden items, and manipulating objects with intricate occlusion relationships.
- **p. 7 / 4.1. Experimental Results - extractive body cue:** Results on the COLOSSEUM Benchmark.
- **p. 8 / 4.1. Experimental Results - extractive body cue:** To evaluate the real-world performance of ActiveVLA, we conduct a series of real-world manipulation experiments under complex and highly occluded scenarios.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The pipeline of ActiveVLA. ActiveVLA is a 3D vision-language-action framework that adopts a two-stage, coarse-to-fine strategy. In the coarse stage, three orthographic projections ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Results on RLBench. "Avg. Rank" denotes the average rank across all 18 tasks, where a lower value signifies better overall performance. ActiveVLA attains ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Results on the COLOSSEUM Benchmark. The table presents performance across 14 generalization scenarios. "Avg. Rank" indicates the mean ranking of each method over ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results of fine-grained manipulation tasks. Left of the dotted line (coarse stage): (a) project 3D modalities onto orthographic images, then (b) predict ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Performance on the GemBench benchmark. Results are reported as mean success rates without confidence intervals.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Visualization of ActiveVLA in complex manipulation tasks. It actively perceives and precisely completes tasks despite severe occlusions and complex spatial structures. baselines such ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on key components. We report the suc- cess rate (%) and inference time (s) over 100 trials. A-VS (Active View Selection) ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-world experiments are conducted on a KINOVA GEN2 robot with a RealSense D455 camera in an eye-to-hand setup, covering occlusion-rich manipulation tasks. | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 7 (4.1. Experimental Results) |
| Task/environment | Right of the dotted line (fine stage): using these regions, perform (c) active view selection and (d) active 3D zoom-in for fine-grained manipulation in ... | reset, timeout, object/scene variation | p. 7 (4.1. Experimental Results), p. 6 (4. Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 5 (3.3. 3D Action Prediction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Component Performance A-VS A-3Z RLBench COLOSSEUM GemBench 87.6/0.26 63.6/0.33 48.9/0.21 " 89.4/0.45 64.5/0.51 49.4/0.48 " " 91.8/0.53 65.9/0.62 51.3/0.59 1 2 3 4 5 ... | definition/direction/unit from same section | p. 8 (4.2. Ablation Study) |
| Results are reported as mean success rates without confidence intervals. | definition/direction/unit from same section | p. 7 (4.1. Experimental Results) |
| As shown in Table 3, ActiveVLA achieves the best performance across core levels L1-L3, with success rates of 92.4%, 66.3%, and 45.1%, surpassing 8147 | definition/direction/unit from same section | p. 7 (4.1. Experimental Results) |
| ActiveVLA achieves a new state of the art on RLBench with a 91.8% average success rate and an average rank of 1.22. | definition/direction/unit from same section | p. 6 (4.1. Experimental Results) |
| We report the success rate (%) and inference time (s) over 100 trials. | definition/direction/unit from same section | p. 8 (4.2. Ablation Study) |
| COLOSSEUM [48] extends RLBench with 12 perturbation types involving object, scene, and camera variations for robustness evaluation. | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. The pipeline of ActiveVLA. ActiveVLA is a 3D vision-language-action framework that adopts a two-stage, coarse-to-fine strategy. In the coarse stage, three orthographic ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare ActiveVLA with state-of-the-art baselines. | comparison identity and matched condition | p. 6 (4. Experiments) |
| Results in Table 2 show that ActiveVLA achieves a new state of the art on COLOSSEUM, with an average success rate of 65.9% and ... | comparison identity and matched condition | p. 7 (4.1. Experimental Results) |
| The fixed-view baseline achieves 87.6% success in 0.26 s per trial. | comparison identity and matched condition | p. 8 (4.2. Ablation Study) |
| It actively perceives and precisely completes tasks despite severe occlusions and complex spatial structures. baselines such as 3D-LOTUS++ and BridgeVLA. | comparison identity and matched condition | p. 8 (4.1. Experimental Results) |
| Results are reported as mean success rates without confidence intervals. | comparison identity and matched condition | p. 7 (4.1. Experimental Results) |
| Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Results are reported as mean success rates without confidence intervals. | component/input/data sensitivity | p. 7 (4.1. Experimental Results) |
| Overall, ActiveVLA surpasses BridgeVLA in most categories, confirming its stronger visual generalization and invariant representation learning capability. | component/input/data sensitivity | p. 7 (4.1. Experimental Results) |
| Table 4. Ablation study on key components. We report the suc- cess rate (%) and inference time (s) over 100 trials. A-VS (Active View ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Our ActiveVLA adopts the pretrained VLM backbone from BridgeVLA [33], built on PaliGemma [3] with a SigLIP encoder [63] and Gemma decoder [53], pre-trained ... | component/input/data sensitivity | p. 6 (4. Experiments) |
| Component Performance A-VS A-3Z RLBench COLOSSEUM GemBench 87.6/0.26 63.6/0.33 48.9/0.21 " 89.4/0.45 64.5/0.51 49.4/0.48 " " 91.8/0.53 65.9/0.62 51.3/0.59 1 2 3 4 5 ... | component/input/data sensitivity | p. 8 (4.2. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142 | Results in Table 2 show that ActiveVLA achieves a new state of the art on COLOSSEUM, with an average success rate of 65.9% and ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results), p. 8 (4.2. Ablation Study), p. 8 (4.2. Ablation Study), p. 1 (Figure/Table caption), p. 6 (4.1. Experimental Results) |
| Primary metric/result | As shown in Table 3, ActiveVLA achieves the best performance across core levels L1-L3, with success rates of 92.4%, 66.3%, and 45.1%, surpassing 8147 | numeric claim only at cited anchor | p. 7 (4.1. Experimental Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments - extractive body cue:** RLBench [23] features 18 tasks using a Franka Panda robot with RGB-D inputs from four calibrated cameras and 100 demonstrations per task.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** The fixed-view baseline achieves 87.6% success in 0.26 s per trial.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Adding A-VS dynamically selects informative views, raising performance to 89.4% at 0.45 s by improving scene coverage and reducing occlusion.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Further introducing A3Z enables virtual optical zoom for high-resolution closeups, achieving 91.8% success at 0.53 s.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** We report the success rate (%) and inference time (s) over 100 trials.
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** Rank" denotes the average rank across all 18 tasks, where a lower value signifies better overall performance.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place ... | p. 6 (4.1. Experimental Results) |
| body limitation/failure cue | COLOSSEUM [48] extends RLBench with 12 perturbation types involving object, scene, and camera variations for robustness evaluation. | p. 6 (4. Experiments) |
| body limitation/failure cue | It remains robust to variations in object size, color, lighting, and texture, obtaining 72.4% on MO-SIZE and 64.4% on RO-SIZE. | p. 7 (4.1. Experimental Results) |
| body limitation/failure cue | Adding A-VS dynamically selects informative views, raising performance to 89.4% at 0.45 s by improving scene coverage and reducing occlusion. | p. 8 (4.2. Ablation Study) |
| body limitation/failure cue | It actively perceives and precisely completes tasks despite severe occlusions and complex spatial structures. baselines such as 3D-LOTUS++ and BridgeVLA. | p. 8 (4.1. Experimental Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We report the success rate (%) and inference time (s) over 100 trials. | p. 8 (4.2. Ablation Study) |
| All experiments run on eight NVIDIA H100 GPUs and a 192-vCPU Intel Xeon Platinum 8468 system. | p. 6 (4. Experiments) |
| We evaluate ActiveVLA over five trials for statistical reliability, with results shown in Table 1. | p. 6 (4.1. Experimental Results) |
| The fixed-view baseline achieves 87.6% success in 0.26 s per trial. | p. 8 (4.2. Ablation Study) |
| A hierarchical feature fusion module then integrates global and local context to predict rotation, gripper state, and a binary collision flag. • Global Context ... | p. 5 (3.3. 3D Action Prediction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their ...
- **p. 6 / 4.1. Experimental Results - extractive body cue:** It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place Cups, ...
- **p. 6 / 4. Experiments - extractive body cue:** COLOSSEUM [48] extends RLBench with 12 perturbation types involving object, scene, and camera variations for robustness evaluation.
- **p. 7 / 4.1. Experimental Results - extractive body cue:** It remains robust to variations in object size, color, lighting, and texture, obtaining 72.4% on MO-SIZE and 64.4% on RO-SIZE.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Adding A-VS dynamically selects informative views, raising performance to 89.4% at 0.45 s by improving scene coverage and reducing occlusion.
- **p. 8 / 4.1. Experimental Results - extractive body cue:** It actively perceives and precisely completes tasks despite severe occlusions and complex spatial structures. baselines such as 3D-LOTUS++ and BridgeVLA.

- **PDF anchors reviewed:** datasets p. 6 (4. Experiments), p. 7 (4.1. Experimental Results), p. 6 (4. Experiments), p. 8 (4.1. Experimental Results), p. 7 (4.1. Experimental Results), p. 8 (4.1. Experimental Results), metrics p. 8 (4.2. Ablation Study), p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results), p. 6 (4.1. Experimental Results), p. 8 (4.2. Ablation Study), p. 6 (4. Experiments), baselines p. 6 (4. Experiments), p. 7 (4.1. Experimental Results), p. 8 (4.2. Ablation Study), p. 8 (4.1. Experimental Results), p. 7 (4.1. Experimental Results), p. 1 (Figure/Table caption), results p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results), p. 8 (4.2. Ablation Study), p. 8 (4.2. Ablation Study), p. 1 (Figure/Table caption), p. 6 (4.1. Experimental Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
