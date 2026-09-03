# Method - Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p145.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p145.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (A. Construction of Interactive Digital Twins), p. 3 (A. Construction of Interactive Digital Twins), p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins), p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 5 (C. Motion Planning via Simulation-Informed Prompting)): Physical simulation: Finally, we integrate a physics simulator 'S [17] equipped with the robot's URDF U to model dynamics lunder interaction, The simulator computes physically plausible state transitions when applying ...

## Method Body Digest

- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** Physical simulation: Finally, we integrate a physics simulator 'S [17] equipped with the robot's URDF U to model dynamics lunder interaction, The simulator computes physically ...
- **p. 3 / A. Construction of Interactive Digital Twins - extractive body cue:** AS shown in Figure 2, our construction pipeline consists of two key stages: (1) reconstructing scenes with accurate geometry and visual appearance, and (2) making ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We consider a tabletop setting with ‘one robotic arm. ‘The framework's input consists of a natural language instruction { specifying the task, and an RGB ...
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** ‘Through this construction pipeline, we obtain an interactive digital twin where the mesh representation provides physical structure, the Gaussian splatting enables efficient and realistic rendering, ...
- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** With the active subgoal +) and selected viewpoint C; determined, the framework proceeds to low-level action generation, We employ the Cross-Entropy Method (CEM) [39] for ...
- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** The corresponding elite actions are then used (0 update the sampling distribution, This sampling and refinement process is repeated for three iterations, after which the ...
- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** decomposition localizes the optimization objective, improving sample efficiency and enhancing planning robustness.
- **p. 4 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** Given initial multi-view observations Jp and a task instruction I, the VLM generates a set of subtasks . each specifying an intermediate objective.

## Design Rationale

- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** To validate the effectiveness of our framework, in this section, we design eight real-world manipulation tasks that require 6 DoF control, semantic understanding, and diverse ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Central o our framework is a pre-trained vision-language model (VLM). ‘The model processes an ordered sequence of interleaved text and RGB images and returns a ...
- **p. 3 / A. Construction of Interactive Digital Twins - extractive body cue:** Unlike prior work, which often focuses solely on static reconstruction [40, 24), our method produces dynamic, actionconditioned digital twins by combining mesh-based physical modeling with ...

## Source Evidence Cues

- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** Physical simulation: Finally, we integrate a physics simulator 'S [17] equipped with the robot's URDF U to model dynamics lunder interaction, The simulator computes physically ...
- **p. 3 / A. Construction of Interactive Digital Twins - extractive body cue:** AS shown in Figure 2, our construction pipeline consists of two key stages: (1) reconstructing scenes with accurate geometry and visual appearance, and (2) making ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We consider a tabletop setting with ‘one robotic arm. ‘The framework's input consists of a natural language instruction { specifying the task, and an RGB ...
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** ‘Through this construction pipeline, we obtain an interactive digital twin where the mesh representation provides physical structure, the Gaussian splatting enables efficient and realistic rendering, ...
- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** With the active subgoal +) and selected viewpoint C; determined, the framework proceeds to low-level action generation, We employ the Cross-Entropy Method (CEM) [39] for ...
- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** The corresponding elite actions are then used (0 update the sampling distribution, This sampling and refinement process is repeated for three iterations, after which the ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Physical simulation: Finally, we integrate a physics simulator 'S [17] equipped with the robot's URDF U to model dynamics lunder interaction, The ... | p. 4 (A. Construction of Interactive Digital Twins), p. 3 (A. Construction of Interactive Digital Twins) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | AS shown in Figure 2, our construction pipeline consists of two key stages: (1) reconstructing scenes with accurate geometry and visual appearance, ... | p. 3 (A. Construction of Interactive Digital Twins), p. 3 (III. PROBLEM FORMULATION) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | We consider a tabletop setting with ‘one robotic arm. ‘The framework's input consists of a natural language instruction { specifying the task, ... | p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** decomposition localizes the optimization objective, improving sample efficiency and enhancing planning robustness.
- **p. 4 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** Given initial multi-view observations Jp and a task instruction I, the VLM generates a set of subtasks . each specifying an intermediate objective.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Central o our framework is a pre-trained vision-language model (VLM). ‘The model processes an ordered sequence of interleaved text and RGB images and returns a ...
- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** The corresponding elite actions are then used (0 update the sampling distribution, This sampling and refinement process is repeated for three iterations, after which the ...
- **p. 4 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** Our approach decomposes tasks into subgoals, adaptively selects viewpoints to facilitate VLM reasoning, and ‘optimizes actions through sampling-based planning.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (C. Motion Planning via Simulation-Informed Prompting), p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 5 (C. Motion Planning via Simulation-Informed Prompting).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | consider, tabletop, setting, robotic, framework, input, consists, natural, language, instruction, specifying, task, RGB, video | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | consider, tabletop, setting, robotic, framework, input, consists, natural, language, instruction | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | validate, effectiveness, framework, section, design, eight, real-world, manipulation, tasks, require | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | decomposition, localizes, optimization, objective, improving, sample, efficiency, enhancing, planning, robustness | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We consider a tabletop setting with ‘one robotic arm. ‘The framework's input consists of a natural language instruction { specifying the task, and an RGB ...
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** High-level planning Future observations of sampled actions VLM evaluation Fig.
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** At each step, the interactive digital twin simulates future states for candidate actions and render the outcomes multiple viewpoints.
- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** Conditioned on 7, and I,, the VLM selects the viewpoint Cy that provides the most informative "observation for distinguishing between action outcomes.
- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** Since robot actions are defined in SE2(3) space but the VLM operates solely on 2D visual inputs, spatial reasoning critically depends on viewpoint selection.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Each action ay € R is defined as the 6-DoF gripper pose and the finger status (open or closed
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | A task is considered a failure if the robot causes imeversible results or if the maximum step budget or time limit is ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Central o our framework is a pre-trained vision-language model (VLM). ‘The model processes an ordered sequence of interleaved text and RGB images ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | The planning policies are rolled out twice per scene to consider the randomness in VLM planning, resulting in 10 trials per task ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We do not assume access to task-specific training data, in-context ‘examples, or hard-coded motion primitives as used in prior work (20, 27, 13, 25].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Physical, simulation, Finally, integrate, physics, simulator, equipped, robot, URDF, model, dynamics, lunder, interaction, computes, physically, plausible, state, transitions, when, applying.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | MOKA [13] chooses the 2D keypoints as intermediate representations for VLM to predict, which are then converted into actions based on the ... | p. 5 (A. Experimental setup), p. 6 (B. Quantitative results) |
| Filtering / recovery | We adopt GPT-4o [1] for both our method and the baselines. | p. 5 (A. Experimental setup), p. 5 (B. Quantitative results) |
| Monitoring / re-entry | As shown in Table Ill, while performance varies across df= ferent tasks due to their diverse requirements, our full method achieves the ... | p. 6 (B. Quantitative results), p. 8 (B. Quantitative results) |

## Failure and Ablation Link

- **p. 6 / B. Quantitative results - extractive body cue:** To assess the contribution of each component in our frame- ‘work, we begin with the full system and systematically remove each component in turn.
- **p. 6 / B. Quantitative results - extractive body cue:** In the "wio CEM" setting, we simply take the mean value of the selected actions without optimizing the action distribution or resampling,
- **p. 8 / B. Quantitative results - extractive body cue:** We validate the effectiveness of our components.
- **p. 8 / B. Quantitative results - extractive body cue:** For example, the robot may attempt to move the gripper directly to the drum without first picking up the drumstick.
- **p. 5 / A. Experimental setup - extractive body cue:** For both OpenVLA and 79, we report their performances under a zero-shot setting and after task-specific fine-tuning on 20 expert demonstrations for each task.
- **p. 5 / A. Experimental setup - extractive body cue:** MOKA [13] chooses the 2D keypoints as intermediate representations for VLM to predict, which are then converted into actions based on the depth information from ...
- **p. 5 / A. Experimental setup - extractive body cue:** A task is considered a failure if the robot causes imeversible results or if the maximum step budget or time limit is reached. ‘The task ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (A. Construction of Interactive Digital Twins), p. 3 (A. Construction of Interactive Digital Twins), p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins), p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 5 (C. Motion Planning via Simulation-Informed Prompting), objective p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 4 (C. Motion Planning via Simulation-Informed Prompting), p. 3 (III. PROBLEM FORMULATION), p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 4 (C. Motion Planning via Simulation-Informed Prompting), temporal p. 5 (A. Experimental setup), p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION), p. 6 (B. Quantitative results), p. 1 (Abstract), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** AS shown in Figure 2, our construction pipeline consists of two key stages: (1) reconstructing scenes with accurate geometry and visual appearance, and (2) making the scene interactable to support ... (p. 3, A. Construction of Interactive Digital Twins).
- **Objective/update evidence:** decomposition localizes the optimization objective, improving sample efficiency and enhancing planning robustness. (p. 5, C. Motion Planning via Simulation-Informed Prompting).
- **Temporal/runtime evidence:** A task is considered a failure if the robot causes imeversible results or if the maximum step budget or time limit is reached. ‘The task is successful iff the success ... (p. 5, A. Experimental setup).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
