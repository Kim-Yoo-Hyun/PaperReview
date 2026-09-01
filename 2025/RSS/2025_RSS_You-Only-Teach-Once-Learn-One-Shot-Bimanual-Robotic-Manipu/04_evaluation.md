# Evaluation - You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p149.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p149.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (B. Results Comparison), p. 9 (B. Results Comparison), p. 9 (B. Results Comparison), p. 11 (B. Results Comparison), p. 17 (A. Implementation Details of Our BiDP), p. 10 (B. Results Comparison)): ong-horizon bimanual manipulation tasks, the existing stateof-the-art methods still have a lot of room for improvement, such as the gradually decaying effect over multiple substeps and less exploration of efficient ...

## Evaluation Body Digest

- **p. 8 / A. Experiment Setups - extractive body cue:** We then processed these data into the form suitable for BiDP, including extracting 3D point clouds of manipulated objects and saving the corresponding multi-step end-effector ...
- **p. 7 / A. Experiment Setups - extractive body cue:** 1) Tasks: We evaluate YOTO on five real-world bimanual tasks, including pull drawer, pour water, unscrew bottle, uncover Lid and open box.
- **p. 8 / A. Experiment Setups - extractive body cue:** The task pull drawer with 243 episodes is used to train all models.
- **p. 11 / B. Results Comparison - extractive body cue:** also makes our model more robust compared to all baselines The core idea here is to rely on the still rapidly developing capabilities of vision ...
- **p. 9 / B. Results Comparison - extractive body cue:** pall rawr TT SOIT our water TO epraNTeT Methods Sane -pa- pick place sale - pa - Avge / pe - pk cone ts pour ...
- **p. 10 / B. Results Comparison - extractive body cue:** 7: Visualization of five bimanual tasks performed on real robots.
- **p. 10 / B. Results Comparison - extractive body cue:** IV, following the mainstream in-distribution setting, we performed extensive policies training and real robot evaluations on five long-horizon tasks, and reported a detailed performance comparison ...
- **p. 11 / B. Results Comparison - extractive body cue:** We can see that the two robot arms have leamed the movements demonstrated by human hands and complete these ‘complex tasks in an orderly manner.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** A. Experiment Setups (p. 7); B. Results Comparison (p. 8); A. Implementation Details of Our BiDP (p. 17); C. Evaluation Results and Performance Analysis (p. 21).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B. Results Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | ong-horizon bimanual manipulation tasks, the existing stateof-the-art methods still have a lot of room for improvement, such as the gradually decaying effect over multiple ... | p. 10 (B. Results Comparison) |
| B. Results Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | Next, we replaced the input with point clouds containing only manipulated objects (id-2) or predicted simplified sparse keyposes (id-3), and the success rate and ... | p. 9 (B. Results Comparison) |
| B. Results Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results suggest that reducing unnecessary distractions in the input and learning fewer simplified actions are the right direction ‘When both are used together ... | p. 9 (B. Results Comparison) |
| B. Results Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | In summary, these results verify that our BiDP indeed outperforms prior methods with the least amount of performance degradation in OOD generalization | p. 11 (B. Results Comparison) |
| A. Implementation Details of Our BiDP | EMPIRICAL / REAL-ROBOT OR HARDWARE | For every evaluation in the real world, we run the policy in a randomly initialized placement of objects for dozens of, episodes (please refer ... | p. 17 (A. Implementation Details of Our BiDP) |

## Dataset / Benchmark Role

- **p. 8 / A. Experiment Setups - extractive body cue:** We then processed these data into the form suitable for BiDP, including extracting 3D point clouds of manipulated objects and saving the corresponding multi-step end-effector ...
- **p. 7 / A. Experiment Setups - extractive body cue:** 1) Tasks: We evaluate YOTO on five real-world bimanual tasks, including pull drawer, pour water, unscrew bottle, uncover Lid and open box.
- **p. 8 / A. Experiment Setups - extractive body cue:** The task pull drawer with 243 episodes is used to train all models.
- **p. 11 / B. Results Comparison - extractive body cue:** also makes our model more robust compared to all baselines The core idea here is to rely on the still rapidly developing capabilities of vision ...
- **p. 9 / B. Results Comparison - extractive body cue:** pall rawr TT SOIT our water TO epraNTeT Methods Sane -pa- pick place sale - pa - Avge / pe - pk cone ts pour ...
- **p. 10 / B. Results Comparison - extractive body cue:** 7: Visualization of five bimanual tasks performed on real robots.
- **p. 10 / B. Results Comparison - extractive body cue:** IV, following the mainstream in-distribution setting, we performed extensive policies training and real robot evaluations on five long-horizon tasks, and reported a detailed performance comparison ...
- **p. 11 / B. Results Comparison - extractive body cue:** We can see that the two robot arms have leamed the movements demonstrated by human hands and complete these ‘complex tasks in an orderly manner.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Our proposed YOTO (You Only Teach Once) facilitates v:
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: A detailed example of extracted motion trajectories with corresponding keyframes of both left hand and right hand. It is best to 200m in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: We collected a variety of manipulated objects in instance-level for each of five bimanual tasks to improve and verify the generalizability of trained ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Illustrations of extracted hand motion trajectories by using (a) unhandled raw 3D hand center points, (b) projected hand center points on the 2D ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Ablation studies on expanded training data at different scales using geometric transformations. The task pull drawer with 243 episodes is treated as the ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 7: Visualization of five bimanual tasks performed on real robots. We use different colors such as teal, ol
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 8. These results further reveal the simplicity, versatility and scalability of YOTO. In the future, we will explore using YOTO to handle more intricate, ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 9: Examples of using vision foundation models (VFMs) to detect and segment manipulated objects

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We then processed these data into the form suitable for BiDP, including extracting 3D point clouds of manipulated objects and saving the corresponding multi-step ... | embodiment, simulator version and control stack | p. 8 (A. Experiment Setups), p. 7 (A. Experiment Setups) |
| Task/environment | 1) Tasks: We evaluate YOTO on five real-world bimanual tasks, including pull drawer, pour water, unscrew bottle, uncover Lid and open box. | reset, timeout, object/scene variation | p. 7 (A. Experiment Setups), p. 8 (A. Experiment Setups) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 17 (A. Implementation Details of Our BiDP), p. 4 (A. Problem Formulation) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| ‘TABLE V: Comparison of the average success rate of various ‘methods on all five tasks (in-distribution evaluations), | definition/direction/unit from same section | p. 9 (B. Results Comparison) |
| Next, we replaced the input with point clouds containing only manipulated objects (id-2) or predicted simplified sparse keyposes (id-3), and the success rate and ... | definition/direction/unit from same section | p. 9 (B. Results Comparison) |
| ong-horizon bimanual manipulation tasks, the existing stateof-the-art methods still have a lot of room for improvement, such as the gradually decaying effect over multiple ... | definition/direction/unit from same section | p. 10 (B. Results Comparison) |
| For every evaluation in the real world, we run the policy in a randomly initialized placement of objects for dozens of, episodes (please refer ... | definition/direction/unit from same section | p. 17 (A. Implementation Details of Our BiDP) |
| Specifically, we first implement the auto-rollout strategy to collect real robot data. | definition/direction/unit from same section | p. 8 (A. Experiment Setups) |
| We first discuss the quality of the extracted motion trajectories, which is the core concept of this paper and extremely important for the various ... | definition/direction/unit from same section | p. 8 (B. Results Comparison) |
| (1) First, the diffusion-based strategy always performed better than the transformer-based ACT. | definition/direction/unit from same section | p. 10 (B. Results Comparison) |
| We can see that the two robot arms have leamed the movements demonstrated by human hands and complete these ‘complex tasks in an orderly ... | definition/direction/unit from same section | p. 11 (B. Results Comparison) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| also makes our model more robust compared to all baselines The core idea here is to rely on the still rapidly developing capabilities of ... | comparison identity and matched condition | p. 11 (B. Results Comparison) |
| 3) Baselines: We compare our method to four strong baselines. | comparison identity and matched condition | p. 8 (A. Experiment Setups) |
| 5, we compared the general effect of 3D hand | comparison identity and matched condition | p. 8 (B. Results Comparison) |
| Despite being a solid baseline, it performed the worst on this challenging longhorizon task. | comparison identity and matched condition | p. 9 (B. Results Comparison) |
| ong-horizon bimanual manipulation tasks, the existing stateof-the-art methods still have a lot of room for improvement, such as the gradually decaying effect over multiple ... | comparison identity and matched condition | p. 10 (B. Results Comparison) |
| In summary, these results verify that our BiDP indeed outperforms prior methods with the least amount of performance degradation in OOD generalization | comparison identity and matched condition | p. 11 (B. Results Comparison) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Il, ‘we quantitatively illustrate the effectiveness of each strategy cone by one through many ablation studies. | component/input/data sensitivity | p. 9 (B. Results Comparison) |
| First, the method (id-1) without any proposed strategy can be regarded as the vanilla EquiBot [95], which takes the entire point cloud scene as ... | component/input/data sensitivity | p. 9 (B. Results Comparison) |
| It is a variant of diffusion policy with a simpler point cloud encoder. | component/input/data sensitivity | p. 8 (A. Experiment Setups) |
| 6: Ablation studies on expanded training data at different scales using geometric transformations. | component/input/data sensitivity | p. 8 (A. Experiment Setups) |
| Comparing to EquiBot, our BiDP still has a clear advantage, thanks to the fact that we use explicit 3D geometric transformations for expanding the ... | component/input/data sensitivity | p. 10 (B. Results Comparison) |
| Therefore, reducing the number of points to 1024 ‘can make training faster without hurting performance. | component/input/data sensitivity | p. 17 (A. Implementation Details of Our BiDP) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| As an altemative, we propose to project all 3D points {f!"°}/_, onto the 2D image, nd then lft these points to 3D by applying ... | ong-horizon bimanual manipulation tasks, the existing stateof-the-art methods still have a lot of room for improvement, such as the gradually decaying effect over multiple ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (B. Results Comparison), p. 9 (B. Results Comparison), p. 9 (B. Results Comparison), p. 11 (B. Results Comparison), p. 17 (A. Implementation Details of Our BiDP), p. 10 (B. Results Comparison) |
| Primary metric/result | Next, we replaced the input with point clouds containing only manipulated objects (id-2) or predicted simplified sparse keyposes (id-3), and the success rate and ... | numeric claim only at cited anchor | p. 9 (B. Results Comparison) |

- Numeric sentences retained from the body:
- **p. 8 / A. Experiment Setups - extractive body cue:** This magnitude is comparable to existing large-scale bimanual teleoperation methods such as RDT [53] (6K+ self-created episodes) and zp [7] (5~100 hours posttraining data), but ...
- **p. 8 / A. Experiment Setups - extractive body cue:** 4) Metries: We train all methods for 500 or 1,000 epochs and only save the last checkpoint for testing.
- **p. 8 / A. Experiment Setups - extractive body cue:** We evaluate each model with 5 trials for each single object (last three tasks with 30, 25 and 20 trials, respectively) or 2 trials for ...
- **p. 8 / A. Experiment Setups - extractive body cue:** The task pull drawer with 243 episodes is used to train all models.
- **p. 8 / A. Experiment Setups - extractive body cue:** The task pull drawer with 243 episodes is treated as the not expanded version,
- **p. 9 / B. Results Comparison - extractive body cue:** pall rawr TT SOIT our water TO epraNTeT Methods Sane -pa- pick place sale - pa - Avge / pe - pk cone ts pour ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In short, these limitations highlight the need for further innovations to enhance robustness, generalization, and scalability in bimanual robot manipulation, | p. 11 (VI. CONCLUSION AND Limitation) |
| body limitation/failure cue | tation: Although YOTO has achieved impressive performance on various long-horizon bimanual manipulation tasks, we conclude that it has at least the following limitations. | p. 11 (VI. CONCLUSION AND Limitation) |
| body limitation/failure cue | Fig. 15: From top to bottom, we have examples of failed cases in all five tasks during evaluation, We have outlined and magnified the ... | p. 21 (Figure/Table caption) |
| body limitation/failure cue | Firstly, when directly applying advanced 3D hand mesh reconstruction methods (ei ther HaMeR [67] or WiLoR [71)) the resulting hand trajectory is always unstable ... | p. 9 (B. Results Comparison) |
| body limitation/failure cue | Here, we answer the questions raised at the beginning one by one, including basic in-distribution results and generalizations to out-of-distribution settings, | p. 8 (B. Results Comparison) |
| body limitation/failure cue | Although above tests have new variations in object placements, we choose two tasks pul drawer and uncover 1id to perform more challenging ‘out-of-distribution (QOD) ... | p. 8 (A. Experiment Setups) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4) Metries: We train all methods for 500 or 1,000 epochs and only save the last checkpoint for testing. | p. 8 (A. Experiment Setups) |
| For the noise prediction network, we inherits hyperparameters from the ‘original Diffusion Policy [15], Specifically, to optimize for inference speed in all experiments, we ... | p. 17 (A. Implementation Details of Our BiDP) |
| At inference time, we also need to preprocess the binocular RGB observations to obtain the point cloud of manipulated objects. | p. 17 (A. Implementation Details of Our BiDP) |
| More importantly, all tasks are tong-horizon, indicating that they are quite complex due to containing multiple substeps. | p. 7 (A. Experiment Setups) |
| It consists of 5 substeps including pick up the bottle (L), bring the bottle close to the right arm (L), unscrew the cap (R), ... | p. 7 (A. Experiment Setups) |
| The number of all OOD trials is quadrupled. | p. 8 (A. Experiment Setups) |
| 2) High-Level Features Extraction: Given a video demonstration (the left stream) of one specified bimanual task, we run our vision perception pipeline to obtain ... | p. 4 (B. Hand Motion Extraction and Injection) |
| For imitation learning, the agent mimics manipulation plans from labeled demonstrations D - {(O,A),}*,, where N is the number of trajectories, O = {0,,S/,S8}L, ... | p. 4 (A. Problem Formulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / VI. CONCLUSION AND Limitation - extractive body cue:** In short, these limitations highlight the need for further innovations to enhance robustness, generalization, and scalability in bimanual robot manipulation,
- **p. 11 / VI. CONCLUSION AND Limitation - extractive body cue:** tation: Although YOTO has achieved impressive performance on various long-horizon bimanual manipulation tasks, we conclude that it has at least the following limitations.
- **p. 21 / Figure/Table caption - extractive body cue:** Fig. 15: From top to bottom, we have examples of failed cases in all five tasks during evaluation, We have outlined and magnified the areas ...
- **p. 9 / B. Results Comparison - extractive body cue:** Firstly, when directly applying advanced 3D hand mesh reconstruction methods (ei ther HaMeR [67] or WiLoR [71)) the resulting hand trajectory is always unstable and ...
- **p. 8 / B. Results Comparison - extractive body cue:** Here, we answer the questions raised at the beginning one by one, including basic in-distribution results and generalizations to out-of-distribution settings,
- **p. 8 / A. Experiment Setups - extractive body cue:** Although above tests have new variations in object placements, we choose two tasks pul drawer and uncover 1id to perform more challenging ‘out-of-distribution (QOD) evaluations ...

- **PDF anchors reviewed:** datasets p. 8 (A. Experiment Setups), p. 7 (A. Experiment Setups), p. 8 (A. Experiment Setups), p. 11 (B. Results Comparison), p. 9 (B. Results Comparison), p. 10 (B. Results Comparison), metrics p. 9 (B. Results Comparison), p. 9 (B. Results Comparison), p. 10 (B. Results Comparison), p. 17 (A. Implementation Details of Our BiDP), p. 8 (A. Experiment Setups), p. 8 (B. Results Comparison), baselines p. 11 (B. Results Comparison), p. 8 (A. Experiment Setups), p. 8 (B. Results Comparison), p. 9 (B. Results Comparison), p. 10 (B. Results Comparison), p. 11 (B. Results Comparison), results p. 10 (B. Results Comparison), p. 9 (B. Results Comparison), p. 9 (B. Results Comparison), p. 11 (B. Results Comparison), p. 17 (A. Implementation Details of Our BiDP), p. 10 (B. Results Comparison).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
