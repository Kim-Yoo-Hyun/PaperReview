# Method - SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2509.18610. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING), p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING)): The twostage training procedure prescribed in [8] is used to first train a history network to predict time-varying system parameters in a latent vector by ingesting a sliding window of ...

## Method Body Digest

- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** The twostage training procedure prescribed in [8] is used to first train a history network to predict time-varying system parameters in a latent vector by ...
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** The deep learned policy architecture is adopted from the SV-Net described in [8], with an additional image preprocessing step appended to the feature extractor network.
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** This full network is trained with a loss on the expert demonstrator's motor commands over the 2s trajectory chunks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we ask the question: "Can we train a visionlanguage drone navigation policy to reach previously unseen goal objects in a previously unseen ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** At deployment, we inference CLIPSeg [11] to produce open-vocabulary semantic images of the environment as conditioning inputs, processed by an end-to-end visuomotor drone policy for ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** SINGER consists of three central components: (i) a semantics-rich photorealistic flight simulator based on 3D Gaussian Splatting for efficient data generation with expert demonstrations, (ii) ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This produces training data for imitation learning a lightweight, robust vision-language guidance and control policy. robot manipulation datasets [4], [5], state-of-the-art policies endow robots with ...
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** We pass the output patch-logits from CLIPSeg into the feature extractor along with the current state measurement during training.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our contributions as follows: • We introduce a high-fidelity drone simulator for efficient imitation learning in language-specified drone navigation problems built on language ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce SINGER (Semantic In-situ Navigation and Guidance for Embodied Robots), a pipeline for training language-conditioned drone navigation policies addressing the aforementioned ...

## Source Evidence Cues

- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** The twostage training procedure prescribed in [8] is used to first train a history network to predict time-varying system parameters in a latent vector by ...
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** The deep learned policy architecture is adopted from the SV-Net described in [8], with an additional image preprocessing step appended to the feature extractor network.
- **Detected method headings:** V. SINGER POLICY ARCHITECTURE AND TRAINING (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The twostage training procedure prescribed in [8] is used to first train a history network to predict time-varying system parameters in a ... | p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING), p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The deep learned policy architecture is adopted from the SV-Net described in [8], with an additional image preprocessing step appended to the ... | p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The twostage training procedure prescribed in [8] is used to first train a history network to predict time-varying system parameters in a ... | p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** This full network is trained with a loss on the expert demonstrator's motor commands over the 2s trajectory chunks.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | question, train, visionlanguage, drone, navigation, policy, reach, previously, unseen, goal, objects, environment, only, board | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | question, train, visionlanguage, drone, navigation, policy, reach, previously, unseen, goal | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summarize, contributions, follows, introduce, high-fidelity, drone, simulator, efficient, imitation, learning | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | full, network, trained, loss, expert, demonstrator, motor, commands, over, trajectory | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we ask the question: "Can we train a visionlanguage drone navigation policy to reach previously unseen goal objects in a previously unseen ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** At deployment, we inference CLIPSeg [11] to produce open-vocabulary semantic images of the environment as conditioning inputs, processed by an end-to-end visuomotor drone policy for ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** SINGER consists of three central components: (i) a semantics-rich photorealistic flight simulator based on 3D Gaussian Splatting for efficient data generation with expert demonstrations, (ii) ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This produces training data for imitation learning a lightweight, robust vision-language guidance and control policy. robot manipulation datasets [4], [5], state-of-the-art policies endow robots with ...
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** We pass the output patch-logits from CLIPSeg into the feature extractor along with the current state measurement during training.
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** Amounting to 907,440 samples of observation-action labeled data pairs, this data captures a finite range of environments and objects that the drone might see in ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We assume that the robot can only use onboard sensors and compute to safely navigate to the specified goal location, specifically using collectivethrust and body-rate ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | We sample RGB images from the 3DGS Ik, at each time step, which is processed into Ik proc with CLIPSeg. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Each experiment consisted of a randomized initial location in the 3DGS environment and a semantic query, and ten policy rollouts. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | When deployed in hardware in the hardest evaluation scenario (three unseen semantic queries in an unseen deployment environment) SINGER performs the best ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** The twostage training procedure prescribed in [8] is used to first train a history network to predict time-varying system parameters in a latent vector by ...
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** This imposes a significant bottleneck on the inference time of the policy (3Hz on NVIDIA Jetson Orin Nano 8Gb), and is the primary reason why ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** twostage, training, procedure, prescribed, first, train, history, network, predict, time-varying, system, parameters, latent, vector, ingesting, sliding, window, changes, observable, states.
- **Relevant PDF headings:** V. SINGER POLICY ARCHITECTURE AND TRAINING (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Baseline and SINGER On Hardware We evaluate the real-world performance of SINGER against a baseline in six hardware experiments with five trials ... | p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |
| Global / local decision | The baseline fails to track the correct semantic query 16.67% of the time (5/30), demonstrating the limited semantic scene understanding of the ... | p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Motion execution / recovery | The overall success rate of the policy insimulation is also comparable to the results in hardware. | p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / VI. EXPERIMENTS - extractive body cue:** The policy is evaluated on successful flight towards the queried object without collisions.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** When the external true-north is removed from SINGER and it must rely on its internal sensors, SINGER still performs comparably or better than the baseline, ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Without a reliable true-north, the onboard magnetometer is susceptible to varying external magnetic fields induced by heavy machinery nearby.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** The baseline was completely unable to perform without an externally provided true north heading, as the velocity set point requires a reliable heading in the ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** SINGER performs the best at this experiment difficulty, reaching the goal region 73% of the time, and reaching sub-meter proximity 92.7% of the time with ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** This results in one more failure case (6/30) vs. the baseline at (5/30) due to tracking the incorrect semantic query, as the drone cannot maintain ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Crosshatching direction on unsuccessful trials denotes the reason for failure, where collisions are counted while the policy has the query in-view, while query-not-in-view describes cases ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING), p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING), objective p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING), temporal p. 4 (IV. LANGUAGE-CONDITIONED DATA SYNTHESIS), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
