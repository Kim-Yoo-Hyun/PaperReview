# Method - RoboDreamer: Learning Compositional World Models for Robot Imagination

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v235/zhou24f.html; PDF retrieval source: https://arxiv.org/pdf/2404.12377. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2.1. Planning with Text-Conditioned Video Generation), p. 3 (2.1. Planning with Text-Conditioned Video Generation)): Given a UPDP G, we then use a trajectory-task conditioned policy π(·/{xh}H h=0, c) : X H+1×C →∆(AH) to infer executable actions from synthesized videos.

## Method Body Digest

- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** Given a UPDP G, we then use a trajectory-task conditioned policy π(·/{xh}H h=0, c) : X H+1×C →∆(AH) to infer executable actions from synthesized videos.
- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** To implement this generation problem, we use the video diffusion model and use the base source code from (Ko et al., 2023).
- **p. 3 / 2.2. Executing Videos Plans - extractive body cue:** The policy takes as input two adjacent image observations xt and xt+1 in the synthesized video τ and outputs an action a to execute.
- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** RoboDreamer: Learning Compositional World Models for Robot Imagination pick orange from bottom drawer and place on counter Language Instruction Parsing pick orange VP / action ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are three-fold. • We introduce RoboDreamer, a compositional world model capable of factorizing the video generation process by leveraging the inherent compositionality of ...
- **p. 2 / 1. Introduction - extractive body cue:** By utilizing a text parser, we dissect language instructions into a set of primitives, isolating actions and the spatial relationships between objects.
- **p. 1 / 1. Introduction - extractive body cue:** Task Instruction: "move pepsi can near plastic bottle" AVDC RoboDreamer Figure 1: Compositional Action Specification.
- **p. 1 / 1. Introduction - extractive body cue:** When existing text-to-video models (AVDC (Ko et al., 2023)) are given unusual combinations of language instructions, they are unable to synthesize videos that align accurately ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are three-fold. • We introduce RoboDreamer, a compositional world model capable of factorizing the video generation process by leveraging the inherent compositionality of ...
- **p. 2 / 1. Introduction - extractive body cue:** This enables our approach to generalize to both new combinations of language and multimodal input. process by leveraging the inherent compositionality of natural language.
- **p. 1 / 1. Introduction - extractive body cue:** In response, we introduce RoboDreamer, a compositional world model capable of factorizing the video generation 1.

## Source Evidence Cues

- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** Given a UPDP G, we then use a trajectory-task conditioned policy π(·/{xh}H h=0, c) : X H+1×C →∆(AH) to infer executable actions from synthesized videos.
- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** To implement this generation problem, we use the video diffusion model and use the base source code from (Ko et al., 2023).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Given a UPDP G, we then use a trajectory-task conditioned policy π(·/{xh}H h=0, c) : X H+1×C →∆(AH) to infer executable actions ... | p. 3 (2.1. Planning with Text-Conditioned Video Generation), p. 3 (2.1. Planning with Text-Conditioned Video Generation) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | To implement this generation problem, we use the video diffusion model and use the base source code from (Ko et al., 2023). | p. 3 (2.1. Planning with Text-Conditioned Video Generation) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | Given a UPDP G, we then use a trajectory-task conditioned policy π(·/{xh}H h=0, c) : X H+1×C →∆(AH) to infer executable actions ... | p. 3 (2.1. Planning with Text-Conditioned Video Generation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update PDF body cue not selected; no claim inferred - inspect equations and algorithm boxes
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, takes, input, adjacent, image, observations, synthesized, video, outputs, action, execute, RoboDreamer, Learning, Compositional | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | policy, takes, input, adjacent, image, observations, synthesized, video, outputs, action | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | contributions, three-fold, introduce, RoboDreamer, compositional, world, model, capable, factorizing, video | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | not stated or recoverable in the selected PDF body | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2.2. Executing Videos Plans - extractive body cue:** The policy takes as input two adjacent image observations xt and xt+1 in the synthesized video τ and outputs an action a to execute.
- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** RoboDreamer: Learning Compositional World Models for Robot Imagination pick orange from bottom drawer and place on counter Language Instruction Parsing pick orange VP / action ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are three-fold. • We introduce RoboDreamer, a compositional world model capable of factorizing the video generation process by leveraging the inherent compositionality of ...
- **p. 2 / 1. Introduction - extractive body cue:** By utilizing a text parser, we dissect language instructions into a set of primitives, isolating actions and the spatial relationships between objects.
- **p. 1 / 1. Introduction - extractive body cue:** Task Instruction: "move pepsi can near plastic bottle" AVDC RoboDreamer Figure 1: Compositional Action Specification.
- **p. 1 / 1. Introduction - extractive body cue:** When existing text-to-video models (AVDC (Ko et al., 2023)) are given unusual combinations of language instructions, they are unable to synthesize videos that align accurately ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | We use a spatial-temporal convolution network in each ResNet block of U-Net for efficiency. | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | We use a similar tiling approach to enhance temporal consistency. | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | RoboDreamer: Learning Compositional World Models for Robot Imagination Algorithm 1 Training 1: Input: Diffusion Model ϵθ, Training Step N 2: for i ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.1. Evaluation on Video Generation - extractive body cue:** We use pre-trained models to encode multi-modal instructions.
- **p. 7 / 4.2. Evaluation on Robotic Planning - extractive body cue:** We use the open-source text-to-video codebase from (Ko et al., 2023) to train models.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Given, UPDP, then, trajectory-task, conditioned, policy, infer, executable, actions, synthesized, videos, implement, generation, problem, video, diffusion, model, base, source, code.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | We take the real-world robotics dataset RT-1 (Brohan et al., 2022) to evaluate video generation. | p. 6 (4.1. Evaluation on Video Generation), p. 6 (4.1. Evaluation on Video Generation) |
| Filtering / recovery | According to the results presented in Table 3, RoboDreamer achieves superior task success rates compared to baseline models even if RoboDreamer is ... | p. 7 (4.2. Evaluation on Robotic Planning), p. 5 (Figure/Table caption) |
| Monitoring / re-entry | According to the results presented in Table 3, RoboDreamer achieves superior task success rates compared to baseline models even if RoboDreamer is ... | p. 7 (4.2. Evaluation on Robotic Planning), p. 8 (4.2. Evaluation on Robotic Planning) |

## Failure and Ablation Link

- **p. 6 / 4.1. Evaluation on Video Generation - extractive body cue:** We compare RoboDreamer with AVDC (Ko et al., 2023), a video generation model for robotics; HiP (Ajay et al., 2023), a latent video diffusion model ...
- **p. 7 / 4.1. Evaluation on Video Generation - extractive body cue:** By factorizing textual instructions into primitive components, RoboDreamer could successfully generalize to unseen task instructions by formulating them into combinations of seen components.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Compositional World Models. Given language instructions and multimodal instructions such as goal images and sketches, our approach factorizes the generation into a composition ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Overall framework of RoboDreamer. On the left, We leverage the natural compositionally of language to parse instructions into components like action phrases and ...
- **p. 8 / 6. Conclusion - extractive body cue:** Limitations Although RoboDreamer exhibits strong performance in robot planning tasks, it has several limitations.
- **p. 6 / 4.1. Evaluation on Video Generation - extractive body cue:** The scores are 0, 1, where 0 means the robotic planning in the generated videos is unreasonable or fails to solve tasks and 1 means ...
- **p. 8 / 4.2. Evaluation on Robotic Planning - extractive body cue:** UniPi performs poorly as it does not align with task instructions well.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2.1. Planning with Text-Conditioned Video Generation), p. 3 (2.1. Planning with Text-Conditioned Video Generation), objective 본문 anchor 없음, temporal p. 6 (4.1. Evaluation on Video Generation), p. 7 (4.1. Evaluation on Video Generation), p. 7 (4.1. Evaluation on Video Generation), p. 5 (3.2. Compositional Generation), p. 2 (2. Background), p. 3 (2.1. Planning with Text-Conditioned Video Generation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The policy takes as input two adjacent image observations xt and xt+1 in the synthesized video τ and outputs an action a to execute. (p. 3, 2.2. Executing Videos Plans).
- **Objective/update evidence:** To implement this generation problem, we use the video diffusion model and use the base source code from (Ko et al., 2023). (p. 3, 2.1. Planning with Text-Conditioned Video Generation).
- **Temporal/runtime evidence:** For all methods, we use pertaining T5-XXL as text encoder. (p. 6, 4.1. Evaluation on Video Generation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
