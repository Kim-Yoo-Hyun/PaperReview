# Evaluation - ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OheAR2xrtb; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114743. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 1 (Figure/Table caption)): Design Average Ours w/o SE(3) 24±4.48 Ours w/o Eqv-Diff 57±6.52 Ours 76±2.24 While EquiBot achieves commendable results in both success rate and Dgeo, it struggles with more complex, long-horizon tasks ...

## Evaluation Body Digest

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** (3) Is our method applicable to real-world robotic manipulation tasks?
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Since our tasks contain more than one stage and include two robots and various objects, making the process of demonstration collection very time-consuming, we only ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We design six representative robot manipulation tasks: Open Bottle Cap, Open Door, Rotate Triangle, Calligraphy, Cloth Folding, and Cloth Fling.
- **p. 10 / 0.6 Results - extractive body cue:** Results for our real robot tasks are given in Table 4.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** (2024), we collect demonstrations and train our policy under the Training setting (T), subsequently testing the trained policy on both T and New Poses (NP), ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In contrast, ET-SEED consistently outperforms across all six tasks, with minimal performance drop when facing unseen object poses.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Success rates (↑) and standard deviation of different tasks in simulation. Open Bottle Cap Open Door Rotate Triangle T NP T NP
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** We report Dgeo in the same manner as success rates.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 8); 0.6 Results (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Design Average Ours w/o SE(3) 24±4.48 Ours w/o Eqv-Diff 57±6.52 Ours 76±2.24 While EquiBot achieves commendable results in both success rate and Dgeo, it ... | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | (2) Can our method achieve comparable performance with fewer demonstrations? | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, ET-SEED consistently outperforms across all six tasks, with minimal performance drop when facing unseen object poses. | p. 9 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Success rates (↑) and standard deviation of different tasks in simulation. Open Bottle Cap Open Door Rotate Triangle T NP T NP | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Success rates in real-world robot experiments. | p. 10 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** (3) Is our method applicable to real-world robotic manipulation tasks?
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Since our tasks contain more than one stage and include two robots and various objects, making the process of demonstration collection very time-consuming, we only ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We design six representative robot manipulation tasks: Open Bottle Cap, Open Door, Rotate Triangle, Calligraphy, Cloth Folding, and Cloth Fling.
- **p. 10 / 0.6 Results - extractive body cue:** Results for our real robot tasks are given in Table 4.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** (2024), we collect demonstrations and train our policy under the Training setting (T), subsequently testing the trained policy on both T and New Poses (NP), ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In contrast, ET-SEED consistently outperforms across all six tasks, with minimal performance drop when facing unseen object poses.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: ET-SEED is a visual imitation learning algorithm that marries SE(3) equivariant visual representations with diffusion policies. (a) ET-SEED achieve surprising efficiency and spatial ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of the denoising pro- cess of ET-SEED. A random trajectory xK first passes through an invariant transition for K -1 times and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Overview of our pipeline. A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant denoising ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Success rates (↑) and standard deviation of different tasks in simulation. Open Bottle Cap Open Door Rotate Triangle T NP T NP
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: SE(3) Geodesic distances (↓) of different tasks in simulation. Open bottle cap Open Door Rotate Triangle T NP T NP
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Ablation studies. Design Average Ours w/o SE(3) 24±4.48 Ours w/o Eqv-Diff 57±6.52 Ours
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4: Visualizations of the real-world environments used in our experiments. The tasks are performed using multiple Microsoft Azure Kinect cameras and Intel® RealSense for ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 4: Success rates in real-world robot experiments.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (3) Is our method applicable to real-world robotic manipulation tasks? | embodiment, simulator version and control stack | p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Task/environment | Since our tasks contain more than one stage and include two robots and various objects, making the process of demonstration collection very time-consuming, we ... | reset, timeout, object/scene variation | p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (4 METHOD), p. 7 (4 METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 7 (4 METHOD), p. 4 (4 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Success rates (↑) and standard deviation of different tasks in simulation. Open Bottle Cap Open Door Rotate Triangle T NP T NP | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We report Dgeo in the same manner as success rates. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Since we generate complete manipulation trajectories, the final success rate alone is inadequate for fully assessing the trajectory's quality. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Table 4: Success rates in real-world robot experiments. | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| A brief overview is illustrated in fig. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| The Franka arm and the gripper are teleoperated by the keyboard. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Figure 5: Loss curve of P1Net, P2Net and P3Net. After only several gradient descent, the loss of P1Net converges almost to 0, while the ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 6: Loss curve of two diffusion process. After only several gradient descent, the loss of Inv.+Eqv. process onverges much faster than the Pure ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| DP3 and DP3+Aug are used to compare ET-SEED with baseline methods that utilize data augmentation to achieve spatial generalization, while EquiBot allows for a ... | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| We systematically evaluate ET-SEED through both simulation and real-world experiments, aiming to address the following research questions: (1) Does our method demonstrate superior spatial ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| We compare our method against the following baselines: • 3D Diffusion Policy (DP3) (Ze et al., 2024): A diffusion-based 3D visuomotor policy. • 3D ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| The DP3+Aug baseline utilizes augmentations during training. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Consistent with our simulation findings, in real world experiments, ET-SEED performs better than baselines in all the four tasks, given only 20 demonstrations. | comparison identity and matched condition | p. 10 (0.6 Results) |
| Figure 1: ET-SEED is a visual imitation learning algorithm that marries SE(3) equivariant visual representations with diffusion policies. (a) ET-SEED achieve surprising efficiency and ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct ablation studies on the New Pose (NP) scenario of the representative Opening Door task to evaluate the effectiveness of different components of ... | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| In this variant, we use a standard PointNet++ to predict noise at each step. • Ours w/o Eqv-Diff: Our method without the SE(3) equivariant ... | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| Further details and discussions of their equivariant properties can be found in appendix G . | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| Figure 1: ET-SEED is a visual imitation learning algorithm that marries SE(3) equivariant visual representations with diffusion policies. (a) ET-SEED achieve surprising efficiency and ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Figure 2: Illustration of the denoising pro- cess of ET-SEED. A random trajectory xK first passes through an invariant transition for K -1 times ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 3: Overview of our pipeline. A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are mainly as followed: • We propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion policy defined on SE(3) manifold, which ... | Design Average Ours w/o SE(3) 24±4.48 Ours w/o Eqv-Diff 57±6.52 Ours 76±2.24 While EquiBot achieves commendable results in both success rate and Dgeo, it ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Primary metric/result | (2) Can our method achieve comparable performance with fewer demonstrations? | numeric claim only at cited anchor | p. 8 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Design Average Ours w/o SE(3) 24±4.48 Ours w/o Eqv-Diff 57±6.52 Ours 76±2.24 While EquiBot achieves commendable results in both success rate and Dgeo, it struggles ...
- **p. 5 / 4 METHOD - extractive body cue:** In ET-SEED, we set the parameter n = 2, meaning there are K -1 p1-like transitions (referred to as "SE(3) Invariant Denoising Steps") and one ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, the proposed method has certain limitations. | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | Figure 3: Overview of our pipeline. A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | The standard deviation of the Gaussian noise is set to 10% of the workspace size. | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | In this variant, we use a standard PointNet++ to predict noise at each step. • Ours w/o Eqv-Diff: Our method without the SE(3) equivariant ... | p. 9 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We systematically evaluate ET-SEED through both simulation and real-world experiments, aiming to address the following research questions: (1) Does our method demonstrate superior spatial ... | p. 8 (5 EXPERIMENTS) |
| We evaluate all methods using two metrics, based on 20 evaluation rollouts, averaged over 5 random seeds. | p. 9 (5 EXPERIMENTS) |
| In contrast, ET-SEED consistently outperforms across all six tasks, with minimal performance drop when facing unseen object poses. | p. 9 (5 EXPERIMENTS) |
| Each position is evaluated with one trial. | p. 10 (5 EXPERIMENTS) |
| Method Open Bottle Cap Open Door Calligraphy Fold Garment DP3 0.2 0.2 0.0 0.1 DP3+Aug 0.2 0.3 0.0 0.2 EquiBot 0.6 0.5 0.0 0.3 ... | p. 10 (5 EXPERIMENTS) |
| In ET-SEED, we set the parameter n = 2, meaning there are K -1 p1-like transitions (referred to as "SE(3) Invariant Denoising Steps") and ... | p. 5 (4 METHOD) |
| In this paper, we propose ET-SEED, a trajectorylevel end-to-end SE(3) equivariant diffusion model for robotic manipulation. | p. 4 (4 METHOD) |
| ET-SEED can theoretically guarantee the output actions are equivariant to any SE(3) transformation applied on the input observation, while only involving one equivariant denoising ... | p. 4 (4 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6 CONCLUSION - extractive body cue:** However, the proposed method has certain limitations.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Overview of our pipeline. A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant denoising ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** The standard deviation of the Gaussian noise is set to 10% of the workspace size.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In this variant, we use a standard PointNet++ to predict noise at each step. • Ours w/o Eqv-Diff: Our method without the SE(3) equivariant denoising ...

- **Evidence anchors reviewed:** datasets p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (0.6 Results), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), metrics p. 8 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), baselines p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (0.6 Results), p. 1 (Figure/Table caption), results p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
