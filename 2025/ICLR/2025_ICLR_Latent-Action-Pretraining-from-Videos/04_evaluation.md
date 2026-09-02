# Evaluation - Latent Action Pretraining from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2410.11758.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS)): Furthermore, by comparing LAPA which does not leverage action-labeled trajectories during pretraining with models that use action-labeled trajectories during pretraining (ACTIONVLA and OPENVLA), we observe an interesting finding: LAPA o ...

## Evaluation Body Digest

- **p. 5 / 4 EXPERIMENTS - extractive body cue:** 4.1 BENCHMARKS AND ENVIRONMENTS We evaluate the effectiveness of LAPA on 9 different task categories in 2 different simulation environments and 3 different real-world robotic ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Across three benchmarks spanning both simulation and real-world robot experiments, we show that our method significantly improves transfer to downstream tasks compared to existing approaches.
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Real-World Tabletop Manipulation experiments used a 7 DOF Franka Emika Panda robot arm in three environments (shown in Figure 9 (c)).
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** We compare against OPENVLA for real-world robot experiments by fine-tuning the pretrained OPENVLA on our downstream tasks.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** OPENVLA (Kim et al., 2024) is a state-of-the-art VLA model that was pretrained on 970k realworld robot demonstrations from the Open X-Embodiment Dataset (Collaboration et ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We evaluate on both simulation (left) and real-world robot setup (right).
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 4.5 LEARNING FROM HUMAN MANIPULATION VIDEOS Scratch UniPi VPT LAPA 0 10 20 30 40 50 60 AVG Success Rate (%) 34.4 0.7 45.8 52.1 ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Open-X Pretraining From Figure 3, we see that VLAs pretrained on the Open-X dataset outperforms VLAs pretrained on the Bridgev2 dataset, showing that data scaling ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 5); B DETAILS ON EXPERIMENTAL SETUP (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, by comparing LAPA which does not leverage action-labeled trajectories during pretraining with models that use action-labeled trajectories during pretraining (ACTIONVLA and OPENVLA), we ... | p. 7 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Scaling Ablation Results of LAPA. We scale 4 dimensions of LAPA: model parameters (in millions), data size (ratio among Bridgev2), and the ... | p. 9 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results imply that when scaling pretraining to Internet-scale videos that go beyond manipulation videos, scaling LAPA in terms of model, dataset, and latent ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Average success rate (%) ± StdErr are shown (detailed results provided in Appendix G.3). | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4.5 LEARNING FROM HUMAN MANIPULATION VIDEOS Scratch UniPi VPT LAPA 0 10 20 30 40 50 60 AVG Success Rate (%) 34.4 0.7 45.8 ... | p. 8 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / 4 EXPERIMENTS - extractive body cue:** 4.1 BENCHMARKS AND ENVIRONMENTS We evaluate the effectiveness of LAPA on 9 different task categories in 2 different simulation environments and 3 different real-world robotic ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Across three benchmarks spanning both simulation and real-world robot experiments, we show that our method significantly improves transfer to downstream tasks compared to existing approaches.
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Real-World Tabletop Manipulation experiments used a 7 DOF Franka Emika Panda robot arm in three environments (shown in Figure 9 (c)).
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** We compare against OPENVLA for real-world robot experiments by fine-tuning the pretrained OPENVLA on our downstream tasks.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** OPENVLA (Kim et al., 2024) is a state-of-the-art VLA model that was pretrained on 970k realworld robot demonstrations from the Open X-Embodiment Dataset (Collaboration et ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We evaluate on both simulation (left) and real-world robot setup (right).
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 4.5 LEARNING FROM HUMAN MANIPULATION VIDEOS Scratch UniPi VPT LAPA 0 10 20 30 40 50 60 AVG Success Rate (%) 34.4 0.7 45.8 52.1 ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Open-X Pretraining From Figure 3, we see that VLAs pretrained on the Open-X dataset outperforms VLAs pretrained on the Bridgev2 dataset, showing that data scaling ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Problem Formulation. We investigate building a generalist robotic foundation model from human motion videos without action labels. VQ-VAE-based objective (Van Den Oord et ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Overview of Latent Action Pretraining. (1) Latent Action Quantization: We first learn discrete latent actions in a fully unsupervised manner using the VQ-VAE ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Language Table Results. Average Success Rate (%) ± StdErr across the three different pretrain- finetune combinations from the Language Table benchmark as described ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Real-world Tabletop Manipulation Results. We evaluate on a total of 54 rollouts for each model encompassing unseen object combinations, unseen objects and unseen ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Evaluation Results divided into eval types. We average the success rate across the 3 tasks depending on what capability we are trying to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Pretraining from Human Video Results. Average success rate (%) ± StdErr of LAPA and baselines pretrained on human manipulation videos where the embodiment ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Scaling Ablation Results of LAPA. We scale 4 dimensions of LAPA: model parameters (in millions), data size (ratio among Bridgev2), and the latent ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 6: Latent Action Analysis. We condition the current observation x1 and quantized latent action to the decoder of the latent action quantization model. We ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1 BENCHMARKS AND ENVIRONMENTS We evaluate the effectiveness of LAPA on 9 different task categories in 2 different simulation environments and 3 different real-world ... | embodiment, simulator version and control stack | p. 5 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Task/environment | Across three benchmarks spanning both simulation and real-world robot experiments, we show that our method significantly improves transfer to downstream tasks compared to existing ... | reset, timeout, object/scene variation | p. 10 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (2. Latent Pretraining), p. 2 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (2. Latent Pretraining), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Average Success Rate (%) ± StdErr across the three different pretrainfinetune combinations from the Language Table benchmark as described in Table 3. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Average success rate (%) ± StdErr are shown (detailed results provided in Appendix G.3). | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| We average the success rate across the 3 tasks depending on what capability we are trying to quantify: (1) seen objects but unseen combinations, ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Average success rate (%) ± StdErr of LAPA and baselines pretrained on human manipulation videos where the embodiment and environment gap is extreme. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| 4.5 LEARNING FROM HUMAN MANIPULATION VIDEOS Scratch UniPi VPT LAPA 0 10 20 30 40 50 60 AVG Success Rate (%) 34.4 0.7 45.8 ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| We scale 4 dimensions of LAPA: model parameters (in millions), data size (ratio among Bridgev2), and the latent action sequence and vocabulary size, and ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| 5 ABLATION AND ANALYSIS 5.1 SCALING MODEL, DATA, AND LATENT ACTION SIZE 30 75 150 300 54 55 56 57 AVG Success Rate (%) ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 15: Additional Ablation Results of LAPA. We further analyze the performance of LAPA by varying the window size for latent action quantization and ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (2024) since it is not a behavior cloning baseline. | comparison identity and matched condition | p. 5 (4 EXPERIMENTS) |
| 4.2 BASELINES For the underlying VLM, we use the 7B Large World Model (LWM-Chat-1M) (Liu et al., 2024). | comparison identity and matched condition | p. 5 (4 EXPERIMENTS) |
| Further details of baseline models are provided in Appendix C. | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| As shown in Table 1, LAPA largely outperforms SCRATCH and narrows the gap with ACTIONVLA despite not using action labels during pretraining. | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| Also, as shown in Table 2, LAPA (Open-X) outperforms OpenVLA (Open-X) on all types of generalization settings. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| When comparing LAPA with OPENVLA, we see that LAPA significantly outperforms OPENVLA on 2 out of 3 tasks (Figure 3). | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1: Problem Formulation. We investigate building a generalist robotic foundation model from human motion videos without action labels. VQ-VAE-based objective (Van Den Oord ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| 4.4 REAL-WORLD RESULTS We pretrain our models on (1) Bridgev2 (Walke et al., 2023) to measure the cross-embodiment performance (WidowX embodiment for pretraining and ... | component/input/data sensitivity | p. 6 (4 EXPERIMENTS) |
| We use a LAPA model that has only undergone pretraining, without any action finetuning. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| 6 LIMITATIONS AND CONCLUSION In this paper, we introduce Latent Action Pretraining, a scalable pretraining method for building VLAs without using ground-truth action labels. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| In this section, we demonstrate the effectiveness of Latent Action Pretraining as a general-purpose pretaining method. | component/input/data sensitivity | p. 5 (4 EXPERIMENTS) |
| This highlights LAPA's effectiveness in a multi-embodiment setting by showcasing its ability to leverage a shared latent action space during pretraining, akin to how ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and ... | Furthermore, by comparing LAPA which does not leverage action-labeled trajectories during pretraining with models that use action-labeled trajectories during pretraining (ACTIONVLA and OPENVLA), we ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Primary metric/result | Figure 5: Scaling Ablation Results of LAPA. We scale 4 dimensions of LAPA: model parameters (in millions), data size (ratio among Bridgev2), and the ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** We assess our models on 4 tasks (Figure 9 (b)) using the 7 DOF WidowX robot arm.
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** Each task involves 150 trajectories across 15 objects.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** In-domain (1k) Cross-task (7k) Cross-env (1k) Seen Unseen Seen Unseen Seen Unseen SCRATCH 15.6±9.2 15.2±8.3 27.2±13.6 22.4±11.0 15.6±9.2 15.2±8.3 UNIPI 22.0±12.5 13.2±7.7 20.8±12.0 16.0±9.1 13.6±8.6 ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Pretraining LAPA on 181k trajectories and finetuning on only separate tasks (7k), we evaluate all 5 task categories, similar to the in-domain setup, to assess ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** When comparing LAPA and SCRATCH in Table 1 and Table 7, 8 in Appendix G.1, latent pretraining significantly benefits the separate task as well the ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We evaluate on a total of 54 rollouts for each model encompassing unseen object combinations, unseen objects and unseen instructions.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away from the red cube and red ... | p. 25 (Figure/Table caption) |
| body limitation/failure cue | We observe that most failures of LAPA are due to early grasping. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | Like before, UNIPI is constrained by its diffusion model's planning limitations, while VPT performs strongly, even surpassing ACTIONVLA in the unseen setting. | p. 6 (4 EXPERIMENTS) |
| body limitation/failure cue | 6 LIMITATIONS AND CONCLUSION In this paper, we introduce Latent Action Pretraining, a scalable pretraining method for building VLAs without using ground-truth action labels. | p. 10 (4 EXPERIMENTS) |
| body limitation/failure cue | 3We leave parameter efficient fine-tuning approaches as future work for finetuning (Hu et al., 2022). | p. 5 (4 EXPERIMENTS) |
| body limitation/failure cue | UNIPI (Du et al., 2023) uses a video diffusion model during pretraining to generate video rollouts given a language instruction, which does not require ... | p. 5 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Codebook replacement technique from NSVQ is applied during early training steps to maximize codebook utilization. | p. 4 (2. Latent Pretraining) |
| In contrast, OPENVLA required a total of 21,500 A100-hours with a batch size of 2048. | p. 8 (4 EXPERIMENTS) |
| For pretraining LAPA (Open-X), the best-performing model, we use 8 H100 GPUs for 34 hours with a batch size of 128 (total of 272 ... | p. 8 (4 EXPERIMENTS) |
| Action Finetuning Latent Action Pretraining x1 0 1 2 3 4 Codebook of Latent Actions Pick up the milk and put it in the ... | p. 3 (2. Latent Pretraining) |
| Related work pretrains a vision encoder on egocentric human videos (Grauman et al., 2022) to improve visual representations (Nair et al., 2022; Dasari et ... | p. 3 (2. Latent Pretraining) |
| The decoder is trained to take the latent action zt and xt and reconstruct xt+H. | p. 4 (2. Latent Pretraining) |
| As with latent pretraining, we freeze the vision encoder and unfreeze all of the parameters of the underlying language model.3 | p. 5 (2. Latent Pretraining) |
| 2We also tried leaving the latent action head and adding additional head to decode the latent to ground-truth actions following Schmidt & Jiang (2024) ... | p. 5 (4 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 25 / Figure/Table caption - extractive body cue:** Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away from the red cube and red pentagon', ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We observe that most failures of LAPA are due to early grasping.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Like before, UNIPI is constrained by its diffusion model's planning limitations, while VPT performs strongly, even surpassing ACTIONVLA in the unseen setting.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 6 LIMITATIONS AND CONCLUSION In this paper, we introduce Latent Action Pretraining, a scalable pretraining method for building VLAs without using ground-truth action labels.
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** 3We leave parameter efficient fine-tuning approaches as future work for finetuning (Hu et al., 2022).
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** UNIPI (Du et al., 2023) uses a video diffusion model during pretraining to generate video rollouts given a language instruction, which does not require any ...

- **Evidence anchors reviewed:** datasets p. 5 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), metrics p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), baselines p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), results p. 7 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
