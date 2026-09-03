# Method - From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p076.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p076.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 9 (B. Policy Steering for Open-World Alignment), p. 6 (A. From Action Rollouts to Behavior Narration), p. 8 (B. Policy Steering for Open-World Alignment), p. 8 (B. Policy Steering for Open-World Alignment), p. 7 (B. Policy Steering for Open-World Alignment), p. 6 (A. From Action Rollouts to Behavior Narration)): Our system queries the VLM twice to first generate behavior narrations and then select the best action plan, The overall inference time is 3.7 seconds among which the generation of ...

## Method Body Digest

- **p. 9 / B. Policy Steering for Open-World Alignment - extractive body cue:** Our system queries the VLM twice to first generate behavior narrations and then select the best action plan, The overall inference time is 3.7 seconds ...
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** This method uses the encoder £4 on ground-truth future observations 10 get privileged (posterior) future latent states Zeer as input for the VLM.
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** This indicates that the VLM struggles to reason directly about predicted action outcomes from the world model's latent states and essentially degrades toa traditional end-to-end ...
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** To fully leverage the VLM's open-world reasoning capabilities for generalized policy steering, it is essential to enable the ‘model to interpret predicted action outcomes through ...
- **p. 7 / B. Policy Steering for Open-World Alignment - extractive body cue:** We first keep the VLM's role as the verifier unchanged and ablate the effect of using an explicit world model to predict action outcomes.
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** We use GPT-4o [29] to process the predicted visual observations and generate behavior narrations in a zero-shot manner.
- **p. 7 / B. Policy Steering for Open-World Alignment - extractive body cue:** For each phase, we visualize the imagined T-step rollouts decoded from the world model for the 3 out of 6 action plans sampled from the ...
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** Inthe Bag task, we modify the original task description from "Please pick up a bag of chips from the table and minimize the contact region ...

## Design Rationale

- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** In Figure 4, we present examples of runtime policy steering using our approach for the Fork task and additional examples for Cup and Bag tasks ...
- **p. 4 / 1. InTRopucTION - extractive body cue:** The training data consists of both successful and failed rollouts from the base policy (a / 0) and additional demonstration data, This allows the world ...
- **p. 2 / 1. InTRopucTION - extractive body cue:** Ultimately, this alignment step enables ‘our "VLM-in-the-loop" policy steering approach to interpret, action plans as behavior narrations and select high-quality plans by reasoning over those ...

## Source Evidence Cues

- **p. 9 / B. Policy Steering for Open-World Alignment - extractive body cue:** Our system queries the VLM twice to first generate behavior narrations and then select the best action plan, The overall inference time is 3.7 seconds ...
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** This method uses the encoder £4 on ground-truth future observations 10 get privileged (posterior) future latent states Zeer as input for the VLM.
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** This indicates that the VLM struggles to reason directly about predicted action outcomes from the world model's latent states and essentially degrades toa traditional end-to-end ...
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** To fully leverage the VLM's open-world reasoning capabilities for generalized policy steering, it is essential to enable the ‘model to interpret predicted action outcomes through ...
- **p. 7 / B. Policy Steering for Open-World Alignment - extractive body cue:** We first keep the VLM's role as the verifier unchanged and ablate the effect of using an explicit world model to predict action outcomes.
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** We use GPT-4o [29] to process the predicted visual observations and generate behavior narrations in a zero-shot manner.
- **p. 7 / B. Policy Steering for Open-World Alignment - extractive body cue:** For each phase, we visualize the imagined T-step rollouts decoded from the world model for the 3 out of 6 action plans sampled from the ...
- **Detected method headings:** B. Policy Steering for Open-World Alignment (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Our system queries the VLM twice to first generate behavior narrations and then select the best action plan, The overall inference time ... | p. 9 (B. Policy Steering for Open-World Alignment), p. 6 (A. From Action Rollouts to Behavior Narration) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | This method uses the encoder £4 on ground-truth future observations 10 get privileged (posterior) future latent states Zeer as input for the ... | p. 6 (A. From Action Rollouts to Behavior Narration), p. 8 (B. Policy Steering for Open-World Alignment) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | This indicates that the VLM struggles to reason directly about predicted action outcomes from the world model's latent states and essentially degrades ... | p. 8 (B. Policy Steering for Open-World Alignment), p. 8 (B. Policy Steering for Open-World Alignment) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** Inthe Bag task, we modify the original task description from "Please pick up a bag of chips from the table and minimize the contact region ...
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** We also compare our approach with several baselines to investigate the advantages of using an explicit world model for predicting action outcomes and decoding a ...
- **p. 9 / B. Policy Steering for Open-World Alignment - extractive body cue:** We also showcase an additional application of our system as a runtime monitor Which returns if a single action plan is good or bad, opening ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | robot, observations, ZxQ, combine, RGB, image, data, proprioceptive, states, end-effector, pose, gripper, state, denotes | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | robot, observations, ZxQ, combine, RGB, image, data, proprioceptive, states, end-effector | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Figure, present, examples, runtime, policy, steering, Fork, task, additional, Cup | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | Inthe, Bag, task, modify, original, description, Please, pick, chips, table | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1. InTRopucTION - extractive body cue:** The robot's observations 0 < O :=ZxQ combine RGB image data I € T and proprioceptive states q © Q(eg., end-effector pose, gripper state), and ...
- **p. 4 / 1. InTRopucTION - extractive body cue:** The training data consists of both successful and failed rollouts from the base policy (a / 0) and additional demonstration data, This allows the world ...
- **p. 2 / 1. InTRopucTION - extractive body cue:** In this work, we contribute to the predictive category of methods, Our method anticipates future outcomes of the policy's actions via a latent ‘world model, ...
- **p. 2 / 1. InTRopucTION - extractive body cue:** To predict challenging action outcomes (eg. interaction dynamics of a manipulator and a deformable bag), we use state-of-the-art world models [25, 50] to predict lower-dimensional ...
- **p. 3 / 1. InTRopucTION - extractive body cue:** Specifically, we take advantage of recent advances in latent dynamics ‘models [25, 50] which can learn lower-dimensional latent state representations from high-dimensional observation-action data collected ...
- **p. 4 / 1. InTRopucTION - extractive body cue:** IV-A), a Recurrent State Space Model (RSSM) is pretrained to leam good latent embeddings of the dynamics conditioned on the observations and actions.
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** This method uses the encoder £4 on ground-truth future observations 10 get privileged (posterior) future latent states Zeer as input for the VLM.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | For each step trajectory snippet {(0},a3}£27 from the dataset, the encoder £4 processes the initial observation o} at timestep f, and the ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | We also introduce a third task that features longer horizon and more complex interactions Fork-to-Bow! | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | For each method, we conduct 20 trials with | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / B. Policy Steering for Open-World Alignment - extractive body cue:** Our system queries the VLM twice to first generate behavior narrations and then select the best action plan, The overall inference time is 3.7 seconds ...
- **p. 7 / B. Policy Steering for Open-World Alignment - extractive body cue:** For each phase, we visualize the imagined T-step rollouts decoded from the world model for the 3 out of 6 action plans sampled from the ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We fine-tune the model using the Low-Rank Adaptation (LoRA) technique [20], keeping both the encoder £ and the latent ‘dynamics model f,, frozen during the ...
- **p. 9 / B. Policy Steering for Open-World Alignment - extractive body cue:** Inference time for each component in the system (averaged across 3 runs) shows that FOREWARN greatly reduces the time to generate behavior narrations from our ...
- **p. 9 / B. Policy Steering for Open-World Alignment - extractive body cue:** Our system queries the VLM twice to first generate behavior narrations and then select the best action plan, The overall inference time is 3.7 seconds ...
- **p. 7 / B. Policy Steering for Open-World Alignment - extractive body cue:** For each phase, we visualize the imagined T-step rollouts decoded from the world model for the 3 out of 6 action plans sampled from the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** system, queries, VLM, twice, first, generate, behavior, narrations, then, select, best, action, plan, overall, inference, time, seconds, among, generation, candidate.
- **Relevant PDF headings:** B. Policy Steering for Open-World Alignment (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures. | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Filtering / recovery | Fig. 3: Examples of Behavior Narrations Predicted by Each Approach. The top row displays the ground-truth robot ‘observations and the prompt used ... | p. 7 (Figure/Table caption), p. 6 (V. EXPERIMENTS) |
| Monitoring / re-entry | V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec. | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTS - extractive body cue:** VLM Fine-tuning, We construct our VQA dataset for fine-tuning from the same offline dataset, Dyyy, used to train the world model.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We fine-tune the model using the Low-Rank Adaptation (LoRA) technique [20], keeping both the encoder £ and the latent ‘dynamics model f,, frozen during the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Training FOREWARN. In part A (Sec. IV-A), a Recurrent State Space Model (RSSM) is pretrained to leam good latent embeddings of the dynamics ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We use this task to study how our framework performs when faced with harder-to-predict interaction outcomes and nuanced failures (e.g., crushing the chips inside the ...
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** (4) Classfier-Dyn-Latent, which is similar to VLM-DynLat-Category, but instead of relying ‘on a VLM, it directly takes the predicted latent embeddings Seq 88 input and ...
- **p. 9 / VI. Limrrations - extractive body cue:** B2 revealed that our system's primary failures stem from the world model's imprecise "imagination", exacerbated by our limited training data.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 9 (B. Policy Steering for Open-World Alignment), p. 6 (A. From Action Rollouts to Behavior Narration), p. 8 (B. Policy Steering for Open-World Alignment), p. 8 (B. Policy Steering for Open-World Alignment), p. 7 (B. Policy Steering for Open-World Alignment), p. 6 (A. From Action Rollouts to Behavior Narration), objective p. 8 (B. Policy Steering for Open-World Alignment), p. 6 (A. From Action Rollouts to Behavior Narration), p. 9 (B. Policy Steering for Open-World Alignment), temporal p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 3 (1. InTRopucTION), p. 3 (1. InTRopucTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** To predict challenging action outcomes (eg. interaction dynamics of a manipulator and a deformable bag), we use state-of-the-art world models [25, 50] to predict lower-dimensional latent state representations from highdimensional ... (p. 2, 1. InTRopucTION).
- **Objective/update evidence:** We use GPT-4o [29] to process the predicted visual observations and generate behavior narrations in a zero-shot manner. (p. 6, A. From Action Rollouts to Behavior Narration).
- **Temporal/runtime evidence:** We also introduce a third task that features longer horizon and more complex interactions Fork-to-Bow! (p. 5, V. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
