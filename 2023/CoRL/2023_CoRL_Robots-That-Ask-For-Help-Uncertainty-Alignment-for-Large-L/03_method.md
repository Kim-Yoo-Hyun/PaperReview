# Method - Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.01928; PDF retrieval source: https://arxiv.org/pdf/2307.01928. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction)): Language model planners can generate step-by-step robot plans, where each step y is composed of variable-length sequences of symbols (σ1,σ2,...,σk), e.g., text tokens as input to a language-conditioned policy [1] ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive PDF cue:** Language model planners can generate step-by-step robot plans, where each step y is composed of variable-length sequences of symbols (σ1,σ2,...,σk), e.g., text tokens as input ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state st at time t, given a user ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We propose KNOWNO- Know When You Don't Know - a framework for aligning the uncertainty of LLM-based planners utilizing the theory of conformal prediction (CP) ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our policy π is composed of four parts (Fig.
- **p. 5 / 1 Introduction - extractive PDF cue:** Suppose that each data point consists of a sequence of augmented context x = (˜x0,˜x1,...,˜xT-1) and true labels y = (y0,y1,...,yT-1), where T is the ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Accurately modeling and accounting for uncertainty is a longstanding challenge towards robots that operate reliably in unstructured and novel environments.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we present KNOWNO, which is a framework for measuring and aligning the uncertainty of LLM-based planners such that they know when they ...
- **p. 3 / 1 Introduction - extractive PDF cue:** This eliminates plans that the LLM considers unlikely and reduces the problem of next-step prediction down to a single next-token prediction - aligning with LLM ...

## Design Rationale

- **p. 5 / 1 Introduction - extractive PDF cue:** Here, we present a novel extension of CP to multi-step settings that tackles this challenge.
- **p. 2 / 1 Introduction - extractive PDF cue:** We propose KNOWNO- Know When You Don't Know - a framework for aligning the uncertainty of LLM-based planners utilizing the theory of conformal prediction (CP) ...
- **p. 4 / 1 Introduction - extractive PDF cue:** We introduce CP below, and then present the different practical settings we consider (possibly involving multiple planning steps and/or multiple correct plans per step).

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive PDF cue:** Language model planners can generate step-by-step robot plans, where each step y is composed of variable-length sequences of symbols (σ1,σ2,...,σk), e.g., text tokens as input ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state st at time t, given a user ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We propose KNOWNO- Know When You Don't Know - a framework for aligning the uncertainty of LLM-based planners utilizing the theory of conformal prediction (CP) ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our policy π is composed of four parts (Fig.
- **p. 5 / 1 Introduction - extractive PDF cue:** Suppose that each data point consists of a sequence of augmented context x = (˜x0,˜x1,...,˜xT-1) and true labels y = (y0,y1,...,yT-1), where T is the ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Accurately modeling and accounting for uncertainty is a longstanding challenge towards robots that operate reliably in unstructured and novel environments.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we present KNOWNO, which is a framework for measuring and aligning the uncertainty of LLM-based planners such that they know when they ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Language model planners can generate step-by-step robot plans, where each step y is composed of variable-length sequences of symbols (σ1,σ2,...,σk), e.g., text ... | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state st at time t, ... | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | We propose KNOWNO- Know When You Don't Know - a framework for aligning the uncertainty of LLM-based planners utilizing the theory of ... | p. 2 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1 Introduction - extractive PDF cue:** This eliminates plans that the LLM considers unlikely and reduces the problem of next-step prediction down to a single next-token prediction - aligning with LLM ...
- **p. 1 / Abstract - extractive PDF cue:** KNOWNO builds on the theory of conformal prediction to provide statistical guarantees on task completion while minimizing human help in complex multi-step planning settings.
- **p. 2 / 1 Introduction - extractive PDF cue:** CP also minimizes the average size of prediction sets, thus addressing the goal of minimal help.
- **p. 2 / 1 Introduction - extractive PDF cue:** We formalize these challenges via two desiderata: (i) calibrated confidence: the robot should seek sufficient help to ensure a statistically guaranteed level of task success ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our goal in this work is to address uncertainty alignment: achieve a desired level of task success while minimizing human help.
- **p. 4 / 1 Introduction - extractive PDF cue:** new scenarios ξ∼D, and (ii) minimal help: the policy minimizes the number /C(·)/ of options presented to the human on average across scenarios ξ∼D.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | environment, formulated, partially, observable, Markov, decision, process, POMDP, given, state, time, user, instruction, robot | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | environment, formulated, partially, observable, Markov, decision, process, POMDP, given, state | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Here, present, novel, extension, multi-step, settings, tackles, challenge, KNOWNO-, Know | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | eliminates, plans, LLM, considers, unlikely, reduces, problem, next-step, prediction, down | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive PDF cue:** The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state st at time t, given a user ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Language model planners can generate step-by-step robot plans, where each step y is composed of variable-length sequences of symbols (σ1,σ2,...,σk), e.g., text tokens as input ...
- **p. 3 / 1 Introduction - extractive PDF cue:** We formalize this by considering a joint distribution D over scenarios ξ:=(e,ℓ,g), where e is an environment (POMDP), ℓis a (potentially ambiguous) language instruction, and ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Moreover, natural language instructions in realworld environments often contain a high degree of ambiguity inherently or unintentionally from humans, and confidently following an incorrectly constructed ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We make the following contributions: (1) Given a language instruction, we utilize a pre-trained LLM with uncalibrated confidence to generate a set of possible actions ...
- **p. 4 / 1 Introduction - extractive PDF cue:** We collect N i.i.d. scenarios from the distribution D, and the corresponding contexts summarizing the robot observation and instruction (Section 2).
- **p. 1 / 1 Introduction - extractive PDF cue:** Such false confidence in incorrect outputs poses a significant challenge to LLM-based planning in robotics.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Next we use the lowest score over the timesteps as the score for the sequence4: ˆf(x)y := min t∈[T] ˆf(xt)yt. | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Suppose that each data point consists of a sequence of augmented context x = (˜x0,˜x1,...,˜xT-1) and true labels y = (y0,y1,...,yT-1), where ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Labeling the calibration data takes about 4 hours (for 400 examples) in the multi-step setting and 1.5 hours in single-step settings. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4 Experiments - extractive PDF cue:** Second, it requires 20× inference time compared to other methods.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Language, model, planners, generate, step-by-step, robot, plans, where, step, composed, variable-length, sequences, symbols, text, tokens, input, language-conditioned, policy, Fig, environment.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | In future deployment, we envision that a robot can interact with an end-user (e.g., in a home) to collect a dataset through ... | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Filtering / recovery | Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a language instruction, an LLM generates possible ... | p. 2 (Figure/Table caption), p. 6 (4 Experiments) |
| Monitoring / re-entry | Nonetheless, KnowNo still achieves 1-ϵ target success rate, as the coverage guarantee from CP makes no assumption about the LLM confidences (e.g., ... | p. 8 (4 Experiments), p. 2 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 4 Experiments - extractive PDF cue:** Lastly, we consider No Help where the option with the highest score is always executed without any human intervention.
- **p. 8 / 4 Experiments - extractive PDF cue:** We also run KNOWNO with two other LLMs (without hardware evaluation).
- **p. 9 / 6 Discussion - extractive PDF cue:** Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the text ...
- **p. 9 / 6 Discussion - extractive PDF cue:** Another limitation is that, for the task guarantee to hold, the human needs to faithfully provide help when the robot needs it.
- **p. 7 / 4 Experiments - extractive PDF cue:** First, we investigate whether KNOWNO and the baselines achieve a given target task success rate consistently in the three settings - we set the failure ...
- **p. 6 / 4 Experiments - extractive PDF cue:** Note that the ϵ level is not used in Prompt Set or Binary, and so the user cannot explicitly control the task success rate.
- **p. 7 / 4 Experiments - extractive PDF cue:** Simple Set and Ensemble Set cannot achieve coverage consistently.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction), objective p. 3 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), temporal p. 5 (1 Introduction), p. 5 (1 Introduction), p. 9 (5 Related Work), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 6 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
