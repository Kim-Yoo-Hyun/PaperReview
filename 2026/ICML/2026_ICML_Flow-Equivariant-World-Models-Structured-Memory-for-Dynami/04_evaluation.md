# Evaluation - Flow Equivariant World Models: Structured Memory for Dynamic Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=jgqFnXEDGG; PDF retrieval source: https://openreview.net/pdf/25b19208166528c9c48b16cdd741d730218a8089.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 23 (Figure/Table caption), p. 6 (4. Experiments), p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 7 (4.2. 2D MNIST World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark)): Comparatively, the DFoT model achieves an equivariance error of 2.36.

## Evaluation Body Digest

- **p. 7 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** To validate FloWM on this more difficult setting, we further introduce a simple 3D dataset, built in the Miniworld environment (Chevalier-Boisvert et al., 2023).
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** The optimal distance for the reward function is at a distance of 2 away. of FloWM to more realistic datasets, and reinforces that the bottleneck ...
- **p. 6 / 4.2. 2D MNIST World Benchmark - extractive body cue:** To test our architecture on partially observable dynamic world modeling, we propose a simple MNIST World dataset.
- **p. 6 / 4.1. Diffusion-based and Recurrent Baselines - extractive body cue:** Following standard practice, we first train a spatial downsampling VAE for each dataset to encode video frames into a latent representation that is then input ...
- **p. 7 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** On the 3D Dynamic Block World dataset, we compare our Transformer-Based FloWM from Section 3.2 and Fig.
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** In total the experiment is run across 8 episodes, and requires no additional trained parameters.
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** We find that before training, the FloWM has an equivariance error of 6.96 (in L2 distance) meaning the original predictions are off by roughly 5 ...
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** Comparatively, the DFoT model achieves an equivariance error of 2.36.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.2. 2D MNIST World Benchmark (p. 6); 4.3. 3D Dynamic Block World Benchmark (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. 3D Dynamic Block World Benchmark | EMPIRICAL / SOURCE-REPORTED EVALUATION | Comparatively, the DFoT model achieves an equivariance error of 2.36. | p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 6. As with the static MNIST World dataset, in this setting, the default configuration of FloWM with velocity channels only adds noise to ... | p. 23 (Figure/Table caption) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our results demonstrate that the structured dynamic memory afforded by flow equivariance is critical for modeling partially observed dynamic environments. | p. 6 (4. Experiments) |
| 4.3. 3D Dynamic Block World Benchmark | EMPIRICAL / SOURCE-REPORTED EVALUATION | Experiment details are in §G, and additional results on textured and static variants of Block World are in §E. | p. 7 (4.3. 3D Dynamic Block World Benchmark) |
| 4.2. 2D MNIST World Benchmark | EMPIRICAL / SOURCE-REPORTED EVALUATION | Through additional results in §F, we explore how the DFoT model can sometimes handle partial observability, object dynamics, and self-motion individually, but not in ... | p. 7 (4.2. 2D MNIST World Benchmark) |

## Dataset / Benchmark Role

- **p. 7 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** To validate FloWM on this more difficult setting, we further introduce a simple 3D dataset, built in the Miniworld environment (Chevalier-Boisvert et al., 2023).
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** The optimal distance for the reward function is at a distance of 2 away. of FloWM to more realistic datasets, and reinforces that the bottleneck ...
- **p. 6 / 4.2. 2D MNIST World Benchmark - extractive body cue:** To test our architecture on partially observable dynamic world modeling, we propose a simple MNIST World dataset.
- **p. 6 / 4.1. Diffusion-based and Recurrent Baselines - extractive body cue:** Following standard practice, we first train a spatial downsampling VAE for each dataset to encode video frames into a latent representation that is then input ...
- **p. 7 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** On the 3D Dynamic Block World dataset, we compare our Transformer-Based FloWM from Section 3.2 and Fig.
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** In total the experiment is run across 8 episodes, and requires no additional trained parameters.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Flow Equivariant World Models (FloWM) maintain structured dynamic memory in partially observed environ- ments. When an agent observes dynamics, turns away, then turns ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Existing world model memory is inherently limited in partially observed dynamic environments. a) Standard autoregressive video diffusion evicts frames beyond the sliding window. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Visualization of the Simple Recurrent FloWM on MNIST World. The world state (bottom) is windowed to pro- duce an observation ft. The RNN ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Transformer-Based FloWM. a) Image observation ft at time t and memory tokens ht within the current field of view (FoV) are passed through ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. FloWM generalizes further and trains faster. a) Timesteps 0 to 49 are given as observations. Models are trained to predict up to t ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Flow Equivariant World Models accurately predict moving objects in a 3D environment over long time-spans. a) Visualization of rollout (after 50 observation frames). ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Downstream Planning on Block World. Distance to the red block using a simple MPC planning algorithm for different learned world models. The optimal ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Ground truth block positions and trained probe predictions visualized for two of six blocks in a Dynamic Block World rollout (top down view). ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To validate FloWM on this more difficult setting, we further introduce a simple 3D dataset, built in the Miniworld environment (Chevalier-Boisvert et al., 2023). | embodiment, simulator version and control stack | p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Task/environment | The optimal distance for the reward function is at a distance of 2 away. of FloWM to more realistic datasets, and reinforces that the ... | reset, timeout, object/scene variation | p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 6 (4.2. 2D MNIST World Benchmark) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We find that before training, the FloWM has an equivariance error of 6.96 (in L2 distance) meaning the original predictions are off by roughly ... | definition/direction/unit from same section | p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Comparatively, the DFoT model achieves an equivariance error of 2.36. | definition/direction/unit from same section | p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Length extrapolation errors vs. time are plotted in Fig. | definition/direction/unit from same section | p. 7 (4.2. 2D MNIST World Benchmark) |
| Such ‘hallucinations' make the model's MSE error worse than the simple all-black baseline. | definition/direction/unit from same section | p. 7 (4.2. 2D MNIST World Benchmark) |
| Figure 13. Rollout Error (MSE) vs. Forward Prediction Steps for all data subsets of MNIST World. The dynamic subset is replicated from the main ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Our results demonstrate that the structured dynamic memory afforded by flow equivariance is critical for modeling partially observed dynamic environments. | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Figure 11. Probe Prediction Through Time on a test set rollout on Dynamic Block World. a) Here we visualize the position prediction for the ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 6. As with the static MNIST World dataset, in this setting, the default configuration of FloWM with velocity channels only adds noise to ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also include ablations FloWM (no VC), FloWM (no VC, no SME), and the diffusion baselines mentioned above. | comparison identity and matched condition | p. 7 (4.2. 2D MNIST World Benchmark) |
| 4 with the diffusion and RSSM baselines, also including the ablations FloWM (no VC) and FloWM (no VC, no SME). | comparison identity and matched condition | p. 7 (4.3. 3D Dynamic Block World Benchmark) |
| This baseline is visualized in Figure 2(c). | comparison identity and matched condition | p. 6 (4.1. Diffusion-based and Recurrent Baselines) |
| For the 3D Block World dataset, we additionally implement a Recurrent State Space Model (RSSM) based on Dreamer V3's world model, as a representative ... | comparison identity and matched condition | p. 6 (4.1. Diffusion-based and Recurrent Baselines) |
| As presented in Figure 7 and Table 3, FloWM quickly finds its way to the red block, while the baselines often hallucinate a red ... | comparison identity and matched condition | p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Though this task is relatively simple, we believe it demonstrates the downstream utility of being able to properly predict dynamics in partially observed settings, ... | comparison identity and matched condition | p. 8 (4.3. 3D Dynamic Block World Benchmark) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6. Flow Equivariant World Models accurately predict moving objects in a 3D environment over long time-spans. a) Visualization of rollout (after 50 observation ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We include ablations on data subsets with different combinations of partial observability, presence of object dynamics, and self-motion in §F. | component/input/data sensitivity | p. 6 (4.2. 2D MNIST World Benchmark) |
| Flow Equivariant World Models: Structured Memory for Dynamic Environments Figure 6. | component/input/data sensitivity | p. 7 (4.2. 2D MNIST World Benchmark) |
| Learned Equivariant Representation. | component/input/data sensitivity | p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Finally, we then leverage these probes to quantitatively test one core assumption made in constructing the 3D FloWM model - that the FloWM ViT ... | component/input/data sensitivity | p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Figure 5. FloWM generalizes further and trains faster. a) Timesteps 0 to 49 are given as observations. Models are trained to predict up to ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which ... | Comparatively, the DFoT model achieves an equivariance error of 2.36. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 23 (Figure/Table caption), p. 6 (4. Experiments), p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 7 (4.2. 2D MNIST World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Primary metric/result | Table 6. As with the static MNIST World dataset, in this setting, the default configuration of FloWM with velocity channels only adds noise to ... | numeric claim only at cited anchor | p. 23 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** We report the metrics on rollouts of 70 and 210 prediction frames, given 70 frames of context in Table 21.
- **p. 7 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** Similar to the 2D experiments, we observe that FloWM's predictions remain consistent for as many as 210 frames of future prediction, while the baselines diverge.
- **p. 7 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** This supports the applicability 1We report results on 70 frames of context to match the DFoTSSM training requirements better, and find either 50 or 70 ...
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** In total the experiment is run across 8 episodes, and requires no additional trained parameters.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Similarly, future work may extend FloWM beyond the current discrete velocity sets V to continuous families; however prior empirical and theoretical results suggest that ... | p. 9 (6. Discussion) |
| body limitation/failure cue | Figure 2. Existing world model memory is inherently limited in partially observed dynamic environments. a) Standard autoregressive video diffusion evicts frames beyond the sliding ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Predictions from FloWM remain consistent with ground truth for 150 timesteps past the observation window, well beyond its training prediction horizon of 20 timesteps, ... | p. 7 (4.2. 2D MNIST World Benchmark) |
| body limitation/failure cue | During inference, DFoT maintains a sliding window composed of context and prediction frames at different noise levels; after denoising is complete on one chunk, ... | p. 6 (4.1. Diffusion-based and Recurrent Baselines) |
| body limitation/failure cue | Figure 5. FloWM generalizes further and trains faster. a) Timesteps 0 to 49 are given as observations. Models are trained to predict up to ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Perceptually, the DFoT and SSM models frequently hallucinate new objects and forget old ones, while the RSSM model degrades to a blurry average of ... | p. 7 (4.3. 3D Dynamic Block World Benchmark) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Ultimately, over the entire test set, we find the FloWM probe is able to decode block position with 96% accuracy while the DFoT & ... | p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Precisely, we compute an approximate ‘equivariance error' as the difference between the decoded position of the block at time t + 1, and the ... | p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Code is available on our project page. | p. 6 (4. Experiments) |
| To test length generalization, we additionally run inference up to 150 prediction frames. | p. 6 (4.2. 2D MNIST World Benchmark) |
| We further find that models combining SME and VC require orders of magnitude less training steps to converge compared with those without these priors, ... | p. 7 (4.2. 2D MNIST World Benchmark) |
| Predictions from FloWM remain consistent with ground truth for 150 timesteps past the observation window, well beyond its training prediction horizon of 20 timesteps, ... | p. 7 (4.2. 2D MNIST World Benchmark) |
| Therefore, instead, we simply treat the output of the encoder as if it were performing this equivariant lift, and anticipate that the transformation T ... | p. 5 (3.1. Generalized Flow Equivariance) |
| The flow ψt maps from some initial group element g0 to a new element gt (i.e. ψt(ν) · g0 = gt) by following the ... | p. 2 (3.1. Generalized Flow Equivariance) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6. Discussion - extractive body cue:** Similarly, future work may extend FloWM beyond the current discrete velocity sets V to continuous families; however prior empirical and theoretical results suggest that even ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Existing world model memory is inherently limited in partially observed dynamic environments. a) Standard autoregressive video diffusion evicts frames beyond the sliding window. ...
- **p. 7 / 4.2. 2D MNIST World Benchmark - extractive body cue:** Predictions from FloWM remain consistent with ground truth for 150 timesteps past the observation window, well beyond its training prediction horizon of 20 timesteps, while ...
- **p. 6 / 4.1. Diffusion-based and Recurrent Baselines - extractive body cue:** During inference, DFoT maintains a sliding window composed of context and prediction frames at different noise levels; after denoising is complete on one chunk, the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. FloWM generalizes further and trains faster. a) Timesteps 0 to 49 are given as observations. Models are trained to predict up to t ...
- **p. 7 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** Perceptually, the DFoT and SSM models frequently hallucinate new objects and forget old ones, while the RSSM model degrades to a blurry average of many ...

- **Evidence anchors reviewed:** datasets p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 6 (4.2. 2D MNIST World Benchmark), p. 6 (4.1. Diffusion-based and Recurrent Baselines), p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark), metrics p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 7 (4.2. 2D MNIST World Benchmark), p. 7 (4.2. 2D MNIST World Benchmark), p. 26 (Figure/Table caption), p. 6 (4. Experiments), baselines p. 7 (4.2. 2D MNIST World Benchmark), p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 6 (4.1. Diffusion-based and Recurrent Baselines), p. 6 (4.1. Diffusion-based and Recurrent Baselines), p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark), results p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 23 (Figure/Table caption), p. 6 (4. Experiments), p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 7 (4.2. 2D MNIST World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
