# Evaluation - SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 8 (4.3. Ablation study), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 8 (4.3. Ablation study)): Our approach consistently achieves a substantially higher success rate than baselines, highlighting the effectiveness of simulation-enabled VLMs for action planning.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We use ⇡0.5 [2], a recent open-source VLA model pretrained on a large robot manipulation dataset, as a representative baseline.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We compare our approach against the following baselines: (1) VLA models that are trained on largescale robot action datasets to directly predict joint velocities from ...
- **p. 7 / 4.2. Results - extractive body cue:** 5 shows simulation and real-world rollouts of six of our seven tasks.
- **p. 5 / 4. Experiments - extractive body cue:** To evaluate the effectiveness of our framework, we design seven challenging, real-world, physics-aware, fine-grained manipulation tasks.
- **p. 7 / 4.2. Results - extractive body cue:** In contrast, our method integrates simulation-enabled reasoning with VLM, enabling the robot to iteratively refine its action plan using simulation rollouts as context.
- **p. 8 / 4.5. Limitations - extractive body cue:** We include an optional replanning mechanism for recovery that updates the simulator using real-world feedback (see Suppl.
- **p. 8 / 4.4. Failure Case Analysis - extractive body cue:** Execution failures arise when kinematic or dynamic discrepancies between simulation and reality cause actions that succeed in simulation to fail in real-world execution.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We evaluate our system using a Franka Research 3 robot arm with a parallel-jaw gripper.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach consistently achieves a substantially higher success rate than baselines, highlighting the effectiveness of simulation-enabled VLMs for action planning. | p. 6 (4.1. Experimental Setup) |
| 4.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | VLM-based methods, VoxPoser and MOKA, leveraging VLM's strong sceneunderstanding and reasoning capabilities, achieve non-zero success rates on tasks such as bowl stacking, shape rope ... | p. 7 (4.2. Results) |
| 4.3. Ablation study | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1) affects performance, reporting success rates over 10 trials in Table 4: using only 3 samples degrades performance, as limited rollouts fail to provide ... | p. 8 (4.3. Ablation study) |
| 4.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | 10 shows the results of the remaining task. achieve a sufficiently large contact area. | p. 6 (4.1. Experimental Setup) |
| 4.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, our method consistently outperforms baseline methods across all evaluated tasks, highlighting its strong performance on challenging, physicsaware, fine-grained manipulation tasks. | p. 7 (4.2. Results) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We use ⇡0.5 [2], a recent open-source VLA model pretrained on a large robot manipulation dataset, as a representative baseline.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We compare our approach against the following baselines: (1) VLA models that are trained on largescale robot action datasets to directly predict joint velocities from ...
- **p. 7 / 4.2. Results - extractive body cue:** 5 shows simulation and real-world rollouts of six of our seven tasks.
- **p. 5 / 4. Experiments - extractive body cue:** To evaluate the effectiveness of our framework, we design seven challenging, real-world, physics-aware, fine-grained manipulation tasks.
- **p. 7 / 4.2. Results - extractive body cue:** In contrast, our method integrates simulation-enabled reasoning with VLM, enabling the robot to iteratively refine its action plan using simulation rollouts as context.
- **p. 8 / 4.5. Limitations - extractive body cue:** We include an optional replanning mechanism for recovery that updates the simulator using real-world feedback (see Suppl.
- **p. 8 / 4.4. Failure Case Analysis - extractive body cue:** Execution failures arise when kinematic or dynamic discrepancies between simulation and reality cause actions that succeed in simulation to fail in real-world execution.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We evaluate our system using a Franka Research 3 robot arm with a parallel-jaw gripper.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Simulation-Enabled VLM Action Planning. Given a single RGB-D image and a language task description (left), our method efficiently constructs a physics simulator that ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Simulation construction from a single RGBD image. Given an RGB-D image and a language task description, our pipeline automatically generates either a mesh-based ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Method overview. Our method first instantiates a physics simulator given the real-world scene. Next, a VLM-based action sampler and optimizer iteratively refine the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Action optimization process. We show a representative example from the non-toppling push task. The left three images show simulation rollouts from initial VLM-sampled ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Definition of tasks. For each manipulation task, we list the corresponding instruction and success criteria. Tasks Instruction Success Condition Non-toppling push Push the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Success rates of our method and baselines. For each task, we run 10 trials per method. Our approach consistently achieves a substantially higher ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results. The figure shows the initial state, execution progress, and final state for six tasks in both the real world (top) and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation. Success rates (%) over 10 trials for each task after removing each component of our method. Results demonstrate the importance of VLM-conditioned ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use ⇡0.5 [2], a recent open-source VLA model pretrained on a large robot manipulation dataset, as a representative baseline. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | We compare our approach against the following baselines: (1) VLA models that are trained on largescale robot action datasets to directly predict joint velocities ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 5 (3.2. Action Planning via Simulation-enabled VLM) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3.1. Simulation Construction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 1) affects performance, reporting success rates over 10 trials in Table 4: using only 3 samples degrades performance, as limited rollouts fail to provide ... | definition/direction/unit from same section | p. 8 (4.3. Ablation study) |
| Success rates of our method and baselines. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Success rate is our primary evaluation metric. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| VLM-based methods, VoxPoser and MOKA, leveraging VLM's strong sceneunderstanding and reasoning capabilities, achieve non-zero success rates on tasks such as bowl stacking, shape rope ... | definition/direction/unit from same section | p. 7 (4.2. Results) |
| Success rates (%) over 10 trials varying numbers of in-context examples for tasks non-toppling push, bowl stacking, shape rope. #Samples Non-toppling push Bowl stacking ... | definition/direction/unit from same section | p. 8 (4.3. Ablation study) |
| However, they struggle with tasks that require precise action planning, where small errors, such as pushing the wrong part of an object (in non-toppling ... | definition/direction/unit from same section | p. 7 (4.2. Results) |
| Figure 2. Simulation construction from a single RGBD image. Given an RGB-D image and a language task description, our pipeline automatically generates either a ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. Method overview. Our method first instantiates a physics simulator given the real-world scene. Next, a VLM-based action sampler and optimizer iteratively refine ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Overall, our method consistently outperforms baseline methods across all evaluated tasks, highlighting its strong performance on challenging, physicsaware, fine-grained manipulation tasks. | comparison identity and matched condition | p. 7 (4.2. Results) |
| However, the variant still outperforms baseline methods, largely due to the hierarchical action sampling strategy introduced in Sec. | comparison identity and matched condition | p. 8 (4.3. Ablation study) |
| Qualitative comparison with baseline methods. | comparison identity and matched condition | p. 7 (4.1. Experimental Setup) |
| We assess whether our method enables zero-shot planning on these tasks, comparing it against other state-of-the-art zero-shot methods. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Success rates of our method and baselines. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| We use ⇡0.5 [2], a recent open-source VLA model pretrained on a large robot manipulation dataset, as a representative baseline. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| (2) Removing simulation rollout context: We evaluate whether current VLMs can reason effectively without simulation rollouts. | component/input/data sensitivity | p. 7 (4.3. Ablation study) |
| Table 3. Ablation. Success rates (%) over 10 trials for each task after removing each component of our method. Results demonstrate the importance of ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We validate our design choices through systematic ablation studies. | component/input/data sensitivity | p. 5 (4. Experiments) |
| For simulation, we implement the projective dynamics variant solver using PyTorch [47] and the MPM simulator using Warp [39]. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| This indicates that language-based reasoning without physical grounding cannot reliably infer successful action. | component/input/data sensitivity | p. 8 (4.3. Ablation study) |
| However, the variant still outperforms baseline methods, largely due to the hierarchical action sampling strategy introduced in Sec. | component/input/data sensitivity | p. 8 (4.3. Ablation study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We ... | Our approach consistently achieves a substantially higher success rate than baselines, highlighting the effectiveness of simulation-enabled VLMs for action planning. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 8 (4.3. Ablation study), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 8 (4.3. Ablation study) |
| Primary metric/result | VLM-based methods, VoxPoser and MOKA, leveraging VLM's strong sceneunderstanding and reasoning capabilities, achieve non-zero success rates on tasks such as bowl stacking, shape rope ... | numeric claim only at cited anchor | p. 7 (4.2. Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We evaluate our system using a Franka Research 3 robot arm with a parallel-jaw gripper.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For each task, we run 10 trials per method.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Success rates (%) over 10 trials for each task after removing each component of our method.
- **p. 8 / 4.3. Ablation study - extractive body cue:** Success rates (%) over 10 trials varying numbers of in-context examples for tasks non-toppling push, bowl stacking, shape rope. #Samples Non-toppling push Bowl stacking Shape ...
- **p. 8 / 4.3. Ablation study - extractive body cue:** 1) affects performance, reporting success rates over 10 trials in Table 4: using only 3 samples degrades performance, as limited rollouts fail to provide sufficient ...
- **p. 4 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** I0, `task, s0; VLM " }; 5 S S [ {si SIMROLLOUT ! s0, ai; SIM " }; // Iterative action optimization 6 for k ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Planning failures occur when the robot fails to generate a feasible action sequence even after multiple rounds of action optimization. | p. 8 (4.4. Failure Case Analysis) |
| body limitation/failure cue | Failures are categorized as perception, planning, or execution. successful action sequence is particularly challenging. | p. 8 (4.4. Failure Case Analysis) |
| body limitation/failure cue | We show representative failures from baseline methods that lack simulationenabled reasoning. | p. 7 (4.1. Experimental Setup) |
| body limitation/failure cue | However, they struggle with tasks that require precise action planning, where small errors, such as pushing the wrong part of an object (in non-toppling ... | p. 7 (4.2. Results) |
| body limitation/failure cue | Table 1. Definition of tasks. For each manipulation task, we list the corresponding instruction and success criteria. Tasks Instruction Success Condition Non-toppling push Push ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Figure 4. Action optimization process. We show a representative example from the non-toppling push task. The left three images show simulation rollouts from initial ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each task, we run 10 trials per method. | p. 6 (4.1. Experimental Setup) |
| Success rates (%) over 10 trials varying numbers of in-context examples for tasks non-toppling push, bowl stacking, shape rope. #Samples Non-toppling push Bowl stacking ... | p. 8 (4.3. Ablation study) |
| 1) affects performance, reporting success rates over 10 trials in Table 4: using only 3 samples degrades performance, as limited rollouts fail to provide ... | p. 8 (4.3. Ablation study) |
| For each action sequence, we construct an optimization context ci by subsampling time steps and gathering intermediate information. | p. 5 (3.2. Action Planning via Simulation-enabled VLM) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.4. Failure Case Analysis - extractive body cue:** Planning failures occur when the robot fails to generate a feasible action sequence even after multiple rounds of action optimization.
- **p. 8 / 4.4. Failure Case Analysis - extractive body cue:** Failures are categorized as perception, planning, or execution. successful action sequence is particularly challenging.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** We show representative failures from baseline methods that lack simulationenabled reasoning.
- **p. 7 / 4.2. Results - extractive body cue:** However, they struggle with tasks that require precise action planning, where small errors, such as pushing the wrong part of an object (in non-toppling push) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Definition of tasks. For each manipulation task, we list the corresponding instruction and success criteria. Tasks Instruction Success Condition Non-toppling push Push the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Action optimization process. We show a representative example from the non-toppling push task. The left three images show simulation rollouts from initial VLM-sampled ...

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 5 (4. Experiments), p. 7 (4.2. Results), p. 8 (4.5. Limitations), metrics p. 8 (4.3. Ablation study), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 8 (4.3. Ablation study), p. 7 (4.2. Results), baselines p. 7 (4.2. Results), p. 8 (4.3. Ablation study), p. 7 (4.1. Experimental Setup), p. 5 (4. Experiments), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), results p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 8 (4.3. Ablation study), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 8 (4.3. Ablation study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 3. Ablation. Success rates (%) over 10 trials for each task after removing each component of our method. Results demonstrate the importance of VLM-conditioned sampling and the VLM's simulation-enabled ... (p. 7, Figure/Table caption).
- **Metric evidence:** Success rates (%) over 10 trials varying numbers of in-context examples for tasks non-toppling push, bowl stacking, shape rope. #Samples Non-toppling push Bowl stacking Shape rope 3 samples 50% 50% ... (p. 8, 4.3. Ablation study).
- **Baseline/ablation evidence:** Qualitative comparison with baseline methods. (p. 7, 4.1. Experimental Setup).
- **Failure/negative evidence:** However, they struggle with tasks that require precise action planning, where small errors, such as pushing the wrong part of an object (in non-toppling push) or squeezing an incorrect region ... (p. 7, 4.2. Results).
