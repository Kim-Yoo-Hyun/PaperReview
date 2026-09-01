# Evaluation - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=2845H8Ua5D; PDF retrieval source: https://openreview.net/pdf/f2c61f8b6264a4b3e7b4a7a87c0a7f09e8cc9b48.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (5 Experiments), p. 10 (Figure/Table caption), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments)): Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback improves performance for π0-base model, while our method ...

## Evaluation Body Digest

- **p. 6 / 5 Experiments - extractive PDF cue:** The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized fusion ...
- **p. 6 / 5 Experiments - extractive PDF cue:** This section presents a comprehensive suite of real-world contact-rich manipulation experiments and analytical studies to empirically validate the ForceVLA model.
- **p. 8 / 5 Experiments - extractive PDF cue:** These results underscore the critical role of the proposed FVLMoE architecture in intelligently integrating force information-not just for sensing contact, but for modulating action in ...
- **p. 9 / 5 Experiments - extractive PDF cue:** These results confirm two core design insights: force should be introduced post-VLM to preserve pretrained representations, and sophisticated fusion (via FVLMoE) is essential to fully ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We trained ForceVLA using approximately 50 expert demonstrations per task.
- **p. 8 / 5 Experiments - extractive PDF cue:** 1, which varies the bottle type in the bottle pumping task; (2) Object Gen.
- **p. 7 / 5 Experiments - extractive PDF cue:** ForceVLA significantly outperforms all baselines on five contact-rich tasks.
- **p. 9 / 5 Experiments - extractive PDF cue:** (a-b) Different object geometries; (c) variation in socket height; (d) partial visual occlusion; (e) unstable socket conditions.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** 5 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback improves performance ... | p. 7 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As demonstrated in Figure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outperforming all baseline configurations. | p. 7 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Trajectory visualizations across tasks and conditions. (a) USB insertion, (b) bottle pumping, and (c) plug insertion under stable and unstable socket conditions. ... | p. 10 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, it achieved an 80.00% success rate, outperforming baselines that lacked force input or processed it naively. | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, our proposed ForceVLA architecture achieved a markedly higher 80% success rate. | p. 9 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 5 Experiments - extractive PDF cue:** The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized fusion ...
- **p. 6 / 5 Experiments - extractive PDF cue:** This section presents a comprehensive suite of real-world contact-rich manipulation experiments and analytical studies to empirically validate the ForceVLA model.
- **p. 8 / 5 Experiments - extractive PDF cue:** These results underscore the critical role of the proposed FVLMoE architecture in intelligently integrating force information-not just for sensing contact, but for modulating action in ...
- **p. 9 / 5 Experiments - extractive PDF cue:** These results confirm two core design insights: force should be introduced post-VLM to preserve pretrained representations, and sophisticated fusion (via FVLMoE) is essential to fully ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We trained ForceVLA using approximately 50 expert demonstrations per task.
- **p. 8 / 5 Experiments - extractive PDF cue:** 1, which varies the bottle type in the bottle pumping task; (2) Object Gen.
- **p. 7 / 5 Experiments - extractive PDF cue:** ForceVLA significantly outperforms all baselines on five contact-rich tasks.
- **p. 9 / 5 Experiments - extractive PDF cue:** (a-b) Different object geometries; (c) variation in socket height; (d) partial visual occlusion; (e) unstable socket conditions.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. In ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Robot manipulation tasks setting. Problem Formulation. Figure 2 shows the set- ting of robot manipulation tasks. The robot's observation at timestep t consists ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of our ForceVLA model. Visual and language inputs are processed by a pre- trained VLM to form contextual embeddings. External force signals ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Overview of task setups used in evaluation. (a) Insert USB, (b) pump bottle, (c) insert plug, (d) peel cucumber, and (e) wipe board. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback improves performance for ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Performance of cucumber peeling.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Success rates (%) of different models under various experimental conditions. Maximum values in each column are highlighted in bold; second-best values are underlined.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; (e) ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized ... | embodiment, simulator version and control stack | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Task/environment | This section presents a comprehensive suite of real-world contact-rich manipulation experiments and analytical studies to empirically validate the ForceVLA model. | reset, timeout, object/scene variation | p. 6 (5 Experiments), p. 8 (5 Experiments) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 4 (1 Introduction), p. 4 (1 Introduction) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 3 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Model performance is primarily evaluated using the task success rate across all five challenging contact-rich manipulation tasks. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Incorporating external force feedback improves performance for π0-base model, while our method achieves the highest average success rate, demonstrating robust performance under complex interaction ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| 1, it achieved an 80.00% success rate, outperforming baselines that lacked force input or processed it naively. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| However, our proposed ForceVLA architecture achieved a markedly higher 80% success rate. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Figure 7: Trajectory visualizations across tasks and conditions. (a) USB insertion, (b) bottle pumping, and (c) plug insertion under stable and unstable socket conditions. ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Table 5: Multi-task joint training success rates (%). ForceVLA (Ours) demonstrates superior average performance and excels or matches the best performance in all individual ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Table 2: Success rates (%) of different models under various experimental conditions. Maximum values in each column are highlighted in bold; second-best values are ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized ... | comparison identity and matched condition | p. 6 (5 Experiments) |
| ForceVLA significantly outperforms all baselines on five contact-rich tasks. | comparison identity and matched condition | p. 7 (5 Experiments) |
| As demonstrated in Figure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outperforming all baseline configurations. | comparison identity and matched condition | p. 7 (5 Experiments) |
| 1, it achieved an 80.00% success rate, outperforming baselines that lacked force input or processed it naively. | comparison identity and matched condition | p. 8 (5 Experiments) |
| Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| For our foundational baseline, we evaluated π0-base and π0-fast variants. | comparison identity and matched condition | p. 8 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The specific variants include π0-base[10] w/o F (standard π0 without force input), π0-base[10] w/ F (π0 with force signals directly concatenated to state inputs), ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized ... | component/input/data sensitivity | p. 6 (5 Experiments) |
| Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 6: Success rates comparison between ForceVLA and ForceVLA without force inputs. The drop column indicates the absolute percentage decrease in success rate when ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |
| Compared to the standard π0-base model without force feedback (π0-base w/ F), which achieved an average of 37.3%, ForceVLA shows an improvement of 23.2%. | component/input/data sensitivity | p. 7 (5 Experiments) |
| For our foundational baseline, we evaluated π0-base and π0-fast variants. | component/input/data sensitivity | p. 8 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Key to our approach is a force-aware Mixture-of-Experts-based fusion module, which enables dynamic processing and deep integration of force, visual, and language features during ... | Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback improves performance ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (5 Experiments), p. 10 (Figure/Table caption), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments) |
| Primary metric/result | As demonstrated in Figure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outperforming all baseline configurations. | numeric claim only at cited anchor | p. 7 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 5 Experiments - extractive PDF cue:** Evaluation was conducted over 20 trials each for the insertion and pumping tasks, 10 trials for the more timeconsuming whiteboard task, and 15 trials for ...
- **p. 6 / 1 Introduction - extractive PDF cue:** Visual data was captured from two RGB-D cameras: one static third-person view (RealSense D435 at 1280x720, 30 FPS) and one wrist-mounted camera (RealSense D415 at ...
- **p. 6 / 1 Introduction - extractive PDF cue:** The resulting dataset, which we term ForceVLA-Data, comprises a total of 244 trajectories, amounting to 140 thousand synchronized timesteps.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 7: Trajectory visualizations across tasks and conditions. (a) USB insertion, (b) bottle pumping, and (c) plug insertion under stable and unstable socket conditions. ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | 2, which changes the plug type in the plug insertion task; (3) Height Gen., which adjusts the initial bottle height and measures success under ... | p. 8 (5 Experiments) |
| body limitation/failure cue | Visual Occlusion Unstable Socket Average π0-base[10] w/o F 48.00% 10.00% 66.67% 60.00% 10.00% 38.93% π0-base[10] w/ F 32.00% 10.00% 77.78% 30.00% 10.00% 31.96% π0-fast[25] ... | p. 8 (5 Experiments) |
| body limitation/failure cue | Similarly, in the "Unstable Socket" scenario (Figure 7c), ForceVLA maintained compliant control as the socket shifted, dynamically adjusting the plug's pose to complete insertion, ... | p. 9 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Evaluation was conducted over 20 trials each for the insertion and pumping tasks, 10 trials for the more timeconsuming whiteboard task, and 15 trials ... | p. 7 (5 Experiments) |
| Code and data will be released at website. | p. 1 (Abstract) |
| By leveraging VLM-based encoders, these models demonstrate strong performance in semantic grounding, language following, and zeroshot generalization. π0 [10] further enhances this framework using ... | p. 1 (1 Introduction) |
| Through a gating mechanism, FVLMoE computes dynamic routing weights over expert subnetworks, each specialized for different modalities across task execution phases. | p. 2 (1 Introduction) |
| Flow-based architectures such as π0 [10, 21] integrate pretrained vision-language encoders with fast action decoders to achieve high-frequency outputs. | p. 3 (1 Introduction) |
| Visual inputs from multiple RGB cameras and task instructions are encoded by a SigLIP-based [55] vision-language model (based on PaliGemma [11]) into contextual embeddings. | p. 4 (1 Introduction) |
| In prevalent sparse MoE implementations, for an input token x, the gating network G(x) produces scores or logits that are used to select a ... | p. 4 (1 Introduction) |
| Ein is passed through an encoder layer for shared refinement to facilitate holistic interaction among all constituent force, visual, and language tokens. | p. 5 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; (e) ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. In ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 7: Trajectory visualizations across tasks and conditions. (a) USB insertion, (b) bottle pumping, and (c) plug insertion under stable and unstable socket conditions. Each ...
- **p. 8 / 5 Experiments - extractive PDF cue:** 2, which changes the plug type in the plug insertion task; (3) Height Gen., which adjusts the initial bottle height and measures success under torque ...
- **p. 8 / 5 Experiments - extractive PDF cue:** Visual Occlusion Unstable Socket Average π0-base[10] w/o F 48.00% 10.00% 66.67% 60.00% 10.00% 38.93% π0-base[10] w/ F 32.00% 10.00% 77.78% 30.00% 10.00% 31.96% π0-fast[25] w/o ...
- **p. 9 / 5 Experiments - extractive PDF cue:** Similarly, in the "Unstable Socket" scenario (Figure 7c), ForceVLA maintained compliant control as the socket shifted, dynamically adjusting the plug's pose to complete insertion, while ...

- **PDF anchors reviewed:** datasets p. 6 (5 Experiments), p. 6 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), metrics p. 7 (5 Experiments), p. 7 (5 Experiments), p. 9 (Figure/Table caption), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 10 (Figure/Table caption), baselines p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 2 (Figure/Table caption), p. 8 (5 Experiments), results p. 7 (Figure/Table caption), p. 7 (5 Experiments), p. 10 (Figure/Table caption), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
