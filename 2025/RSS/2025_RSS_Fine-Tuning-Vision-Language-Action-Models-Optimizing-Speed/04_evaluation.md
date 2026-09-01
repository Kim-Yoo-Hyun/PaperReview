# Evaluation - Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p017.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p017.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup), p. 8 (C. ALOHA Task Performance Results), p. 9 (C. ALOHA Task Performance Results), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 8 (C. ALOHA Task Performance Results)): Finally, OpenVLA-OFT+ achieves the highest performance across both task execution and language following (see Figure 7 for examples of successful task rollouts).

## Evaluation Body Digest

- **p. 5 / A. LIBERO Experimental Setup - extractive body cue:** We evaluate on the LIBERO simulation benchmark [26], which features a Franka Emika Panda arm in simulation with demonstrations containing camera images, robot state, task ...
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** 1) ALOHA Task Suite Details: Below are detailed specitications for each task in our ALOHA experiments: 1. "fold shorts" «+ Task: Bimanual folding of white ...
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** datasets (6K episodes and 8K hours of bimanual data, respec tively). ‘This suggests that the fine-tuning technique can be more crucial than pretraining data coverage ...
- **p. 5 / A. LIBERO Experimental Setup - extractive body cue:** We use four task suites-LIBERO-Spatial, LIBERO-Object, LIBEROGoal, and LIBERO-Long-each providing 500 expert demonstrations across 10 tasks to assess policy generalization 10 lifferent spatial layouts, objects, ...
- **p. 8 / C. ALOHA Task Performance Results - extractive body cue:** However, it struggles with the "put X into pot" task which has a larger training dataset, suggesting limited scalability compared to VLA-based approaches.
- **p. 10 / C. ALOHA Task Performance Results - extractive body cue:** ach query processes thee 224 % 224 px images, 14D robot sate, and a task command ("coop raisins into bow").
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** 7: Sample successful OpenVLA-OFTS rollouts on the ALOHA robot.
- **p. 14 / B. Implementation Details - extractive body cue:** Low-dimensional robot states are also projected to the language embedding space through a 2-layer MLP with GELU activation

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** A. LIBERO Experimental Setup (p. 5); C. ALOHA Task Performance Results (p. 8); B. Implementation Details (p. 14); C. Feature-wise Linear Modulation (FILM) Implementation (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| C. ALOHA Task Performance Results | EMPIRICAL / SIMULATION | Finally, OpenVLA-OFT+ achieves the highest performance across both task execution and language following (see Figure 7 for examples of successful task rollouts). | p. 9 (C. ALOHA Task Performance Results) |
| A. LIBERO Experimental Setup | EMPIRICAL / SIMULATION | For methods using action chunking, we set chunk size to A' = 8 to match the Diffusion Policy baseline [5], and execute full chunks ... | p. 5 (A. LIBERO Experimental Setup) |
| C. ALOHA Task Performance Results | EMPIRICAL / SIMULATION | ACT, while able to complete basic tasks, produces less precise actions and achieves the lowest overall performance. | p. 8 (C. ALOHA Task Performance Results) |
| C. ALOHA Task Performance Results | EMPIRICAL / SIMULATION | Success rates in approaching for language-dependent tasks. | p. 9 (C. ALOHA Task Performance Results) |
| C. Feature-wise Linear Modulation (FILM) Implementation | EMPIRICAL / SIMULATION | DDINOv2 ['s] vision transformers in OpenVLA\s fuse vision backbone, The average tsk description embedling modules visual features throvgh sale and shift operations at each ... | p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |

## Dataset / Benchmark Role

- **p. 5 / A. LIBERO Experimental Setup - extractive body cue:** We evaluate on the LIBERO simulation benchmark [26], which features a Franka Emika Panda arm in simulation with demonstrations containing camera images, robot state, task ...
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** 1) ALOHA Task Suite Details: Below are detailed specitications for each task in our ALOHA experiments: 1. "fold shorts" «+ Task: Bimanual folding of white ...
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** datasets (6K episodes and 8K hours of bimanual data, respec tively). ‘This suggests that the fine-tuning technique can be more crucial than pretraining data coverage ...
- **p. 5 / A. LIBERO Experimental Setup - extractive body cue:** We use four task suites-LIBERO-Spatial, LIBERO-Object, LIBEROGoal, and LIBERO-Long-each providing 500 expert demonstrations across 10 tasks to assess policy generalization 10 lifferent spatial layouts, objects, ...
- **p. 8 / C. ALOHA Task Performance Results - extractive body cue:** However, it struggles with the "put X into pot" task which has a larger training dataset, suggesting limited scalability compared to VLA-based approaches.
- **p. 10 / C. ALOHA Task Performance Results - extractive body cue:** ach query processes thee 224 % 224 px images, 14D robot sate, and a task command ("coop raisins into bow").
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** 7: Sample successful OpenVLA-OFTS rollouts on the ALOHA robot.
- **p. 14 / B. Implementation Details - extractive body cue:** Low-dimensional robot states are also projected to the language embedding space through a 2-layer MLP with GELU activation

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: OpenVLA-OFT+ on the bimanual ALOHA robot. Our Optimized Fine-Tuning (OFT) recipe enhances fnesuned OpeaVLA pic and inpt-outptfeibliy. The resulting OpeaVLA-OFT+ policies execute diverse ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Key design decisions for VLA fine-tuning. Left: Comparison between autoregressive decoding, which generates ations sequcntilly, and parallel decoding, which leverages bidirectional stention and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: LIBERO simulation benchmark [26] task suites. We study VLA finening design decisions using four representative task suites. Here we ‘depict two often tasks ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: ALOWA task performance results. Comparison between policies tine from scratch (ACT, Diffusion Policy) and fine-tuned VLAs (RDF-IB, xo, ‘OpenVLA-OFT#) scoss four ALOHA manipulstion ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 6: Sample rollouts contrasting RDT-1B and zp error handling in ALOHA tasks. Top In some cases, RDT-IB fails 10 respond to missed howl placement, ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 8: Features nar modulation (FILM) implementation in OpenVL
- **p. 19 / Figure/Table caption - extractive body cue:** Fig. 9: Iniil states for "old shorts" task evaluations. We use the smallest variance in inital positions for this task due to the small numberof ...
- **p. 21 / Figure/Table caption - extractive body cue:** Fig. 12: Initial states for "put X into pot" task evaluations (in-distrbution version). Food object

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate on the LIBERO simulation benchmark [26], which features a Franka Emika Panda arm in simulation with demonstrations containing camera images, robot state, ... | embodiment, simulator version and control stack | p. 5 (A. LIBERO Experimental Setup), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| Task/environment | 1) ALOHA Task Suite Details: Below are detailed specitications for each task in our ALOHA experiments: 1. "fold shorts" «+ Task: Bimanual folding of ... | reset, timeout, object/scene variation | p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 9 (C. ALOHA Task Performance Results) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 7 (3) LI regression objective) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1. Iyrropucrion), p. 4 (B. Implementing Alternative Design Components) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Success rates in approaching for language-dependent tasks. | definition/direction/unit from same section | p. 9 (C. ALOHA Task Performance Results) |
| To provide fine-grained assessment, we use a predetermined rubric that assigns scores for partial task completion (see Appendix FF for details). | definition/direction/unit from same section | p. 8 (C. ALOHA Task Performance Results) |
| 6: Sample rollouts contrasting RDT-1B and zp error handling in ALOHA tasks. | definition/direction/unit from same section | p. 9 (C. ALOHA Task Performance Results) |
| [23], we filter unsuccessful demonstrations and fine-tune OpenVLA via LoRA [1+] on each task suite independently. | definition/direction/unit from same section | p. 5 (A. LIBERO Experimental Setup) |
| We test checkpoints every 50K steps and report the best performance for each run, Unless specified otherwise, policies receive one third-person image and language ... | definition/direction/unit from same section | p. 5 (A. LIBERO Experimental Setup) |
| The baseline methods trained from scratch show varying levels of success. | definition/direction/unit from same section | p. 8 (C. ALOHA Task Performance Results) |
| Bold and underlined values show best and second-best performance | definition/direction/unit from same section | p. 10 (C. ALOHA Task Performance Results) |
| ‘otably, OpenVLA-OFT+'s throughput (77.9 Hz) approaches RDT-1B's (84.1 Hz) despite being 7% larger, as it generates actions in a single forward pass rather than ... | definition/direction/unit from same section | p. 10 (C. ALOHA Task Performance Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fine-tuned VLA pol cies generally outperform the from-scratch baselines in both task execution and language following, consistent with prior findings (27, 3]. | comparison identity and matched condition | p. 8 (C. ALOHA Task Performance Results) |
| However, for broader comparison, we also include LIBERO results from prior state-of-the-art imitation learning methods, such as Diffusion Policy [5], Octo [49], DiT Policy ... | comparison identity and matched condition | p. 5 (A. LIBERO Experimental Setup) |
| Our primary baseline in this study is the base OpenVLA ‘model fine-tuned using the original fine-tuning recipe. | comparison identity and matched condition | p. 5 (A. LIBERO Experimental Setup) |
| The baseline methods trained from scratch show varying levels of success. | comparison identity and matched condition | p. 8 (C. ALOHA Task Performance Results) |
| While its language following slightly trails RDT1B's, mo achieves better overall task completion, making it the strongest baseline. | comparison identity and matched condition | p. 9 (C. ALOHA Task Performance Results) |
| In contrast, OpenVLA-OFT+ achieves 77.9 Hz throughput, though its latency is higher compared 10 the policies in the prior LIBERO experiments since it must ... | comparison identity and matched condition | p. 9 (C. ALOHA Task Performance Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Note that we do not use FILM for LIBERO ‘experiments since the fine-tuned policies without it already demonstrate good language grounding. | component/input/data sensitivity | p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| On the other hhand, with a continuous action representation, the VLA can directly model the action distribution without lossy discretization | component/input/data sensitivity | p. 14 (B. Implementation Details) |
| Note that Seer uses additional LIBERO90 pretraining data | component/input/data sensitivity | p. 5 (A. LIBERO Experimental Setup) |
| Our primary baseline in this study is the base OpenVLA ‘model fine-tuned using the original fine-tuning recipe. | component/input/data sensitivity | p. 5 (A. LIBERO Experimental Setup) |
| datasets (6K episodes and 8K hours of bimanual data, respec tively). ‘This suggests that the fine-tuning technique can be more crucial than pretraining data ... | component/input/data sensitivity | p. 9 (C. ALOHA Task Performance Results) |
| [37], we multiply F by (1 +7) instead of 7 since + and 9 are near zero at initialization. ‘This helps preserve the visual ... | component/input/data sensitivity | p. 14 (C. Feature-wise Linear Modulation (FILM) Implementation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In the next section, ‘we present a parallel generation scheme that enables efficient action chunking. | Finally, OpenVLA-OFT+ achieves the highest performance across both task execution and language following (see Figure 7 for examples of successful task rollouts). | PDF body cue; verify exact table/figure and matched conditions | p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup), p. 8 (C. ALOHA Task Performance Results), p. 9 (C. ALOHA Task Performance Results), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 8 (C. ALOHA Task Performance Results) |
| Primary metric/result | For methods using action chunking, we set chunk size to A' = 8 to match the Diffusion Policy baseline [5], and execute full chunks ... | numeric claim only at cited anchor | p. 5 (A. LIBERO Experimental Setup) |

- Numeric sentences retained from the body:
- **p. 5 / A. LIBERO Experimental Setup - extractive body cue:** We use four task suites-LIBERO-Spatial, LIBERO-Object, LIBEROGoal, and LIBERO-Long-each providing 500 expert demonstrations across 10 tasks to assess policy generalization 10 lifferent spatial layouts, objects, ...
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** The original OpenVLA formulation, even with just the additional wrist camera inputs, shows poor efficiency with 1.8 Hz throughput and 0.543 sec latency.
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** In contrast, OpenVLA-OFT+ achieves 77.9 Hz throughput, though its latency is higher compared 10 the policies in the prior LIBERO experiments since it must process ...
- **p. 10 / C. ALOHA Task Performance Results - extractive body cue:** ‘otably, OpenVLA-OFT+'s throughput (77.9 Hz) approaches RDT-1B's (84.1 Hz) despite being 7% larger, as it generates actions in a single forward pass rather than requiring ...
- **p. 14 / B. Implementation Details - extractive body cue:** LI regression: The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions.
- **p. 7 / 3) LI regression objective - extractive body cue:** Prior works [54, 27, 3] have shown that vanilla LoRA finetuning with autoregressive VLAs [23] is impractical for such tasks, as its throughput (3-5 Hz. ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often successfully recovering from initial failures (as ... | p. 9 (C. ALOHA Task Performance Results) |
| body limitation/failure cue | As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into | p. 8 (C. ALOHA Task Performance Results) |
| body limitation/failure cue | Among VLAs, we observe distinct charac teristics: RDT-IB achieves good language following through its "Alternating Condition Injection" scheme (27], but shows a limitation in ... | p. 8 (C. ALOHA Task Performance Results) |
| body limitation/failure cue | Top In some cases, RDT-IB fails 10 respond to missed howl placement, coatiauing 10 pour iagredieats into empey space. | p. 9 (C. ALOHA Task Performance Results) |
| body limitation/failure cue | We maintain the same convergence criterion as in the LIBERO experiments (training until mean normalized LI loss falls below 0.01) and similar learning rate ... | p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| body limitation/failure cue | While LI regression may help smoothen out noise in training demonstrations by encouraging the policy to learn the median mode in demonstrated actions, it ... | p. 10 (VII. Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We test checkpoints every 50K steps and report the best performance for each run, Unless specified otherwise, policies receive one third-person image and language ... | p. 5 (A. LIBERO Experimental Setup) |
| We fine-tune OpenVLA using OFT+ on each task independently for 50-150K gradient steps (total batch size 32 with 8 A100/H100-80GB GPUs) with action chunk ... | p. 8 (3) LI regression objective) |
| for non-diffusion methods and 100-250K steps for diffusion methods (which converge slower), using a batch size of 64-128 across 8 A100/H100 GPUs. | p. 5 (A. LIBERO Experimental Setup) |
| We maintain the same convergence criterion as in the LIBERO experiments (training until mean normalized LI loss falls below 0.01) and similar learning rate ... | p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| We evaluate checkpoints every SOK steps, with the 150K ‘checkpoint achieving best performance in all task suites except for LIBERO-Goal. | p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| In our implementation, following Perez et al. | p. 14 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| + DDIM [46] sampler with 50 diffusion timesteps | p. 14 (B. Implementation Details) |
| ‘otably, OpenVLA-OFT+'s throughput (77.9 Hz) approaches RDT-1B's (84.1 Hz) despite being 7% larger, as it generates actions in a single forward pass rather than ... | p. 10 (C. ALOHA Task Performance Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often successfully recovering from initial failures (as shown ...
- **p. 8 / C. ALOHA Task Performance Results - extractive body cue:** As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into
- **p. 8 / C. ALOHA Task Performance Results - extractive body cue:** Among VLAs, we observe distinct charac teristics: RDT-IB achieves good language following through its "Alternating Condition Injection" scheme (27], but shows a limitation in handling ...
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** Top In some cases, RDT-IB fails 10 respond to missed howl placement, coatiauing 10 pour iagredieats into empey space.
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** We maintain the same convergence criterion as in the LIBERO experiments (training until mean normalized LI loss falls below 0.01) and similar learning rate decay ...
- **p. 10 / VII. Discussion - extractive body cue:** While LI regression may help smoothen out noise in training demonstrations by encouraging the policy to learn the median mode in demonstrated actions, it may ...

- **PDF anchors reviewed:** datasets p. 5 (A. LIBERO Experimental Setup), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup), p. 8 (C. ALOHA Task Performance Results), p. 10 (C. ALOHA Task Performance Results), metrics p. 9 (C. ALOHA Task Performance Results), p. 8 (C. ALOHA Task Performance Results), p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup), p. 5 (A. LIBERO Experimental Setup), p. 8 (C. ALOHA Task Performance Results), baselines p. 8 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup), p. 5 (A. LIBERO Experimental Setup), p. 8 (C. ALOHA Task Performance Results), p. 9 (C. ALOHA Task Performance Results), p. 9 (C. ALOHA Task Performance Results), results p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup), p. 8 (C. ALOHA Task Performance Results), p. 9 (C. ALOHA Task Performance Results), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 8 (C. ALOHA Task Performance Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
