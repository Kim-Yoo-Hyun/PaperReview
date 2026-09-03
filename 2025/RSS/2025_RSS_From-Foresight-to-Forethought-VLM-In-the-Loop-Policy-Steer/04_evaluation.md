# Evaluation - From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p076.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p076.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS)): V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec.

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTS - extractive body cue:** We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We collected 250 real-world trajectories per task, including both successful and failed rollouts from the base policy, along with additional 100 demonstrations used in base ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** In this task, the robot must pick up a fork from the table and place it inside a bowl.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** For each step trajectory snippet {(0},a3}£27 from the dataset, the encoder £4 processes the initial observation o} at timestep f, and the forward dynamies model ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** This task is considerably more challenging than the other two tasks for three reasons: 1) it requires Jonger-horizon planning to effectively navigate distinct phases; 2) ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** For our multi-modal imitative action generation «/ 04)- We use a Diffusion Policy [6] trained on 100 teleoperated demonstrations per task.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: Examples of Behavior Narrations Predicted by Each Approach. The top row displays the ground-truth robot ‘observations and the prompt used for querying VLMs. ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec. | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We collected 250 real-world trajectories per task, including both successful and failed rollouts from the base policy, along with additional 100 demonstrations used in ... | p. 6 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTS - extractive body cue:** We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We collected 250 real-world trajectories per task, including both successful and failed rollouts from the base policy, along with additional 100 demonstrations used in base ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** In this task, the robot must pick up a fork from the table and place it inside a bowl.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** For each step trajectory snippet {(0},a3}£27 from the dataset, the encoder £4 processes the initial observation o} at timestep f, and the forward dynamies model ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We present FOREWARN, an VLM-in-the-loop policy steering algorithm for multi-modal generative robot policies.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Training FOREWARN. In part A (Sec. IV-A), a Recurrent State Space Model (RSSM) is pretrained to leam good latent embeddings of the dynamics ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: Examples of Behavior Narrations Predicted by Each Approach. The top row displays the ground-truth robot ‘observations and the prompt used for querying VLMs. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Policy Steering: Fork Task. We visualize the steering process for the Fork task including two phases (Pick and Place). For each phase, we ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5: Generalization to Environmental Changes. For each task, we test our method against similar objects of different colors and sizes and also change the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures. | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Task/environment | We collected 250 real-world trajectories per task, including both successful and failed rollouts from the base policy, along with additional 100 demonstrations used in ... | reset, timeout, object/scene variation | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (1. InTRopucTION), p. 4 (1. InTRopucTION) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (1. InTRopucTION), p. 2 (1. InTRopucTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| This task is considerably more challenging than the other two tasks for three reasons: 1) it requires Jonger-horizon planning to effectively navigate distinct phases; ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| For our multi-modal imitative action generation «/ 04)- We use a Diffusion Policy [6] trained on 100 teleoperated demonstrations per task. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| We collected 250 real-world trajectories per task, including both successful and failed rollouts from the base policy, along with additional 100 demonstrations used in ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Fig. 3: Examples of Behavior Narrations Predicted by Each Approach. The top row displays the ground-truth robot ‘observations and the prompt used for querying ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 4: Policy Steering: Fork Task. We visualize the steering process for the Fork task including two phases (Pick and Place). For each phase, ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 3: Examples of Behavior Narrations Predicted by Each Approach. The top row displays the ground-truth robot ‘observations and the prompt used for querying ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| VLM Fine-tuning, We construct our VQA dataset for fine-tuning from the same offline dataset, Dyyy, used to train the world model. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| We fine-tune the model using the Low-Rank Adaptation (LoRA) technique [20], keeping both the encoder £ and the latent ‘dynamics model f,, frozen during ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Fig. 2: Training FOREWARN. In part A (Sec. IV-A), a Recurrent State Space Model (RSSM) is pretrained to leam good latent embeddings of the ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In Figure 4, we present examples of runtime policy steering using our approach for the Fork task and additional examples for Cup and Bag ... | V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Primary metric/result | We collected 250 real-world trajectories per task, including both successful and failed rollouts from the base policy, along with additional 100 demonstrations used in ... | numeric claim only at cited anchor | p. 6 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** We use 50 rollouts to evaluate the performance.
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** For FOREWARN, FOREWARN-Oracle and VLM- ‘Act, the mean and standard deviation are reported by running, 3 seeds for the finetuning experiments while VLM-Img and VLM-Img-Oracle, ...
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** For each method, we conduct 20 trials with

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures. | p. 5 (V. EXPERIMENTS) |
| body limitation/failure cue | We use this task to study how our framework performs when faced with harder-to-predict interaction outcomes and nuanced failures (e.g., crushing the chips inside ... | p. 5 (V. EXPERIMENTS) |
| body limitation/failure cue | (4) Classfier-Dyn-Latent, which is similar to VLM-DynLat-Category, but instead of relying ‘on a VLM, it directly takes the predicted latent embeddings Seq 88 input ... | p. 8 (B. Policy Steering for Open-World Alignment) |
| body limitation/failure cue | B2 revealed that our system's primary failures stem from the world model's imprecise "imagination", exacerbated by our limited training data. | p. 9 (VI. Limrrations) |
| body limitation/failure cue | Our experiments across diverse manipulation tasks confirm that FOREWARN not only provides interpretable and reliable failure detection, but also significantly enhances policy success rates ... | p. 9 (VI. Limrrations) |
| body limitation/failure cue | In contrast, the baselines either fail to interpret action outcomes effectively, resulting in unsafe behaviors, or experience severe performance degradation in novel task specifications. | p. 8 (B. Policy Steering for Open-World Alignment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We fine-tune the model using the Low-Rank Adaptation (LoRA) technique [20], keeping both the encoder £ and the latent ‘dynamics model f,, frozen during ... | p. 6 (V. EXPERIMENTS) |
| When deploying FOREWARN for run-time policy steering, we begin by sampling 100 action plans from the base policy and aggregating them into K = ... | p. 6 (V. EXPERIMENTS) |
| Inference time for each component in the system (averaged across 3 runs) shows that FOREWARN greatly reduces the time to generate behavior narrations from ... | p. 9 (B. Policy Steering for Open-World Alignment) |
| Our system queries the VLM twice to first generate behavior narrations and then select the best action plan, The overall inference time is 3.7 ... | p. 9 (B. Policy Steering for Open-World Alignment) |
| For each phase, we visualize the imagined T-step rollouts decoded from the world model for the 3 out of 6 action plans sampled from ... | p. 7 (B. Policy Steering for Open-World Alignment) |
| These results show that existing state-of-the-art VLMs struggle to decode finegrained motion details from video observations, underscoring the importance of fine-tuning for improved performance ... | p. 7 (A. From Action Rollouts to Behavior Narration) |
| For each method, we conduct 20 trials with | p. 8 (B. Policy Steering for Open-World Alignment) |
| randomly initialized task configurations and report the average success rate across these trials. | p. 8 (B. Policy Steering for Open-World Alignment) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / V. EXPERIMENTS - extractive body cue:** We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We use this task to study how our framework performs when faced with harder-to-predict interaction outcomes and nuanced failures (e.g., crushing the chips inside the ...
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** (4) Classfier-Dyn-Latent, which is similar to VLM-DynLat-Category, but instead of relying ‘on a VLM, it directly takes the predicted latent embeddings Seq 88 input and ...
- **p. 9 / VI. Limrrations - extractive body cue:** B2 revealed that our system's primary failures stem from the world model's imprecise "imagination", exacerbated by our limited training data.
- **p. 9 / VI. Limrrations - extractive body cue:** Our experiments across diverse manipulation tasks confirm that FOREWARN not only provides interpretable and reliable failure detection, but also significantly enhances policy success rates through ...
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** In contrast, the baselines either fail to interpret action outcomes effectively, resulting in unsafe behaviors, or experience severe performance degradation in novel task specifications.

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), metrics p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 7 (Figure/Table caption), results p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** In this task, the robot must pick up a fork from the table and place it inside a bowl. (p. 5, V. EXPERIMENTS).
- **Metric evidence:** V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec. (p. 5, V. EXPERIMENTS).
- **Baseline/ablation evidence:** V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec. (p. 5, V. EXPERIMENTS).
- **Failure/negative evidence:** However, at runtime, the policy exhibits a range of degradations, from complete task failures (such as the robot knocking down the cup during grasping, shown in the center of Figure ... (p. 1, 1. InTRopucTION).
