# Method - AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://deepmind.google/research/publications/48151/; PDF retrieval source: https://deepmind.google/research/publications/48151/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3. Place the napkin onto), p. 1 (ABSTRACT), p. 7 (3. Place the napkin onto), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3. Place the napkin onto)): Robot episodes are first embedded by a visual encoder, then k-means unsupervised clustering is done in the space.

## Method Body Digest

- **p. 7 / 3. Place the napkin onto - extractive body cue:** Robot episodes are first embedded by a visual encoder, then k-means unsupervised clustering is done in the space.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios ...
- **p. 7 / 3. Place the napkin onto - extractive body cue:** Language diversity: To measure language diversity, we use the L2 distance in a language embedding space - specifically that of Universal Sentence Encoder (Cer et ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** AutoRT is, to the best of our knowledge, the first system where LLM-controlled robots are allowed to drive autonomously in real world settings, propose their ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The scene description step perceive objects in the environment, the task proposal step suggests possible things the robot could do with them, and then the ...
- **p. 5 / 3. Place the napkin onto - extractive body cue:** For example, if 1 person is supervising 3 robots, then the human teleoperation collect policy was sampled p < 1 3 of the time to ...
- **p. 5 / 3. Place the napkin onto - extractive body cue:** The first two proposed tasks by the LLM are classified as πteleop, the second two tasks are classified as πrt2, an autonomous policy from (Brohan ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This process takes into account constraints specified via "constitutional prompting", where rules about robot behaviour can be defined by the user.

## Design Rationale

- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show that AutoRT scales robot deployment by allowing 1 human to supervise 3-5 mobile manipulators.
- **p. 1 / ABSTRACT - extractive body cue:** Guiding data collection by tapping into the knowledge of foundation models enables AutoRT to effectively reason about autonomy tradeoffs and safety while significantly scaling up ...

## Source Evidence Cues

- **p. 7 / 3. Place the napkin onto - extractive body cue:** Robot episodes are first embedded by a visual encoder, then k-means unsupervised clustering is done in the space.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios ...
- **p. 7 / 3. Place the napkin onto - extractive body cue:** Language diversity: To measure language diversity, we use the L2 distance in a language embedding space - specifically that of Universal Sentence Encoder (Cer et ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** AutoRT is, to the best of our knowledge, the first system where LLM-controlled robots are allowed to drive autonomously in real world settings, propose their ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The scene description step perceive objects in the environment, the task proposal step suggests possible things the robot could do with them, and then the ...
- **p. 5 / 3. Place the napkin onto - extractive body cue:** For example, if 1 person is supervising 3 robots, then the human teleoperation collect policy was sampled p < 1 3 of the time to ...
- **p. 5 / 3. Place the napkin onto - extractive body cue:** The first two proposed tasks by the LLM are classified as πteleop, the second two tasks are classified as πrt2, an autonomous policy from (Brohan ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Robot episodes are first embedded by a visual encoder, then k-means unsupervised clustering is done in the space. | p. 7 (3. Place the napkin onto), p. 1 (ABSTRACT) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in ... | p. 1 (ABSTRACT), p. 7 (3. Place the napkin onto) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | Language diversity: To measure language diversity, we use the L2 distance in a language embedding space - specifically that of Universal Sentence ... | p. 7 (3. Place the napkin onto), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 INTRODUCTION - extractive body cue:** This process takes into account constraints specified via "constitutional prompting", where rules about robot behaviour can be defined by the user.
- **p. 5 / 3. Place the napkin onto - extractive body cue:** Teleoperated data is the most action diverse policy, so we focus on keeping throughput of teleoperation high (no worse than a "1 human 1 robot" ...
- **p. 5 / 3. Place the napkin onto - extractive body cue:** Each πi has a different sampling probability pi that is adjusted during collect primarily based on the number of robots supervised per person.
- **p. 6 / 3. Place the napkin onto - extractive body cue:** Evaluating this is challenging, because downstream methods for utilizing such data are still imperfect - despite considerable recent progress, RL methods present scalability challenges to ...
- **p. 7 / 3. Place the napkin onto - extractive body cue:** We also did an experiment where human supervisors directly optimized the visual diversity at collect time based on robot feedback.
- **p. 7 / 3. Place the napkin onto - extractive body cue:** 5.2 TASK GENERATION In this section we study the quality of task generation prior to filtering based on feasibility (is the task possible) and relevance ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 2 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | breakdown, throughput, collect, policy, visualization, action, trajectories, Appendix, generated, task, LLM, asked, either, output | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | breakdown, throughput, collect, policy, visualization, action, trajectories, Appendix, generated, task | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | AutoRT, system, leverages, existing, foundation, models, scale, deployment, operational, robots | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | process, takes, account, constraints, specified, constitutional, prompting, where, rules, about | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3. Place the napkin onto - extractive body cue:** For a breakdown of throughput by collect policy, or visualization of action trajectories, see Appendix I.
- **p. 5 / 3. Place the napkin onto - extractive body cue:** For each generated task, the LLM is asked to either output a collect policy or a reason to reject that task.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** AutoRT is, to the best of our knowledge, the first system where LLM-controlled robots are allowed to drive autonomously in real world settings, propose their ...
- **p. 7 / 3. Place the napkin onto - extractive body cue:** AutoRT generates language embeddings that are further apart. consider two different axes of diversity: visual diversity (how diverse are the collected trajectories visually), and language ...
- **p. 1 / ABSTRACT - extractive body cue:** Foundation models that incorporate language, vision, and more recently actions have revolutionized the ability to harness internet scale data to reason about useful tasks.
- **p. 1 / ABSTRACT - extractive body cue:** AutoRT leverages vision-language models (VLMs) for scene understanding and grounding, and further uses large language models (LLMs) for proposing diverse and novel instructions to be ...
- **p. 4 / 3. Place the napkin onto - extractive body cue:** A fourth category, the guidance rules, provides an input for an optional high-level human command: "The human command, which the robot should follow if given: ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | We demonstrate AutoRT proposing instructions to over 20 robots across multiple buildings and collecting 77k real robot episodes via both teleoperation and ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | AutoRT is such a hybrid approach, collecting both teleoperated and autonomous episodes based on supply of human supervision, with a focus on ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | We demonstrate AutoRT proposing instructions to over 20 robots across multiple buildings and collecting 77k real robot episodes via both teleoperation and ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Robot, episodes, first, embedded, visual, encoder, then, k-means, unsupervised, clustering, done, space, AutoRT, system, leverages, existing, foundation, models, scale, deployment.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | First, 5 test scenes were set up with objects that the robot should not interact with, including lifelike toy animals, sharp items, ... | p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto) |
| Coverage / augmentation | Figure 9: Hours of data collected per policy per day. We aimed for teleop collect throughput to exceed a simple 1 person:1 ... | p. 26 (Figure/Table caption), p. 10 (3. Place the napkin onto) |
| Downstream learning interface | Table 1: AutoRT data, split by collect policy used. Scripted policy was used most frequently, while teleoperation had the highest success rate. ... | p. 7 (Figure/Table caption), p. 9 (3. Place the napkin onto) |

## Failure and Ablation Link

- **p. 8 / 3. Place the napkin onto - extractive body cue:** 5.3 AFFORDANCE AND ROBOT CONSTITUTION In this section we study the effect of constitutional prompting and LLM self-critiquing on identifying safe and feasible tasks.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Effect of constitutional prompting on safety of proposed tasks Task Generation Unsafe prompting Minimal prompting Constitutional prompting Filter % Safe Recall
- **p. 9 / 3. Place the napkin onto - extractive body cue:** Adversarial Testing of Constitutional Prompting: To measure the effect of constitutional prompting, we set up deliberately adversarial scenes, and ablate our rules from the task ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 6: Tasks used to evaluate training ablations Task Group Tasks Picking pick utensil, pick office supplies, pick chips, pick bag, pick coffee cup, pick ...
- **p. 10 / 3. Place the napkin onto - extractive body cue:** Failures of perception such as hallucination of objects, lack of generalization to novel environments, and motion blur can introduce and propagate failures in the system.
- **p. 10 / 3. Place the napkin onto - extractive body cue:** Despite the promise of AutoRT, the current approach comes with a number of limitations.
- **p. 8 / 3. Place the napkin onto - extractive body cue:** How often does the LLM reject (or fail to reject) tasks that should be rejected?

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3. Place the napkin onto), p. 1 (ABSTRACT), p. 7 (3. Place the napkin onto), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3. Place the napkin onto), objective p. 2 (1 INTRODUCTION), p. 5 (3. Place the napkin onto), p. 5 (3. Place the napkin onto), p. 6 (3. Place the napkin onto), p. 7 (3. Place the napkin onto), p. 7 (3. Place the napkin onto), temporal p. 1 (ABSTRACT), p. 2 (2 RELATED WORK), p. 2 (1 INTRODUCTION), p. 3 (2 RELATED WORK), p. 4 (3. Place the napkin onto), p. 4 (3. Place the napkin onto).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
