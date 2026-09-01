# Evaluation - Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=cb0xbZ3APM; PDF retrieval source: https://openreview.net/pdf/a125f5bc144a834ceef1946ec665a202b39c5b8c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (6 Experiments), p. 10 (Figure/Table caption), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 10 (6 Experiments), p. 7 (6 Experiments)): 6a shows that for the "table bussing" task our recipe achieves comparable performance to the embodiment specific results from above.

## Evaluation Body Digest

- **p. 9 / 6 Experiments - extractive PDF cue:** The robot is tasked with moving objects from a kitchen counter into an (already open) drawer.
- **p. 9 / 6 Experiments - extractive PDF cue:** In any scene, a robot can typically execute many sensible actions, for example grasping different objects.
- **p. 7 / 6 Experiments - extractive PDF cue:** A, B for details on tasks, datasets, and model training.
- **p. 7 / 6 Experiments - extractive PDF cue:** We further show results on the LIBERO simulation benchmark [31], as well as on DROID [23] in the real world.
- **p. 8 / 6 Experiments - extractive PDF cue:** We also evaluate our generalist on the open source benchmark DROID [23] for the same set of tabletop manipulation tasks as in [38].
- **p. 10 / 6 Experiments - extractive PDF cue:** The VLM backbone is thus not damaged by backpropagation from the action expert but still receives a learning signal (from discrete actions) that adapts its ...
- **p. 10 / 6 Experiments - extractive PDF cue:** Experiments across numerous real-world and simulated tasks provide strong evidence for our hypothesis about the degradation of the VLM backbone with naïve training, and a ...
- **p. 8 / 6 Experiments - extractive PDF cue:** Freezing the backbone is not a viable option for knowledge insulation, since the representations in the pre-trained model are not sufficient for robotics, leading to ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 6 Experiments (p. 7); A Dataset & task details (p. 17); A.1 Common public benchmarks (p. 17); A.3 Datasets for training the generalist model (p. 18); 4. Experimental result reproducibility (p. 20); 7. Experiment statistical significance (p. 20); 8. Experiments compute resources (p. 21).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 6a shows that for the "table bussing" task our recipe achieves comparable performance to the embodiment specific results from above. | p. 8 (6 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Success rates (%) on the LIBERO [31] benchmark. Our method achieves a state-of-the-art in LIBERO-90 and LIBERO-Spatial, but is worse on LIBERO-10. ... | p. 10 (Figure/Table caption) |
| 6 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method consistently achieves the highest performance in the real world evaluations. | p. 7 (6 Experiments) |
| 6 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method received a score of 0.55 ± 0.09, π0 received 0.49 ± 0.09, and π0-FAST achieved 0.45 ± 0.09. | p. 8 (6 Experiments) |
| 6 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Spatial Object Goal 10 (Long) 90 Baku [20] - - - 86.0 90.0 MoDE [39] - - - 94.0 95.0 OpenVLA-OFT [25] 97.6 98.4 ... | p. 10 (6 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 6 Experiments - extractive PDF cue:** The robot is tasked with moving objects from a kitchen counter into an (already open) drawer.
- **p. 9 / 6 Experiments - extractive PDF cue:** In any scene, a robot can typically execute many sensible actions, for example grasping different objects.
- **p. 7 / 6 Experiments - extractive PDF cue:** A, B for details on tasks, datasets, and model training.
- **p. 7 / 6 Experiments - extractive PDF cue:** We further show results on the LIBERO simulation benchmark [31], as well as on DROID [23] in the real world.
- **p. 8 / 6 Experiments - extractive PDF cue:** We also evaluate our generalist on the open source benchmark DROID [23] for the same set of tabletop manipulation tasks as in [38].
- **p. 10 / 6 Experiments - extractive PDF cue:** The VLM backbone is thus not damaged by backpropagation from the action expert but still receives a learning signal (from discrete actions) that adapts its ...
- **p. 10 / 6 Experiments - extractive PDF cue:** Experiments across numerous real-world and simulated tasks provide strong evidence for our hypothesis about the degradation of the VLM backbone with naïve training, and a ...
- **p. 8 / 6 Experiments - extractive PDF cue:** Freezing the backbone is not a viable option for knowledge insulation, since the representations in the pre-trained model are not sufficient for robotics, leading to ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The key idea of our approach is to train the VLM backbone with a next-token prediction loss on discretized actions and general VLM ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Problems with standard VLA recipes. The robot is instructed to bus the spoon into the bin. π0 [7] (left) ignores the command and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Evaluation setups. The left three tasks are evaluated in completely unseen environments. actions and yℓ,a denotes both language tokens as well as discretized ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Comparison to baselines for the "items in drawer" task. Our method outperforms all other baselines both in terms of performance and the ability ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Comparison of multiple models/architectures on "table bussing" task with specialist models trained on a single robot embodiment. Our model has the highest performance, ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: Results on "table bussing" task with generalist model trained on many embodiments. Our model follows language well, and trains as quickly as π0-FAST. ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 7: Generalization to novel objects (mobile manipulator).
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 8: Performance on "shirt folding". We also show that removing VLM data (e.g. ours w/o VLM data) leads to slightly worse task completion percentage. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The robot is tasked with moving objects from a kitchen counter into an (already open) drawer. | embodiment, simulator version and control stack | p. 9 (6 Experiments), p. 9 (6 Experiments) |
| Task/environment | In any scene, a robot can typically execute many sensible actions, for example grasping different objects. | reset, timeout, object/scene variation | p. 9 (6 Experiments), p. 7 (6 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (Abstract), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Spatial Object Goal 10 (Long) 90 Baku [20] - - - 86.0 90.0 MoDE [39] - - - 94.0 95.0 OpenVLA-OFT [25] 97.6 98.4 ... | definition/direction/unit from same section | p. 10 (6 Experiments) |
| Table 1: Success rates (%) on the LIBERO [31] benchmark. Our method achieves a state-of-the-art in LIBERO-90 and LIBERO-Spatial, but is worse on LIBERO-10. ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Our method received a score of 0.55 ± 0.09, π0 received 0.49 ± 0.09, and π0-FAST achieved 0.45 ± 0.09. | definition/direction/unit from same section | p. 8 (6 Experiments) |
| (a) Different training strategies (b) Performance over number of training steps Figure 6: Results on "table bussing" task with generalist model trained on many ... | definition/direction/unit from same section | p. 9 (6 Experiments) |
| Figure 8: Performance on "shirt folding". We also show that removing VLM data (e.g. ours w/o VLM data) leads to slightly worse task completion ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Task performance & comparison to baselines. | definition/direction/unit from same section | p. 7 (6 Experiments) |
| This seems to hurt performance on this task significantly. | definition/direction/unit from same section | p. 7 (6 Experiments) |
| In comparison joint-training degrades in task completion. | definition/direction/unit from same section | p. 8 (6 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms all other baselines both in terms of performance and the ability of the model to follow language instructions. | comparison identity and matched condition | p. 8 (6 Experiments) |
| How does our method compare to strong baseline VLAs π0 [7], π0-FAST [38], HybridVLA [33], OpenVLA-OFT [25] in terms of absolute task performance? | comparison identity and matched condition | p. 7 (6 Experiments) |
| Table 1: Success rates (%) on the LIBERO [31] benchmark. Our method achieves a state-of-the-art in LIBERO-90 and LIBERO-Spatial, but is worse on LIBERO-10. ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Task performance & comparison to baselines. | comparison identity and matched condition | p. 7 (6 Experiments) |
| 4b, stopping the gradient flow from the action expert is an effective way of improving language following compared to π0 and joint-training without stop-gradient ... | comparison identity and matched condition | p. 9 (6 Experiments) |
| Finally, our approach achieves a new state-of-the-art in LIBERO-90 and LIBERO-Spatial [31] as shown in Tab. | comparison identity and matched condition | p. 8 (6 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This ablation removes both the stop-gradient and cotraining on VLM data from our proposed method, which can also be considered a variant of HybridVLA ... | component/input/data sensitivity | p. 7 (6 Experiments) |
| 4b, stopping the gradient flow from the action expert is an effective way of improving language following compared to π0 and joint-training without stop-gradient ... | component/input/data sensitivity | p. 9 (6 Experiments) |
| The core idea in our approach is to use discretized actions to provide a learning signal to fine-tune VLM representations, while simultaneously training a ... | component/input/data sensitivity | p. 10 (6 Experiments) |
| What is the effect of stopping the gradient flow? | component/input/data sensitivity | p. 7 (6 Experiments) |
| OpenVLA-OFT follows language well and has low inference time, but has the lowest overall performance. detailed ablation of modeling choices made for our method ... | component/input/data sensitivity | p. 8 (6 Experiments) |
| 7, then joint-training without stop-gradient can also achieve good language following. | component/input/data sensitivity | p. 9 (6 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation. | 6a shows that for the "table bussing" task our recipe achieves comparable performance to the embodiment specific results from above. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (6 Experiments), p. 10 (Figure/Table caption), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 10 (6 Experiments), p. 7 (6 Experiments) |
| Primary metric/result | Table 1: Success rates (%) on the LIBERO [31] benchmark. Our method achieves a state-of-the-art in LIBERO-90 and LIBERO-Spatial, but is worse on LIBERO-10. ... | numeric claim only at cited anchor | p. 10 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 6 Experiments - extractive PDF cue:** Our method received a score of 0.55 ± 0.09, π0 received 0.49 ± 0.09, and π0-FAST achieved 0.45 ± 0.09.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 4a) with a common failure mode of being unable to open the drawer. | p. 7 (6 Experiments) |
| body limitation/failure cue | 7 Discussion & Limitations We analyze the performance, generalization, and language following capabilities of continuousaction VLAs that fine-tune VLMs to output continuous actions, show ... | p. 10 (6 Experiments) |
| body limitation/failure cue | A common limitation of many robot policies is that they pay much more attention to images than the language input [25]. | p. 7 (6 Experiments) |
| body limitation/failure cue | Our method provides an effective recipe for training continuous-action VLAs, but does have limitations. | p. 10 (6 Experiments) |
| body limitation/failure cue | Figure 10: Comparison of different state representations on "table bussing" task. Our method works well with both text and continuous state, while π0 works ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Problems with standard VLA recipes. The robot is instructed to bus the spoon into the bin. π0 [7] (left) ignores the command ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| OpenVLA-OFT follows language well and has low inference time, but has the lowest overall performance. detailed ablation of modeling choices made for our method ... | p. 8 (6 Experiments) |
| Our model has the highest performance, low inference time, and follows language instructions well. π0-FAST also follows language well and has good performance, but ... | p. 8 (6 Experiments) |
| Since here we use the discrete action tokens only during training time, one may wonder whether simpler, naive tokenization is sufficient for learning good ... | p. 10 (6 Experiments) |
| How fast does our model train in terms of training steps? | p. 7 (6 Experiments) |
| Notably π0 performs worse when evaluated after the same number of training steps; we elucidate why in Fig. | p. 9 (6 Experiments) |
| In comparison, π0 trains significantly slower, requiring 7.5 times as many training steps to reach a similar performance. | p. 9 (6 Experiments) |
| As experiments show, having both action representations at training time is crucial. autoregressive decoding with large models, a challenge only exacerbated by ever larger ... | p. 2 (1 Introduction) |
| At inference time, generating continuous actions with the smaller action expert is desirable for fast and precise control, while representation learning with discrete actions ... | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 6 Experiments - extractive PDF cue:** 4a) with a common failure mode of being unable to open the drawer.
- **p. 10 / 6 Experiments - extractive PDF cue:** 7 Discussion & Limitations We analyze the performance, generalization, and language following capabilities of continuousaction VLAs that fine-tune VLMs to output continuous actions, show that ...
- **p. 7 / 6 Experiments - extractive PDF cue:** A common limitation of many robot policies is that they pay much more attention to images than the language input [25].
- **p. 10 / 6 Experiments - extractive PDF cue:** Our method provides an effective recipe for training continuous-action VLAs, but does have limitations.
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 10: Comparison of different state representations on "table bussing" task. Our method works well with both text and continuous state, while π0 works worse ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Problems with standard VLA recipes. The robot is instructed to bus the spoon into the bin. π0 [7] (left) ignores the command and ...

- **PDF anchors reviewed:** datasets p. 9 (6 Experiments), p. 9 (6 Experiments), p. 7 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 10 (6 Experiments), metrics p. 10 (6 Experiments), p. 10 (Figure/Table caption), p. 8 (6 Experiments), p. 9 (6 Experiments), p. 9 (Figure/Table caption), p. 7 (6 Experiments), baselines p. 8 (6 Experiments), p. 7 (6 Experiments), p. 10 (Figure/Table caption), p. 7 (6 Experiments), p. 9 (6 Experiments), p. 8 (6 Experiments), results p. 8 (6 Experiments), p. 10 (Figure/Table caption), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 10 (6 Experiments), p. 7 (6 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
