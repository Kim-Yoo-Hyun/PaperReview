# Insights — Eureka: Human-Level Reward Design via Coding Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IEduRUO55F; PDF retrieval source: https://openreview.net/forum?id=IEduRUO55F. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1.
- **p. 3 / 3 METHOD - extractive body cue:** EUREKA consists of three algorithmic components: 1) environment as context that enables zero-shot generation of executable rewards, 2) evolutionary search that iteratively proposes and refines ...
- **p. 3 / 3 METHOD - extractive body cue:** We propose directly feeding the raw environment source code (without the reward code, if exists) as context.
- **p. 5 / 3 METHOD - extractive body cue:** We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Enables a new gradient-free in-context learning approach to reinforcement learning from human feedback (RLHF) that can generate more performant and human-aligned reward functions 2
- **p. 4 / 3 METHOD - extractive body cue:** In practice, to ensure that the environment code fits within the LLM's context window and does not leak simulation internals (so that we can expect ...
- **p. 3 / 3 METHOD - extractive body cue:** Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code is that it ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 3 (3 METHOD), p. 5 (3 METHOD), p. 2 (1 INTRODUCTION), p. 4 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 PROBLEM SETTING AND DEFINITIONS The goal of reward design is to return a shaped reward function for a ground-truth reward function that may be ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, it iterates between reward sampling, GPU-accelerated reward evaluation, and reward reflection to progressively improve its reward outputs. domain expertise to construct task prompts or ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Despite their fundamental importance, reward functions are known to be notoriously difficult to design in practice (Russell & Norvig, 1995; Sutton & Barto, 2018); a ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing attempts require substantial Figure 1: EUREKA generates human-level reward functions across diverse robots and tasks.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Large Language Models (LLMs) have excelled as high-level semantic planners for robotics tasks (Ahn et al., 2022; Singh et al., 2023), but whether they can ...
- **p. 7 / 4.3 RESULTS - extractive body cue:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: EUREKA can zero-shot generate executable rewards and then flexibly improve them with many distinct types of free-form modification, such as (1) changing the ...
- **Boundary to test:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 iterations on both benchmarks.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1. | p. 2 (1 INTRODUCTION), p. 3 (3 METHOD) |
| Reported outcome | Figure 12: EUREKA reward functions' improvement over alternative reward functions are statistically significant. Dexterity Performance Breakdown. We present the raw success rates of EUREKA, L2R, Human, and Sparse in Fig. 13. | p. 29 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Failure/limitation | This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 iterations on both benchmarks. | p. 7 (4.3 RESULTS), p. 4 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code is that it exposes these environment variables, which is easy ...를 In practice, to ensure that the environment code fits within the LLM's context window and does not leak simulation internals (so that we can expect the same prompt to generalize to new ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 iterations on both benchmarks.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, Reward Design, Large Language Model, NVIDIA`.
- **Reading predecessor in the generated track queue:** Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DrEureka: Language Model Guided Sim-To-Real Transfer (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 iterations on both benchmarks.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In addition to coverage over robot form factors, we ensure depth in our evaluation by including all 20 tasks from the Bidexterous Manipulation (Dexterity) benchmark (Chen et al., 2022)..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 4: EUREKA outperforms Human and L2R across all tasks. In particular, EUREKA realizes much greater gains on high-dimensional dexterity environments. about these tasks, making them ideal testbeds for assessing EUREKA's reward ....
4. Report the body metric and its denominator/aggregation: Figure 13: Raw success rates of all methods on the Dexterity benchmark. Reward Reflection Ablations. In Fig. 14, we provide a detailed per-task breakdown on the impact of removing reward reflection in ....
5. Re-run the body-reported ablation/failure condition: This ablation helps study, given a fixed number of reward function budget, whether it is more advantageous to perform the EUREKA evolution or simply sample more first-attempt rewards without iterative improvement..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD); the primary result is directionally consistent at p. 29 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (4.3 RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, Evolution-driven, Universal mechanism이 Figure 4: EUREKA outperforms Human and L2R across all tasks. In particular, EUREKA realizes much greater ... 대비 Figure 13: Raw success rates of all methods on the Dexterity benchmark. Reward Reflection Ablations. In Fig. 14, ...을 개선하고, This consistent improvement also cannot be replaced by just sampling more in the first iteration as ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
