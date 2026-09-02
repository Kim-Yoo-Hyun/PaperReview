# Evaluation - Evaluating Real-World Robot Manipulation Policies in Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=LZh48DTg71; PDF retrieval source: https://arxiv.org/pdf/2405.05941.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor), p. 10 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor)): Thus, the approaches we introduced in Section IV-B for narrowing the visual gap between simulated and real scene can significantly improve real-andsim evaluation performance correlation, but only if applied jointly ...

## Evaluation Body Digest

- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Models that obtain low real-world performance, such as RT1 (Begin) on Google Robot tasks and RT-1-X on BridgeData V2 tasks, similarly have low performance in ...
- **p. 9 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** We use the RT-1 (Converged), RT-1 (Begin), and RT1-X checkpoints on the Google robot drawer opening and closing tasks, and we compare the correlations between ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** In this section, we empirically test the performance correlation between real-world robot evaluations and simulated evaluations in SIMPLER environments for a representative set of open-source ...
- **p. 9 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** To test whether this trend observed in simulation holds in real-world evaluations, we design a novel realworld distribution shift evaluation, where we change the real ...
- **p. 7 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** 4) When building simulation environments, we simplified object and robot's physical properties like center of mass and static & dynamic friction, as their precise modeling ...
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Additionally, we find that some policies have higher sensitivity to visual differences between simulation and real-world environments.
- **p. 10 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** When developing SIMPLER environments, we simplified the physical properties (e.g., center of mass and friction coefficients) of objects and robots due to the complexity and ...
- **p. 10 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Green Screen Drawer Matching Robot Matching MMRV ↓ Real-Sim Success Gap ↓ ✗ ✗ ✗ 0.087 0.272 ✗ ✓ ✗ 0.087 0.266 ✗ ✗ ✓ ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** VI. EXPERIMENTAL RESULTS (p. 7); 2) Can simulated evaluations not only capture the perfor (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 2) Can simulated evaluations not only capture the perfor | BENCHMARK / DATASET | Thus, the approaches we introduced in Section IV-B for narrowing the visual gap between simulated and real scene can significantly improve real-andsim evaluation performance ... | p. 10 (2) Can simulated evaluations not only capture the perfor) |
| 2) Can simulated evaluations not only capture the perfor | BENCHMARK / DATASET | For Octo simulated evaluations, since the model involves a non-deterministic diffusion head, we average its success rates across three different random seeds to produce ... | p. 7 (2) Can simulated evaluations not only capture the perfor) |
| 2) Can simulated evaluations not only capture the perfor | BENCHMARK / DATASET | We observe a strong correlation between the relative performances in simulation and in the real world across most policy checkpoints 0.0 0.2 0.4 0.6 ... | p. 7 (2) Can simulated evaluations not only capture the perfor) |
| 2) Can simulated evaluations not only capture the perfor | BENCHMARK / DATASET | For simulated results and realworld results, we report the difference in success rate with and without each distribution shift: ∆Success(shift) = 1 2 2 ... | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| 2) Can simulated evaluations not only capture the perfor | BENCHMARK / DATASET | To investigate whether our results are sensitive to the underlying physics simulator, we reproduce the Google Robot evaluation in Isaac Simulator Ablation SAPIEN MMRV ... | p. 10 (2) Can simulated evaluations not only capture the perfor) |

## Dataset / Benchmark Role

- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Models that obtain low real-world performance, such as RT1 (Begin) on Google Robot tasks and RT-1-X on BridgeData V2 tasks, similarly have low performance in ...
- **p. 9 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** We use the RT-1 (Converged), RT-1 (Begin), and RT1-X checkpoints on the Google robot drawer opening and closing tasks, and we compare the correlations between ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** In this section, we empirically test the performance correlation between real-world robot evaluations and simulated evaluations in SIMPLER environments for a representative set of open-source ...
- **p. 9 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** To test whether this trend observed in simulation holds in real-world evaluations, we design a novel realworld distribution shift evaluation, where we change the real ...
- **p. 7 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** 4) When building simulation environments, we simplified object and robot's physical properties like center of mass and static & dynamic friction, as their precise modeling ...
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Additionally, we find that some policies have higher sensitivity to visual differences between simulation and real-world environments.
- **p. 10 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** When developing SIMPLER environments, we simplified the physical properties (e.g., center of mass and friction coefficients) of objects and robots due to the complexity and ...
- **p. 10 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Green Screen Drawer Matching Robot Matching MMRV ↓ Real-Sim Success Gap ↓ ✗ ✗ ✗ 0.087 0.272 ✗ ✓ ✗ 0.087 0.266 ✗ ✗ ✓ ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Characterizing generalist robot manipulation policies typically involves evaluating them on many tasks across many scenarios, a laborious undertaking in the real world (top ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: We introduce SIMPLER, a suite of open-source simulated evaluation environments for common real robot manipulation setups, namely the Google Robot evaluations from the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and Pearson correlation coefficient (Pearson r, range [-1, 1], higher ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We perform system identification (SysID) for closing the control gap between real and simulated environments. We visualize the open-loop execution of demonstration actions ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Illustration of our "Visual Matching" approach for reducing the visual appearance gap between real environments and raw simula- tion. Visual Matching consists of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Real vs. SIMPLER success rates on Google Robot tasks. SIMPLER environments with the "Visual Matching" evaluation setup show strong correlation to real policy ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Real vs. simulation success rates for BridgeData V2 tasks. SIMPLER evaluations have strong correlation with real policy per- formance: for all but one ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Change in success rate under various distribution shifts for two RT-1 policies trained without and with data augmentation. Success rates are averaged across ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Models that obtain low real-world performance, such as RT1 (Begin) on Google Robot tasks and RT-1-X on BridgeData V2 tasks, similarly have low performance ... | embodiment, simulator version and control stack | p. 8 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor) |
| Task/environment | We use the RT-1 (Converged), RT-1 (Begin), and RT1-X checkpoints on the Google robot drawer opening and closing tasks, and we compare the correlations ... | reset, timeout, object/scene variation | p. 9 (2) Can simulated evaluations not only capture the perfor), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (Abstract), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For Octo simulated evaluations, since the model involves a non-deterministic diffusion head, we average its success rates across three different random seeds to produce ... | definition/direction/unit from same section | p. 7 (2) Can simulated evaluations not only capture the perfor) |
| We observe a strong correlation between the relative performances in simulation and in the real world across most policy checkpoints 0.0 0.2 0.4 0.6 ... | definition/direction/unit from same section | p. 7 (2) Can simulated evaluations not only capture the perfor) |
| ∆ Real success rate -0.03 -0.08 -0.11 -0.39 -0.46 ∆ SIMPLER success rate Background Lighting Distractors Table texture Camera pose -0.05 -0.06 -0.08 -0.14 ... | definition/direction/unit from same section | p. 9 (2) Can simulated evaluations not only capture the perfor) |
| 7: Real vs. simulation success rates for BridgeData V2 tasks. | definition/direction/unit from same section | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| For example, RT-1 (15%) and OctoBase exhibit the most significant success rate change between real world and simulation. | definition/direction/unit from same section | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| 8: Change in success rate under various distribution shifts for two RT-1 policies trained without and with data augmentation. | definition/direction/unit from same section | p. 9 (2) Can simulated evaluations not only capture the perfor) |
| Both physics simulators lead to good correlation between simulated and real-world evaluation success rates. | definition/direction/unit from same section | p. 10 (2) Can simulated evaluations not only capture the perfor) |
| We find that our simulated evaluation remains effective across a spectrum of plausible physical property parameters, evidenced by the low MMRV and the high ... | definition/direction/unit from same section | p. 10 (2) Can simulated evaluations not only capture the perfor) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Furthermore, "Visual Matching" (VisMatch) outperforms "Variant Aggregation" (VarAgg). | comparison identity and matched condition | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| Using a combination of "green-screened" background and curated foreground object and robot assets provides the best real-tosim performance correlations. tuning the drawer but not ... | comparison identity and matched condition | p. 10 (2) Can simulated evaluations not only capture the perfor) |
| For simulated results and realworld results, we report the difference in success rate with and without each distribution shift: ∆Success(shift) = 1 2 2 ... | comparison identity and matched condition | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| 8: Change in success rate under various distribution shifts for two RT-1 policies trained without and with data augmentation. | comparison identity and matched condition | p. 9 (2) Can simulated evaluations not only capture the perfor) |
| Ablation Studies We ablate the effect of the approaches we introduced in Section IV for closing the control and visual gaps between simulation and ... | comparison identity and matched condition | p. 9 (2) Can simulated evaluations not only capture the perfor) |
| 10: Comparison of SIMPLER-"Variant Aggregation" using SAPIEN (default) vs. | comparison identity and matched condition | p. 10 (2) Can simulated evaluations not only capture the perfor) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 8: Change in success rate under various distribution shifts for two RT-1 policies trained without and with data augmentation. Success rates are averaged ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Ablation Studies We ablate the effect of the approaches we introduced in Section IV for closing the control and visual gaps between simulation and ... | component/input/data sensitivity | p. 9 (2) Can simulated evaluations not only capture the perfor) |
| mance relationships across different policies, but also accurately reproduce real-world policy behavior modes within the same policy, like sensitivity to various visual distribution shifts? | component/input/data sensitivity | p. 7 (2) Can simulated evaluations not only capture the perfor) |
| Furthermore, "Visual Matching" (VisMatch) outperforms "Variant Aggregation" (VarAgg). | component/input/data sensitivity | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| These issues are exacerbated under Variant Aggregation, which has much larger visual distribution shifts to the real world (Fig. | component/input/data sensitivity | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| Sensitivity to physical property gap. | component/input/data sensitivity | p. 10 (2) Can simulated evaluations not only capture the perfor) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • ... | Thus, the approaches we introduced in Section IV-B for narrowing the visual gap between simulated and real scene can significantly improve real-andsim evaluation performance ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor), p. 10 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor) |
| Primary metric/result | For Octo simulated evaluations, since the model involves a non-deterministic diffusion head, we average its success rates across three different random seeds to produce ... | numeric claim only at cited anchor | p. 7 (2) Can simulated evaluations not only capture the perfor) |

- Numeric sentences retained from the body:
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** For simulated results and realworld results, we report the difference in success rate with and without each distribution shift: ∆Success(shift) = 1 2 2 X ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** For both setups, we perform extensive paired sim-and-real evaluations for multiple open-source manipulation policies such as RT-1X [11] and Octo [50], and we demonstrate strong ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and Pearson correlation coefficient (Pearson r, range [-1, 1], ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Our current set of environments has several limitations. | p. 10 (VII. CONCLUSION) |
| body limitation/failure cue | Additionally, we demonstrate that SIMPLER evaluations accurately capture finegrained characteristics of real-world policies beyond average performance, such as their robustness to various distribution shifts. | p. 10 (VII. CONCLUSION) |
| body limitation/failure cue | We evaluate two RT-1 checkpoints with different robustness behaviors to distribution shifts. | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| body limitation/failure cue | Beyond comparing average policy performances, it would be beneficial to let practitioners gauge more nuanced aspects of a policy's behavior, such as its robustness ... | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| body limitation/failure cue | See Table VIII for detailed results. robustness to various distribution shifts in the real world. | p. 9 (2) Can simulated evaluations not only capture the perfor) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For evaluations in the Google Robot environments, we additionally use a number of RT-1 [6] checkpoints at various stages of training: RT-1 trained to ... | p. 7 (2) Can simulated evaluations not only capture the perfor) |
| Detailed evaluation protocols for each task, including the number of evaluation trials, are presented in the supplementary. | p. 7 (2) Can simulated evaluations not only capture the perfor) |
| We evaluate two RT-1 checkpoints with different robustness behaviors to distribution shifts. | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| Additionally, we find that an alternative implementation of SIMPLER using "Variant Aggregation" (Section IV-B) instead of "Visual Matching" performs worse. | p. 8 (2) Can simulated evaluations not only capture the perfor) |
| We use the RT-1 (Converged), RT-1 (Begin), and RT1-X checkpoints on the Google robot drawer opening and closing tasks, and we compare the correlations ... | p. 9 (2) Can simulated evaluations not only capture the perfor) |
| In particular, we also observe a strong realto-sim performance correlation across most checkpoints for SIMPLER-Isaac. | p. 10 (2) Can simulated evaluations not only capture the perfor) |
| All environments can be imported with a single line of code and can be interacted with through a standard Gym interface. | p. 2 (I. INTRODUCTION) |
| Additionally, we open-source policy inference code for real-to-sim evaluation of common generalist robot policies (RT-1 [6], RT-1-X [11], and Octo [50]), and we provide ... | p. 2 (I. INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and Pearson correlation coefficient (Pearson r, range [-1, 1], higher ...
- **p. 10 / VII. CONCLUSION - extractive body cue:** Our current set of environments has several limitations.
- **p. 10 / VII. CONCLUSION - extractive body cue:** Additionally, we demonstrate that SIMPLER evaluations accurately capture finegrained characteristics of real-world policies beyond average performance, such as their robustness to various distribution shifts.
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** We evaluate two RT-1 checkpoints with different robustness behaviors to distribution shifts.
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Beyond comparing average policy performances, it would be beneficial to let practitioners gauge more nuanced aspects of a policy's behavior, such as its robustness to ...
- **p. 9 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** See Table VIII for detailed results. robustness to various distribution shifts in the real world.

- **Evidence anchors reviewed:** datasets p. 8 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor), p. 7 (VI. EXPERIMENTAL RESULTS), p. 9 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor), metrics p. 7 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor), baselines p. 8 (2) Can simulated evaluations not only capture the perfor), p. 10 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor), p. 10 (2) Can simulated evaluations not only capture the perfor), results p. 10 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor), p. 10 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
