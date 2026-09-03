# Evaluation - Audio-VLA: Adding Contact Audio Perception to Vision-Language-Action Model for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2511.09958v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT)): I, AudioVLA achieves 97.6% average success rate on LIBERO and 55.1% on RLBench, outperforming all comparative methods.

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENT - extractive body cue:** The performance gap reveals that in tasks requiring precise force control and continuous state monitoring, visual modality nearly loses its ability to perceive contact states ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** [27], domain shift is implemented by randomly varying lighting conditions and desktop surface material colors throughout the environments. b) Real-world setup: The real-world experimental setup ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** 3: Experimental setup showing the hardware platform and real-world manipulation tasks of contact audio feedback: Erasing All Whiteboard Marks (EAWM) and Scooping 5 Grams of ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** The doubling of EAWM success rates after LoRA finetuning [26] and consistent improvements across both simulation and real-world experiments demonstrate that LoRA [26] is particularly ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Additionally, we conduct ablation studies in both simulation and real-world settings to investigate the effectiveness of incorporating contact audio signals into VLA. a) Simulation Experiments ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Ablation Studies Ablation studies on RLBench in Table III and real robot experiments in Table IV reveal the importance of both audio modality integration and ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** AudioVLA preserves 30% and 20% success rates on EAWM and S5GO respectively, whereas vision-only methods approach near-zero performance.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** The inferior performance of the vision-only configuration compared to the full configuration demonstrates that audio provides critical information for TABLE IV: Ablation study results on ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENT (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | I, AudioVLA achieves 97.6% average success rate on LIBERO and 55.1% on RLBench, outperforming all comparative methods. | p. 6 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | II, in seen environmental conditions, our Audio-VLA achieves threefold improvements in success rates compared to OpenVLA-OFT [39] and π0-FAST [5] on both EAWM and ... | p. 6 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | The doubling of EAWM success rates after LoRA finetuning [26] and consistent improvements across both simulation and real-world experiments demonstrate that LoRA [26] is ... | p. 7 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | The inferior performance of the vision-only configuration compared to the full configuration demonstrates that audio provides critical information for TABLE IV: Ablation study results ... | p. 7 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Whether acoustic feedback improves performance in scenarios where contact dynamics are difficult to perceive visually. | p. 5 (IV. EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENT - extractive body cue:** The performance gap reveals that in tasks requiring precise force control and continuous state monitoring, visual modality nearly loses its ability to perceive contact states ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** [27], domain shift is implemented by randomly varying lighting conditions and desktop surface material colors throughout the environments. b) Real-world setup: The real-world experimental setup ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** 3: Experimental setup showing the hardware platform and real-world manipulation tasks of contact audio feedback: Erasing All Whiteboard Marks (EAWM) and Scooping 5 Grams of ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** The doubling of EAWM success rates after LoRA finetuning [26] and consistent improvements across both simulation and real-world experiments demonstrate that LoRA [26] is particularly ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Additionally, we conduct ablation studies in both simulation and real-world settings to investigate the effectiveness of incorporating contact audio signals into VLA. a) Simulation Experiments ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Ablation Studies Ablation studies on RLBench in Table III and real robot experiments in Table IV reveal the importance of both audio modality integration and ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Unlike VLA models, Audio-VLA incorporates audio perception, enabling better assessment of contact states and understanding of manipulation dynamics. events [13] and interaction feedback ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Architecture of Audio-VLA. The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Experimental setup showing the hardware platform and real-world manipulation tasks of contact audio feedback: Erasing All Whiteboard Marks (EAWM) and Scooping 5 Grams ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The performance gap reveals that in tasks requiring precise force control and continuous state monitoring, visual modality nearly loses its ability to perceive contact ... | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Task/environment | [27], domain shift is implemented by randomly varying lighting conditions and desktop surface material colors throughout the environments. b) Real-world setup: The real-world experimental ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| AudioVLA preserves 30% and 20% success rates on EAWM and S5GO respectively, whereas vision-only methods approach near-zero performance. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| The inferior performance of the vision-only configuration compared to the full configuration demonstrates that audio provides critical information for TABLE IV: Ablation study results ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| I, AudioVLA achieves 97.6% average success rate on LIBERO and 55.1% on RLBench, outperforming all comparative methods. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| The doubling of EAWM success rates after LoRA finetuning [26] and consistent improvements across both simulation and real-world experiments demonstrate that LoRA [26] is ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| Whether acoustic feedback improves performance in scenarios where contact dynamics are difficult to perceive visually. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENT) |
| Training is performed in the standard environments with incorporated audio feedback, following all official configurations. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENT) |
| Fig. 1: Unlike VLA models, Audio-VLA incorporates audio perception, enabling better assessment of contact states and understanding of manipulation dynamics. events [13] and interaction ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: Architecture of Audio-VLA. The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The inferior performance of the vision-only configuration compared to the full configuration demonstrates that audio provides critical information for TABLE IV: Ablation study results ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENT) |
| For EAWM, a black marker creates different shapes on the whiteboard compared to training, and for S5GO, a darker oatmeal variety with distinct granular ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENT) |
| I, AudioVLA achieves 97.6% average success rate on LIBERO and 55.1% on RLBench, outperforming all comparative methods. | comparison identity and matched condition | p. 6 (IV. EXPERIMENT) |
| In contact-intensive Tasks 2 and 3, Audio-VLA maintains over 66% performance retention, significantly outperforming comparative methods. | comparison identity and matched condition | p. 6 (IV. EXPERIMENT) |
| The pre-trained audio encoder cannot effectively process manipulation-specific sounds without LoRA [26]. | comparison identity and matched condition | p. 7 (IV. EXPERIMENT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additionally, we conduct ablation studies in both simulation and real-world settings to investigate the effectiveness of incorporating contact audio signals into VLA. a) Simulation ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENT) |
| The pre-trained audio encoder cannot effectively process manipulation-specific sounds without LoRA [26]. | component/input/data sensitivity | p. 7 (IV. EXPERIMENT) |
| Ablation Studies Ablation studies on RLBench in Table III and real robot experiments in Table IV reveal the importance of both audio modality integration ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENT) |
| The robustness differential validates that contact audio provides environment-invariant physical signals. | component/input/data sensitivity | p. 6 (IV. EXPERIMENT) |
| Fig. 2: Architecture of Audio-VLA. The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi | I, AudioVLA achieves 97.6% average success rate on LIBERO and 55.1% on RLBench, outperforming all comparative methods. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Primary metric/result | II, in seen environmental conditions, our Audio-VLA achieves threefold improvements in success rates compared to OpenVLA-OFT [39] and π0-FAST [5] on both EAWM and ... | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENT - extractive body cue:** Visual data is captured at 480×640 resolution, while two piezoelectric contact microphones mounted on both sides of the gripper record audio at 44.1kHz sampling rate.
- **p. 5 / IV. EXPERIMENT - extractive body cue:** Evaluation Protocols: Evaluations are conducted with inference on an NVIDIA H20 GPU communicating with the robot platform through ROS [38], where inference and execution run ...
- **p. 3 / III. METHOD - extractive body cue:** I(·) t ∈RB×3×H×W denotes the raw RGB images from different camera viewpoints at timestep t, with B representing the batch size, H = W representing ...
- **p. 3 / III. METHOD - extractive body cue:** In the Frequency BSpline Projection (FBSP) layer [25], we reduced both the hop length and window length to enhance temporal resolution while maintaining sufficient frequency ...
- **p. 4 / III. METHOD - extractive body cue:** This is achieved through the minimization of the mean L1 loss function: L = 1 K · D K-1 X k=0 D X i=1

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable information particularly when visual perception fails ... | p. 6 (IV. EXPERIMENT) |
| body limitation/failure cue | This paper presents Audio-VLA, a multimodal manipulation policy that integrates acoustic perception into VLA models to overcome vision-only limitations. | p. 7 (V. CONCLUSION) |
| body limitation/failure cue | Experimental results demonstrate that Audio-VLA achieves superior performance in both simulation environments and real-world tasks, proving the contribution of contact audio perception in overcoming ... | p. 7 (V. CONCLUSION) |
| body limitation/failure cue | Audio-VLA overcomes these limitations through acoustic signatures of interaction physics. | p. 6 (IV. EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The LoRA [26] rank is set to 32, training runs for 50k to 100k steps depending on the task, the batch size is 8, ... | p. 6 (IV. EXPERIMENT) |
| Evaluation Protocols: Evaluations are conducted with inference on an NVIDIA H20 GPU communicating with the robot platform through ROS [38], where inference and execution ... | p. 5 (IV. EXPERIMENT) |
| 3: Experimental setup showing the hardware platform and real-world manipulation tasks of contact audio feedback: Erasing All Whiteboard Marks (EAWM) and Scooping 5 Grams ... | p. 5 (IV. EXPERIMENT) |
| Formally, TCR is defined as: TCR = Achieved Progress Task Target ∈[0, 1] (13) where the achieved progress is task-specific, in this paper: • ... | p. 6 (IV. EXPERIMENT) |
| Audio Encoder LoRA Fine-tuning Necessity. | p. 7 (IV. EXPERIMENT) |
| The pre-trained audio encoder cannot effectively process manipulation-specific sounds without LoRA [26]. | p. 7 (IV. EXPERIMENT) |
| Subsequently, we extract the action hidden states Hact from Hdec, where each vector h(m) ∈Rdllm for m = 1, . . . , K ... | p. 4 (III. METHOD) |
| I(·) t ∈RB×3×H×W denotes the raw RGB images from different camera viewpoints at timestep t, with B representing the batch size, H = W ... | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / IV. EXPERIMENT - extractive body cue:** Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable information particularly when visual perception fails to ...
- **p. 7 / V. CONCLUSION - extractive body cue:** This paper presents Audio-VLA, a multimodal manipulation policy that integrates acoustic perception into VLA models to overcome vision-only limitations.
- **p. 7 / V. CONCLUSION - extractive body cue:** Experimental results demonstrate that Audio-VLA achieves superior performance in both simulation environments and real-world tasks, proving the contribution of contact audio perception in overcoming visual ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Audio-VLA overcomes these limitations through acoustic signatures of interaction physics.

- **Evidence anchors reviewed:** datasets p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), metrics p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), baselines p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), results p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
