# Evaluation - Generate Subgoal Images before Act: Unlocking the Chain-of-Thought Reasoning in Diffusion Model for Robot Manipulation with Multimodal Prompts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Quantitative Results of Success Rate), p. 7 (4.4. Further Analysis), p. 8 (4.4. Further Analysis), p. 6 (4.1. Experiment Setup), p. 7 (4.3. Quantitative Results of Success Rate), p. 8 (4.4. Further Analysis)): 1 demonstrate CoTDiffusion significantly outperforms other baselines in success rate.

## Evaluation Body Digest

- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Benchmark & Tasks We conduct evaluation on VIMABENCH, a benchmark suite for multimodal robot learning, which is built on the Ravens robot simulator [50].
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** For more details regarding the simulation benchmark and tasks setting, please refer to Appendix A .
- **p. 7 / 4.4. Further Analysis - extractive PDF cue:** Robustness to Insufficient Perception Rich visual observations from diverse views are crucial for complex robot manipulation tasks.
- **p. 8 / 4.4. Further Analysis - extractive PDF cue:** This demonstrates the power of ‘a image is worth a thousand words' - the subgoal images facilitate the generalization of the foundation model to unseen ...
- **p. 7 / 4.4. Further Analysis - extractive PDF cue:** 3 shows, CoTDiffusion still achieves much better fidelity than SuSIE even though SuSIE has got improved after fine-tuning on the same datasets in VIMABENCH.
- **p. 8 / 4.4. Further Analysis - extractive PDF cue:** For L3 generalization, taking an example, we complex the prompt such as ‘rearrange ... then rotate/twist/stack ...' to demand extra tasks such as rotating, twisting ...
- **p. 7 / 4.3. Quantitative Results of Success Rate - extractive PDF cue:** Gato and Flamingo gets low success rates on longhorizon tasks without explicit subgoal generation to correct the accumulative deviation errors from the instructions.
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** The final success rate on long-horizon tasks can be a fair metric.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experiment Setup (p. 6); 4.3. Quantitative Results of Success Rate (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Quantitative Results of Success Rate | EMPIRICAL / SIMULATION | 1 demonstrate CoTDiffusion significantly outperforms other baselines in success rate. | p. 6 (4.3. Quantitative Results of Success Rate) |
| 4.4. Further Analysis | EMPIRICAL / SIMULATION | 3 shows, CoTDiffusion still achieves much better fidelity than SuSIE even though SuSIE has got improved after fine-tuning on the same datasets in VIMABENCH. | p. 7 (4.4. Further Analysis) |
| 4.4. Further Analysis | EMPIRICAL / SIMULATION | CoTDiffusion achieves outstanding gain in the zero-shot performance of combinatorial tasks. | p. 8 (4.4. Further Analysis) |
| 4.1. Experiment Setup | EMPIRICAL / SIMULATION | The final success rate on long-horizon tasks can be a fair metric. | p. 6 (4.1. Experiment Setup) |
| 4.3. Quantitative Results of Success Rate | EMPIRICAL / SIMULATION | The evaluations of success rates on three typical longhorizon tasks with multi-modal prompts. | p. 7 (4.3. Quantitative Results of Success Rate) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Benchmark & Tasks We conduct evaluation on VIMABENCH, a benchmark suite for multimodal robot learning, which is built on the Ravens robot simulator [50].
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** For more details regarding the simulation benchmark and tasks setting, please refer to Appendix A .
- **p. 7 / 4.4. Further Analysis - extractive PDF cue:** Robustness to Insufficient Perception Rich visual observations from diverse views are crucial for complex robot manipulation tasks.
- **p. 8 / 4.4. Further Analysis - extractive PDF cue:** This demonstrates the power of ‘a image is worth a thousand words' - the subgoal images facilitate the generalization of the foundation model to unseen ...
- **p. 7 / 4.4. Further Analysis - extractive PDF cue:** 3 shows, CoTDiffusion still achieves much better fidelity than SuSIE even though SuSIE has got improved after fine-tuning on the same datasets in VIMABENCH.
- **p. 8 / 4.4. Further Analysis - extractive PDF cue:** For L3 generalization, taking an example, we complex the prompt such as ‘rearrange ... then rotate/twist/stack ...' to demand extra tasks such as rotating, twisting ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. A motivation example of robotics manipulation tasks in multi-modal instructions. The subgoal images are worth a thou- sand words, inspiring us to propose ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Method overview: CoTDiffusion consists of a multi-modal encoder and vision encoder V , semantic alignment module S, conditional diffusion model E and foundation ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Two phase of coarse-to-fine alignment pipeline. of mask residuals patch { ˆmi}N-1 i=1 can be viewed as im- plicitly decomposing the prompt into ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of CoTDiffusion in three typical long-horizon tasks with multi-modal prompts in VIMA-BENCH.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. The evaluations of success rates on three typical long- horizon tasks with multi-modal prompts.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. The evaluations of performance drop of different methods on single-view and multi-view from VIMA-BENCH.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Quantitative comparisons of FID betweeen methods on all three tasks, including visual rearrange, reasoning and constraints.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. The normalized CLIP scores for each generation step, reflecting the step-wise accuracy of instruction following.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Benchmark & Tasks We conduct evaluation on VIMABENCH, a benchmark suite for multimodal robot learning, which is built on the Ravens robot simulator [50]. | embodiment, simulator version and control stack | p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup) |
| Task/environment | For more details regarding the simulation benchmark and tasks setting, please refer to Appendix A . | reset, timeout, object/scene variation | p. 6 (4.1. Experiment Setup), p. 7 (4.4. Further Analysis) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3.4. Goal-conditioned Policy Model), p. 3 (3.1. Pipeline Overview) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.1. Pipeline Overview), p. 3 (3.1. Pipeline Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Gato and Flamingo gets low success rates on longhorizon tasks without explicit subgoal generation to correct the accumulative deviation errors from the instructions. | definition/direction/unit from same section | p. 7 (4.3. Quantitative Results of Success Rate) |
| The final success rate on long-horizon tasks can be a fair metric. | definition/direction/unit from same section | p. 6 (4.1. Experiment Setup) |
| 1 demonstrate CoTDiffusion significantly outperforms other baselines in success rate. | definition/direction/unit from same section | p. 6 (4.3. Quantitative Results of Success Rate) |
| The evaluations of success rates on three typical longhorizon tasks with multi-modal prompts. | definition/direction/unit from same section | p. 7 (4.3. Quantitative Results of Success Rate) |
| The normalized CLIP scores for each generation step, reflecting the step-wise accuracy of instruction following. | definition/direction/unit from same section | p. 8 (4.4. Further Analysis) |
| erated keyframes and general prompts, normalized by the CLIP score between ground truth ultimate goal image and prompts. | definition/direction/unit from same section | p. 8 (4.4. Further Analysis) |
| Figure 1. A motivation example of robotics manipulation tasks in multi-modal instructions. The subgoal images are worth a thou- sand words, inspiring us to ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Method overview: CoTDiffusion consists of a multi-modal encoder and vision encoder V , semantic alignment module S, conditional diffusion model E and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1 demonstrate CoTDiffusion significantly outperforms other baselines in success rate. | comparison identity and matched condition | p. 6 (4.3. Quantitative Results of Success Rate) |
| For fair comparison, we finetune the model with the same oracle data with CoTDiffusion. | comparison identity and matched condition | p. 6 (4.2. Baselines) |
| 2, visual planning approach demonstrates greater robustness to limited observations, with a smaller performance drop in single-view compared to abstract methods. | comparison identity and matched condition | p. 7 (4.4. Further Analysis) |
| Quantitative comparisons of FID betweeen methods on all three tasks, including visual rearrange, reasoning and constraints. | comparison identity and matched condition | p. 7 (4.4. Further Analysis) |
| Additionally, we observe that the bi-directional generation may impedes the diffusion model training if without coarse semantic pretraining. | comparison identity and matched condition | p. 8 (4.4. Further Analysis) |
| Without chain-of-thought reasoning abilities, SuSIE struggles to follow instructions when given general multi-modal prompts, let alone generate subgoal images with smooth progressions. | comparison identity and matched condition | p. 8 (4.4. Further Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additionally, we observe that the bi-directional generation may impedes the diffusion model training if without coarse semantic pretraining. | component/input/data sensitivity | p. 8 (4.4. Further Analysis) |
| Gato and Flamingo gets low success rates on longhorizon tasks without explicit subgoal generation to correct the accumulative deviation errors from the instructions. | component/input/data sensitivity | p. 7 (4.3. Quantitative Results of Success Rate) |
| In contrast, CoTDiffusion develops intrinsic chainof-thought reasoning and alignment for generated subgoal images for flexible visual planning directly from the raw multi-modal prompts, without ... | component/input/data sensitivity | p. 7 (4.3. Quantitative Results of Success Rate) |
| Without chain-of-thought reasoning abilities, SuSIE struggles to follow instructions when given general multi-modal prompts, let alone generate subgoal images with smooth progressions. | component/input/data sensitivity | p. 8 (4.4. Further Analysis) |
| VIMA adpots an object-centric approach to flatten all the observation and prompts into object tokens sequence and predicts motor actions autoregressively and demonstrates SOTA ... | component/input/data sensitivity | p. 6 (4.2. Baselines) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of this work are as follows: • We propose a hierarchical framework CoTDiffusion that the high-level diffusion model translates the multi-modal prompts ... | 1 demonstrate CoTDiffusion significantly outperforms other baselines in success rate. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Quantitative Results of Success Rate), p. 7 (4.4. Further Analysis), p. 8 (4.4. Further Analysis), p. 6 (4.1. Experiment Setup), p. 7 (4.3. Quantitative Results of Success Rate), p. 8 (4.4. Further Analysis) |
| Primary metric/result | 3 shows, CoTDiffusion still achieves much better fidelity than SuSIE even though SuSIE has got improved after fine-tuning on the same datasets in VIMABENCH. | numeric claim only at cited anchor | p. 7 (4.4. Further Analysis) |

- Numeric sentences retained from the body:
- **p. 7 / 4.3. Quantitative Results of Success Rate - extractive PDF cue:** Methodology Rearrange Reasoning Constraints Overall Gato 6.4 ± 1.3 2.5 ± 0.4 25.2 ± 3.1 11.4 ± 1.6 Flamingo 17.5 ± 1.6 3.0 ± 0.5 ...
- **p. 7 / 4.4. Further Analysis - extractive PDF cue:** We attribute this to two potential reasons: First, accurate and grounded subgoal images generated in visual planners provide supplemental visual context, which can partly compensate ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Incorporating commonsense knowledge from pre-trained MLLM like GPT-4V provides an avenue for more generalizable and promising reasoning in CoTDiffusion, which leaves as our future ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Additionally, ablating coarse pretraining and bi-directional generation degrades performance, validating their benefits. | p. 7 (4.4. Further Analysis) |
| body limitation/failure cue | Robustness to Insufficient Perception Rich visual observations from diverse views are crucial for complex robot manipulation tasks. | p. 7 (4.4. Further Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Specifically, we first capture visual representation from both the initial and current observation using a shared vision encoder V and concatenate with prompt tokens ... | p. 4 (3.2. Pre-training Coarse Semantic Alignment) |
| So we fed the aligned tokens into a mask predictor D to decode the mask region and set modeling mask prediction as a pretext ... | p. 5 (3.2. Pre-training Coarse Semantic Alignment) |
| Two phase of coarse-to-fine alignment pipeline. of mask residuals patch { ˆmi}N-1 i=1 can be viewed as implicitly decomposing the prompt into spatial manipulation ... | p. 5 (3.2. Pre-training Coarse Semantic Alignment) |
| As the initial observation and prompt remain fixed across different generation steps, the align tokens at various stage tend to so similar that may ... | p. 8 (4.4. Further Analysis) |
| Given the initial observation x0 and a multi-modal prompt P as task instruction potentially needs to be reached by N subgoal steps, robots are ... | p. 3 (3.1. Pipeline Overview) |
| Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! / {z ... | p. 3 (3.1. Pipeline Overview) |
| Conditional Diffusion Model ℰ Semantic Alignment Module " Foundation Model Multi-Modal Encoder Vision Encoder Sweep three into Without exceeding Initial Observation #! | p. 4 (3.1. Pipeline Overview) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Incorporating commonsense knowledge from pre-trained MLLM like GPT-4V provides an avenue for more generalizable and promising reasoning in CoTDiffusion, which leaves as our future work.
- **p. 7 / 4.4. Further Analysis - extractive PDF cue:** Additionally, ablating coarse pretraining and bi-directional generation degrades performance, validating their benefits.
- **p. 7 / 4.4. Further Analysis - extractive PDF cue:** Robustness to Insufficient Perception Rich visual observations from diverse views are crucial for complex robot manipulation tasks.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup), p. 7 (4.4. Further Analysis), p. 8 (4.4. Further Analysis), p. 7 (4.4. Further Analysis), p. 8 (4.4. Further Analysis), metrics p. 7 (4.3. Quantitative Results of Success Rate), p. 6 (4.1. Experiment Setup), p. 6 (4.3. Quantitative Results of Success Rate), p. 7 (4.3. Quantitative Results of Success Rate), p. 8 (4.4. Further Analysis), p. 8 (4.4. Further Analysis), baselines p. 6 (4.3. Quantitative Results of Success Rate), p. 6 (4.2. Baselines), p. 7 (4.4. Further Analysis), p. 7 (4.4. Further Analysis), p. 8 (4.4. Further Analysis), p. 8 (4.4. Further Analysis), results p. 6 (4.3. Quantitative Results of Success Rate), p. 7 (4.4. Further Analysis), p. 8 (4.4. Further Analysis), p. 6 (4.1. Experiment Setup), p. 7 (4.3. Quantitative Results of Success Rate), p. 8 (4.4. Further Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
