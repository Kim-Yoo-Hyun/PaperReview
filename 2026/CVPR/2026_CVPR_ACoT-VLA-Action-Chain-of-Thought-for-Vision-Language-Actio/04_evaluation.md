# Evaluation - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Real-World Deployment), p. 6 (4.2. Simulation Experiments), p. 7 (4.2. Simulation Experiments), p. 6 (4.2. Simulation Experiments), p. 7 (4.2. Simulation Experiments), p. 8 (4.3. Ablation Study)): 3, our approach achieves consistently higher average success rates than both π0.5 and π0, i.e., 66.7% against 61.0% and 33.8%.

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For simulation experiments, we strictly follow the official training splits provided by the corresponding benchmark (LIBERO [32], LIBERO-Plus [15], and VLABench [58]), and train our ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For the real-world setting, all demonstrations used for model training are collected on our own robotic platform.
- **p. 6 / 4.2. Simulation Experiments - extractive PDF cue:** We evaluate our approach on LIBERO benchmark, which targets four distinct robot capabilities: spatial awareness (Spatial), object manipulation (Object), goal completion (Goal), and long-horizon reasoning ...
- **p. 7 / 4.2. Simulation Experiments - extractive PDF cue:** Built on ManiSkill3 [45], VLABench is designed to benchmark both VLAs and VLMs on diverse robotic tasks.
- **p. 8 / 4.4. Real-World Deployment - extractive PDF cue:** To further validate the effectiveness of our framework, we conduct extensive real-world experiments on the AgiBot G1 robot.
- **p. 6 / 4.2. Simulation Experiments - extractive PDF cue:** In this section, we conduct the simulation evaluations across three benchmarks, i.e., LIBERO [32], LIBERO-Plus [15], and VLABench [58], to comprehensively evaluate our approach's performance ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We examine each component's contribution via systematic ablation experiments on the LIBERO benchmark, which are Name Action shift Action horizon Equi. horizon Spatial Object Goal ...
- **p. 8 / 4.4. Real-World Deployment - extractive PDF cue:** Additionally, to examine the cross-embodiment adaptability, we also perform the "Open-set Pick" task on the AgileX robotic platform.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Simulation Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Real-World Deployment | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3, our approach achieves consistently higher average success rates than both π0.5 and π0, i.e., 66.7% against 61.0% and 33.8%. | p. 8 (4.4. Real-World Deployment) |
| 4.2. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to previous stateof-the-art method π0.5, our approach achieves a 1.6% absolute improvement in average. | p. 6 (4.2. Simulation Experiments) |
| 4.2. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, our method maintains exceptional performance under the Supervised Fine-Tuning setting, reaching an 88.0% average success rate. | p. 7 (4.2. Simulation Experiments) |
| 4.2. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As reported in Table 1, the quantitative evaluation results demonstrate that our proposed approach outperforms existing methods across all tracks. | p. 6 (4.2. Simulation Experiments) |
| 4.2. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, our method achieves the best performance across both IS (63.5%) and PS (47.4%). | p. 7 (4.2. Simulation Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For simulation experiments, we strictly follow the official training splits provided by the corresponding benchmark (LIBERO [32], LIBERO-Plus [15], and VLABench [58]), and train our ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For the real-world setting, all demonstrations used for model training are collected on our own robotic platform.
- **p. 6 / 4.2. Simulation Experiments - extractive PDF cue:** We evaluate our approach on LIBERO benchmark, which targets four distinct robot capabilities: spatial awareness (Spatial), object manipulation (Object), goal completion (Goal), and long-horizon reasoning ...
- **p. 7 / 4.2. Simulation Experiments - extractive PDF cue:** Built on ManiSkill3 [45], VLABench is designed to benchmark both VLAs and VLMs on diverse robotic tasks.
- **p. 8 / 4.4. Real-World Deployment - extractive PDF cue:** To further validate the effectiveness of our framework, we conduct extensive real-world experiments on the AgiBot G1 robot.
- **p. 6 / 4.2. Simulation Experiments - extractive PDF cue:** In this section, we conduct the simulation evaluations across three benchmarks, i.e., LIBERO [32], LIBERO-Plus [15], and VLABench [58], to comprehensively evaluate our approach's performance ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We examine each component's contribution via systematic ablation experiments on the LIBERO benchmark, which are Name Action shift Action horizon Equi. horizon Spatial Object Goal ...
- **p. 8 / 4.4. Real-World Deployment - extractive PDF cue:** Additionally, to examine the cross-embodiment adaptability, we also perform the "Open-set Pick" task on the AgileX robotic platform.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Chain-of-Thought in different spaces. (a) Language CoT paradigm predicts sub-tasks as intermediate reasoning. (b) Visual CoT paradigm synthesizes a goal image to provide ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Architectural Overview of ACoT-VLA. The framework consists of three main components operating on features from a shared VLM backbone. (a) The Explicit Action ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison on the LIBERO benchmark. Our proposed approach is trained on the LIBERO dataset. † represents that the LLM backbone is frozen during ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison on the LIBERO-Plus benchmark. Methods under Zero-Shot Transfer are trained on LIBERO dataset and directly evaluated on LIBERO-Plus. Supervised Fine-Tuning denotes models ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Comparison on the VLABench benchmark. IS and PS represent Intention score and Progress score, respectively. All models are trained for 60K steps. † ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Module ablations. The performance is gradually im- proved with the continuous addition of proposed methods. are directly evaluated on LIBERO-Plus to assess general- ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Reference action parameter ablation. We observe that dif- ferent reference-action configurations within EAR generally lead to performance improvements. Methods Spatial Object Goal Long
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 6. Comparison of KV-cache interaction strategies in IAR. shown in Table 4, Table 5, and Table 6. Note that we adopt π0.5 as the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For simulation experiments, we strictly follow the official training splits provided by the corresponding benchmark (LIBERO [32], LIBERO-Plus [15], and VLABench [58]), and train ... | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Task/environment | For the real-world setting, all demonstrations used for model training are collected on our own robotic platform. | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Simulation Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Furthermore, our method maintains exceptional performance under the Supervised Fine-Tuning setting, reaching an 88.0% average success rate. | definition/direction/unit from same section | p. 7 (4.2. Simulation Experiments) |
| In Table 4, experiment "#3" incorporates both EAR and IAR, achieving the highest average success rate of 98.5%. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| 3, our approach achieves consistently higher average success rates than both π0.5 and π0, i.e., 66.7% against 61.0% and 33.8%. | definition/direction/unit from same section | p. 8 (4.4. Real-World Deployment) |
| Table 1. Comparison on the LIBERO benchmark. Our proposed approach is trained on the LIBERO dataset. † represents that the LLM backbone is frozen ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Notably, we observe a pronounced improvement on LIBERO-Long suite, where tasks require long-horizon manipulation with strict error control. | definition/direction/unit from same section | p. 6 (4.2. Simulation Experiments) |
| Notably, the "Downsample" strategy achieves the best performance, suggesting that VLM's features may contain redundancy for action prediction. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| The reduced dimension in the downsampling strategy is set to d′ = 128. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| We set the balance factors in training losses as λ1 = λ2 = 0.5. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 6. Comparison of KV-cache interaction strategies in IAR. shown in Table 4, Table 5, and Table 6. Note that we adopt π0.5 as ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| As shown in Table 6, all three variants outperform the baseline, indicating that extracting implicit action cues from VLM benefits policy learning. | comparison identity and matched condition | p. 8 (4.3. Ablation Study) |
| Compared to previous stateof-the-art method π0.5, our approach achieves a 1.6% absolute improvement in average. | comparison identity and matched condition | p. 6 (4.2. Simulation Experiments) |
| As reported in Table 1, the quantitative evaluation results demonstrate that our proposed approach outperforms existing methods across all tracks. | comparison identity and matched condition | p. 6 (4.2. Simulation Experiments) |
| Baseline 98.8 98.2 98.0 92.4 96.9 Query 98.8 99.0 97.2 92.8 97.0 Attention Pooling 99.4 98.6 98.2 92.8 97.3 Downsample 99.2 99.2 98.2 95.6 ... | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| We observe that various parameter combinations consistently bring improvements over the baseline, indicating that providing action cues is broadly beneficial for policy learning. | comparison identity and matched condition | p. 8 (4.3. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4. Module ablations. The performance is gradually im- proved with the continuous addition of proposed methods. are directly evaluated on LIBERO-Plus to assess ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We examine each component's contribution via systematic ablation experiments on the LIBERO benchmark, which are Name Action shift Action horizon Equi. horizon Spatial Object ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| To further examine the effect of explicit action references in EAR, we investigate different settings of action shift and action horizon, as summarized in ... | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| 4.2, we evaluate our approach on three simulation benchmarks, followed by comprehensive ablation studies in Sec. | component/input/data sensitivity | p. 5 (4. Experiments) |
| For simulation experiments, we strictly follow the official training splits provided by the corresponding benchmark (LIBERO [32], LIBERO-Plus [15], and VLABench [58]), and train ... | component/input/data sensitivity | p. 5 (4.1. Experimental Setup) |
| As shown in Table 6, all three variants outperform the baseline, indicating that extracting implicit action cues from VLM benefits policy learning. | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our main contributions are as follows: • Conceptually, we introduce Action Chain of Thought (ACoT), a new paradigm for generalist robot policies. | 3, our approach achieves consistently higher average success rates than both π0.5 and π0, i.e., 66.7% against 61.0% and 33.8%. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Real-World Deployment), p. 6 (4.2. Simulation Experiments), p. 7 (4.2. Simulation Experiments), p. 6 (4.2. Simulation Experiments), p. 7 (4.2. Simulation Experiments), p. 8 (4.3. Ablation Study) |
| Primary metric/result | Compared to previous stateof-the-art method π0.5, our approach achieves a 1.6% absolute improvement in average. | numeric claim only at cited anchor | p. 6 (4.2. Simulation Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** Specifically, we adopt SigLIP [55] as the visual encoder, while the LLM backbone is instantiated as Gemma 2B architecture [3] with N = 18 layers ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** Regarding the EAR, we employ a compact Transformer-based design composed of N = 18 layers.
- **p. 6 / 4.2. Simulation Experiments - extractive PDF cue:** Each task suite consists of 10 tasks and provides 50 human-teleoperated demonstrations per task for policy training.
- **p. 6 / 4.2. Simulation Experiments - extractive PDF cue:** For each task, the policy is evaluated over 50 trials, amounting to 2, 000 total rollouts.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Concretely, LIBERO-Plus introduces 7 perturbation dimensions, i.e., camera-viewpoints (Camera), robot-initialstates (Robot), language-variations (Language), lightingconditions (Light), background-textures (Background), sensor-noise (Noi ... | p. 6 (4.2. Simulation Experiments) |
| body limitation/failure cue | Specifically, under the Zero-Shot regime, our approach demonstrates pronounced robustness against distribution shifts such as robot initial-state perturbations (+3.2%) and language variations (+4.2%), where ... | p. 7 (4.2. Simulation Experiments) |
| body limitation/failure cue | Through leveraging actions as intermediate reasoning, the model feeds the action head with structured action guidance, which significantly enhances the robustness in long-horizon manipulation ... | p. 6 (4.2. Simulation Experiments) |
| body limitation/failure cue | These results highlight the effectiveness of our action-space reasoning in improving generalization and robust policy learning. | p. 7 (4.2. Simulation Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Concretely, the learning rate follows a cosinedecay schedule with a warm-up phase of 10K steps, a peak learning rate of 5e-5, and a decay ... | p. 6 (4.1. Experimental Setup) |
| For frame processing, each input frame is resized to 224 × 224 prior to the visual encoder. | p. 5 (4.1. Experimental Setup) |
| Specifically, we adopt SigLIP [55] as the visual encoder, while the LLM backbone is instantiated as Gemma 2B architecture [3] with N = 18 ... | p. 5 (4.1. Experimental Setup) |
| For each task, the policy is evaluated over 50 trials, amounting to 2, 000 total rollouts. | p. 6 (4.2. Simulation Experiments) |
| All models are trained for 60K steps. † indicates that the LLM backbone is frozen during training. | p. 7 (4.2. Simulation Experiments) |
| This gain suggests that exploiting the implicit action distribution encoded in vision-language representations can also provide effective guidance for policy learning. | p. 7 (4.3. Ablation Study) |
| 2 (c), given a noisy action segment ˜at:t+H-1, we first encode it into noisy action embedding via a MLP projector. | p. 4 (3.4. Action-Guided Prediction) |
| Note that although both encode action-relevant information, they may highlight different facets of the underlying motion. | p. 4 (3.4. Action-Guided Prediction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Simulation Experiments - extractive PDF cue:** Concretely, LIBERO-Plus introduces 7 perturbation dimensions, i.e., camera-viewpoints (Camera), robot-initialstates (Robot), language-variations (Language), lightingconditions (Light), background-textures (Background), sensor-noise (Noi ...
- **p. 7 / 4.2. Simulation Experiments - extractive PDF cue:** Specifically, under the Zero-Shot regime, our approach demonstrates pronounced robustness against distribution shifts such as robot initial-state perturbations (+3.2%) and language variations (+4.2%), where existing ...
- **p. 6 / 4.2. Simulation Experiments - extractive PDF cue:** Through leveraging actions as intermediate reasoning, the model feeds the action head with structured action guidance, which significantly enhances the robustness in long-horizon manipulation tasks.
- **p. 7 / 4.2. Simulation Experiments - extractive PDF cue:** These results highlight the effectiveness of our action-space reasoning in improving generalization and robust policy learning.

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Simulation Experiments), p. 7 (4.2. Simulation Experiments), p. 8 (4.4. Real-World Deployment), p. 6 (4.2. Simulation Experiments), metrics p. 7 (4.2. Simulation Experiments), p. 7 (4.3. Ablation Study), p. 8 (4.4. Real-World Deployment), p. 5 (Figure/Table caption), p. 6 (4.2. Simulation Experiments), p. 8 (4.3. Ablation Study), baselines p. 7 (Figure/Table caption), p. 8 (4.3. Ablation Study), p. 6 (4.2. Simulation Experiments), p. 6 (4.2. Simulation Experiments), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), results p. 8 (4.4. Real-World Deployment), p. 6 (4.2. Simulation Experiments), p. 7 (4.2. Simulation Experiments), p. 6 (4.2. Simulation Experiments), p. 7 (4.2. Simulation Experiments), p. 8 (4.3. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
