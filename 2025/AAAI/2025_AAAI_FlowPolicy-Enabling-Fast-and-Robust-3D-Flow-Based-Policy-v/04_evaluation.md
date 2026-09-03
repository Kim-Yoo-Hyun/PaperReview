# Evaluation - FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33617; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33617. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Abstract), p. 7 (Abstract), p. 6 (Figure/Table caption), p. 6 (Abstract), p. 1 (Figure/Table caption), p. 5 (Abstract)): Both generally improve the accuracy with more demonstrations, but FlowPolicy typically has a higher success rate and avoids the performance bottleneck as presented in DP3.

## Evaluation Body Digest

- **p. 5 / Abstract - extractive body cue:** Experiments Dataset and Implementation Details Simulation Benchmarks We choose two preeminent environmental simulators, Adroit (Rajeswaran et al.
- **p. 5 / Abstract - extractive body cue:** In contrast, the Metaworld benchmark offers a diverse array of tasks that span the spectrum of difficulty levels, from easy to very hard, typically surmounted ...
- **p. 3 / Abstract - extractive body cue:** Visual observations include the robot state and scene point clouds, and actions are usually sequences of trajectories of the robot to accomplish a specific task.
- **p. 3 / Abstract - extractive body cue:** More importantly, Consistency-FM can be trained to produce a robust flow model without the aid of distillation, which is valuable to robots performing unseen tasks, ...
- **p. 4 / Abstract - extractive body cue:** With the conditional constraints of visual features, FlowPolicy enables the efficient capture of spatial information that is critical to fine robotic manipulation tasks.
- **p. 6 / Abstract - extractive body cue:** As a result, FlowPolicy decodes high-quality robot actions in just one step of inference, which demonstrates the effectiveness of consistency flow matching in robot manipulation ...
- **p. 7 / Abstract - extractive body cue:** This further demonstrates that our proposed FlowPolicy has a more delicate understanding and generative ability in robot manipulation tasks.
- **p. 7 / Abstract - extractive body cue:** FlowPolicy accelerates the transfer of data from the noise to the action space by defining straightline flows, thereby improving the inference efficiency of robotic manipulation ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Abstract | EMPIRICAL / SIMULATION | Both generally improve the accuracy with more demonstrations, but FlowPolicy typically has a higher success rate and avoids the performance bottleneck as presented in ... | p. 7 (Abstract) |
| Abstract | EMPIRICAL / SIMULATION | For hard-level tasks (i.e., ‘Pick-Place'), the success rate of the task can be significantly improved by increasing the number of expert presentations, as shown ... | p. 7 (Abstract) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 4: Illustrations of the learning curves. Compared to Simple DP3 and DP3, FlowPolicy demonstrates higher sta- bility, learning efficiency, and success rates. all ... | p. 6 (Figure/Table caption) |
| Abstract | EMPIRICAL / SIMULATION | Among 3D-based baselines, our approach achieves the best success rate with the shortest inference time. | p. 6 (Abstract) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 1: Comparison of FlowPolicy with 2D-based method DP (Chi et al. 2023) and 3D-based methods DP3 (Ze et al. 2024) and Simple DP3 ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / Abstract - extractive body cue:** Experiments Dataset and Implementation Details Simulation Benchmarks We choose two preeminent environmental simulators, Adroit (Rajeswaran et al.
- **p. 5 / Abstract - extractive body cue:** In contrast, the Metaworld benchmark offers a diverse array of tasks that span the spectrum of difficulty levels, from easy to very hard, typically surmounted ...
- **p. 3 / Abstract - extractive body cue:** Visual observations include the robot state and scene point clouds, and actions are usually sequences of trajectories of the robot to accomplish a specific task.
- **p. 3 / Abstract - extractive body cue:** More importantly, Consistency-FM can be trained to produce a robust flow model without the aid of distillation, which is valuable to robots performing unseen tasks, ...
- **p. 4 / Abstract - extractive body cue:** With the conditional constraints of visual features, FlowPolicy enables the efficient capture of spatial information that is critical to fine robotic manipulation tasks.
- **p. 6 / Abstract - extractive body cue:** As a result, FlowPolicy decodes high-quality robot actions in just one step of inference, which demonstrates the effectiveness of consistency flow matching in robot manipulation ...
- **p. 7 / Abstract - extractive body cue:** This further demonstrates that our proposed FlowPolicy has a more delicate understanding and generative ability in robot manipulation tasks.
- **p. 7 / Abstract - extractive body cue:** FlowPolicy accelerates the transfer of data from the noise to the action space by defining straightline flows, thereby improving the inference efficiency of robotic manipulation ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Comparison of FlowPolicy with 2D-based method DP (Chi et al. 2023) and 3D-based methods DP3 (Ze et al. 2024) and Simple DP3 in ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Overall pipeline. The top section visualizes FlowPolicy, where a straight-line flow enables the fastest data transition from the noise distribution to the action ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Quantitative comparison of runtime between state-of-the-art policy models (Chi et al. 2023; Ze et al. 2024) and the proposed FlowPolicy. We evaluate 37 ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Comparisons on success rate between state-of-the-art 2D-based (Chi et al. 2023; Hu et al. 2024; Prasad et al. 2024) and 3D-based (Ze et ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative Comparison of FlowPolicy and DP3 (Ze et al. 2024) on two challenging manipulation tasks from Adroit and Metaworld. Our method successfully generates ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Illustrations of the learning curves. Compared to Simple DP3 and DP3, FlowPolicy demonstrates higher sta- bility, learning efficiency, and success rates. all success ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Ablation on the number of expert demonstrations. We choose four typical tasks to explore the impact of dif- ferent numbers of demonstrations on ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Experiments Dataset and Implementation Details Simulation Benchmarks We choose two preeminent environmental simulators, Adroit (Rajeswaran et al. | embodiment, simulator version and control stack | p. 5 (Abstract), p. 5 (Abstract) |
| Task/environment | In contrast, the Metaworld benchmark offers a diverse array of tasks that span the spectrum of difficulty levels, from easy to very hard, typically ... | reset, timeout, object/scene variation | p. 5 (Abstract), p. 3 (Abstract) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 3 (Abstract) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 5 (Abstract), p. 2 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Both generally improve the accuracy with more demonstrations, but FlowPolicy typically has a higher success rate and avoids the performance bottleneck as presented in ... | definition/direction/unit from same section | p. 7 (Abstract) |
| We evaluate 37 tasks from Adroit and Metaworld across 3 random seeds and report the success rate (%) with standard deviation. ‘∗' indicates that ... | definition/direction/unit from same section | p. 5 (Abstract) |
| However, DP3 reaches performance saturation more easily, which even leads to a decrease in the success rate when the number of demonstrations is sufficient ... | definition/direction/unit from same section | p. 7 (Abstract) |
| Figure 1: Comparison of FlowPolicy with 2D-based method DP (Chi et al. 2023) and 3D-based methods DP3 (Ze et al. 2024) and Simple DP3 ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The higher the success rate, the better, and the lower the NFE and inference time, the better. | definition/direction/unit from same section | p. 5 (Abstract) |
| Among 3D-based baselines, our approach achieves the best success rate with the shortest inference time. | definition/direction/unit from same section | p. 6 (Abstract) |
| Quantitative Comparisons on Success Rate Further, Table 2 shows the average success rate of each model on 37 tasks in Adroit and Metaworld. | definition/direction/unit from same section | p. 6 (Abstract) |
| In the training phase, we regress the consistency vector field and learn the straight-line flow through velocity consistency loss, which directly generates the robot ... | definition/direction/unit from same section | p. 4 (Abstract) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also compared state-of-the-art 2D-based approaches, including diffusion policy (DP) (Chi et al. | comparison identity and matched condition | p. 5 (Abstract) |
| 3D-based baselines generally outperform 2D-based ones, owing to the richer spatial representation offered by point clouds. | comparison identity and matched condition | p. 6 (Abstract) |
| Figure 4: Illustrations of the learning curves. Compared to Simple DP3 and DP3, FlowPolicy demonstrates higher sta- bility, learning efficiency, and success rates. all ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 1: Quantitative comparison of runtime between state-of-the-art policy models (Chi et al. 2023; Ze et al. 2024) and the proposed FlowPolicy. We evaluate ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| DP3 is the state-of-the-art 3D vision-based conditional diffusion policy model. | comparison identity and matched condition | p. 4 (Abstract) |
| For non-hard tasks (i.e., ‘Reach Wall', ‘Hammer'), FlowPolicy can outperform DP3 with a limited number of presentations. | comparison identity and matched condition | p. 7 (Abstract) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| More importantly, Consistency-FM can be trained to produce a robust flow model without the aid of distillation, which is valuable to robots performing unseen ... | component/input/data sensitivity | p. 3 (Abstract) |
| 2024) is a generalized method for efficiently learning straight-line flows without approximating the entire probabilistic path. | component/input/data sensitivity | p. 4 (Abstract) |
| We further conduct ablation studies to verify the influence of the number of expert demonstrations. | component/input/data sensitivity | p. 7 (Abstract) |
| Ablation Studies on Expert Demonstrations The success rate of the agent in accomplishing tasks depends on the number and quality of expert demonstrations, where ... | component/input/data sensitivity | p. 7 (Abstract) |
| Finally, we describe the design details of each component. | component/input/data sensitivity | p. 3 (Abstract) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and ... | Both generally improve the accuracy with more demonstrations, but FlowPolicy typically has a higher success rate and avoids the performance bottleneck as presented in ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Abstract), p. 7 (Abstract), p. 6 (Figure/Table caption), p. 6 (Abstract), p. 1 (Figure/Table caption), p. 5 (Abstract) |
| Primary metric/result | For hard-level tasks (i.e., ‘Pick-Place'), the success rate of the task can be significantly improved by increasing the number of expert presentations, as shown ... | numeric claim only at cited anchor | p. 7 (Abstract) |

- Numeric sentences retained from the body:
- **p. 5 / Abstract - extractive body cue:** Methods NFE Adroit Metaworld Average Hammer Door Pen Easy(21) Medium(4) Hard(4) Very Hard(5) DP 10 103.6±0.6 102.5±0.4 94.9±6.7 104.9±2.2 105.3±0.6 120.3±1.4 103.3±2.7 106.1±2.4 DP3 10 ...
- **p. 5 / Abstract - extractive body cue:** We evaluate 37 tasks from Adroit and Metaworld across 3 random seeds and report inference time per step (ms) with standard deviation.
- **p. 5 / Abstract - extractive body cue:** Our FlowPolicy enables real-time robot operations with an average time of 19.9ms in onestep inference, which is 7 × faster than DP3 and 3 × ...
- **p. 5 / Abstract - extractive body cue:** Methods NFE Adroit Metaworld Average Hammer Door Pen Easy(21) Medium(4) Hard(4) Very Hard(5) DP 10 16±10 34±11 13±2 50.7±6.1 11.0±2.5 5.25±2.5 22.0±5.0 35.2±5.3 Adaflow∗ - ...
- **p. 5 / Abstract - extractive body cue:** We evaluate 37 tasks from Adroit and Metaworld across 3 random seeds and report the success rate (%) with standard deviation. ‘∗' indicates that the ...
- **p. 5 / Abstract - extractive body cue:** 2021), as our benchmarks for a comprehensive set of 37 tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our method successfully generates high-quality actions at real-time speeds, completing these tasks effectively, whereas DP3 either produces lower-quality actions (left) or fails to complete ... | p. 6 (Abstract) |
| body limitation/failure cue | DP3 unsuccessfully picks up the red cube and fails the task. | p. 7 (Abstract) |
| body limitation/failure cue | Although DP3 accomplishes the dexterity task, the diffusion policy generated based on DP3 fails to ensure consistency with the target pen in 3D space ... | p. 7 (Abstract) |
| body limitation/failure cue | Due to the complexity of the target distribution solution, Consistency-FM does not regress directly on the ground truth vector field, instead, it directly defines ... | p. 4 (Abstract) |
| body limitation/failure cue | Expert demonstrations Policy FlowPolicy State Noise a1 a0 Action Flow Network Execute Single-view Images Robot state Encoder Sparse 3D Encoder Compact 3D Repr. | p. 3 (Abstract) |
| body limitation/failure cue | The top section visualizes FlowPolicy, where a straight-line flow enables the fastest data transition from the noise distribution to the action distribution (Adroit: Open ... | p. 3 (Abstract) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each task is run repeatedly under three different random seeds, and their means and variances as well as inference times are calculated. | p. 5 (Abstract) |
| During the training phase, the weights are updated using the AdamW optimizer with a learning rate of 1e-4 and a batch size of 128. | p. 6 (Abstract) |
| We evaluate 37 tasks from Adroit and Metaworld across 3 random seeds and report inference time per step (ms) with standard deviation. | p. 5 (Abstract) |
| Comparison with State-of-the-art Methods Quantitative Comparisons on Runtime Table 1 reports the average inference time of each model for 3 dexterity tasks from Adroit ... | p. 6 (Abstract) |
| Nevertheless, diffusion-based solutions are inevitably plagued by substantial runtime inefficiencies, as they typically require numerous sampling steps during inference to generate high-quality actions. | p. 2 (Abstract) |
| 2024) and Simple DP3 in terms of inference time and average success rate on Adroit and Metaworld. | p. 1 (Abstract) |
| 0 30 60 90 120 150 0 20 40 60 80 Inference time (ms) Success rate (%) FlowPolicy(ours) (one-step) Simple DP3 DP3 Metaworld DP ... | p. 1 (Abstract) |
| 1, our approach achieves a 7× reduction in average inference time while maintaining a competitive average success rate compared to state-of-the-art methods based on ... | p. 2 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Abstract - extractive body cue:** Our method successfully generates high-quality actions at real-time speeds, completing these tasks effectively, whereas DP3 either produces lower-quality actions (left) or fails to complete the ...
- **p. 7 / Abstract - extractive body cue:** DP3 unsuccessfully picks up the red cube and fails the task.
- **p. 7 / Abstract - extractive body cue:** Although DP3 accomplishes the dexterity task, the diffusion policy generated based on DP3 fails to ensure consistency with the target pen in 3D space compared ...
- **p. 4 / Abstract - extractive body cue:** Due to the complexity of the target distribution solution, Consistency-FM does not regress directly on the ground truth vector field, instead, it directly defines a ...
- **p. 3 / Abstract - extractive body cue:** Expert demonstrations Policy FlowPolicy State Noise a1 a0 Action Flow Network Execute Single-view Images Robot state Encoder Sparse 3D Encoder Compact 3D Repr.
- **p. 3 / Abstract - extractive body cue:** The top section visualizes FlowPolicy, where a straight-line flow enables the fastest data transition from the noise distribution to the action distribution (Adroit: Open the ...

- **Evidence anchors reviewed:** datasets p. 5 (Abstract), p. 5 (Abstract), p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 6 (Abstract), metrics p. 7 (Abstract), p. 5 (Abstract), p. 7 (Abstract), p. 1 (Figure/Table caption), p. 5 (Abstract), p. 6 (Abstract), baselines p. 5 (Abstract), p. 6 (Abstract), p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), p. 4 (Abstract), p. 7 (Abstract), results p. 7 (Abstract), p. 7 (Abstract), p. 6 (Figure/Table caption), p. 6 (Abstract), p. 1 (Figure/Table caption), p. 5 (Abstract).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 5: Ablation on the number of expert demonstrations. We choose four typical tasks to explore the impact of dif- ferent numbers of demonstrations on FlowPolicy and DP3. Both generally ... (p. 7, Figure/Table caption).
- **Metric evidence:** Both generally improve the accuracy with more demonstrations, but FlowPolicy typically has a higher success rate and avoids the performance bottleneck as presented in DP3. (p. 7, Abstract).
- **Baseline/ablation evidence:** We also compared state-of-the-art 2D-based approaches, including diffusion policy (DP) (Chi et al. (p. 5, Abstract).
- **Failure/negative evidence:** Our method successfully generates high-quality actions at real-time speeds, completing these tasks effectively, whereas DP3 either produces lower-quality actions (left) or fails to complete the task (right). task. (p. 6, Abstract).
