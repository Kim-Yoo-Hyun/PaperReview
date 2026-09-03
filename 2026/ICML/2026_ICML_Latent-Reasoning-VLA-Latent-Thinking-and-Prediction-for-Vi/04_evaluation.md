# Evaluation - Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=P64X2q1n1H; PDF retrieval source: https://openreview.net/pdf/d1d48bb8ae32dab3bc513e65d14fb7fc84c438ea.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2. Real-World Experiments), p. 7 (4.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 7 (4.1. Simulation Experiments), p. 17 (Figure/Table caption), p. 8 (4.2. Real-World Experiments)): As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and surpassing GR00T N1.5 overall.

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive body cue:** We evaluate the effectiveness of LaRA-VLA and the overall system through a comprehensive set of experiments spanning both simulation benchmarks and real-world robotic manipulation tasks.
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** SimplerEnv evaluates real-to-sim generalization of robot manipulation policies trained on real-world data.
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** Based on these benchmarks, we construct two training datasets, LIBERO-LaRA and Bridge-LaRA, which are used to train LaRA-VLA.
- **p. 6 / 4. Experiments - extractive body cue:** (Section 4.1) • How well does LaRA-VLA perform on long-horizon real-world manipulation tasks compared to state-of-the-art approaches?
- **p. 8 / 4.1. Simulation Experiments - extractive body cue:** Benchmark Method Gaussian Blur-H Gaussian Blur-L Gaussian Noise-H Gaussian Noise-L LIBERO Qwen-GR00T (Community, 2026) 30.0 76.0 55.7 87.9 LaRA-VLA (Ours) 42.9 79.4 76.0 92.7 SimplerEnv ...
- **p. 8 / 4.2. Real-World Experiments - extractive body cue:** For data collection, we record 100 demonstration trajectories per task category at 30 Hz.
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** On LIBERO, LaRA-VLA achieves the best overall performance with an average success rate of 97.9%, including 99.8% on the Object suite and 96.6% on the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7. Latent collapse analysis. corruption, but LaRA-VLA consistently maintains higher success rates across all perturbation types and severity lev- els. These results indicate that ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Simulation Experiments (p. 7); 4.2. Real-World Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Real-World Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and surpassing GR00T ... | p. 8 (4.2. Real-World Experiments) |
| 4.1. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | On LIBERO, LaRA-VLA achieves the best overall performance with an average success rate of 97.9%, including 99.8% on the Object suite and 96.6% on ... | p. 7 (4.1. Simulation Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7. Latent collapse analysis. corruption, but LaRA-VLA consistently maintains higher success rates across all perturbation types and severity lev- els. These results indicate ... | p. 9 (Figure/Table caption) |
| 4.1. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | On SimplerEnv-WidowX, which evaluates real-to-sim generalization under diverse visual conditions, LaRA-VLA attains the highest average success rate of 68.8%, outperforming No-CoT, Textual CoT, and ... | p. 7 (4.1. Simulation Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 12. Prompt for subtask description generation. actions without attending to explicit CoT-related tokens. Table 9 reports the results on four SimplerEnv tasks. Training ... | p. 17 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive body cue:** We evaluate the effectiveness of LaRA-VLA and the overall system through a comprehensive set of experiments spanning both simulation benchmarks and real-world robotic manipulation tasks.
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** SimplerEnv evaluates real-to-sim generalization of robot manipulation policies trained on real-world data.
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** Based on these benchmarks, we construct two training datasets, LIBERO-LaRA and Bridge-LaRA, which are used to train LaRA-VLA.
- **p. 6 / 4. Experiments - extractive body cue:** (Section 4.1) • How well does LaRA-VLA perform on long-horizon real-world manipulation tasks compared to state-of-the-art approaches?
- **p. 8 / 4.1. Simulation Experiments - extractive body cue:** Benchmark Method Gaussian Blur-H Gaussian Blur-L Gaussian Noise-H Gaussian Noise-L LIBERO Qwen-GR00T (Community, 2026) 30.0 76.0 55.7 87.9 LaRA-VLA (Ours) 42.9 79.4 76.0 92.7 SimplerEnv ...
- **p. 8 / 4.2. Real-World Experiments - extractive body cue:** For data collection, we record 100 demonstration trajectories per task category at 30 Hz.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison of CoT formulations in VLA models. (a) Textual CoT-based VLA explicitly generates discrete reasoning tokens and decodes them into actions through autoregressive ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. A taxonomy of VLA models based on the representation forms of chain-of-thought CoT and actions. Specifically, we categorize models by whether their textual ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Overview of LaRA-VLA. Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Performance comparisons with state-of-the-art methods on LIBERO, grouped by different CoT paradigms. CoT Type
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Attention mechanism used in LaRA-VLA. of the current visual observation and language instruction, the intermediate text-based reasoning latent, and the pre- dicted future ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Performance comparisons with state-of-the-art methods on SimplerEnv-WindowX, grouped by different CoT paradigms. CoT Type
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Real-world setup of four long-horizon tasks. proach offer? (Section 4.3)
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Real-world results. ThinkAct (Huang et al., 2025), MolmoAct (Lee et al., 2025), π0.5 (Intelligence et al., 2025), and DeepThinkVLA (Yin et al., 2025). ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate the effectiveness of LaRA-VLA and the overall system through a comprehensive set of experiments spanning both simulation benchmarks and real-world robotic manipulation ... | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 7 (4.1. Simulation Experiments) |
| Task/environment | SimplerEnv evaluates real-to-sim generalization of robot manipulation policies trained on real-world data. | reset, timeout, object/scene variation | p. 7 (4.1. Simulation Experiments), p. 7 (4.1. Simulation Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 4 (3.3. Training Procedures) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (3.3. Training Procedures), p. 5 (3.3. Training Procedures) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| On LIBERO, LaRA-VLA achieves the best overall performance with an average success rate of 97.9%, including 99.8% on the Object suite and 96.6% on ... | definition/direction/unit from same section | p. 7 (4.1. Simulation Experiments) |
| Figure 7. Latent collapse analysis. corruption, but LaRA-VLA consistently maintains higher success rates across all perturbation types and severity lev- els. These results indicate ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| We report success rates for each suite and the overall average over 50 rollouts per task. | definition/direction/unit from same section | p. 7 (4.1. Simulation Experiments) |
| We report task success rates under Gaussian blur and Gaussian noise with two severity levels. | definition/direction/unit from same section | p. 8 (4.1. Simulation Experiments) |
| As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and surpassing GR00T ... | definition/direction/unit from same section | p. 8 (4.2. Real-World Experiments) |
| Table 7. Subtask-level and overall success rates (%) on real-world robot tasks. | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Figure 12. Prompt for subtask description generation. actions without attending to explicit CoT-related tokens. Table 9 reports the results on four SimplerEnv tasks. Training ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Latent tokens associated with different reasoning components form wellseparated and semantically coherent clusters, demonstrating clear functional specialization rather than degeneration into uniform or uninformative ... | definition/direction/unit from same section | p. 9 (4.3. Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (Section 4.1) • How well does LaRA-VLA perform on long-horizon real-world manipulation tasks compared to state-of-the-art approaches? | comparison identity and matched condition | p. 6 (4. Experiments) |
| Our experiments are designed to address the following questions: • How effective is LaRA-VLA compared to state-of-the-art methods in simulation benchmarks? | comparison identity and matched condition | p. 6 (4. Experiments) |
| On SimplerEnv-WidowX, which evaluates real-to-sim generalization under diverse visual conditions, LaRA-VLA attains the highest average success rate of 68.8%, outperforming No-CoT, Textual CoT, and ... | comparison identity and matched condition | p. 7 (4.1. Simulation Experiments) |
| As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and surpassing GR00T ... | comparison identity and matched condition | p. 8 (4.2. Real-World Experiments) |
| Performance comparisons with state-of-the-art methods on SimplerEnv-WindowX, grouped by different CoT paradigms. | comparison identity and matched condition | p. 7 (4. Experiments) |
| We further compare LaRA-VLA with Qwen-GR00T (Community, 2026), which serves as a no-CoT baseline without latent reasoning. | comparison identity and matched condition | p. 8 (4.3. Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 9. Effect of CoT supervision and inference-time reasoning on SimplerEnv. We compare models trained with or without CoT supervision and evaluate whether CoT-related ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Table 8. Effect of action pretraining on SimplerEnv. We compare models with and without discrete action supervision during the pretraining stages, while keeping all ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Figure 11. Prompt for object identification. D. Additional Experiments D.1. Additional Analysis Effect of Action Pretraining. We further study the effect of action supervision ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Figure 13. Effect of EMA on latent text token distributions. Without EMA, bounding-box and motion-related latent tokens exhibit stronger overlap, indicating greater semantic entanglement. ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| (Section 4.2) • How effective are the latent reasoning components in LaRA-VLA, and what additional advantages does our ap6 | component/input/data sensitivity | p. 6 (4. Experiments) |
| Ablation study of different forms of CoT supervision on SimplerEnv. | component/input/data sensitivity | p. 8 (4.1. Simulation Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are threefold: • We introduce a latent-reasoning paradigm for VisionLanguage-Action models, in which chain-of-thought reasoning is internalized into continuous latent representations across ... | As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and surpassing GR00T ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2. Real-World Experiments), p. 7 (4.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 7 (4.1. Simulation Experiments), p. 17 (Figure/Table caption), p. 8 (4.2. Real-World Experiments) |
| Primary metric/result | On LIBERO, LaRA-VLA achieves the best overall performance with an average success rate of 97.9%, including 99.8% on the Object suite and 96.6% on ... | numeric claim only at cited anchor | p. 7 (4.1. Simulation Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4. Experiments - extractive body cue:** No CoT OpenVLA (Kim et al., 2025b) 0.0 0.0 0.0 4.1 1.0 Octo (Ghosh et al., 2024) 47.2 9.7 4.2 56.9 29.5 OpenVLA-OFT (Kim et ...
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** We report success rates for each suite and the overall average over 50 rollouts per task.
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** We evaluate on WidowX robots across four tasks and report pertask success rates and the overall average over 24 rollouts per task.
- **p. 8 / 4.2. Real-World Experiments - extractive body cue:** For data collection, we record 100 demonstration trajectories per task category at 30 Hz.
- **p. 8 / 4.2. Real-World Experiments - extractive body cue:** During evaluation, each task is executed for 12 rollout trials.
- **p. 9 / 4.3. Analysis - extractive body cue:** As shown in Figure 8, LaRA-VLA achieves the lowest inference latency among all compared methods, requiring only 135 ms per rollout.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This suggests that the learned latent space does not collapse or become highly unstable under visual perturbations. | p. 8 (4.3. Analysis) |
| body limitation/failure cue | Although LaRA-VLA achieves fast inference and strong performance through latent chain-of-thought reasoning, several limitations remain and warrant further investigation. | p. 9 (5. Limitations) |
| body limitation/failure cue | Improving training efficiency while preserving stable latent reasoning remains an important direction for future work. | p. 9 (5. Limitations) |
| body limitation/failure cue | Table 4. Robustness under visual perturbations. We report task success rates under Gaussian blur and Gaussian noise with two severity levels. H and L ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 12. Prompt for subtask description generation. actions without attending to explicit CoT-related tokens. Table 9 reports the results on four SimplerEnv tasks. Training ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | On LIBERO, LaRA-VLA achieves the best overall performance with an average success rate of 97.9%, including 99.8% on the Object suite and 96.6% on ... | p. 7 (4.1. Simulation Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) a curriculum-based transition from ... | p. 5 (3.3. Training Procedures) |
| To stabilize visual latent learning and prevent representation collapse, we follow prior work (Chen et al., 2025a) and update the parameters used to compute ... | p. 5 (3.3. Training Procedures) |
| Implementation details and training hyperparameters of LaRAVLA are provided in Appendix A. | p. 7 (4.1. Simulation Experiments) |
| Compared with explicit CoT methods, LaRA-VLA avoids autoregressive textual reasoning and reduces inference time by up to 90%. | p. 9 (4.3. Analysis) |
| Together, these findings show that predictive supervision and action grounding provide sufficient inductive bias to maintain structured latent reasoning, even without explicit discrete chain-of-thought ... | p. 9 (4.3. Analysis) |
| Given input images and a language instruction, the image encoder first maps the visual observation to a sequence of visual tokens, denoted as v, ... | p. 4 (3.3. Training Procedures) |
| Through the inverse dynamics supervision applied in earlier stages, this latent context already encodes coarse-grained actionrelevant information. | p. 6 (3.3. Training Procedures) |
| During evaluation, each task is executed for 12 rollout trials. | p. 8 (4.2. Real-World Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.3. Analysis - extractive body cue:** This suggests that the learned latent space does not collapse or become highly unstable under visual perturbations.
- **p. 9 / 5. Limitations - extractive body cue:** Although LaRA-VLA achieves fast inference and strong performance through latent chain-of-thought reasoning, several limitations remain and warrant further investigation.
- **p. 9 / 5. Limitations - extractive body cue:** Improving training efficiency while preserving stable latent reasoning remains an important direction for future work.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Robustness under visual perturbations. We report task success rates under Gaussian blur and Gaussian noise with two severity levels. H and L denote ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 12. Prompt for subtask description generation. actions without attending to explicit CoT-related tokens. Table 9 reports the results on four SimplerEnv tasks. Training with ...
- **p. 7 / 4.1. Simulation Experiments - extractive body cue:** On LIBERO, LaRA-VLA achieves the best overall performance with an average success rate of 97.9%, including 99.8% on the Object suite and 96.6% on the ...

- **Evidence anchors reviewed:** datasets p. 6 (4. Experiments), p. 7 (4.1. Simulation Experiments), p. 7 (4.1. Simulation Experiments), p. 6 (4. Experiments), p. 8 (4.1. Simulation Experiments), p. 8 (4.2. Real-World Experiments), metrics p. 7 (4.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 7 (4.1. Simulation Experiments), p. 8 (4.1. Simulation Experiments), p. 8 (4.2. Real-World Experiments), p. 15 (Figure/Table caption), baselines p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. Simulation Experiments), p. 8 (4.2. Real-World Experiments), p. 7 (4. Experiments), p. 8 (4.3. Analysis), results p. 8 (4.2. Real-World Experiments), p. 7 (4.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 7 (4.1. Simulation Experiments), p. 17 (Figure/Table caption), p. 8 (4.2. Real-World Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
