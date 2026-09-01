# Evaluation - NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1143_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01143.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (4 Experiments), p. 9 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments)): Additionally, we can see from Model#3 of Table 5 that the pretraining of Q-former on reasonings brings slight improvement to the success rates of the model.

## Evaluation Body Digest

- **p. 12 / 4 Experiments - extractive PDF cue:** 4.5 Cross Dataset Generalization Ability We evaluate the generalization ability of NavGPT-2 in two aspects: generalize to free-form language instructions and to various unseen environments.
- **p. 13 / 4 Experiments - extractive PDF cue:** We highlight that generalization challenges in unseen environments stem from the biases in connectivity graphs of training environments and visual differences in new scenes.
- **p. 11 / 4 Experiments - extractive PDF cue:** The current SOTA method [75] is achieved by scaling up the training environment for DUET with HM3D [60] and Gibson [76], besides the original 61 ...
- **p. 12 / 4 Experiments - extractive PDF cue:** NavGPT-2 outperforms all DUET variants in SR on the validation unseen split, and it reaches the same performance as DUET with full R2R data when ...
- **p. 11 / 4 Experiments - extractive PDF cue:** When considering the same training scale in MP3D, our method beats the original DUET by 2% in SR on the test unseen split and is ...
- **p. 13 / 4 Experiments - extractive PDF cue:** Methods # RxR-EN HM3D nDTW↑sDTW↑OSR↑SR↑ SPL↑ TL NE↓OSR↑SR↑ SPL↑ DUET 1 37.77 17.39 44.54 25.07 19.65 20.27 6.60 42.70 25.60 13.32 NavGPT-2FlanT5-XXL 2 38.50 19.24 ...
- **p. 14 / 4 Experiments - extractive PDF cue:** For the encoder-decoder model FlanT5, a 3.79% increment in SR is observed on the Val Unseen split when the model size is increased from XL ...
- **p. 9 / 4 Experiments - extractive PDF cue:** We adopt a comprehensive set of navigation metrics to evaluate performance [6], including Trajectory Length (TL), which measures the average path length in meters; Navigation ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Additionally, we can see from Model#3 of Table 5 that the pretraining of Q-former on reasonings brings slight improvement to the success rates of ... | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We adopt a comprehensive set of navigation metrics to evaluate performance [6], including Trajectory Length (TL), which measures the average path length in meters; ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 4, NavGPT-2 significantly outperforms DUET. | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | NavGPT-2 outperforms all DUET variants in SR on the validation unseen split, and it reaches the same performance as DUET with full R2R data ... | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our 5B model outperforms NaviLLM [80] (7B) by 3% SR on test split while still maintaining the language capacity to generate self-explained navigation reasoning. | p. 11 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 12 / 4 Experiments - extractive PDF cue:** 4.5 Cross Dataset Generalization Ability We evaluate the generalization ability of NavGPT-2 in two aspects: generalize to free-form language instructions and to various unseen environments.
- **p. 13 / 4 Experiments - extractive PDF cue:** We highlight that generalization challenges in unseen environments stem from the biases in connectivity graphs of training environments and visual differences in new scenes.
- **p. 11 / 4 Experiments - extractive PDF cue:** The current SOTA method [75] is achieved by scaling up the training environment for DUET with HM3D [60] and Gibson [76], besides the original 61 ...
- **p. 12 / 4 Experiments - extractive PDF cue:** NavGPT-2 outperforms all DUET variants in SR on the validation unseen split, and it reaches the same performance as DUET with full R2R data when ...
- **p. 11 / 4 Experiments - extractive PDF cue:** When considering the same training scale in MP3D, our method beats the original DUET by 2% in SR on the test unseen split and is ...
- **p. 13 / 4 Experiments - extractive PDF cue:** Methods # RxR-EN HM3D nDTW↑sDTW↑OSR↑SR↑ SPL↑ TL NE↓OSR↑SR↑ SPL↑ DUET 1 37.77 17.39 44.54 25.07 19.65 20.27 6.60 42.70 25.60 13.32 NavGPT-2FlanT5-XXL 2 38.50 19.24 ...
- **p. 14 / 4 Experiments - extractive PDF cue:** For the encoder-decoder model FlanT5, a 3.79% increment in SR is observed on the Val Unseen split when the model size is increased from XL ...
- **p. 9 / 4 Experiments - extractive PDF cue:** We adopt a comprehensive set of navigation metrics to evaluate performance [6], including Trajectory Length (TL), which measures the average path length in meters; Navigation ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Left: Besides performing effective navigation planning, NavGPT-2 is capable of generating navigational reasoning in a human-interpretable way. Right: NavGPT-2 can support multi-round interaction ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 2: Model architecture of NavGPT-2, it consists of a multimodality Large Language Model and a topological graph-based navigation policy network. The yellow blocks indicate ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 3: Navigation system prompt for NavGPT-2. action planning. The topological graph is maintained on the fly and served as a memorization mechanism to trace ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 4: Data generation pipeline and visual instruction tuning on navigation reasoning data. {I, O} denotes the instruction-observation pairs on the R2R trajectories. R is ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of single-run performance on R2R dataset. NavGPT-2 surpass all pervious methods incorporating LLMs and eliminate the gap between SOTA methods on the ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 2: Human study on NavGPT-2 generated navigational reasoning. Methods Accuracy Informativeness Rationality GPT-4V 2.31 2.95 2.34 NavGPT-2FlanT5-XL
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 3: Comparison of different scales of training data. Methods # Val Seen Val Unseen TL NE↓OSR↑SR↑SPL↑TL NE↓OSR↑SR↑SPL↑ 10% R2R training data: DUET
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 4: Comparison of zero-shot performance on RxR and HM3D. Methods # RxR-EN HM3D nDTW↑sDTW↑OSR↑SR↑ SPL↑ TL NE↓OSR↑SR↑

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.5 Cross Dataset Generalization Ability We evaluate the generalization ability of NavGPT-2 in two aspects: generalize to free-form language instructions and to various unseen ... | embodiment, simulator version and control stack | p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Task/environment | We highlight that generalization challenges in unseen environments stem from the biases in connectivity graphs of training environments and visual differences in new scenes. | reset, timeout, object/scene variation | p. 13 (4 Experiments), p. 11 (4 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 4 (3 Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (3 Method), p. 8 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We adopt a comprehensive set of navigation metrics to evaluate performance [6], including Trajectory Length (TL), which measures the average path length in meters; ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| As shown in Table 2, NavGPT-2 scored 1.66 on Accuracy, 1.93 on Informativeness, and 1.78 on Rationality, indicating the quality of generated reasonings is ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| Additionally, we can see from Model#3 of Table 5 that the pretraining of Q-former on reasonings brings slight improvement to the success rates of ... | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Compared to the baseline methods, NavGPT-2 bypass it by 4% SR and 2% SPL on the test split even if we do not incorporate ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Specifically, we engaged 10 volunteers to evaluate the navigational reasoning generated by NavGPT-2, focusing on its accuracy, informativeness, and rationality. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Noticeably the GPT-4V scored 2.31, 2.95, and 2.34 respectively, demonstrating an effective way to generate navigational reasoning data. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| Methods # RxR-EN HM3D nDTW↑sDTW↑OSR↑SR↑ SPL↑ TL NE↓OSR↑SR↑ SPL↑ DUET 1 37.77 17.39 44.54 25.07 19.65 20.27 6.60 42.70 25.60 13.32 NavGPT-2FlanT5-XXL 2 38.50 ... | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Methods # Val Seen Val Unseen TL NE↓OSR↑SR↑SPL↑TL NE↓OSR↑SR↑SPL↑ NavGPT-2FlanT5-XL 1 13.02 3.34 74.24 69.44 61.72 13.68 3.37 74.37 67.52 56.01 w/o policy model ... | definition/direction/unit from same section | p. 14 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the baseline methods, NavGPT-2 bypass it by 4% SR and 2% SPL on the test split even if we do not incorporate ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| We adopt a comprehensive set of navigation metrics to evaluate performance [6], including Trajectory Length (TL), which measures the average path length in meters; ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| Specifically, we categorized them into distinct categories: - VLN Specialists with Vision-Language-Action Pretraining [3,14, 15,26-28,31,57,75]: These methods are initialized from general vision-language models [40,63] ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| The only difference lies in the language branch, where we harness the LLM's latent and the baseline adopt a 12layer transformer initialized from LXMERT ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| As shown in Table 4, NavGPT-2 outperforms DUET by 3.67% | comparison identity and matched condition | p. 12 (4 Experiments) |
| NavGPT-2 outperforms all DUET variants in SR on the validation unseen split, and it reaches the same performance as DUET with full R2R data ... | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.6 Ablation Study We ablate the core design choices applied in this paper, including the effect of incorporating a navigation-specific policy model, pretraining the ... | component/input/data sensitivity | p. 13 (4 Experiments) |
| 4.4 The Effect of Data Amount In Table 3 we initialize DUET from LXMERT and compare the model performance when finetuning 10%, 50%, and ... | component/input/data sensitivity | p. 12 (4 Experiments) |
| Table 5: Effect of navigation policy network and pretrained Q-former for reasoning. Methods # Val Seen Val Unseen TL NE↓OSR↑SR↑SPL↑TL NE↓OSR↑SR↑SPL↑ NavGPT-2FlanT5-XL 1 13.02 ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| NavGPT-2 outperforms all DUET variants in SR on the validation unseen split, and it reaches the same performance as DUET with full R2R data ... | component/input/data sensitivity | p. 12 (4 Experiments) |
| To achieve this, we remove all the visual-language cross-attention layers in the Q-former and policy network and use only a single graph-aware self-attention layer ... | component/input/data sensitivity | p. 13 (4 Experiments) |
| In stage two, we freeze the pretrained VLM from stage one and finetune the downstream policy network with a batch size of 2 and ... | component/input/data sensitivity | p. 9 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: (1) We propose a pipeline to incorporate VLN specialists with VLMs free from LLM training. | Additionally, we can see from Model#3 of Table 5 that the pretraining of Q-former on reasonings brings slight improvement to the success rates of ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (4 Experiments), p. 9 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Primary metric/result | We adopt a comprehensive set of navigation metrics to evaluate performance [6], including Trajectory Length (TL), which measures the average path length in meters; ... | numeric claim only at cited anchor | p. 9 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 9 / 4 Experiments - extractive PDF cue:** We adopt a comprehensive set of navigation metrics to evaluate performance [6], including Trajectory Length (TL), which measures the average path length in meters; Navigation ...
- **p. 9 / 4 Experiments - extractive PDF cue:** To optimize learning efficiency, a linear warmup strategy is applied to the learning rate for the first 1,000 steps, gradually increasing it from 10-8 to ...
- **p. 11 / 4 Experiments - extractive PDF cue:** The only difference lies in the language branch, where we harness the LLM's latent and the baseline adopt a 12layer transformer initialized from LXMERT [63].
- **p. 11 / 4 Experiments - extractive PDF cue:** The current SOTA method [75] is achieved by scaling up the training environment for DUET with HM3D [60] and Gibson [76], besides the original 61 ...
- **p. 13 / 4 Experiments - extractive PDF cue:** Therefore, we assess NavGPT-2's zero-shot performance in HM3D by sampling 1000 trajectories from ScaleVLN [75] using Habitat Simulator rendered images, which offer environments visually deviant ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We will leave a detailed investigation of this problem for future work. | p. 14 (4 Experiments) |
| body limitation/failure cue | We hypothesize this improvement is due to the projection of visual features into the same LLM hidden space as language, leading to a more ... | p. 13 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In stage one, we initialize the model from pretrained InstructBLIP checkpoints and train the Q-former for 200K steps with a batch size of 8. | p. 9 (4 Experiments) |
| In stage two, we freeze the pretrained VLM from stage one and finetune the downstream policy network with a batch size of 2 and ... | p. 9 (4 Experiments) |
| The accuracy assessment, with a scoring range from 0 (Entirely incorrect) to 3 (Completely accurate), 6 Our model is smaller (1.5B and 5B) than ... | p. 11 (4 Experiments) |
| But for the decoder-only models Vicuna (Model#3 and Model#4), although they are larger in size than FlanT5-XXL, their performance is much worse. | p. 14 (4 Experiments) |
| For the encoder-decoder model FlanT5, a 3.79% increment in SR is observed on the Val Unseen split when the model size is increased from ... | p. 14 (4 Experiments) |
| Specifically, for a candidate view image oi, we incorporate a frozen ViT-g/14 from EVA-CLIP [24] as the vision encoder to extract visual feature Zv ... | p. 5 (3 Method) |
| For action prediction, the model employs both hidden representations of image tokens and instruction text tokens that have been processed by the LLM encoder ... | p. 5 (3 Method) |
| For decoder-only LLMs, we obtain the latents from the last decoder layer. | p. 6 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 4 Experiments - extractive PDF cue:** We will leave a detailed investigation of this problem for future work.
- **p. 13 / 4 Experiments - extractive PDF cue:** We hypothesize this improvement is due to the projection of visual features into the same LLM hidden space as language, leading to a more robust ...

- **PDF anchors reviewed:** datasets p. 12 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), metrics p. 9 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), baselines p. 11 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), results p. 13 (4 Experiments), p. 9 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
