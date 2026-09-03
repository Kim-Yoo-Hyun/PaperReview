# Evaluation - MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38919; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38919. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 6 (Abstract), p. 6 (Abstract), p. 5 (Abstract), p. 7 (Abstract), p. 7 (Abstract)): Table 1: Performance of different methods on 37 Tasks. We evaluate the performance of our method on 3 Adroit and 34 Meta- World tasks with three random seeds, comparing it ...

## Evaluation Body Digest

- **p. 2 / Abstract - extractive body cue:** Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference latency. ...
- **p. 7 / Abstract - extractive body cue:** 5 reports the performance of different methods in real-world robotic experiments, measured by success rate (%) and average task completion time (s).
- **p. 7 / Abstract - extractive body cue:** 3, we present the performance of MP1 and Flowpolicy on the hammer task in the simulation environment, as well as the experimental results for the ...
- **p. 3 / Abstract - extractive body cue:** MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D point clouds P ...
- **p. 4 / Abstract - extractive body cue:** Such ambiguity is particularly detrimental in robot learning, where subtle differences in object pose or scene configuration are critical for success, especially in few-shot learning ...
- **p. 5 / Abstract - extractive body cue:** Simulation benchmark In simulation, we evaluate the proposed method on three tasks from the Adroit benchmark.
- **p. 2 / Abstract - extractive body cue:** 2022) aligned 2D visual-language features, allowing the robot to generalize to new target tasks.
- **p. 4 / Abstract - extractive body cue:** 2024)) on Adroit Hammer and real-world Hammer tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Performance of different methods on 37 Tasks. We evaluate the performance of our method on 3 Adroit and 34 Meta- World tasks ... | p. 5 (Figure/Table caption) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the 21 "Easy" tasks in Meta-World, the proposed approach achieves a success rate of 88.2%, representing a 3.4% improvement over the FlowPolicy. | p. 6 (Abstract) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | As the number of training steps increases, all methods demonstrate improved success rates; however, MP1 achieves faster convergence and higher final success rates across ... | p. 6 (Abstract) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | The overall average success rate reaches 78.9%±2.1%, which significantly outperforms the previous best method, FlowPolicy, at 71.6%±3.5%. | p. 5 (Abstract) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | As the number of demonstrations increases, the success rate improves significantly across various tasks. | p. 7 (Abstract) |

## Dataset / Benchmark Role

- **p. 2 / Abstract - extractive body cue:** Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference latency. ...
- **p. 7 / Abstract - extractive body cue:** 5 reports the performance of different methods in real-world robotic experiments, measured by success rate (%) and average task completion time (s).
- **p. 7 / Abstract - extractive body cue:** 3, we present the performance of MP1 and Flowpolicy on the hammer task in the simulation environment, as well as the experimental results for the ...
- **p. 3 / Abstract - extractive body cue:** MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D point clouds P ...
- **p. 4 / Abstract - extractive body cue:** Such ambiguity is particularly detrimental in robot learning, where subtle differences in object pose or scene configuration are critical for success, especially in few-shot learning ...
- **p. 5 / Abstract - extractive body cue:** Simulation benchmark In simulation, we evaluate the proposed method on three tasks from the Adroit benchmark.
- **p. 2 / Abstract - extractive body cue:** 2022) aligned 2D visual-language features, allowing the robot to generalize to new target tasks.
- **p. 4 / Abstract - extractive body cue:** 2024)) on Adroit Hammer and real-world Hammer tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: The proposed method outperforms SOTA methods (DP3 (Ze et al. 2024) and FlowPolicy (Zhang et al. 2024)) on the Adroit and Meta-World tasks, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Overview of MP1. The MP1 takes the historical observation point cloud and the robot's state as inputs. These inputs are processed through a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative comparison of the proposed MP1 and the previous SOTA method (FlowPolicy (Zhang et al. 2024)) on Adroit Hammer and real-world Hammer tasks. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Performance of different methods on 37 Tasks. We evaluate the performance of our method on 3 Adroit and 34 Meta- World tasks with ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Comparison of inference times for different methods evaluated on the Meta-World and Adroit benchmark. Due to its multi-step denoising process, Diffusion-based approaches run ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: Ablation Study on Dispersive Loss for Adroit and Meta-World Tasks. -Lossdis signifies that the Dispersive Loss term has been omitted. 0 3K 6K ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Success rate curves of different methods on multi- ple Meta-World tasks. We compare the performance of MP1, FlowPolicy, and DP3 on four tasks. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4: Performance of different flow ratios (when r̸ = t) in Adroit Pen and Meta-World tasks. Fig. 1 and Tab. 2 summarize the inference ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference ... | embodiment, simulator version and control stack | p. 2 (Abstract), p. 7 (Abstract) |
| Task/environment | 5 reports the performance of different methods in real-world robotic experiments, measured by success rate (%) and average task completion time (s). | reset, timeout, object/scene variation | p. 7 (Abstract), p. 7 (Abstract) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 3 (Abstract), p. 3 (Abstract) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 4 (Abstract), p. 4 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: Success rate curves of different methods on multi- ple Meta-World tasks. We compare the performance of MP1, FlowPolicy, and DP3 on four ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| 5 reports the performance of different methods in real-world robotic experiments, measured by success rate (%) and average task completion time (s). | definition/direction/unit from same section | p. 7 (Abstract) |
| MP1 achieves SOTA performance in both success rate and task completion time across all five tasks, with an average success rate of 90% and ... | definition/direction/unit from same section | p. 7 (Abstract) |
| Finally, the overall success rate and standard deviation for the task are computed across all three seeds. | definition/direction/unit from same section | p. 5 (Abstract) |
| Moreover, the proposed method maintains a consistently low standard deviation on certain subtasks (for example, the standard deviation for Adroit Hammer, Door, and the ... | definition/direction/unit from same section | p. 6 (Abstract) |
| Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference ... | definition/direction/unit from same section | p. 2 (Abstract) |
| In the Meta-World tasks, it can be observed that the MP1 achieves a higher success rate on "Very Hard" tasks compared to its performance ... | definition/direction/unit from same section | p. 5 (Abstract) |
| Figure 1: The proposed method outperforms SOTA methods (DP3 (Ze et al. 2024) and FlowPolicy (Zhang et al. 2024)) on the Adroit and Meta-World ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| MP1 is capable of one-step inference and, compared to state-of-the-art (SOTA) methods, improves the average success rate by 7.3% (Tab. | comparison identity and matched condition | p. 2 (Abstract) |
| Table 1: Performance of different methods on 37 Tasks. We evaluate the performance of our method on 3 Adroit and 34 Meta- World tasks ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Figure 1: The proposed method outperforms SOTA methods (DP3 (Ze et al. 2024) and FlowPolicy (Zhang et al. 2024)) on the Adroit and Meta-World ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference ... | comparison identity and matched condition | p. 2 (Abstract) |
| Baselines In our comparison with existing SOTA methods, we include DP (Chi et al. | comparison identity and matched condition | p. 5 (Abstract) |
| 4, performance declines when it reverts to Flow Matching (ratio = 0), compared to the case where r̸ = t. | comparison identity and matched condition | p. 6 (Abstract) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3 compares the standard MP1 with a variant in which the Dispersive Loss is removed. | component/input/data sensitivity | p. 6 (Abstract) |
| Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference ... | component/input/data sensitivity | p. 2 (Abstract) |
| Figure 5: The effect of the number of demonstrations on dif- ferent methods. As the number increases, the success rate gradually improves. Task / | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| 0 2 5 10 20 0 50 100 Success Rate (%) 0 18 19 81 82 0 12 14 66 79 Lever Pull MP1 ... | component/input/data sensitivity | p. 7 (Abstract) |
| Acting as a contrastivestyle regularizer without positive pairs, it sharpens state discrimination while the original regression term still aligns each state to its expert ... | component/input/data sensitivity | p. 2 (Abstract) |
| Furthermore, by encouraging the latent embeddings of different input states to disperse, we improve the model's generalization abilities and task success rate, all without ... | component/input/data sensitivity | p. 3 (Abstract) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework. | Table 1: Performance of different methods on 37 Tasks. We evaluate the performance of our method on 3 Adroit and 34 Meta- World tasks ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 6 (Abstract), p. 6 (Abstract), p. 5 (Abstract), p. 7 (Abstract), p. 7 (Abstract) |
| Primary metric/result | On the 21 "Easy" tasks in Meta-World, the proposed approach achieves a success rate of 88.2%, representing a 3.4% improvement over the FlowPolicy. | numeric claim only at cited anchor | p. 6 (Abstract) |

- Numeric sentences retained from the body:
- **p. 2 / Abstract - extractive body cue:** For example, MeanFlow can reduce inference latency to around 6.8 ms, far better than the 10-20 steps required by diffusion strategies.
- **p. 4 / Abstract - extractive body cue:** MP1 FlowPolicy Adroit: Hammer (FlowPolicy: 15.3ms/ MP1:7.1ms) Real-world: Hammer (FlowPolicy: 22.3s/ MP1:18.6s) failure success Figure 3: Qualitative comparison of the proposed MP1 and the previous ...
- **p. 4 / Abstract - extractive body cue:** Our method is faster, with 7.1ms in the simulated hammer and 18.6s in the real-world scenario.
- **p. 5 / Abstract - extractive body cue:** Methods Publication NFE Adroit Meta-World Average Hammer Door Pen Easy (21) Medium (4) Hard (4) Very Hard (5) DP RSS'23 10 16±10 34±11 13±2 50.7±6.1 ...
- **p. 5 / Abstract - extractive body cue:** Methods Publication NFE Adroit /ms Meta-World /ms Average /ms Hammer Door Pen Easy (21) Medium (4) Hard (4) Very Hard (5) DP3 RSS'24 10 129.5±13.9 ...
- **p. 5 / Abstract - extractive body cue:** MP1 achieves SOTA inference speed across all sub-tasks, with an average latency of just 6.8 ms-nearly 2× faster than the best FlowPolicy (which relies on ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | MP1 FlowPolicy Adroit: Hammer (FlowPolicy: 15.3ms/ MP1:7.1ms) Real-world: Hammer (FlowPolicy: 22.3s/ MP1:18.6s) failure success Figure 3: Qualitative comparison of the proposed MP1 and the ... | p. 4 (Abstract) |
| body limitation/failure cue | 3D Input Robot Learning To overcome the limitations of 2D inputs, 3D inputs have gained prominence. | p. 2 (Abstract) |
| body limitation/failure cue | However, a purely regression-based objective fails to impose explicit regularization on the policy's internal feature space (Wang and He 2025). | p. 2 (Abstract) |
| body limitation/failure cue | Moreover, our method successfully completes the real-world hammer task, whereas FlowPolicy fails. estimate of the total derivative, with a stop-gradient sg(·) to ensure stability: ... | p. 4 (Abstract) |
| body limitation/failure cue | Conclusion In this paper, we address the limitations of existing Diffusion-based and Flow-based approaches by introducing MeanFlow into robot learning. | p. 7 (Abstract) |
| body limitation/failure cue | Unlike Diffusion-based methods, our approach does not require multi-step denoising; distinct from existing Flowbased approaches, the MP1 does not rely on ODE solvers, consistency ... | p. 3 (Abstract) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All training and testing are performed on an NVIDIA RTX 4090 GPU, with a batch size of 128, optimization uses the AdamW optimizer with ... | p. 5 (Abstract) |
| This Lcfg is combined with a Dispersive Loss (Ldisp) imposed on the UNet's hidden states to jointly optimize the network parameters. inference time due ... | p. 3 (Abstract) |
| We conduct inference speed tests for three seeds on the same GPU. | p. 5 (Abstract) |
| However, a notable drawback of Diffusion Models is their relatively long inference time. | p. 1 (Abstract) |
| Its average inference time is only 6.8 ms-19× faster than DP3 and nearly 2× faster than FlowPolicy. | p. 1 (Abstract) |
| However, diffusion still faces challenges related to inference time. | p. 2 (Abstract) |
| On an NVIDIA 4090, our method attains an average inference time of 6.8 ms. | p. 6 (Abstract) |
| Because Dispersive Loss is computed once per forward pass and vanishes at inference, MP1 preserves its hallmark 1-NFE speed. | p. 2 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Abstract - extractive body cue:** MP1 FlowPolicy Adroit: Hammer (FlowPolicy: 15.3ms/ MP1:7.1ms) Real-world: Hammer (FlowPolicy: 22.3s/ MP1:18.6s) failure success Figure 3: Qualitative comparison of the proposed MP1 and the previous ...
- **p. 2 / Abstract - extractive body cue:** 3D Input Robot Learning To overcome the limitations of 2D inputs, 3D inputs have gained prominence.
- **p. 2 / Abstract - extractive body cue:** However, a purely regression-based objective fails to impose explicit regularization on the policy's internal feature space (Wang and He 2025).
- **p. 4 / Abstract - extractive body cue:** Moreover, our method successfully completes the real-world hammer task, whereas FlowPolicy fails. estimate of the total derivative, with a stop-gradient sg(·) to ensure stability: utgt ...
- **p. 7 / Abstract - extractive body cue:** Conclusion In this paper, we address the limitations of existing Diffusion-based and Flow-based approaches by introducing MeanFlow into robot learning.
- **p. 3 / Abstract - extractive body cue:** Unlike Diffusion-based methods, our approach does not require multi-step denoising; distinct from existing Flowbased approaches, the MP1 does not rely on ODE solvers, consistency constraints, ...

- **Evidence anchors reviewed:** datasets p. 2 (Abstract), p. 7 (Abstract), p. 7 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 5 (Abstract), metrics p. 6 (Figure/Table caption), p. 7 (Abstract), p. 7 (Abstract), p. 5 (Abstract), p. 6 (Abstract), p. 2 (Abstract), baselines p. 2 (Abstract), p. 5 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Abstract), p. 5 (Abstract), p. 6 (Abstract), results p. 5 (Figure/Table caption), p. 6 (Abstract), p. 6 (Abstract), p. 5 (Abstract), p. 7 (Abstract), p. 7 (Abstract).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 6: Real-world setup. Real-world Experimental Results In Fig. 3, we present the performance of MP1 and Flowpol- icy on the hammer task in the simulation environment, as well as ... (p. 7, Figure/Table caption).
- **Metric evidence:** 5 reports the performance of different methods in real-world robotic experiments, measured by success rate (%) and average task completion time (s). (p. 7, Abstract).
- **Baseline/ablation evidence:** MP1 is capable of one-step inference and, compared to state-of-the-art (SOTA) methods, improves the average success rate by 7.3% (Tab. (p. 2, Abstract).
- **Failure/negative evidence:** However, a purely regression-based objective fails to impose explicit regularization on the policy's internal feature space (Wang and He 2025). (p. 2, Abstract).
