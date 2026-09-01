# Evaluation - ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=72UR53jN7T; PDF retrieval source: https://openreview.net/pdf/b35b0fc70612e191baced400f754db8ff1fae711.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4 Experiment), p. 9 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment)): On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA [54], verifying the effectiveness on diverse manipulation settings.

## Evaluation Body Digest

- **p. 7 / 4 Experiment - extractive PDF cue:** Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the book and place ...
- **p. 6 / 4 Experiment - extractive PDF cue:** Training Datasets and Evaluation Benchmarks For SFT cold-start, we fine-tune the MLLM using trajectories from the subset of OXE, and QA tasks from RoboVQA [38], ...
- **p. 6 / 4 Experiment - extractive PDF cue:** We evaluate ThinkAct on two robot manipulation and three embodied reasoning benchmarks.
- **p. 8 / 4 Experiment - extractive PDF cue:** We focus on two key aspects: (1) how reasoning facilitates effective few-shot adaptation to new tasks and environments, and (2) how it enables the robot ...
- **p. 7 / 4 Experiment - extractive PDF cue:** Dataset Split / Metric GPT-4V [1] LLaVAVideo [17] InternVL2.5 [8] InternVL3 [56] NVILA [27] Qwen2.5-VL [2] Qwen2.5-VL* [2] Magma [48] ThinkAct (Ours) EgoPlanBench2 Daily life ...
- **p. 8 / 4 Experiment - extractive PDF cue:** That seems clear now.</think> <answer>The carpet on the floor is rectangular.</answer> (a) RoboVQA (b) OpenEQA ThinkAct w/o RL ThinkAct ThinkAct Figure 4: Qualitative comparison of ...
- **p. 9 / 4 Experiment - extractive PDF cue:** First, the robot needs to move the mug closer to the microwave ...
- **p. 9 / 4 Experiment - extractive PDF cue:** This requires the robot to move the mug up and into the microwave, which seems to be the next logical step.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiment (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA [54], verifying the effectiveness on ... | p. 6 (4 Experiment) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | Method SimplerEnv EgoPlan RoboVQA ThinkAct (Ours) 60.1 48.2 59.8 Ours w/o rtraj 59.2 47.9 58.5 Ours w/o rgoal 59.1 47.6 58.9 Ours w/o rtraj, ... | p. 9 (4 Experiment) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, on the SimplerEnv, incorporating our reasoning-guided visual plan latents allows ThinkAct to outperform our baseline action model, DiT-Policy, by 15.5%, 16.9%, and 11.4% ... | p. 6 (4 Experiment) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | ThinkAct outperforms the second-best method by 2.5% and 4.1 BLEU score on these two benchmarks, demonstrating its strength in long-horizon and multi-step planning. | p. 7 (4 Experiment) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | We start from the full version of ThinkAct, which achieves the best performance across all benchmarks. | p. 8 (4 Experiment) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiment - extractive PDF cue:** Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the book and place ...
- **p. 6 / 4 Experiment - extractive PDF cue:** Training Datasets and Evaluation Benchmarks For SFT cold-start, we fine-tune the MLLM using trajectories from the subset of OXE, and QA tasks from RoboVQA [38], ...
- **p. 6 / 4 Experiment - extractive PDF cue:** We evaluate ThinkAct on two robot manipulation and three embodied reasoning benchmarks.
- **p. 8 / 4 Experiment - extractive PDF cue:** We focus on two key aspects: (1) how reasoning facilitates effective few-shot adaptation to new tasks and environments, and (2) how it enables the robot ...
- **p. 7 / 4 Experiment - extractive PDF cue:** Dataset Split / Metric GPT-4V [1] LLaVAVideo [17] InternVL2.5 [8] InternVL3 [56] NVILA [27] Qwen2.5-VL [2] Qwen2.5-VL* [2] Magma [48] ThinkAct (Ours) EgoPlanBench2 Daily life ...
- **p. 8 / 4 Experiment - extractive PDF cue:** That seems clear now.</think> <answer>The carpet on the floor is rectangular.</answer> (a) RoboVQA (b) OpenEQA ThinkAct w/o RL ThinkAct ThinkAct Figure 4: Qualitative comparison of ...
- **p. 9 / 4 Experiment - extractive PDF cue:** First, the robot needs to move the mug closer to the microwave ...
- **p. 9 / 4 Experiment - extractive PDF cue:** This requires the robot to move the mug up and into the microwave, which seems to be the next logical step.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: We introduce ThinkAct, a reasoning VLA framework capable of thinking before acting. Through reasoning reinforced by our action-aligned visual feedback, ThinkAct enables capabilities ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of our ThinkAct. (a) Given observation ot and instruction l, ThinkAct advances action-aligned rewards derived from visual trajectory τ to incentivize embodied ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative comparisons of robot manipulation tasks on SimplerEnv [20] and LIBERO [24] benchmarks. Bold denotes the best result.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative comparisons of embodied reasoning tasks on EgoPlan-Bench2, RoboVQA, and OpenEQA benchmarks. Note that, Qwen2.5-VL* indicates fine-tuning the original Qwen2.5-VL using EgoPlan-IT [7] ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Qualitative results of intermediate reasoning steps and visualized trajectory for robot manipulation tasks on SimplerEnv and LIBERO benchmarks. Embodied Reasoning In Tab. 2, ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Qualitative comparison of reasoning process and the derived answer for our ThinkAct with and without RL for embodied reasoning tasks on RoboVQA and ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative ablation study for our proposed RL rewards in ThinkAct on SimplerEnv, EgoPlan- Bench2, and RoboVQA benchmarks.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Few-shot adaptation results on LIBERO. We use 10 demonstrations per task for fine-tuning. Fail to pick up target object!! Replan & Execute Struggle ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the book and ... | embodiment, simulator version and control stack | p. 7 (4 Experiment), p. 6 (4 Experiment) |
| Task/environment | Training Datasets and Evaluation Benchmarks For SFT cold-start, we fine-tune the MLLM using trajectories from the subset of OXE, and QA tasks from RoboVQA ... | reset, timeout, object/scene variation | p. 6 (4 Experiment), p. 6 (4 Experiment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 3 (3 Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3 Method), p. 5 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For reasoning benchmarks, EgoPlan-Bench2 [35] uses accuracy on multiple-choice questions, while RoboVQA [38] and OpenEQA [29] are free-form QA tasks evaluated using BLEU score ... | definition/direction/unit from same section | p. 6 (4 Experiment) |
| For manipulation tasks, SimplerEnv [20] containing diverse scenes and LIBERO [24] with long-horizon tasks are evaluated using task success rate. | definition/direction/unit from same section | p. 6 (4 Experiment) |
| Method SimplerEnv EgoPlan RoboVQA ThinkAct (Ours) 60.1 48.2 59.8 Ours w/o rtraj 59.2 47.9 58.5 Ours w/o rgoal 59.1 47.6 58.9 Ours w/o rtraj, ... | definition/direction/unit from same section | p. 9 (4 Experiment) |
| ThinkAct outperforms the second-best method by 2.5% and 4.1 BLEU score on these two benchmarks, demonstrating its strength in long-horizon and multi-step planning. | definition/direction/unit from same section | p. 7 (4 Experiment) |
| Without the goal reward, performance also declines, suggesting that rgoal plays a key role in incentivizing long-horizon reasoning. | definition/direction/unit from same section | p. 8 (4 Experiment) |
| Figure 1: We introduce ThinkAct, a reasoning VLA framework capable of thinking before acting. Through reasoning reinforced by our action-aligned visual feedback, ThinkAct enables ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| 3, we ablate the proposed goal reward rgoal and trajectory reward rtraj to analyze their individual contributions to reasoning and planning. | definition/direction/unit from same section | p. 8 (4 Experiment) |
| Figure 2: Overview of our ThinkAct. (a) Given observation ot and instruction l, ThinkAct advances action-aligned rewards derived from visual trajectory τ to incentivize ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA [54], verifying the effectiveness on ... | comparison identity and matched condition | p. 6 (4 Experiment) |
| 1, on the SimplerEnv, incorporating our reasoning-guided visual plan latents allows ThinkAct to outperform our baseline action model, DiT-Policy, by 15.5%, 16.9%, and 11.4% ... | comparison identity and matched condition | p. 6 (4 Experiment) |
| ThinkAct outperforms the second-best method by 2.5% and 4.1 BLEU score on these two benchmarks, demonstrating its strength in long-horizon and multi-step planning. | comparison identity and matched condition | p. 7 (4 Experiment) |
| When both rtraj and rgoal are removed, leaving only QA-style reward from QA datasets, the model shows only marginal improvements over the SFT baseline, ... | comparison identity and matched condition | p. 8 (4 Experiment) |
| That seems clear now.</think> <answer>The carpet on the floor is rectangular.</answer> (a) RoboVQA (b) OpenEQA ThinkAct w/o RL ThinkAct ThinkAct Figure 4: Qualitative comparison ... | comparison identity and matched condition | p. 8 (4 Experiment) |
| Table 2: Quantitative comparisons of embodied reasoning tasks on EgoPlan-Bench2, RoboVQA, and OpenEQA benchmarks. Note that, Qwen2.5-VL* indicates fine-tuning the original Qwen2.5-VL using EgoPlan-IT ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Finally, the SFT cold-start model without RL yields the lowest scores, verifying the effectiveness of our RL fine-tuning for eliciting the reasoning capability in ... | component/input/data sensitivity | p. 8 (4 Experiment) |
| When both rtraj and rgoal are removed, leaving only QA-style reward from QA datasets, the model shows only marginal improvements over the SFT baseline, ... | component/input/data sensitivity | p. 8 (4 Experiment) |
| SimplerEnv [20] includes Google-VM (Visual Matching), Google-VA (Variant Aggregation), and Bridge-VM setups, introducing variations in color, material, lighting, and camera pose to evaluate model ... | component/input/data sensitivity | p. 6 (4 Experiment) |
| Table 3: Quantitative ablation study for our proposed RL rewards in ThinkAct on SimplerEnv, EgoPlan- Bench2, and RoboVQA benchmarks. | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| LIBERO [24] tasks are further fine-tuned for 75K iterations with batch size 128. | component/input/data sensitivity | p. 6 (4 Experiment) |
| Note that, Qwen2.5-VL* indicates fine-tuning the original Qwen2.5-VL using EgoPlan-IT [7] and RoboVQA [38] datasets. | component/input/data sensitivity | p. 7 (4 Experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visual-grounded embodied reasoning connected ... | On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA [54], verifying the effectiveness on ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4 Experiment), p. 9 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment) |
| Primary metric/result | Method SimplerEnv EgoPlan RoboVQA ThinkAct (Ours) 60.1 48.2 59.8 Ours w/o rtraj 59.2 47.9 58.5 Ours w/o rgoal 59.1 47.6 58.9 Ours w/o rtraj, ... | numeric claim only at cited anchor | p. 9 (4 Experiment) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Through extensive experiments across embodied reasoning and robot manipulation benchmarks, we demonstrated strong long-horizon planning, few-shot adaptation, and emergent behaviors such as failure detection ... | p. 10 (5 Conclusion) |
| body limitation/failure cue | Limitations Since ThinkAct builds on pretrained multimodal LLMs, it inevitably inherits their limitations, particularly hallucinations in visual or spatial reasoning. | p. 10 (5 Conclusion) |
| body limitation/failure cue | We focus on two key aspects: (1) how reasoning facilitates effective few-shot adaptation to new tasks and environments, and (2) how it enables the ... | p. 8 (4 Experiment) |
| body limitation/failure cue | Figure 6: Demonstration of self-reflection and correction capability of ThinkAct. The reasoning MLLM identifies the failure and generates a revised plan that recovers from ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | 4(a), using a RoboVQA [38] example, the SFT cold-start model focuses only on the current state and fails to reason over future steps, while ... | p. 8 (4 Experiment) |
| body limitation/failure cue | SimplerEnv [20] includes Google-VM (Visual Matching), Google-VA (Variant Aggregation), and Bridge-VM setups, introducing variations in color, material, lighting, and camera pose to evaluate model ... | p. 6 (4 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The cold-start stage runs for 20K iterations with batch size 32 and learning rate 1e-5 using DeepSpeed ZeRO-3. | p. 5 (4 Experiment) |
| For reasoning-enhanced action adaptation, we connect the visual plan ct via a Q-Former [18] as the latent projector with 32 queries and fine-tune on ... | p. 6 (4 Experiment) |
| LIBERO [24] tasks are further fine-tuned for 75K iterations with batch size 128. | p. 6 (4 Experiment) |
| 4.1 Experimental Setup Implementation Details We initialize Fθ with Qwen2.5-VL 7B [2]. | p. 5 (4 Experiment) |
| Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the book and ... | p. 7 (4 Experiment) |
| 4(a), using a RoboVQA [38] example, the SFT cold-start model focuses only on the current state and fails to reason over future steps, while ... | p. 8 (4 Experiment) |
| Based on this reasoning, the next steps are: | p. 9 (4 Experiment) |
| Reward acts at every step (a) (b) Latent Projector State Encoder reasons every N steps Figure 2: Overview of our ThinkAct. | p. 4 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 Conclusion - extractive PDF cue:** Through extensive experiments across embodied reasoning and robot manipulation benchmarks, we demonstrated strong long-horizon planning, few-shot adaptation, and emergent behaviors such as failure detection and ...
- **p. 10 / 5 Conclusion - extractive PDF cue:** Limitations Since ThinkAct builds on pretrained multimodal LLMs, it inevitably inherits their limitations, particularly hallucinations in visual or spatial reasoning.
- **p. 8 / 4 Experiment - extractive PDF cue:** We focus on two key aspects: (1) how reasoning facilitates effective few-shot adaptation to new tasks and environments, and (2) how it enables the robot ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: Demonstration of self-reflection and correction capability of ThinkAct. The reasoning MLLM identifies the failure and generates a revised plan that recovers from execution ...
- **p. 8 / 4 Experiment - extractive PDF cue:** 4(a), using a RoboVQA [38] example, the SFT cold-start model focuses only on the current state and fails to reason over future steps, while the ...
- **p. 6 / 4 Experiment - extractive PDF cue:** SimplerEnv [20] includes Google-VM (Visual Matching), Google-VA (Variant Aggregation), and Bridge-VM setups, introducing variations in color, material, lighting, and camera pose to evaluate model robustness.

- **PDF anchors reviewed:** datasets p. 7 (4 Experiment), p. 6 (4 Experiment), p. 6 (4 Experiment), p. 8 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), metrics p. 6 (4 Experiment), p. 6 (4 Experiment), p. 9 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 2 (Figure/Table caption), baselines p. 6 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment), p. 7 (Figure/Table caption), results p. 6 (4 Experiment), p. 9 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
