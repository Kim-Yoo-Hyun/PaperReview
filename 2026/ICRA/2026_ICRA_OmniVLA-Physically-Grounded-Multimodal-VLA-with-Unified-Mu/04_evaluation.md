# Evaluation - OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2511.01210. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption)): On average, OmniVLA outperforms VLA-RGB model and VLA-RAW model by 59% and 28% in success rate respectively.

## Evaluation Body Digest

- **p. 6 / IV. EVALUATION - extractive PDF cue:** This is likely due to SmolVLA is pretrained with lerobot robot arm dataset [2].
- **p. 6 / IV. EVALUATION - extractive PDF cue:** As the SmolVLA pretraining dataset does not include any non-RGB sensor, we consider the number of episodes reasonable and showing high learning efficiency of our ...
- **p. 5 / IV. EVALUATION - extractive PDF cue:** 5: Examples of Robotic Manipulation Task Completion over Time.
- **p. 5 / IV. EVALUATION - extractive PDF cue:** We evaluate OmniVLA with a real-world prototype across several sensor-related manipulation tasks.
- **p. 5 / IV. EVALUATION - extractive PDF cue:** We evaluate model performance using task success rates computed over 25 independent trials per task with random object placement, complemented by task scores: 0.5 score ...
- **p. 6 / IV. EVALUATION - extractive PDF cue:** Success Rate Task Score Base Model Thermal mmWave Acoustic Average Thermal mmWave Acoustic Average SmolVLA 80% 84% 88% 84% 0.91 0.88 0.92 0.90 Pi0 68% ...
- **p. 6 / IV. EVALUATION - extractive PDF cue:** On average, OmniVLA outperforms VLA-RGB model and VLA-RAW model by 59% and 28% in success rate respectively.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Success rates over number of demonstration episodes. Thermal mmWave Acoustic 0 20 40 60

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EVALUATION (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | On average, OmniVLA outperforms VLA-RGB model and VLA-RAW model by 59% and 28% in success rate respectively. | p. 6 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 6, OmniVLA constantly outperforms VLA-RAW model, achieving similar success rate with only around 50% of the training episodes. | p. 6 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate model performance using task success rates computed over 25 independent trials per task with random object placement, complemented by task scores: 0.5 ... | p. 5 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | OmniVLA significantly outperforms RGB-only VLA models and VLA models trained with unprocessed sensor images. | p. 5 (IV. EVALUATION) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7: Success rates when adapting to unseen tasks. We compare the pretrained OmniVLA model with two base- lines, OmniVLA-Base (no pretraining), Pretrained VLA- ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / IV. EVALUATION - extractive PDF cue:** This is likely due to SmolVLA is pretrained with lerobot robot arm dataset [2].
- **p. 6 / IV. EVALUATION - extractive PDF cue:** As the SmolVLA pretraining dataset does not include any non-RGB sensor, we consider the number of episodes reasonable and showing high learning efficiency of our ...
- **p. 5 / IV. EVALUATION - extractive PDF cue:** 5: Examples of Robotic Manipulation Task Completion over Time.
- **p. 5 / IV. EVALUATION - extractive PDF cue:** We evaluate OmniVLA with a real-world prototype across several sensor-related manipulation tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Instead of relying solely on RGB cameras, OmniVLA equips robots with multi-sensor perception. We use beam- forming heatmaps as acoustic and mmWave sensor ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: System Overview. OmniVLA processes diverse sensor data into image-like 2D spatial representations, and then overlays sensor information onto RGB images to produce spatially ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: Hardware Implementation. (a) robot arm and sensor setup (b) sensor module, integrating multiple sensors and cameras. the embedding of ith sensor image. We ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: Examples of Robotic Manipulation Task Completion over Time. (a) Thermal: finding the cold drink. (b) mmWave: opening the box with an object inside. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Success rates over number of demonstration episodes. Thermal mmWave Acoustic 0 20 40 60
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Success rates when adapting to unseen tasks. We compare the pretrained OmniVLA model with two base- lines, OmniVLA-Base (no pretraining), Pretrained VLA- RAW ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This is likely due to SmolVLA is pretrained with lerobot robot arm dataset [2]. | embodiment, simulator version and control stack | p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION) |
| Task/environment | As the SmolVLA pretraining dataset does not include any non-RGB sensor, we consider the number of episodes reasonable and showing high learning efficiency of ... | reset, timeout, object/scene variation | p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. SYSTEM DESIGN), p. 1 (I. INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (III. SYSTEM DESIGN), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate model performance using task success rates computed over 25 independent trials per task with random object placement, complemented by task scores: 0.5 ... | definition/direction/unit from same section | p. 5 (IV. EVALUATION) |
| Success Rate Task Score Base Model Thermal mmWave Acoustic Average Thermal mmWave Acoustic Average SmolVLA 80% 84% 88% 84% 0.91 0.88 0.92 0.90 Pi0 ... | definition/direction/unit from same section | p. 6 (IV. EVALUATION) |
| On average, OmniVLA outperforms VLA-RGB model and VLA-RAW model by 59% and 28% in success rate respectively. | definition/direction/unit from same section | p. 6 (IV. EVALUATION) |
| Fig. 6: Success rates over number of demonstration episodes. Thermal mmWave Acoustic 0 20 40 60 | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 7: Success rates when adapting to unseen tasks. We compare the pretrained OmniVLA model with two base- lines, OmniVLA-Base (no pretraining), Pretrained VLA- ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| 5: Examples of Robotic Manipulation Task Completion over Time. | definition/direction/unit from same section | p. 5 (IV. EVALUATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Second, we show that our approach provides superior generalization capability for sensor-related tasks, outperforming baselines. | comparison identity and matched condition | p. 5 (IV. EVALUATION) |
| Multi-sensory Task Performance We first evaluate OmniVLA performance on manipulation tasks compared with the baselines. | comparison identity and matched condition | p. 6 (IV. EVALUATION) |
| OmniVLA consistently outperforms all baseline configurations across the three tasks, demonstrating the effectiveness of our unified multi-sensory perception approach. | comparison identity and matched condition | p. 6 (IV. EVALUATION) |
| OmniVLA significantly outperforms RGB-only VLA models and VLA models trained with unprocessed sensor images. | comparison identity and matched condition | p. 5 (IV. EVALUATION) |
| Fig. 7: Success rates when adapting to unseen tasks. We compare the pretrained OmniVLA model with two base- lines, OmniVLA-Base (no pretraining), Pretrained VLA- ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For baselines, we compare our approach against the following ablation baselines: (1) VLA-RGB (modality ablation): VLA models with standard RGB input only for training ... | component/input/data sensitivity | p. 6 (IV. EVALUATION) |
| (2) VLARAW (representation ablation): VLA models with raw sensor data/images for training and inference input. | component/input/data sensitivity | p. 6 (IV. EVALUATION) |
| (3) Acoustic modality: Locating a ringing mobile phone concealed beneath opaque coverings using spatial audio cues from the microphone array, and removing the covering ... | component/input/data sensitivity | p. 5 (IV. EVALUATION) |
| Fig. 1: Instead of relying solely on RGB cameras, OmniVLA equips robots with multi-sensor perception. We use beam- forming heatmaps as acoustic and mmWave ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Fig. 2: System Overview. OmniVLA processes diverse sensor data into image-like 2D spatial representations, and then overlays sensor information onto RGB images to produce ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Fig. 7: Success rates when adapting to unseen tasks. We compare the pretrained OmniVLA model with two base- lines, OmniVLA-Base (no pretraining), Pretrained VLA- ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into ... | On average, OmniVLA outperforms VLA-RGB model and VLA-RAW model by 59% and 28% in success rate respectively. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | As shown in Figure 6, OmniVLA constantly outperforms VLA-RAW model, achieving similar success rate with only around 50% of the training episodes. | numeric claim only at cited anchor | p. 6 (IV. EVALUATION) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EVALUATION - extractive PDF cue:** We use 8 NVIDIA A100 GPUs on a server for distributed training and use a local RTX 4090 GPU for model inference during system evaluation.
- **p. 5 / IV. EVALUATION - extractive PDF cue:** Depending on the size of the demonstration dataset, the time required for training is around 14 hours for 50 K optimization steps with batch size ...
- **p. 6 / IV. EVALUATION - extractive PDF cue:** We evaluate OmniVLA after training on 100 expert demonstration episodes of thermal and acoustic modality tasks and 200 episodes of mmWave modality task individually.
- **p. 6 / IV. EVALUATION - extractive PDF cue:** To evaluate the applicability of our approach on different base VLA models, we apply it to Pi0 [1] and compare the performance across 3 tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | We underline that our architecture does not require all sensors shown here. | p. 5 (III. SYSTEM DESIGN) |
| body limitation/failure cue | As the SmolVLA pretraining dataset does not include any non-RGB sensor, we consider the number of episodes reasonable and showing high learning efficiency of ... | p. 6 (IV. EVALUATION) |
| body limitation/failure cue | This allows the model to generate a full action chunk step by step from random noise. | p. 4 (III. SYSTEM DESIGN) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Depending on the size of the demonstration dataset, the time required for training is around 14 hours for 50 K optimization steps with batch ... | p. 5 (IV. EVALUATION) |
| We evaluate model performance using task success rates computed over 25 independent trials per task with random object placement, complemented by task scores: 0.5 ... | p. 5 (IV. EVALUATION) |
| introduce sensor-masked images, a spatially grounded and semantically aligned representation that allows reusing pre-trained vision encoders, provides a uniform representation across sensor hardware, and ... | p. 2 (2) We) |
| This brings several benefits that solve the challenges above: (i) making sensor information spatially grounded in RGB pixel coordinates to facilitate robotic manipulation on ... | p. 2 (I. INTRODUCTION) |
| This undermines the potential of robots to utilize additional sensory hardware and perform challenging tasks that require perception capability similar to or even beyond ... | p. 1 (I. INTRODUCTION) |
| Second, sensors differ in format, field of view, and resolution, calling for a scalable, uniform representation rather than training sensor fusion models that depend ... | p. 1 (I. INTRODUCTION) |
| We utilize the existing frozen vision encoders to encode sensor-masked images. | p. 3 (III. SYSTEM DESIGN) |
| Similar to the principle of RGB camera, the azimuth-elevation heatmap reveals the environmental information in a direct way for human understanding and acts as ... | p. 3 (III. SYSTEM DESIGN) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, ...
- **p. 5 / III. SYSTEM DESIGN - extractive PDF cue:** We underline that our architecture does not require all sensors shown here.
- **p. 6 / IV. EVALUATION - extractive PDF cue:** As the SmolVLA pretraining dataset does not include any non-RGB sensor, we consider the number of episodes reasonable and showing high learning efficiency of our ...
- **p. 4 / III. SYSTEM DESIGN - extractive PDF cue:** This allows the model to generate a full action chunk step by step from random noise.

- **PDF anchors reviewed:** datasets p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION), metrics p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (IV. EVALUATION), baselines p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 7 (Figure/Table caption), results p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
