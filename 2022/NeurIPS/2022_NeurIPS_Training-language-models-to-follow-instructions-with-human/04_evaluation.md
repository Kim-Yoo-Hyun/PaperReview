# Evaluation - Training language models to follow instructions with human feedback

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (68 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.02155; PDF retrieval source: https://arxiv.org/pdf/2203.02155. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (4 Results), p. 12 (4 Results), p. 13 (4 Results), p. 2 (Figure/Table caption), p. 11 (4 Results), p. 11 (4 Results)): When evaluated only on prompts that were not adversarially selected against GPT-3, our PPO models are still significantly more truthful and informative than GPT-3 (although the absolute improvement decreases by ...

## Evaluation Body Digest

- **p. 13 / 4 Results - extractive body cue:** Second, it can be difficult for public NLP datasets to obtain a very high diversity of inputs (at least, on the kinds of inputs that ...
- **p. 12 / 4 Results - extractive body cue:** We ran an experiment where we split our labelers into 5 groups, and train 5 RMs (with 3 different seeds) using 5-fold cross validation (training ...
- **p. 13 / 4 Results - extractive body cue:** First, public NLP datasets are designed to capture tasks that are easy to evaluate with automatic metrics, such as classification, question answering, and to a ...
- **p. 15 / 4 Results - extractive body cue:** In Figure 33, we show that there is a value of the pretraining mix coefficient that both reverses the performance regressions on SQuADv2 and DROP ...
- **p. 10 / 4 Results - extractive body cue:** In this section, we provide experimental evidence for our claims in Section 1, sorted into three parts: results on the API prompt distribution, results on ...
- **p. 12 / 4 Results - extractive body cue:** Public NLP datasets are not reflective of how our language models are used.
- **p. 14 / 4 Results - extractive body cue:** These datasets consists of pairs of sentences which can highlight potential bias.
- **p. 14 / 4 Results - extractive body cue:** We can minimize performance regressions on public NLP datasets by modifying our RLHF fine-tuning procedure.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 3.2 Dataset (p. 6); 3.6 Evaluation (p. 9); 4 Results (p. 10); A.3 Dataset sizes (p. 33).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | When evaluated only on prompts that were not adversarially selected against GPT-3, our PPO models are still significantly more truthful and informative than GPT-3 ... | p. 13 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | This indicates that these datasets are not sufficiently diverse to improve performance on our API prompt 12 | p. 12 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4.2 Results on public NLP datasets InstructGPT models show improvements in truthfulness over GPT-3. | p. 13 (4 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those ... | p. 2 (Figure/Table caption) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4.1 Results on the API distribution Labelers significantly prefer InstructGPT outputs over outputs from GPT-3. | p. 11 (4 Results) |

## Dataset / Benchmark Role

- **p. 13 / 4 Results - extractive body cue:** Second, it can be difficult for public NLP datasets to obtain a very high diversity of inputs (at least, on the kinds of inputs that ...
- **p. 12 / 4 Results - extractive body cue:** We ran an experiment where we split our labelers into 5 groups, and train 5 RMs (with 3 different seeds) using 5-fold cross validation (training ...
- **p. 13 / 4 Results - extractive body cue:** First, public NLP datasets are designed to capture tasks that are easy to evaluate with automatic metrics, such as classification, question answering, and to a ...
- **p. 15 / 4 Results - extractive body cue:** In Figure 33, we show that there is a value of the pretraining mix coefficient that both reverses the performance regressions on SQuADv2 and DROP ...
- **p. 10 / 4 Results - extractive body cue:** In this section, we provide experimental evidence for our claims in Section 1, sorted into three parts: results on the API prompt distribution, results on ...
- **p. 12 / 4 Results - extractive body cue:** Public NLP datasets are not reflective of how our language models are used.
- **p. 14 / 4 Results - extractive body cue:** These datasets consists of pairs of sentences which can highlight potential bias.
- **p. 14 / 4 Results - extractive body cue:** We can minimize performance regressions on public NLP datasets by modifying our RLHF fine-tuning procedure.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those from ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: A diagram illustrating the three steps of our method: (1) supervised fine-tuning (SFT), (2) reward model (RM) training, and (3) reinforcement learning via ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Distribution of use case categories from our API prompt dataset. Use-case (%) Generation 45.6% Open QA
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Illustrative prompts from our API prompt dataset. These are fictional examples inspired by real usage-see more examples in Appendix A.2.1. Use-case Prompt Brainstorming ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Labeler-collected metadata on the API distribution. Metadata Scale Overall quality Likert scale; 1-7 Fails to follow the correct instruction / task Binary Inappropriate ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 3: Preference results of our models, measured by winrate against the 175B SFT model. Left: results on prompts submitted to GPT models on the ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 4: Metadata results on the API distribution. Note that, due to dataset sizes, these results are collapsed across model sizes. See Appendix E.2 for ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 5: Comparing our models with FLAN and T0 in terms of Likert scores on a 1-7 scale, on the InstructGPT prompt distribution. FLAN and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Second, it can be difficult for public NLP datasets to obtain a very high diversity of inputs (at least, on the kinds of inputs ... | embodiment, simulator version and control stack | p. 13 (4 Results), p. 12 (4 Results) |
| Task/environment | We ran an experiment where we split our labelers into 5 groups, and train 5 RMs (with 3 different seeds) using 5-fold cross validation ... | reset, timeout, object/scene variation | p. 12 (4 Results), p. 13 (4 Results) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 1 (Body text (section not recovered)), p. 1 (Abstract) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 13: Tuning FLAN and T0 based on reward model scores batch size of 64, a learning rate of 6e-6 and 1 million examples. ... | definition/direction/unit from same section | p. 43 (Figure/Table caption) |
| Figure 36: Likert scores as a function of KL reward coefficient. The blue line indicates the reward value when the coefficient is zero (not ... | definition/direction/unit from same section | p. 57 (Figure/Table caption) |
| To summarize: all of our models are rated as less toxic than expected given the prompt (they get a negative score on a scale ... | definition/direction/unit from same section | p. 14 (4 Results) |
| In Figure 33, we show that there is a value of the pretraining mix coefficient that both reverses the performance regressions on SQuADv2 and ... | definition/direction/unit from same section | p. 15 (4 Results) |
| [...] Prompt: What is the purpose of the list C in the code below? def binomial_coefficient(n, r): C = [0 for i in range(r ... | definition/direction/unit from same section | p. 15 (4 Results) |
| Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We see further evidence of this from the generalization capabilities of our reward models. | definition/direction/unit from same section | p. 12 (4 Results) |
| GPT GPT (prompted) SFT PPO-ptx FLAN T0 Model 2 4 6 Likert score Figure 5: Comparing our models with FLAN and T0 in terms ... | definition/direction/unit from same section | p. 12 (4 Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| In particular, according to held-out workers, all of our InstructGPT models still greatly outperform the GPT-3 baselines. | comparison identity and matched condition | p. 12 (4 Results) |
| To illustrate the magnitude of our gains: when compared directly, 175B InstructGPT outputs are preferred to GPT-3 outputs 85 ± 3% of the time, ... | comparison identity and matched condition | p. 11 (4 Results) |
| Specifically, compared to GPT-3, InstructGPT outputs are more appropriate in the context of a customer assistant, more often follow explicit constraints defined in the ... | comparison identity and matched condition | p. 11 (4 Results) |
| We find that these models perform better than GPT-3, on par with GPT-3 with a well-chosen prompt, and worse than our SFT baseline. | comparison identity and matched condition | p. 12 (4 Results) |
| We believe our InstructGPT model outperforms FLAN and T0 for two reasons. | comparison identity and matched condition | p. 13 (4 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Figure 38: Human evaluation metrics as a function of learning rates. E.9 Learning rate optimization for PPO models For both 1.3B and 6B models, ... | component/input/data sensitivity | p. 58 (Figure/Table caption) |
| This advantage disappears when the respectful prompt is removed ("no prompt"). | component/input/data sensitivity | p. 14 (4 Results) |
| A total of 1,729 prompts were labeled for three different 175B models, both with and without "respectful" instructions. | component/input/data sensitivity | p. 14 (4 Results) |
| Figure 43: Model samples on a prompt cherry-picked to show instruction following behavior in other languages, along with random samples from the GPT-3 175B ... | component/input/data sensitivity | p. 63 (Figure/Table caption) |
| In Figure 29 we show that adding pretraining updates to our PPO fine-tuning (PPO-ptx) mitigates these performance regressions on all datasets, and even surpasses ... | component/input/data sensitivity | p. 15 (4 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| See Section 3 for more details on our method. sizes (1.3B, 6B, and 175B parameters), and all of our models use the GPT-3 architecture. | When evaluated only on prompts that were not adversarially selected against GPT-3, our PPO models are still significantly more truthful and informative than GPT-3 ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (4 Results), p. 12 (4 Results), p. 13 (4 Results), p. 2 (Figure/Table caption), p. 11 (4 Results), p. 11 (4 Results) |
| Primary metric/result | This indicates that these datasets are not sufficiently diverse to improve performance on our API prompt 12 | numeric claim only at cited anchor | p. 12 (4 Results) |

- Numeric sentences retained from the body:
- **p. 11 / 4 Results - extractive body cue:** To illustrate the magnitude of our gains: when compared directly, 175B InstructGPT outputs are preferred to GPT-3 outputs 85 ± 3% of the time, and ...
- **p. 12 / 4 Results - extractive body cue:** These RMs have an accuracy of 69.6 ± 0.9% on predicting the preferences of labelers in the held-out group, a small decrease from their 72.4 ...
- **p. 13 / 4 Results - extractive body cue:** In a head to head comparison, our 175B InstructGPT model outputs were preferred over our FLAN model 78 ±4% of the time and over our ...
- **p. 1 / Abstract - extractive body cue:** In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x ...
- **p. 3 / 1 Introduction - extractive body cue:** On our test set, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having over 100x fewer parameters.
- **p. 3 / 1 Introduction - extractive body cue:** Outputs from our 175B InstructGPT are preferred to 175B GPT-3 outputs 85 ± 3% of the time, and preferred 71 ± 4% of the time ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations. | p. 20 (5 Discussion) |
| body limitation/failure cue | We then consider areas for improvement before a larger discussion of the limitations of our work in Section 5.3. | p. 18 (5 Discussion) |
| body limitation/failure cue | the real world with customers.10 This enables an important feedback loop on the techniques' effectiveness and limitations. | p. 18 (5 Discussion) |
| body limitation/failure cue | Perhaps the greatest limitation of our models is that, in most cases, they follow the user's instruction, even if that could lead to harm ... | p. 19 (5 Discussion) |
| body limitation/failure cue | However, our approach does provides us with a clear empirical feedback loop of what works and what does not. | p. 17 (5 Discussion) |
| body limitation/failure cue | Our proposal for mitigating the alignment tax, by incorporating pretraining data into RLHF finetuning, does not completely mitigate performance regressions, and may make certain ... | p. 20 (5 Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We qualitatively probe InstructGPT's capabilities, and find that it is able to follow instructions for summarizing code, answer questions about code, and sometimes follows ... | p. 4 (1 Introduction) |
| We ran an experiment where we split our labelers into 5 groups, and train 5 RMs (with 3 different seeds) using 5-fold cross validation ... | p. 12 (4 Results) |
| We do this in two ways: we run model samples through the Perspective API8 to obtain automatic toxicity scores, which is the 8www.perspectiveapi.com 13 | p. 13 (4 Results) |
| For the code QA example, GPT-3 does answer the question about 50% of the time. | p. 15 (4 Results) |
| (2) InstructGPT can summarize and answer questions about code more reliably than GPT-3 (though its answer here isn't quite correct). | p. 15 (4 Results) |
| Our 175B PPO-ptx model is able to reliably answers questions about code, and can also follow instructions in other languages; however, we notice that ... | p. 16 (4 Results) |
| Note that these samples do not fully reflect GPT-3's ability to answer questions, since it has not been prompted into a "question answering" mode. ... | p. 16 (4 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 20 / 5 Discussion - extractive body cue:** In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations.
- **p. 18 / 5 Discussion - extractive body cue:** We then consider areas for improvement before a larger discussion of the limitations of our work in Section 5.3.
- **p. 18 / 5 Discussion - extractive body cue:** the real world with customers.10 This enables an important feedback loop on the techniques' effectiveness and limitations.
- **p. 19 / 5 Discussion - extractive body cue:** Perhaps the greatest limitation of our models is that, in most cases, they follow the user's instruction, even if that could lead to harm in ...
- **p. 17 / 5 Discussion - extractive body cue:** However, our approach does provides us with a clear empirical feedback loop of what works and what does not.
- **p. 20 / 5 Discussion - extractive body cue:** Our proposal for mitigating the alignment tax, by incorporating pretraining data into RLHF finetuning, does not completely mitigate performance regressions, and may make certain undesirable ...

- **Evidence anchors reviewed:** datasets p. 13 (4 Results), p. 12 (4 Results), p. 13 (4 Results), p. 15 (4 Results), p. 10 (4 Results), p. 12 (4 Results), metrics p. 43 (Figure/Table caption), p. 57 (Figure/Table caption), p. 14 (4 Results), p. 15 (4 Results), p. 15 (4 Results), p. 2 (Figure/Table caption), baselines p. 2 (Figure/Table caption), p. 12 (4 Results), p. 11 (4 Results), p. 11 (4 Results), p. 12 (4 Results), p. 13 (4 Results), results p. 13 (4 Results), p. 12 (4 Results), p. 13 (4 Results), p. 2 (Figure/Table caption), p. 11 (4 Results), p. 11 (4 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
