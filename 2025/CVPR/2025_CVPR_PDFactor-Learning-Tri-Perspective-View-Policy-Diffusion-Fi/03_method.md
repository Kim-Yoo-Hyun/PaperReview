# Method - PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 5 (3. We aim to model their joint dis), p. 5 (3.4. Score Matching Loss), p. 4 (3.2. Tri-Perspective View Projection), p. 4 (3. Method), p. 3 (3. Method)): In particular, given RGB-D observations \protect \mathbf {o}, language instruction \protect \mathbf {l} and robot proprioception \protect \mathbf {c}, our goal is to learn a multi-task policy \pi (\ ma ...

## Method Body Digest

- **p. 3 / 3. Method - extractive PDF cue:** In particular, given RGB-D observations \protect \mathbf {o}, language instruction \protect \mathbf {l} and robot proprioception \protect \mathbf {c}, our goal is to learn a ...
- **p. 5 / 3. We aim to model their joint dis - extractive PDF cue:** Notably, since our denoising network is small, we can sample t multiple times given latent triplane features \protect \mathbf {T}, which helps model convergence and ...
- **p. 5 / 3.4. Score Matching Loss - extractive PDF cue:** After obtaining three 2D feature planes, we introduce score matching loss.
- **p. 4 / 3.2. Tri-Perspective View Projection - extractive PDF cue:** Specifically, given a set of multi-view RGB-D images captured by sensor cameras, we first pass images, which consist of 6 channels including RGB and coordinates ...
- **p. 4 / 3. Method - extractive PDF cue:** Then the triplane tokens are fed into a multi-view transformer along with the instruction and robot proprioception to produce triplane features.
- **p. 3 / 3. Method - extractive PDF cue:** By reparameterizing \mu _\theta as a noise prediction network \epsilon _\theta , the objective can be simplified to mean-squared error between the predicted noise \epsil ...
- **p. 6 / 3. We aim to model their joint dis - extractive PDF cue:** Latent vector \protect \mathbf {z} is aggregated at the location of \protect \mathbf {a}_ t.
- **p. 5 / 3. We aim to model their joint dis - extractive PDF cue:** For the gripper open state and collision state, we simply pass latent vector \protect \mathbf {z} through an MLP to predict a binary label optimized ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In this work, we propose PDFactor, a novel multi-task manipulation agent that leverages a tri-perspective view transformer to learn a hybrid action representation.
- **p. 2 / 1. Introduction - extractive PDF cue:** To summarise, our work presents the following three contributions: • We formulate a hybrid action representation termed Policy Diffusion Field to ground continuous and multimodal ...
- **p. 3 / 3. Method - extractive PDF cue:** In particular, given RGB-D observations \protect \mathbf {o}, language instruction \protect \mathbf {l} and robot proprioception \protect \mathbf {c}, our goal is to learn a ...

## Source Evidence Cues

- **p. 3 / 3. Method - extractive PDF cue:** In particular, given RGB-D observations \protect \mathbf {o}, language instruction \protect \mathbf {l} and robot proprioception \protect \mathbf {c}, our goal is to learn a ...
- **p. 5 / 3. We aim to model their joint dis - extractive PDF cue:** Notably, since our denoising network is small, we can sample t multiple times given latent triplane features \protect \mathbf {T}, which helps model convergence and ...
- **p. 5 / 3.4. Score Matching Loss - extractive PDF cue:** After obtaining three 2D feature planes, we introduce score matching loss.
- **p. 4 / 3.2. Tri-Perspective View Projection - extractive PDF cue:** Specifically, given a set of multi-view RGB-D images captured by sensor cameras, we first pass images, which consist of 6 channels including RGB and coordinates ...
- **p. 4 / 3. Method - extractive PDF cue:** Then the triplane tokens are fed into a multi-view transformer along with the instruction and robot proprioception to produce triplane features.
- **p. 3 / 3. Method - extractive PDF cue:** By reparameterizing \mu _\theta as a noise prediction network \epsilon _\theta , the objective can be simplified to mean-squared error between the predicted noise \epsil ...
- **p. 6 / 3. We aim to model their joint dis - extractive PDF cue:** Latent vector \protect \mathbf {z} is aggregated at the location of \protect \mathbf {a}_ t.
- **Detected method headings:** 2.2. Diffusion Models for Robotic Manipulation (p. 3); 3. Method (p. 3); Model (p. 5); 3. We aim to model their joint dis (p. 5); 4.2. Comparison with State-of-the-Art Methods (p. 6); 4.3. Ablation Study & Model Analysis (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | In particular, given RGB-D observations \protect \mathbf {o}, language instruction \protect \mathbf {l} and robot proprioception \protect \mathbf {c}, our goal is ... | p. 3 (3. Method), p. 5 (3. We aim to model their joint dis) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | Notably, since our denoising network is small, we can sample t multiple times given latent triplane features \protect \mathbf {T}, which helps ... | p. 5 (3. We aim to model their joint dis), p. 5 (3.4. Score Matching Loss) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | After obtaining three 2D feature planes, we introduce score matching loss. | p. 5 (3.4. Score Matching Loss), p. 4 (3.2. Tri-Perspective View Projection) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3. We aim to model their joint dis - extractive PDF cue:** For the gripper open state and collision state, we simply pass latent vector \protect \mathbf {z} through an MLP to predict a binary label optimized ...
- **p. 3 / 3. Method - extractive PDF cue:** By reparameterizing \mu _\theta as a noise prediction network \epsilon _\theta , the objective can be simplified to mean-squared error between the predicted noise \epsil ...
- **p. 5 / 3.4. Score Matching Loss - extractive PDF cue:** After obtaining three 2D feature planes, we introduce score matching loss.
- **p. 3 / 3. Method - extractive PDF cue:** The reverse process aims to determine the posterior distribution of the less noisy sample \protect \mathbf {x}_{t-1} given the noisy sample \protect \mathbf {x}_ t: ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 3 (3. Method), p. 5 (3. We aim to model their joint dis), p. 5 (3. We aim to model their joint dis), p. 4 (3.3. Tri-Perspective View Transformer), p. 4 (3.2. Tri-Perspective View Projection).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | particular, given, RGB-D, observations, protect, mathbf, language, instruction, robot, proprioception, goal, learn, multi-task, policy | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | particular, given, RGB-D, observations, protect, mathbf, language, instruction, robot, proprioception | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | PDFactor, novel, multi-task, manipulation, agent, leverages, tri-perspective, view, transformer, learn | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | gripper, open, state, collision, simply, pass, latent, vector, protect, mathbf | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive PDF cue:** In particular, given RGB-D observations \protect \mathbf {o}, language instruction \protect \mathbf {l} and robot proprioception \protect \mathbf {c}, our goal is to learn a ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Thus the action space is aligned and translationally anchored to the visual features observed from input images, which simplifies the mapping from states to actions ...
- **p. 1 / 1. Introduction - extractive PDF cue:** (c) The proposed hybrid policy learns a latent diffusion field from visual observations and then leverages a small network to decode corresponding action score gradient ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To summarise, our work presents the following three contributions: • We formulate a hybrid action representation termed Policy Diffusion Field to ground continuous and multimodal ...
- **p. 4 / 3.3. Tri-Perspective View Transformer - extractive PDF cue:** We concatenate the triplane and instruction sequences as input tokens which are then processed by a sequence of transformer blocks.
- **p. 3 / 3. Method - extractive PDF cue:** In this section, we elaborate on the proposed PDFactor, a multi-task agent that learns a language-conditioned policy for real-world robotic manipulation.
- **p. 4 / 3.3. Tri-Perspective View Transformer - extractive PDF cue:** The tri-perspective view transformer is responsible to extract latent triplane features from projected tri-perspective view features \ifmm ode \lb race \else \textbraceleft \fi \mathbf {V}_{\text ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Noisy sample \protect \mathbf {x}_ t at arbitrary time step t can be obtained from \ mathbf { x } _t=\sqrt {\Bar ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | ×N Denoising MLP Proprioception AdaLN Reshape Query Pooling Noise Layer Norm MLP Scale, Shift Timestep Sinusodal Encoding MLP Instruction Encoder MLP Gaussian ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3. We aim to model their joint dis - extractive PDF cue:** Notably, since our denoising network is small, we can sample t multiple times given latent triplane features \protect \mathbf {T}, which helps model convergence and ...
- **p. 6 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** Compared with PDFactor, the performance of the vanilla diffusion transformer drops by 15.2%, and the inference time increases significantly, potentially attributed to the explicit spatial ...
- **p. 8 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** Contrary to the prevailing assumption that diffusion-based policies are slower than non-diffusion policies, our model manages to achieve a significant decrease in inference time compared ...
- **p. 8 / 4.4. Evaluation in the Real World - extractive PDF cue:** We collect 15 demonstrations per task and train PDFactor-B with the collected dataset for 10k steps with the same hyperparameters as the simulation data.
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** A single-layer MLP can lead to competitive results with negligible parameters and inference time increasing.
- **p. 5 / 3. We aim to model their joint dis - extractive PDF cue:** At inference time, next keyframe action is sampled via a reverse diffusion process following DDPM: \m a t hbf

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** particular, given, RGB-D, observations, protect, mathbf, language, instruction, robot, proprioception, goal, learn, multi-task, policy, thbf, where, action, consists, DoF, pose.
- **Relevant PDF headings:** 2.2. Diffusion Models for Robotic Manipulation (p. 3); 3. Method (p. 3); Model (p. 5); 3. We aim to model their joint dis (p. 5); 4.2. Comparison with State-of-the-Art Methods (p. 6); 4.3. Ablation Study & Model Analysis (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | We collect 15 demonstrations per task and train PDFactor-B with the collected dataset for 10k steps with the same hyperparameters as the ... | p. 8 (4.4. Evaluation in the Real World), p. 6 (4.1. Experiment Setup) |
| Grasp / trajectory generation | For example, in place cups task, the agent is required to have comprehensive spatial understanding and long-horizon reasoning abilities to hang mugs ... | p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 6 (4.3. Ablation Study & Model Analysis) |
| Contact execution / correction | Our method achieves the best performance with an average success rate of 87.3% among all 18 tasks, an absolute improvement of 5.9% ... | p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** We conduct an ablation study to analyze the impact of several design choices for PDFactor and report results in Tab.
- **p. 6 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** We implement a vanilla baseline where we directly train a diffusion transformer conditioned on triplane features and instructions without utilizing score matching loss.
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** Besides, we implement a variant by replacing feature projection with point renderer in RVT [21].
- **p. 8 / 4.3. Ablation Study & Model Analysis - extractive PDF cue:** Variants Planning Tools Long Rotation Motion Multimodal Precision Occlusion Avg.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation on denoising MLP depth. Inference speed is measured in FPS. 10 25 50 100 Demonstrations 0.4
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. (a) Learning efficiency. We show the learning curves of PDFactor and RVT-2. PDFactor demonstrates faster convergence with a higher performance than previous state-of-the-art ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. PDFactor Overview. The 3D point cloud reconstructed from the multi-view RGB-D images is first featurized and projected to three orthogonal views, which are ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3. Method), p. 5 (3. We aim to model their joint dis), p. 5 (3.4. Score Matching Loss), p. 4 (3.2. Tri-Perspective View Projection), p. 4 (3. Method), p. 3 (3. Method), objective p. 5 (3. We aim to model their joint dis), p. 3 (3. Method), p. 5 (3.4. Score Matching Loss), p. 3 (3. Method), temporal p. 3 (3. Method), p. 4 (3. Method), p. 7 (4.3. Ablation Study & Model Analysis), p. 8 (4.3. Ablation Study & Model Analysis), p. 5 (3. We aim to model their joint dis), p. 5 (3. We aim to model their joint dis).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
