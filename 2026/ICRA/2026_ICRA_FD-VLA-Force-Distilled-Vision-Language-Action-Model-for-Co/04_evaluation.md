# Evaluation - FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2602.02142. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption)): Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, substantially outperforming both SmolVLA without force encoding (23.3%), DP3 (11.1%) and even ...

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Results are averaged over 30 evaluation episodes per task.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** To efficiently collect expert demonstrations, we use the 3Dconnexion SpaceMouse to teleoperate the robotic arm.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** This section presents an extensive evaluation of the FDVLA model through real-world experiments and analytical studies.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, substantially outperforming both SmolVLA without force encoding ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** 6 presents the success rates across three contact-rich manipulation tasks.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overview of our framework. During training, measured force signals are encoded into an actual force token via a lightweight projection. A learnable query ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: Visualization of the real robotic platform. We use a UR5e robot arm as the main manipulation platform, the Kinect Azure camera as the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, substantially outperforming both SmolVLA without force ... | p. 6 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6: Success rates for three contact-rich manipulation tasks: Plug in Socket, Clean Whiteboard, and Press Button. Results are averaged over 30 evaluation episodes ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7: Illustration of our visual generalization settings: (Left) Novel Background, where the scene's background differs from training; and (Right) Visual Perturbation, which involves ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Results are averaged over 30 evaluation episodes per task.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** To efficiently collect expert demonstrations, we use the 3Dconnexion SpaceMouse to teleoperate the robotic arm.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** This section presents an extensive evaluation of the FDVLA model through real-world experiments and analytical studies.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overview of our framework. During training, measured force signals are encoded into an actual force token via a lightweight projection. A learnable query ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Visualization of raw force in the plug insertion task.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visualization of real-world experimental tasks: 1) Clean the whiteboard, 2) Press the emergency button, 3) Insert the plug into the socket. the control ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: Visualization of the real robotic platform. We use a UR5e robot arm as the main manipulation platform, the Kinect Azure camera as the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: Success rates for three contact-rich manipulation tasks: Plug in Socket, Clean Whiteboard, and Press Button. Results are averaged over 30 evaluation episodes per ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Illustration of our visual generalization settings: (Left) Novel Background, where the scene's background differs from training; and (Right) Visual Perturbation, which involves changes ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Results are averaged over 30 evaluation episodes per task. | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | To efficiently collect expert demonstrations, we use the 3Dconnexion SpaceMouse to teleoperate the robotic arm. | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, substantially outperforming both SmolVLA without force ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| 6 presents the success rates across three contact-rich manipulation tasks. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 2: Overview of our framework. During training, measured force signals are encoded into an actual force token via a lightweight projection. A learnable ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 5: Visualization of the real robotic platform. We use a UR5e robot arm as the main manipulation platform, the Kinect Azure camera as ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 7: Illustration of our visual generalization settings: (Left) Novel Background, where the scene's background differs from training; and (Right) Visual Perturbation, which involves ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| DP3 is selected as a strong diffusion-based control framework with a parameter scale comparable to ours, which provides a capacity-matched baseline that excels at ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| For all baselines, we standardize training data, evaluation tasks, and optimization budgets to control for dataset and compute confounds, and we report all evaluation ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We compare FD-VLA (ours) with SmolVLA, π0 and DP3, SmolVLA and π0 are evaluated with and without force inputs. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| In the Press Emergency Button task, success required the button to be fully depressed and remain engaged without rebound. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Fig. 2: Overview of our framework. During training, measured force signals are encoded into an actual force token via a lightweight projection. A learnable ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Fig. 4: Visualization of real-world experimental tasks: 1) Clean the whiteboard, 2) Press the emergency button, 3) Insert the plug into the socket. the ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Fig. 5: Visualization of the real robotic platform. We use a UR5e robot arm as the main manipulation platform, the Kinect Azure camera as ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the main contributions of this work are summarized as follows: • We propose the FD-VLA framework that injects a distilled force token ... | Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, substantially outperforming both SmolVLA without force ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Fig. 6: Success rates for three contact-rich manipulation tasks: Plug in Socket, Clean Whiteboard, and Press Button. Results are averaged over 30 evaluation episodes ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | This architecture allows our system to leverage the semantic richness of pretrained VLM while introducing stable, taskrelevant physical reasoning through force distillation, achieving both ... | p. 4 (III. METHODOLOGY) |
| body limitation/failure cue | Finally, FDM mitigates the noise and instability of raw sensor signals by learning a supervised latent embedding that serves as a denoised, taskrelevant proxy ... | p. 4 (III. METHODOLOGY) |
| body limitation/failure cue | Our model achieves consistently higher performance, which highlights the benefit of force distillation for accurate and robust manipulation. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | For evaluation, each task was trained using a set of 50 demonstrations and subsequently evaluated over 30 independent test trials to ensure statistical robustness. | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Note that the FDM is trained to align with real force signals f aF ∈R1×D encoded by a projection layer only during the training ... | p. 4 (III. METHODOLOGY) |
| For the Clean Whiteboard task, a trial was considered successful only if all visible markings on the whiteboard were completely erased. | p. 6 (IV. EXPERIMENTS) |
| For evaluation, each task was trained using a set of 50 demonstrations and subsequently evaluated over 30 independent test trials to ensure statistical robustness. | p. 6 (IV. EXPERIMENTS) |
| Force Distillation Module (FDM) Our FDM generates a compact, state-aware force representation that can be seamlessly integrated into the VLA pipeline without requiring specialized ... | p. 4 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** This architecture allows our system to leverage the semantic richness of pretrained VLM while introducing stable, taskrelevant physical reasoning through force distillation, achieving both robustness ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Finally, FDM mitigates the noise and instability of raw sensor signals by learning a supervised latent embedding that serves as a denoised, taskrelevant proxy for ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Our model achieves consistently higher performance, which highlights the benefit of force distillation for accurate and robust manipulation.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** For evaluation, each task was trained using a set of 50 demonstrations and subsequently evaluated over 30 independent test trials to ensure statistical robustness.

- **PDF anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), results p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
