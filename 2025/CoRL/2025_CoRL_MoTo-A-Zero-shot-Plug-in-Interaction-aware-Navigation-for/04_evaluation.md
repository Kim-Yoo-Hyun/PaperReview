# Evaluation - MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/wu25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25c/wu25c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment), p. 13 (A.3 Training Details), p. 2 (Figure/Table caption)): All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best view in color). success rate further ...

## Evaluation Body Digest

- **p. 13 / A.1 Simulator Experiment - extractive PDF cue:** The OVMM benchmark consists of 60 extensive indoor scenes and contains more than 18k 3D models of everyday objects.OVMM utilizes Hello Robot as an agent ...
- **p. 13 / A.2 Real World Experiment - extractive PDF cue:** For the real-world experiments, we use HEXMOVE as the base and two PiPER robotic arms to build a dual-arm mobile manipulation robot, which is equipped ...
- **p. 8 / 5 Experiment - extractive PDF cue:** Avg "Bring me food." "Serve me water." "Prepare a meal." 0 0.2 0.4 0.6 0.8 1 Success Rate Avg "Bring me food." "Serve me water." ...
- **p. 7 / 5 Experiment - extractive PDF cue:** Our training and testing methods fully comply with the OVMM baseline settings (Home-Robot).
- **p. 7 / 5 Experiment - extractive PDF cue:** As shown in Table 1, Home-Robot w/ MoTo outperforms Home-Robot (RL), achieving a 3.52% higher overall success rate.
- **p. 8 / 5 Experiment - extractive PDF cue:** Wrong interaction keypoints will result in the robot moving elsewhere due to physical constraints that prevent it from performing fixed-base manipulation actions.
- **p. 14 / A.3 Training Details - extractive PDF cue:** The target is the object to be interacted with, and the subgoal is the condition that needs to be completed.
- **p. 8 / 5 Experiment - extractive PDF cue:** All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best view ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** 5 Experiment (p. 7); A Implementation Details (p. 13); A.1 Simulator Experiment (p. 13); A.2 Real World Experiment (p. 13).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best ... | p. 8 (5 Experiment) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, Home-Robot w/ MoTo outperforms Home-Robot (RL), achieving a 3.52% higher overall success rate. | p. 7 (5 Experiment) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Since L3MVN only ensures proximity to the target while ignoring the feasibility of subsequent manipulations, it yields only a marginal overall success rate gain ... | p. 8 (5 Experiment) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | The similar success rates in stages FindObj and Pick are due to MoTo's focus on interaction-aware navigation, which is invoked only after finding a ... | p. 7 (5 Experiment) |
| A.3 Training Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | We ensured the diversity of viewpoints in the expert trajectories during the collection process in order to achieve a higher viewpoint generalization. | p. 13 (A.3 Training Details) |

## Dataset / Benchmark Role

- **p. 13 / A.1 Simulator Experiment - extractive PDF cue:** The OVMM benchmark consists of 60 extensive indoor scenes and contains more than 18k 3D models of everyday objects.OVMM utilizes Hello Robot as an agent ...
- **p. 13 / A.2 Real World Experiment - extractive PDF cue:** For the real-world experiments, we use HEXMOVE as the base and two PiPER robotic arms to build a dual-arm mobile manipulation robot, which is equipped ...
- **p. 8 / 5 Experiment - extractive PDF cue:** Avg "Bring me food." "Serve me water." "Prepare a meal." 0 0.2 0.4 0.6 0.8 1 Success Rate Avg "Bring me food." "Serve me water." ...
- **p. 7 / 5 Experiment - extractive PDF cue:** Our training and testing methods fully comply with the OVMM baseline settings (Home-Robot).
- **p. 7 / 5 Experiment - extractive PDF cue:** As shown in Table 1, Home-Robot w/ MoTo outperforms Home-Robot (RL), achieving a 3.52% higher overall success rate.
- **p. 8 / 5 Experiment - extractive PDF cue:** Wrong interaction keypoints will result in the robot moving elsewhere due to physical constraints that prevent it from performing fixed-base manipulation actions.
- **p. 14 / A.3 Training Details - extractive PDF cue:** The target is the object to be interacted with, and the subgoal is the condition that needs to be completed.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: MoTo can be plugged into any fixed-base manipulation model and transferred to mobile manipulation tasks in a zero-shot manner, enabling generalized mobile manipulation. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The pipeline of MoTo. Based on robot scanning RGB-D observation to get 3D scene point clouds and graphs, we utilize VLM and multi-view ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison results on the OVMM benchmark. Partial success rates indicate the execution of each stage, conditioned on the success of the preceding one. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation experiments for optimization cost terms and keypoint generation variants.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3: Real-world experimental results. All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 4: Real-world experimental platforms and deployment environments. A.2 Real World Experiment For the real-world experiments, we use HEXMOVE as the base and two PiPER ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 3: Real-world task instructions. The target is the object to be interacted with, and the subgoal is the condition that needs to be completed. ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 5: Visualization of mobile manipulation trajectories for real-world experiments. object to reduce the optimized search space, searching for the optimal arm joint angle {θarm ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The OVMM benchmark consists of 60 extensive indoor scenes and contains more than 18k 3D models of everyday objects.OVMM utilizes Hello Robot as an ... | embodiment, simulator version and control stack | p. 13 (A.1 Simulator Experiment), p. 13 (A.2 Real World Experiment) |
| Task/environment | For the real-world experiments, we use HEXMOVE as the base and two PiPER robotic arms to build a dual-arm mobile manipulation robot, which is ... | reset, timeout, object/scene variation | p. 13 (A.2 Real World Experiment), p. 8 (5 Experiment) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best ... | definition/direction/unit from same section | p. 8 (5 Experiment) |
| The inconsistency of multi-view keypoints in the "w/o Fusion" setting results in a serious performance drop (2.42% lower success rate compared to Single View), ... | definition/direction/unit from same section | p. 8 (5 Experiment) |
| As shown in Table 1, Home-Robot w/ MoTo outperforms Home-Robot (RL), achieving a 3.52% higher overall success rate. | definition/direction/unit from same section | p. 7 (5 Experiment) |
| The similar success rates in stages FindObj and Pick are due to MoTo's focus on interaction-aware navigation, which is invoked only after finding a ... | definition/direction/unit from same section | p. 7 (5 Experiment) |
| Figure 1: MoTo can be plugged into any fixed-base manipulation model and transferred to mobile manipulation tasks in a zero-shot manner, enabling generalized mobile ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 2: The pipeline of MoTo. Based on robot scanning RGB-D observation to get 3D scene point clouds and graphs, we utilize VLM and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| To better fine-tune OpenVLA [11] to mitigate cross-robot ontology differences, we collected a total of 20k data and fine-tuned 10k epoch on 8 RTX ... | definition/direction/unit from same section | p. 13 (A.3 Training Details) |
| We fine-tuned the model for 150,000 gradient steps on 8 NVIDIA RTX 4090 GPUs (total batch size 128) using the AdamW optimizer (learning rate ... | definition/direction/unit from same section | p. 13 (A.3 Training Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 5.1 Comparison with State-of-the-art Methods Table 1 demonstrates the performance of MoTo on the OVMM [18] validation set compared to the baseline, decomposing it ... | comparison identity and matched condition | p. 7 (5 Experiment) |
| Our training and testing methods fully comply with the OVMM baseline settings (Home-Robot). | comparison identity and matched condition | p. 7 (5 Experiment) |
| 5.3 Real World Experiments The OVMM baseline cannot be directly deployed in the real world due to the sim-to-real gap. | comparison identity and matched condition | p. 8 (5 Experiment) |
| Interestingly, iDP3 and AnyGrasp outperform RDT-1B in mobile manipulation, owing to stronger viewpoint generalization from 3D point cloud observations. | comparison identity and matched condition | p. 8 (5 Experiment) |
| We utilize an OVMM-heuristic baseline to collect manipulation expert trajectories that include robot proprioception, action, and visual observations to fine-tune off-the-shelf manipulation foundation models. | comparison identity and matched condition | p. 13 (A.1 Simulator Experiment) |
| In the OVMM simulator, we collect expert demonstration data for pick-and-place during mobile manipulation with heuristic baselines. | comparison identity and matched condition | p. 13 (A.3 Training Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2: Ablation experiments for optimization cost terms and keypoint generation variants. | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| The similar success rates in stages FindObj and Pick are due to MoTo's focus on interaction-aware navigation, which is invoked only after finding a ... | component/input/data sensitivity | p. 7 (5 Experiment) |
| We further investigated variants of the keypoint extraction and fusion pipeline. | component/input/data sensitivity | p. 8 (5 Experiment) |
| 5.2 Ablation Study Table 2 reports a systematic ablation of our full MoTo pipeline in OVMM, isolating the contribution of each optimization cost term ... | component/input/data sensitivity | p. 8 (5 Experiment) |
| We utilize an OVMM-heuristic baseline to collect manipulation expert trajectories that include robot proprioception, action, and visual observations to fine-tune off-the-shelf manipulation foundation models. | component/input/data sensitivity | p. 13 (A.1 Simulator Experiment) |
| To better fine-tune OpenVLA [11] to mitigate cross-robot ontology differences, we collected a total of 20k data and fine-tuned 10k epoch on 8 RTX ... | component/input/data sensitivity | p. 13 (A.3 Training Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo). | All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment), p. 13 (A.3 Training Details), p. 2 (Figure/Table caption) |
| Primary metric/result | As shown in Table 1, Home-Robot w/ MoTo outperforms Home-Robot (RL), achieving a 3.52% higher overall success rate. | numeric claim only at cited anchor | p. 7 (5 Experiment) |

- Numeric sentences retained from the body:
- **p. 13 / A.1 Simulator Experiment - extractive PDF cue:** The simulator experiments are training and testing on 8 RTX 3090 GPUs.
- **p. 13 / A.2 Real World Experiment - extractive PDF cue:** The real-world experiments are all performed on a single RTX 4060 GPU.
- **p. 13 / A.3 Training Details - extractive PDF cue:** To better fine-tune OpenVLA [11] to mitigate cross-robot ontology differences, we collected a total of 20k data and fine-tuned 10k epoch on 8 RTX 3090 ...
- **p. 13 / A.3 Training Details - extractive PDF cue:** We fine-tuned the model for 150,000 gradient steps on 8 NVIDIA RTX 4090 GPUs (total batch size 128) using the AdamW optimizer (learning rate 1×10-4, ...
- **p. 13 / A.3 Training Details - extractive PDF cue:** To better fine-tune OpenVLA [11] to mitigate cross-robot ontology differences, we collected a total of 20k data and fine-tuned 10k epoch on 8 RTX 3090 ...
- **p. 13 / A.3 Training Details - extractive PDF cue:** We fine-tuned the model for 150,000 gradient steps on 8 NVIDIA RTX 4090 GPUs (total batch size 128) using the AdamW optimizer (learning rate 1×10-4, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into 3D space and votes to generate ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Figure 7: Failure Cases in real-world experiments. D.1 Manipulation Visualization Figure 6 demonstrates the scene keypoint generation and mobile trajectory in task "Serve me ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | 5.3 Real World Experiments The OVMM baseline cannot be directly deployed in the real world due to the sim-to-real gap. | p. 8 (5 Experiment) |
| body limitation/failure cue | The inconsistency of multi-view keypoints in the "w/o Fusion" setting results in a serious performance drop (2.42% lower success rate compared to Single View), ... | p. 8 (5 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We fine-tuned the model for 150,000 gradient steps on 8 NVIDIA RTX 4090 GPUs (total batch size 128) using the AdamW optimizer (learning rate ... | p. 13 (A.3 Training Details) |
| The implementation details are in Appendix A.1. | p. 7 (5 Experiment) |
| All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best ... | p. 8 (5 Experiment) |
| The real-world experiments are all performed on a single RTX 4060 GPU. | p. 13 (A.2 Real World Experiment) |
| We uniformly sample Nq query points on the robot surface Ωto evaluate the collision cost: Fc t = Nq X j=1 max(0, ϵ0 -D(qj ... | p. 6 (4 Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into 3D space and votes to generate keypoints ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 7: Failure Cases in real-world experiments. D.1 Manipulation Visualization Figure 6 demonstrates the scene keypoint generation and mobile trajectory in task "Serve me water". ...
- **p. 8 / 5 Experiment - extractive PDF cue:** 5.3 Real World Experiments The OVMM baseline cannot be directly deployed in the real world due to the sim-to-real gap.
- **p. 8 / 5 Experiment - extractive PDF cue:** The inconsistency of multi-view keypoints in the "w/o Fusion" setting results in a serious performance drop (2.42% lower success rate compared to Single View), because ...

- **PDF anchors reviewed:** datasets p. 13 (A.1 Simulator Experiment), p. 13 (A.2 Real World Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment), metrics p. 8 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 2 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 7 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment), p. 8 (5 Experiment), p. 13 (A.1 Simulator Experiment), p. 13 (A.3 Training Details), results p. 8 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment), p. 13 (A.3 Training Details), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
