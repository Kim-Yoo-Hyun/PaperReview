# Evaluation - Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.07343; PDF retrieval source: https://arxiv.org/pdf/2409.07343. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Abstract), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (1 Introduction), p. 2 (1 Introduction)): We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, double the performance of the next ...

## Evaluation Body Digest

- **p. 1 / Abstract - extractive body cue:** Learning from expert demonstrations is a promising approach for training robotic manipulation policies from limited data.
- **p. 1 / 1 Introduction - extractive body cue:** While BC has achieved significant success for different tasks, robot policy learning remains a challenging problem, given the requirement of high precision, the sequential correlation ...
- **p. 2 / 1 Introduction - extractive body cue:** Inspired by recent flow-based generative models, we propose PointFlowMatch, a novel imitation learning algorithm for robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** PointFlowMatch uses point cloud observations that prove to be more effective than images [9, 10] and builds upon a CFM formulation to learn the distribution ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as well ...
- **p. 1 / Abstract - extractive body cue:** We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, double ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Ablation of observation type (images vs point clouds), vector field formulation (R6 vs SO(3)), and training objective (DDIM vs CFM) for our method, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Comparison of CFM and DDIM for varying values of the number of inference steps k. We compare the inference time (↓) measured in ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** A Additional Experiments (p. 11).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, ... | p. 1 (Abstract) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2: Ablation of observation type (images vs point clouds), vector field formulation (R6 vs SO(3)), and training objective (DDIM vs CFM) for our ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 3: Comparison of CFM and DDIM for varying values of the number of inference steps k. We compare the inference time (↓) measured ... | p. 7 (Figure/Table caption) |
| 1 Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | While BC has achieved significant success for different tasks, robot policy learning remains a challenging problem, given the requirement of high precision, the sequential ... | p. 1 (1 Introduction) |

## Dataset / Benchmark Role

- **p. 1 / Abstract - extractive body cue:** Learning from expert demonstrations is a promising approach for training robotic manipulation policies from limited data.
- **p. 1 / 1 Introduction - extractive body cue:** While BC has achieved significant success for different tasks, robot policy learning remains a challenging problem, given the requirement of high precision, the sequential correlation ...
- **p. 2 / 1 Introduction - extractive body cue:** Inspired by recent flow-based generative models, we propose PointFlowMatch, a novel imitation learning algorithm for robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** PointFlowMatch uses point cloud observations that prove to be more effective than images [9, 10] and builds upon a CFM formulation to learn the distribution ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 1: Diffusion and CFM are repeatedly applied to a noisy trajectory, thereby iteratively yielding a clean trajectory that can be executed on the robot. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Example images of the eight RLBench tasks.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as well ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Ablation of observation type (images vs point clouds), vector field formulation (R6 vs SO(3)), and training objective (DDIM vs CFM) for our method, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Comparison of CFM and DDIM for varying values of the number of inference steps k. We compare the inference time (↓) measured in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: We demonstrate PointFlowMatch on a real robotic setup. We evaluate on two tasks: open box and sponge on plate. 4.3 Real Robot Experiments ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 5: Simplified Example. The left figure shows the edge case when random samples are close to the opposite pole of the target sample. Here ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Comparison of different state dimensions and their respective velocities, target calculation and pro- gression formulations. For definitions of the Log(•)- and Exp(•)-maps we ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Learning from expert demonstrations is a promising approach for training robotic manipulation policies from limited data. | embodiment, simulator version and control stack | p. 1 (Abstract), p. 1 (1 Introduction) |
| Task/environment | While BC has achieved significant success for different tasks, robot policy learning remains a challenging problem, given the requirement of high precision, the sequential ... | reset, timeout, object/scene variation | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 1 (Abstract), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, ... | definition/direction/unit from same section | p. 1 (Abstract) |
| Table 2: Ablation of observation type (images vs point clouds), vector field formulation (R6 vs SO(3)), and training objective (DDIM vs CFM) for our ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 3: Comparison of CFM and DDIM for varying values of the number of inference steps k. We compare the inference time (↓) measured ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Most prominently, Diffusion Policy [6] adopts a score-matching formulation of generative diffusion models. | definition/direction/unit from same section | p. 1 (1 Introduction) |
| Figure 5: Simplified Example. The left figure shows the edge case when random samples are close to the opposite pole of the target sample. ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| In the typical case of Gaussians, a closed-form solution is available, enabling us to directly generate fully noised and intermediate, partially noised, samples. | definition/direction/unit from same section | p. 2 (1 Introduction) |
| We evaluate the performance of our proposed method on the popular RLBench benchmark [14] and compare it against strong recent baselines with both image ... | definition/direction/unit from same section | p. 2 (1 Introduction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 2: Ablation of observation type (images vs point clouds), vector field formulation (R6 vs SO(3)), and training objective (DDIM vs CFM) for our ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, ... | comparison identity and matched condition | p. 1 (Abstract) |
| While BC has achieved significant success for different tasks, robot policy learning remains a challenging problem, given the requirement of high precision, the sequential ... | comparison identity and matched condition | p. 1 (1 Introduction) |
| We evaluate the performance of our proposed method on the popular RLBench benchmark [14] and compare it against strong recent baselines with both image ... | comparison identity and matched condition | p. 2 (1 Introduction) |
| Figure 3: Comparison of CFM and DDIM for varying values of the number of inference steps k. We compare the inference time (↓) measured ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| CFM is a simulation-free approach, i.e. it starts directly from noise without requiring a forward diffusion process. | component/input/data sensitivity | p. 2 (1 Introduction) |
| Table 2: Ablation of observation type (images vs point clouds), vector field formulation (R6 vs SO(3)), and training objective (DDIM vs CFM) for our ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 3: Comparison of CFM and DDIM for varying values of the number of inference steps k. We compare the inference time (↓) measured ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Inspired by recent flow-based generative models, we propose PointFlowMatch, a novel imitation learning algorithm for robotic manipulation. | We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Abstract), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Primary metric/result | Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In addition to this, as usual in the fixed-data imitation learning setting, CFM cannot extrapolate out of distribution and thus, only learns motion correction ... | p. 8 (5 Conclusion) |
| body limitation/failure cue | Limitations: There are a few limitations to our proposed method. | p. 8 (5 Conclusion) |
| body limitation/failure cue | To overcome these limitations, Conditional Flow Matching (CFM) has been proposed as an efficient generalization of diffusion models [12, 13, 11]. | p. 2 (1 Introduction) |
| body limitation/failure cue | The forward diffusion process starts with expert robot trajectories and gradually adds Gaussian noise until the signal approximates pure noise. | p. 1 (1 Introduction) |
| body limitation/failure cue | This is a stochastic process that results in Gaussian conditional probability paths mapping Gaussian noise to data, with specific choices of mean and standard ... | p. 1 (1 Introduction) |
| body limitation/failure cue | CFM is a simulation-free approach, i.e. it starts directly from noise without requiring a forward diffusion process. | p. 2 (1 Introduction) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In turn, in the cases where no closed-form solution for the forward diffusion process is available, training time will increase [11]. | p. 2 (1 Introduction) |
| The denoising process reverts these steps and it is used as a training signal for the model. | p. 1 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Conclusion - extractive body cue:** In addition to this, as usual in the fixed-data imitation learning setting, CFM cannot extrapolate out of distribution and thus, only learns motion correction behavior ...
- **p. 8 / 5 Conclusion - extractive body cue:** Limitations: There are a few limitations to our proposed method.
- **p. 2 / 1 Introduction - extractive body cue:** To overcome these limitations, Conditional Flow Matching (CFM) has been proposed as an efficient generalization of diffusion models [12, 13, 11].
- **p. 1 / 1 Introduction - extractive body cue:** The forward diffusion process starts with expert robot trajectories and gradually adds Gaussian noise until the signal approximates pure noise.
- **p. 1 / 1 Introduction - extractive body cue:** This is a stochastic process that results in Gaussian conditional probability paths mapping Gaussian noise to data, with specific choices of mean and standard deviation ...
- **p. 2 / 1 Introduction - extractive body cue:** CFM is a simulation-free approach, i.e. it starts directly from noise without requiring a forward diffusion process.

- **Evidence anchors reviewed:** datasets p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), metrics p. 6 (Figure/Table caption), p. 1 (Abstract), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (1 Introduction), p. 11 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 7 (Figure/Table caption), results p. 1 (Abstract), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (1 Introduction), p. 2 (1 Introduction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as well as the delta to our ... (p. 6, Figure/Table caption).
- **Metric evidence:** We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, double the performance of the next ... (p. 1, Abstract).
- **Baseline/ablation evidence:** Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as well as the delta to our ... (p. 6, Figure/Table caption).
- **Failure/negative evidence:** In addition to this, as usual in the fixed-data imitation learning setting, CFM cannot extrapolate out of distribution and thus, only learns motion correction behavior when included in the demonstration ... (p. 8, 5 Conclusion).
