# Evaluation - Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p071.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p071.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS)): This divergence can be explained by stochasticity on an easy task: if the first CP generation is already earning .98 success rate, subsequent chaining steps may not have much room ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** 1) Robomimic: From the robomimic [17] benchmark suite, we evaluate our method on the Lift, Can, Square and Tool Hang tasks, which compromise all the ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Simulation Experiments Tasks: We evaluate Consistency Policy on six tasks across three benchmarks [9, 10, 17].
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Policy NFE Lift Can Square ToolHang Push-T DDPM 27 1.00 .97 ± .01 .93 ± .02 .79 ± .03 .87 ± .03 DDiM 9 1.00 ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We use a human demonstration dataset of 566 demonstrations and report results for policies using state-based observations.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** This task tests long horizon performance and control of a mobile base along with a standard robot arm (see Fig.
- **p. 9 / IV. EXPERIMENTS - extractive body cue:** The role of dropout in the CTM Objective: Regularization techniques such as dropout [32] are usually used to prevent a highly expressive model from overfitting ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** 2) Plug Insertion: The robot has to pick up a plug and insert it into a socket.
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Success rates and standard errors are presented for each task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | This divergence can be explained by stochasticity on an easy task: if the first CP generation is already earning .98 success rate, subsequent chaining ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | Results: Table IV shows how the baseline DDiM-variant of Diffusion Policy achieves similar average success rates as our method on the Rubbish Clean Up ... | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | On Robomimic Can, single-step CP actually outperforms 3-step CP and registers a marginal improvement over DDPM. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | Trash Clean Up Plug Insertion Microwave Success Inference Success Inference Success Rate Rate Time (ms) Rate Time (ms) DDiM 0.8 ± .13 192 0.6 ... | p. 8 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | We suggest that any user wishing to improve performance on a difficult task begin by trying subdivided discretized time and only attempt further hyperparameter ... | p. 8 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** 1) Robomimic: From the robomimic [17] benchmark suite, we evaluate our method on the Lift, Can, Square and Tool Hang tasks, which compromise all the ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Simulation Experiments Tasks: We evaluate Consistency Policy on six tasks across three benchmarks [9, 10, 17].
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Policy NFE Lift Can Square ToolHang Push-T DDPM 27 1.00 .97 ± .01 .93 ± .02 .79 ± .03 .87 ± .03 DDiM 9 1.00 ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We use a human demonstration dataset of 566 demonstrations and report results for policies using state-based observations.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** This task tests long horizon performance and control of a mobile base along with a standard robot arm (see Fig.
- **p. 9 / IV. EXPERIMENTS - extractive body cue:** The role of dropout in the CTM Objective: Regularization techniques such as dropout [32] are usually used to prevent a highly expressive model from overfitting ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** 2) Plug Insertion: The robot has to pick up a plug and insert it into a socket.
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Success rates and standard errors are presented for each task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action distribution ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: CTM enforces self-consistency along a PFODE (black) by sampling points s, u, t in time such that 0 ≤s < u < t ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Robomimic Tasks. We evaluate our method on the single-robot Robomimic [17] tasks. From left to right, and in increasing order of difficulty, we ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: State-based Simulation Tasks. We also evaluate our method on two state-based tasks: Franka Kitchen [10] (Left) and Push-T [6, 9] (Right). Franka Kitchen ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Rubbish Clean Up. This task involves: (1) picking up trash, (2) placing the trash in the trash can, then (3) closing the lid ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Plug Insertion. This task involves: (1) picking up a power adapter, (2) bringing it to a plug and inserting it completely arm rotation ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Microwave. This task involves: (1) navigating to and opening a microwave, (2) navigating to and picking up a bag of broccoli, (3) placing ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 1) Robomimic: From the robomimic [17] benchmark suite, we evaluate our method on the Lift, Can, Square and Tool Hang tasks, which compromise all ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | Simulation Experiments Tasks: We evaluate Consistency Policy on six tasks across three benchmarks [9, 10, 17]. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 4 (2) Student Model (Consistency Policy)) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 3 (III. CONSISTENCY POLICY), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Metrics: The key metric we report in the Robomimic experiments is the average success rate earned by a particular policy network on the given ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Metrics: For each trained policy, we report average success rates on one policy checkpoint (selected using validation mean-squared error). | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Success rates and standard errors are presented for each task. | definition/direction/unit from same section | p. 8 (IV. EXPERIMENTS) |
| This divergence can be explained by stochasticity on an easy task: if the first CP generation is already earning .98 success rate, subsequent chaining ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Doing so allows us to directly compare the generation speed and success rates of the baselines versus our own. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| For success rates, we average over 10 trials for the first and third tasks while we average over 20 trials for the second task. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Trash Clean Up Plug Insertion Microwave Success Inference Success Inference Success Rate Rate Time (ms) Rate Time (ms) DDiM 0.8 ± .13 192 0.6 ... | definition/direction/unit from same section | p. 8 (IV. EXPERIMENTS) |
| We begin by demonstrating Consistency Policy's strengths in accuracy and inference speed on a variety of common robotics baselines that include both image and ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Thus, we construct an optimistically strong baseline by assuming these speedups can be realized without degrading performance from the standard sequential samplers. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Doing so allows us to directly compare the generation speed and success rates of the baselines versus our own. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Benchmarking was done with vanilla Diffusion Policy since we used this as our baseline. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| On Robomimic Can, single-step CP actually outperforms 3-step CP and registers a marginal improvement over DDPM. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Thus, we choose as our baseline method the faster and more realistic DDiM variant of Diffusion Policy, which uses 15 steps for policy inference. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| Results: Table IV shows how the baseline DDiM-variant of Diffusion Policy achieves similar average success rates as our method on the Rubbish Clean Up ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Finally, we perform ablations over our core design choices and explore the intricacies of our model. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Thus, we construct an optimistically strong baseline by assuming these speedups can be realized without degrading performance from the standard sequential samplers. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Ablations We perform several ablations to validate and explore our design choices. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| Thus, we choose as our baseline method the faster and more realistic DDiM variant of Diffusion Policy, which uses 15 steps for policy inference. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| In our ablation (see Table V) comparing all three objectives, we vary the consistency objective but maintain the auxillary DSM objective as in Eq. | component/input/data sensitivity | p. 8 (IV. EXPERIMENTS) |
| As in other ablations, we think the benefit of this choice is most apparent on harder tasks such as Tool Hang where there is ... | component/input/data sensitivity | p. 8 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, we demonstrate that inference speed of our approach is on average about an order of magnitude faster than the fastest baseline (see Table ... | This divergence can be explained by stochasticity on an easy task: if the first CP generation is already earning .98 success rate, subsequent chaining ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Primary metric/result | Results: Table IV shows how the baseline DDiM-variant of Diffusion Policy achieves similar average success rates as our method on the Rubbish Clean Up ... | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The authors publish average speedups for DDPM and DDiM, the two diffusion schedulers used in Diffusion Policy, of 3.7x and 1.6x respectively.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Diffusion Policy [6] evaluated their models with 100 steps of DDPM and 15 steps of DDiM, so we report 100 3.7 = 27 and 15 ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Policy NFE Lift Can Square ToolHang Push-T DDPM 27 1.00 .97 ± .01 .93 ± .02 .79 ± .03 .87 ± .03 DDiM 9 1.00 ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Policy NFE Inference Time (ms) DDPM 100 110 DDiM 15 11 CP (ours) 1 1 CP (ours) 3 2 Table III: Simulation Inference Speeds - ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Thus, we choose as our baseline method the faster and more realistic DDiM variant of Diffusion Policy, which uses 15 steps for policy inference.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For success rates, we average over 10 trials for the first and third tasks while we average over 20 trials for the second task.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In future work, we will explore how we can potentially re-introduce multimodality to Consistency Policy through more complex sampling schemes. | p. 9 (V. LIMITATIONS) |
| body limitation/failure cue | Single-step CP often falls in between DDPM and DDiM in terms of success rate, especially on the harder tasks such as Square and Tool ... | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | More discussion about the mobile task in particular is present in Limitations see Sec. | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | Note that we are optimistic in assuming that speeding up the baseline DDPM and DDiM Policies [6] with ParaDiGMS [27] does not result in ... | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | ParaDiGMS's experiments do not show any degradation in performance when using parallel sampling, but they do assume access to sufficient compute. | p. 5 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Policy NFE Inference Time (ms) DDPM 100 110 DDiM 15 11 CP (ours) 1 1 CP (ours) 3 2 Table III: Simulation Inference Speeds ... | p. 6 (IV. EXPERIMENTS) |
| We also report inference time on the 3070 Ti GPU. | p. 7 (IV. EXPERIMENTS) |
| We adopt the procedure from ParaDiGMS [27] and compute averages and standard errors using the best checkpoint evaluated 200 times in an online setting. | p. 6 (IV. EXPERIMENTS) |
| Baselines Since our goal is for Consistency Policy to maintain Diffusion Policy's performance while reducing inference time, the DDPM and DDiM variants of Diffusion ... | p. 5 (IV. EXPERIMENTS) |
| However, our method has much lower inference time (∼9x lower latency). | p. 7 (IV. EXPERIMENTS) |
| As an initial step towards exploring this hypothesis, we removed dropout from only the two generations from s →0 at training time while retaining ... | p. 9 (IV. EXPERIMENTS) |
| We sample training times t from a uniform distribution over the discretized timesteps. | p. 4 (2) Student Model (Consistency Policy)) |
| ParaDiGMS's experiments do not show any degradation in performance when using parallel sampling, but they do assume access to sufficient compute. | p. 5 (IV. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / V. LIMITATIONS - extractive body cue:** In future work, we will explore how we can potentially re-introduce multimodality to Consistency Policy through more complex sampling schemes.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Single-step CP often falls in between DDPM and DDiM in terms of success rate, especially on the harder tasks such as Square and Tool Hang, ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** More discussion about the mobile task in particular is present in Limitations see Sec.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Note that we are optimistic in assuming that speeding up the baseline DDPM and DDiM Policies [6] with ParaDiGMS [27] does not result in a ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action distribution ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ParaDiGMS's experiments do not show any degradation in performance when using parallel sampling, but they do assume access to sufficient compute.

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 9 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), baselines p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), results p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
