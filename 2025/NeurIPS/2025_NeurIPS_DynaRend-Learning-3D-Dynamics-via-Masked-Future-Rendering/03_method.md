# Method - DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=r4dzaP61QH; PDF retrieval source: https://arxiv.org/pdf/2510.24261. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology), p. 5 (3 Methodology), p. 3 (3 Methodology)): Each demonstration consists of a trajectory sequence where each element is represented as a triplet including visual observation O, language instruction l, and end-effector state A.

## Method Body Digest

- **p. 4 / 3 Methodology - extractive body cue:** Each demonstration consists of a trajectory sequence where each element is represented as a triplet including visual observation O, language instruction l, and end-effector state ...
- **p. 4 / 3 Methodology - extractive body cue:** To incorporate task-specific information, we encode the language instruction using a pretrained CLIP [34] text encoder and concatenate the resulting embeddings l with the triplane ...
- **p. 6 / 3 Methodology - extractive body cue:** This position is then used to query the triplane representation for subsequent rotation and gripper state prediction, following the same decoding procedure as during training.
- **p. 6 / 3 Methodology - extractive body cue:** The resulting feature is then passed through a lightweight MLP to predict discretized rotation Euler angles and the binary gripper open/close state, both supervised using ...
- **p. 5 / 3 Methodology - extractive body cue:** (3) Both the reconstructive and predictive networks share the same architecture and are jointly used as the triplane encoder for downstream policy learning.
- **p. 3 / 3 Methodology - extractive body cue:** Given feature volumes, we leverage differentiable volumetric rendering to learn a reconstructive model and a predictive model for pretraining, detailed in Sec.
- **p. 3 / 3 Methodology - extractive body cue:** Among various paradigms, keyframe-based manipulation has emerged as a popular approach, where the agent is tasked with predicting the next key action state - including ...
- **p. 6 / 3 Methodology - extractive body cue:** The overall objective for pretraining is a weighted combination of two loss terms for reconstruction and future prediction respectively: Lpretrain = λreconLrecon + λpredLpred, (6) ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Our contribution can be summarized as follows: • We propose DynaRend, a novel representation learning framework that learns generalizable triplane features via masked future rendering ...
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our method on two challenging robotic manipulation benchmarks, RLBench [21] and Colosseum [32].
- **p. 3 / 3 Methodology - extractive body cue:** In this section, we present the proposed DynaRend in detail.

## Source Evidence Cues

- **p. 4 / 3 Methodology - extractive body cue:** Each demonstration consists of a trajectory sequence where each element is represented as a triplet including visual observation O, language instruction l, and end-effector state ...
- **p. 4 / 3 Methodology - extractive body cue:** To incorporate task-specific information, we encode the language instruction using a pretrained CLIP [34] text encoder and concatenate the resulting embeddings l with the triplane ...
- **p. 6 / 3 Methodology - extractive body cue:** This position is then used to query the triplane representation for subsequent rotation and gripper state prediction, following the same decoding procedure as during training.
- **p. 6 / 3 Methodology - extractive body cue:** The resulting feature is then passed through a lightweight MLP to predict discretized rotation Euler angles and the binary gripper open/close state, both supervised using ...
- **p. 5 / 3 Methodology - extractive body cue:** (3) Both the reconstructive and predictive networks share the same architecture and are jointly used as the triplane encoder for downstream policy learning.
- **p. 3 / 3 Methodology - extractive body cue:** Given feature volumes, we leverage differentiable volumetric rendering to learn a reconstructive model and a predictive model for pretraining, detailed in Sec.
- **p. 3 / 3 Methodology - extractive body cue:** Among various paradigms, keyframe-based manipulation has emerged as a popular approach, where the agent is tasked with predicting the next key action state - including ...
- **Detected method headings:** 3 Methodology (p. 3); Method (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Each demonstration consists of a trajectory sequence where each element is represented as a triplet including visual observation O, language instruction l, ... | p. 4 (3 Methodology), p. 4 (3 Methodology) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To incorporate task-specific information, we encode the language instruction using a pretrained CLIP [34] text encoder and concatenate the resulting embeddings l ... | p. 4 (3 Methodology), p. 6 (3 Methodology) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | This position is then used to query the triplane representation for subsequent rotation and gripper state prediction, following the same decoding procedure ... | p. 6 (3 Methodology), p. 6 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 Methodology - extractive body cue:** The overall objective for pretraining is a weighted combination of two loss terms for reconstruction and future prediction respectively: Lpretrain = λreconLrecon + λpredLpred, (6) ...
- **p. 6 / 3 Methodology - extractive body cue:** The ground-truth action translation is projected onto the three orthogonal planes to generate corresponding target heatmaps, which are used to supervise the predicted action heatmaps ...
- **p. 4 / 3 Methodology - extractive body cue:** The learning objective for the agent is to predict the end-effector state of the nearest future keyframe, conditioned on the current observation O and the ...
- **p. 4 / 3 Methodology - extractive body cue:** To this end, we formulate the pretraining task as a combination of two complementary objectives: reconstruction, which encourages understanding of scene geometry, and future prediction, ...
- **p. 5 / 3 Methodology - extractive body cue:** The rendering loss is computed as the mean squared error between the rendered outputs and the corresponding ground-truth values from the target images.
- **p. 5 / 3 Methodology - extractive body cue:** The rendering losses for reconstruction and future prediction are formulated as Lrecon = λc//C(r) -ˆC(r, Vnow)// + λs//S(r) -ˆS(r, Vnow)// + λdSiLog(D(r), ˆD(r, Vnow)), Lpred ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 6 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Among, various, paradigms, keyframe-based, manipulation, emerged, popular, where, agent, tasked, predicting, next, action, state | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Among, various, paradigms, keyframe-based, manipulation, emerged, popular, where, agent, tasked | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contribution, summarized, follows, DynaRend, novel, representation, learning, framework, learns, generalizable | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | overall, objective, pretraining, weighted, combination, loss, terms, reconstruction, future, prediction | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 Methodology - extractive body cue:** Among various paradigms, keyframe-based manipulation has emerged as a popular approach, where the agent is tasked with predicting the next key action state - including ...
- **p. 3 / 3 Methodology - extractive body cue:** 3.1 Problem Definition Language-conditioned robotic manipulation is a fundamental yet challenging task that requires agents to ground natural language instructions into executable actions based on ...
- **p. 4 / 3 Methodology - extractive body cue:** Each demonstration consists of a trajectory sequence where each element is represented as a triplet including visual observation O, language instruction l, and end-effector state ...
- **p. 4 / 3 Methodology - extractive body cue:** The learning objective for the agent is to predict the end-effector state of the nearest future keyframe, conditioned on the current observation O and the ...
- **p. 6 / 3 Methodology - extractive body cue:** The objective is to predict the next keyframe action A = {apose, agripper}, where apose = {atrans, arot} ∈SE(3) is the end-effector pose, and agripper ...
- **p. 2 / 1 Introduction - extractive body cue:** The masked features and the language instruction are processed through a reconstructive and a predictive model, yielding two intermediate feature volumes that represent the current ...
- **p. 6 / 3 Methodology - extractive body cue:** For rotation component arot and gripper state agripper, we query the triplane features at the predicted action translation position by interpolating the three planes and ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The input observation at each time step consists of four calibrated RGB-D images captured from the front, left shoulder, right shoulder, and ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | For both settings, each task is evaluated over 25 rollout episodes, and we report the average task success rate. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For both settings, each task is evaluated over 25 rollout episodes, and we report the average task success rate. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 Methodology - extractive body cue:** To incorporate task-specific information, we encode the language instruction using a pretrained CLIP [34] text encoder and concatenate the resulting embeddings l with the triplane ...
- **p. 6 / 3 Methodology - extractive body cue:** This position is then used to query the triplane representation for subsequent rotation and gripper state prediction, following the same decoding procedure as during training.
- **p. 3 / 3 Methodology - extractive body cue:** Given feature volumes, we leverage differentiable volumetric rendering to learn a reconstructive model and a predictive model for pretraining, detailed in Sec.
- **p. 7 / 4 Experiments - extractive body cue:** Each task is evaluated with 25 rollouts under 5 different seeds.
- **p. 9 / 4 Experiments - extractive body cue:** The training hyperparameters are kept consistent with the simulation experiments.
- **p. 9 / 4 Experiments - extractive body cue:** We pretrain our model on the collected real-world dataset for 30k steps with augmented views and fine-tune it for an additional 10k steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** demonstration, consists, trajectory, sequence, where, element, represented, triplet, including, visual, observation, language, instruction, end-effector, state, incorporate, task-specific, information, encode, pretrained.
- **Relevant PDF headings:** 3 Methodology (p. 3); Method (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We conduct simulation experiments on two challenging robotic manipulation benchmarks: RLBench [21] and Colosseum [32]. | p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Action / skill decoding | Our model achieves the best trade-off between success rate and inference speed when compared to other baseline methods, demonstrating strong manipulation performance ... | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Receding execution / feedback | Notably, compared to the baseline RVT [13] model, DynaRend achieves an average success rate improvement of 32.3%. | p. 7 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive body cue:** Additionally, we perform an ablation study on the effect of the masking ratio applied to the triplane features in Fig.
- **p. 7 / 4 Experiments - extractive body cue:** Moreover, unlike prior methods that rely on large-scale external pretraining datasets, our method is pretrained solely on task-relevant multi-view RGB-D data without additional external supervision.
- **p. 8 / 4 Experiments - extractive body cue:** We attribute these gains to the robust spatial and physical priors captured during the 3D-aware masked future rendering pretraining, which enables the policy to better ...
- **p. 9 / 4 Experiments - extractive body cue:** Incorporating synthetic views during pretraining helps mitigate overfitting to the limited camera viewpoints and encourages the model to learn more viewinvariant and robust 3D representations ...
- **p. 7 / 4 Experiments - extractive body cue:** Even relative to RVT-2, a two-stage variant of RVT that incorporates additional refinement, our method still shows noticeable gains.
- **p. 9 / 4 Experiments - extractive body cue:** We further conduct an ablation on the target view augmentation strategy, as shown in Tab.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: DynaRend framework overview. (a) We reconstruct the point cloud from multi-view RGB-D inputs, encode it with an MLP, and project it onto three ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology), p. 5 (3 Methodology), p. 3 (3 Methodology), objective p. 6 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology), temporal p. 6 (4 Experiments), p. 6 (4 Experiments), p. 3 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
