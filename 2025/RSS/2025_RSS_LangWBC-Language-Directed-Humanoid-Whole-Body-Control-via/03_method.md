# Method - LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p065.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p065.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (B. Language-Directed Student Policy), p. 3 (B. Generative Action Modeling), p. 4 (A. Motion-Tracking Teacher Policy), p. 5 (B. Language-Directed Student Policy), p. 3 (B. Generative Action Modeling), p. 4 (A. Motion-Tracking Teacher Policy)): The decoder then takes the sampled latent vector =: along with the latest state observation to output the action We use an MLP with layer sizes of 2048, 1024, and ...

## Method Body Digest

- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** The decoder then takes the sampled latent vector =: along with the latest state observation to output the action We use an MLP with layer ...
- **p. 3 / B. Generative Action Modeling - extractive body cue:** Then, «stdent policy, leveraging a CVAE architecture, jointly models high-level linguistic insretions and low-level physical actions of the teacher policy ina unified Intent space, During ...
- **p. 4 / A. Motion-Tracking Teacher Policy - extractive body cue:** ‘The teacher policy is trained using Proximal Policy Optimization (PPO) [33] to minimize the discrepancy between the robot's movements and the reference motions. ‘To encourage ...
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** We use a batch size of 1024 64 and a learning rate of 1 x 10°, with one epoch per iteration, We then use the ...
- **p. 3 / B. Generative Action Modeling - extractive body cue:** Retargeted Teacher Training Physics Simulator Mocap Dataset (© Tracking keypoint Student Training ‘Cloning + "Aperson waits _ CUP [rnse forward" Encoder ‘Mocap Dataset qatudent rm ...
- **p. 4 / A. Motion-Tracking Teacher Policy - extractive body cue:** Where Am is a weighting coefficient, and Lyq encourages consistent policy outputs for mirrored states, ie.,
- **p. 2 / B. Generative Action Modeling - extractive body cue:** For example, OmniH12O [10] uses a pre-trained fixed-length MDM model [40] for text-conditioned motion generation, followed by a tracking controller.
- **p. 3 / A. Motion-Tracking Teacher Policy - extractive body cue:** 1) Motion Retargeting: To ensure the MoCap trajectories are kinematically feasible for the teacher policy to track, we perform motion retargeting by applying inverse kinematics ...

## Design Rationale

- **p. 2 / 1. Iyrropucrion - extractive body cue:** Furthermore, our framework enables smooth transitions between motion clips and generates novel motions through interpolation, demonstrating generalization beyond the training data
- **p. 2 / 1. Iyrropucrion - extractive body cue:** ‘+ Our method enables the generation of diverse motions, smooth transitions, and adaptability to a wide range of textual inputs, including the synthesis of novel ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present an end-to-end, language-directed policy for real-world humanoid whole-body ‘control.

## Source Evidence Cues

- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** The decoder then takes the sampled latent vector =: along with the latest state observation to output the action We use an MLP with layer ...
- **p. 3 / B. Generative Action Modeling - extractive body cue:** Then, «stdent policy, leveraging a CVAE architecture, jointly models high-level linguistic insretions and low-level physical actions of the teacher policy ina unified Intent space, During ...
- **p. 4 / A. Motion-Tracking Teacher Policy - extractive body cue:** ‘The teacher policy is trained using Proximal Policy Optimization (PPO) [33] to minimize the discrepancy between the robot's movements and the reference motions. ‘To encourage ...
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** We use a batch size of 1024 64 and a learning rate of 1 x 10°, with one epoch per iteration, We then use the ...
- **p. 3 / B. Generative Action Modeling - extractive body cue:** Retargeted Teacher Training Physics Simulator Mocap Dataset (© Tracking keypoint Student Training ‘Cloning + "Aperson waits _ CUP [rnse forward" Encoder ‘Mocap Dataset qatudent rm ...
- **p. 4 / A. Motion-Tracking Teacher Policy - extractive body cue:** Where Am is a weighting coefficient, and Lyq encourages consistent policy outputs for mirrored states, ie.,
- **p. 2 / B. Generative Action Modeling - extractive body cue:** For example, OmniH12O [10] uses a pre-trained fixed-length MDM model [40] for text-conditioned motion generation, followed by a tracking controller.
- **Detected method headings:** B. Generative Action Modeling (p. 2); A. Motion-Tracking Teacher Policy (p. 3); B. Language-Directed Student Policy (p. 4); A. Teacher Policy Input State (p. 13)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | The decoder then takes the sampled latent vector =: along with the latest state observation to output the action We use an ... | p. 5 (B. Language-Directed Student Policy), p. 3 (B. Generative Action Modeling) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | Then, «stdent policy, leveraging a CVAE architecture, jointly models high-level linguistic insretions and low-level physical actions of the teacher policy ina unified ... | p. 3 (B. Generative Action Modeling), p. 4 (A. Motion-Tracking Teacher Policy) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | ‘The teacher policy is trained using Proximal Policy Optimization (PPO) [33] to minimize the discrepancy between the robot's movements and the reference ... | p. 4 (A. Motion-Tracking Teacher Policy), p. 5 (B. Language-Directed Student Policy) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / A. Motion-Tracking Teacher Policy - extractive body cue:** ‘The teacher policy is trained using Proximal Policy Optimization (PPO) [33] to minimize the discrepancy between the robot's movements and the reference motions. ‘To encourage ...
- **p. 3 / A. Motion-Tracking Teacher Policy - extractive body cue:** 1) Motion Retargeting: To ensure the MoCap trajectories are kinematically feasible for the teacher policy to track, we perform motion retargeting by applying inverse kinematics ...
- **p. 3 / A. Motion-Tracking Teacher Policy - extractive body cue:** The optimization is solved using the LM algorithm with joint limit constraints, yielding kinematically feasible motions that closely match the original MoCap data, The detailed ...
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** 5) Poliey Update: We update the student with the loss in (8).
- **p. 4 / A. Motion-Tracking Teacher Policy - extractive body cue:** REWARD FUNCTION COMPONENTS FoR TEACHER POLICY
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** The training objective follows the variational lower bound
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 4 (A. Motion-Tracking Teacher Policy), p. 5 (B. Language-Directed Student Policy), p. 3 (A. Motion-Tracking Teacher Policy), p. 3 (A. Motion-Tracking Teacher Policy), p. 4 (A. Motion-Tracking Teacher Policy), p. 5 (B. Language-Directed Student Policy).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | enable, robot, interpret, natural, language, commands, design, CVAE-based, student, policy, encodes, textual, instructions, physical | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | enable, robot, interpret, natural, language, commands, design, CVAE-based, student, policy | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | Furthermore, framework, enables, smooth, transitions, between, motion, clips, generates, novel | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | teacher, policy, trained, Proximal, Optimization, PPO, minimize, discrepancy, between, robot | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / B. Language-Directed Student Policy - extractive body cue:** ‘To enable the robot to interpret and act on natural language commands, we design a CVAE-based student policy that encodes textual instructions and physical actions ...
- **p. 4 / B. Language-Directed Student Policy - extractive body cue:** We input a sequence of historical observations and actions, sampled at 10 Hz over a 2-second window, yielding a 20-step trajectory of input-output pars.
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** The decoder then takes the sampled latent vector =: along with the latest state observation to output the action We use an MLP with layer ...
- **p. 3 / III. MerHops - extractive body cue:** A CVAE student policy is then used to align these physically-plausible motions with language inputs, forming a unified latent space that captures the joint distribution ...
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** 2) Teacher Action Query: For each state encountered by the student, the corresponding optimal action is obtained bby querying the teacher policy.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Then, a student policy based on a Conditional Variational Autoencoder (CVAE) [36] is trained via behavior cloning to learn the ‘mapping from natural language commands ...
- **p. 3 / III. MerHops - extractive body cue:** In this section, we present LangWBC, an end-to-end framework that jointly models high-level linguistic instructions and low-level physical actions, enabling robots to execute complex whole-body ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | At each time step, the student is given the language command and its history observation, | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | We input a sequence of historical observations and actions, sampled at 10 Hz over a 2-second window, yielding a 20-step trajectory of ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | At each time step, the student is given the language command and its history observation, | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | We input a sequence of historical observations and actions, sampled at 10 Hz over a 2-second window, yielding a 20-step trajectory of ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / A. Motion-Tracking Teacher Policy - extractive body cue:** ‘The teacher policy is trained using Proximal Policy Optimization (PPO) [33] to minimize the discrepancy between the robot's movements and the reference motions. ‘To encourage ...
- **p. 3 / B. Generative Action Modeling - extractive body cue:** Retargeted Teacher Training Physics Simulator Mocap Dataset (© Tracking keypoint Student Training ‘Cloning + "Aperson waits _ CUP [rnse forward" Encoder ‘Mocap Dataset qatudent rm ...
- **p. 2 / B. Generative Action Modeling - extractive body cue:** For example, OmniH12O [10] uses a pre-trained fixed-length MDM model [40] for text-conditioned motion generation, followed by a tracking controller.
- **p. 3 / A. Motion-Tracking Teacher Policy - extractive body cue:** The optimization is solved using the LM algorithm with joint limit constraints, yielding kinematically feasible motions that closely match the original MoCap data, The detailed ...
- **p. 3 / B. Generative Action Modeling - extractive body cue:** Retargeted Teacher Training Physics Simulator Mocap Dataset (© Tracking keypoint Student Training ‘Cloning + "Aperson waits _ CUP [rnse forward" Encoder ‘Mocap Dataset qatudent rm ...
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** ‘The training process consists of five steps

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** decoder, then, takes, sampled, latent, vector, along, latest, state, observation, output, action, MLP, layer, sizes, units, encoder, stdent, policy, leveraging.
- **Relevant PDF headings:** B. Generative Action Modeling (p. 2); A. Motion-Tracking Teacher Policy (p. 3); B. Language-Directed Student Policy (p. 4); A. Teacher Policy Input State (p. 13).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | We conduct extensive experiments to evaluate our framework for language-directed humanoid whole-body control with 4 Unitree GI humanoid robot. | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Balance-aware whole-body execution | Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The ... | p. 9 (Figure/Table caption), p. 5 (IV. EXPERIMENTS) |
| Recovery / adaptation | Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The ... | p. 9 (Figure/Table caption), p. 5 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks (top ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We then analyze the learned latent space and its contribution to the policy's generalization to unseen commands, highlight key features such as smooth transitions and ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 12. Lower-body Motion Examples. The framework also enables various lowercbady movements soch as stepping, squating and balancing. These motions are also sucessfully transfered tothe ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks (top ...
- **p. 9 / C. Generalization to Unseen Texts - extractive body cue:** ietepolating between walking (Command 1) and side stepping (Command 2) predoces walking the side, a whole-body masion that does not exist i the
- **p. 7 / C. Generalization to Unseen Texts - extractive body cue:** We find the poticy performs forward motion in a consistent speed and style despite phrasing differences like "move" vs. "walk." demonstrating robustness to linguistic variation
- **p. 7 / C. Generalization to Unseen Texts - extractive body cue:** CLIP encoder handles minor linguistic variations well, it produces significantly different encodings for out-of-distribution commands, which the MLP policy struggles to generalize from.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (B. Language-Directed Student Policy), p. 3 (B. Generative Action Modeling), p. 4 (A. Motion-Tracking Teacher Policy), p. 5 (B. Language-Directed Student Policy), p. 3 (B. Generative Action Modeling), p. 4 (A. Motion-Tracking Teacher Policy), objective p. 4 (A. Motion-Tracking Teacher Policy), p. 3 (A. Motion-Tracking Teacher Policy), p. 3 (A. Motion-Tracking Teacher Policy), p. 5 (B. Language-Directed Student Policy), p. 4 (A. Motion-Tracking Teacher Policy), p. 5 (B. Language-Directed Student Policy), temporal p. 5 (B. Language-Directed Student Policy), p. 4 (B. Language-Directed Student Policy), p. 5 (IV. EXPERIMENTS), p. 3 (A. Motion-Tracking Teacher Policy), p. 1 (1. Iyrropucrion), p. 1 (Body text (section boundary not confidently recovered)).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** ‘The teacher policy is trained using Proximal Policy Optimization (PPO) [33] to minimize the discrepancy between the robot's movements and the reference motions. ‘To encourage symmetry inthe learned policy, we ... (p. 4, A. Motion-Tracking Teacher Policy).
- **Objective/update evidence:** ‘The teacher policy is trained using Proximal Policy Optimization (PPO) [33] to minimize the discrepancy between the robot's movements and the reference motions. ‘To encourage symmetry inthe learned policy, we ... (p. 4, A. Motion-Tracking Teacher Policy).
- **Temporal/runtime evidence:** We input a sequence of historical observations and actions, sampled at 10 Hz over a 2-second window, yielding a 20-step trajectory of input-output pars. (p. 4, B. Language-Directed Student Policy).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
