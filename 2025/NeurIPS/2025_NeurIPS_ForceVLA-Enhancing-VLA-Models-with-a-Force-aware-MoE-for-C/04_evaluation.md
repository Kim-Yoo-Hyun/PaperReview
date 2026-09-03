# Evaluation - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=2845H8Ua5D; PDF retrieval source: https://arxiv.org/pdf/2505.22159. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 6 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), p. 7 (5 Experiments), p. 6 (5 Experiments)): Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback improves performance for π0-base model, while our method ...

## Evaluation Body Digest

- **p. 6 / 5 Experiments - extractive body cue:** The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized fusion ...
- **p. 6 / 5 Experiments - extractive body cue:** This section presents a comprehensive suite of real-world contact-rich manipulation experiments and analytical studies to empirically validate the ForceVLA model.
- **p. 8 / 5 Experiments - extractive body cue:** These results underscore the critical role of the proposed FVLMoE architecture in intelligently integrating force information-not just for sensing contact, but for modulating action in ...
- **p. 9 / 5 Experiments - extractive body cue:** These results confirm two core design insights: force should be introduced post-VLM to preserve pretrained representations, and sophisticated fusion (via FVLMoE) is essential to fully ...
- **p. 7 / 5 Experiments - extractive body cue:** 1, which varies the bottle type in the bottle pumping task; (2) Object Gen.
- **p. 7 / 5 Experiments - extractive body cue:** These settings include: (1) Object Gen.
- **p. 8 / 5 Experiments - extractive body cue:** (a-b) Different object geometries; (c) variation in socket height; (d) partial visual occlusion; (e) unstable socket conditions.
- **p. 9 / 5 Experiments - extractive body cue:** 5.5 Visualization and Case Studies Figure 7 illustrates ForceVLA's ability to adapt motion in response to contact feedback during complex manipulation tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** 5 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback improves performance ... | p. 7 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As demonstrated in Figure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outperforming all baseline configurations. | p. 6 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, it achieved an 80.00% success rate, outperforming baselines that lacked force input or processed it naively. | p. 8 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Trajectory visualizations across tasks and conditions. (a) USB insertion, (b) bottle pumping, and (c) plug insertion under stable and unstable socket conditions. ... | p. 9 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The π0-base architecture demonstrated superior overall performance: π0-base w/ F (40.2%) and π0-base w/o F (37.3%) significantly outperformed π0-fast w/ F (14.2%) and π0-fast ... | p. 7 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 5 Experiments - extractive body cue:** The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized fusion ...
- **p. 6 / 5 Experiments - extractive body cue:** This section presents a comprehensive suite of real-world contact-rich manipulation experiments and analytical studies to empirically validate the ForceVLA model.
- **p. 8 / 5 Experiments - extractive body cue:** These results underscore the critical role of the proposed FVLMoE architecture in intelligently integrating force information-not just for sensing contact, but for modulating action in ...
- **p. 9 / 5 Experiments - extractive body cue:** These results confirm two core design insights: force should be introduced post-VLM to preserve pretrained representations, and sophisticated fusion (via FVLMoE) is essential to fully ...
- **p. 7 / 5 Experiments - extractive body cue:** 1, which varies the bottle type in the bottle pumping task; (2) Object Gen.
- **p. 7 / 5 Experiments - extractive body cue:** These settings include: (1) Object Gen.
- **p. 8 / 5 Experiments - extractive body cue:** (a-b) Different object geometries; (c) variation in socket height; (d) partial visual occlusion; (e) unstable socket conditions.
- **p. 9 / 5 Experiments - extractive body cue:** 5.5 Visualization and Case Studies Figure 7 illustrates ForceVLA's ability to adapt motion in response to contact feedback during complex manipulation tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. In ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Robot manipulation tasks setting. Problem Formulation. Figure 2 shows the set- ting of robot manipulation tasks. The robot's observation at timestep t consists ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Overview of our ForceVLA model. Visual and language inputs are processed by a pre- trained VLM to form contextual embeddings. External force signals ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Overview of task setups used in evaluation. (a) Insert USB, (b) pump bottle, (c) insert plug, (d) peel cucumber, and (e) wipe board. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback improves performance for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance of cucumber peeling.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; (e) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Success rates (%) of different models under various experimental conditions. Maximum values in each column are highlighted in bold; second-best values are underlined.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized ... | embodiment, simulator version and control stack | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Task/environment | This section presents a comprehensive suite of real-world contact-rich manipulation experiments and analytical studies to empirically validate the ForceVLA model. | reset, timeout, object/scene variation | p. 6 (5 Experiments), p. 8 (5 Experiments) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 2 (1 Introduction), p. 4 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Model performance is primarily evaluated using the task success rate across all five challenging contact-rich manipulation tasks. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Incorporating external force feedback improves performance for π0-base model, while our method achieves the highest average success rate, demonstrating robust performance under complex interaction ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| As demonstrated in Figure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outperforming all baseline configurations. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Insert USB Insert Plug Pump Bottle Wipe Board-1 Wipe Board-2 Peel Cucumber Average 0 10 20 30 40 50 60 70 80 90 100 ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| 1, it achieved an 80.00% success rate, outperforming baselines that lacked force input or processed it naively. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Notably, the MoE-based early fusion failed entirely (0% success rate), highlighting that altering the input representations of a pretrained VLM disrupts its learned feature ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| However, our proposed ForceVLA architecture achieved a markedly higher 80% success rate. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Table 5: Multi-task joint training success rates (%). ForceVLA (Ours) demonstrates superior average performance and excels or matches the best performance in all individual ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized ... | comparison identity and matched condition | p. 6 (5 Experiments) |
| As demonstrated in Figure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outperforming all baseline configurations. | comparison identity and matched condition | p. 6 (5 Experiments) |
| ForceVLA significantly outperforms all baselines on five contact-rich tasks. | comparison identity and matched condition | p. 7 (5 Experiments) |
| 1, it achieved an 80.00% success rate, outperforming baselines that lacked force input or processed it naively. | comparison identity and matched condition | p. 8 (5 Experiments) |
| Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| 5.4 Ablation Studies Table 3: Ablation Results Model Success Rate baseline[10] 45% linear before VLM 55% MoE before VLM 0 concate after VLM 60% ... | comparison identity and matched condition | p. 8 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The specific variants include π0-base[10] w/o F (standard π0 without force input), π0-base[10] w/ F (π0 with force signals directly concatenated to state inputs), ... | component/input/data sensitivity | p. 6 (5 Experiments) |
| The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized ... | component/input/data sensitivity | p. 6 (5 Experiments) |
| For our foundational baseline, we evaluated π0-base and π0-fast variants. | component/input/data sensitivity | p. 7 (5 Experiments) |
| We attribute this sensitivity to its highly optimized and compact token space, which is likely disrupted by naively projected force tokens lacking corresponding large-scale ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| Notably, the MoE-based early fusion failed entirely (0% success rate), highlighting that altering the input representations of a pretrained VLM disrupts its learned feature ... | component/input/data sensitivity | p. 8 (5 Experiments) |
| 5.4 Ablation Studies Table 3: Ablation Results Model Success Rate baseline[10] 45% linear before VLM 55% MoE before VLM 0 concate after VLM 60% ... | component/input/data sensitivity | p. 8 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are: • We present a novel framework that integrates force, vision, language, and action for improved precision and stability on contact-rich ... | Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback improves performance ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 6 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), p. 7 (5 Experiments), p. 6 (5 Experiments) |
| Primary metric/result | As demonstrated in Figure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outperforming all baseline configurations. | numeric claim only at cited anchor | p. 6 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiments - extractive body cue:** Evaluation was conducted over 20 trials each for the insertion and pumping tasks, 10 trials for the more timeconsuming whiteboard task, and 15 trials for ...
- **p. 5 / 1 Introduction - extractive body cue:** Visual data was captured from two RGB-D cameras: one static third-person view (RealSense D435 at 1280x720, 30 FPS) and one wrist-mounted camera (RealSense D415 at ...
- **p. 5 / 1 Introduction - extractive body cue:** The resulting dataset, which we term ForceVLA-Data, comprises a total of 244 trajectories, amounting to 140 thousand synchronized timesteps.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 7: Trajectory visualizations across tasks and conditions. (a) USB insertion, (b) bottle pumping, and (c) plug insertion under stable and unstable socket conditions. ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Visual Occlusion Unstable Socket Average π0-base[10] w/o F 48.00% 10.00% 66.67% 60.00% 10.00% 38.93% π0-base[10] w/ F 32.00% 10.00% 77.78% 30.00% 10.00% 31.96% π0-fast[25] ... | p. 8 (5 Experiments) |
| body limitation/failure cue | Similarly, in the "Unstable Socket" scenario (Figure 7c), ForceVLA maintained compliant control as the socket shifted, dynamically adjusting the plug's pose to complete insertion, ... | p. 9 (5 Experiments) |
| body limitation/failure cue | Figure 19: Key frames from Insert Plug Unstable task videos. 20 | p. 20 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Evaluation was conducted over 20 trials each for the insertion and pumping tasks, 10 trials for the more timeconsuming whiteboard task, and 15 trials ... | p. 6 (5 Experiments) |
| Code and data will be released at website. | p. 1 (Abstract) |
| By leveraging VLM-based encoders, these models demonstrate strong performance in semantic grounding, language following, and zeroshot generalization. π0 [10] further enhances this framework using ... | p. 1 (1 Introduction) |
| Through a gating mechanism, FVLMoE computes dynamic routing weights over expert subnetworks, each specialized for different modalities across task execution phases. | p. 2 (1 Introduction) |
| In prevalent sparse MoE implementations, for an input token x, the gating network G(x) produces scores or logits 3 | p. 3 (1 Introduction) |
| Flow-based architectures such as π0 [10, 21] integrate pretrained vision-language encoders with fast action decoders to achieve high-frequency outputs. | p. 3 (1 Introduction) |
| Visual inputs from multiple RGB cameras and task instructions are encoded by a SigLIP-based [50] vision-language model (based on PaliGemma [11]) into contextual embeddings. | p. 4 (1 Introduction) |
| The resulting dataset, which we term ForceVLA-Data, comprises a total of 244 trajectories, amounting to 140 thousand synchronized timesteps. | p. 5 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly. In ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Trajectory visualizations across tasks and conditions. (a) USB insertion, (b) bottle pumping, and (c) plug insertion under stable and unstable socket conditions. Each ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; (e) ...
- **p. 8 / 5 Experiments - extractive body cue:** Visual Occlusion Unstable Socket Average π0-base[10] w/o F 48.00% 10.00% 66.67% 60.00% 10.00% 38.93% π0-base[10] w/ F 32.00% 10.00% 77.78% 30.00% 10.00% 31.96% π0-fast[25] w/o ...
- **p. 9 / 5 Experiments - extractive body cue:** Similarly, in the "Unstable Socket" scenario (Figure 7c), ForceVLA maintained compliant control as the socket shifted, dynamically adjusting the plug's pose to complete insertion, while ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 19: Key frames from Insert Plug Unstable task videos. 20

- **Evidence anchors reviewed:** datasets p. 6 (5 Experiments), p. 6 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), metrics p. 6 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), baselines p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 2 (Figure/Table caption), p. 8 (5 Experiments), results p. 7 (Figure/Table caption), p. 6 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), p. 7 (5 Experiments), p. 6 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
