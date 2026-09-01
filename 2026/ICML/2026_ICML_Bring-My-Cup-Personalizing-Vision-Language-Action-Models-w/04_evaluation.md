# Evaluation - Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fm6Z3wfTae; PDF retrieval source: https://openreview.net/pdf/68e389cf48e82eb16b32f886139baddd9122f43d.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup), p. 8 (5.2. Baselines), p. 7 (5.1. Experimental Setup), p. 9 (5.5. Error Case Analysis), p. 45 (Figure/Table caption)): VAP improves average SR from 18.8% to 58.8%, significantly outperforming soft/hard prompts which remain in the 27.5-31.2% range.

## Evaluation Body Digest

- **p. 6 / 4.2. Real-world Benchmarks - extractive PDF cue:** Spanning both selection and pick-and-place tasks, this benchmark rigorously evaluates whether VAP can reliably identify and manipulate userspecified objects on physical hardware.
- **p. 6 / 4.2. Real-world Benchmarks - extractive PDF cue:** We construct a real-world benchmark analogous to the simulation structure (Figure 2, bottom).
- **p. 8 / 5.4. Results on Real-world Benchmark - extractive PDF cue:** We evaluate VAP on a real-world benchmark comprising four selection and four pick-and-place tasks (Figure 5).
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** Performance on the Personalized-SIMPLER benchmark with the Google Robot platform.
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** For pick and pick-and-place tasks, we additionally report Correct Movement Ratio (CMR), the fraction of episodes in which the policy moves the target personal object ...
- **p. 8 / 5.3. Results on Simulation Benchmarks - extractive PDF cue:** On Personalized-SIMPLER (Google Robot), VAP yields substantial gains in both correct-object interaction (CMR) and task completion (SR).
- **p. 9 / 5.7. Comparison to Visual Prompting Alternatives - extractive PDF cue:** Within the same frozen VLA, we additionally compare against a broad set of visual prompting strategies adopted in prior robotics work, including opaque masks, bounding ...
- **p. 9 / 5.6. Efficiency of VAP - extractive PDF cue:** This confirms that VAP enhances performance without compromising the real-time responsiveness of the robotic system.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Benchmarks (p. 6); 4.1. Simulation Benchmarks (p. 6); 4.2. Real-world Benchmarks (p. 6); 5. Experiments (p. 6); 5.1. Experimental Setup (p. 6); 5.3. Results on Simulation Benchmarks (p. 8); 5.4. Results on Real-world Benchmark (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.4. Results on Real-world Benchmark | EMPIRICAL / REAL-ROBOT OR HARDWARE | VAP improves average SR from 18.8% to 58.8%, significantly outperforming soft/hard prompts which remain in the 27.5-31.2% range. | p. 8 (5.4. Results on Real-world Benchmark) |
| 5.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | VAP's modular perception pipeline achieves consistently high success rates, whereas prior methods struggle to personalize. | p. 7 (5.1. Experimental Setup) |
| 5.2. Baselines | EMPIRICAL / REAL-ROBOT OR HARDWARE | This optimized setup achieves > 95% accuracy on VQA recognition probes, and we further verify that the learned token transfers to the VLA with ... | p. 8 (5.2. Baselines) |
| 5.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report Success Rate (SR), the fraction of episodes that complete the task, following standard VLA evaluations (Intelligence et al., 2025; Kim et al., ... | p. 7 (5.1. Experimental Setup) |
| 5.5. Error Case Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Personalizing Vision-Language-Action Models with Visual Attentive Prompting Average (Pointing) Average (P&P) Vase Plushie Cup Slipper Plant Stuffed Toy Pouch Scrubber 0 25 50 75 ... | p. 9 (5.5. Error Case Analysis) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Real-world Benchmarks - extractive PDF cue:** Spanning both selection and pick-and-place tasks, this benchmark rigorously evaluates whether VAP can reliably identify and manipulate userspecified objects on physical hardware.
- **p. 6 / 4.2. Real-world Benchmarks - extractive PDF cue:** We construct a real-world benchmark analogous to the simulation structure (Figure 2, bottom).
- **p. 8 / 5.4. Results on Real-world Benchmark - extractive PDF cue:** We evaluate VAP on a real-world benchmark comprising four selection and four pick-and-place tasks (Figure 5).
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** Performance on the Personalized-SIMPLER benchmark with the Google Robot platform.
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** For pick and pick-and-place tasks, we additionally report Correct Movement Ratio (CMR), the fraction of episodes in which the policy moves the target personal object ...
- **p. 8 / 5.3. Results on Simulation Benchmarks - extractive PDF cue:** On Personalized-SIMPLER (Google Robot), VAP yields substantial gains in both correct-object interaction (CMR) and task completion (SR).
- **p. 9 / 5.7. Comparison to Visual Prompting Alternatives - extractive PDF cue:** Within the same frozen VLA, we additionally compare against a broad set of visual prompting strategies adopted in prior robotics work, including opaque masks, bounding ...
- **p. 9 / 5.6. Efficiency of VAP - extractive PDF cue:** This confirms that VAP enhances performance without compromising the real-time responsiveness of the robotic system.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Manipulating personal objects with VLA. Existing vision-language-action (VLA) models cannot handle per- sonal objects such as <my cup>, because they can only interpret ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of Evaluation Benchmarks. We evaluate in simulation (Personalized-SIMPLER, Personalized-VLABench) and on a real SO-101 robot. In each benchmark, one object is replaced ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. VAP builds a visual memory from a few reference images, grounds the target with frozen detection and segmentation, and prompts a frozen VLA ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Overview of our personalization benchmarks. We report the robot platform, task types, number of tasks and episodes, number of personal object categories, and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 2. Each benchmark requires a frozen VLA to act on a user-specific object instance given a few reference im- ages, in the presence of ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Overview of our real-world experimental setup.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Performance on the Personalized-SIMPLER benchmark with the Google Robot platform. Track 1 evaluates visual matching under unseen personal objects, and Track 2 aggregates ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Performance on the Personalized-SIMPLER benchmark using the WidowX platform across four manipulation tasks. For each task, we evaluate 10 runs of 24 episodes ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Spanning both selection and pick-and-place tasks, this benchmark rigorously evaluates whether VAP can reliably identify and manipulate userspecified objects on physical hardware. | embodiment, simulator version and control stack | p. 6 (4.2. Real-world Benchmarks), p. 6 (4.2. Real-world Benchmarks) |
| Task/environment | We construct a real-world benchmark analogous to the simulation structure (Figure 2, bottom). | reset, timeout, object/scene variation | p. 6 (4.2. Real-world Benchmarks), p. 8 (5.4. Results on Real-world Benchmark) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3.1. Problem Formulation), p. 3 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.1. Problem Formulation), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 18. Controlled occlusion sweep on Personalized-SIMPLER. We vary the number of consecutive frames during which the target is fully occluded and report tracking ... | definition/direction/unit from same section | p. 45 (Figure/Table caption) |
| VAP's modular perception pipeline achieves consistently high success rates, whereas prior methods struggle to personalize. | definition/direction/unit from same section | p. 7 (5.1. Experimental Setup) |
| We report Success Rate (SR), the fraction of episodes that complete the task, following standard VLA evaluations (Intelligence et al., 2025; Kim et al., ... | definition/direction/unit from same section | p. 7 (5.1. Experimental Setup) |
| Personalizing Vision-Language-Action Models with Visual Attentive Prompting Average (Pointing) Average (P&P) Vase Plushie Cup Slipper Plant Stuffed Toy Pouch Scrubber 0 25 50 75 ... | definition/direction/unit from same section | p. 9 (5.5. Error Case Analysis) |
| Figure 5. Real-world performance. We report SR over 20 trials for all tasks, and CMR specifically for pick-and-place tasks (inappli- cable to selection). VAP ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| This optimized setup achieves > 95% accuracy on VQA recognition probes, and we further verify that the learned token transfers to the VLA with ... | definition/direction/unit from same section | p. 8 (5.2. Baselines) |
| While baselines occasionally register high interaction rates (CMR) in confined setups, they fail to translate this into successful task completion. | definition/direction/unit from same section | p. 8 (5.3. Results on Simulation Benchmarks) |
| Table 13. Error-mode breakdown for VAP across benchmarks with more details. "Fail (%)" is computed over all evaluation episodes. Case 1-3 are computed conditional ... | definition/direction/unit from same section | p. 39 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| VAP outperforms other baselines across all scenarios. | comparison identity and matched condition | p. 7 (5.1. Experimental Setup) |
| This advantage extends to placement tasks (Tasks 4-6), where VAP consistently outperforms all baselines, attaining > 90% SR on Tasks 4 and 5. | comparison identity and matched condition | p. 8 (5.3. Results on Simulation Benchmarks) |
| To stress-test the last hypothesis in particular, we maximize the strength of the Soft Prompt baseline using Yo'LLaVA-style supervision and oracle hard negatives sampled ... | comparison identity and matched condition | p. 8 (5.2. Baselines) |
| Table 2. Performance on the Personalized-SIMPLER benchmark with the Google Robot platform. Track 1 evaluates visual matching under unseen personal objects, and Track 2 ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| This section describes the experimental setup, metrics, and baselines used to evaluate VAP on the benchmarks in Section 4. | comparison identity and matched condition | p. 6 (5. Experiments) |
| Table 11. Short and long textual descriptions for personal objects used in our benchmarks. Short descriptions and long descriptions are used as rich prompts ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 14. Ablation of instruction rewriting on single-view Personalized-SIMPLER. "Mask-only" removes rewriting, while "Rewrite- only" removes the visual highlight but keeps the same tint-color ... | component/input/data sensitivity | p. 43 (Figure/Table caption) |
| Table 17. Ablation of visual prompt design on single-view Personalized-SIMPLER. The top block compares VAP's mask-aligned tint against alternative visual prompting strategies, including approaches ... | component/input/data sensitivity | p. 45 (Figure/Table caption) |
| Track 1 evaluates visual matching under unseen personal objects, and Track 2 aggregates performance across systematic visual variants. | component/input/data sensitivity | p. 7 (5.1. Experimental Setup) |
| We extract textual descriptions from the reference images and use an LLM to append these details to the instruction (generating Short or Long variants). | component/input/data sensitivity | p. 7 (5.2. Baselines) |
| Crucially, these gains persist under variant aggregation (SR 58.2%, CMR 87.3%), confirming robustness to visual perturbations. | component/input/data sensitivity | p. 8 (5.3. Results on Simulation Benchmarks) |
| Personalizing Vision-Language-Action Models with Visual Attentive Prompting These three baselines isolate distinct hypotheses about whether personalization can be achieved without retraining: whether VLAs already ... | component/input/data sensitivity | p. 8 (5.2. Baselines) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects ... | VAP improves average SR from 18.8% to 58.8%, significantly outperforming soft/hard prompts which remain in the 27.5-31.2% range. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup), p. 8 (5.2. Baselines), p. 7 (5.1. Experimental Setup), p. 9 (5.5. Error Case Analysis), p. 45 (Figure/Table caption) |
| Primary metric/result | VAP's modular perception pipeline achieves consistently high success rates, whereas prior methods struggle to personalize. | numeric claim only at cited anchor | p. 7 (5.1. Experimental Setup) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Simulation Benchmarks - extractive PDF cue:** Following original evaluation protocols, we generate 1,685 Fractal episodes across visual-matching and variant-aggregation tracks (enumerating visual perturbations), and use the standard 96 episodes for Bridge ...
- **p. 6 / 4.1. Simulation Benchmarks - extractive PDF cue:** The benchmark comprises 250 episodes (5 tasks × 50 episodes), providing personalized instructions (e.g., "select my leather bag") and multi-view observations.
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** For each task, we evaluate 10 runs of 24 episodes and report the mean.
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** For each task, we evaluate 10 runs of 50 episodes and report the mean.
- **p. 8 / 5.3. Results on Simulation Benchmarks - extractive PDF cue:** VAP adds minimal overhead (0.02 s) to the control loop.
- **p. 8 / 5.3. Results on Simulation Benchmarks - extractive PDF cue:** Phase Component Time (s) Initialization Grounding DINO 0.19 Segmentation & Embedding 0.07 Per Step SAM2 Tracking 0.02 VLA Policy Inference 0.20 surpasses the strongest baseline ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the intended personal object in all relevant ... | p. 42 (Figure/Table caption) |
| body limitation/failure cue | Figure 9. Soft Prompt: relatively consistent localization yet failed execution. Across the rollout, the token-patch similarity heatmaps remain largely concentrated near the intended personal ... | p. 25 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. Manipulating personal objects with VLA. Existing vision-language-action (VLA) models cannot handle per- sonal objects such as <my cup>, because they can only ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | First, the sequential factorization of grounding and manipulation does not itself bound performance: reliable spatio-temporal tracking maintains target identity through several seconds of complete ... | p. 9 (5.5. Error Case Analysis) |
| body limitation/failure cue | Figure 3. VAP builds a visual memory from a few reference images, grounds the target with frozen detection and segmentation, and prompts a frozen ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Failure analysis across benchmarks. | p. 8 (5.4. Results on Real-world Benchmark) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Appendix A provides additional environment and hyperparameter details. | p. 6 (5. Experiments) |
| For experiments on Personalized-SIMPLER, we instead use the π0 checkpoint released for the Fractal and Bridge set6 | p. 6 (5.1. Experimental Setup) |
| For each personal object, we optimize a specific token embedding within the VLA's language encoder using the reference images. | p. 7 (5.2. Baselines) |
| We fine-tune the base checkpoint π0.5 solely for environment adaptation, using generic data that explicitly excludes personal objects and personalized instructions. | p. 7 (5.1. Experimental Setup) |
| We report SR over 20 trials for all tasks, and CMR specifically for pick-and-place tasks (inapplicable to selection). | p. 9 (5.5. Error Case Analysis) |
| We provide qualitative examples and several plausible design directions in Appendix D (see also Appendix D.2), and leave their implementation to future work. | p. 9 (5.5. Error Case Analysis) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 42 / Figure/Table caption - extractive PDF cue:** Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the intended personal object in all relevant views, ...
- **p. 25 / Figure/Table caption - extractive PDF cue:** Figure 9. Soft Prompt: relatively consistent localization yet failed execution. Across the rollout, the token-patch similarity heatmaps remain largely concentrated near the intended personal object, ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Manipulating personal objects with VLA. Existing vision-language-action (VLA) models cannot handle per- sonal objects such as <my cup>, because they can only interpret ...
- **p. 9 / 5.5. Error Case Analysis - extractive PDF cue:** First, the sequential factorization of grounding and manipulation does not itself bound performance: reliable spatio-temporal tracking maintains target identity through several seconds of complete invisibility, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. VAP builds a visual memory from a few reference images, grounds the target with frozen detection and segmentation, and prompts a frozen VLA ...
- **p. 8 / 5.4. Results on Real-world Benchmark - extractive PDF cue:** Failure analysis across benchmarks.

- **PDF anchors reviewed:** datasets p. 6 (4.2. Real-world Benchmarks), p. 6 (4.2. Real-world Benchmarks), p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup), p. 8 (5.3. Results on Simulation Benchmarks), metrics p. 45 (Figure/Table caption), p. 7 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup), p. 9 (5.5. Error Case Analysis), p. 9 (Figure/Table caption), p. 8 (5.2. Baselines), baselines p. 7 (5.1. Experimental Setup), p. 8 (5.3. Results on Simulation Benchmarks), p. 8 (5.2. Baselines), p. 7 (Figure/Table caption), p. 6 (5. Experiments), p. 19 (Figure/Table caption), results p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup), p. 8 (5.2. Baselines), p. 7 (5.1. Experimental Setup), p. 9 (5.5. Error Case Analysis), p. 45 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
