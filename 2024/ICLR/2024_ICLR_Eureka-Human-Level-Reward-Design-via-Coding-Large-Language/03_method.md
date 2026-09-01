# Method - Eureka: Human-Level Reward Design via Coding Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IEduRUO55F; PDF retrieval source: https://openreview.net/forum?id=IEduRUO55F. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD)): We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts.

## Method Body Digest

- **p. 5 / 3 METHOD - extractive body cue:** We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts.
- **p. 3 / 3 METHOD - extractive body cue:** EUREKA consists of three algorithmic components: 1) environment as context that enables zero-shot generation of executable rewards, 2) evolutionary search that iteratively proposes and refines ...
- **p. 4 / 3 METHOD - extractive body cue:** In practice, to ensure that the environment code fits within the LLM's context window and does not leak simulation internals (so that we can expect ...
- **p. 3 / 3 METHOD - extractive body cue:** Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code is that it ...
- **p. 5 / 3 METHOD - extractive body cue:** 3), reward reflection tracks the scalar values of all reward components and the task fitness function at intermediate policy checkpoints throughout training.
- **p. 4 / 3 METHOD - extractive body cue:** As seen, EUREKA adeptly composes over existing observation variables (e.g., fingertip pos) in the provided environment code and produces a competent reward code - all ...
- **p. 4 / 3 METHOD - extractive body cue:** Algorithm 1 EUREKA 1: Require: Task description l, environment code M, coding LLM LLM, fitness function F, initial prompt prompt 2: Hyperparameters: search iteration N, ...
- **p. 5 / 3 METHOD - extractive body cue:** Since the generations are i.i.d, the probability that all reward functions from an iteration are buggy exponentially decreases as the number of samples increases.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1.
- **p. 3 / 3 METHOD - extractive body cue:** EUREKA consists of three algorithmic components: 1) environment as context that enables zero-shot generation of executable rewards, 2) evolutionary search that iteratively proposes and refines ...
- **p. 3 / 3 METHOD - extractive body cue:** We propose directly feeding the raw environment source code (without the reward code, if exists) as context.

## Source Evidence Cues

- **p. 5 / 3 METHOD - extractive body cue:** We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts.
- **p. 3 / 3 METHOD - extractive body cue:** EUREKA consists of three algorithmic components: 1) environment as context that enables zero-shot generation of executable rewards, 2) evolutionary search that iteratively proposes and refines ...
- **p. 4 / 3 METHOD - extractive body cue:** In practice, to ensure that the environment code fits within the LLM's context window and does not leak simulation internals (so that we can expect ...
- **p. 3 / 3 METHOD - extractive body cue:** Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code is that it ...
- **p. 5 / 3 METHOD - extractive body cue:** 3), reward reflection tracks the scalar values of all reward components and the task fitness function at intermediate policy checkpoints throughout training.
- **p. 4 / 3 METHOD - extractive body cue:** As seen, EUREKA adeptly composes over existing observation variables (e.g., fingertip pos) in the provided environment code and produces a competent reward code - all ...
- **Detected method headings:** 3 METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts. | p. 5 (3 METHOD), p. 3 (3 METHOD) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | EUREKA consists of three algorithmic components: 1) environment as context that enables zero-shot generation of executable rewards, 2) evolutionary search that iteratively ... | p. 3 (3 METHOD), p. 4 (3 METHOD) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | In practice, to ensure that the environment code fits within the LLM's context window and does not leak simulation internals (so that ... | p. 4 (3 METHOD), p. 3 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 METHOD - extractive body cue:** Algorithm 1 EUREKA 1: Require: Task description l, environment code M, coding LLM LLM, fitness function F, initial prompt prompt 2: Hyperparameters: search iteration N, ...
- **p. 5 / 3 METHOD - extractive body cue:** Since the generations are i.i.d, the probability that all reward functions from an iteration are buggy exponentially decreases as the number of samples increases.
- **p. 5 / 3 METHOD - extractive body cue:** By providing detailed accounts on how well the RL algorithm optimizes individual reward components, reward reflection enables EUREKA to produce more intricate and targeted reward ...
- **p. 3 / 3 METHOD - extractive body cue:** 3.1 ENVIRONMENT AS CONTEXT Reward design requires the environment specification to be provided to the LLM.
- **p. 3 / 3 METHOD - extractive body cue:** We propose directly feeding the raw environment source code (without the reward code, if exists) as context.
- **p. 4 / 3 METHOD - extractive body cue:** How can we effectively overcome the sub-optimality of single-sample reward generation?
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 4 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, reward, function, over, environment, state, action, variables, only, requirement, source, code, exposes, easy | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Given, reward, function, over, environment, state, action, variables, only, requirement | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | introduce, Evolution-driven, Universal, REward, Kit, Agent, EUREKA, novel, design, algorithm | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Algorithm, EUREKA, Require, Task, description, environment, code, coding, LLM, fitness | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 METHOD - extractive body cue:** Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code is that it ...
- **p. 4 / 3 METHOD - extractive body cue:** In practice, to ensure that the environment code fits within the LLM's context window and does not leak simulation internals (so that we can expect ...
- **p. 5 / 3 METHOD - extractive body cue:** We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In an RDP, the goal is to output a reward function R ∈R such that the policy π := AM(R) that optimizes R achieves the ...
- **p. 4 / 3 METHOD - extractive body cue:** As seen, EUREKA adeptly composes over existing observation variables (e.g., fingertip pos) in the provided environment code and produces a competent reward code - all ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Enables a new gradient-free in-context learning approach to reinforcement learning from human feedback (RLHF) that can generate more performant and human-aligned reward functions 2
- **p. 5 / 3 METHOD - extractive body cue:** 2, where the snapshot values of av penalty are provided as a list in the reward feedback.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | Evolution (32 Samples), which performs only the initial reward generation step, sampling the same number of reward functions as two iterations in ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | G.3, we provide several examples of EUREKA (Human Init.) steps. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | Evolution (32 Samples), which performs only the initial reward generation step, sampling the same number of reward functions as two iterations in ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 METHOD - extractive body cue:** We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts.
- **p. 5 / 3 METHOD - extractive body cue:** 3), reward reflection tracks the scalar values of all reward components and the task fitness function at intermediate policy checkpoints throughout training.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** For each final reward function obtained from each method, we run 5 independent PPO training runs and report the average of the maximum task metric ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** reward, reflection, automated, feedback, summarizes, policy, training, dynamics, texts, EUREKA, consists, three, algorithmic, components, environment, context, enables, zero-shot, generation, executable.
- **Relevant PDF headings:** 3 METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | In addition to coverage over robot form factors, we ensure depth in our evaluation by including all 20 tasks from the Bidexterous ... | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Coverage / augmentation | Figure 4: EUREKA outperforms Human and L2R across all tasks. In particular, EUREKA realizes much greater gains on high-dimensional dexterity environments. about ... | p. 6 (Figure/Table caption), p. 28 (Figure/Table caption) |
| Downstream learning interface | Figure 12: EUREKA reward functions' improvement over alternative reward functions are statistically significant. Dexterity Performance Breakdown. We present the raw success rates ... | p. 29 (Figure/Table caption), p. 2 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 4.3 RESULTS - extractive body cue:** This ablation helps study, given a fixed number of reward function budget, whether it is more advantageous to perform the EUREKA evolution or simply sample ...
- **p. 7 / 4.3 RESULTS - extractive body cue:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** We use GPT-4 (OpenAI, 2023), in particular the gpt-4-0314 variant, as the backbone LLM for all LLM-based reward-design algorithms unless specified otherwise.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Isaac and Dexterity share a well-tuned PPO implementation (Schulman et al., 2017; Makoviichuk & Makoviychuk, 2021), and we use this implementation and the task-specific PPO ...
- **p. 8 / 4.3 RESULTS - extractive body cue:** To demonstrate the importance of curriculum learning, we also directly train a policy from scratch on the target task using EUREKA reward without the first-stage ...
- **p. 8 / 4.3 RESULTS - extractive body cue:** This task is highly dynamic and requires a Shadow Hand to continuously rotate a pen to achieve some pre-defined spinning patterns for as many cycles ...
- **p. 29 / Figure/Table caption - extractive body cue:** Figure 13: Raw success rates of all methods on the Dexterity benchmark. Reward Reflection Ablations. In Fig. 14, we provide a detailed per-task breakdown on ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), objective p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), temporal p. 7 (4.3 RESULTS), p. 8 (4.3 RESULTS), p. 8 (4.3 RESULTS), p. 9 (4.3 RESULTS), p. 9 (4.3 RESULTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
