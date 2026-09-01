# Evaluation - Learning Interactive Real-World Simulators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/c4d66eae503694424123b93ac0fbaf17-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2310.06114. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 22 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (1. Put cup 2. Pen 3. Apple), p. 22 (Figure/Table caption), p. 8 (Figure/Table caption)): Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot data in UniSim achieves the best ...

## Evaluation Body Digest

- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** [Bottom] Real-robot execution of an RL policy trained in simulation and zero-shot onto the real Language Table task.
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** We then directly deploy the RL policy trained in the simulator onto the real robot in zero-shot, and observe successful task executions as shown in ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 12: First real observations and last real observations of executing the RL policy trained from UniSim in the real world in zero-shot. Middle plot ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot data ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Ablations of history conditioning using FVD, FID, and Inception score, and CLIP score on Ego4D. Conditioning on multiple frames is better than on ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** CIDEr scores for PaLIX finetuned only on simulated data from UniSim compared to no finetuning and finetuning on true video data from ActivityNet Captions.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Diverse and stochastic simulations. On the left, we use text to specify the object being revealed by suffixing "uncovering" with the object name. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Evaluation of RL policy. Percentage of successful simulated rollouts (out of 48 tasks) using the VLA policy with and without RL finetuning on ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** A ADDITIONAL RESULTS (p. 15); A.2 ADDITIONAL REAL-ROBOT RESULTS FOR LONG-HORIZON LANGUAGE POLICY (p. 16); A.3 ADDITIONAL RESULTS ON LEARNING RL POLICY IN UNISIM (p. 17); B DATASETS (p. 19).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot ... | p. 22 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Evaluation of RL policy. Percentage of successful simulated rollouts (out of 48 tasks) using the VLA policy with and without RL finetuning ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Diverse and stochastic simulations. On the left, we use text to specify the object being revealed by suffixing "uncovering" with the object ... | p. 6 (Figure/Table caption) |
| 1. Put cup 2. Pen 3. Apple | EMPIRICAL / REAL-ROBOT OR HARDWARE | Purely finetuning on generated data drastically improves the captioning performance from no finetuning at all on ActivityNet (15.2 to 46.23), while achieving 84% performance ... | p. 8 (1. Put cup 2. Pen 3. Apple) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 7: Hyperparameters for training the VLA RL policy using the ACME framework. D.3 DETAILS OF VIDEO CAPTIONING Note that even though UniSim is ... | p. 22 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** [Bottom] Real-robot execution of an RL policy trained in simulation and zero-shot onto the real Language Table task.
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** We then directly deploy the RL policy trained in the simulator onto the real robot in zero-shot, and observe successful task executions as shown in ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: A universal simulator (UniSim). The simulator of the real-world learns from broad data with diverse information including objects, scenes, human activities, motions in ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Training and inference of UniSim. UniSim is a video diffusion model trained to predict the next (variable length) set of observation frames (ot) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Specifically, the reverse process learns a denoising model ϵθ(o(k) t , k/ht-1, at-1) that, conditioned on the history, generates the next observationfrom initial ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Action-rich simulations. UniSim can support manipulation actions such as "cut carrots", "wash hands", and "pickup bowl" from the same initial frame (top left) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Long-horizon simulations. UniSim sequentially simulates 8 interactions autoregressively. The simulated interactions maintain temporal consistency across long-horizon interactions, correctly preserving objects and locations (ca ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Ablations of history conditioning using FVD, FID, and Inception score, and CLIP score on Ego4D. Conditioning on multiple frames is better than on ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6: Simulations of low-data domains using the Habitat object navigation using HM3D dataset (Ra- makrishnan et al., 2021) with only 700 training exam- ples. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Diverse and stochastic simulations. On the left, we use text to specify the object being revealed by suffixing "uncovering" with the object name. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | [Bottom] Real-robot execution of an RL policy trained in simulation and zero-shot onto the real Language Table task. | embodiment, simulator version and control stack | p. 8 (1. Put cup 2. Pen 3. Apple), p. 8 (1. Put cup 2. Pen 3. Apple) |
| Task/environment | We then directly deploy the RL policy trained in the simulator onto the real robot in zero-shot, and observe successful task executions as shown ... | reset, timeout, object/scene variation | p. 8 (1. Put cup 2. Pen 3. Apple) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 7 (1. Put cup 2. Pen 3. Apple) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 7 (1. Put cup 2. Pen 3. Apple), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 8: [Top] Simulation from low-level controls. UniSim supports low-level control actions as inputs to move endpoint horizontally, vertically, and diagonally. [Bottom] Real-robot execution ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 12: First real observations and last real observations of executing the RL policy trained from UniSim in the real world in zero-shot. Middle ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Table 1: Ablations of history conditioning using FVD, FID, and Inception score, and CLIP score on Ego4D. Conditioning on multiple frames is better than ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| CIDEr scores for PaLIX finetuned only on simulated data from UniSim compared to no finetuning and finetuning on true video data from ActivityNet Captions. | definition/direction/unit from same section | p. 8 (1. Put cup 2. Pen 3. Apple) |
| Figure 5: Diverse and stochastic simulations. On the left, we use text to specify the object being revealed by suffixing "uncovering" with the object ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 3: Evaluation of RL policy. Percentage of successful simulated rollouts (out of 48 tasks) using the VLA policy with and without RL finetuning ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 7: Long-horizon simulation. A VLM poliy generates high-level language actions (first row) which are executed in the simulator (middle row) similar to how ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2: Evaluation of long-horizon actions. Re- duction in distance to goal (RDG) defined in Equa- tion 3 across 5 evaluation runs of VLM ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| CIDEr scores for PaLIX finetuned only on simulated data from UniSim compared to no finetuning and finetuning on true video data from ActivityNet Captions. | comparison identity and matched condition | p. 8 (1. Put cup 2. Pen 3. Apple) |
| Table 1: Ablations of history conditioning using FVD, FID, and Inception score, and CLIP score on Ego4D. Conditioning on multiple frames is better than ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Table 3: Evaluation of RL policy. Percentage of successful simulated rollouts (out of 48 tasks) using the VLA policy with and without RL finetuning ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We compare PaLI-X finetuned on purely generated videos to pretrained PaLI-X without finetuning and PaLI-X finetuned on original ActivityNet Captions in Table 4. | comparison identity and matched condition | p. 8 (1. Put cup 2. Pen 3. Apple) |
| Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We compare PaLI-X finetuned on purely generated videos to pretrained PaLI-X without finetuning and PaLI-X finetuned on original ActivityNet Captions in Table 4. | component/input/data sensitivity | p. 8 (1. Put cup 2. Pen 3. Apple) |
| Table 1: Ablations of history conditioning using FVD, FID, and Inception score, and CLIP score on Ego4D. Conditioning on multiple frames is better than ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 3: Evaluation of RL policy. Percentage of successful simulated rollouts (out of 48 tasks) using the VLA policy with and without RL finetuning ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Figure 13: Failed environment simulation from the action "uncover bottle" without training on broad data as in UniSim. Top two videos are generated from ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Figure 6: Simulations of low-data domains using the Habitat object navigation using HM3D dataset (Ra- makrishnan et al., 2021) with only 700 training exam- ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose to combine a wealth of data in a conditional video generation framework to instantiate a universal simulator (UniSim)1. | Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot ... | PDF body cue; verify exact table/figure and matched conditions | p. 22 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (1. Put cup 2. Pen 3. Apple), p. 22 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Table 3: Evaluation of RL policy. Percentage of successful simulated rollouts (out of 48 tasks) using the VLA policy with and without RL finetuning ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 8. Close top - extractive body cue:** Condition FID ↓ FVD ↓ IS ↑ CLIP ↑ 1 frame 59.47 315.69 3.03 22.55 4 distant 34.89 237 3.43 22.62 4 recent 34.63 211.3 ...
- **p. 6 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** Conditioning on 4 frames is better than conditioning on a single frame, but conditioning on history that is too far in the past (4 frames ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** RDG (moved) RDG (all) VLM-BC 0.11 ± 0.13 0.07 ± 0.11 Simulator-Hindsight 0.34 ±0.13 0.34 ± 0.13 Table 2: Evaluation of long-horizon actions.
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** Percentage of successful simulated rollouts (out of 48 tasks) using the VLA policy with and without RL finetuning on Language Table (assessed qualitatively using video ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Flexibility in diffusion models promotes simulation of highly stochastic environments that cannot be controlled by actions, so that a policy can learn to only ... | p. 5 (8. Close top) |
| body limitation/failure cue | We see that the simulated rollouts capture both the endpoint movements and the physics of collision. | p. 8 (1. Put cup 2. Pen 3. Apple) |
| body limitation/failure cue | Figure 2: Training and inference of UniSim. UniSim is a video diffusion model trained to predict the next (variable length) set of observation frames ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Specifically, the reverse process learns a denoising model ϵθ(o(k) t , k/ht-1, at-1) that, conditioned on the history, generates the next observationfrom ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 13: Failed environment simulation from the action "uncover bottle" without training on broad data as in UniSim. Top two videos are generated from ... | p. 24 (Figure/Table caption) |
| body limitation/failure cue | Figure 14: When the text-to-video model behind UniSim is only trained on data from Brohan et al. (2022) as opposed incorporating broad data from ... | p. 25 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Since different datasets are curated by different industrial or research communities for different purposes, divergence in information is natural and hard to overcome, posing ... | p. 1 (1 INTRODUCTION) |
| For simulated continuous control actions, we encode them via language embeddings and concatenate the text embeddings with discretized control values. • Real robot data. | p. 3 (1 INTRODUCTION) |
| Specifically, the reverse process learns a denoising model ϵθ(o(k) t , k/ht-1, at-1) that, conditioned on the history, generates the next observationfrom initial noise ... | p. 4 (1 INTRODUCTION) |
| During each evaluation run, we set the long-horizon goal by modifying the location of 3-4 blocks, and measure the blocks' distance to their goal ... | p. 6 (1. Put cup 2. Pen 3. Apple) |
| To acquire reward information, we use the number of steps-to-completion from the training data as a proxy reward to train a model that maps ... | p. 7 (1. Put cup 2. Pen 3. Apple) |
| We first do a sanity check on simulating real-robot executions by applying low-level control actions (e.g., ∆x = 0.05, δy = 0.05) repeatedly for ... | p. 8 (1. Put cup 2. Pen 3. Apple) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 8. Close top - extractive body cue:** Flexibility in diffusion models promotes simulation of highly stochastic environments that cannot be controlled by actions, so that a policy can learn to only control ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** We see that the simulated rollouts capture both the endpoint movements and the physics of collision.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Training and inference of UniSim. UniSim is a video diffusion model trained to predict the next (variable length) set of observation frames (ot) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Specifically, the reverse process learns a denoising model ϵθ(o(k) t , k/ht-1, at-1) that, conditioned on the history, generates the next observationfrom initial ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 13: Failed environment simulation from the action "uncover bottle" without training on broad data as in UniSim. Top two videos are generated from only ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 14: When the text-to-video model behind UniSim is only trained on data from Brohan et al. (2022) as opposed incorporating broad data from the ...

- **PDF anchors reviewed:** datasets p. 8 (1. Put cup 2. Pen 3. Apple), p. 8 (1. Put cup 2. Pen 3. Apple), metrics p. 8 (Figure/Table caption), p. 18 (Figure/Table caption), p. 22 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (1. Put cup 2. Pen 3. Apple), p. 6 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 8 (1. Put cup 2. Pen 3. Apple), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (1. Put cup 2. Pen 3. Apple), p. 22 (Figure/Table caption), results p. 22 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (1. Put cup 2. Pen 3. Apple), p. 22 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
