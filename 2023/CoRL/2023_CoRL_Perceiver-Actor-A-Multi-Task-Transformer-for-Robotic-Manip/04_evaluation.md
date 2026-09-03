# Evaluation - Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.05451; PDF retrieval source: https://arxiv.org/pdf/2209.05451. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 8 (4 Results), p. 27 (Figure/Table caption), p. 6 (4 Results), p. 7 (4 Results)): Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. ...

## Evaluation Body Digest

- **p. 6 / 4 Results - extractive body cue:** All keyframes from an episode have the same language goal, which is constructed from templates (but human-annotated for real-world tasks).
- **p. 6 / 4 Results - extractive body cue:** We report average success rates on 25 evaluation episodes per task (25 × 18 = 450 total episodes) for agents trained with n = 10, ...
- **p. 7 / 4 Results - extractive body cue:** Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task.
- **p. 8 / 4 Results - extractive body cue:** The left two are simulated tasks, and the right two are real-world tasks.
- **p. 8 / 4 Results - extractive body cue:** But overall, we are excited about scaling up robot learning with Transformers by focusing on diverse rather than narrow multi-task data for robotic manipulation.
- **p. 7 / 4 Results - extractive body cue:** For a number of tasks, C2FARM-BC actually performs worse with more demonstrations, likely due to insufficient capacity.
- **p. 7 / 4 Results - extractive body cue:** Success rate of PERACT after ablating key components.
- **p. 8 / 4 Results - extractive body cue:** Success rates (mean %) of a multitask model trained an evaluated 7 realworld tasks (see Figure 1).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Results (p. 6); C Evaluation Workflow (p. 21).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5. Success rates (mean %) of multi-task and single-task PERACT agents trained with 100 demos and evaluated on 25 episodes. In Table 1, ... | p. 24 (Figure/Table caption) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Similar to the simulation results, we find that PERACT is able to achieve > 65% success on simple short-horizon tasks like pressing hand-sanitizers from ... | p. 8 (4 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 11. Perturbation Tests. Results from a multi-task PERACT agent trained on a single drawer and evaluated on several instances perturbed drawers. Each perturbation ... | p. 27 (Figure/Table caption) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | [14] that has achieved state-of-the-art results on RLBench tasks. | p. 6 (4 Results) |

## Dataset / Benchmark Role

- **p. 6 / 4 Results - extractive body cue:** All keyframes from an episode have the same language goal, which is constructed from templates (but human-annotated for real-world tasks).
- **p. 6 / 4 Results - extractive body cue:** We report average success rates on 25 evaluation episodes per task (25 × 18 = 450 total episodes) for agents trained with n = 10, ...
- **p. 7 / 4 Results - extractive body cue:** Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task.
- **p. 8 / 4 Results - extractive body cue:** The left two are simulated tasks, and the right two are real-world tasks.
- **p. 8 / 4 Results - extractive body cue:** But overall, we are excited about scaling up robot learning with Transformers by focusing on diverse rather than narrow multi-task data for robotic manipulation.
- **p. 7 / 4 Results - extractive body cue:** For a number of tasks, C2FARM-BC actually performs worse with more demonstrations, likely due to insufficient capacity.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Language-Conditioned Manipulation Tasks: PERACT is a language-conditioned multi-task agent capable of imitating a wide range of 6-DoF manipulation tasks. We conduct experiments on ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. PERACT Overview. PERACT is a language-conditioned behavior-cloning agent trained with supervised learning to detect actions. PERACT takes as input a language goal and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Ablation Experiments. Success rate of PER- ACT after ablating key components. Ablations. Table 1 reports PERACT w/o Lang, an agent without any language ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Global vs. Local Receptive Field Ex- periments. Success rates of PERACT against various C2FARM-BC [14] baselines To further investigate our Transformer agent's global ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Q-Prediction Examples: Qualitative examples of translation Q-Predictions from PERACT along with expert actions, highlighted with dotted-circles. The left two are simulated tasks, and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Success rates (mean %) of a multi- task model trained an evaluated 7 real- world tasks (see Figure 1). We also validated our ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 3. Language-Conditioned Tasks in RLBench [15]. Setup. Our simulated experiments are set in RLBench [15]. We select 18 out of 100 tasks that involve ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | All keyframes from an episode have the same language goal, which is constructed from templates (but human-annotated for real-world tasks). | embodiment, simulator version and control stack | p. 6 (4 Results), p. 6 (4 Results) |
| Task/environment | We report average success rates on 25 evaluation episodes per task (25 × 18 = 450 total episodes) for agents trained with n = ... | reset, timeout, object/scene variation | p. 6 (4 Results), p. 7 (4 Results) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (Abstract), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 5. Success rates (mean %) of multi-task and single-task PERACT agents trained with 100 demos and evaluated on 25 episodes. In Table 1, ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Success rate of PERACT after ablating key components. | definition/direction/unit from same section | p. 7 (4 Results) |
| Success rates (mean %) of a multitask model trained an evaluated 7 realworld tasks (see Figure 1). | definition/direction/unit from same section | p. 8 (4 Results) |
| Table 4. Sensitivity Analysis. Success rates (mean %) of various PERACT agents trained with 100 demonstrations per task. We investigate three factors that affect ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Evaluations are scored either 0 for failures or 100 for complete successes. | definition/direction/unit from same section | p. 6 (4 Results) |
| With insufficient demonstrations, Image-BC has near zero performance on most tasks. | definition/direction/unit from same section | p. 6 (4 Results) |
| See the supplementary video for qualitative results that showcase the diversity of tasks and robustness to scene changes. | definition/direction/unit from same section | p. 8 (4 Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| PERACT outperforms C2FARM-BC [14], the most competitive baseline, with an average improvement of 1.33× with 10 demos and 2.83× with 100 demos. | comparison identity and matched condition | p. 7 (4 Results) |
| [14] that has achieved state-of-the-art results on RLBench tasks. | comparison identity and matched condition | p. 6 (4 Results) |
| During evaluation, an agent keeps taking actions until an oracle indicates task-completion or reaches a maximum of 25 steps. | comparison identity and matched condition | p. 6 (4 Results) |
| Success rates of PERACT against various C2FARM-BC [14] baselines To further investigate our Transformer agent's global receptive field, we conduct additional experiments on the ... | comparison identity and matched condition | p. 7 (4 Results) |
| Other issues included the agent exploiting biases in the dataset like in prior work [16]. | comparison identity and matched condition | p. 8 (4 Results) |
| And [64] indicates a single level of a 643 voxel grid without the coarse-to-fine-grain scheme. | comparison identity and matched condition | p. 8 (4 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 3. Ablation Experiments. Success rate of PER- ACT after ablating key components. Ablations. Table 1 reports PERACT w/o Lang, an agent without any ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| The focus here is to evaluate the performance of a single multi-task agent trained on all tasks and variants. | component/input/data sensitivity | p. 6 (4 Results) |
| These variants are randomly sampled during data generation, but kept consistent during evaluations for one-to-one comparisons. | component/input/data sensitivity | p. 6 (4 Results) |
| Since additional training demonstrations include additional task variants to optimize for, they might end up hurting performance. | component/input/data sensitivity | p. 7 (4 Results) |
| This could be addressed by scaling up expert data with more diverse tasks and task variants. | component/input/data sensitivity | p. 8 (4 Results) |
| And [64] indicates a single level of a 643 voxel grid without the coarse-to-fine-grain scheme. | component/input/data sensitivity | p. 8 (4 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric ... | Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 8 (4 Results), p. 27 (Figure/Table caption), p. 6 (4 Results), p. 7 (4 Results) |
| Primary metric/result | Table 5. Success rates (mean %) of multi-task and single-task PERACT agents trained with 100 demos and evaluated on 25 episodes. In Table 1, ... | numeric claim only at cited anchor | p. 24 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Results - extractive body cue:** There are a total of 249 variations across 18 tasks, and the number of extracted keyframes range from 2-17.
- **p. 6 / 4 Results - extractive body cue:** Each multi-task agent is evaluated independently on all 18 tasks.
- **p. 6 / 4 Results - extractive body cue:** We report average success rates on 25 evaluation episodes per task (25 × 18 = 450 total episodes) for agents trained with n = 10, ...
- **p. 6 / 4 Results - extractive body cue:** During evaluation, an agent keeps taking actions until an oracle indicates task-completion or reaches a maximum of 25 steps.
- **p. 6 / 4 Results - extractive body cue:** 4.2 Simulation Results Table 1 reports success rates of multi-task agents trained on all 18 tasks.
- **p. 7 / 4 Results - extractive body cue:** Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Evaluations are scored either 0 for failures or 100 for complete successes. | p. 6 (4 Results) |
| body limitation/failure cue | Each evaluation episode is scored either a 0 for failure or 100 for succces. | p. 7 (4 Results) |
| body limitation/failure cue | These are very high-precision tasks where being off by a few centimeters or degrees could lead to unrecoverable failures. | p. 7 (4 Results) |
| body limitation/failure cue | The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states. | p. 8 (4 Results) |
| body limitation/failure cue | Figure 2. PERACT Overview. PERACT is a language-conditioned behavior-cloning agent trained with supervised learning to detect actions. PERACT takes as input a language goal ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | See Appendix L for an extended discussion on PERACT's limitations. | p. 8 (4 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Transformers [2] have become prevalent in natural language processing and computer vision. | p. 1 (1 Introduction) |
| PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action". | p. 1 (Abstract) |
| The code and pre-trained models will be made available at peract.github.io. | p. 2 (1 Introduction) |
| But in PERACT, we use a Perceiver2 Transformer [1] to encode very high-dimensional input of up to 1 million voxels with only a small ... | p. 2 (1 Introduction) |
| We also study both CNN and ViT vision encoders. | p. 6 (4 Results) |
| During evaluation, an agent keeps taking actions until an oracle indicates task-completion or reaches a maximum of 25 steps. | p. 6 (4 Results) |
| 0 10000 20000 30000 40000 Training Steps 0 20 40 60 80 100 Success Rate PerAct PerAct w/o skip PerAct w/o Perceiver PerAct w/ ... | p. 7 (4 Results) |
| Local Receptive Fields 0 10000 20000 30000 40000 Training Steps 0 20 40 60 80 100 Success Rate PerAct C2FARM-BC [16,16] C2FARM-BC [32,32] C2FARM-BC ... | p. 7 (4 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4 Results - extractive body cue:** Evaluations are scored either 0 for failures or 100 for complete successes.
- **p. 7 / 4 Results - extractive body cue:** Each evaluation episode is scored either a 0 for failure or 100 for succces.
- **p. 7 / 4 Results - extractive body cue:** These are very high-precision tasks where being off by a few centimeters or degrees could lead to unrecoverable failures.
- **p. 8 / 4 Results - extractive body cue:** The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. PERACT Overview. PERACT is a language-conditioned behavior-cloning agent trained with supervised learning to detect actions. PERACT takes as input a language goal and ...
- **p. 8 / 4 Results - extractive body cue:** See Appendix L for an extended discussion on PERACT's limitations.

- **Evidence anchors reviewed:** datasets p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 8 (4 Results), p. 7 (4 Results), metrics p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 7 (4 Results), p. 8 (4 Results), p. 23 (Figure/Table caption), p. 6 (4 Results), baselines p. 7 (4 Results), p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 8 (4 Results), results p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 8 (4 Results), p. 27 (Figure/Table caption), p. 6 (4 Results), p. 7 (4 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. ... (p. 7, Figure/Table caption).
- **Metric evidence:** Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. ... (p. 7, Figure/Table caption).
- **Baseline/ablation evidence:** PERACT outperforms C2FARM-BC [14], the most competitive baseline, with an average improvement of 1.33× with 10 demos and 2.83× with 100 demos. (p. 7, 4 Results).
- **Failure/negative evidence:** The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states. (p. 8, 4 Results).
