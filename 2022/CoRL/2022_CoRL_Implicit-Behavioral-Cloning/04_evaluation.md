# Evaluation - Implicit Behavioral Cloning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v164/florence22a.html; PDF retrieval source: https://arxiv.org/pdf/2109.00137. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract), p. 1 (1 Introduction), p. 6 (1 Introduction)): Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations each, with ± std. dev. Baselines from [26] ...

## Evaluation Body Digest

- **p. 6 / 1 Introduction - extractive body cue:** Real-world robot results, success % shown is mean +/- std.dev (20 rollouts per seed, 3 seeds = 60 trials per method per task).
- **p. 7 / 1 Introduction - extractive body cue:** Results using our hardware configuration (a, see Appendix for full description) on real-world visual manipulation tasks, including (b) multi-modal targeted block pushing, (c) precise oriented ...
- **p. 4 / 1 Introduction - extractive body cue:** Standard deviations are shown in Tables 2, 3, 4, 5, 6. image human unknown multimodal Benchmark input demos cardinality solutions D4RL Human-Experts    ...
- **p. 1 / Abstract - extractive body cue:** In the real world, robots with implicit policies can learn complex and remarkably subtle behaviors on contact-rich tasks from human demonstrations, including tasks with high ...
- **p. 2 / 1 Introduction - extractive body cue:** For learning complex, closed-loop, multimodal visuomotor tasks such as precise block insertion (c) and sorting (d) from human demonstrations, implicit policies perform substantially better than ...
- **p. 4 / 1 Introduction - extractive body cue:** We evaluate our implicit (EBM) and explicit (MSE) policies across the subset of tasks for which offline datasets of human demonstrations are provided, which is ...
- **p. 5 / 1 Introduction - extractive body cue:** We train implicit (EBM) and explicit (MSE) policies from 50 teleoperated human demonstrations, and test on episodes with unseen particle configurations.
- **p. 1 / Abstract - extractive body cue:** We find these policies provide competitive results or outperform state-of-the-art offline reinforcement learning methods on the challenging human-expert tasks from the D4RL benchmark suite, despite ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** C.3 Additional Real-World Experimental Details (p. 13); C Additional Experimental Details and Analysis (p. 17); C.3 Additional Real-World Experimental Details (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations each, with ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 6. Real-world robot results, success % shown is mean +/- std.dev (20 rollouts per seed, 3 seeds = 60 trials per method per ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 9. Results using our hardware configuration (a, see Appendix for full description) on real-world visual manipulation tasks, including (b) multi-modal targeted block pushing, ... | p. 7 (Figure/Table caption) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find these policies provide competitive results or outperform state-of-the-art offline reinforcement learning methods on the challenging human-expert tasks from the D4RL benchmark suite, ... | p. 1 (Abstract) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our experiments show that this simple change can lead to remarkable improvements in performance across a wide range of contact-rich tasks: from bi-manually scooping ... | p. 1 (1 Introduction) |

## Dataset / Benchmark Role

- **p. 6 / 1 Introduction - extractive body cue:** Real-world robot results, success % shown is mean +/- std.dev (20 rollouts per seed, 3 seeds = 60 trials per method per task).
- **p. 7 / 1 Introduction - extractive body cue:** Results using our hardware configuration (a, see Appendix for full description) on real-world visual manipulation tasks, including (b) multi-modal targeted block pushing, (c) precise oriented ...
- **p. 4 / 1 Introduction - extractive body cue:** Standard deviations are shown in Tables 2, 3, 4, 5, 6. image human unknown multimodal Benchmark input demos cardinality solutions D4RL Human-Experts    ...
- **p. 1 / Abstract - extractive body cue:** In the real world, robots with implicit policies can learn complex and remarkably subtle behaviors on contact-rich tasks from human demonstrations, including tasks with high ...
- **p. 2 / 1 Introduction - extractive body cue:** For learning complex, closed-loop, multimodal visuomotor tasks such as precise block insertion (c) and sorting (d) from human demonstrations, implicit policies perform substantially better than ...
- **p. 4 / 1 Introduction - extractive body cue:** We evaluate our implicit (EBM) and explicit (MSE) policies across the subset of tasks for which offline datasets of human demonstrations are provided, which is ...
- **p. 5 / 1 Introduction - extractive body cue:** We train implicit (EBM) and explicit (MSE) policies from 50 teleoperated human demonstrations, and test on episodes with unseen particle configurations.
- **p. 1 / Abstract - extractive body cue:** We find these policies provide competitive results or outperform state-of-the-art offline reinforcement learning methods on the challenging human-expert tasks from the D4RL benchmark suite, despite ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. (a) In contrast to explicit policies, implicit policies leverage parameterized energy functions that take both observations (e.g. images) and actions as inputs, and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Comparison between implicit vs explicit learning of 1D functions, R1 →R1, showing extrapolation (outside of x=[0,1]) behavior beyond training samples and detailed views ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Representations of multi-valued functions showing extrapolations beyond the training samples (outside of shown ‘X' training samples) and detail views of notable regions. (a,d) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Comparison of implicit and explicit ConvMLP models on a simple coordinate regression task [23], RW×H×C →R2 (a). The architectures shown in (b) are ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 5. Comparisons between implicit and explicit policies across 6 various simulated and real domains (Table 1), including author-reported baselines on the human-expert D4RL tasks. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Each benchmark is characterized by a unique set of attributes. We evaluate implicit models for learning BC policies across a variety of robotic ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations each, with ± ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Comparison of policy performance on the N-D particle environment, 2,000 demonstrations each. N-D Particle Integrator is a simple environment with linear dynamics but ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-world robot results, success % shown is mean +/- std.dev (20 rollouts per seed, 3 seeds = 60 trials per method per task). | embodiment, simulator version and control stack | p. 6 (1 Introduction), p. 7 (1 Introduction) |
| Task/environment | Results using our hardware configuration (a, see Appendix for full description) on real-world visual manipulation tasks, including (b) multi-modal targeted block pushing, (c) precise ... | reset, timeout, object/scene variation | p. 7 (1 Introduction), p. 4 (1 Introduction) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 1 (Abstract) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 6 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 6. Real-world robot results, success % shown is mean +/- std.dev (20 rollouts per seed, 3 seeds = 60 trials per method per ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 9. Results using our hardware configuration (a, see Appendix for full description) on real-world visual manipulation tasks, including (b) multi-modal targeted block pushing, ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations each, with ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| The failures of the Nearest-Neighbor baseline, with only 0-4% success rate, show that generalization is required for this task. | definition/direction/unit from same section | p. 5 (1 Introduction) |
| For any set-valued function F(x): x∈Rm→P(Rn)\{∅}, there exists a function g(·) that can be approximated by some continuous function approximator gθ(·) with arbitrarily small ... | definition/direction/unit from same section | p. 7 (1 Introduction) |
| We find these policies provide competitive results or outperform state-of-the-art offline reinforcement learning methods on the challenging human-expert tasks from the D4RL benchmark suite, ... | definition/direction/unit from same section | p. 1 (Abstract) |
| On robotic policy learning tasks we show that implicit behavioral cloning policies with energy-based models (EBM) often outperform common explicit (Mean Square Error, or ... | definition/direction/unit from same section | p. 1 (Abstract) |
| Explicit "MSE" models are trained with Mean Square Error (MSE), explicit "MDN" models are Mixture Density Networks (MDN) [21], and implicit "EBM" models are ... | definition/direction/unit from same section | p. 2 (1 Introduction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations each, with ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| We find these policies provide competitive results or outperform state-of-the-art offline reinforcement learning methods on the challenging human-expert tasks from the D4RL benchmark suite, ... | comparison identity and matched condition | p. 1 (Abstract) |
| Results show that implicit models for BC exhibit the capacity to learn long-horizon, closed-loop visuomotor tasks better than their explicit counterparts - and surprisingly, ... | comparison identity and matched condition | p. 1 (1 Introduction) |
| Across all four tasks, we observe significantly higher performance for the implicit policies compared to the explicit baseline. | comparison identity and matched condition | p. 6 (1 Introduction) |
| Comparisons between implicit and explicit policies across 6 various simulated and real domains (Table 1), including author-reported baselines on the human-expert D4RL tasks. | comparison identity and matched condition | p. 4 (1 Introduction) |
| Figure 6. Comparison of policy performance on the N-D particle environment, 2,000 demonstrations each. N-D Particle Integrator is a simple environment with linear dynamics ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We evaluate implicit (EBM) and explicit (MSE and MDN [30, 31]) policies on both variants, trained from a dataset of 2,000 demonstrations using a ... | component/input/data sensitivity | p. 5 (1 Introduction) |
| Table 3. Results on simulated xArm6 pushing tasks, average of 3 random seeds, 100 evaluations each, with ± std. dev. Simulated Pushing consists of ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Implicit models are able to approximate discontinuities sharply without introducing intermediate artifacts (Fig. | component/input/data sensitivity | p. 2 (1 Introduction) |
| To demonstrate a breadth of approaches, we present results with three different EBM training and inference methods discussed below, however a comprehensive comparison of ... | component/input/data sensitivity | p. 2 (1 Introduction) |
| Once the training data is uncorrelated (i.e. random noise) and without regularization (Fig. | component/input/data sensitivity | p. 3 (1 Introduction) |
| The red/green pushing tasks, including multi-modal variant (Fig. | component/input/data sensitivity | p. 7 (1 Introduction) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose to reformulate BC using implicit models - specifically, the composition of argmin with a continuous energy function Eθ (see ... | Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations each, with ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract), p. 1 (1 Introduction), p. 6 (1 Introduction) |
| Primary metric/result | Table 6. Real-world robot results, success % shown is mean +/- std.dev (20 rollouts per seed, 3 seeds = 60 trials per method per ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 1 Introduction - extractive body cue:** Baselines Ours Explicit Implicit Explicit Implicit Method NearestBC CQL [26] S4RL [27] BC (MSE) BC (EBM) BC (MSE) BC (EBM) Neighbor (from CQL [26]) w/ ...
- **p. 5 / 1 Introduction - extractive body cue:** 5, shown for N = 2), the policy must switch to the second goal.
- **p. 5 / 1 Introduction - extractive body cue:** Varying N from 1 to 32 dimensions, but holding the number of demonstrations constant, we find we are able to train 95% successful implicit policies ...
- **p. 5 / 1 Introduction - extractive body cue:** Method Single Target, Multi Target, Single Target, states states pixels EBM 100 ±0 99.0 ±0.0 100 ±0 MDN 100 ±0 99.7 ±0.5 10.0 ±4.3 MSE ...
- **p. 5 / 1 Introduction - extractive body cue:** The agent has 3 degrees of freedom (2 for position, 1 for orientation).
- **p. 6 / 1 Introduction - extractive body cue:** For the state-based inputs, since the number of particles vary between episodes, we flatten the poses of the particles and 0-pad the vector to match ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In terms of limitations, a primary comparison with explicit models is that they typically require more compute, both in training and inference (see Appendix ... | p. 8 (7 Conclusion) |
| body limitation/failure cue | The failures of the Nearest-Neighbor baseline, with only 0-4% success rate, show that generalization is required for this task. | p. 5 (1 Introduction) |
| body limitation/failure cue | Although considerable research has been devoted to developing new imitation learning methods [7, 8, 9] to address BC's known limitations, here we investigate a ... | p. 1 (1 Introduction) |
| body limitation/failure cue | The Nearest-Neighbor baseline, meanwhile, cannot generalize, and only performs well on the 1D task (see Appendix for more analysis). | p. 5 (1 Introduction) |
| body limitation/failure cue | Once the training data is uncorrelated (i.e. random noise) and without regularization (Fig. | p. 3 (1 Introduction) |
| body limitation/failure cue | (a,d) Single discontinuity between constant values; (b,e) piecewise continuous sections with differing dy dx, (c,f) random Gaussian noise, for unregularized models. | p. 3 (1 Introduction) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Real-world robot results, success % shown is mean +/- std.dev (20 rollouts per seed, 3 seeds = 60 trials per method per task). | p. 6 (1 Introduction) |
| 1), and at inference time (given o) performs implicit regression by optimizing for the optimal action ˆa via sampling or gradient descent [11, 12]. | p. 1 (1 Introduction) |
| Explicit ReLU-MLP trained as MDN 1:512:512:10 gaussians 5k steps shown density is: Implicit ReLU-MLP trained as EBM 2:512:512:1 5k steps shown density is: normalized ... | p. 3 (1 Introduction) |
| Surprisingly, we find that our implementations of 4 | p. 4 (1 Introduction) |
| Results shown are the average of 3 random seeds, 100 evaluations each, with ± std. dev. | p. 5 (1 Introduction) |
| For the image-based inputs, we also test two types of encoders with different forms of dimensionality reduction: spatial soft(arg)max and average pooling over dense ... | p. 5 (1 Introduction) |
| EBM and MSE policies on the task use the best corresponding image encoder from the planar sweeping task. | p. 6 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7 Conclusion - extractive body cue:** In terms of limitations, a primary comparison with explicit models is that they typically require more compute, both in training and inference (see Appendix for ...
- **p. 5 / 1 Introduction - extractive body cue:** The failures of the Nearest-Neighbor baseline, with only 0-4% success rate, show that generalization is required for this task.
- **p. 1 / 1 Introduction - extractive body cue:** Although considerable research has been devoted to developing new imitation learning methods [7, 8, 9] to address BC's known limitations, here we investigate a fundamental ...
- **p. 5 / 1 Introduction - extractive body cue:** The Nearest-Neighbor baseline, meanwhile, cannot generalize, and only performs well on the 1D task (see Appendix for more analysis).
- **p. 3 / 1 Introduction - extractive body cue:** Once the training data is uncorrelated (i.e. random noise) and without regularization (Fig.
- **p. 3 / 1 Introduction - extractive body cue:** (a,d) Single discontinuity between constant values; (b,e) piecewise continuous sections with differing dy dx, (c,f) random Gaussian noise, for unregularized models.

- **Evidence anchors reviewed:** datasets p. 6 (1 Introduction), p. 7 (1 Introduction), p. 4 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 4 (1 Introduction), metrics p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 5 (1 Introduction), p. 7 (1 Introduction), p. 1 (Abstract), baselines p. 5 (Figure/Table caption), p. 1 (Abstract), p. 1 (1 Introduction), p. 6 (1 Introduction), p. 4 (1 Introduction), p. 5 (Figure/Table caption), results p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract), p. 1 (1 Introduction), p. 6 (1 Introduction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations each, with ± std. dev. Baselines from [26] ... (p. 5, Figure/Table caption).
- **Metric evidence:** Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations each, with ± std. dev. Baselines from [26] ... (p. 5, Figure/Table caption).
- **Baseline/ablation evidence:** Table 2. Baseline comparisons on D4RL [17] tasks with human-expert data. Results shown are the average of 3 random seeds, 100 evaluations each, with ± std. dev. Baselines from [26] ... (p. 5, Figure/Table caption).
- **Failure/negative evidence:** The failures of the Nearest-Neighbor baseline, with only 0-4% success rate, show that generalization is required for this task. (p. 5, 1 Introduction).
