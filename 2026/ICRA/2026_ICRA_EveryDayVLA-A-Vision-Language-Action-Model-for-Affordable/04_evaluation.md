# Evaluation - EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2511.05397. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS)): For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared to continuous-action baselines.

## Evaluation Body Digest

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Baselines On the LIBERO simulation benchmark, we report success rates across all four task suites, comparing against Diffusion Policy [3], Octo [5], DiT Policy [48], ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Our dataset was captured across multiple tabletop environments and span a diverse task set: pick1 - Base 2 - Shoulder 3 - Elbow 4 - ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Real-world evaluation results on in-distribution tasks, including picking a block, ball and rock.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our model is able to beat state-of-the art models on tasks and environments present in the training set by 49% on average.
- **p. 6 / V. RESULTS - extractive body cue:** Although our model performs similarly to [19] on picking and placing blocks (most common task in the collected dataset), the latter struggles when placing to ...
- **p. 6 / V. RESULTS - extractive body cue:** Generalization results On generalization and robustness evaluation of unseen tasks, environments and conditions (Table IV), our model does the best.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared to ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our experiments show better success rates on almost every single task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4); V. RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared ... | p. 4 (IV. EXPERIMENTS) |
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results on Real-World Tests In real-world, in-distribution pick-and-place experiments, EverydayVLA outperforms other methods by an average of 49% in success rate across blocks, balls, ... | p. 6 (V. RESULTS) |
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our ensembler shows a 1.6% improvement in success rate compared to the next best method. | p. 6 (V. RESULTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Baselines On the LIBERO simulation benchmark, we report success rates across all four task suites, comparing against Diffusion Policy [3], Octo [5], DiT Policy ... | p. 4 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our experiments show better success rates on almost every single task. | p. 5 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Baselines On the LIBERO simulation benchmark, we report success rates across all four task suites, comparing against Diffusion Policy [3], Octo [5], DiT Policy [48], ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Our dataset was captured across multiple tabletop environments and span a diverse task set: pick1 - Base 2 - Shoulder 3 - Elbow 4 - ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Real-world evaluation results on in-distribution tasks, including picking a block, ball and rock.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our model is able to beat state-of-the art models on tasks and environments present in the training set by 49% on average.
- **p. 6 / V. RESULTS - extractive body cue:** Although our model performs similarly to [19] on picking and placing blocks (most common task in the collected dataset), the latter struggles when placing to ...
- **p. 6 / V. RESULTS - extractive body cue:** Generalization results On generalization and robustness evaluation of unseen tasks, environments and conditions (Table IV), our model does the best.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. EveryDayVLA system. Top: EveryDayVLA finetunes a VLA for a low-cost manipulator to generate continuous and discrete actions, which are passed to an adaptive ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. EveryDayVLA architecture. The VLA takes as input an image and natural language instruction and these are tokenized via the vision and language encoders, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. EveryDayVLA hardware. The robot consists of 7 joints, including a base and claw gripper as the end-effector. In sum, the hardware costs $311.98, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Real-world evaluation results on in-distribution tasks, including picking a block, ball and rock. Our model is able to beat state-of-the art models on ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5. Static and dynamic distractors. Top: We benchmark our model with static distractors, and a cluttered scene where we add different objects, and vary ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Baselines On the LIBERO simulation benchmark, we report success rates across all four task suites, comparing against Diffusion Policy [3], Octo [5], DiT Policy ... | embodiment, simulator version and control stack | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Task/environment | Our dataset was captured across multiple tabletop environments and span a diverse task set: pick1 - Base 2 - Shoulder 3 - Elbow 4 ... | reset, timeout, object/scene variation | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 4 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Baselines On the LIBERO simulation benchmark, we report success rates across all four task suites, comparing against Diffusion Policy [3], Octo [5], DiT Policy ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Our experiments show better success rates on almost every single task. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Our ensembler shows a 1.6% improvement in success rate compared to the next best method. | definition/direction/unit from same section | p. 6 (V. RESULTS) |
| Results on Real-World Tests In real-world, in-distribution pick-and-place experiments, EverydayVLA outperforms other methods by an average of 49% in success rate across blocks, balls, ... | definition/direction/unit from same section | p. 6 (V. RESULTS) |
| THE BEST SCORES ARE HIGHLIGHTED IN BOLD, AND THE SECOND-BEST SCORES ARE UNDERLINED. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 1. EveryDayVLA system. Top: EveryDayVLA finetunes a VLA for a low-cost manipulator to generate continuous and discrete actions, which are passed to an ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared ... | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| AdaHorizon outperforms all baselines by dynamically adjusting the executed action-chunk length: for complex manipulation tasks, shorter chunks enable timely replanning and higher success rates, ... | comparison identity and matched condition | p. 6 (V. RESULTS) |
| Baselines On the LIBERO simulation benchmark, we report success rates across all four task suites, comparing against Diffusion Policy [3], Octo [5], DiT Policy ... | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| Results on LIBERO simulation benchmark Across the four LIBERO suites, our method trails the top-performing baseline by an average of 3.9 % (Table II). | comparison identity and matched condition | p. 5 (V. RESULTS) |
| Our ensembler shows a 1.6% improvement in success rate compared to the next best method. | comparison identity and matched condition | p. 6 (V. RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Dataset We fine-tune the OpenVLA-7B model [19] on our custom dataset of 1,200 demonstrations-each pairing a naturallanguage instruction with an RGB observation sequence and ... | component/input/data sensitivity | p. 4 (IV. EXPERIMENTS) |
| On ball pick-and-place, EverydayVLA exceeds both baselines in every variant except "pick-and-place right." For rock manipulation, our model achieves comparable success, underscoring its robustness ... | component/input/data sensitivity | p. 6 (V. RESULTS) |
| In an ablation against using only continuous (Cont-L1) or only discrete (AR) actions, AdaHorizon consistently improves performance in every suite-on average by 0.8 % ... | component/input/data sensitivity | p. 6 (V. RESULTS) |
| Policy inputs: third-person image, language instruction Spatial SR (%) Object SR (%) Goal SR (%) Long SR (%) Average SR (%) Diffusion Policy (scratch) ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon). | For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Primary metric/result | Results on Real-World Tests In real-world, in-distribution pick-and-place experiments, EverydayVLA outperforms other methods by an average of 49% in success rate across blocks, balls, ... | numeric claim only at cited anchor | p. 6 (V. RESULTS) |

- Numeric sentences retained from the body:
- **p. 6 / V. RESULTS - extractive body cue:** We also achieve an inference rate of up to 108.4 Hz (Table III), adding only 0.9 ms of latency relative to OpenVLA-OFT [35], which corresponds ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well as relatively low number of expert ... | p. 6 (VI. CONCLUSIONS) |
| body limitation/failure cue | The primary failure mode for EverydayVLA is delayed object release and not finishing the task in a timely manner. | p. 6 (V. RESULTS) |
| body limitation/failure cue | Fig. 1. EveryDayVLA system. Top: EveryDayVLA finetunes a VLA for a low-cost manipulator to generate continuous and discrete actions, which are passed to an ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | In real-world trials, we evaluate both in-distribution and out-of-distribution scenarios against OpenVLA and OpenVLA-OFT. | p. 4 (IV. EXPERIMENTS) |
| body limitation/failure cue | Method Inference Rate (Hz) ↑ Latency (sec) ↓ OpenVLA [19] 4.2 0.2396 OpenVLA-OFT [35] 109.7 0.0729 Oursli 54.2-108.4 0.0738 TABLE IV GENERALIZATION AND ROBUSTNESS ... | p. 5 (V. RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details We extended the [35] codebase to jointly train autoregressive and regression heads and deploy with our AdaHorizon ensembler. | p. 4 (IV. EXPERIMENTS) |
| On the other hand, diffusion-based VLAs suffer from long training times [33] [34], and multiple denoising steps. | p. 2 (III. METHOD) |
| We use a LoRA rank of 32, batch size 8, and 4-step gradient accumulation. | p. 4 (IV. EXPERIMENTS) |
| Hardware We built a $300 6-DOF robotic manipulator (see Figure 3), using brackets on online marketplaces due to cost constraints. | p. 3 (III. METHOD) |
| EveryDayVLA uses the Prismatic-7B VLM [45], which uses a two part visual encoder, containing pretrained SigLIP [46] and DinoV2 [47] models. | p. 3 (III. METHOD) |
| Top: We benchmark our model with static distractors, and a cluttered scene where we add different objects, and vary the arrangement after every single ... | p. 5 (V. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / VI. CONCLUSIONS - extractive body cue:** We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well as relatively low number of expert demonstrations ...
- **p. 6 / V. RESULTS - extractive body cue:** The primary failure mode for EverydayVLA is delayed object release and not finishing the task in a timely manner.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. EveryDayVLA system. Top: EveryDayVLA finetunes a VLA for a low-cost manipulator to generate continuous and discrete actions, which are passed to an adaptive ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In real-world trials, we evaluate both in-distribution and out-of-distribution scenarios against OpenVLA and OpenVLA-OFT.
- **p. 5 / V. RESULTS - extractive body cue:** Method Inference Rate (Hz) ↑ Latency (sec) ↓ OpenVLA [19] 4.2 0.2396 OpenVLA-OFT [35] 109.7 0.0729 Oursli 54.2-108.4 0.0738 TABLE IV GENERALIZATION AND ROBUSTNESS TO ...

- **Evidence anchors reviewed:** datasets p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS), metrics p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 5 (IV. EXPERIMENTS), baselines p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 4 (IV. EXPERIMENTS), p. 5 (V. RESULTS), p. 6 (V. RESULTS), results p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
