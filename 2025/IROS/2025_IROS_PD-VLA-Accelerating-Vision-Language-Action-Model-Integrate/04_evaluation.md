# Evaluation - PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.02310; PDF retrieval source: https://arxiv.org/pdf/2503.02310. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption)): Compared with prior stateof-the-art approaches, PD-VLA achieves the best average performance, attaining a 91.7% success rate on the most challenging LIBERO-Long benchmark.

## Evaluation Body Digest

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The CALVIN benchmark [35] is built on top of the PyBullet [46] simulator and involves a Franka Panda Robot arm that manipulates the scene.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We collect a small robotic dataset including 3 tasks: push the button, lift the block, and pour the water into the bowl.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Can PD-VLA be effectively deployed in real-world robotic systems?
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Each task contains 50 demonstrations and evaluates 10 episodes for success rates.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Additionally, considering the requirements of robotic tasks, we also report execution frequency (in Hertz, Hz).
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Method Spatial Object Goal Long Average Diffusion Policy [26] 78.3% 92.5% 68.3% 50.5% 72.4% Octo [6] 78.9% 85.7% 84.6% 51.1% 75.1% OpenVLA [37] 84.9% 88.4% ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Compared with prior stateof-the-art approaches, PD-VLA achieves the best average performance, attaining a 91.7% success rate on the most challenging LIBERO-Long benchmark.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We report the success rate and the average number of completed sequential tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared with prior stateof-the-art approaches, PD-VLA achieves the best average performance, attaining a 91.7% success rate on the most challenging LIBERO-Long benchmark. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | These components enable PD-VLA to improve 2.34 in success rates and realize 2.52× execution frequency compared to the fundamental model LLaVA-VLA. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method demonstrates competitive performance, with PD-VLA achieving significant improvements over the fundamental LLaVA-VLA model, further validating its effectiveness. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the success rate and the average number of completed sequential tasks. | p. 4 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Method Input Data Success Rate (%) Avg. len. | p. 5 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The CALVIN benchmark [35] is built on top of the PyBullet [46] simulator and involves a Franka Panda Robot arm that manipulates the scene.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We collect a small robotic dataset including 3 tasks: push the button, lift the block, and pour the water into the bowl.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Can PD-VLA be effectively deployed in real-world robotic systems?
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Each task contains 50 demonstrations and evaluates 10 episodes for success rates.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Additionally, considering the requirements of robotic tasks, we also report execution frequency (in Hertz, Hz).
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Method Spatial Object Goal Long Average Diffusion Policy [26] 78.3% 92.5% 68.3% 50.5% 72.4% Octo [6] 78.9% 85.7% 84.6% 51.1% 75.1% OpenVLA [37] 84.9% 88.4% ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Comparison between the proposed parallel decoding on the left and traditional autoregressive (AR) decoding on the right. Unlike AR decoding, which predicts action ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The network architecture of our PD-VLA with a chunk size of m. Given images, proprioception and language instructions, our method first tokenizes the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: Representative results of real-world experiments. The sequential images showcase the trajectories of a robotic arm successfully executing three tasks.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Comparison of minimum, average, and maximum inference speed (tokens per second) between AR decoding and parallel decoding with different decoding horizons n.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Real-World Setup. The left panel shows the mechanical arm and the right panel shows the camera used. task. This demonstrates its suitability for ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The CALVIN benchmark [35] is built on top of the PyBullet [46] simulator and involves a Franka Panda Robot arm that manipulates the scene. | embodiment, simulator version and control stack | p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | We collect a small robotic dataset including 3 tasks: push the button, lift the block, and pour the water into the bowl. | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Compared with prior stateof-the-art approaches, PD-VLA achieves the best average performance, attaining a 91.7% success rate on the most challenging LIBERO-Long benchmark. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| We report the success rate and the average number of completed sequential tasks. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Method Input Data Success Rate (%) Avg. len. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| We report the success rates for each subtask and the average completed length across all five tasks. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Each task contains 50 demonstrations and evaluates 10 episodes for success rates. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 1: Comparison between the proposed parallel decoding on the left and traditional autoregressive (AR) decoding on the right. Unlike AR decoding, which predicts ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We concentrate on several experiments to answer the following questions: Q1. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Fig. 3: Representative results of real-world experiments. The sequential images showcase the trajectories of a robotic arm successfully executing three tasks. | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For a comprehensive comparison, we include various baselines, such as the official MCIL [35] model and other prevalent models like HULC [36] and RT-1 ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| How does the effectiveness of PDVLA compare with baselines and other acceleration methods? | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| Here, we select 2 state-of-the-art training-free methods for VLM. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| These components enable PD-VLA to improve 2.34 in success rates and realize 2.52× execution frequency compared to the fundamental model LLaVA-VLA. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Compared with prior stateof-the-art approaches, PD-VLA achieves the best average performance, attaining a 91.7% success rate on the most challenging LIBERO-Long benchmark. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Fig. 1: Comparison between the proposed parallel decoding on the left and traditional autoregressive (AR) decoding on the right. Unlike AR decoding, which predicts ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation Study Table III presents a detailed summary of the ablation studies performed on two key components of our PD-VLA. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Is the coordination among different components effective? | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |
| 1/5 2/5 3/5 4/5 5/5 ABCD→D MCIL [35] RGB ALL 37.3 2.7 0.2 0.0 0.0 0.40 HULC [36] RGB ALL 89.2 70.1 54.8 42.0 ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Second, the ablation study of parallel decoding reveals the inefficiency in the inference process. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| In addition, we replace PD with other acceleration methods. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section, we introduce the details of our method PD-VLA. | Compared with prior stateof-the-art approaches, PD-VLA achieves the best average performance, attaining a 91.7% success rate on the most challenging LIBERO-Long benchmark. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Primary metric/result | These components enable PD-VLA to improve 2.34 in success rates and realize 2.52× execution frequency compared to the fundamental model LLaVA-VLA. | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** CALVIN consists of 34 tasks and 4 different environments (A, B, C and D).
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We report the success rate for each evaluation suite as well as the overall average, where each suite comprises 10 tasks, and each task is ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our fundamental model LLaVA-VLA is trained using 8 NVIDIA H100 GPUs over 1 epoch, which requires approximately 10 hours.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The 7token method performs better than the 16-token one because it aligns with the distribution of the single action, facilitating more efficient decoding in accordance ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** With the increasing decoding horizon, the number of fixed tokens increases accordingly, which contributes to the decoding speed improved from 41.48 to 52.84 tokens/second.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Notably, the redundant tokens when n = 16 make execution frequency even lower.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Notably, our PD-VLA does not incur extra training costs. | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | All tasks include distractors to validate the robustness of the model. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | For the task "pour water", LLaVA-VLA failed to complete this task, while PD-VLA has a 50% higher success rate. | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| However, the decoding speed is still limited, resulting in a longer single inference time. | p. 6 (IV. EXPERIMENTS) |
| Parallel decoding substantially increases the average decoding speed by 1.28×, thus the single inference time is reduced and satisfies the demand of high-frequency inference. | p. 6 (IV. EXPERIMENTS) |
| In this paper, we use vicuna-7bv1.5 [48] as the LLM backbone and clip-vit-large-patch14336 [49] as the vision encoder to build LLaVA-7b-v1.5 [32]. | p. 5 (IV. EXPERIMENTS) |
| However, extended action sequences consume longer single inference time, which impacts the continuity and effectiveness of the actions. | p. 3 (III. METHOD) |
| Then the images are processed through fencoder into the visual tokens hI. | p. 3 (III. METHOD) |
| In mathematics, it equals several Jacobi decodings with several Gauss-Seidel steps. | p. 4 (III. METHOD) |
| When n is less than the total action dimensions l, it decodes n action token in one iteration and then proceeds to the next ... | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Notably, our PD-VLA does not incur extra training costs.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** All tasks include distractors to validate the robustness of the model.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For the task "pour water", LLaVA-VLA failed to complete this task, while PD-VLA has a 50% higher success rate.

- **Evidence anchors reviewed:** datasets p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), baselines p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), results p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
