# Evaluation - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.15818; PDF retrieval source: https://arxiv.org/pdf/2307.15818. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4. Experiments), p. 8 (4. Experiments), p. 8 (4. Experiments), p. 9 (4. Experiments), p. 10 (4. Experiments), p. 10 (4. Experiments)): We observe that our VLA models significantly outperform the baselines across all categories, with our best RT-2-PaLI-X model achieving more than 3x average success rate over the next best baseline ...

## Evaluation Body Digest

- **p. 7 / 4. Experiments - extractive body cue:** Each robot demonstration trajectory is annotated with a natural language instruction that describes the task performed, consisting of a verb describing the skill (e.g., "pick", ...
- **p. 8 / 4. Experiments - extractive body cue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Figure 3 shows example generalization evaluations, which are split into unseen categories (objects, backgrounds and environments), ...
- **p. 9 / 4. Experiments - extractive body cue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Figure 5 / Real-world out-of-distribution behaviors in the Language Table environment.
- **p. 8 / 4. Experiments - extractive body cue:** We also show qualitative real-world out-of-distribution behaviors behaviors in Figure 5, demonstrating novel pushing tasks and targeting objects not before seen in this environment.
- **p. 7 / 4. Experiments - extractive body cue:** Note, however, that these "in-distribution" evaluations still vary the placement of objects and factors such as time of day and robot position, requiring the skills ...
- **p. 11 / 4. Experiments - extractive body cue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Prompt: Given <img> I need to hammer a nail, what object from the scene might be ...
- **p. 9 / 4. Experiments - extractive body cue:** Model Language-Table BC-Zero (Jang et al., 2021) 72 ± 3 RT-1 (Brohan et al., 2022) 74 ± 13 LAVA (Lynch et al., 2022) 77 ± ...
- **p. 6 / 4. Experiments - extractive body cue:** Our experiments focus on real-world generalization and emergent capabilities of RT-2 and aim to answer the following questions: 6

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observe that our VLA models significantly outperform the baselines across all categories, with our best RT-2-PaLI-X model achieving more than 3x average success ... | p. 9 (4. Experiments) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The performance on seen tasks is similar between the RT-2 models and RT-1, with other baselines attaining a lower success rate. | p. 8 (4. Experiments) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Here, on average, both instantiations of RT-2 perform similarly, resulting in ∼2x improvement over the next two baselines, RT-1 and MOO, and ∼6x better ... | p. 8 (4. Experiments) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We also note that while the larger PaLI-X-based model results in better symbol understanding, reasoning and person recognition performance on average, the smaller PaLM-E-based ... | p. 9 (4. Experiments) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, we observe that training a very large model from scratch results in a very poor performance even for the 5B model. | p. 10 (4. Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4. Experiments - extractive body cue:** Each robot demonstration trajectory is annotated with a natural language instruction that describes the task performed, consisting of a verb describing the skill (e.g., "pick", ...
- **p. 8 / 4. Experiments - extractive body cue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Figure 3 shows example generalization evaluations, which are split into unseen categories (objects, backgrounds and environments), ...
- **p. 9 / 4. Experiments - extractive body cue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Figure 5 / Real-world out-of-distribution behaviors in the Language Table environment.
- **p. 8 / 4. Experiments - extractive body cue:** We also show qualitative real-world out-of-distribution behaviors behaviors in Figure 5, demonstrating novel pushing tasks and targeting objects not before seen in this environment.
- **p. 7 / 4. Experiments - extractive body cue:** Note, however, that these "in-distribution" evaluations still vary the placement of objects and factors such as time of day and robot position, requiring the skills ...
- **p. 11 / 4. Experiments - extractive body cue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Prompt: Given <img> I need to hammer a nail, what object from the scene might be ...
- **p. 9 / 4. Experiments - extractive body cue:** Model Language-Table BC-Zero (Jang et al., 2021) 72 ± 3 RT-1 (Brohan et al., 2022) 74 ± 13 LAVA (Lynch et al., 2022) 77 ± ...
- **p. 6 / 4. Experiments - extractive body cue:** Our experiments focus on real-world generalization and emergent capabilities of RT-2 and aim to answer the following questions: 6

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption PDF body cue not selected; no claim inferred

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Each robot demonstration trajectory is annotated with a natural language instruction that describes the task performed, consisting of a verb describing the skill (e.g., ... | embodiment, simulator version and control stack | p. 7 (4. Experiments), p. 8 (4. Experiments) |
| Task/environment | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Figure 3 shows example generalization evaluations, which are split into unseen categories (objects, backgrounds and ... | reset, timeout, object/scene variation | p. 8 (4. Experiments), p. 9 (4. Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 6 (3.2. Robot-Action Fine-tuning) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 5 (3.2. Robot-Action Fine-tuning) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The performance on seen tasks is similar between the RT-2 models and RT-1, with other baselines attaining a lower success rate. | definition/direction/unit from same section | p. 8 (4. Experiments) |
| We observe that our VLA models significantly outperform the baselines across all categories, with our best RT-2-PaLI-X model achieving more than 3x average success ... | definition/direction/unit from same section | p. 9 (4. Experiments) |
| We also demonstrate examples of RT-2 execution on the project website: robotics-transformer2.github.io. | definition/direction/unit from same section | p. 7 (4. Experiments) |
| To evaluate in-distribution performance as well as generalization capabilities, we compare the RT-2-PaLI-X and RT-2-PaLM-E models to the four baselines listed in the previous ... | definition/direction/unit from same section | p. 7 (4. Experiments) |
| Due to its reduced size, the resulting model can run inference at a similar rate (5 Hz) as the other baselines. | definition/direction/unit from same section | p. 8 (4. Experiments) |
| We demonstrate some examples of such interactions in Figure 2. | definition/direction/unit from same section | p. 9 (4. Experiments) |
| (b) Ablations of RT-2-PaLI-X showcasing the impact of parameter count and training strategy on generalization. | definition/direction/unit from same section | p. 10 (4. Experiments) |
| First, we observe that training a very large model from scratch results in a very poor performance even for the 5B model. | definition/direction/unit from same section | p. 10 (4. Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare our method to multiple state-of-the-art baselines that challenge different aspects of our method. | comparison identity and matched condition | p. 7 (4. Experiments) |
| We observe a significant performance boost when using our model compared to the baselines, indicating that the VLM-based pre-training together with the expressiveness of ... | comparison identity and matched condition | p. 8 (4. Experiments) |
| We observe that our VLA models significantly outperform the baselines across all categories, with our best RT-2-PaLI-X model achieving more than 3x average success ... | comparison identity and matched condition | p. 9 (4. Experiments) |
| To provide an additional point of comparison using open-source baselines and environments, we leverage the open-source Language-Table simulation environment from Lynch et al. | comparison identity and matched condition | p. 8 (4. Experiments) |
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (a) Performance comparison on various emergent skill evaluations (Figure 8) between RT-2 and two baselines. | comparison identity and matched condition | p. 10 (4. Experiments) |
| All of the baselines use the exact same robotic data. | comparison identity and matched condition | p. 7 (4. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Inspired by the chain-of-thought prompting method in LLMs (Wei et al., 2022), we fine-tune a variant of RT-2 with PaLM-E for just a few ... | component/input/data sensitivity | p. 10 (4. Experiments) |
| In particular, we compare two different model sizes, 5B and 55B, as well as three different training routines: training a model from scratch, without ... | component/input/data sensitivity | p. 10 (4. Experiments) |
| To compare against state-of-the-art pretrained representations, we use VC-1 (Majumdar et al., 2023a) and R3M (Nair et al., 2022b), with policies implemented by training ... | component/input/data sensitivity | p. 7 (4. Experiments) |
| We co-fine-tune a smaller PaLI 3B model on several prediction tasks, including in-domain VQA tasks, for the Language-Table dataset, and evaluate the resulting policy ... | component/input/data sensitivity | p. 8 (4. Experiments) |
| The difference between the RT-2 models and the baseline is most pronounced in the various generalization experiments, suggesting that the strength of vision-language-action models ... | component/input/data sensitivity | p. 8 (4. Experiments) |
| We refer to such capabilities as emergent, in the sense that they emerge by transferring Internet-scale pretraining. | component/input/data sensitivity | p. 9 (4. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contribution is RT-2, a family of models derived from fine-tuning large vision-language models trained on web-scale data to directly act as generalizable ... | We observe that our VLA models significantly outperform the baselines across all categories, with our best RT-2-PaLI-X model achieving more than 3x average success ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4. Experiments), p. 8 (4. Experiments), p. 8 (4. Experiments), p. 9 (4. Experiments), p. 10 (4. Experiments), p. 10 (4. Experiments) |
| Primary metric/result | The performance on seen tasks is similar between the RT-2 models and RT-1, with other baselines attaining a lower success rate. | numeric claim only at cited anchor | p. 8 (4. Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4. Experiments - extractive body cue:** (2022), which was collected with 13 robots over 17 months in an office kitchen environment.
- **p. 7 / 4. Experiments - extractive body cue:** For the seen tasks category, we use the same suite of seen instructions as in RT-1 (Brohan et al., 2022), which include over 200 tasks ...
- **p. 8 / 4. Experiments - extractive body cue:** These evaluations consists of over 280 tasks that focus primarily on pick and placing skills in many diverse scenarios.
- **p. 8 / 4. Experiments - extractive body cue:** Here, on average, both instantiations of RT-2 perform similarly, resulting in ∼2x improvement over the next two baselines, RT-1 and MOO, and ∼6x better than ...
- **p. 8 / 4. Experiments - extractive body cue:** Due to its reduced size, the resulting model can run inference at a similar rate (5 Hz) as the other baselines.
- **p. 9 / 4. Experiments - extractive body cue:** Model Language-Table BC-Zero (Jang et al., 2021) 72 ± 3 RT-1 (Brohan et al., 2022) 74 ± 13 LAVA (Lynch et al., 2022) 77 ± ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Even though RT-2 exhibits promising generalization properties, there are multiple limitations of this approach. | p. 11 (5. Limitations) |
| body limitation/failure cue | This is also connected to another current limitation in that there are only a small number of generally available VLM models that can be ... | p. 11 (5. Limitations) |
| body limitation/failure cue | For the task "pick up the bag about to fall off the table," RT-2 demonstrates physical understanding to disambiguate between two bags and recognize ... | p. 9 (4. Experiments) |
| body limitation/failure cue | We also show qualitative real-world out-of-distribution behaviors behaviors in Figure 5, demonstrating novel pushing tasks and targeting objects not before seen in this environment. | p. 8 (4. Experiments) |
| body limitation/failure cue | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Figure 5 / Real-world out-of-distribution behaviors in the Language Table environment. | p. 9 (4. Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For all RT-2 training runs we adopt the hyperparameters from the original PaLI-X (Chen et al., 2023a) and PaLM-E (Driess et al., 2023) papers, ... | p. 7 (4. Experiments) |
| Due to its reduced size, the resulting model can run inference at a similar rate (5 Hz) as the other baselines. | p. 8 (4. Experiments) |
| For the action prediction task, we discretize and encode actions as text in the format "X Y", where X and Y range between {-10, ... | p. 8 (4. Experiments) |
| Identical RT-2-PaLI-3B model checkpoint is used as in Tab. | p. 9 (4. Experiments) |
| Inspired by the chain-of-thought prompting method in LLMs (Wei et al., 2022), we fine-tune a variant of RT-2 with PaLM-E for just a few ... | p. 10 (4. Experiments) |
| The smaller version of that model, consisting of 5B parameters, can run at a frequency of around 5 Hz. | p. 6 (3.3. Real-Time Inference) |
| The largest model we evaluated, the 55B parameter RT-2-PaLI-X-55B model, can run at a frequency of 1-3 Hz. | p. 6 (3.3. Real-Time Inference) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / 5. Limitations - extractive body cue:** Even though RT-2 exhibits promising generalization properties, there are multiple limitations of this approach.
- **p. 11 / 5. Limitations - extractive body cue:** This is also connected to another current limitation in that there are only a small number of generally available VLM models that can be used ...
- **p. 9 / 4. Experiments - extractive body cue:** For the task "pick up the bag about to fall off the table," RT-2 demonstrates physical understanding to disambiguate between two bags and recognize the ...
- **p. 8 / 4. Experiments - extractive body cue:** We also show qualitative real-world out-of-distribution behaviors behaviors in Figure 5, demonstrating novel pushing tasks and targeting objects not before seen in this environment.
- **p. 9 / 4. Experiments - extractive body cue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Figure 5 / Real-world out-of-distribution behaviors in the Language Table environment.

- **Evidence anchors reviewed:** datasets p. 7 (4. Experiments), p. 8 (4. Experiments), p. 9 (4. Experiments), p. 8 (4. Experiments), p. 7 (4. Experiments), p. 11 (4. Experiments), metrics p. 8 (4. Experiments), p. 9 (4. Experiments), p. 7 (4. Experiments), p. 7 (4. Experiments), p. 8 (4. Experiments), p. 9 (4. Experiments), baselines p. 7 (4. Experiments), p. 8 (4. Experiments), p. 9 (4. Experiments), p. 8 (4. Experiments), p. 10 (4. Experiments), p. 7 (4. Experiments), results p. 9 (4. Experiments), p. 8 (4. Experiments), p. 8 (4. Experiments), p. 9 (4. Experiments), p. 10 (4. Experiments), p. 10 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (a) Performance comparison on various emergent skill evaluations (Figure 8) between RT-2 and two baselines. (p. 10, 4. Experiments).
- **Metric evidence:** To evaluate in-distribution performance as well as generalization capabilities, we compare the RT-2-PaLI-X and RT-2-PaLM-E models to the four baselines listed in the previous sections. (p. 7, 4. Experiments).
- **Baseline/ablation evidence:** We compare our method to multiple state-of-the-art baselines that challenge different aspects of our method. (p. 7, 4. Experiments).
- **Failure/negative evidence:** Even though RT-2 exhibits promising generalization properties, there are multiple limitations of this approach. (p. 11, 5. Limitations).
