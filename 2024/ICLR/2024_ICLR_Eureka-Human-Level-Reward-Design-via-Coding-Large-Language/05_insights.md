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

- **Paper-specific interface:** Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code is that it exposes these environment variables, which ... (p. 3, 3 METHOD).
- **Paper-specific mechanism:** We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1. (p. 2, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is Figure 10: EUREKA reward functions enjoy improved sample efficiency compared to various baseline reward functions on aggregate over 20 Dexterity tasks. Additional Evaluation Metrics. In Fig. 11, we present holistic ... (p. 28, Figure/Table caption); the relevant task/metric cue is Averaged over all Isaac tasks, EUREKA without reward reflection reduces the average normalized score by 28.6%; in App. (p. 7, 4.3 RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** This skill requires the cooperation of two hands to ensure that the cap does not fall 1[dist > 0.03] CatchAbreast (422, 52) This class corresponds to the Catch Abreast task. (p. 19, B ENVIRONMENT DETAILS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, Reward Design, Large Language Model, NVIDIA`.
- **Reading predecessor in the generated track queue:** Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DrEureka: Language Model Guided Sim-To-Real Transfer (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 iterations on both benchmarks.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code is that it exposes these environment variables, which ... (p. 3, 3 METHOD); preserve the objective/update rule: Algorithm 1 EUREKA 1: Require: Task description l, environment code M, coding LLM LLM, fitness function F, initial prompt prompt 2: Hyperparameters: search iteration N, iteration batch size K 3: ... (p. 4, 3 METHOD).
2. Use the paper-reported task/data/environment cue: Our environments consist of 10 distinct robots and 29 tasks implemented using the IsaacGym simulator (Makoviychuk et al., 2021). (p. 5, 4 EXPERIMENTS).
3. Compare against the reported or matched baseline: This ablation helps study, given a fixed number of reward function budget, whether it is more advantageous to perform the EUREKA evolution or simply sample more first-attempt rewards without iterative ... (p. 7, 4.3 RESULTS).
4. Report the body metric with its denominator and aggregation: Averaged over all Isaac tasks, EUREKA without reward reflection reduces the average normalized score by 28.6%; in App. (p. 7, 4.3 RESULTS).
5. Re-run the reported ablation or stress/failure condition: This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 iterations on both benchmarks. (p. 7, 4.3 RESULTS); if none is reported, design one around: This skill requires the cooperation of two hands to ensure that the cap does not fall 1[dist > 0.03] CatchAbreast (422, 52) This class corresponds to the Catch Abreast task. (p. 19, B ENVIRONMENT DETAILS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), match the reported outcome at p. 28 (Figure/Table caption), p. 29 (Figure/Table caption), p. 7 (4.3 RESULTS), and measure the boundary at p. 19 (B ENVIRONMENT DETAILS), p. 7 (4.3 RESULTS).

## Falsifiable research question

Under the paper's stated interface (Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code ...), does the paper-specific mechanism (We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: ...) retain the reported evaluation outcome (Averaged over all Isaac tasks, EUREKA without reward reflection reduces the average normalized score by 28.6%; in App.) when tested against the paper's strongest explicit boundary (This skill requires the cooperation of two hands to ensure that the cap does not fall 1[dist > ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Averaged over all Isaac tasks, EUREKA without reward reflection reduces the average normalized score by 28.6%; in App.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (45 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1. (p. 2, 1 INTRODUCTION).
- **Paper-supported outcome:** Figure 10: EUREKA reward functions enjoy improved sample efficiency compared to various baseline reward functions on aggregate over 20 Dexterity tasks. Additional Evaluation Metrics. In Fig. 11, we present holistic ... (p. 28, Figure/Table caption).
- **Strongest explicit boundary:** This skill requires the cooperation of two hands to ensure that the cap does not fall 1[dist > 0.03] CatchAbreast (422, 52) This class corresponds to the Catch Abreast task. (p. 19, B ENVIRONMENT DETAILS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
