# Evaluation - TD-MPC2: Scalable, Robust World Models for Continuous Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.16828; PDF retrieval source: https://arxiv.org/pdf/2310.16828. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 22 (Figure/Table caption), p. 23 (Figure/Table caption), p. 5 (Figure/Table caption), p. 23 (Figure/Table caption), p. 7 (4.1 RESULTS), p. 6 (Figure/Table caption)): Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable to existing methods on easy tasks, while outperforming other methods on hard ...

## Evaluation Body Digest

- **p. 8 / 4.1 RESULTS - extractive body cue:** However, TD-MPC2 can be readily applied to tasks with other input 120k environment steps corresponds to 20 episodes in DMControl and 100 episodes in Meta-World.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Pick YCB considers manipulation of all 74 objects from the YCB (Calli et al., 2015) dataset.
- **p. 7 / 4.1 RESULTS - extractive body cue:** (Left) Normalized score as a function of model size on the two 80-task and 30-task datasets.
- **p. 7 / 4.1 RESULTS - extractive body cue:** Approximate TD-MPC2 training cost on the 80-task dataset, reported in GPU days on a single NVIDIA GeForce RTX 3090 GPU.
- **p. 9 / 4.1 RESULTS - extractive body cue:** To demonstrate this, we replace the encoder of TD-MPC2 with a shallow convolutional encoder, and benchmark it against current state-of-the-art methods for visual RL on ...
- **p. 9 / 4.1 RESULTS - extractive body cue:** To accelerate research in this area, we are releasing 300+ TD-MPC2 models, including 12 multitask models, as well as datasets and code, and we are ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Success rate (%) as a function of environment steps on 5 object manipulation tasks from ManiSkill2.
- **p. 8 / 4.1 RESULTS - extractive body cue:** Episode return as a function of environment steps on 10 image-based DMControl tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 5); 4.1 RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable to existing methods on easy tasks, ... | p. 22 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 16. Single-task MyoSuite results. Success rate (%) as a function of environment steps. This task domain includes high-dimensional contact-rich musculoskeletal motor control (A ... | p. 23 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4. Single-task RL. Episode return (DMControl) and success rate (others) as a function of environment steps across 104 continuous control tasks spanning 4 ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 14. Single-task ManiSkill2 results. Success rate (%) as a function of environment steps on 5 object manipulation tasks from ManiSkill2. Pick YCB is ... | p. 23 (Figure/Table caption) |
| 4.1 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | To summarize agent performance with a single metric, we produce a normalized score that is an average of all individual task success rates (Meta-World) ... | p. 7 (4.1 RESULTS) |

## Dataset / Benchmark Role

- **p. 8 / 4.1 RESULTS - extractive body cue:** However, TD-MPC2 can be readily applied to tasks with other input 120k environment steps corresponds to 20 episodes in DMControl and 100 episodes in Meta-World.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Pick YCB considers manipulation of all 74 objects from the YCB (Calli et al., 2015) dataset.
- **p. 7 / 4.1 RESULTS - extractive body cue:** (Left) Normalized score as a function of model size on the two 80-task and 30-task datasets.
- **p. 7 / 4.1 RESULTS - extractive body cue:** Approximate TD-MPC2 training cost on the 80-task dataset, reported in GPU days on a single NVIDIA GeForce RTX 3090 GPU.
- **p. 9 / 4.1 RESULTS - extractive body cue:** To demonstrate this, we replace the encoder of TD-MPC2 with a shallow convolutional encoder, and benchmark it against current state-of-the-art methods for visual RL on ...
- **p. 9 / 4.1 RESULTS - extractive body cue:** To accelerate research in this area, we are releasing 300+ TD-MPC2 models, including 12 multitask models, as well as datasets and code, and we are ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Success rate (%) as a function of environment steps on 5 object manipulation tasks from ManiSkill2.
- **p. 8 / 4.1 RESULTS - extractive body cue:** Episode return as a function of environment steps on 10 image-based DMControl tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview. TD-MPC2 compares favorably to existing model-free and model-based RL methods across 104 continuous control tasks spanning multiple domains, with a single set ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Tasks. TD-MPC2 performs 104 diverse tasks from (left to right) DMControl (Tassa et al., 2018), Meta-World (Yu et al., 2019), ManiSkill2 (Gu et ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. The TD-MPC2 architecture. Observations s are encoded into their (normalized) latent representation z. The model then recurrently predicts actions ˆa, rewards ˆr, and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Single-task RL. Episode return (DMControl) and success rate (others) as a function of environment steps across 104 continuous control tasks spanning 4 diverse ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. High-dimensional locomotion. Episode return as a function of environment steps in Humanoid (A ∈R21) and Dog (A ∈R38) locomotion tasks from DMControl. SAC ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Object manipulation. Success rate (%) as a function of environment steps on 5 object manipulation tasks from ManiSkill2. Pick YCB considers manipulation of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Massively multi-task world models. (Left) Normalized score as a function of model size on the two 80-task and 30-task datasets. TD-MPC2 capabilities scale ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Training cost. Ap- proximate TD-MPC2 training cost on the 80-task dataset, reported in GPU days on a single NVIDIA GeForce RTX 3090 GPU. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, TD-MPC2 can be readily applied to tasks with other input 120k environment steps corresponds to 20 episodes in DMControl and 100 episodes in ... | embodiment, simulator version and control stack | p. 8 (4.1 RESULTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | Pick YCB considers manipulation of all 74 objects from the YCB (Calli et al., 2015) dataset. | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 7 (4.1 RESULTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To summarize agent performance with a single metric, we produce a normalized score that is an average of all individual task success rates (Meta-World) ... | definition/direction/unit from same section | p. 7 (4.1 RESULTS) |
| Figure 4. Single-task RL. Episode return (DMControl) and success rate (others) as a function of environment steps across 104 continuous control tasks spanning 4 ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Success rate (%) as a function of environment steps on 5 object manipulation tasks from ManiSkill2. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable to existing methods on easy tasks, ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Figure 16. Single-task MyoSuite results. Success rate (%) as a function of environment steps. This task domain includes high-dimensional contact-rich musculoskeletal motor control (A ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Figure 17. Few-shot learning. Normalized episode return (DMControl) and success rate (Meta- World) as a function of environment steps while finetuning a 19M parameter ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Tasks include high-dimensional state and action spaces (up to A ∈R39), sparse rewards, multi-object manipulation, physiologically accurate musculoskeletal motor control, complex locomotion (e.g. | definition/direction/unit from same section | p. 5 (4 EXPERIMENTS) |
| Lastly, we want to remark that, while TD-MPC2 relies on rewards for task learning, it is useful to adopt a generalized notion of reward ... | definition/direction/unit from same section | p. 9 (4.1 RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| TD-MPC2 outperforms baselines by a large margin on these tasks, despite using the same hyperparameters across all tasks. | comparison identity and matched condition | p. 6 (4.1 RESULTS) |
| Our primary baselines represent the state-of-the-art in data-efficient RL, and include (1) Soft Actor-Critic (SAC) (Haarnoja et al., 2018), a model-free actor-critic algorithm based ... | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| TD-MPC2 performs comparably to the two best baselines, DrQ-v2 and DreamerV3, without any changes to hyperparameters. | comparison identity and matched condition | p. 9 (4.1 RESULTS) |
| Due to our careful design of the TD-MPC2 algorithm, scaling up is straightforward: to improve rate of convergence we use a 4× larger batch ... | comparison identity and matched condition | p. 7 (4.1 RESULTS) |
| TD-MPC2 is comparable to state-of-the-art. | comparison identity and matched condition | p. 8 (4.1 RESULTS) |
| To demonstrate this, we replace the encoder of TD-MPC2 with a shallow convolutional encoder, and benchmark it against current state-of-the-art methods for visual RL ... | comparison identity and matched condition | p. 9 (4.1 RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our ablations highlight the relative importance of each design choice; red is the default formulation of TD-MPC2. | component/input/data sensitivity | p. 8 (4.1 RESULTS) |
| Our main ablations, shown in Figure 9, are conducted on three of the most difficult online RL tasks, as well as largescale multitask training ... | component/input/data sensitivity | p. 8 (4.1 RESULTS) |
| TD-MPC2 performs comparably to the two best baselines, DrQ-v2 and DreamerV3, without any changes to hyperparameters. | component/input/data sensitivity | p. 9 (4.1 RESULTS) |
| Figure 3. The TD-MPC2 architecture. Observations s are encoded into their (normalized) latent representation z. The model then recurrently predicts actions ˆa, rewards ˆr, ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Table 5. MyoSuite. We consider a total of 10 continuous control tasks from the MyoSuite domain. The MyoSuite benchmark is designed for high-dimensional physiologically ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |
| Figure 18. Normalized task embeddings. Normalized score of 19M parameter multitask (80 tasks) TD-MPC2 agents, with and without normalized task embeddings e as described ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we present TDMPC2: a significant step towards achieving this goal. | Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable to existing methods on easy tasks, ... | PDF body cue; verify exact table/figure and matched conditions | p. 22 (Figure/Table caption), p. 23 (Figure/Table caption), p. 5 (Figure/Table caption), p. 23 (Figure/Table caption), p. 7 (4.1 RESULTS), p. 6 (Figure/Table caption) |
| Primary metric/result | Figure 16. Single-task MyoSuite results. Success rate (%) as a function of environment steps. This task domain includes high-dimensional contact-rich musculoskeletal motor control (A ... | numeric claim only at cited anchor | p. 23 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** We evaluate TD-MPC2 across a total of 104 diverse continuous control tasks spanning 4 task domains: DMControl (Tassa et al., 2018), Meta-World (Yu et al., ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Success rate (%) as a function of environment steps on 5 object manipulation tasks from ManiSkill2.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Pick YCB considers manipulation of all 74 objects from the YCB (Calli et al., 2015) dataset.
- **p. 7 / 4.1 RESULTS - extractive body cue:** (Right) T-SNE (van der Maaten & Hinton, 2008) visualization of task embeddings learned by a TD-MPC2 agent trained on 80 tasks from DMControl and Meta-World.
- **p. 7 / 4.1 RESULTS - extractive body cue:** Approximate TD-MPC2 training cost on the 80-task dataset, reported in GPU days on a single NVIDIA GeForce RTX 3090 GPU.
- **p. 7 / 4.1 RESULTS - extractive body cue:** 0 20 40 60 Normalized score 24.0 47.0 Finetuning 10 tasks From scratch Finetuned Figure 8.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While we are excited by the potential of generalist world models, several challenges remain: (i) misspecification of task rewards can lead to unintended outcomes ... | p. 9 (4.1 RESULTS) |
| body limitation/failure cue | Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable to existing methods on easy tasks, ... | p. 22 (Figure/Table caption) |
| body limitation/failure cue | Notably, performance does not appear to have saturated for our largest models (317M parameters) on either dataset, and we can thus expect results to ... | p. 7 (4.1 RESULTS) |
| body limitation/failure cue | Figure 2. Tasks. TD-MPC2 performs 104 diverse tasks from (left to right) DMControl (Tassa et al., 2018), Meta-World (Yu et al., 2019), ManiSkill2 (Gu ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | While our work mainly focuses on the scaling and robustness of world models, we also explore the efficacy of finetuning pretrained world models for ... | p. 7 (4.1 RESULTS) |
| body limitation/failure cue | We observe that all of our proposed improvements contribute meaningfully to the robustness and strong performance of TD-MPC2 in both single-task RL and multi-task ... | p. 8 (4.1 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Due to our careful design of the TD-MPC2 algorithm, scaling up is straightforward: to improve rate of convergence we use a 4× larger batch ... | p. 7 (4.1 RESULTS) |
| (Curves) Normalized score as a function of environment steps, averaged across three of the most difficult tasks: Dog Run, Humanoid Walk (DMControl), and Pick ... | p. 8 (4.1 RESULTS) |
| Historically, RL algorithms have been notoriously sensitive to architecture, hyperparameters, characteristics of the task, and even random seed (Henderson et al., 2018), with no ... | p. 9 (4.1 RESULTS) |
| Additionally, it is worth noting that both SAC and TD-MPC use a larger batch size of 512, while 256 is sufficient for stable learning ... | p. 6 (4 EXPERIMENTS) |
| Success rate (%) as a function of environment steps on 5 object manipulation tasks from ManiSkill2. | p. 6 (4 EXPERIMENTS) |
| Params (M) GPU days Score 1 3.7 16.0 5 4.2 49.5 19 5.3 57.1 48 12 68.0 317 33 70.6 Massively multitask world models. | p. 7 (4.1 RESULTS) |
| Mean and 95% CIs over 3 random seeds. | p. 8 (4.1 RESULTS) |
| TD-MPC2 performs comparably to the two best baselines, DrQ-v2 and DreamerV3, without any changes to hyperparameters. | p. 9 (4.1 RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4.1 RESULTS - extractive body cue:** While we are excited by the potential of generalist world models, several challenges remain: (i) misspecification of task rewards can lead to unintended outcomes (Clark ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable to existing methods on easy tasks, while ...
- **p. 7 / 4.1 RESULTS - extractive body cue:** Notably, performance does not appear to have saturated for our largest models (317M parameters) on either dataset, and we can thus expect results to continue ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Tasks. TD-MPC2 performs 104 diverse tasks from (left to right) DMControl (Tassa et al., 2018), Meta-World (Yu et al., 2019), ManiSkill2 (Gu et ...
- **p. 7 / 4.1 RESULTS - extractive body cue:** While our work mainly focuses on the scaling and robustness of world models, we also explore the efficacy of finetuning pretrained world models for few-shot ...
- **p. 8 / 4.1 RESULTS - extractive body cue:** We observe that all of our proposed improvements contribute meaningfully to the robustness and strong performance of TD-MPC2 in both single-task RL and multi-task RL.

- **Evidence anchors reviewed:** datasets p. 8 (4.1 RESULTS), p. 6 (4 EXPERIMENTS), p. 7 (4.1 RESULTS), p. 7 (4.1 RESULTS), p. 9 (4.1 RESULTS), p. 9 (4.1 RESULTS), metrics p. 7 (4.1 RESULTS), p. 5 (Figure/Table caption), p. 6 (4 EXPERIMENTS), p. 22 (Figure/Table caption), p. 23 (Figure/Table caption), p. 24 (Figure/Table caption), baselines p. 6 (4.1 RESULTS), p. 6 (4 EXPERIMENTS), p. 9 (4.1 RESULTS), p. 7 (4.1 RESULTS), p. 8 (4.1 RESULTS), p. 9 (4.1 RESULTS), results p. 22 (Figure/Table caption), p. 23 (Figure/Table caption), p. 5 (Figure/Table caption), p. 23 (Figure/Table caption), p. 7 (4.1 RESULTS), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 16. Single-task MyoSuite results. Success rate (%) as a function of environment steps. This task domain includes high-dimensional contact-rich musculoskeletal motor control (A ∈R39) with a physiologically accurate robot ... (p. 23, Figure/Table caption).
- **Metric evidence:** To summarize agent performance with a single metric, we produce a normalized score that is an average of all individual task success rates (Meta-World) and episode returns normalized to the ... (p. 7, 4.1 RESULTS).
- **Baseline/ablation evidence:** TD-MPC2 outperforms baselines by a large margin on these tasks, despite using the same hyperparameters across all tasks. (p. 6, 4.1 RESULTS).
- **Failure/negative evidence:** While we are excited by the potential of generalist world models, several challenges remain: (i) misspecification of task rewards can lead to unintended outcomes (Clark & Amodei, 2016) that may ... (p. 9, 4.1 RESULTS).
