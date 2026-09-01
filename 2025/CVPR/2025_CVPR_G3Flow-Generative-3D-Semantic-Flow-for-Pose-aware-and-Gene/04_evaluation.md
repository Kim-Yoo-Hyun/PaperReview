# Evaluation - G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_G3Flow_Generative_3D_Semantic_Flow_for_Pose-aware_and_Generalizable_Object_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_G3Flow_Generative_3D_Semantic_Flow_for_Pose-aware_and_Generalizable_Object_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (34.04 Hz), p. 7 (4.4. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.1. Experimental Setup), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation on Pose-aware Manipulation Tasks)): G3Flow achieved a success rate of 70.7% on previously unseen tool categories, which is 13.4% higher than the best baseline.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We evaluate our approach on five distinct manipulation tasks from the RoboTwin benchmark [19], as illustrated in Figure 6.
- **p. 7 / 4.3. Evaluation on Generalization Performance - extractive body cue:** Unlike tasks that require the satisfaction of terminal constraints, we choose as few and similar visible objects as possible for the training set and select ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For each task, we train policies using 100 expert demonstrations and evaluate across 3 random seeds with 100 test episodes per seed.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Robotic manipulation tasks have stringent requirements for real-time performance.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Performance is measured through average success rates and standard deviations across seeds.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Success rates (in %) of cross-object generalization tasks.. We report the mean and standard deviation computed over 3 random seeds. (a) Shoe Place ...
- **p. 7 / 34.04 Hz - extractive body cue:** G3Flow achieved a success rate of 70.7% on previously unseen tool categories, which is 13.4% higher than the best baseline.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** As shown in Table 4, our approach improves success rates by 22.6% and 41.2% over scenelevel features, and by 9.3% and 3.7% over D3Fields.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Evaluation on Pose-aware Manipulation Tasks (p. 6); 4.3. Evaluation on Generalization Performance (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 34.04 Hz | EMPIRICAL / REAL-ROBOT OR HARDWARE | G3Flow achieved a success rate of 70.7% on previously unseen tool categories, which is 13.4% higher than the best baseline. | p. 7 (34.04 Hz) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 4, our approach improves success rates by 22.6% and 41.2% over scenelevel features, and by 9.3% and 3.7% over D3Fields. | p. 7 (4.4. Ablation Study) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5. Ablation on VFMs. Success rates of G3Flow imple- mented with different VFMs (our method uses DINOv2) on the Shoe Place (T) task. ... | p. 8 (Figure/Table caption) |
| 4.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Performance is measured through average success rates and standard deviations across seeds. | p. 6 (4.1. Experimental Setup) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Ablation on Quality of Semantic Field. We compare the success rates of scene-level features, D3Fields and G3Flow on Shoe Place and Dual ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We evaluate our approach on five distinct manipulation tasks from the RoboTwin benchmark [19], as illustrated in Figure 6.
- **p. 7 / 4.3. Evaluation on Generalization Performance - extractive body cue:** Unlike tasks that require the satisfaction of terminal constraints, we choose as few and similar visible objects as possible for the training set and select ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For each task, we train policies using 100 expert demonstrations and evaluate across 3 random seeds with 100 test episodes per seed.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Robotic manipulation tasks have stringent requirements for real-time performance.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Motivation of G3Flow. Our approach leverages 3D generative model and language-guided detection model to gen- erate 3D semantic flow (top). Through continuous field ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Pipeline of G3Flow. Our framework consists of (top) an initialization phase that generates comprehensive 3D representation (surface normals, wireframe, and geometry) through object-centric ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Failure mode of single-view 3D generation. When using a single view for 3D generation, certain geometric details may be inaccurately reconstructed due to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Spatial alignment via object tracking. We achieve alignment between the semantic flow and the physical object in real world by synchronizing the relative ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. G3Flow-enhanced diffusion policy.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Success rates (in %) of simulation tasks for terminal constraint control tasks. We report the mean and standard deviation computed over 3 random ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Success rates (in %) of cross-object generalization tasks.. We report the mean and standard deviation computed over 3 random seeds. (a) Shoe Place ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Five testing benchmark tasks.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our approach on five distinct manipulation tasks from the RoboTwin benchmark [19], as illustrated in Figure 6. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 7 (4.3. Evaluation on Generalization Performance) |
| Task/environment | Unlike tasks that require the satisfaction of terminal constraints, we choose as few and similar visible objects as possible for the training set and ... | reset, timeout, object/scene variation | p. 7 (4.3. Evaluation on Generalization Performance), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 5 (3.4. G3Flow-Enhanced Diffusion Policy), p. 5 (3.4. G3Flow-Enhanced Diffusion Policy) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 3 (3.1. Overview), p. 3 (3.1. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Performance is measured through average success rates and standard deviations across seeds. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Table 2. Success rates (in %) of cross-object generalization tasks.. We report the mean and standard deviation computed over 3 random seeds. (a) Shoe ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| G3Flow achieved a success rate of 70.7% on previously unseen tool categories, which is 13.4% higher than the best baseline. | definition/direction/unit from same section | p. 7 (34.04 Hz) |
| As shown in Table 4, our approach improves success rates by 22.6% and 41.2% over scenelevel features, and by 9.3% and 3.7% over D3Fields. | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| Table 4. Ablation on Quality of Semantic Field. We compare the success rates of scene-level features, D3Fields and G3Flow on Shoe Place and Dual ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 5. Ablation on VFMs. Success rates of G3Flow imple- mented with different VFMs (our method uses DINOv2) on the Shoe Place (T) task. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. Motivation of G3Flow. Our approach leverages 3D generative model and language-guided detection model to gen- erate 3D semantic flow (top). Through continuous ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 3. Failure mode of single-view 3D generation. When using a single view for 3D generation, certain geometric details may be inaccurately reconstructed due ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| G3Flow nearly doubles the success rate compared to the strongest baseline, suggesting that our semantic representations effectively encode spatial relationships and object orientations. | comparison identity and matched condition | p. 7 (4.2. Evaluation on Pose-aware Manipulation Tasks) |
| Our method significantly outperforms baselines, achieving a decision frequency of 34.04 Hz, nearly 6 times faster than GenDP [34], meeting the requirements of most ... | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| 1, G3Flow consistently outperforms 1740 | comparison identity and matched condition | p. 6 (4.2. Evaluation on Pose-aware Manipulation Tasks) |
| Baselines: We use the 3D Diffusion Policy (DP3) [40], which utilizes efficient point encoders to create compact 3D representations, and its variant with RGB ... | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Table 5. Ablation on VFMs. Success rates of G3Flow imple- mented with different VFMs (our method uses DINOv2) on the Shoe Place (T) task. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 4. Ablation on Quality of Semantic Field. We compare the success rates of scene-level features, D3Fields and G3Flow on Shoe Place and Dual ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Baselines: We use the 3D Diffusion Policy (DP3) [40], which utilizes efficient point encoders to create compact 3D representations, and its variant with RGB ... | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| Ablation on Quality of Semantic Field. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| We conducted an ablation study comparing our method against conventional scene-level feature clouds and D3Fields, using the Shoe Place (T) and Dual Shoes Place ... | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Table 5. Ablation on VFMs. Success rates of G3Flow imple- mented with different VFMs (our method uses DINOv2) on the Shoe Place (T) task. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 7. Seen and unseen object sets for four tasks with high terminal constraint requirements. employ PCA to reduce the feature dimensions of DINOv2 ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our framework consists of (top) an initialization phase that generates comprehensive 3D representation (surface normals, wireframe, and geometry) through object-centric exploration and digital twin ... | G3Flow achieved a success rate of 70.7% on previously unseen tool categories, which is 13.4% higher than the best baseline. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (34.04 Hz), p. 7 (4.4. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.1. Experimental Setup), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation on Pose-aware Manipulation Tasks) |
| Primary metric/result | As shown in Table 4, our approach improves success rates by 22.6% and 41.2% over scenelevel features, and by 9.3% and 3.7% over D3Fields. | numeric claim only at cited anchor | p. 7 (4.4. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Seen and unseen object sets for four tasks with high terminal constraint requirements. employ PCA to reduce the feature dimensions of DINOv2 to 5, and ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We train 3000 epochs for all the tasks with batch size 256 for G3Flow and DP3.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For DP, we train 300 epochs for all the tasks with batch size 128.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Our method significantly outperforms baselines, achieving a decision frequency of 34.04 Hz, nearly 6 times faster than GenDP [34], meeting the requirements of most real-time ...
- **p. 6 / 3.4. G3Flow-Enhanced Diffusion Policy - extractive body cue:** Shoe Place (T) Dual Shoes Place (T) Tool Adjust (T) Bottle Adjust (T) Average DP 26.0±11.4 3.3±1.2 21.7±5.1 16.3±4.6 16.8 (#51.5) 3D DP 54.0±6.9 13.0±1.7 ...
- **p. 6 / 3.4. G3Flow-Enhanced Diffusion Policy - extractive body cue:** Shoe Place (G) Dual Shoes Place (G) Diverse Bottles Pick (G) Tool Adjust (G) Average DP 17.7±3.2 3.0±2.6 8.7±3.2 16.0±11.3 11.4 (#38.7) 3D DP 51.0±6.6 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Failure mode of single-view 3D generation. When using a single view for 3D generation, certain geometric details may be inaccurately reconstructed due ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | By uniquely integrating 3D generative models for digital twin creation, vision foundation models for semantic feature extraction, and robust pose tracking, G3Flow enables complete ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 4. Spatial alignment via object tracking. We achieve alignment between the semantic flow and the physical object in real world by synchronizing the ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Table 4. Ablation on Quality of Semantic Field. We compare the success rates of scene-level features, D3Fields and G3Flow on Shoe Place and Dual ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | This indicates robust handling of geometric variations while preserving semantic understanding. | p. 7 (34.04 Hz) |
| body limitation/failure cue | While D3Fields benefits from human prior knowledge, our method outperforms it by focusing on object-centered visual inputs, which reduces irrelevant background noise (Sec. | p. 7 (4.4. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For DP, we train 300 epochs for all the tasks with batch size 128. | p. 6 (4.1. Experimental Setup) |
| Performance is measured through average success rates and standard deviations across seeds. | p. 6 (4.1. Experimental Setup) |
| G3Flow nearly doubles the success rate compared to the strongest baseline, suggesting that our semantic representations effectively encode spatial relationships and object orientations. | p. 7 (4.2. Evaluation on Pose-aware Manipulation Tasks) |
| ! … FoundationPose Diffusion Model Fields Encoder Semantic Condition Other Conditions Desc. | p. 4 (3.2. Initial Semantic Flow Construction) |
| Our policy integrates three distinct types of information through separate MLP encoders. | p. 5 (3.4. G3Flow-Enhanced Diffusion Policy) |
| Finally, the current robot joint states are encoded into robot state features fp, ensuring awareness of the manipulator's configuration. | p. 5 (3.4. G3Flow-Enhanced Diffusion Policy) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Failure mode of single-view 3D generation. When using a single view for 3D generation, certain geometric details may be inaccurately reconstructed due to ...
- **p. 8 / 5. Conclusion - extractive body cue:** By uniquely integrating 3D generative models for digital twin creation, vision foundation models for semantic feature extraction, and robust pose tracking, G3Flow enables complete semantic ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Spatial alignment via object tracking. We achieve alignment between the semantic flow and the physical object in real world by synchronizing the relative ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation on Quality of Semantic Field. We compare the success rates of scene-level features, D3Fields and G3Flow on Shoe Place and Dual Shoes ...
- **p. 7 / 34.04 Hz - extractive body cue:** This indicates robust handling of geometric variations while preserving semantic understanding.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** While D3Fields benefits from human prior knowledge, our method outperforms it by focusing on object-centered visual inputs, which reduces irrelevant background noise (Sec.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 7 (4.3. Evaluation on Generalization Performance), p. 6 (4.1. Experimental Setup), p. 7 (4.4. Ablation Study), metrics p. 6 (4.1. Experimental Setup), p. 6 (Figure/Table caption), p. 7 (34.04 Hz), p. 7 (4.4. Ablation Study), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 7 (4.2. Evaluation on Pose-aware Manipulation Tasks), p. 7 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Pose-aware Manipulation Tasks), p. 6 (4.1. Experimental Setup), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 7 (34.04 Hz), p. 7 (4.4. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.1. Experimental Setup), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation on Pose-aware Manipulation Tasks).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
