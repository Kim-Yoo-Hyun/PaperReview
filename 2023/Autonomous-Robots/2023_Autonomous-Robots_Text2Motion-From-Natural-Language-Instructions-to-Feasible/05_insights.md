# Insights — Text2Motion: From Natural Language Instructions to Feasible Plans

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.12153; PDF retrieval source: https://arxiv.org/pdf/2303.12153. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to solve ...
- **p. 5 / 4.2 Shooting-based planning - extractive body cue:** To this end, the first strategy we propose is a shooting-based Algorithm 1 Shooting-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP 2: function ...
- **p. 6 / 4.3 Search-based planning - extractive body cue:** We propose a second planner, greedy-search (see Figure 2, Right), which at each planning iteration ranks candidate skills predicted by the LLM and adds the ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are twofold: (i) a hybrid LLM planner that synergistically integrates shooting-based and search-based planning strategies to construct geometrically feasible plans for tasks not ...
- **p. 3 / 3.1 LLM and skill library - extractive body cue:** Each skill ψ consists of a policy π(a/s) and a parameterized manipulation primitive ϕ(a) [59], and is associated with a contextual bandit, or a single-timestep ...
- **p. 5 / 4.1 Goal prediction - extractive body cue:** We define a satisfaction function F G sat (s) : S →{0, 1} which takes as input a geometric state s and evaluates to 1 ...
- **p. 6 / 4.3 Search-based planning - extractive body cue:** We then compute the usefulness scores Sllm(ψk t ) by summing the token Algorithm 2 Search-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 5 (4.2 Shooting-based planning), p. 6 (4.3 Search-based planning), p. 2 (1 Introduction), p. 3 (3.1 LLM and skill library), p. 5 (4.1 Goal prediction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Such strategies are challenged in long-horizon settings, where the 1.
- **p. 3 / 3.1 LLM and skill library - extractive body cue:** If the skill succeeds, it receives a binary reward of r (or ¬r if it fails).
- **p. 4 / 3.2 The planning objective - extractive body cue:** If just one skill fails (reward ¬r), then the entire plan fails.
- **p. 1 / 1 Introduction - extractive body cue:** Such systems can generalize within the logical planning domain specified by experts.
- **p. 2 / 1 Introduction - extractive body cue:** Therefore, we ask in this paper: how can we verify the correctness and feasibility of LLM-generated plans prior to execution?
- **p. 11 / 6.1 Feasibility planning is required - extractive body cue:** Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with PAP tasks.
- **p. 9 / 5.5 Evaluation and metrics - extractive body cue:** Two failure cases are tracked: i) planning failure: the method does not produce a sequence of skills ψ1:H whose optimized parameters a∗ 1:H (Eq.
- **Boundary to test:** Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with PAP tasks.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to solve complex sequential manipulation tasks (Figure 1). | p. 2 (1 Introduction), p. 5 (4.2 Shooting-based planning) |
| Reported outcome | In the first two tasks (LH, Figure 5), we find that shooting achieves slightly higher success rates than greedy-search, while both methods achieve 100% success rates in the third task (LH + ... | p. 11 (6.2 Search-based reasoning is), p. 11 (6.2 Search-based reasoning is) |
| Failure/limitation | Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with PAP tasks. | p. 11 (6.1 Feasibility planning is required), p. 9 (5.5 Evaluation and metrics) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 We define a satisfaction function F G sat (s) : S →{0, 1} which takes as input a geometric state s and evaluates to 1 if any goal proposition g ∈G predicted ...를 Each skill ψ consists of a policy π(a/s) and a parameterized manipulation primitive ϕ(a) [59], and is associated with a contextual bandit, or a single-timestep Markov Decision Process (MDP): M = (S, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with PAP tasks.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to solve complex sequential manipulation tasks (Figure 1).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Planning and control`; tags: `Robotics, LLM planning, task and motion planning, feasibility, skill chaining`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with PAP tasks.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For example, Task 1 in Figure 4 requires the robot to pick and place three objects for a total of six skills..
3. Compare against the body-reported baseline or a matched simpler baseline: Top: Our method (Text2Motion) significantly outperforms all baselines on tasks involving partial affordance perception (Task 4, 5, 6)..
4. Report the body metric and its denominator/aggregation: Reported metrics: We report success rates and subgoal completion rates for all methods..
5. Re-run the body-reported ablation/failure condition: We use two pretrained language models, both of which were accessed through the OpenAI API: i) text-davinci-003, a variant of the InstructGPT [61] language model family which is finetuned from GPT-3 with ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (4.2 Shooting-based planning), p. 5 (4.1 Goal prediction), p. 6 (4.3 Search-based planning); the primary result is directionally consistent at p. 11 (6.2 Search-based reasoning is), p. 11 (6.2 Search-based reasoning is), p. 10 (6.1 Feasibility planning is required); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Text2Motion, language-based, planning mechanism이 Top: Our method (Text2Motion) significantly outperforms all baselines on tasks involving partial affordance perception (Task 4, ... 대비 Reported metrics: We report success rates and subgoal completion rates for all methods.을 개선하고, Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
