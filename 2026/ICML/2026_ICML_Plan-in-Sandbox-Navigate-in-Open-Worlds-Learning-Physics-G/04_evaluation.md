# Evaluation - Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=W5e8c9nwNo; PDF retrieval source: https://openreview.net/pdf/27299763732e881621b2b6f37e47e47722f2e575.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation), p. 6 (4.1. Experimental Settings), p. 7 (4.3. Analysis on Sandbox Data), p. 7 (4.3. Analysis on Sandbox Data), p. 8 (4.4. Analysis on Evolution)): SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** GOAT-Bench: This benchmark challenges robots to sequentially execute 5 to 10 subtasks within unseen real-world scenes.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** A-EQA: Designed for active exploration and question answering, the A-EQA dataset comprises 557 natural language queries across 63 real-world indoor scenes.
- **p. 7 / 4.3. Analysis on Sandbox Data - extractive PDF cue:** This confirms that our approach effectively mitigates the dependency on massive datasets, paving a scalable avenue for enhancing navigation policies by integrating abundant, low-cost sandbox ...
- **p. 7 / 4.3. Analysis on Sandbox Data - extractive PDF cue:** All experiments use the model with 2B parameters on A-EQA. ing complementary environments during the Genesis phase, the agent learns more robust navigation priors that ...
- **p. 8 / 4.5. Analysis and Ablation - extractive PDF cue:** Effects of Main Components. "Task" denotes synthesized tasks; "Exp" denotes experience rules; "AAC" denotes Asymmetric Adaptive Clipping.
- **p. 8 / 4.5. Analysis and Ablation - extractive PDF cue:** Subsequently, the introduction of sandbox-synthesized tasks (+Task) serves as a primary driver of capability, further raising A-EQA scores to 50.71% (2B) and 57.14% (4B).
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** Adhering to the OpenEQA (Majumdar et al., 2024) standards, we quantify performance using LLM-Match Success Rate (SR†) and LLM-Match Success weighted by Path Length (SPL†), ...
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** GOAT-Bench employs standard Success Rate (SR) and Success weighted by Path Length (SPL).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Settings (p. 6); 4.2. Main Navigation Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Main Navigation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin. | p. 6 (4.2. Main Navigation Results) |
| 4.5. Analysis and Ablation | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 3, the full SAGE framework achieves substantial improvements of 9.70%/6.03% on A-EQA and 7.52%/8.09% on GOATBench compared to the baselines ... | p. 8 (4.5. Analysis and Ablation) |
| 4.1. Experimental Settings | EMPIRICAL / REAL-ROBOT OR HARDWARE | Adhering to the OpenEQA (Majumdar et al., 2024) standards, we quantify performance using LLM-Match Success Rate (SR†) and LLM-Match Success weighted by Path Length ... | p. 6 (4.1. Experimental Settings) |
| 4.3. Analysis on Sandbox Data | EMPIRICAL / REAL-ROBOT OR HARDWARE | As illustrated in Figure 5 (a), the MIX strategy achieves the highest performance with an SR† of 53.21%, surpassing the individual HM3D and InteriorGS. | p. 7 (4.3. Analysis on Sandbox Data) |
| 4.3. Analysis on Sandbox Data | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, we observe a trend of diminishing marginal returns; while the performance gain slows from 50% to 100% data scale, the trajectory efficiency SPL† ... | p. 7 (4.3. Analysis on Sandbox Data) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** GOAT-Bench: This benchmark challenges robots to sequentially execute 5 to 10 subtasks within unseen real-world scenes.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** A-EQA: Designed for active exploration and question answering, the A-EQA dataset comprises 557 natural language queries across 63 real-world indoor scenes.
- **p. 7 / 4.3. Analysis on Sandbox Data - extractive PDF cue:** This confirms that our approach effectively mitigates the dependency on massive datasets, paving a scalable avenue for enhancing navigation policies by integrating abundant, low-cost sandbox ...
- **p. 7 / 4.3. Analysis on Sandbox Data - extractive PDF cue:** All experiments use the model with 2B parameters on A-EQA. ing complementary environments during the Genesis phase, the agent learns more robust navigation priors that ...
- **p. 8 / 4.5. Analysis and Ablation - extractive PDF cue:** Effects of Main Components. "Task" denotes synthesized tasks; "Exp" denotes experience rules; "AAC" denotes Asymmetric Adaptive Clipping.
- **p. 8 / 4.5. Analysis and Ablation - extractive PDF cue:** Subsequently, the introduction of sandbox-synthesized tasks (+Task) serves as a primary driver of capability, further raising A-EQA scores to 50.71% (2B) and 57.14% (4B).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. (a): Our SAGE framework utilizes a physics-grounded sandbox for self-evolving data generation and policy optimization, enabling the agent to bridge the gap between ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The SAGE Framework. The system operates in three phases: (a) Genesis: A sandbox environment ES synthesizes task-oriented experience rules Kexp. (b) Evolution: The ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Asymmetric Adaptive Clipping (AAC). While both standard and augmented samples share a conservative lower bound (1 -ϵstd) to prevent policy collapse under A ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. (a)&(b): Impact of fixed and dynamic experience-injection probabilities on navigation performance. We compare fixed η ∈{0.0, 0.5, 0.8, 1.0} with a validation-dependent dynamic ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Performance of SAGE on A-EQA and GOAT-Bench. A-EQA results include both SR† (Eq. 14) and SPL† (Eq. 15). Methods with * are reported ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. (a): Comparison of data composition strategies. (b): Impact of data scale on model performance. All experiments use the model with 2B parameters on ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation on Visual Context Length. We analyze the impact of the number of input frames vt on navigation performance. vt = 4 yields ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Effects of Main Components. "Task" denotes syn- thesized tasks; "Exp" denotes experience rules; "AAC" denotes Asymmetric Adaptive Clipping. Cret indicates experience re- trieved ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | GOAT-Bench: This benchmark challenges robots to sequentially execute 5 to 10 subtasks within unseen real-world scenes. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Task/environment | A-EQA: Designed for active exploration and question answering, the A-EQA dataset comprises 557 natural language queries across 63 real-world indoor scenes. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Settings), p. 7 (4.3. Analysis on Sandbox Data) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (2.1. Physics-Grounded Interaction Sandbox), p. 3 (2.3. Navigation Task) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Adhering to the OpenEQA (Majumdar et al., 2024) standards, we quantify performance using LLM-Match Success Rate (SR†) and LLM-Match Success weighted by Path Length ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| GOAT-Bench employs standard Success Rate (SR) and Success weighted by Path Length (SPL). | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| Notably, we observe a trend of diminishing marginal returns; while the performance gain slows from 50% to 100% data scale, the trajectory efficiency SPL† ... | definition/direction/unit from same section | p. 7 (4.3. Analysis on Sandbox Data) |
| In contrast, the dynamic schedule preserves experience guidance in early training and gradually anneals ηt as validation performance improves, achieving the best SR† and ... | definition/direction/unit from same section | p. 8 (4.4. Analysis on Evolution) |
| However, extending to 5 frames yields diminishing returns (SPL drops to 36.67%), suggesting that redundant visual tokens may dilute the VLM's attention without adding ... | definition/direction/unit from same section | p. 8 (4.4. Analysis on Evolution) |
| Heavy reliance on priors yields quick rewards but risks constrain7 | definition/direction/unit from same section | p. 7 (4.4. Analysis on Evolution) |
| Figure 3. Asymmetric Adaptive Clipping (AAC). While both standard and augmented samples share a conservative lower bound (1 -ϵstd) to prevent policy collapse under ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 9. Sensitivity to ϵexp schedules. All values are in percent (%). Schedule A-EQA GOAT-Bench SR† SPL† SR SPL | definition/direction/unit from same section | p. 14 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin. | comparison identity and matched condition | p. 6 (4.2. Main Navigation Results) |
| When controlling for model capacity, our 2B model significantly outperforms the 3D-Mem baseline with the identical backbone, achieving gains of +8.9% on A-EQA and ... | comparison identity and matched condition | p. 6 (4.2. Main Navigation Results) |
| As shown in Table 3, the full SAGE framework achieves substantial improvements of 9.70%/6.03% on A-EQA and 7.52%/8.09% on GOATBench compared to the baselines ... | comparison identity and matched condition | p. 8 (4.5. Analysis and Ablation) |
| Benchmarking against the set of 14,526 efficiently synthesized valid trajectories (comprising 7,988 from HM3D and 6,538 from InteriorGS) as the 100% baseline, Figure 5 ... | comparison identity and matched condition | p. 7 (4.3. Analysis on Sandbox Data) |
| Method A-EQA GOAT-Bench SR† SPL† SR SPL RL Baselines SenseAct-NN Skill Chain 24.7 13.3 29.5 11.3 SenseAct-NN Monolithic 20.6 10.1 12.3 6.8 Closed-Source VLMs ... | comparison identity and matched condition | p. 7 (4.2. Main Navigation Results) |
| Training via Genesis and Evolution (+G.&E.) boosts A-EQA SR† by 6.29% over the zero-shot baseline, 8 | comparison identity and matched condition | p. 8 (4.5. Analysis and Ablation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We benchmark SAGE against a diverse set of state-of-the-art (SOTA) methods categorized into two paradigms: (1) RL Paradigm, including SenseAct-NN variants (Khanna et al., ... | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |
| Effects of Main Components. "Task" denotes synthesized tasks; "Exp" denotes experience rules; "AAC" denotes Asymmetric Adaptive Clipping. | component/input/data sensitivity | p. 8 (4.5. Analysis and Ablation) |
| An optimally relaxed bound (ϵexp = 1.0) balances this, enabling rapid experience absorption without policy collapse, achieving a peak SR† of 53.21% and SPL† ... | component/input/data sensitivity | p. 8 (4.4. Analysis on Evolution) |
| Table 8. Effect of mismatched experience injection. All values are in percent (%). | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 9. Sensitivity to ϵexp schedules. All values are in percent (%). Schedule A-EQA GOAT-Bench SR† SPL† SR SPL | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Figure 7. Visualization of the word cloud. rules using regular expressions. The entire trajectory is discarded if the generated output fails to match the ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity ... | SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation), p. 6 (4.1. Experimental Settings), p. 7 (4.3. Analysis on Sandbox Data), p. 7 (4.3. Analysis on Sandbox Data), p. 8 (4.4. Analysis on Evolution) |
| Primary metric/result | As shown in Table 3, the full SAGE framework achieves substantial improvements of 9.70%/6.03% on A-EQA and 7.52%/8.09% on GOATBench compared to the baselines ... | numeric claim only at cited anchor | p. 8 (4.5. Analysis and Ablation) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** Following the evaluation protocol established by 3D-Mem, we conduct evaluations on a subset of the Val Unseen split in the main text, totaling 278 subtasks ...
- **p. 8 / 4.4. Analysis on Evolution - extractive PDF cue:** Conversely, aggressive updates (ϵexp = 1.2) lead to instability and performance degradation after 100 steps.
- **p. 8 / 4.4. Analysis on Evolution - extractive PDF cue:** However, extending to 5 frames yields diminishing returns (SPL drops to 36.67%), suggesting that redundant visual tokens may dilute the VLM's attention without adding actionable ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† is set to 0. | p. 6 (4.1. Experimental Settings) |
| body limitation/failure cue | Figure 7. Visualization of the word cloud. rules using regular expressions. The entire trajectory is discarded if the generated output fails to match the ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | Furthermore, we demonstrate the system's practical robustness via Real-World Deployment in Appendix J. | p. 6 (4.1. Experimental Settings) |
| body limitation/failure cue | All experiments use the model with 2B parameters on A-EQA. ing complementary environments during the Genesis phase, the agent learns more robust navigation priors ... | p. 7 (4.3. Analysis on Sandbox Data) |
| body limitation/failure cue | Conservative clipping (ϵexp = 0.4) causes underfitting, failing to exploit Genesis signals. | p. 8 (4.4. Analysis on Evolution) |
| body limitation/failure cue | Conversely, aggressive updates (ϵexp = 1.2) lead to instability and performance degradation after 100 steps. | p. 8 (4.4. Analysis on Evolution) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All results reported are averaged over 3 independent random seeds. | p. 6 (4.1. Experimental Settings) |
| Implementation details and full-set evaluation are provided in Appendix A and H. | p. 6 (4.1. Experimental Settings) |
| Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation 0 50 100 150 200 Training Steps 42 44 46 ... | p. 7 (4.2. Main Navigation Results) |
| Conversely, aggressive updates (ϵexp = 1.2) lead to instability and performance degradation after 100 steps. | p. 8 (4.4. Analysis on Evolution) |
| An optimally relaxed bound (ϵexp = 1.0) balances this, enabling rapid experience absorption without policy collapse, achieving a peak SR† of 53.21% and SPL† ... | p. 8 (4.4. Analysis on Evolution) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† is set to 0.
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 7. Visualization of the word cloud. rules using regular expressions. The entire trajectory is discarded if the generated output fails to match the required ...
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** Furthermore, we demonstrate the system's practical robustness via Real-World Deployment in Appendix J.
- **p. 7 / 4.3. Analysis on Sandbox Data - extractive PDF cue:** All experiments use the model with 2B parameters on A-EQA. ing complementary environments during the Genesis phase, the agent learns more robust navigation priors that ...
- **p. 8 / 4.4. Analysis on Evolution - extractive PDF cue:** Conservative clipping (ϵexp = 0.4) causes underfitting, failing to exploit Genesis signals.
- **p. 8 / 4.4. Analysis on Evolution - extractive PDF cue:** Conversely, aggressive updates (ϵexp = 1.2) lead to instability and performance degradation after 100 steps.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.3. Analysis on Sandbox Data), p. 7 (4.3. Analysis on Sandbox Data), p. 8 (4.5. Analysis and Ablation), p. 8 (4.5. Analysis and Ablation), metrics p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.3. Analysis on Sandbox Data), p. 8 (4.4. Analysis on Evolution), p. 8 (4.4. Analysis on Evolution), p. 7 (4.4. Analysis on Evolution), baselines p. 6 (4.2. Main Navigation Results), p. 6 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation), p. 7 (4.3. Analysis on Sandbox Data), p. 7 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation), results p. 6 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation), p. 6 (4.1. Experimental Settings), p. 7 (4.3. Analysis on Sandbox Data), p. 7 (4.3. Analysis on Sandbox Data), p. 8 (4.4. Analysis on Evolution).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
