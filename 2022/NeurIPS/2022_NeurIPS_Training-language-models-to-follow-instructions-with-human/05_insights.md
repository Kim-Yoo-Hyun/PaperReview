# Insights — Training language models to follow instructions with human feedback

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (68 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.02155; PDF retrieval source: https://arxiv.org/pdf/2203.02155. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** See Section 3 for more details on our method. sizes (1.3B, 6B, and 175B parameters), and all of our models use the GPT-3 architecture.
- **p. 4 / 1 Introduction - extractive body cue:** The rest of this paper is structured as follows: We first detail related work in Section 2, before diving into our method and experiment details ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.
- **p. 1 / Abstract - extractive body cue:** We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.
- **p. 2 / 1 Introduction - extractive body cue:** We mainly evaluate our models by having our labelers rate the quality of model outputs on our test set, consisting of prompts from held-out customers ...
- **p. 2 / 1 Introduction - extractive body cue:** Our InstructGPT models (PPO-ptx) as well as its variant trained without pretraining mix (PPO) significantly outperform the GPT-3 baselines (GPT, GPT prompted); outputs from our ...
- **p. 4 / 1 Introduction - extractive body cue:** To test the generalization of our models, we conduct a preliminary experiment with held-out labelers, and find that they prefer InstructGPT outputs to outputs from ...
- **Contribution anchor:** p. 3 (1 Introduction), p. 4 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 4 / 1 Introduction - extractive body cue:** Finally we give an extended discussion of our work in Section 5, including implications for alignment research (5.1), what we are aligning to (5.2), limitations ...
- **p. 1 / 1 Introduction - extractive body cue:** Current affiliations: AA: Anthropic; PC: Alignment Research Center.
- **p. 4 / 1 Introduction - extractive body cue:** Our models generalize to the preferences of "held-out" labelers that did not produce any training data.
- **p. 20 / 5 Discussion - extractive body cue:** In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations.
- **p. 18 / 5 Discussion - extractive body cue:** We then consider areas for improvement before a larger discussion of the limitations of our work in Section 5.3.
- **p. 18 / 5 Discussion - extractive body cue:** the real world with customers.10 This enables an important feedback loop on the techniques' effectiveness and limitations.
- **p. 19 / 5 Discussion - extractive body cue:** Perhaps the greatest limitation of our models is that, in most cases, they follow the user's instruction, even if that could lead to harm in ...
- **Boundary to test:** In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | See Section 3 for more details on our method. sizes (1.3B, 6B, and 175B parameters), and all of our models use the GPT-3 architecture. | p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Reported outcome | When evaluated only on prompts that were not adversarially selected against GPT-3, our PPO models are still significantly more truthful and informative than GPT-3 (although the absolute improvement decreases by a couple ... | p. 13 (4 Results), p. 12 (4 Results) |
| Failure/limitation | In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations. | p. 20 (5 Discussion), p. 18 (5 Discussion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `논문이 명시한 observation과 task input → task state 또는 decision variable → paper-specific output/action`.
- 이 논문의 재사용 가능한 지점은 Training language models to follow instructions with human feedback Long Ouyang∗ Jeff Wu∗ Xu Jiang∗ Diogo Almeida∗ Carroll L.를 We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 task state 또는 decision variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: See Section 3 for more details on our method. sizes (1.3B, 6B, and 175B parameters), and all of our models use the GPT-3 architecture.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Foundations: Vision and Language Models`; tags: `LLM, instruction tuning, alignment`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Second, it can be difficult for public NLP datasets to obtain a very high diversity of inputs (at least, on the kinds of inputs that real-world users would be interested in using)..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those from the 175B SFT model. Our InstructGPT models ....
4. Report the body metric and its denominator/aggregation: Figure 13: Tuning FLAN and T0 based on reward model scores batch size of 64, a learning rate of 6e-6 and 1 million examples. Once again using the reward model score, we ....
5. Re-run the body-reported ablation/failure condition: Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those from the 175B SFT model. Our InstructGPT models ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction); the primary result is directionally consistent at p. 13 (4 Results), p. 12 (4 Results), p. 13 (4 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 See, Section, more mechanism이 Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often ... 대비 Figure 13: Tuning FLAN and T0 based on reward model scores batch size of 64, a learning rate ...을 개선하고, In the longer term, alignment failures could lead to more severe consequences, particularly if these models ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
