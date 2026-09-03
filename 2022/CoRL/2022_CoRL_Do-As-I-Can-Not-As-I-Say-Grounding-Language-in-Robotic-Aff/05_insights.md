# Insights — Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2204.01691; PDF retrieval source: https://arxiv.org/pdf/2204.01691. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is capable ...
- **p. 2 / 1 Introduction - extractive body cue:** Our method, SayCan, extracts and leverages the knowledge within LLMs in physically-grounded tasks.
- **p. 1 / Abstract - extractive body cue:** We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are ...
- **p. 4 / 2 Preliminaries - extractive body cue:** With this approach, we are able to effectively extract knowledge from the language model, but it leaves a major issue: while the decoding of the ...
- **p. 6 / 2 Preliminaries - extractive body cue:** We test our method in two environments: a real office kitchen and a mock environment mirroring the kitchen, which is also the environment in which ...
- **p. 2 / 2 Preliminaries - extractive body cue:** Recent breakthroughs initiated by neural network-based Attention architectures [2] have enabled efficient scaling of so-called Large Language Models (LLMs).
- **p. 5 / 2 Preliminaries - extractive body cue:** To learn a language-conditioned RL policy, we use MT-Opt [14] in the Everyday Robots simulator using RetinaGAN sim-to-real transfer [16].
- **Contribution anchor:** p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries), p. 2 (2 Preliminaries)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** With prompt engineering, a LLM may be capable of splitting the high-level instruction into sub-tasks, but it cannot do so without the context of what ...
- **p. 2 / 1 Introduction - extractive body cue:** This question poses a major challenge.
- **p. 11 / 5.1 Results - extractive body cue:** As presented herein, SayCan only receives environmental feedback through value functions at the current decision step, meaning if a skill fails or the environment changes, ...
- **p. 3 / 2 Preliminaries - extractive body cue:** Assuming that a skill that succeeds makes progress on i with probability p(ℓπ/i) (i.e., its probability of being the right skill), and a skill that ...
- **p. 7 / 5.1 Results - extractive body cue:** Appendix E.6 shows additional rollouts with complex decisions, embodiment grounding, and long-horizon tasks in Figures 14-17 as well as failures in Figure 16.
- **p. 12 / 7 Related Work - extractive body cue:** Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation.
- **p. 12 / 7 Related Work - extractive body cue:** 8 Conclusions, Limitations and Future Work We presented SayCan, a method that enables leveraging and grounding the rich knowledge in large language models to complete ...
- **Boundary to test:** Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is capable of completing long-horizon, abstract, natural language instructions ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Reported outcome | Table 2: Success rates of instructions by family. PaLM-SayCan achieves a planning success rate of 84% and execution success rate of 74% in the training environment and 81% planning and 60% execution ... | p. 9 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Failure/limitation | Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation. | p. 12 (7 Related Work), p. 12 (7 Related Work) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 The goal of TD methods is to learn state or state-action value functions (Q-function) Qπ(s, a), which represents the discounted sum of rewards when starting from state s and action a, followed ...를 Therefore, to adapt language models to our problem statement, we must somehow inform them that we specifically want the high-level instruction to be broken down into sequences of available low-level skills.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is capable of completing long-horizon, abstract, natural language instructions ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `LLM, affordance, Planning, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The robot interacts with a large portion of the kitchen environment and successfully performs sequences of manipulation and navigation skills..
3. Compare against the body-reported baseline or a matched simpler baseline: We also find that PaLM outperforms FLAN..
4. Report the body metric and its denominator/aggregation: Table 2: Success rates of instructions by family. PaLM-SayCan achieves a planning success rate of 84% and execution success rate of 74% in the training environment and 81% planning and 60% execution ....
5. Re-run the body-reported ablation/failure condition: These tasks require PaLMSayCan to plan many steps without error and for the robot to navigate and interact with a significant portion of the kitchen..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 2 (2 Preliminaries), p. 5 (2 Preliminaries); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (5.1 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 evaluate, number, real-world mechanism이 We also find that PaLM outperforms FLAN. 대비 Table 2: Success rates of instructions by family. PaLM-SayCan achieves a planning success rate of 84% and execution ...을 개선하고, Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
