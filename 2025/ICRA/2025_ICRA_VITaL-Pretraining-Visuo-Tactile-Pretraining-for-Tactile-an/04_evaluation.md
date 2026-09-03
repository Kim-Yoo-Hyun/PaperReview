# Evaluation - VITaL Pretraining: Visuo-Tactile Pretraining for Tactile and Non-Tactile Manipulation Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2403.11898v2. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTAL EVALUATION)): This is significantly higher than the 20% and 45% success rates that learning from vision only with ACT and diffusion policy (respectively) achieves.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** In this task, the robot has to navigate to a USB cable, unplug it from its holder, and plug it into the last port of ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** 6. t-SNE plot comparing the latent space of a demonstration (from the cable plugging testing dataset) before and after visuo-tactile pretraining, showing how pretraining aligns ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** For both pretrained and non-pretrained tactileonly diffusion policies, the robot would pick up the USB cable, but then would alternate between trying to move back ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We used the same run parameters as the cable plugging task, with 100 demos collected, an 80/20 train/test split, and noise added to the predicted ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Comparing the two imitation learning methods, we found that Diffusion Policy's success rate was less sensitive than ACT, with a higher accuracy for the non-pretrained ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We found that by pretraining a visuo-tactile agent, we were able to solve the cable plugging task, reaching a 95% success rate for ACT.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Success rate for our experiment tasks.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** All experiments were run 20 times, with the total success rate shown.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** IV. EXPERIMENTAL EVALUATION (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | This is significantly higher than the 20% and 45% success rates that learning from vision only with ACT and diffusion policy (respectively) achieves. | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | In all block stacking experiments, as with cable plugging, we observed that visuo-tactile pretraining improved performance for both visuo-tactile and vision-only agents, and that ... | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 7. Success rate for our experiment tasks. All experiments were run 20 times, with the total success rate shown. The use of visuo-tactile ... | p. 6 (Figure/Table caption) |
| IV. EXPERIMENTAL EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Comparing the two imitation learning methods, we found that Diffusion Policy's success rate was less sensitive than ACT, with a higher accuracy for the ... | p. 5 (IV. EXPERIMENTAL EVALUATION) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** In this task, the robot has to navigate to a USB cable, unplug it from its holder, and plug it into the last port of ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** 6. t-SNE plot comparing the latent space of a demonstration (from the cable plugging testing dataset) before and after visuo-tactile pretraining, showing how pretraining aligns ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** For both pretrained and non-pretrained tactileonly diffusion policies, the robot would pick up the USB cable, but then would alternate between trying to move back ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We used the same run parameters as the cable plugging task, with 100 demos collected, an 80/20 train/test split, and noise added to the predicted ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Diagram of our approach. First, a vision encoder and a tactile encoder are pretrained on the collected demonstrations using a temporally informed multi-modal ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Contrastive loss visualization. A series of visual observations V1, V2, ..., VN and tactile observations T1, T2, ..., TN are collected, and the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Imitation learning networks. ACT (left) is trained as an autoencoder, predicting a sequence of actions at each timestep (at). At inference, the latent ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4. Expermental Setup. A GelSight captures tactile observations, while 6 Realsense cameras observe the scene (only two can be seen above; three are out ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5. GelSight sensor outputs, showing the RGB images from the GelSight's camera and the processed strain data for both the covered and uncovered gelsight. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6. t-SNE plot comparing the latent space of a demonstration (from the cable plugging testing dataset) before and after visuo-tactile pretraining, showing how pretraining ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7. Success rate for our experiment tasks. All experiments were run 20 times, with the total success rate shown. The use of visuo-tactile pretraining ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In this task, the robot has to navigate to a USB cable, unplug it from its holder, and plug it into the last port ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Task/environment | 6. t-SNE plot comparing the latent space of a demonstration (from the cable plugging testing dataset) before and after visuo-tactile pretraining, showing how pretraining ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 2 (1) Action), p. 4 (III. METHODS) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 2 (1) Action), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Comparing the two imitation learning methods, we found that Diffusion Policy's success rate was less sensitive than ACT, with a higher accuracy for the ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| We found that by pretraining a visuo-tactile agent, we were able to solve the cable plugging task, reaching a 95% success rate for ACT. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Success rate for our experiment tasks. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| All experiments were run 20 times, with the total success rate shown. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Fig. 1. Diagram of our approach. First, a vision encoder and a tactile encoder are pretrained on the collected demonstrations using a temporally informed ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2. Contrastive loss visualization. A series of visual observations V1, V2, ..., VN and tactile observations T1, T2, ..., TN are collected, and ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Interestingly, the nonpretrained ACT model outperformed the pretrained model in this task. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Also, the large more stochastic motions of Diffusion Policy caused an increase in contact force, with Diffusion Policy increasing GelSight strain by about 15% ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Interestingly, unlike the USB plugging task, the visuo-tactile agents did not consistently outperform their vision-only counterparts. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| This result illustrates the key benefit of using visuo-tactile pretraining on a vision-only agent: the agent gains a significant performance boost from tactile data ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Fig. 1. Diagram of our approach. First, a vision encoder and a tactile encoder are pretrained on the collected demonstrations using a temporally informed ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Fig. 4. Expermental Setup. A GelSight captures tactile observations, while 6 Realsense cameras observe the scene (only two can be seen above; three are ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This result illustrates the key benefit of using visuo-tactile pretraining on a vision-only agent: the agent gains a significant performance boost from tactile data ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Fig. 4. Expermental Setup. A GelSight captures tactile observations, while 6 Realsense cameras observe the scene (only two can be seen above; three are ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Finally, we evaluated the models without vision input (only tactile and positional data). | component/input/data sensitivity | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Interestingly, the nonpretrained ACT model outperformed the pretrained model in this task. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Block Stacking In addition to cable plugging, we also evaluated our pretraining strategy on two block-stacking tasks to see how well the system performed ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Fig. 1. Diagram of our approach. First, a vision encoder and a tactile encoder are pretrained on the collected demonstrations using a temporally informed ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Next, we propose a new methodology for using tactile data in imitation learning: VITaL (Vison-only Imitation using Tactile Latent) pretraining, in which we discard ... | This is significantly higher than the 20% and 45% success rates that learning from vision only with ACT and diffusion policy (respectively) achieves. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Primary metric/result | In all block stacking experiments, as with cable plugging, we observed that visuo-tactile pretraining improved performance for both visuo-tactile and vision-only agents, and that ... | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTAL EVALUATION) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Diffusion's longer re-plan horizon (re-planning every 8 steps instead of every step) and stochastic nature lead to larger motions, tending to jump around the port ...
- **p. 4 / III. METHODS - extractive body cue:** We take advantage of noise scheduler decoupling, using 100 denoising steps during training and 10 steps at inference.
- **p. 4 / III. METHODS - extractive body cue:** The data collection system was run at 10 Hz.
- **p. 5 / III. METHODS - extractive body cue:** The strain map is rendered in the LAB color space, with the brightness of each pixel corresponding to the normal strain (depth), and the color ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A major limitation of this work is that task-specific data was used for pretraining. | p. 6 (V. CONCLUSIONS) |
| body limitation/failure cue | Although this is relatively small in absolute terms, it corresponds to a 50% and 20% decrease in failures for ACT and Diffusion Policy, respectively. | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| body limitation/failure cue | Evaluating this alternative approach is left for future work. | p. 6 (V. CONCLUSIONS) |
| body limitation/failure cue | Fig. 3. Imitation learning networks. ACT (left) is trained as an autoencoder, predicting a sequence of actions at each timestep (at). At inference, the ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | To increase the task's difficulty, we added random noise with a standard deviation of 2.5mm to the agent's actions during inference. | p. 5 (IV. EXPERIMENTAL EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Durring evaluation, we let the agents run until they successfully plugged in the cable, reached an un-recoverable state (ie. dropped the USB cable), or ... | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| All of our experiments were run 20 times. | p. 5 (IV. EXPERIMENTAL EVALUATION) |
| We used the same run parameters as the cable plugging task, with 100 demos collected, an 80/20 train/test split, and noise added to the ... | p. 6 (IV. EXPERIMENTAL EVALUATION) |
| A series of visual observations V1, V2, ..., VN and tactile observations T1, T2, ..., TN are collected, and the vision encoder and tactile ... | p. 3 (III. METHODS) |
| The use of an auto-encoder for this task helps to reduce the negative effects of multi-modal distributions in the training data, as the latent ... | p. 2 (1) Action) |
| Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of ... | p. 2 (1) Action) |
| A diagram of our two implementations can be seen in Figure 3. | p. 3 (III. METHODS) |
| The data collection system was run at 10 Hz. | p. 4 (III. METHODS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. CONCLUSIONS - extractive body cue:** A major limitation of this work is that task-specific data was used for pretraining.
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Although this is relatively small in absolute terms, it corresponds to a 50% and 20% decrease in failures for ACT and Diffusion Policy, respectively.
- **p. 6 / V. CONCLUSIONS - extractive body cue:** Evaluating this alternative approach is left for future work.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Imitation learning networks. ACT (left) is trained as an autoencoder, predicting a sequence of actions at each timestep (at). At inference, the latent ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** To increase the task's difficulty, we added random noise with a standard deviation of 2.5mm to the agent's actions during inference.

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), metrics p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption), results p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTAL EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
