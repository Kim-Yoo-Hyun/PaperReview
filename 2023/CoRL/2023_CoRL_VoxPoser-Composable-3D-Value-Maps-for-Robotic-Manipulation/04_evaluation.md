# Evaluation - VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.05973; PDF retrieval source: https://arxiv.org/pdf/2307.05973. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (3 Method), p. 22 (A.5.2 Full Results on Simulated Environments), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method)): VoxPoser outperforms both baselines across 13 tasks from two categories on both seen and unseen tasks and maintains similar success rates. smoother trajectories but takes more time for optimization.

## Evaluation Body Digest

- **p. 7 / 3 Method - extractive body cue:** 4.2 Generalization to Unseen Instructions and Attributes To provide rigorous quantitative evaluations on generalization, we set up a simulated block-world environment that mirrors our real-world ...
- **p. 18 / A.1 Code Release - extractive body cue:** We provide an open-sourced implementation of VoxPoser at github.com/huangwl18/VoxPoser based on RLBench [134], as its diversity of tasks and scenes best resembles our real-world setup.
- **p. 20 / A.4 Real-World Environment Setup - extractive body cue:** For tasks with disturbances, we apply three kinds of disturbances to the environment, which we pre-select a sequence of them at the start of the ...
- **p. 18 / A.2 Emergent Behavioral Capabilities - extractive body cue:** VoxPoser similarly adjusts its action based on the feedback. • Multi-step Visual Program [136, 137]: Given a task "open the drawer precisely by half" where ...
- **p. 7 / 3 Method - extractive body cue:** We find that VoxPoser can effectively synthesize robot trajectories for everyday manipulation tasks with a high average success rate.
- **p. 21 / A.5 Simulated Environment Setup - extractive body cue:** We implement a tabletop manipulation environment with a Franka Emika Panda robot in SAPIEN [120].
- **p. 19 / A.3 APIs for VoxPoser - extractive body cue:** Besides exposing NumPy [16] and the Transforms3d library to the LLM, we provide the following environment APIs that LLMs can choose to invoke: detect(obj name): ...
- **p. 8 / 3 Method - extractive body cue:** This observation aligns with our real-world experiment, where most errors are from perception.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** A.5.2 Full Results on Simulated Environments (p. 22).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 3 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | VoxPoser outperforms both baselines across 13 tasks from two categories on both seen and unseen tasks and maintains similar success rates. smoother trajectories but ... | p. 7 (3 Method) |
| A.5.2 Full Results on Simulated Environments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Each entry represents success rate averaged across 20 episodes. | p. 22 (A.5.2 Full Results on Simulated Environments) |
| 3 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that VoxPoser can effectively synthesize robot trajectories for everyday manipulation tasks with a high average success rate. | p. 7 (3 Method) |
| 3 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, we can learn an effective dynamics model with less than 3 minutes of online interactions by using these trajectories as exploration prior, leading ... | p. 8 (3 Method) |
| 3 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4, VoxPoser achieves lowest "specification error" due to its generalization and flexibility. | p. 8 (3 Method) |

## Dataset / Benchmark Role

- **p. 7 / 3 Method - extractive body cue:** 4.2 Generalization to Unseen Instructions and Attributes To provide rigorous quantitative evaluations on generalization, we set up a simulated block-world environment that mirrors our real-world ...
- **p. 18 / A.1 Code Release - extractive body cue:** We provide an open-sourced implementation of VoxPoser at github.com/huangwl18/VoxPoser based on RLBench [134], as its diversity of tasks and scenes best resembles our real-world setup.
- **p. 20 / A.4 Real-World Environment Setup - extractive body cue:** For tasks with disturbances, we apply three kinds of disturbances to the environment, which we pre-select a sequence of them at the start of the ...
- **p. 18 / A.2 Emergent Behavioral Capabilities - extractive body cue:** VoxPoser similarly adjusts its action based on the feedback. • Multi-step Visual Program [136, 137]: Given a task "open the drawer precisely by half" where ...
- **p. 7 / 3 Method - extractive body cue:** We find that VoxPoser can effectively synthesize robot trajectories for everyday manipulation tasks with a high average success rate.
- **p. 21 / A.5 Simulated Environment Setup - extractive body cue:** We implement a tabletop manipulation environment with a Franka Emika Panda robot in SAPIEN [120].
- **p. 19 / A.3 APIs for VoxPoser - extractive body cue:** Besides exposing NumPy [16] and the Transforms3d library to the LLM, we provide the following environment APIs that LLMs can choose to invoke: detect(obj name): ...
- **p. 8 / 3 Method - extractive body cue:** This observation aligns with our real-world experiment, where most errors are from perception.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: VOXPOSER extracts language-conditioned affordances and constraints from LLMs and grounds them to the perceptual space using VLMs, using a code interface and without ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of VOXPOSER. Given the RGB-D observation of the environment and a language in- struction, LLMs generate code, which interacts with VLMs, to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of composed 3D value maps and rollouts in real-world environments. The top row demonstrates where "entity of interest" is an object or ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Success rate in real-world domain. Vox- Poser performs everyday manipulation tasks with high success and is more robust to disturbances than the baseline ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Success rate in simulated domain. "SI" and "UI" are seen and unseen instructions. "SA" and "UA" are seen and unseen attributes. VoxPoser outperforms ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: VoxPoser enables efficient dynamics learning by using zero-shot synthesized trajectories as prior. TLE (time limit exceeded) means exceeding 12 hours. Results are re- ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Error breakdown of components. Vox- Poser significantly reduces specification error. each represented as a sequence of end-effector waypoints, that act as priors for ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 5: Emergent behavioral capabilities by VoxPoser inherited from the language model, including behav- ioral commonsense reasoning (top left), fine-grained language correction (top right), multi-step ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.2 Generalization to Unseen Instructions and Attributes To provide rigorous quantitative evaluations on generalization, we set up a simulated block-world environment that mirrors our ... | embodiment, simulator version and control stack | p. 7 (3 Method), p. 18 (A.1 Code Release) |
| Task/environment | We provide an open-sourced implementation of VoxPoser at github.com/huangwl18/VoxPoser based on RLBench [134], as its diversity of tasks and scenes best resembles our real-world ... | reset, timeout, object/scene variation | p. 18 (A.1 Code Release), p. 20 (A.4 Real-World Environment Setup) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 6 (3 Method), p. 4 (3 Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 6 (3 Method), p. 3 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Each entry represents success rate averaged across 20 episodes. | definition/direction/unit from same section | p. 22 (A.5.2 Full Results on Simulated Environments) |
| We find that VoxPoser can effectively synthesize robot trajectories for everyday manipulation tasks with a high average success rate. | definition/direction/unit from same section | p. 7 (3 Method) |
| 0.0% 17.5% 65.0% UI UA Composition 0.0% 25.0% 76.7% Table 2: Success rate in simulated domain. "SI" and "UI" are seen and unseen instructions. ... | definition/direction/unit from same section | p. 7 (3 Method) |
| However, we can learn an effective dynamics model with less than 3 minutes of online interactions by using these trajectories as exploration prior, leading ... | definition/direction/unit from same section | p. 8 (3 Method) |
| Errors by which are attributed to "specification error". | definition/direction/unit from same section | p. 8 (3 Method) |
| Figure 3: Visualization of composed 3D value maps and rollouts in real-world environments. The top row demonstrates where "entity of interest" is an object ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Note that in MPC settings, "movable" and the input value maps are functions that can be re-evaluated to reflect the latest environment observation. cm2index(cm,direction): ... | definition/direction/unit from same section | p. 19 (A.3 APIs for VoxPoser) |
| Besides exposing NumPy [16] and the Transforms3d library to the LLM, we provide the following environment APIs that LLMs can choose to invoke: detect(obj ... | definition/direction/unit from same section | p. 19 (A.3 APIs for VoxPoser) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| VoxPoser outperforms both baselines across 13 tasks from two categories on both seen and unseen tasks and maintains similar success rates. smoother trajectories but ... | comparison identity and matched condition | p. 7 (3 Method) |
| Seen instructions/attributes may appear in the prompt (or in the training data for supervised baselines). | comparison identity and matched condition | p. 7 (3 Method) |
| We compare to a variant of Code as Policies [75] as a baseline that uses an LLM with action primitives. | comparison identity and matched condition | p. 20 (A.4 Real-World Environment Setup) |
| In comparison, exploring without prior all exceed the maximum 12-hour limit. | comparison identity and matched condition | p. 8 (3 Method) |
| Figure 1: VOXPOSER extracts language-conditioned affordances and constraints from LLMs and grounds them to the perceptual space using VLMs, using a code interface and ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| For each task, we evaluate each method on two settings: without and with disturbances. | comparison identity and matched condition | p. 20 (A.4 Real-World Environment Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For baselines, we ablate the two components of VoxPoser, LLM and motion planner, by comparing to a variant of [75] that combines an LLM ... | component/input/data sensitivity | p. 7 (3 Method) |
| Figure 1: VOXPOSER extracts language-conditioned affordances and constraints from LLMs and grounds them to the perceptual space using VLMs, using a code interface and ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| We further compare to a variant of Code as Policies [75] that uses LLMs to parameterize a pre-defined list of simple primitives (e.g., move ... | component/input/data sensitivity | p. 7 (3 Method) |
| In comparison, exploring without prior all exceed the maximum 12-hour limit. | component/input/data sensitivity | p. 8 (3 Method) |
| Figure 4: Error breakdown of components. Vox- Poser significantly reduces specification error. each represented as a sequence of end-effector waypoints, that act as priors ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| For each task, we evaluate each method on two settings: without and with disturbances. | component/input/data sensitivity | p. 20 (A.4 Real-World Environment Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where each waypoint ... | VoxPoser outperforms both baselines across 13 tasks from two categories on both seen and unseen tasks and maintains similar success rates. smoother trajectories but ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (3 Method), p. 22 (A.5.2 Full Results on Simulated Environments), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method) |
| Primary metric/result | Each entry represents success rate averaged across 20 episodes. | numeric claim only at cited anchor | p. 22 (A.5.2 Full Results on Simulated Environments) |

- Numeric sentences retained from the body:
- **p. 7 / 3 Method - extractive body cue:** VoxPoser outperforms both baselines across 13 tasks from two categories on both seen and unseen tasks and maintains similar success rates. smoother trajectories but takes ...
- **p. 8 / 3 Method - extractive body cue:** Zero-Shot No Prior w/ Prior Task Success Success Time(s) Success Time(s) Door 6.7%±4.4% 58.3±4.4% TLE 88.3%±1.67%142.3±22.4 Window 3.3%±3.3% 36.7%±1.7% TLE 80.0%±2.9% 137.0±7.5 Fridge 18.3%±3.3%70.0%±2.9% TLE ...
- **p. 8 / 3 Method - extractive body cue:** TLE (time limit exceeded) means exceeding 12 hours.
- **p. 20 / A.4 Real-World Environment Setup - extractive body cue:** At the start of each rollout, both cameras start recording and return the real-time RGB-D observations at 20 Hz.
- **p. 21 / A.5.1 Tasks - extractive body cue:** We create a custom suite of 13 tasks shown in Table 4.
- **p. 22 / A.5.2 Full Results on Simulated Environments - extractive body cue:** Each entry represents success rate averaged across 20 episodes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 5 Conclusion, Limitations, & Future Works In this work, we present VOXPOSER, a general framework for extracting affordances and constraints, grounded in 3D perceptual ... | p. 8 (3 Method) |
| body limitation/failure cue | Despite compelling results, VoxPoser has several limitations. | p. 8 (3 Method) |
| body limitation/failure cue | This serves as a lighthearted example that language models can exhibit limitations similar to human reasoning. | p. 18 (A.2 Emergent Behavioral Capabilities) |
| body limitation/failure cue | VoxPoser performs everyday manipulation tasks with high success and is more robust to disturbances than the baseline using action primitives. | p. 7 (3 Method) |
| body limitation/failure cue | Due to fast replanning capabilities, it is also robust to external disturbances, such as moving targets/obstacles and pulling the drawer open after it has ... | p. 7 (3 Method) |
| body limitation/failure cue | Figure 2: Overview of VOXPOSER. Given the RGB-D observation of the environment and a language in- struction, LLMs generate code, which interacts with VLMs, ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Concretely, we aim to obtain a voxel value map Vt i = VoxPoser(ot, ℓi) by prompting an LLM and executing the code via a ... | p. 4 (3 Method) |
| Given the RGB-D observation of the environment and a language instruction, LLMs generate code, which interacts with VLMs, to produce a sequence of 3D ... | p. 4 (3 Method) |
| Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment observation at ... | p. 5 (3 Method) |
| 4 Experiments and Analysis We first discuss our implementation details. | p. 6 (3 Method) |
| The cost map used by the motion planner is computed as the negative of the weighted sum of normalized affordance and avoidance maps with ... | p. 6 (3 Method) |
| We further compare to a variant of Code as Policies [75] that uses LLMs to parameterize a pre-defined list of simple primitives (e.g., move ... | p. 7 (3 Method) |
| Results are reported over 3 runs different seeds. | p. 8 (3 Method) |
| We provide an open-sourced implementation of VoxPoser at github.com/huangwl18/VoxPoser based on RLBench [134], as its diversity of tasks and scenes best resembles our real-world ... | p. 18 (A.1 Code Release) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 3 Method - extractive body cue:** 5 Conclusion, Limitations, & Future Works In this work, we present VOXPOSER, a general framework for extracting affordances and constraints, grounded in 3D perceptual space, ...
- **p. 8 / 3 Method - extractive body cue:** Despite compelling results, VoxPoser has several limitations.
- **p. 18 / A.2 Emergent Behavioral Capabilities - extractive body cue:** This serves as a lighthearted example that language models can exhibit limitations similar to human reasoning.
- **p. 7 / 3 Method - extractive body cue:** VoxPoser performs everyday manipulation tasks with high success and is more robust to disturbances than the baseline using action primitives.
- **p. 7 / 3 Method - extractive body cue:** Due to fast replanning capabilities, it is also robust to external disturbances, such as moving targets/obstacles and pulling the drawer open after it has been ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of VOXPOSER. Given the RGB-D observation of the environment and a language in- struction, LLMs generate code, which interacts with VLMs, to ...

- **PDF anchors reviewed:** datasets p. 7 (3 Method), p. 18 (A.1 Code Release), p. 20 (A.4 Real-World Environment Setup), p. 18 (A.2 Emergent Behavioral Capabilities), p. 7 (3 Method), p. 21 (A.5 Simulated Environment Setup), metrics p. 22 (A.5.2 Full Results on Simulated Environments), p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 5 (Figure/Table caption), baselines p. 7 (3 Method), p. 7 (3 Method), p. 20 (A.4 Real-World Environment Setup), p. 8 (3 Method), p. 1 (Figure/Table caption), p. 20 (A.4 Real-World Environment Setup), results p. 7 (3 Method), p. 22 (A.5.2 Full Results on Simulated Environments), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
