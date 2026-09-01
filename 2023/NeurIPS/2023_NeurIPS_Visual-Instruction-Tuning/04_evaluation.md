# Evaluation - Visual Instruction Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.08485; PDF retrieval source: https://arxiv.org/pdf/2304.08485. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), p. 6 (5 Experiments)): Surprisingly, this scheme is able to provide consistent improvement over all question classes, and achieves a new SoTA accuracy of 92.53%.

## Evaluation Body Digest

- **p. 8 / 5 Experiments - extractive PDF cue:** The benchmark dataset is split into training, validation, and test splits with 12726, 4241, and 4241 examples, respectively.
- **p. 7 / 5 Experiments - extractive PDF cue:** To evaluate the model's capability in more challenging tasks and generalizability to novel domains, we collect a diverse set of 24 images with 60 questions ...
- **p. 5 / 5 Experiments - extractive PDF cue:** We assess the performance of LLaVA in instruction-following and visual reasoning capabilities with two primary experimental settings: multimodal chatbot and the ScienceQA dataset, respectively.
- **p. 5 / 5 Experiments - extractive PDF cue:** We pre-train our model on the filtered CC-595K subset for 1 epoch with a learning rate of 2e-3 and a batch size of 128, and ...
- **p. 6 / 5 Experiments - extractive PDF cue:** Note that while these images are out-of-domain for LLaVA, LLaVA is still able to understand the scenes and follow the question instruction to provide a ...
- **p. 6 / 5 Experiments - extractive PDF cue:** Surprisingly, although LLaVA is trained with a small multimodal instruction-following dataset (∼80K unique images), it demonstrates quite similar reasoning results with multimodal GPT-4 on these ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We create two benchmarks to evaluate the model's performance.
- **p. 8 / 5 Experiments - extractive PDF cue:** We consider two representative methods, including GPT-3.5 model (text-davinci-002) with and without chainof-thought (CoT), LLaMA-Adapter [59], as well as multimodal chain-of-thought (MM-CoT) [61], which is ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 5 Experiments (p. 5); B More Results (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Surprisingly, this scheme is able to provide consistent improvement over all question classes, and achieves a new SoTA accuracy of 92.53%. | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Thanks to visual instruction tuning, LLaVA achieves significantly better performance compared with BLIP-2 (+29%) and OpenFlamingo (+48%). | p. 7 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to the text-only GPT-4 that has access to ground-truth labels, LLaVA achieves an impressive 81.7% performance on complex reasoning questions, with an overall ... | p. 7 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Interestingly, the text-only GPT-4, which cannot process images, improves the overall performance of the model on questions that have an image as context. | p. 8 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 7: Accuracy (%) on Science QA dataset. Question categories: NAT = natural science, SOC = social science, LAN = language science, TXT = ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 5 Experiments - extractive PDF cue:** The benchmark dataset is split into training, validation, and test splits with 12726, 4241, and 4241 examples, respectively.
- **p. 7 / 5 Experiments - extractive PDF cue:** To evaluate the model's capability in more challenging tasks and generalizability to novel domains, we collect a diverse set of 24 images with 60 questions ...
- **p. 5 / 5 Experiments - extractive PDF cue:** We assess the performance of LLaVA in instruction-following and visual reasoning capabilities with two primary experimental settings: multimodal chatbot and the ScienceQA dataset, respectively.
- **p. 5 / 5 Experiments - extractive PDF cue:** We pre-train our model on the filtered CC-595K subset for 1 epoch with a learning rate of 2e-3 and a batch size of 128, and ...
- **p. 6 / 5 Experiments - extractive PDF cue:** Note that while these images are out-of-domain for LLaVA, LLaVA is still able to understand the scenes and follow the question instruction to provide a ...
- **p. 6 / 5 Experiments - extractive PDF cue:** Surprisingly, although LLaVA is trained with a small multimodal instruction-following dataset (∼80K unique images), it demonstrates quite similar reasoning results with multimodal GPT-4 on these ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We create two benchmarks to evaluate the model's performance.
- **p. 8 / 5 Experiments - extractive PDF cue:** We consider two representative methods, including GPT-3.5 model (text-davinci-002) with and without chainof-thought (CoT), LLaMA-Adapter [59], as well as multimodal chain-of-thought (MM-CoT) [61], which is ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1: One example to illustrate the instruction-following data. The top block shows the contexts such as captions and boxes used to prompt GPT, and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 1: LLaVA network architecture. For an input image Xv, we consider the pre-trained CLIP visual encoder ViT-L/14 [40], which provides the visual feature Zv ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 2. We perform instruction-tuning of the LLM on the prediction tokens, using its original auto-regressive training objective. Specifically, for a sequence of length L, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2: The input sequence used to train the model. Only two conversation turns are illustrated here; in practice, the number of turns varies based ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3: Example prompt from GPT-4 paper [36] to compare visual reasoning and chat capabilities. Compared to BLIP-2 [28] and OpenFlamingo [5], LLaVA accurately follows ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation on LLaVA-Bench (COCO) with different training data. We report relative scores w.r.t. a text-only GPT-4 model that uses ground truth image captions ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5: Instruction-following capability comparison using relative scores on LLaVA-Bench (In-the- Wild). The results are reported in the format of mean ± std. For the ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6: Challenging examples from LLaVA-Bench (In-the-Wild), we provide extremely-detailed annotation for each image for an accurate evaluation. Some questions require the model to extract ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The benchmark dataset is split into training, validation, and test splits with 12726, 4241, and 4241 examples, respectively. | embodiment, simulator version and control stack | p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Task/environment | To evaluate the model's capability in more challenging tasks and generalizability to novel domains, we collect a diverse set of 24 images with 60 ... | reset, timeout, object/scene variation | p. 7 (5 Experiments), p. 5 (5 Experiments) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| It evaluates the helpfulness, relevance, accuracy, and level of detail of the responses from the assistants, and gives an overall score on a scale ... | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Compared to the text-only GPT-4 that has access to ground-truth labels, LLaVA achieves an impressive 81.7% performance on complex reasoning questions, with an overall ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| We report relative scores w.r.t. the text-only GPT-4 model that uses the textural ground truth description as visual input. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| It yields 90.92% accuracy, which is quite close to the SoTA 91.68%. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| The GPT-4 judge can identify such cases and correct some of the errors that LLaVA makes. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Table 7: Accuracy (%) on Science QA dataset. Question categories: NAT = natural science, SOC = social science, LAN = language science, TXT = ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 2: LLaVA generates HTML/JS code for an interactive website based on user sketch inputs. The interactive interface works after fixing a minor error ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| We assess the performance of LLaVA in instruction-following and visual reasoning capabilities with two primary experimental settings: multimodal chatbot and the ScienceQA dataset, respectively. | definition/direction/unit from same section | p. 5 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to BLIP-2 [28] and OpenFlamingo [5], LLaVA accurately follows the user's instructions, instead of simply describing the scene. | comparison identity and matched condition | p. 6 (5 Experiments) |
| Thanks to visual instruction tuning, LLaVA achieves significantly better performance compared with BLIP-2 (+29%) and OpenFlamingo (+48%). | comparison identity and matched condition | p. 7 (5 Experiments) |
| We hope LLaVA serves as a solid baseline on the benchmarks, on which our findings can inspire future work in developing more capable LMMs. | comparison identity and matched condition | p. 7 (5 Experiments) |
| For more baseline numbers, please see [34]. | comparison identity and matched condition | p. 8 (5 Experiments) |
| To explore the limit of LLMs, we also prompt GPT-4 using 2-shot in-context-learning and achieve 82.69% accuracy, which is a 7.52% absolute gain compared ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| For comparisons, we quote the prompt and response of the multimodal GPT-4 from their paper, and query BLIP-2 and OpenFlamingo model checkpoints to get ... | comparison identity and matched condition | p. 5 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 8: Design choice ablations (%). The differ- ence with the best variant is reported in red text. Ablations. We ablate several design choices ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Conversation Detail description Complex reasoning All Full data 83.1 75.3 96.5 85.1 Detail + Complex 81.5 (-1.6) 73.3 (-2.0) 90.8 (-5.7) 81.9 (-3.2) Conv ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| We consider two representative methods, including GPT-3.5 model (text-davinci-002) with and without chainof-thought (CoT), LLaMA-Adapter [59], as well as multimodal chain-of-thought (MM-CoT) [61], which ... | component/input/data sensitivity | p. 8 (5 Experiments) |
| Figure 3: LLaVA is capable of recognizing the visual content following the user's intent, without directly prompting for visual recognition. It also provides a ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| We pre-train our model on the filtered CC-595K subset for 1 epoch with a learning rate of 2e-3 and a batch size of 128, ... | component/input/data sensitivity | p. 5 (5 Experiments) |
| Figure 4: LLaVA relates the movie scenes to the textual knowledge from the pretrained LLM. The painting depicts a dog in a humorous situation, ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present LLaVA-Bench with two challenging benchmarks, with a diverse selection of paired images, instructions and detailed annotations. • Open-source. | Surprisingly, this scheme is able to provide consistent improvement over all question classes, and achieves a new SoTA accuracy of 92.53%. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), p. 6 (5 Experiments) |
| Primary metric/result | Thanks to visual instruction tuning, LLaVA achieves significantly better performance compared with BLIP-2 (+29%) and OpenFlamingo (+48%). | numeric claim only at cited anchor | p. 7 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 5 Experiments - extractive PDF cue:** We pre-train our model on the filtered CC-595K subset for 1 epoch with a learning rate of 2e-3 and a batch size of 128, and ...
- **p. 7 / 5 Experiments - extractive PDF cue:** Conversation Detail description Complex reasoning All OpenFlamingo [5] 19.3 ± 0.5 19.0 ± 0.5 19.1 ± 0.7 19.1 ± 0.4 BLIP-2 [28] 54.6 ± 1.4 ...
- **p. 7 / 5 Experiments - extractive PDF cue:** First, with instruction tuning, the model's ability of following user instructions improves significantly by over 50 points.
- **p. 7 / 5 Experiments - extractive PDF cue:** Second, adding a small amount of detailed description and complex reasoning questions contributes to a considerable improvement of the model's overall capability by 7 points.
- **p. 8 / 5 Experiments - extractive PDF cue:** For LLaVA, we use the visual features before the last layer, ask the model to first predict reasons and then the answer, and train it ...
- **p. 9 / Method - extractive PDF cue:** To decide the order between the answer and reasoning process in the model prediction, we run both variants and observe that answer-first reports the best ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We also observed an interesting failure of LLaVA, as it responds with yes when asked if strawberry-flavored yogurt is present, even though the fridge ... | p. 7 (5 Experiments) |
| body limitation/failure cue | Additionally, it is not clear how the man is able to maintain balance and stability while ironing clothes in such an unstable environment. | p. 6 (5 Experiments) |
| body limitation/failure cue | Whenever GPT-4 fails to provide answers, we use the prediction from our method. | p. 8 (5 Experiments) |
| body limitation/failure cue | For a substantial number of questions, we note that GPT-4 fails simply because it reports that there is insufficient context such as images or ... | p. 8 (5 Experiments) |
| body limitation/failure cue | We hope LLaVA serves as a solid baseline on the benchmarks, on which our findings can inspire future work in developing more capable LMMs. | p. 7 (5 Experiments) |
| body limitation/failure cue | The scene depicted in the image is peculiar as it involves a makeshift ironing setup on a vehicle, which can be both unsafe and ... | p. 6 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We pre-train our model on the filtered CC-595K subset for 1 epoch with a learning rate of 2e-3 and a batch size of 128, ... | p. 5 (5 Experiments) |
| We train all models with 8× A100s, following Vicuna's hyperparameters [9]. | p. 5 (5 Experiments) |
| For LLaVA, we use the visual features before the last layer, ask the model to first predict reasons and then the answer, and train ... | p. 8 (5 Experiments) |
| To decide the order between the answer and reasoning process in the model prediction, we run both variants and observe that answer-first reports the ... | p. 9 (Method) |
| Training the model for 24 epochs does not improve the performance. | p. 9 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5 Experiments - extractive PDF cue:** We also observed an interesting failure of LLaVA, as it responds with yes when asked if strawberry-flavored yogurt is present, even though the fridge contains ...
- **p. 6 / 5 Experiments - extractive PDF cue:** Additionally, it is not clear how the man is able to maintain balance and stability while ironing clothes in such an unstable environment.
- **p. 8 / 5 Experiments - extractive PDF cue:** Whenever GPT-4 fails to provide answers, we use the prediction from our method.
- **p. 8 / 5 Experiments - extractive PDF cue:** For a substantial number of questions, we note that GPT-4 fails simply because it reports that there is insufficient context such as images or plots.
- **p. 7 / 5 Experiments - extractive PDF cue:** We hope LLaVA serves as a solid baseline on the benchmarks, on which our findings can inspire future work in developing more capable LMMs.
- **p. 6 / 5 Experiments - extractive PDF cue:** The scene depicted in the image is peculiar as it involves a makeshift ironing setup on a vehicle, which can be both unsafe and unconventional.

- **PDF anchors reviewed:** datasets p. 8 (5 Experiments), p. 7 (5 Experiments), p. 5 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), metrics p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), baselines p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 5 (5 Experiments), results p. 8 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), p. 6 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
