# Evaluation - TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=b1CVu9l5GO; PDF retrieval source: https://openreview.net/pdf/cc4b18989f84e02c6b06df8b480b7156ad8ee1ee.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 6 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 18 (Figure/Table caption)): Table 1: Performance results on three SimplerEnv Google robot tasks under two evaluation metrics: visual matching and variant aggregation. Overall performance is calculated as the average over all the results. ...

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** We design 8 real-world robot tasks with different manipulation skills and objects including 4 unseen tasks for generalization evaluation.
- **p. 5 / 4 EXPERIMENT - extractive PDF cue:** To comprehensively evaluate our model's performance, we conducted experiments across a wide range of environmental setups, including 3 tasks with 137 different configurations in simulation ...
- **p. 5 / 4 EXPERIMENT - extractive PDF cue:** We benchmark our approach against the following generalist policies, including state-ofthe-art open-sourced models: OpenVLA (Kim et al., 2024): A 7B parameter VLA trained on the ...
- **p. 6 / 4 EXPERIMENT - extractive PDF cue:** These results suggest that the visual trace prompting technique employed in TraceVLA enhances the model's ability to generalize across different robotic manipulation tasks and environmental ...
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** Despite sharing the same robot embodiment as BridgeData-v2, differences in setup, lighting, and camera angles necessitated collecting 30 demonstration trajectories per task for finetuning.
- **p. 6 / 4 EXPERIMENT - extractive PDF cue:** As shown in Table 1, TraceVLA consistently outperforms OpenVLA across various tasks and evaluation metrics in the SimplerEnv Google robot tasks.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** It involves sampling a few episodes and visually inspecting the generated trace to ensure that the selected N provides an appropriate balance between historical context ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** While a longer N includes more past observations, it can clutter the visual context and potentially obscure key objects or the robot end-effector, while a ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 EXPERIMENT (p. 5); B QUALITATIVE RESULTS ON REAL ROBOT ROLLOUTS (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Performance results on three SimplerEnv Google robot tasks under two evaluation metrics: visual matching and variant aggregation. Overall performance is calculated as ... | p. 6 (Figure/Table caption) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results suggest that the visual trace prompting technique employed in TraceVLA enhances the model's ability to generalize across different robotic manipulation tasks and ... | p. 6 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | 0 2 4 6 8 10 Number of Successful Trials Pickplace Corn Pickplace Knife Swipe Corn Sink Fold Cloth 1 4 0 2 8 ... | p. 7 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 9, using a smaller number of steps (N = 3) results in a 3.2% performance improvement. | p. 9 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, when visual trace prompting is incorporated, the success rate of OpenVLA model increases to 47.7%, highlighting the significant impact of visual traces on ... | p. 8 (4 EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** We design 8 real-world robot tasks with different manipulation skills and objects including 4 unseen tasks for generalization evaluation.
- **p. 5 / 4 EXPERIMENT - extractive PDF cue:** To comprehensively evaluate our model's performance, we conducted experiments across a wide range of environmental setups, including 3 tasks with 137 different configurations in simulation ...
- **p. 5 / 4 EXPERIMENT - extractive PDF cue:** We benchmark our approach against the following generalist policies, including state-ofthe-art open-sourced models: OpenVLA (Kim et al., 2024): A 7B parameter VLA trained on the ...
- **p. 6 / 4 EXPERIMENT - extractive PDF cue:** These results suggest that the visual trace prompting technique employed in TraceVLA enhances the model's ability to generalize across different robotic manipulation tasks and environmental ...
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** Despite sharing the same robot embodiment as BridgeData-v2, differences in setup, lighting, and camera angles necessitated collecting 30 demonstration trajectories per task for finetuning.
- **p. 6 / 4 EXPERIMENT - extractive PDF cue:** As shown in Table 1, TraceVLA consistently outperforms OpenVLA across various tasks and evaluation metrics in the SimplerEnv Google robot tasks.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** It involves sampling a few episodes and visually inspecting the generated trace to ensure that the selected N provides an appropriate balance between historical context ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** While a longer N includes more past observations, it can clutter the visual context and potentially obscure key objects or the robot end-effector, while a ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: An illustration of our method. The first image shows the original robot's observation, while the second contains the same image with overlaid visual ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. In additional, we finetuned a more compact VLA model, TraceVLA-Phi3, using the 4B-parameter Phi-3-Vision as a backbone on the Open X-Embodiments dataset, which ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: An illustration of visual trace generation. Given a sequence of historical image observations, we first use Co-tracker to extract dense point trajectories and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Performance results on three SimplerEnv Google robot tasks under two evaluation metrics: visual matching and variant aggregation. Overall performance is calculated as the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: (Left): 7B TraceVLA vs. 7B OpenVLA. (Right): 4B TraceVLA-Phi3 vs. 4B OpenVLA-Phi3. Numbers are averaged across the visual matching and variant aggregation metrics. ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Comparison of OpenVLA and TraceVLA performance across various environmental variations: camera orientations, lighting, background, distractors, and table texture. Environmental Variant Aggregation. Figure 4 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Real robot setup. We design 8 real-world robot tasks with different manipulation skills and objects including 4 unseen tasks for generalization evaluation. 0 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6: Performance comparison of TraceVLA and OpenVLA on8 real-world WidowX-250 robot manipula- tion tasks. We evaluate TraceVLA on physical WidowX-250 robot manipulation tasks using ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We design 8 real-world robot tasks with different manipulation skills and objects including 4 unseen tasks for generalization evaluation. | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENT), p. 5 (4 EXPERIMENT) |
| Task/environment | To comprehensively evaluate our model's performance, we conducted experiments across a wide range of environmental setups, including 3 tasks with 137 different configurations in ... | reset, timeout, object/scene variation | p. 5 (4 EXPERIMENT), p. 5 (4 EXPERIMENT) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (2 PRELIMINARIES), p. 3 (2 PRELIMINARIES) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Camera orientations Lighting darker Background change Distractor Table texture Success Rate (%) OpenVLA TraceVLA Camera Lighting Background Distractor TraceVLA OpenVLA TraceVLA OpenVLA TraceVLA Table ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENT) |
| However, when visual trace prompting is incorporated, the success rate of OpenVLA model increases to 47.7%, highlighting the significant impact of visual traces on ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |
| Table 2: Impact of line thickness on performance. Transparency: We varied the transparency of the visual traces by adjusting the α parameter. Lower α ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| 20% 25% 30% 35% 40% 45% 50% 55% 60% Success Rate (%) Move Near Pick Coke Drawer Open/Close 50.6% 34.1% 36.0% 55.0% 44.0% 44.0% ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENT) |
| (Right): Comparison of average success rates between the base OpenVLA,TraceVLA, and OpenVLA finetuned with a sequence of 6 images. | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |
| 3 6 9 12 Steps of Visual Trace 35% 40% 45% 50% Average Success Rate 43.5% 47.7% 47.5% 46.6% OpenVLA Success Rate: 40.2% Figure ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENT) |
| Table 3: Impact of transparency on performance. Color: The choice of color scheme was also tested. The default TraceVLA color scheme uses RYPBG (Red, ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Table 5: Multitask success rates on LIBERO simulation benchmarks. In addition to SimplerEnv and WIDOWX-250 real robot experiments, in this section, we conduct an ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: Performance results on three SimplerEnv Google robot tasks under two evaluation metrics: visual matching and variant aggregation. Overall performance is calculated as ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| As shown in Figure 6a, TraceVLA consistently outperforms the baseline across diverse tasks including soft object manipulation, pick-and-place operations, and object movement. | comparison identity and matched condition | p. 7 (4 EXPERIMENT) |
| Figure 6: Performance comparison of TraceVLA and OpenVLA on8 real-world WidowX-250 robot manipula- tion tasks. We evaluate TraceVLA on physical WidowX-250 robot manipulation tasks ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| In theory, the model should receive more information from these 6 complete frames compared to visual trace prompting. | comparison identity and matched condition | p. 8 (4 EXPERIMENT) |
| Interestingly, using this text-based trace yields a 2.4% average performance gain over the baseline VLA model, suggesting that point tracking information is indeed useful ... | comparison identity and matched condition | p. 8 (4 EXPERIMENT) |
| In addition, we also analyze the time cost of each additional component introduced in TraceVLA compared to the original OpenVLA model. | comparison identity and matched condition | p. 9 (4 EXPERIMENT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our simulation evaluation utilizes SimplerEnv, which incorporates two distinct settings: visual matching and variant aggregation. | component/input/data sensitivity | p. 5 (4 EXPERIMENT) |
| Complementing this, the variant aggregation setting covers a wide range of environmental variations as shown in Figure 4, including backgrounds from different rooms, lighter ... | component/input/data sensitivity | p. 5 (4 EXPERIMENT) |
| Numbers are averaged across the visual matching and variant aggregation metrics. | component/input/data sensitivity | p. 6 (4 EXPERIMENT) |
| These results suggest that the visual trace prompting technique employed in TraceVLA enhances the model's ability to generalize across different robotic manipulation tasks and ... | component/input/data sensitivity | p. 6 (4 EXPERIMENT) |
| 4.3 ABLATION STUDIES To analyze the performance gain from visual trace prompting, we further study the following questions. | component/input/data sensitivity | p. 8 (4 EXPERIMENT) |
| To answer this, we also tested the performance of the 7B OpenVLA and 4B OpenVLA-Phi3 models finetuned on the exact same dataset as ours, ... | component/input/data sensitivity | p. 8 (4 EXPERIMENT) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-XEmbodiment ... | Table 1: Performance results on three SimplerEnv Google robot tasks under two evaluation metrics: visual matching and variant aggregation. Overall performance is calculated as ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 6 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 18 (Figure/Table caption) |
| Primary metric/result | These results suggest that the visual trace prompting technique employed in TraceVLA enhances the model's ability to generalize across different robotic manipulation tasks and ... | numeric claim only at cited anchor | p. 6 (4 EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 5 / 4 EXPERIMENT - extractive PDF cue:** To comprehensively evaluate our model's performance, we conducted experiments across a wide range of environmental setups, including 3 tasks with 137 different configurations in simulation ...
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** We evaluate TraceVLA on physical WidowX-250 robot manipulation tasks using a fixed-mounted third-person view camera capturing 256 × 256 RGB images.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Here, N = 6, which matches the length of the visual trace used in TraceVLA.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** While text descriptions can precisely convey the location and movement of each point, they also increase token count (by ∼150 tokens) compared with visual trace ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** Additionally, you are given the movement information of 5 points in the image.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** Over the last 6 frames, the 5 points moved as follows: Point 1 moved through positions: [244,80], [200,115], [177,31], ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In the pick-place banana task, TraceVLA's only failures occurred due to grasping issues, while OpenVLA, even when successfully grasping 7 | p. 7 (4 EXPERIMENT) |
| body limitation/failure cue | Moreover, relying solely on text fails to 8 | p. 8 (4 EXPERIMENT) |
| body limitation/failure cue | However, as shown in 7 (Right), finetuning OpenVLA with historical information not only fails to improve overall performance but also reduces it by 6%. | p. 8 (4 EXPERIMENT) |
| body limitation/failure cue | 5 LIMITATION ANALYSIS: TRAINING MEMORY COST AND INFERENCE SPEED Since TraceVLA introduces an additional image input into the model and uses CoTracker to obtain ... | p. 9 (4 EXPERIMENT) |
| body limitation/failure cue | Figure 1. In additional, we finetuned a more compact VLA model, TraceVLA-Phi3, using the 4B-parameter Phi-3-Vision as a backbone on the Open X-Embodiments dataset, ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | This comprehensive set of variations allows us to assess the robustness and adaptability of our approach in handling diverse manipulation scenarios, particularly evaluating the ... | p. 5 (4 EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For evaluating memory cost, we launch a single-node multi-gpu training job with 8 H100 graphics cards under varying batch sizes, and we measure the ... | p. 9 (4 EXPERIMENT) |
| Notably, this difference becomes even smaller with a reduced batch size, indicating that while TraceVLA incurs some extra GPU memory cost, this additional GPU ... | p. 9 (4 EXPERIMENT) |
| (Right): Comparison of inference time across different models. | p. 10 (4 EXPERIMENT) |
| Additionally, we pretrained a 4B VLA model with Phi3-Vision as its backbone VLM (Abdin et al., 2024a), on the Open X-Embodiment dataset using a ... | p. 5 (1. We then identify) |
| These trials included 2-3 random distracting objects in the scene except for pushing cloth. | p. 7 (4 EXPERIMENT) |
| 0 2 4 6 8 10 Number of Successful Trials Pickplace Corn Pickplace Knife Swipe Corn Sink Fold Cloth 1 4 0 2 8 ... | p. 7 (4 EXPERIMENT) |
| This performance drop is likely due to redundant information between visual tokens at different timesteps, which may distract the model from focusing on the ... | p. 8 (4 EXPERIMENT) |
| While text descriptions can precisely convey the location and movement of each point, they also increase token count (by ∼150 tokens) compared with visual ... | p. 8 (4 EXPERIMENT) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** In the pick-place banana task, TraceVLA's only failures occurred due to grasping issues, while OpenVLA, even when successfully grasping 7
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Moreover, relying solely on text fails to 8
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** However, as shown in 7 (Right), finetuning OpenVLA with historical information not only fails to improve overall performance but also reduces it by 6%.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** 5 LIMITATION ANALYSIS: TRAINING MEMORY COST AND INFERENCE SPEED Since TraceVLA introduces an additional image input into the model and uses CoTracker to obtain the ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. In additional, we finetuned a more compact VLA model, TraceVLA-Phi3, using the 4B-parameter Phi-3-Vision as a backbone on the Open X-Embodiments dataset, which ...
- **p. 5 / 4 EXPERIMENT - extractive PDF cue:** This comprehensive set of variations allows us to assess the robustness and adaptability of our approach in handling diverse manipulation scenarios, particularly evaluating the spatial ...

- **PDF anchors reviewed:** datasets p. 7 (4 EXPERIMENT), p. 5 (4 EXPERIMENT), p. 5 (4 EXPERIMENT), p. 6 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 6 (4 EXPERIMENT), metrics p. 6 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 18 (Figure/Table caption), p. 6 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), baselines p. 6 (Figure/Table caption), p. 7 (4 EXPERIMENT), p. 7 (Figure/Table caption), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), results p. 6 (Figure/Table caption), p. 6 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 18 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
