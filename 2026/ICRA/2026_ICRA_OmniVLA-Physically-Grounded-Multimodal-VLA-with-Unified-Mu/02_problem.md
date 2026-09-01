# Problem - OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2511.01210. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): This brings several benefits that solve the challenges above: (i) making sensor information spatially grounded in RGB pixel coordinates to facilitate robotic manipulation on target objects, (ii) remaining close to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-language-action (VLA) models have shown strong generalization in robotic manipulation through largescale vision-language pretraining.
- **p. 1 / Abstract - extractive PDF cue:** However, most existing models rely solely on RGB cameras, limiting their perception and, consequently, manipulation capabilities.
- **p. 1 / Abstract - extractive PDF cue:** We present OmniVLA, an omni-modality VLA model that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation.
- **p. 1 / Abstract - extractive PDF cue:** The core of our approach is the sensormasked image, a unified representation that overlays physically meaningful, spatially grounded masks onto the RGB images.
- **p. 1 / Abstract - extractive PDF cue:** These masks are derived from sensors including an infrared camera, a mmWave radar, and a microphone array.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** This brings several benefits that solve the challenges above: (i) making sensor information spatially grounded in RGB pixel coordinates to facilitate robotic manipulation on target ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** There are several challenges in integrating diverse sensors with a VLA model.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This brings several benefits that solve the challenges above: (i) making sensor information spatially grounded in RGB pixel coordinates to facilitate robotic ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Then we overlay the sensor images on the masked regions of RGB images to output sensor-masked images, which are the input for ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Then, overlay, sensor, images, masked, regions, RGB, output, sensor-masked, input | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | second, part, multi-sensor, vision-language-action, model, backbone, designed, sensor-masked | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Then, overlay, sensor, images, masked, regions, RGB, output, sensor-masked, input | p. 3 (III. SYSTEM DESIGN), p. 1 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN) |
| Decision / output variable | action, pose, option or chunk a; body terms: present, OmniVLA, first, multisensory, VLA, integrates, novel, sensing | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: tokens, concatenated, together, language, input, large, model, architecture | p. 4 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN) |
| Success / guarantee | instruction-conditioned task success | p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** There are several challenges in integrating diverse sensors with a VLA model.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To solve these challenges, we take inspiration from how the human brain interprets sensor information: as we are used to RGB images, we naturally anchor ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** They leverage vision-language pretraining to map user prompts and camera observations to robot actions, showing great generalization and instruction following capability.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. SYSTEM DESIGN), p. 1 (Abstract)): We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into an image-native space.

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Building on the sensor-masked images, we propose a tailored VLA model architecture (Figure 2).
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** This enables robots to combine the strong generalization of foundation models and physical information from various sensors seamlessly, to enable physically-grounded spatial intelligence.
- **p. 4 / III. SYSTEM DESIGN - extractive PDF cue:** We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, and (c) acoustic microphone array, by ...
- **p. 1 / Abstract - extractive PDF cue:** This image-native unification keeps sensor input close to RGB statistics to facilitate training, provides a uniform interface across sensor hardware, and enables data-efficient learning with ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We underline that our architecture does not require all sensors shown here. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | As the SmolVLA pretraining dataset does not include any non-RGB sensor, we consider the number of episodes reasonable ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | This allows the model to generate a full action chunk step by step from random noise. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. SYSTEM DESIGN), p. 1 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. SYSTEM DESIGN), p. 1 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN), p. 2 (I. INTRODUCTION), objective p. 4 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
