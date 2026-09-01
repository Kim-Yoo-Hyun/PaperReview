# Evaluation - CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2601.09512; PDF retrieval source: https://arxiv.org/pdf/2601.09512. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION), p. 5 (V. EVALUATION), p. 4 (Figure/Table caption)): Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three random seeds, and the shaded regions ...

## Evaluation Body Digest

- **p. 5 / V. EVALUATION - extractive PDF cue:** We pre-train the policy on a mix of 1000 demonstrations collected in our lab for tasks different from the five continual learning tasks and 2000 ...
- **p. 5 / V. EVALUATION - extractive PDF cue:** Experimental Setup 1) Tasks: We conduct our simulation experiments using the LIBERO benchmark [33], which is designed specifically for continual learning.
- **p. 6 / V. EVALUATION - extractive PDF cue:** Training takes about one hour per simulation task and five hours per real-world task on an NVIDIA RTX 5090 GPU.
- **p. 6 / V. EVALUATION - extractive PDF cue:** Intuitively, compressing new knowledge into fewer model parameters reduces the robot's ability to learn novel tasks.
- **p. 7 / V. EVALUATION - extractive PDF cue:** 5: Increasing the dynamic expansion threshold γ reduces the number of added adapters and, consequently, the capability to learn new tasks (lower FWT), but does ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three random ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** 3) Metrics: We use three metrics to assess continual learning [33], [46]: Area under the success rate curve (AUC), forward transfer (FWT), and negative backward ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** Denoting the success rate on task n after learning the first m ≥n tasks as rn/m, the metrics are defined as AUC = 1 N ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** V. EVALUATION (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three ... | p. 10 (Figure/Table caption) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | CLARE achieves the highest overall performance, as measured by AUC, outperforming the best baseline, ER, by about 10 to 14 percentage points. | p. 6 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Backbone Expandable layers AUC ↑ FWT ↑ NBT ↓ DiT-Dec Linear projection 75.1±1.3 75.0±1.4 1.9±0.4 Decoder 41.8±2.4 45.5±3.8 7.0±1.7 DiT-EncDec Encoder 65.4±2.7 66.5±2.2 1.7±1.2 ... | p. 6 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | CLARE achieves the highest overall performance, as measured by AUC, and demonstrates strong capabilities to acquire new skills without forgetting. "NA" indicates not available. | p. 7 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | We conduct extensive simulation and real-world experiments with a focus on the following research questions: • Q1: Which layers are best suited for expansion? ... | p. 5 (V. EVALUATION) |

## Dataset / Benchmark Role

- **p. 5 / V. EVALUATION - extractive PDF cue:** We pre-train the policy on a mix of 1000 demonstrations collected in our lab for tasks different from the five continual learning tasks and 2000 ...
- **p. 5 / V. EVALUATION - extractive PDF cue:** Experimental Setup 1) Tasks: We conduct our simulation experiments using the LIBERO benchmark [33], which is designed specifically for continual learning.
- **p. 6 / V. EVALUATION - extractive PDF cue:** Training takes about one hour per simulation task and five hours per real-world task on an NVIDIA RTX 5090 GPU.
- **p. 6 / V. EVALUATION - extractive PDF cue:** Intuitively, compressing new knowledge into fewer model parameters reduces the robot's ability to learn novel tasks.
- **p. 7 / V. EVALUATION - extractive PDF cue:** 5: Increasing the dynamic expansion threshold γ reduces the number of added adapters and, consequently, the capability to learn new tasks (lower FWT), but does ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: CLARE autonomously and continually injects lightweight adapters into selected layers of a pre-trained vision-language-action model (VLA). During inference, the most relevant adapters are ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: CLARE sequentially adds adapters and discriminators as side branches to selected VLA modules. Top: During inference, our router activates only the most relevant ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: Model architecture of our base VLA policy. The modules for inserting CLARE adapters are shown as dashed blocks. • Q4: What is the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: CLARE scales to continual learning of 40 tasks on LIBERO-40, whereas experience replay (ER) exhibits significant performance degrada- tion. layers and adaptive layer ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: Increasing the dynamic expansion threshold γ reduces the number of added adapters and, consequently, the capability to learn new tasks (lower FWT), but ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Our five real-world manipulation tasks involve objects of different shapes, weights, and dynamics, as well as different motion patterns. for ER, and NBT ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Inference time and memory complexity of CLARE in our hardware experiments. The values for stages 6-10 are linearly extrapolated.
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three random ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We pre-train the policy on a mix of 1000 demonstrations collected in our lab for tasks different from the five continual learning tasks and ... | embodiment, simulator version and control stack | p. 5 (V. EVALUATION), p. 5 (V. EVALUATION) |
| Task/environment | Experimental Setup 1) Tasks: We conduct our simulation experiments using the LIBERO benchmark [33], which is designed specifically for continual learning. | reset, timeout, object/scene variation | p. 5 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| 3) Metrics: We use three metrics to assess continual learning [33], [46]: Area under the success rate curve (AUC), forward transfer (FWT), and negative ... | definition/direction/unit from same section | p. 6 (V. EVALUATION) |
| Denoting the success rate on task n after learning the first m ≥n tasks as rn/m, the metrics are defined as AUC = 1 ... | definition/direction/unit from same section | p. 6 (V. EVALUATION) |
| Fig. 2: CLARE sequentially adds adapters and discriminators as side branches to selected VLA modules. Top: During inference, our router activates only the most ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| We conduct extensive simulation and real-world experiments with a focus on the following research questions: • Q1: Which layers are best suited for expansion? ... | definition/direction/unit from same section | p. 5 (V. EVALUATION) |
| CLARE achieves the highest overall performance, as measured by AUC, and demonstrates strong capabilities to acquire new skills without forgetting. "NA" indicates not available. | definition/direction/unit from same section | p. 7 (V. EVALUATION) |
| The policy generates chunks of H = 16 end-effector displacement actions, and the first h = 8 actions are sent to a Cartesian controller ... | definition/direction/unit from same section | p. 5 (V. EVALUATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 5) Baselines: We include seven baselines for continual learning without oracle task IDs. | comparison identity and matched condition | p. 6 (V. EVALUATION) |
| CLARE achieves the highest overall performance, as measured by AUC, outperforming the best baseline, ER, by about 10 to 14 percentage points. | comparison identity and matched condition | p. 6 (V. EVALUATION) |
| Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| LIBERO-Long LIBERO-Goal LIBERO-Spatial Method AUC ↑ FWT ↑ NBT ↓ AUC ↑ FWT ↑ NBT ↓ AUC ↑ FWT ↑ NBT ↓ SeqFFT 22.4±0.3 ... | comparison identity and matched condition | p. 7 (V. EVALUATION) |
| CLARE achieves the highest overall performance, as measured by AUC, and demonstrates strong capabilities to acquire new skills without forgetting. "NA" indicates not available. | comparison identity and matched condition | p. 7 (V. EVALUATION) |
| Fig. 1: CLARE autonomously and continually injects lightweight adapters into selected layers of a pre-trained vision-language-action model (VLA). During inference, the most relevant adapters ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 1: CLARE autonomously and continually injects lightweight adapters into selected layers of a pre-trained vision-language-action model (VLA). During inference, the most relevant adapters ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| 5) Baselines: We include seven baselines for continual learning without oracle task IDs. | component/input/data sensitivity | p. 6 (V. EVALUATION) |
| As an ablation, we also consider an encoder-decoder backbone (DiT-EncDec), for which adapters can be added to all 12 transformer layers. | component/input/data sensitivity | p. 6 (V. EVALUATION) |
| CLARE achieves the highest overall performance, as measured by AUC, and demonstrates strong capabilities to acquire new skills without forgetting. "NA" indicates not available. | component/input/data sensitivity | p. 7 (V. EVALUATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| As our method is architecture-agnostic, we keep the following sections general. | Fig. 8: Success rate curves of CLARE and five baselines on the LIBERO-Long benchmark. The solid lines represent the average success rates across three ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION), p. 5 (V. EVALUATION), p. 4 (Figure/Table caption) |
| Primary metric/result | CLARE achieves the highest overall performance, as measured by AUC, outperforming the best baseline, ER, by about 10 to 14 percentage points. | numeric claim only at cited anchor | p. 6 (V. EVALUATION) |

- Numeric sentences retained from the body:
- **p. 5 / V. EVALUATION - extractive PDF cue:** We pre-train the policy on a mix of 1000 demonstrations collected in our lab for tasks different from the five continual learning tasks and 2000 ...
- **p. 5 / V. EVALUATION - extractive PDF cue:** The policy generates chunks of H = 16 end-effector displacement actions, and the first h = 8 actions are sent to a Cartesian controller [41] ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** Backbone Expandable layers AUC ↑ FWT ↑ NBT ↓ DiT-Dec Linear projection 75.1±1.3 75.0±1.4 1.9±0.4 Decoder 41.8±2.4 45.5±3.8 7.0±1.7 DiT-EncDec Encoder 65.4±2.7 66.5±2.2 1.7±1.2 Decoder ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** 1 5 10 15 20 25 30 35 40 Task 1 5 10 15 20 25 30 35 40 Stage AUC = 83.6 FWT = ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** 4: CLARE scales to continual learning of 40 tasks on LIBERO-40, whereas experience replay (ER) exhibits significant performance degradation. layers and adaptive layer normalization (AdaLN) ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** Training takes about one hour per simulation task and five hours per real-world task on an NVIDIA RTX 5090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of 23%. | p. 6 (V. EVALUATION) |
| body limitation/failure cue | SeqFFT and SeqLoRA achieve high performance on new tasks, but cannot sufficiently retain the relevant representations from previous tasks. | p. 7 (5. LEGO) |
| body limitation/failure cue | 5: Increasing the dynamic expansion threshold γ reduces the number of added adapters and, consequently, the capability to learn new tasks (lower FWT), but ... | p. 7 (V. EVALUATION) |
| body limitation/failure cue | As shown in Figure 4, CLARE can sequentially learn and retain 40 distinct tasks, demonstrating the scalability and robustness of our autonomous routing strategy. | p. 6 (V. EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Real Sim. # Params (linear proj.) 0.38M 3.2M 6.08M 1.4M # Params (AdaLN) 0.75M 0.26M 1.00M 0.33M Learning rate 2 × 10-4 1 × ... | p. 5 (IV. METHODOLOGY) |
| For our pre-trained base VLA, we adopt a decoder-only diffusion transformer (DiT-Dec) [42] architecture with 6 transformer | p. 5 (V. EVALUATION) |
| We average all simulation results across three random seeds. | p. 6 (V. EVALUATION) |
| Due to computational constraints, we perform only 10 rollouts per task and stage across three seeds. | p. 6 (V. EVALUATION) |
| 1: for all discriminators Dj ℓ∈Dℓdo 2: Compute the reconstruction error ej ℓ(xℓ) via (4). | p. 3 (IV. METHODOLOGY) |
| We employ a lightweight encoder-decoder structure with ReLU activation functions for the adapters. | p. 3 (IV. METHODOLOGY) |
| We pair each layer with an expanding set of autoencoder discriminators Dℓ= {D1 ℓ, D2 ℓ, . . . }, all of which receive ... | p. 4 (IV. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. EVALUATION - extractive PDF cue:** In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of 23%.
- **p. 7 / 5. LEGO - extractive PDF cue:** SeqFFT and SeqLoRA achieve high performance on new tasks, but cannot sufficiently retain the relevant representations from previous tasks.
- **p. 7 / V. EVALUATION - extractive PDF cue:** 5: Increasing the dynamic expansion threshold γ reduces the number of added adapters and, consequently, the capability to learn new tasks (lower FWT), but does ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** As shown in Figure 4, CLARE can sequentially learn and retain 40 distinct tasks, demonstrating the scalability and robustness of our autonomous routing strategy.

- **PDF anchors reviewed:** datasets p. 5 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION), metrics p. 10 (Figure/Table caption), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 4 (Figure/Table caption), p. 5 (V. EVALUATION), p. 7 (V. EVALUATION), baselines p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 10 (Figure/Table caption), p. 7 (V. EVALUATION), p. 7 (V. EVALUATION), p. 1 (Figure/Table caption), results p. 10 (Figure/Table caption), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION), p. 5 (V. EVALUATION), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
