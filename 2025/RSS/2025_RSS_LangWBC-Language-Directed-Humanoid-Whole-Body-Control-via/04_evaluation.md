# Evaluation - LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p065.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p065.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption)): Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The CLIPSCVAE model (let) produces smooth and coherent iagonal ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We conduct extensive experiments to evaluate our framework for language-directed humanoid whole-body control with 4 Unitree GI humanoid robot.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Finally, we showcase a complex LLM-guided compositional task, illustrating the full capabilities of LangWBC.
- **p. 6 / B. Latent Space Analysis - extractive body cue:** This allows for better generalization to unseen commands, smoother motion interpolation, and more coherent transitions between behaviors.
- **p. 7 / B. Latent Space Analysis - extractive body cue:** ‘can leverage to perform smooth transitions between motions and generate novel, unseen motions.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We begin with an overview and demonstrate diverse motions enabled by our approach.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks (top ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The CLIPSCVAE model (let) ...
- **p. 9 / C. Generalization to Unseen Texts - extractive body cue:** ietepolating between walking (Command 1) and side stepping (Command 2) predoces walking the side, a whole-body masion that does not exist i the

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The CLIPSCVAE model ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We conduct extensive experiments to evaluate our framework for language-directed humanoid whole-body control with 4 Unitree GI humanoid robot.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Finally, we showcase a complex LLM-guided compositional task, illustrating the full capabilities of LangWBC.
- **p. 6 / B. Latent Space Analysis - extractive body cue:** This allows for better generalization to unseen commands, smoother motion interpolation, and more coherent transitions between behaviors.
- **p. 7 / B. Latent Space Analysis - extractive body cue:** ‘can leverage to perform smooth transitions between motions and generate novel, unseen motions.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. tsining phase anda language-directed student
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks (top ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. SNE Analysis of Latent Space. Te plot shows 9 motions from 44 categories of motion, as shown ia the legend, We se that ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Rollouts of Unseen Text Commands. Our metho can generalize to unseen text commands with similar semanical meanings. OF the tre, ‘aly one command ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The CLIPSCVAE model (let) ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 12. Lower-body Motion Examples. The framework also enables various lowercbady movements soch as stepping, squating and balancing. These motions are also sucessfully transfered tothe ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct extensive experiments to evaluate our framework for language-directed humanoid whole-body control with 4 Unitree GI humanoid robot. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | Finally, we showcase a complex LLM-guided compositional task, illustrating the full capabilities of LangWBC. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 6 (B. Latent Space Analysis) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 4 (B. Language-Directed Student Policy), p. 4 (B. Language-Directed Student Policy) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 5 (B. Language-Directed Student Policy), p. 3 (III. MerHops) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We begin with an overview and demonstrate diverse motions enabled by our approach. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| ‘can leverage to perform smooth transitions between motions and generate novel, unseen motions. | definition/direction/unit from same section | p. 7 (B. Latent Space Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The CLIPSCVAE model ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| We then analyze the learned latent space and its contribution to the policy's generalization to unseen commands, highlight key features such as smooth transitions ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Fig. 12. Lower-body Motion Examples. The framework also enables various lowercbady movements soch as stepping, squating and balancing. These motions are also sucessfully transfered ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| We then analyze the learned latent space and its contribution to the policy's generalization to unseen commands, highlight key features such as smooth transitions ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Fig. 12. Lower-body Motion Examples. The framework also enables various lowercbady movements soch as stepping, squating and balancing. These motions are also sucessfully transfered ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Furthermore, our framework enables smooth transitions between motion clips and generates novel motions through interpolation, demonstrating generalization beyond the training data | Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The CLIPSCVAE model ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption) |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- **p. 4 / B. Language-Directed Student Policy - extractive body cue:** We input a sequence of historical observations and actions, sampled at 10 Hz over a 2-second window, yielding a 20-step trajectory of input-output pars.
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** 3) Experience Buffer Construction: We insert the collected student's observations and the teacher's actions to a buffer of 1024 x 512 ( 500,000) state-action pairs
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** We use a batch size of 1024 64 and a learning rate of 1 x 10°, with one epoch per iteration, We then use the ...
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** The student policy also runs at 50 Hz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | ietepolating between walking (Command 1) and side stepping (Command 2) predoces walking the side, a whole-body masion that does not exist i the | p. 9 (C. Generalization to Unseen Texts) |
| body limitation/failure cue | We find the poticy performs forward motion in a consistent speed and style despite phrasing differences like "move" vs. "walk." demonstrating robustness to linguistic ... | p. 7 (C. Generalization to Unseen Texts) |
| body limitation/failure cue | CLIP encoder handles minor linguistic variations well, it produces significantly different encodings for out-of-distribution commands, which the MLP policy struggles to generalize from. | p. 7 (C. Generalization to Unseen Texts) |
| body limitation/failure cue | Moreover, the robot's movement stays agile and stable, demonstrating the framework's robustness to unseen latent codes, | p. 8 (C. Generalization to Unseen Texts) |
| body limitation/failure cue | ‘dynamics of humanoid motion, achieving smooth and coherent transitions ~ such as running, stopping, and switching to limb ‘movements - within a single policy, ... | p. 8 (C. Generalization to Unseen Texts) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use a batch size of 1024 64 and a learning rate of 1 x 10°, with one epoch per iteration, We then use ... | p. 5 (B. Language-Directed Student Policy) |
| The optimization is solved using the LM algorithm with joint limit constraints, yielding kinematically feasible motions that closely match the original MoCap data, The ... | p. 3 (A. Motion-Tracking Teacher Policy) |
| Retargeted Teacher Training Physics Simulator Mocap Dataset (© Tracking keypoint Student Training ‘Cloning + "Aperson waits _ CUP [rnse forward" Encoder ‘Mocap Dataset qatudent ... | p. 3 (B. Generative Action Modeling) |
| 1) Text Caption Embedding: We utilize the CLIP text ‘encoder [30] to convert the input natural language command c* into a fixed-length embedding vector | p. 4 (B. Language-Directed Student Policy) |
| ‘The encoder processes the concatenated textual and observational inputs to produce the parameters of a latent Gaussian distribution, outputting a mean vector jx © ... | p. 4 (B. Language-Directed Student Policy) |
| ‘The training process consists of five steps | p. 5 (B. Language-Directed Student Policy) |
| To verify this property, we apply the tSNE algorithm to embed the high-dimensional latent codes of various motions into a 2D plane. | p. 6 (B. Latent Space Analysis) |
| 5, we plot nine different ‘motions from four categories (walking, raising the left or right hhand, and clapping), with each category color-coded, | p. 6 (B. Latent Space Analysis) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks (top ...
- **p. 9 / C. Generalization to Unseen Texts - extractive body cue:** ietepolating between walking (Command 1) and side stepping (Command 2) predoces walking the side, a whole-body masion that does not exist i the
- **p. 7 / C. Generalization to Unseen Texts - extractive body cue:** We find the poticy performs forward motion in a consistent speed and style despite phrasing differences like "move" vs. "walk." demonstrating robustness to linguistic variation
- **p. 7 / C. Generalization to Unseen Texts - extractive body cue:** CLIP encoder handles minor linguistic variations well, it produces significantly different encodings for out-of-distribution commands, which the MLP policy struggles to generalize from.
- **p. 8 / C. Generalization to Unseen Texts - extractive body cue:** Moreover, the robot's movement stays agile and stable, demonstrating the framework's robustness to unseen latent codes,
- **p. 8 / C. Generalization to Unseen Texts - extractive body cue:** ‘dynamics of humanoid motion, achieving smooth and coherent transitions ~ such as running, stopping, and switching to limb ‘movements - within a single policy, without ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (B. Latent Space Analysis), p. 7 (B. Latent Space Analysis), metrics p. 5 (IV. EXPERIMENTS), p. 5 (Figure/Table caption), p. 7 (B. Latent Space Analysis), baselines p. 9 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (Figure/Table caption), p. 14 (Figure/Table caption), results p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We conduct extensive experiments to evaluate our framework for language-directed humanoid whole-body control with 4 Unitree GI humanoid robot. (p. 5, IV. EXPERIMENTS).
- **Metric evidence:** We begin with an overview and demonstrate diverse motions enabled by our approach. (p. 5, IV. EXPERIMENTS).
- **Baseline/ablation evidence:** We then analyze the learned latent space and its contribution to the policy's generalization to unseen commands, highlight key features such as smooth transitions and latent interpolation, and follow up ... (p. 5, IV. EXPERIMENTS).
- **Failure/negative evidence:** CLIP encoder handles minor linguistic variations well, it produces significantly different encodings for out-of-distribution commands, which the MLP policy struggles to generalize from. (p. 7, C. Generalization to Unseen Texts).
