# Evaluation - VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 7 (Figure/Table caption), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 8 (4.3.2. Embedding Integration Effectiveness)): The evaluation results of residual VQ-VAE architectures.The results demonstrate that the Conv Residual VQ-VAE outperforms the MLP-based version, particularly when trained on the full LIBERO dataset (ALL-LIBERO), highlighting its ability ...

## Evaluation Body Digest

- **p. 6 / 4.2.1. Experiment Setup - extractive body cue:** In simulation, evaluations are performed on the LIBERO90 benchmark within the LIBERO dataset.
- **p. 4 / 4.1.1. Experiment Setup - extractive body cue:** We utilize the LIBERO benchmark[29] to validate and evaluate the effectiveness and scalability of the action tokenizer, using the Franka Panda robot.
- **p. 7 / 4.2.4. Sim&Real Domain Gap Analysis - extractive body cue:** Although real-world data may contain noise, the inclusion of Open X-Embodiment data as a real-world dataset expands the data sources and enriches the diversity of ...
- **p. 4 / 4.1.1. Experiment Setup - extractive body cue:** Specifically, the entire LIBERO task suite-including LIBERO-Spatial, LIBEROObject, LIBERO-Goal, LIBERO-10, and LIBERO-90-is used as the entire LIBERO dataset.
- **p. 5 / 4.2.1. Experiment Setup - extractive body cue:** For each task, we collect 50 demonstrations and evaluate performance over 20 trials: 1) Pull out a tissue paper: The robot need to grasp and ...
- **p. 6 / 4.2.1. Experiment Setup - extractive body cue:** All Evaluation environments:We conduct comprehensive evaluations of VQ-VLA in both simulation and real-world settings.
- **p. 5 / 4.2.1. Experiment Setup - extractive body cue:** Our experimental benchmark comprises six manipulation tasks (4 short-horizon tasks, 2 long-horizon tasks) designed to evaluate the model's ability to handle varying task complexities.
- **p. 7 / 4.2.4. Sim&Real Domain Gap Analysis - extractive body cue:** The model was tested in three real-world tasks (one long-horizon and two short-horizon tasks), and the results are shown in Tab.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 4); 4.1. Simulation Experiments (p. 4); 4.1.1. Experiment Setup (p. 4); 4.2. Real-Word Experiment (p. 5); 4.2.1. Experiment Setup (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1.2. Effectiveness of Conv Residual VQ-VAE | EMPIRICAL / REAL-ROBOT OR HARDWARE | The evaluation results of residual VQ-VAE architectures.The results demonstrate that the Conv Residual VQ-VAE outperforms the MLP-based version, particularly when trained on the full ... | p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Real-world experimental results: We compare the performance of Baseline, VQO, VQO+L, and VQO+L+M on both short-horizon and long-horizon tasks. In terms of ... | p. 7 (Figure/Table caption) |
| 4.2.3. Performance on Long-Horizon Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | VQ-VLA demonstrates outstanding performance on longhorizon tasks ("Put all cups in the basket" and "Put the toy into the drawer"), significantly outperforming baseline model ... | p. 6 (4.2.3. Performance on Long-Horizon Tasks) |
| 4.1.2. Effectiveness of Conv Residual VQ-VAE | EMPIRICAL / REAL-ROBOT OR HARDWARE | The findings indicate that using temporal convolutional networks as the encoder and decoder in the Residual VQ-VAE significantly outperforms the MLP-based architecture in terms ... | p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE) |
| 4.2.3. Performance on Long-Horizon Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | In scenarios where baseline models achieve success rates as low as 15% or nearly 0, the VQO+L+M model achieves significantly higher success rates of ... | p. 6 (4.2.3. Performance on Long-Horizon Tasks) |

## Dataset / Benchmark Role

- **p. 6 / 4.2.1. Experiment Setup - extractive body cue:** In simulation, evaluations are performed on the LIBERO90 benchmark within the LIBERO dataset.
- **p. 4 / 4.1.1. Experiment Setup - extractive body cue:** We utilize the LIBERO benchmark[29] to validate and evaluate the effectiveness and scalability of the action tokenizer, using the Franka Panda robot.
- **p. 7 / 4.2.4. Sim&Real Domain Gap Analysis - extractive body cue:** Although real-world data may contain noise, the inclusion of Open X-Embodiment data as a real-world dataset expands the data sources and enriches the diversity of ...
- **p. 4 / 4.1.1. Experiment Setup - extractive body cue:** Specifically, the entire LIBERO task suite-including LIBERO-Spatial, LIBEROObject, LIBERO-Goal, LIBERO-10, and LIBERO-90-is used as the entire LIBERO dataset.
- **p. 5 / 4.2.1. Experiment Setup - extractive body cue:** For each task, we collect 50 demonstrations and evaluate performance over 20 trials: 1) Pull out a tissue paper: The robot need to grasp and ...
- **p. 6 / 4.2.1. Experiment Setup - extractive body cue:** All Evaluation environments:We conduct comprehensive evaluations of VQ-VLA in both simulation and real-world settings.
- **p. 5 / 4.2.1. Experiment Setup - extractive body cue:** Our experimental benchmark comprises six manipulation tasks (4 short-horizon tasks, 2 long-horizon tasks) designed to evaluate the model's ability to handle varying task complexities.
- **p. 7 / 4.2.4. Sim&Real Domain Gap Analysis - extractive body cue:** The model was tested in three real-world tasks (one long-horizon and two short-horizon tasks), and the results are shown in Tab.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. The VQ-VLA pipeline, consisting of two main stages: (1) training a general convolutional residual VQ-VAE and (2) fine-tuning OpenVLA using the LoRA approach. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. The evaluation results of residual VQ-VAE architec- tures.The results demonstrate that the Conv Residual VQ-VAE outperforms the MLP-based version, particularly when trained on ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Effectiveness of VQ-VAE Action Tokenizers in Scaling Simulation Data.The results demonstrate VQM+R reached 80.98%, outperforming the OpenVLA baseline by 7.45%
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2. All Evaluation environments:We conduct comprehen- sive evaluations of VQ-VLA in both simulation and real-world settings. In simulation, evaluations are performed on the LIBERO- ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Real-world experimental results: We compare the performance of Baseline, VQO, VQO+L, and VQO+L+M on both short-horizon and long-horizon tasks. In terms of the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Tab. 3. The results indicate that the performance of VQL is comparable to that of both VQO+L and VQO, suggesting that the domain gap between ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Performance Comparison Across Real-World Tasks: We observe that the performance of VQL is comparable to that of both VQO+L and VQO, indicating that ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. The Results of Frequencies. We report the comparison results of our VQ-VLA and baseline OpenVLA.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In simulation, evaluations are performed on the LIBERO90 benchmark within the LIBERO dataset. | embodiment, simulator version and control stack | p. 6 (4.2.1. Experiment Setup), p. 4 (4.1.1. Experiment Setup) |
| Task/environment | We utilize the LIBERO benchmark[29] to validate and evaluate the effectiveness and scalability of the action tokenizer, using the Franka Panda robot. | reset, timeout, object/scene variation | p. 4 (4.1.1. Experiment Setup), p. 7 (4.2.4. Sim&Real Domain Gap Analysis) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (3. Methods), p. 3 (3. Methods) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.3. Training Residual VQ-VAE), p. 3 (3.2. Action Tokenizer via Residual VQ-VAE) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In the "Pull out a tissue paper" task, which tests the robot's performance in high-precision dynamic operations (as this task requires continuous, fine-grained grasping ... | definition/direction/unit from same section | p. 6 (4.2.2. Performance on Short-Horizon Tasks) |
| Additionally, in scenarios involving the consecutive execution of multiple subtasks, VQ-VLA not only achieves higher success rates but also significantly reduces task completion time ... | definition/direction/unit from same section | p. 6 (4.2.3. Performance on Long-Horizon Tasks) |
| The findings indicate that using temporal convolutional networks as the encoder and decoder in the Residual VQ-VAE significantly outperforms the MLP-based architecture in terms ... | definition/direction/unit from same section | p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE) |
| Furthermore, when we increased the training data for the VQ-VAE model, transitioning from data solely derived from individual LIBERO tasks to the entire LIBERO ... | definition/direction/unit from same section | p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE) |
| In terms of the average success rate, all VQ-based models outperform the Baseline. | definition/direction/unit from same section | p. 7 (4.2.3. Performance on Long-Horizon Tasks) |
| The best-performing model, VQO+L+M, achieves a success rate that is 23.25% higher than the Baseline on both short-horizon and long-horizon tasks. | definition/direction/unit from same section | p. 7 (4.2.3. Performance on Long-Horizon Tasks) |
| 6, the model with embeddings significantly outperforms the baseline in terms of success rate. | definition/direction/unit from same section | p. 8 (4.3.2. Embedding Integration Effectiveness) |
| The table compares models with and without embeddings across three tasks, showing that embeddings enhance success rates, especially for "Flip the pot upright." | definition/direction/unit from same section | p. 8 (4.3.2. Embedding Integration Effectiveness) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Additionally, the results show that VQO+L+M outperforms VQO+L, which in turn outperforms VQO, indicating the effectiveness of incorporating synthetic data during training without compromising ... | comparison identity and matched condition | p. 7 (4.2.3. Performance on Long-Horizon Tasks) |
| Effectiveness of VQ-VAE Action Tokenizers in Scaling Simulation Data.The results demonstrate VQM+R reached 80.98%, outperforming the OpenVLA baseline by 7.45% | comparison identity and matched condition | p. 5 (4.1.3. Scaling Data Improves VQ-VAE Action Tokenizer) |
| VQ-VLA demonstrates outstanding performance on longhorizon tasks ("Put all cups in the basket" and "Put the toy into the drawer"), significantly outperforming baseline model ... | comparison identity and matched condition | p. 6 (4.2.3. Performance on Long-Horizon Tasks) |
| In terms of the average success rate, all VQ-based models outperform the Baseline. | comparison identity and matched condition | p. 7 (4.2.3. Performance on Long-Horizon Tasks) |
| 6, the model with embeddings significantly outperforms the baseline in terms of success rate. | comparison identity and matched condition | p. 8 (4.3.2. Embedding Integration Effectiveness) |
| 5, indicate that the use of the autoregressive approach for action chunking in the original OpenVLA leads to a significant drop in success rate ... | comparison identity and matched condition | p. 8 (4.3.1. Action Chunking via VQ-VAE and Autoregressive) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To evaluate the impact of embeddings, we conducted an ablation study comparing the model's performance with and without embeddings. | component/input/data sensitivity | p. 8 (4.3.2. Embedding Integration Effectiveness) |
| In this section, we report some ablation studies to show the effectiveness of the design choices of our method. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |
| Additionally, the results show that VQO+L+M outperforms VQO+L, which in turn outperforms VQO, indicating the effectiveness of incorporating synthetic data during training without compromising ... | component/input/data sensitivity | p. 7 (4.2.3. Performance on Long-Horizon Tasks) |
| To evaluate the effectiveness of different action chunking strategies, we design ablation experiments comparing the autoregressive output of OpenVLA to the VQ-based action chunking ... | component/input/data sensitivity | p. 8 (4.3.1. Action Chunking via VQ-VAE and Autoregressive) |
| We also investigate the impact of action tokenizers on the performance, inference speed, and long-horizon capabilities of VLA models, alongside ablation studies to evaluate ... | component/input/data sensitivity | p. 4 (4. Experiments) |
| Specifically, we used two variants of Residual VQ-VAE models: one with a simple MLP as the encoder and decoder, and the other with a ... | component/input/data sensitivity | p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action ... | The evaluation results of residual VQ-VAE architectures.The results demonstrate that the Conv Residual VQ-VAE outperforms the MLP-based version, particularly when trained on the full ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 7 (Figure/Table caption), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 8 (4.3.2. Embedding Integration Effectiveness) |
| Primary metric/result | Figure 3. Real-world experimental results: We compare the performance of Baseline, VQO, VQO+L, and VQO+L+M on both short-horizon and long-horizon tasks. In terms of ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / 4.1.1. Experiment Setup - extractive body cue:** Among these, LIBERO90 comprises 90 short-horizon tasks, while the other task suites each contain 10 tasks, with 50 demonstrations per task.
- **p. 5 / 4.1.1. Experiment Setup - extractive body cue:** Additionally, we fine-tune the original OpenVLA model on the LIBERO-90 dataset using LoRA as a baseline for comparison.For a fair comparison, all fine-tuning on the ...
- **p. 5 / 4.2.1. Experiment Setup - extractive body cue:** The system operates at 20 Hz (moderately reduced from the native 100 Hz control frequency to balance training efficiency and motion continuity), with actions defined ...
- **p. 5 / 4.2.1. Experiment Setup - extractive body cue:** For each task, we collect 50 demonstrations and evaluate performance over 20 trials: 1) Pull out a tissue paper: The robot need to grasp and ...
- **p. 6 / 4.2.3. Performance on Long-Horizon Tasks - extractive body cue:** For the "Put the toy into the drawer" task, a representative longhorizon scenario, the baseline model was only able to complete the first step of ...
- **p. 3 / 3. Methods - extractive body cue:** LLM's vocabulary, OpenVLA overwrites the 256 least-used tokens in the Llama tokenizer (last 256 tokens) rather than using special tokens, as the original tokenizer only ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite these promising results, there still remain some limitations and opportunities for future work. | p. 8 (5. Limitations and Future Works) |
| body limitation/failure cue | 4) Flip the pot upright: We set a flipped pot on the platform, the robot need to flip and upright a fallen cooking pot. | p. 6 (4.2.1. Experiment Setup) |
| body limitation/failure cue | Although real-world data may contain noise, the inclusion of Open X-Embodiment data as a real-world dataset expands the data sources and enriches the diversity ... | p. 7 (4.2.4. Sim&Real Domain Gap Analysis) |
| body limitation/failure cue | In contrast, the VQO+L+M model successfully opened the drawer in all test cases, demonstrating its robustness and reliability in handling complex sequential tasks. | p. 6 (4.2.3. Performance on Long-Horizon Tasks) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Both models are trained on a single A100 GPU with a batch size of 1024, which takes about only 1 week. | p. 5 (4.1.1. Experiment Setup) |
| Additionally, we fine-tune the original OpenVLA model on the LIBERO-90 dataset using LoRA as a baseline for comparison.For a fair comparison, all fine-tuning on ... | p. 5 (4.1.1. Experiment Setup) |
| We finetune each task separately for 100K gradient steps (batch size 4 across 4 A100-80GB GPUs) with action chunk length K=5. | p. 6 (4.2.1. Experiment Setup) |
| To improve the encoder's ability to process temporal and spatial information, we introduced two types of embeddings before the action sequences are passed into ... | p. 3 (3.3. Training Residual VQ-VAE) |
| For example, training on the Open X-Embodiment dataset requires just one A100 GPU and is completed in one week. | p. 4 (3.3. Training Residual VQ-VAE) |
| The use of these embeddings enhances the encoder's ability to process structured data, improving the quality of the latent representations and the overall performance ... | p. 4 (3.3. Training Residual VQ-VAE) |
| For the "Put the toy into the drawer" task, a representative longhorizon scenario, the baseline model was only able to complete the first step ... | p. 6 (4.2.3. Performance on Long-Horizon Tasks) |
| This demonstrates that the integration of embeddings improves the encoder's ability to represent structured action sequences, leading to better overall performance. | p. 8 (4.3.2. Embedding Integration Effectiveness) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Limitations and Future Works - extractive body cue:** Despite these promising results, there still remain some limitations and opportunities for future work.
- **p. 6 / 4.2.1. Experiment Setup - extractive body cue:** 4) Flip the pot upright: We set a flipped pot on the platform, the robot need to flip and upright a fallen cooking pot.
- **p. 7 / 4.2.4. Sim&Real Domain Gap Analysis - extractive body cue:** Although real-world data may contain noise, the inclusion of Open X-Embodiment data as a real-world dataset expands the data sources and enriches the diversity of ...
- **p. 6 / 4.2.3. Performance on Long-Horizon Tasks - extractive body cue:** In contrast, the VQO+L+M model successfully opened the drawer in all test cases, demonstrating its robustness and reliability in handling complex sequential tasks.

- **Evidence anchors reviewed:** datasets p. 6 (4.2.1. Experiment Setup), p. 4 (4.1.1. Experiment Setup), p. 7 (4.2.4. Sim&Real Domain Gap Analysis), p. 4 (4.1.1. Experiment Setup), p. 5 (4.2.1. Experiment Setup), p. 6 (4.2.1. Experiment Setup), metrics p. 6 (4.2.2. Performance on Short-Horizon Tasks), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 7 (4.2.3. Performance on Long-Horizon Tasks), p. 7 (4.2.3. Performance on Long-Horizon Tasks), baselines p. 7 (4.2.3. Performance on Long-Horizon Tasks), p. 5 (4.1.3. Scaling Data Improves VQ-VAE Action Tokenizer), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 7 (4.2.3. Performance on Long-Horizon Tasks), p. 8 (4.3.2. Embedding Integration Effectiveness), p. 8 (4.3.1. Action Chunking via VQ-VAE and Autoregressive), results p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 7 (Figure/Table caption), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 8 (4.3.2. Embedding Integration Effectiveness).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
