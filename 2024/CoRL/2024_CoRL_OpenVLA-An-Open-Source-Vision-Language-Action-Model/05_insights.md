# Insights — OpenVLA: An Open-Source Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/kim25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.
- **p. 2 / 1 Introduction - extractive body cue:** OpenVLA consists of a pretrained visuallyconditioned language model backbone that captures visual features at multiple granularities, fine-tuned on a large, diverse dataset of 970k robot ...
- **p. 3 / 1 Introduction - extractive body cue:** As a final contribution, we open-source all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale, with the hope that ...
- **p. 3 / 1 Introduction - extractive body cue:** of compute efficient fine-tuning methods leveraging low-rank adaptation [LoRA; 25] and model quantization [26] to facilitate adapting OpenVLA models on consumer-grade GPUs instead of large ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** While reproducing this scale of pretraining for robotics is still an open challenge - even the largest robot manipulation datasets [1, 11] only have 100K ...
- **p. 2 / 1 Introduction - extractive body cue:** A key weakness of learned policies for robotic manipulation is their inability to generalize beyond their training data: while existing policies trained for individual skills ...
- **p. 8 / 7.0 GB - extractive body cue:** The current OpenVLA model has several limitations.
- **p. 8 / 7.0 GB - extractive body cue:** 5 Conclusion and Limitations In this work, we presented OpenVLA, a state-of-the-art, open-source vision-language-action model that obtains strong performance for cross-embodiment robot control out-of-the-box.
- **p. 32 / Figure/Table caption - extractive body cue:** Table 10: Fine-tuned vs. frozen vision encoder experiment results. We evaluate the performance of fine-tuning ("Fine-Tuned") vs. freezing the vision encoder ("Frozen Vision") in two ...
- **p. 7 / 4 Experiments - extractive body cue:** Additionally, we evaluate Octo [5] fine-tuned on the target dataset (RT-2-X does not support fine-tuning).
- **p. 6 / 4 Experiments - extractive body cue:** We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when distractors are present.
- **Boundary to test:** The current OpenVLA model has several limitations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 3: Bridge V2 WidowX evaluation task categories and results. We evaluate OpenVLA and prior state-of- the-art generalist robot policies on a comprehensive suite of tasks covering several axes of generalization, as ... | p. 6 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Failure/limitation | The current OpenVLA model has several limitations. | p. 8 (7.0 GB), p. 8 (7.0 GB) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Abstract: Large policies pretrained on a combination of Internet-scale visionlanguage data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new ... (p. 1, Body text (section boundary not confidently recovered)).
- **Paper-specific mechanism:** To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 4: Google robot evaluation results. We evaluate generalist robot policies on in-distribution and out-of- distribution (OOD) tasks on the mobile manipulator used in RT-1 and RT-2 evaluations [2, 7]. ... (p. 6, Figure/Table caption); the relevant task/metric cue is Notably, prior works achieve strong performance only in either precise or diverse tasks, resulting in widely varying success rates. (p. 7, 4 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when distractors are present. (p. 6, 4 Experiments).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `VLA and generalist robot policies`; tags: `VLA, Robotics, Imitation Learning`.
- **Reading predecessor in the generated track queue:** Octo: An Open-Source Generalist Robot Policy (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** π0: A Vision-Language-Action Flow Model for General Robot Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The current OpenVLA model has several limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Abstract: Large policies pretrained on a combination of Internet-scale visionlanguage data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new ... (p. 1, Body text (section boundary not confidently recovered)); preserve the objective/update rule: OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. (p. 1, Body text (section boundary not confidently recovered)).
2. Use the paper-reported task/data/environment cue: (2) Can OpenVLA be effectively fine-tuned on a new robot setup and task, and how does it compare to state-of-the-art data-efficient imitation learning approaches? (p. 5, 4 Experiments).
3. Compare against the reported or matched baseline: (2) Can OpenVLA be effectively fine-tuned on a new robot setup and task, and how does it compare to state-of-the-art data-efficient imitation learning approaches? (p. 5, 4 Experiments).
4. Report the body metric with its denominator and aggregation: Notably, prior works achieve strong performance only in either precise or diverse tasks, resulting in widely varying success rates. (p. 7, 4 Experiments).
5. Re-run the reported ablation or stress/failure condition: See Appendix F for ablation analyses of these components. (p. 7, 4 Experiments); if none is reported, design one around: We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when distractors are present. (p. 6, 4 Experiments).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 25 (Figure/Table caption), and measure the boundary at p. 6 (4 Experiments), p. 8 (7.0 GB).

## Falsifiable research question

Under the paper's stated interface (Abstract: Large policies pretrained on a combination of Internet-scale visionlanguage data and diverse robot demonstrations have the potential to change how we ...), does the paper-specific mechanism (To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation ...) retain the reported evaluation outcome (Notably, prior works achieve strong performance only in either precise or diverse tasks, resulting in widely varying success ...) when tested against the paper's strongest explicit boundary (We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Notably, prior works achieve strong performance only in either precise or diverse tasks, resulting in widely varying success ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies. (p. 2, 1 Introduction).
- **Paper-supported outcome:** Figure 4: Google robot evaluation results. We evaluate generalist robot policies on in-distribution and out-of- distribution (OOD) tasks on the mobile manipulator used in RT-1 and RT-2 evaluations [2, 7]. ... (p. 6, Figure/Table caption).
- **Strongest explicit boundary:** We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when distractors are present. (p. 6, 4 Experiments).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
