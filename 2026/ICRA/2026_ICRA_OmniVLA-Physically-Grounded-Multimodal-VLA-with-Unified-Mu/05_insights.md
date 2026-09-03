# Insights — OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2511.01210. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into an ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the sensor-masked images, we propose a tailored VLA model architecture (Figure 2).
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables robots to combine the strong generalization of foundation models and physical information from various sensors seamlessly, to enable physically-grounded spatial intelligence.
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, and (c) acoustic microphone array, by ...
- **p. 1 / Abstract - extractive body cue:** This image-native unification keeps sensor input close to RGB statistics to facilitate training, provides a uniform interface across sensor hardware, and enables data-efficient learning with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Then, to generate masks for interested objects in the scene, we use a cloud-based Vision-Language Model (VLM) to interpret task request and generate a prompt ...
- **p. 3 / III. SYSTEM DESIGN - extractive body cue:** The tokens are concatenated together with language tokens as input for the large language model in the architecture, and then we generate the final action ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. SYSTEM DESIGN), p. 1 (Abstract), p. 2 (I. INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** This brings several benefits that solve the challenges above: (i) making sensor information spatially grounded in RGB pixel coordinates to facilitate robotic manipulation on target ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** There are several challenges in integrating diverse sensors with a VLA model.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To solve these challenges, we take inspiration from how the human brain interprets sensor information: as we are used to RGB images, we naturally anchor ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** They leverage vision-language pretraining to map user prompts and camera observations to robot actions, showing great generalization and instruction following capability.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, ...
- **p. 5 / III. SYSTEM DESIGN - extractive body cue:** We underline that our architecture does not require all sensors shown here.
- **p. 6 / IV. EVALUATION - extractive body cue:** As the SmolVLA pretraining dataset does not include any non-RGB sensor, we consider the number of episodes reasonable and showing high learning efficiency of our ...
- **Boundary to test:** Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, and (c) acoustic microphone array, by overlaying ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into an image-native space. | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | On average, OmniVLA outperforms VLA-RGB model and VLA-RAW model by 59% and 28% in success rate respectively. | p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION) |
| Failure/limitation | Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, and (c) acoustic microphone array, by overlaying ... | p. 4 (Figure/Table caption), p. 5 (III. SYSTEM DESIGN) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Then we overlay the sensor images on the masked regions of RGB images to output sensor-masked images, which are the input for our multi-sensor vision-language-action model.를 They leverage vision-language pretraining to map user prompts and camera observations to robot actions, showing great generalization and instruction following capability.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, and (c) acoustic microphone array, by overlaying ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into an image-native space.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, and (c) acoustic microphone array, by overlaying ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This is likely due to SmolVLA is pretrained with lerobot robot arm dataset [2]..
3. Compare against the body-reported baseline or a matched simpler baseline: Second, we show that our approach provides superior generalization capability for sensor-related tasks, outperforming baselines..
4. Report the body metric and its denominator/aggregation: We evaluate model performance using task success rates computed over 25 independent trials per task with random object placement, complemented by task scores: 0.5 score for choosing the.
5. Re-run the body-reported ablation/failure condition: For baselines, we compare our approach against the following ablation baselines: (1) VLA-RGB (modality ablation): VLA models with standard RGB input only for training and inference, without our architecture changes..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN), p. 2 (I. INTRODUCTION); the primary result is directionally consistent at p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, OmniVLA, first mechanism이 Second, we show that our approach provides superior generalization capability for sensor-related tasks, outperforming baselines. 대비 We evaluate model performance using task success rates computed over 25 independent trials per task with random object ...을 개선하고, Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
