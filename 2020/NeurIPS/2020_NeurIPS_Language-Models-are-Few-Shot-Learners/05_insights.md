# Insights — Language Models are Few-Shot Learners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (75 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2005.14165; PDF retrieval source: https://arxiv.org/pdf/2005.14165. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 7 / 2 Approach - extractive body cue:** The panels above show four methods for performing a task with a language model - fine-tuning is the traditional method, whereas zero-, one-, and few-shot, ...
- **p. 5 / 1 Introduction - extractive body cue:** Specifically, we evaluate GPT-3 on over two dozen NLP datasets, as well as several novel tasks designed to test rapid adaptation to tasks unlikely to ...
- **p. 5 / 1 Introduction - extractive body cue:** GPT-3 also displays one-shot and few-shot proficiency at tasks designed to test rapid adaption or on-the-fly reasoning, which include unscrambling words, performing arithmetic, and using ...
- **p. 4 / 1 Introduction - extractive body cue:** We show in-context learning performance on a simple task requiring the model to remove random symbols from a word, both with and without a natural ...
- **p. 6 / 1 Introduction - extractive body cue:** In Section 2, we describe our approach and methods for training GPT-3 and evaluating it.
- **p. 8 / 2 Approach - extractive body cue:** 2.1 Model and Architectures We use the same model and architecture as GPT-2 [RWC+19], including the modified initialization, pre-normalization, and reversible tokenization described therein, with ...
- **p. 9 / 2 Approach - extractive body cue:** To train the larger models without running out of memory, we use a mixture of model parallelism within each matrix multiply and model parallelism across ...
- **Contribution anchor:** p. 7 (2 Approach), p. 5 (1 Introduction), p. 5 (1 Introduction), p. 4 (1 Introduction), p. 6 (1 Introduction), p. 8 (2 Approach)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** However, a major limitation to this approach is that while the architecture is task-agnostic, there is still a need for task-specific datasets and task-specific fine-tuning: ...
- **p. 4 / 1 Introduction - extractive body cue:** Aside from pointing to a conceptual limitation in our current NLP techniques, this adaptability has practical advantages - it allows humans to seamlessly mix together ...
- **p. 5 / 1 Introduction - extractive body cue:** We also show that in the few-shot setting, GPT-3 can generate synthetic news articles which human evaluators have difficulty distinguishing from human-generated articles.
- **p. 3 / 1 Introduction - extractive body cue:** Removing this limitation would be desirable, for several reasons.
- **p. 5 / 1 Introduction - extractive body cue:** By presenting a broad characterization of GPT-3's strengths and weaknesses, including these limitations, we hope to stimulate study of few-shot learning in language models and ...
- **p. 33 / 3 Results - extractive body cue:** An important limitation of our contamination analysis is that we cannot be sure that the clean subset is drawn from the same distribution as the ...
- **p. 41 / 8 Conclusion - extractive body cue:** Despite many limitations and weaknesses, these results suggest that very large language models may be an important ingredient in the development of adaptable, general language ...
- **Boundary to test:** An important limitation of our contamination analysis is that we cannot be sure that the clean subset is drawn from the same distribution as the original dataset.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The panels above show four methods for performing a task with a language model - fine-tuning is the traditional method, whereas zero-, one-, and few-shot, which we study in this work, require ... | p. 7 (2 Approach), p. 5 (1 Introduction) |
| Reported outcome | GPT-3 significantly improves SOTA on LAMBADA while achieving respectable performance on two difficult completion prediction datasets. a[Tur20] b[RWC+19] c[LDL19] d[LCH+20] Figure 3.2: On LAMBADA, the few-shot capability of language mode ... | p. 12 (3 Results), p. 16 (Figure/Table caption) |
| Failure/limitation | An important limitation of our contamination analysis is that we cannot be sure that the clean subset is drawn from the same distribution as the original dataset. | p. 33 (3 Results), p. 41 (8 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `논문이 명시한 observation과 task input → task state 또는 decision variable → paper-specific output/action`.
- 이 논문의 재사용 가능한 지점은 Recent work [RWC+19] attempts to do this via what we call "in-context learning", using the text input of a pretrained language model as a form of task specification: the model is conditioned ...를 Exact phrasings for all task descriptions, examples and prompts can be found in Appendix G. • Zero-Shot (0S) is the same as one-shot except that no demonstrations are allowed, and the model ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 task state 또는 decision variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 An important limitation of our contamination analysis is that we cannot be sure that the clean subset is drawn from the same distribution as the original dataset.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The panels above show four methods for performing a task with a language model - fine-tuning is the traditional method, whereas zero-, one-, and few-shot, which we study in this work, require ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Foundations: Vision and Language Models`; tags: `LLM, in-context learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** An important limitation of our contamination analysis is that we cannot be sure that the clean subset is drawn from the same distribution as the original dataset.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We omit the 4 Wikipedia-related tasks in that work because they are entirely contained in our training data, and we also omit the one-billion word benchmark due to a high fraction of ....
3. Compare against the body-reported baseline or a matched simpler baseline: On DROP [DWD+19], a dataset testing discrete reasoning and numeracy in the context of reading comprehension, GPT-3 in a few-shot setting outperforms the fine-tuned BERT baseline from the original paper but is ....
4. Report the body metric and its denominator/aggregation: All scores are F1 except results for RACE which report accuracy. a[JZC+19] b[JN20] c[AI19] d[QIA20] e[SPP+19] fine-tuned RoBERTa..
5. Re-run the body-reported ablation/failure condition: Figure 1.2: Larger models make increasingly efficient use of in-context information. We show in-context learning performance on a simple task requiring the model to remove random symbols from a word, both with ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 8 (2 Approach), p. 9 (2 Approach), p. 6 (2 Approach); the primary result is directionally consistent at p. 12 (3 Results), p. 16 (Figure/Table caption), p. 11 (3 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 panels, above, four mechanism이 On DROP [DWD+19], a dataset testing discrete reasoning and numeracy in the context of reading comprehension, ... 대비 All scores are F1 except results for RACE which report accuracy. a[JZC+19] b[JN20] c[AI19] d[QIA20] e[SPP+19] fine-tuned RoBERTa.을 개선하고, An important limitation of our contamination analysis is that we cannot be sure that the clean ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
