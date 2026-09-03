# Evaluation - Learning to Act Anywhere with Task-centric Latent Actions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p014.html; PDF retrieval source: https://arxiv.org/pdf/2505.06111. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room), p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Figure/Table caption)): Fig. 6: Oracle success rate on R2R in VLN-CE. With only a single-frame RGB input, UniVLA demonstrates performance on par with NaVid, a navigation model that incorporates the entirety of ...

## Evaluation Body Digest

- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** These benchmarks offer a set of languageguided navigation tasks and continuous environments for executing low-level actions in reconstructed photorealistic indoor scenes.
- **p. 6 / 1) Manipulation Benchmark on LIBERO - extractive body cue:** The LIBERO benchmark [48] comprises four task suites specifically designed to facilitate research on lifelong learning in robotic manipulation.
- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** In this experiment, we evaluate UniVLA on the VLN-CE benchmarks [41] to assess its performance on navigation tasks.
- **p. 5 / IV. EVALUATIONS - extractive body cue:** To demonstrate the performance of our proposed generalist policy, our evaluation framework assesses the capabilities of UniVLA across a diverse suite of benchmarks (including manipulation ...
- **p. 6 / 1) Manipulation Benchmark on LIBERO - extractive body cue:** We pretrain our full latent action model on manipulation data, navigation data and human videos data, which are a subset of Open X-Embodiment (OpenX) dataset ...
- **p. 8 / 2) Navigation Benchmark on Room2Room - extractive body cue:** (c) Novel Object: We replaced the object to be manipulated from a screwdriver to an unseen marker pen. encodes all historical observations, while UniVLA conditions ...
- **p. 5 / IV. EVALUATIONS - extractive body cue:** Additionally, we conduct latent action analysis to quantify the task-centric property, and perform ablation studies to explore critical design choices.
- **p. 8 / 2) Navigation Benchmark on Room2Room - extractive body cue:** Method Lightning Variation Visual Distractor Novel Object Average ↑ Succ.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EVALUATIONS (p. 5); 1) Manipulation Benchmark on LIBERO (p. 6); 2) Navigation Benchmark on Room2Room (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 6: Oracle success rate on R2R in VLN-CE. With only a single-frame RGB input, UniVLA demonstrates performance on par with NaVid, a navigation ... | p. 7 (Figure/Table caption) |
| 2) Navigation Benchmark on Room2Room | EMPIRICAL / SOURCE-REPORTED EVALUATION | UniVLA significantly outperforms Seq2Seq and CMA, increasing the oracle success rate from 8.10% to 47.1%. | p. 7 (2) Navigation Benchmark on Room2Room) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 10: Data efficiency. We present the success rate of UniVLA across varying dataset proportions (10%, 20%, 50%, and the full dataset). Our policy ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 4: Task setup on the LIBERO benchmark. TABLE I: Results on LIBERO benchmark across four evaluation suites. Our proposed UniVLA exhibits superior performance ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 9: Data scalability. UniVLA effectively expands its pretraining corpus by incorporating cross-embodiment data from OpenX and unlabeled human demonstrations, leading to continuously improved ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** These benchmarks offer a set of languageguided navigation tasks and continuous environments for executing low-level actions in reconstructed photorealistic indoor scenes.
- **p. 6 / 1) Manipulation Benchmark on LIBERO - extractive body cue:** The LIBERO benchmark [48] comprises four task suites specifically designed to facilitate research on lifelong learning in robotic manipulation.
- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** In this experiment, we evaluate UniVLA on the VLN-CE benchmarks [41] to assess its performance on navigation tasks.
- **p. 5 / IV. EVALUATIONS - extractive body cue:** To demonstrate the performance of our proposed generalist policy, our evaluation framework assesses the capabilities of UniVLA across a diverse suite of benchmarks (including manipulation ...
- **p. 6 / 1) Manipulation Benchmark on LIBERO - extractive body cue:** We pretrain our full latent action model on manipulation data, navigation data and human videos data, which are a subset of Open X-Embodiment (OpenX) dataset ...
- **p. 8 / 2) Navigation Benchmark on Room2Room - extractive body cue:** (c) Novel Object: We replaced the object to be manipulated from a screwdriver to an unseen marker pen. encodes all historical observations, while UniVLA conditions ...
- **p. 5 / IV. EVALUATIONS - extractive body cue:** Additionally, we conduct latent action analysis to quantify the task-centric property, and perform ablation studies to explore critical design choices.
- **p. 8 / 2) Navigation Benchmark on Room2Room - extractive body cue:** Method Lightning Variation Visual Distractor Novel Object Average ↑ Succ.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce UniVLA, a unified vision-language-action (VLA) framework that enables policy learning across different environments. By deriving task-centric latent actions in an unsupervised ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Task-centric latent action learning. We propose a two-stage training framework aimed at disentangling task-centric visual dynamics and changes from extraneous factors. In Stage ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Architecture of the generalist policy. Our policy architecture is founded on the Prismatic-7B Vision-Language Model (VLM) [37], which processes projected visual em- beddings ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Task setup on the LIBERO benchmark. TABLE I: Results on LIBERO benchmark across four evaluation suites. Our proposed UniVLA exhibits superior performance across ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Real-world robot experiments. We propose four different tasks: "Store the screwdriver", "Clean the cutting board", "Fold towel twice", and "Stack tower of hanoi", ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Oracle success rate on R2R in VLN-CE. With only a single-frame RGB input, UniVLA demonstrates performance on par with NaVid, a navigation model ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Setting on generalizability evaluations. We evaluate the generalizability of policies in 3 different settings. (a) Lightning Variation: We dimmed the ambient light and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Latent action analysis. We plot image pairs labeled with the same latent action from different sources of data and embodiments. Each group of ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These benchmarks offer a set of languageguided navigation tasks and continuous environments for executing low-level actions in reconstructed photorealistic indoor scenes. | embodiment, simulator version and control stack | p. 7 (2) Navigation Benchmark on Room2Room), p. 6 (1) Manipulation Benchmark on LIBERO) |
| Task/environment | The LIBERO benchmark [48] comprises four task suites specifically designed to facilitate research on lifelong learning in robotic manipulation. | reset, timeout, object/scene variation | p. 6 (1) Manipulation Benchmark on LIBERO), p. 7 (2) Navigation Benchmark on Room2Room) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 5: Real-world robot experiments. We propose four different tasks: "Store the screwdriver", "Clean the cutting board", "Fold towel twice", and "Stack tower of ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| We use the oracle success rate to evaluate navigation performance. | definition/direction/unit from same section | p. 7 (2) Navigation Benchmark on Room2Room) |
| Fig. 10: Data efficiency. We present the success rate of UniVLA across varying dataset proportions (10%, 20%, 50%, and the full dataset). Our policy ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| UniVLA demonstrates superior performance across all evaluated tasks, showcasing its exceptional ability to generalize from high-level semantic comprehension to low-level visual robustness. | definition/direction/unit from same section | p. 8 (2) Navigation Benchmark on Room2Room) |
| Score Diffusion Policy [17] 20.0 0.60 26.7 0.80 26.7 0.67 24.4 0.69 OpenVLA [39] 13.3 0.93 20.0 0.73 26.7 1.27 20.0 0.98 LAPA [87] ... | definition/direction/unit from same section | p. 8 (2) Navigation Benchmark on Room2Room) |
| To demonstrate the performance of our proposed generalist policy, our evaluation framework assesses the capabilities of UniVLA across a diverse suite of benchmarks (including ... | definition/direction/unit from same section | p. 5 (IV. EVALUATIONS) |
| Our experiments exclusively focus on supervised fine-tuning within the target task suite, evaluating the performance of various policies trained through behavioral cloning on successful ... | definition/direction/unit from same section | p. 6 (1) Manipulation Benchmark on LIBERO) |
| Fig. 2: Task-centric latent action learning. We propose a two-stage training framework aimed at disentangling task-centric visual dynamics and changes from extraneous factors. In ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 4: Task setup on the LIBERO benchmark. TABLE I: Results on LIBERO benchmark across four evaluation suites. Our proposed UniVLA exhibits superior performance ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| UniVLA significantly outperforms Seq2Seq and CMA, increasing the oracle success rate from 8.10% to 47.1%. | comparison identity and matched condition | p. 7 (2) Navigation Benchmark on Room2Room) |
| Fig. 5: Real-world robot experiments. We propose four different tasks: "Store the screwdriver", "Clean the cutting board", "Fold towel twice", and "Stack tower of ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Fig. 1: We introduce UniVLA, a unified vision-language-action (VLA) framework that enables policy learning across different environments. By deriving task-centric latent actions in an ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Fig. 10: Data efficiency. We present the success rate of UniVLA across varying dataset proportions (10%, 20%, 50%, and the full dataset). Our policy ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Additionally, we conduct latent action analysis to quantify the task-centric property, and perform ablation studies to explore critical design choices. | comparison identity and matched condition | p. 5 (IV. EVALUATIONS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 1: We introduce UniVLA, a unified vision-language-action (VLA) framework that enables policy learning across different environments. By deriving task-centric latent actions in an ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Additionally, we conduct latent action analysis to quantify the task-centric property, and perform ablation studies to explore critical design choices. | component/input/data sensitivity | p. 5 (IV. EVALUATIONS) |
| To ensure a fair comparison with UniVLA, we evaluate RGB-only methods that operate without depth or odometry data, directly predicting low-level actions within the ... | component/input/data sensitivity | p. 7 (2) Navigation Benchmark on Room2Room) |
| Fig. 9: Data scalability. UniVLA effectively expands its pretraining corpus by incorporating cross-embodiment data from OpenX and unlabeled human demonstrations, leading to continuously improved ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Fig. 10: Data efficiency. We present the success rate of UniVLA across varying dataset proportions (10%, 20%, 50%, and the full dataset). Our policy ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Fig. 2: Task-centric latent action learning. We propose a two-stage training framework aimed at disentangling task-centric visual dynamics and changes from extraneous factors. In ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are three-folds: • We propose UniVLA, a recipe towards generalist policy by planning in a unified, embodiment-agnostic action space, ... | Fig. 6: Oracle success rate on R2R in VLN-CE. With only a single-frame RGB input, UniVLA demonstrates performance on par with NaVid, a navigation ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room), p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Primary metric/result | UniVLA significantly outperforms Seq2Seq and CMA, increasing the oracle success rate from 8.10% to 47.1%. | numeric claim only at cited anchor | p. 7 (2) Navigation Benchmark on Room2Room) |

- Numeric sentences retained from the body:
- **p. 6 / 1) Manipulation Benchmark on LIBERO - extractive body cue:** 4, our experimental setup includes the following task suites, each consisting of 10 tasks with 50 human-teleoperated demonstrations per task:
- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** All methods are trained on the 10,819 samples in the R2R training split and evaluated on the 1,839 samples in the R2R val-unseen split.
- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** An episode is considered successful if the agent arrives within 3 meters of the goal in the VLN-CE.
- **p. 4 / III. METHODOLOGY - extractive body cue:** We set N = 4 for all our experiments.
- **p. 5 / III. METHODOLOGY - extractive body cue:** At inference time, one step of historical latent action (encoded as N = 4 tokens) is incorporated at each timestep, with the exception of the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | UniVLA demonstrates superior performance across all evaluated tasks, showcasing its exceptional ability to generalize from high-level semantic comprehension to low-level visual robustness. | p. 8 (2) Navigation Benchmark on Room2Room) |
| body limitation/failure cue | It achieves a 66.7% success rate under varying lighting conditions, surpassing Diffusion Policy (20.0%), OpenVLA (13.3%), and LAPA (26.7%), demonstrating robustness to environmental change. | p. 9 (3) Real-world Robot Deployment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At inference time, one step of historical latent action (encoded as N = 4 tokens) is incorporated at each timestep, with the exception of ... | p. 5 (III. METHODOLOGY) |
| We develop three steps to implement UniVLA: 1) (Sec. | p. 3 (III. METHODOLOGY) |
| The compact latent action must thus encode the transformation between observations to minimize prediction error. | p. 3 (III. METHODOLOGY) |
| Latent actions are projected into this vocabulary based on their indices in the action codebook. | p. 4 (III. METHODOLOGY) |
| Sending task instructions to the decoder provides high-level semantic guidance regarding the underlying actions. | p. 4 (III. METHODOLOGY) |
| III-A), they can be naturally decoded into action chunks [93]. | p. 5 (III. METHODOLOGY) |
| It uses a pretrained vision encoder to encode visual observations and a pretrained LLM to predict actions. | p. 7 (2) Navigation Benchmark on Room2Room) |
| We introduce several special tokens to tokenize navigation actions and finetune the model on the R2R training split. • NaVid [91] is a video-based ... | p. 7 (2) Navigation Benchmark on Room2Room) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 2) Navigation Benchmark on Room2Room - extractive body cue:** UniVLA demonstrates superior performance across all evaluated tasks, showcasing its exceptional ability to generalize from high-level semantic comprehension to low-level visual robustness.
- **p. 9 / 3) Real-world Robot Deployment - extractive body cue:** It achieves a 66.7% success rate under varying lighting conditions, surpassing Diffusion Policy (20.0%), OpenVLA (13.3%), and LAPA (26.7%), demonstrating robustness to environmental change.

- **Evidence anchors reviewed:** datasets p. 7 (2) Navigation Benchmark on Room2Room), p. 6 (1) Manipulation Benchmark on LIBERO), p. 7 (2) Navigation Benchmark on Room2Room), p. 5 (IV. EVALUATIONS), p. 6 (1) Manipulation Benchmark on LIBERO), p. 8 (2) Navigation Benchmark on Room2Room), metrics p. 7 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room), p. 10 (Figure/Table caption), p. 8 (2) Navigation Benchmark on Room2Room), p. 8 (2) Navigation Benchmark on Room2Room), p. 5 (IV. EVALUATIONS), baselines p. 6 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 10 (Figure/Table caption), p. 5 (IV. EVALUATIONS), results p. 7 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room), p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Fig. 4: Task setup on the LIBERO benchmark. TABLE I: Results on LIBERO benchmark across four evaluation suites. Our proposed UniVLA exhibits superior performance across all benchmarked tasks compared to ... (p. 6, Figure/Table caption).
- **Metric evidence:** Our experiments exclusively focus on supervised fine-tuning within the target task suite, evaluating the performance of various policies trained through behavioral cloning on successful task demonstrations. (p. 6, 1) Manipulation Benchmark on LIBERO).
- **Baseline/ablation evidence:** Additionally, we conduct latent action analysis to quantify the task-centric property, and perform ablation studies to explore critical design choices. (p. 5, IV. EVALUATIONS).
- **Failure/negative evidence:** While UniVLA advances generalist robotic policies, several limitations remain. (p. 11, VI. LIMITATIONS AND FUTURE WORK).
