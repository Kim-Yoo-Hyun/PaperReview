# Evaluation - Eureka: Human-Level Reward Design via Coding Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IEduRUO55F; PDF retrieval source: https://openreview.net/forum?id=IEduRUO55F. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 29 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (4.3 RESULTS), p. 29 (Figure/Table caption), p. 28 (Figure/Table caption), p. 7 (4.3 RESULTS)): Figure 12: EUREKA reward functions' improvement over alternative reward functions are statistically significant. Dexterity Performance Breakdown. We present the raw success rates of EUREKA, L2R, Human, and Sparse in Fig. ...

## Evaluation Body Digest

- **p. 5 / 4 EXPERIMENTS - extractive body cue:** In addition to coverage over robot form factors, we ensure depth in our evaluation by including all 20 tasks from the Bidexterous Manipulation (Dexterity) benchmark ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Our environments consist of 10 distinct robots and 29 tasks implemented using the IsaacGym simulator (Makoviychuk et al., 2021).
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** These are the original shaped reward functions provided in our benchmark tasks.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Like Human, these are also provided by the benchmark.
- **p. 7 / 4.3 RESULTS - extractive body cue:** As seen, on both benchmarks, EUREKA rewards steadily improve and eventually surpass human rewards in performance despite sub-par initial performances.
- **p. 7 / 4.3 RESULTS - extractive body cue:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 ...
- **p. 8 / 4.3 RESULTS - extractive body cue:** We study whether starting with a human reward function initialization, a common scenario in real-world RL applications, is advantageous for EUREKA.
- **p. 8 / 4.3 RESULTS - extractive body cue:** This task is highly dynamic and requires a Shadow Hand to continuously rotate a pen to achieve some pre-defined spinning patterns for as many cycles ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 5); 4.3 RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 12: EUREKA reward functions' improvement over alternative reward functions are statistically significant. Dexterity Performance Breakdown. We present the raw success rates of EUREKA, ... | p. 29 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2: EUREKA takes unmodified environment source code and language task description as context to zero-shot generate executable reward functions from a coding LLM. ... | p. 2 (Figure/Table caption) |
| 4.3 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, the fact that EUREKA can significantly improve over human rewards even when they are highly sub-optimal hints towards an interesting hypothesis: human designers ... | p. 8 (4.3 RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 13: Raw success rates of all methods on the Dexterity benchmark. Reward Reflection Ablations. In Fig. 14, we provide a detailed per-task breakdown ... | p. 29 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 10: EUREKA reward functions enjoy improved sample efficiency compared to various baseline reward functions on aggregate over 20 Dexterity tasks. Additional Evaluation Metrics. ... | p. 28 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4 EXPERIMENTS - extractive body cue:** In addition to coverage over robot form factors, we ensure depth in our evaluation by including all 20 tasks from the Bidexterous Manipulation (Dexterity) benchmark ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Our environments consist of 10 distinct robots and 29 tasks implemented using the IsaacGym simulator (Makoviychuk et al., 2021).
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** These are the original shaped reward functions provided in our benchmark tasks.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Like Human, these are also provided by the benchmark.
- **p. 7 / 4.3 RESULTS - extractive body cue:** As seen, on both benchmarks, EUREKA rewards steadily improve and eventually surpass human rewards in performance despite sub-par initial performances.
- **p. 7 / 4.3 RESULTS - extractive body cue:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 ...
- **p. 8 / 4.3 RESULTS - extractive body cue:** We study whether starting with a human reward function initialization, a common scenario in real-world RL applications, is advantageous for EUREKA.
- **p. 8 / 4.3 RESULTS - extractive body cue:** This task is highly dynamic and requires a Shadow Hand to continuously rotate a pen to achieve some pre-defined spinning patterns for as many cycles ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: EUREKA generates human-level reward functions across diverse robots and tasks. Combined with curriculum learning, EUREKA for the first time, unlocks rapid pen-spinning capabilities ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: EUREKA takes unmodified environment source code and language task description as context to zero-shot generate executable reward functions from a coding LLM. Then, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: EUREKA can zero-shot generate executable rewards and then flexibly improve them with many distinct types of free-form modification, such as (1) changing the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. This iterative optimization continues until a specified number of iterations has been reached. Finally, we perform multiple random restarts to find better maxima; ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: EUREKA outperforms Human and L2R across all tasks. In particular, EUREKA realizes much greater gains on high-dimensional dexterity environments. about these tasks, making ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: EUREKA progressively produces better rewards via in- context evolutionary reward search. EUREKA consistently improves over time. In Fig. 5, we visualize the average ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Eureka generates novel rewards. EUREKA generates novel rewards. We assess the nov- elty of EUREKA rewards by computing the correlations between EUREKA and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Eureka fine-tuning quickly adapts the policy to successfully spin the pen for many cycles in a row; see project website for videos. In ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In addition to coverage over robot form factors, we ensure depth in our evaluation by including all 20 tasks from the Bidexterous Manipulation (Dexterity) ... | embodiment, simulator version and control stack | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Task/environment | Our environments consist of 10 distinct robots and 29 tasks implemented using the IsaacGym simulator (Makoviychuk et al., 2021). | reset, timeout, object/scene variation | p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 3 (3 METHOD), p. 4 (3 METHOD) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 5 (3 METHOD), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 13: Raw success rates of all methods on the Dexterity benchmark. Reward Reflection Ablations. In Fig. 14, we provide a detailed per-task breakdown ... | definition/direction/unit from same section | p. 29 (Figure/Table caption) |
| Table 3: L2R reward primitives and their implementations. v(q) denotes the vector part of quaternion q, subscript t denotes target value, and n denotes ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Figure 12: EUREKA reward functions' improvement over alternative reward functions are statistically significant. Dexterity Performance Breakdown. We present the raw success rates of EUREKA, ... | definition/direction/unit from same section | p. 29 (Figure/Table caption) |
| For Dexterity, since all tasks are evaluated using the binary success function, we directly report success rates. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Averaged over all Isaac tasks, EUREKA without reward reflection reduces the average normalized score by 28.6%; in App. | definition/direction/unit from same section | p. 7 (4.3 RESULTS) |
| Then, we plot the correlations against the human normalized scores on a scatter-plot in Figure 6, where each point represents a single EUREKA reward ... | definition/direction/unit from same section | p. 7 (4.3 RESULTS) |
| We thoroughly evaluate EUREKA on a diverse suite of robot embodiments and tasks, testing its ability to generate reward functions, solve new tasks, and ... | definition/direction/unit from same section | p. 5 (4 EXPERIMENTS) |
| These are identical to the fitness functions F that we use to evaluate the quality of the generated rewards. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: EUREKA outperforms Human and L2R across all tasks. In particular, EUREKA realizes much greater gains on high-dimensional dexterity environments. about these tasks, ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 10: EUREKA reward functions enjoy improved sample efficiency compared to various baseline reward functions on aggregate over 20 Dexterity tasks. Additional Evaluation Metrics. ... | comparison identity and matched condition | p. 28 (Figure/Table caption) |
| Published as a conference paper at ICLR 2024 Figure 4: EUREKA outperforms Human and L2R across all tasks. | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| As shown, EUREKA mostly generates weakly correlated reward functions that outperform the human ones. | comparison identity and matched condition | p. 7 (4.3 RESULTS) |
| This ablation helps study, given a fixed number of reward function budget, whether it is more advantageous to perform the EUREKA evolution or simply ... | comparison identity and matched condition | p. 7 (4.3 RESULTS) |
| To demonstrate the importance of curriculum learning, we also directly train a policy from scratch on the target task using EUREKA reward without the ... | comparison identity and matched condition | p. 8 (4.3 RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This ablation helps study, given a fixed number of reward function budget, whether it is more advantageous to perform the EUREKA evolution or simply ... | component/input/data sensitivity | p. 7 (4.3 RESULTS) |
| This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after ... | component/input/data sensitivity | p. 7 (4.3 RESULTS) |
| We use GPT-4 (OpenAI, 2023), in particular the gpt-4-0314 variant, as the backbone LLM for all LLM-based reward-design algorithms unless specified otherwise. | component/input/data sensitivity | p. 5 (4 EXPERIMENTS) |
| Isaac and Dexterity share a well-tuned PPO implementation (Schulman et al., 2017; Makoviichuk & Makoviychuk, 2021), and we use this implementation and the task-specific ... | component/input/data sensitivity | p. 6 (4 EXPERIMENTS) |
| To demonstrate the importance of curriculum learning, we also directly train a policy from scratch on the target task using EUREKA reward without the ... | component/input/data sensitivity | p. 8 (4.3 RESULTS) |
| This task is highly dynamic and requires a Shadow Hand to continuously rotate a pen to achieve some pre-defined spinning patterns for as many ... | component/input/data sensitivity | p. 8 (4.3 RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1. | Figure 12: EUREKA reward functions' improvement over alternative reward functions are statistically significant. Dexterity Performance Breakdown. We present the raw success rates of EUREKA, ... | PDF body cue; verify exact table/figure and matched conditions | p. 29 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (4.3 RESULTS), p. 29 (Figure/Table caption), p. 28 (Figure/Table caption), p. 7 (4.3 RESULTS) |
| Primary metric/result | Figure 2: EUREKA takes unmodified environment source code and language task description as context to zero-shot generate executable reward functions from a coding LLM. ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Our environments consist of 10 distinct robots and 29 tasks implemented using the IsaacGym simulator (Makoviychuk et al., 2021).
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** In addition to coverage over robot form factors, we ensure depth in our evaluation by including all 20 tasks from the Bidexterous Manipulation (Dexterity) benchmark ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Dexterity contains 20 complex bi-manual tasks that require a pair of Shadow Hands to solve a wide range of complex manipulation skills, ranging from object ...
- **p. 6 / 4.3 RESULTS - extractive body cue:** Notably, EUREKA exceeds or performs on par to human level on all Isaac tasks and 15 out of 20 tasks on Dexterity (see App.
- **p. 7 / 4.3 RESULTS - extractive body cue:** Evolution (32 Samples), which performs only the initial reward generation step, sampling the same number of reward functions as two iterations in the original EUREKA.
- **p. 5 / 3 METHOD - extractive body cue:** In all our experiments, EUREKA conducts 5 independent runs per environment, and for each run, searches for 5 iterations with K = 16 samples per ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after ... | p. 7 (4.3 RESULTS) |
| body limitation/failure cue | Figure 3: EUREKA can zero-shot generate executable rewards and then flexibly improve them with many distinct types of free-form modification, such as (1) changing ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Furthermore, we ablate GPT-4 with GPT-3.5 and find EUREKA degrades in performance but still matches or exceeds human-level on most Isaac tasks, indicating that ... | p. 7 (4.3 RESULTS) |
| body limitation/failure cue | Figure 14: EUREKA without the reward reflection mechanism exhibits degraded performance. EUREKA with GPT-3.5. In Fig. 15, we compare the performance of EUREKA with ... | p. 30 (Figure/Table caption) |
| body limitation/failure cue | Figure 15: Using GPT3.5 observes performance degradation in EUREKA but still remains comparable to GPT-4 on a majority of the tasks. Reward Correlation Experiments. ... | p. 30 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Algorithm 1 EUREKA 1: Require: Task description l, environment code M, coding LLM LLM, fitness function F, initial prompt prompt 2: Hyperparameters: search iteration ... | p. 4 (3 METHOD) |
| Isaac and Dexterity share a well-tuned PPO implementation (Schulman et al., 2017; Makoviichuk & Makoviychuk, 2021), and we use this implementation and the task-specific ... | p. 6 (4 EXPERIMENTS) |
| For each final reward function obtained from each method, we run 5 independent PPO training runs and report the average of the maximum task ... | p. 6 (4 EXPERIMENTS) |
| In a few cases, EUREKA rewards are even negatively correlated with human rewards but perform significantly better, demonstrating that EUREKA can discover novel reward ... | p. 7 (4.3 RESULTS) |
| G.3, we provide several examples of EUREKA (Human Init.) steps. | p. 8 (4.3 RESULTS) |
| We investigate this capability in EUREKA by teaching a Humanoid agent how to run purely from textual reward reflection; in App. | p. 9 (4.3 RESULTS) |
| 1 for pseudocode; all prompts are included in App. | p. 3 (3 METHOD) |
| In cases where the source code is not available, relevant state information can also be supplied via 3 | p. 3 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.3 RESULTS - extractive body cue:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: EUREKA can zero-shot generate executable rewards and then flexibly improve them with many distinct types of free-form modification, such as (1) changing the ...
- **p. 7 / 4.3 RESULTS - extractive body cue:** Furthermore, we ablate GPT-4 with GPT-3.5 and find EUREKA degrades in performance but still matches or exceeds human-level on most Isaac tasks, indicating that its ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 14: EUREKA without the reward reflection mechanism exhibits degraded performance. EUREKA with GPT-3.5. In Fig. 15, we compare the performance of EUREKA with GPT- ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 15: Using GPT3.5 observes performance degradation in EUREKA but still remains comparable to GPT-4 on a majority of the tasks. Reward Correlation Experiments. To ...

- **PDF anchors reviewed:** datasets p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4.3 RESULTS), p. 7 (4.3 RESULTS), metrics p. 29 (Figure/Table caption), p. 22 (Figure/Table caption), p. 29 (Figure/Table caption), p. 6 (4 EXPERIMENTS), p. 7 (4.3 RESULTS), p. 7 (4.3 RESULTS), baselines p. 6 (Figure/Table caption), p. 28 (Figure/Table caption), p. 6 (4 EXPERIMENTS), p. 7 (4.3 RESULTS), p. 7 (4.3 RESULTS), p. 8 (4.3 RESULTS), results p. 29 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (4.3 RESULTS), p. 29 (Figure/Table caption), p. 28 (Figure/Table caption), p. 7 (4.3 RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
