# Evaluation - Octo: An Open-Source Generalist Robot Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.12213; PDF retrieval source: https://arxiv.org/pdf/2405.12213. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL)): Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over 10 trials on one language-conditioned task ...

## Evaluation Body Digest

- **p. 6 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** We evaluate Octo's capabilities to control robots in environments from the pretraining data out-of-the-box and to efficiently finetune to new tasks and environments with small ...
- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** For each robot, we selected two language tasks from the corresponding OXE dataset and performed 10 trials per task with varying initial conditions (details in ...
- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** In the BridgeV2 domain, we performed a fine-grained analysis of the zero-shot capabilities in Table VII; measuring performance on setups seen in the dataset, and ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Finally, we zero-pad any missing camera channels and align the gripper action spaces between the datasets such that a gripper command of +1 means "the ...
- **p. 6 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** Similar to Octo, RT-1-X is pretrained on the Open X-Embodiment robot dataset and aims to control multiple robots zero-shot, thus providing a natural point of ...
- **p. 5 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** We also evaluate Octo for data-efficient finetuning to new environments and tasks, including with new observations (force-torque inputs in "Berkeley Insertion"), new action spaces (joint ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over 10 ...
- **p. 6 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** Octo Controls Multiple Robots Out-of-the-Box 0.2 0.4 0.6 0.8 1.0 WidowX UR5 RT-1-X (35M) Octo (93M) RT-2-X (55B) RT-1 Robot Success Rate Fig.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over ... | p. 8 (Figure/Table caption) |
| 1) Can Octo control multiple robot embodiments and solve | SYSTEM / EVALUATION SCOPE UNRESOLVED | We evaluated our model on the WidowX tasks using goal image conditioning and found that it achieved a 25% higher success rate than when ... | p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| 1) Can Octo control multiple robot embodiments and solve | SYSTEM / EVALUATION SCOPE UNRESOLVED | While the Octo model achieves high success on novel objects, zero-shot performance slightly degrades in a new scene, and high degradation for novel behaviors ... | p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| 1) Can Octo control multiple robot embodiments and solve | SYSTEM / EVALUATION SCOPE UNRESOLVED | Octo Controls Multiple Robots Out-of-the-Box 0.2 0.4 0.6 0.8 1.0 WidowX UR5 RT-1-X (35M) Octo (93M) RT-2-X (55B) RT-1 Robot Success Rate Fig. | p. 6 (1) Can Octo control multiple robot embodiments and solve) |
| III. THE OCTO MODEL | SYSTEM / EVALUATION SCOPE UNRESOLVED | We use the same diffusion training objective during finetuning and update the full model, a recipe which outperformed those that freeze subsets of the ... | p. 5 (III. THE OCTO MODEL) |

## Dataset / Benchmark Role

- **p. 6 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** We evaluate Octo's capabilities to control robots in environments from the pretraining data out-of-the-box and to efficiently finetune to new tasks and environments with small ...
- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** For each robot, we selected two language tasks from the corresponding OXE dataset and performed 10 trials per task with varying initial conditions (details in ...
- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** In the BridgeV2 domain, we performed a fine-grained analysis of the zero-shot capabilities in Table VII; measuring performance on setups seen in the dataset, and ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Finally, we zero-pad any missing camera channels and align the gripper action spaces between the datasets such that a gripper command of +1 means "the ...
- **p. 6 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** Similar to Octo, RT-1-X is pretrained on the Open X-Embodiment robot dataset and aims to control multiple robots zero-shot, thus providing a natural point of ...
- **p. 5 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** We also evaluate Octo for data-efficient finetuning to new environments and tasks, including with new observations (force-torque inputs in "Berkeley Insertion"), new action spaces (joint ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce Octo, an open-source, generalist policy for robotic manipulation. Octo is a transformer-based policy pretrained on 800k diverse robot episodes from the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Model architecture. Left: Octo tokenizes task descriptions (green) and input observations (blue) using a pretrained language model and a lightweight CNN, respectively. Top: ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Training dataset composition. We curate a subset of 25 datasets from the Open X-Embodiment dataset that have image observations, end-effector actions, and show ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Evaluation Tasks. We evaluate Octo on 9 real robot setups across 4 institutions. Our evaluations capture diverse object interactions (e.g., "WidowX BridgeV2"), long ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Zero-Shot Evaluation. Out-of-the-box, Octo can control multiple robots in environments from the pretraining data. When using natural language to specify tasks, Octo outperforms ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over 10 ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 7: Evaluation Tasks. Replicated from the main text for convenience. We evaluate Octo on 9 real robot setups across 4 institutions in zero-shot and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate Octo's capabilities to control robots in environments from the pretraining data out-of-the-box and to efficiently finetune to new tasks and environments with ... | embodiment, simulator version and control stack | p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Task/environment | For each robot, we selected two language tasks from the corresponding OXE dataset and performed 10 trials per task with varying initial conditions (details ... | reset, timeout, object/scene variation | p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. THE OCTO MODEL), p. 2 (I. INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Octo Controls Multiple Robots Out-of-the-Box 0.2 0.4 0.6 0.8 1.0 WidowX UR5 RT-1-X (35M) Octo (93M) RT-2-X (55B) RT-1 Robot Success Rate Fig. | definition/direction/unit from same section | p. 6 (1) Can Octo control multiple robot embodiments and solve) |
| While all methods acted reasonably across tasks in the pretraining environments, we found that on average Octo had a 29% higher success rate than ... | definition/direction/unit from same section | p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| We evaluated our model on the WidowX tasks using goal image conditioning and found that it achieved a 25% higher success rate than when ... | definition/direction/unit from same section | p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| While a number of prior works have proposed other pretraining schemes for imitation finetuning [25, 24, 26], to our knowledge no prior method provides ... | definition/direction/unit from same section | p. 6 (1) Can Octo control multiple robot embodiments and solve) |
| Fig. 3: Training dataset composition. We curate a subset of 25 datasets from the Open X-Embodiment dataset that have image observations, end-effector actions, and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| We use the AdamW optimizer [51] with an inverse square root decay learning rate schedule [97], with weight decay of 0.1 and gradient clipping ... | definition/direction/unit from same section | p. 5 (III. THE OCTO MODEL) |
| In all finetuning experiments, we employ the same recipe: given a small target domain dataset with around 100 trajectories, we finetune for 50k steps ... | definition/direction/unit from same section | p. 5 (III. THE OCTO MODEL) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On average across the six evaluation setups (detailed in Appendix F), Octo outperforms the next best baseline by 52%. | comparison identity and matched condition | p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| We use the same diffusion training objective during finetuning and update the full model, a recipe which outperformed those that freeze subsets of the ... | comparison identity and matched condition | p. 5 (III. THE OCTO MODEL) |
| We found this policy parameterization to outperform policies trained with MSE action heads or discretized action distributions [10] in both zero-shot and finetuning evaluations. | comparison identity and matched condition | p. 5 (III. THE OCTO MODEL) |
| We adopt this as our from-scratch baseline ("ResNet+Transformer Scratch"). | comparison identity and matched condition | p. 6 (1) Can Octo control multiple robot embodiments and solve) |
| The RT-1-X and RT-2-X models [67] are trained on a more restricted subset of 350K episodes (compared to 800k episodes for Octo). | comparison identity and matched condition | p. 6 (1) Can Octo control multiple robot embodiments and solve) |
| For the WidowX and RT-1 Robot evaluations, we also compared to RT-2-X (55 billion parameters) [103] and found that Octo performed similarly. | comparison identity and matched condition | p. 7 (1) Can Octo control multiple robot embodiments and solve) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 2: Model architecture. Left: Octo tokenizes task descriptions (green) and input observations (blue) using a pretrained language model and a lightweight CNN, respectively. ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| For datasets without language annotations, we always use goal image conditioning. | component/input/data sensitivity | p. 5 (III. THE OCTO MODEL) |
| Training Details We trained two variants of our model: Octo-Small with a transformer backbone that mirrors the size of a ViT-S, and Octo-Base with ... | component/input/data sensitivity | p. 5 (III. THE OCTO MODEL) |
| Unless noted otherwise, we perform all ablations on the OctoSmall model due to our compute budget. | component/input/data sensitivity | p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Aggregate Performance Octo-Small (Ours) 83% DATA RT-X dataset mix [67] 60% Single robot dataset (Bridge Data) 43% POLICY Discretized Action Prediction [67] 18% Continuous ... | component/input/data sensitivity | p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Fig. 1: We introduce Octo, an open-source, generalist policy for robotic manipulation. Octo is a transformer-based policy pretrained on 800k diverse robot episodes from ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In principle, collected ∗Lead authors, ordered alphabetically, see Section A for list of contributions. | Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL) |
| Primary metric/result | We evaluated our model on the WidowX tasks using goal image conditioning and found that it achieved a 25% higher success rate than when ... | numeric claim only at cited anchor | p. 7 (1) Can Octo control multiple robot embodiments and solve) |

- Numeric sentences retained from the body:
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** In all finetuning experiments, we employ the same recipe: given a small target domain dataset with around 100 trajectories, we finetune for 50k steps using ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** The ViT-B was trained for 300k steps with a batch size of 2048 using a TPU v4-128 pod, which took 14 hours.
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** A finetuning run of the same model on a single NVIDIA A5000 GPU with 24GB of VRAM takes approximately 5 hours and can be sped ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** We train using 2 frames of observation history; in our preliminary experiments, we found significantly diminishing gains beyond the first additional frame.
- **p. 5 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** Evaluation setups: We evaluate Octo's capabilities across a representative spectrum of 9 robot learning setups at 4 institutions (see Fig.
- **p. 5 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** Each of the finetuning setups uses ∼100 in-domain demonstrations and finetunes in < 5 hours on a NVIDIA A5000 GPU, using the same hyperparameters across ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While the Octo model achieves high success on novel objects, zero-shot performance slightly degrades in a new scene, and high degradation for novel behaviors ... | p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| body limitation/failure cue | Finally, we zero-pad any missing camera channels and align the gripper action spaces between the datasets such that a gripper command of +1 means ... | p. 5 (III. THE OCTO MODEL) |
| body limitation/failure cue | (1) The hyperparameters α, γ, and σ correspond to the noise schedule: we use the standard cosine schedule from [66]. | p. 5 (III. THE OCTO MODEL) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The ViT-B was trained for 300k steps with a batch size of 2048 using a TPU v4-128 pod, which took 14 hours. | p. 5 (III. THE OCTO MODEL) |
| In all finetuning experiments, we employ the same recipe: given a small target domain dataset with around 100 trajectories, we finetune for 50k steps ... | p. 5 (III. THE OCTO MODEL) |
| Prior model designs that use standard transformer backbones or fuse visual encoders with MLP output heads lock in the type and order of inputs ... | p. 4 (III. THE OCTO MODEL) |
| The attention pattern of the Octo transformer is block-wise masked: observation tokens can only attend causally to tokens from the same or earlier time ... | p. 4 (III. THE OCTO MODEL) |
| Comparisons: We compare Octo's ability to control multiple robots out-of-the-box to the best openly available generalist robot policy, RT-1-X [67], using the released checkpoint. | p. 6 (1) Can Octo control multiple robot embodiments and solve) |
| A ViT-B visual encoder is initialized to the VC-1 weights [57], a state-of-the-art visual representation pretrained on 4,000 hours of ego-centric videos and ImageNet, ... | p. 6 (1) Can Octo control multiple robot embodiments and solve) |
| Each domain uses ∼100 target demonstrations and the same finetuning hyperparameters. | p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Unless noted otherwise, we perform all ablations on the OctoSmall model due to our compute budget. | p. 7 (1) Can Octo control multiple robot embodiments and solve) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** While the Octo model achieves high success on novel objects, zero-shot performance slightly degrades in a new scene, and high degradation for novel behaviors like ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Finally, we zero-pad any missing camera channels and align the gripper action spaces between the datasets such that a gripper command of +1 means "the ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** (1) The hyperparameters α, γ, and σ correspond to the noise schedule: we use the standard cosine schedule from [66].

- **Evidence anchors reviewed:** datasets p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 5 (1) Can Octo control multiple robot embodiments and solve), metrics p. 8 (Figure/Table caption), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 4 (Figure/Table caption), baselines p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), results p. 8 (Figure/Table caption), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over 10 trials on one language-conditioned task ... (p. 8, Figure/Table caption).
- **Metric evidence:** While all methods acted reasonably across tasks in the pretraining environments, we found that on average Octo had a 29% higher success rate than RT-1-X (35M parameters). (p. 7, 1) Can Octo control multiple robot embodiments and solve).
- **Baseline/ablation evidence:** On average across the six evaluation setups (detailed in Appendix F), Octo outperforms the next best baseline by 52%. (p. 7, 1) Can Octo control multiple robot embodiments and solve).
- **Failure/negative evidence:** Although these models represent significant steps toward a true "general-purpose robot model," they have been limited in multiple important aspects: they typically constrain downstream users to a pre-defined and often ... (p. 2, I. INTRODUCTION).
