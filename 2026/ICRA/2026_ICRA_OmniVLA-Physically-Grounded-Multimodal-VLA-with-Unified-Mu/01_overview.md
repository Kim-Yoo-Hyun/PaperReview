# OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html.
> PDF retrieval source: https://arxiv.org/pdf/2511.01210. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Robotics
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html
- Full-text retrieval: https://arxiv.org/pdf/2511.01210
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This brings several benefits that solve the challenges above: (i) making sensor information spatially grounded in RGB pixel coordinates to facilitate robotic manipulation on target objects, (ii) remaining close to RGB statistics ...를 문제로 두고, We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into an image-native space.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-language-action (VLA) models have shown strong generalization in robotic manipulation through largescale vision-language pretraining.
- **p. 1 / Abstract - extractive body cue:** However, most existing models rely solely on RGB cameras, limiting their perception and, consequently, manipulation capabilities.
- **p. 1 / Abstract - extractive body cue:** We present OmniVLA, an omni-modality VLA model that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation.
- **p. 1 / Abstract - extractive body cue:** The core of our approach is the sensormasked image, a unified representation that overlays physically meaningful, spatially grounded masks onto the RGB images.
- **p. 1 / Abstract - extractive body cue:** These masks are derived from sensors including an infrared camera, a mmWave radar, and a microphone array.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This brings several benefits that solve the challenges above: (i) making sensor information spatially grounded in RGB pixel coordinates to facilitate robotic manipulation on target ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** There are several challenges in integrating diverse sensors with a VLA model.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into an ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the sensor-masked images, we propose a tailored VLA model architecture (Figure 2).
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables robots to combine the strong generalization of foundation models and physical information from various sensors seamlessly, to enable physically-grounded spatial intelligence.
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, and (c) acoustic microphone array, by ...
- **p. 1 / Abstract - extractive body cue:** This image-native unification keeps sensor input close to RGB statistics to facilitate training, provides a uniform interface across sensor hardware, and enables data-efficient learning with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Then, to generate masks for interested objects in the scene, we use a cloud-based Vision-Language Model (VLM) to interpret task request and generate a prompt ...
- **p. 3 / III. SYSTEM DESIGN - extractive body cue:** The tokens are concatenated together with language tokens as input for the large language model in the architecture, and then we generate the final action ...
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** We use SmolVLA as our base model by default, modify its architecture, and train our model from its pretrained weights.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Then we overlay the sensor images on the masked regions of RGB images to output sensor-masked images, which are the input for our multi-sensor vision-language-action model. | image/video, language instruction, proprioception과 history | p. 3 (III. SYSTEM DESIGN), p. 1 (I. INTRODUCTION) |
| State/latent | Then, overlay, sensor, images, masked, regions, RGB, output, sensor-masked, input, multi-sensor, vision-language-action | language-grounded task state와 action-policy context | p. 3 (III. SYSTEM DESIGN), p. 1 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN) |
| Output/action | They leverage vision-language pretraining to map user prompts and camera observations to robot actions, showing great generalization and instruction following capability. | continuous action, pose 또는 action chunk | p. 1 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN), p. 2 (I. INTRODUCTION) |
| Objective/outcome | The tokens are concatenated together with language tokens as input for the large language model in the architecture, and then we generate the final action predictions using the action expert. | instruction following, task success, generalization과 latency | p. 3 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into an ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the sensor-masked images, we propose a tailored VLA model architecture (Figure 2).
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables robots to combine the strong generalization of foundation models and physical information from various sensors seamlessly, to enable physically-grounded spatial intelligence.
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, and (c) acoustic microphone array, by ...
- **p. 1 / Abstract - extractive body cue:** This image-native unification keeps sensor input close to RGB statistics to facilitate training, provides a uniform interface across sensor hardware, and enables data-efficient learning with ...
- **p. 6 / IV. EVALUATION - extractive body cue:** On average, OmniVLA outperforms VLA-RGB model and VLA-RAW model by 59% and 28% in success rate respectively.
- **p. 6 / IV. EVALUATION - extractive body cue:** As shown in Figure 6, OmniVLA constantly outperforms VLA-RAW model, achieving similar success rate with only around 50% of the training episodes.
- **p. 5 / IV. EVALUATION - extractive body cue:** We evaluate model performance using task success rates computed over 25 independent trials per task with random object placement, complemented by task scores: 0.5 score ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION) |
| Embodiment/environment | This is likely due to SmolVLA is pretrained with lerobot robot arm dataset [2]. | hardware/simulator version and reset protocol | p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION) |
| Dataset/benchmark | 5: Examples of Robotic Manipulation Task Completion over Time. | role, split, size and leakage | p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION) |
| Metric | We evaluate model performance using task success rates computed over 25 independent trials per task with random object placement, complemented by task scores: 0.5 score for choosing the | definition, denominator, direction and uncertainty | p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION) |
| Baseline/ablation | Second, we show that our approach provides superior generalization capability for sensor-related tasks, outperforming baselines. | fair input/data/compute/action matching | p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, ...
- **p. 5 / III. SYSTEM DESIGN - extractive body cue:** We underline that our architecture does not require all sensors shown here.
- **p. 6 / IV. EVALUATION - extractive body cue:** As the SmolVLA pretraining dataset does not include any non-RGB sensor, we consider the number of episodes reasonable and showing high learning efficiency of our ...
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** This allows the model to generate a full action chunk step by step from random noise.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This brings several benefits that solve the challenges above: (i) making sensor information spatially grounded in RGB pixel coordinates to facilitate robotic manipulation on target objects, (ii) remaining close to RGB statistics ...를 문제로 두고, We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into an image-native space.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
