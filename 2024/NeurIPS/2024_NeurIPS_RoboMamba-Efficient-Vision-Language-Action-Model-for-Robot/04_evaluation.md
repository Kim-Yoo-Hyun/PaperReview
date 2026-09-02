# Evaluation - RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiment), p. 9 (4 Experiment), p. 8 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment)): As shown in Table 2, our RoboMamba achieves a 7.0% improvement on seen tasks and a 2.0% improvement on unseen tasks compared to the previous SOTA ManipLLM.

## Evaluation Body Digest

- **p. 7 / 4 Experiment - extractive body cue:** Datasets (Stage 2) For the dataset used in the robot manipulation fine-tuning stage, we follow the data collection process of previous works [61, 15], adopting ...
- **p. 7 / 4 Experiment - extractive body cue:** Notably, we also directly evaluate RoboMamba's robotic-related reasoning abilities on the 18k validation dataset of RoboVQA, covering robotic tasks such as long-horizon planning, success classification, ...
- **p. 8 / 4 Experiment - extractive body cue:** To comprehensively compare RoboMamba's robotic-related reasoning abilities, we benchmark it against LLaMA-AdapterV2 [45] and TinyLLaVA [83] on the RoboVQA [27] validation set.
- **p. 10 / 4 Experiment - extractive body cue:** 4.5 Real-world experiments As shown in Figure 4, we visualize RoboMamba's reasoning results across various robotic downstream tasks.
- **p. 10 / 4 Experiment - extractive body cue:** Additionally, RoboMamba accurately performs fundamental robotic tasks such as affordance generation and discrimination, proving that it can understand robotic scenes.
- **p. 6 / 4 Experiment - extractive body cue:** In Section 4.1, we introduce our experiment settings, including dataset, implementation, and evaluation benchmark details.
- **p. 8 / 4 Experiment - extractive body cue:** For TinyLLaVA and LLaMA-AdapterV2, we evaluate robotic reasoning abilities after fine-tuning the pre-trained MLLMs on the RoboVQA dataset.
- **p. 9 / 4 Experiment - extractive body cue:** Compared with RWKV-3B [24], Mamba-2.7B achieves significant improvements on both common sense and robotic-related reasoning benchmarks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiment (p. 6); B Dataset description (p. 17); 4. Experimental Result Reproducibility (p. 22); 7. Experiment Statistical Significance (p. 23); 8. Experiments Compute Resources (p. 24).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, our RoboMamba achieves a 7.0% improvement on seen tasks and a 2.0% improvement on unseen tasks compared to the ... | p. 8 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared with RWKV-3B [24], Mamba-2.7B achieves significant improvements on both common sense and robotic-related reasoning benchmarks. | p. 9 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate that leveraging the strong generalization abilities of MLLMs can effectively improve the policy's generalization ability while enhancing accuracy on unseen objects. | p. 8 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | To measure the model's performance, we use the classical manipulation success rate, defined as the ratio of successfully manipulated samples to the total test ... | p. 7 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, we find that RoboMamba achieves promising results across all VQA benchmarks, using only a 2.7B language model. | p. 7 (4 Experiment) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiment - extractive body cue:** Datasets (Stage 2) For the dataset used in the robot manipulation fine-tuning stage, we follow the data collection process of previous works [61, 15], adopting ...
- **p. 7 / 4 Experiment - extractive body cue:** Notably, we also directly evaluate RoboMamba's robotic-related reasoning abilities on the 18k validation dataset of RoboVQA, covering robotic tasks such as long-horizon planning, success classification, ...
- **p. 8 / 4 Experiment - extractive body cue:** To comprehensively compare RoboMamba's robotic-related reasoning abilities, we benchmark it against LLaMA-AdapterV2 [45] and TinyLLaVA [83] on the RoboVQA [27] validation set.
- **p. 10 / 4 Experiment - extractive body cue:** 4.5 Real-world experiments As shown in Figure 4, we visualize RoboMamba's reasoning results across various robotic downstream tasks.
- **p. 10 / 4 Experiment - extractive body cue:** Additionally, RoboMamba accurately performs fundamental robotic tasks such as affordance generation and discrimination, proving that it can understand robotic scenes.
- **p. 6 / 4 Experiment - extractive body cue:** In Section 4.1, we introduce our experiment settings, including dataset, implementation, and evaluation benchmark details.
- **p. 8 / 4 Experiment - extractive body cue:** For TinyLLaVA and LLaMA-AdapterV2, we evaluate robotic reasoning abilities after fine-tuning the pre-trained MLLMs on the RoboVQA dataset.
- **p. 9 / 4 Experiment - extractive body cue:** Compared with RWKV-3B [24], Mamba-2.7B achieves significant improvements on both common sense and robotic-related reasoning benchmarks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of RoboMamba. RoboMamba is an efficient robotic VLA model that combines reasoning and manipulation capabilities. First, we integrate and align a vision ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Overall framework of RoboMamba. RoboMamba projects images onto Mamba's language embedding using a vision encoder and projection layer, which is then concatenated with ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Comparison of general reasoning abilities with previous MLLMs across several benchmarks. 'Res.' indicates the resolution of the input image. RoboVQA1 to RoboVQA4 represent ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Comparison of the success rates between RoboMamba and baselines across various training (seen) and test (unseen) tasks. The representation for each task icon ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 3: Ablation study a) The impact of LLM on reasoning abilities. Ablation study b) The impact of reasoning ability on manipulation accuracy. 4.4
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4: The visualization of RoboMamba's abilities across various robotic downstream tasks in real-world scenarios, including task planning, long-horizon planning, discriminative and generative affordance, past ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 3: Representation of each category icon. Stage 2: Robot manipulation fine-tuning dataset. Representation for Each Category Icon In Table 3, we provide an overview ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 4: Ablation study of different image encoders on reasoning abilities. Encoder Image Resolution OKVQA GQA POPE RoboVQA(BLEU-4) CLIP

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Datasets (Stage 2) For the dataset used in the robot manipulation fine-tuning stage, we follow the data collection process of previous works [61, 15], ... | embodiment, simulator version and control stack | p. 7 (4 Experiment), p. 7 (4 Experiment) |
| Task/environment | Notably, we also directly evaluate RoboMamba's robotic-related reasoning abilities on the 18k validation dataset of RoboVQA, covering robotic tasks such as long-horizon planning, success ... | reset, timeout, object/scene variation | p. 7 (4 Experiment), p. 8 (4 Experiment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (1.1 Hz), p. 3 (1.1 Hz) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1 Introduction), p. 2 (1.1 Hz) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To measure the model's performance, we use the classical manipulation success rate, defined as the ratio of successfully manipulated samples to the total test ... | definition/direction/unit from same section | p. 7 (4 Experiment) |
| Table 2: Comparison of the success rates between RoboMamba and baselines across various training (seen) and test (unseen) tasks. The representation for each task ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Manipulation evaluation benchmarks To evaluate our model's manipulation capabilities, we follow previous works [57, 63, 15] and test open-loop task completion accuracy exclusively in ... | definition/direction/unit from same section | p. 7 (4 Experiment) |
| RoboVQA1 to RoboVQA4 represent the BLEU-1 to BLEU-4 scores, respectively. | definition/direction/unit from same section | p. 8 (4 Experiment) |
| The results demonstrate that leveraging the strong generalization abilities of MLLMs can effectively improve the policy's generalization ability while enhancing accuracy on unseen objects. | definition/direction/unit from same section | p. 8 (4 Experiment) |
| The impact of reasoning abilities on manipulation accuracy. | definition/direction/unit from same section | p. 9 (4 Experiment) |
| Subsequently, we conduct extensive experiments to demonstrate RoboMamba's reasoning and manipulation abilities in Sections 4.2 and 4.3, respectively. | definition/direction/unit from same section | p. 6 (4 Experiment) |
| For task planning, compared to LLaMA-AdapterV2, RoboMamba demonstrates more accurate and long-horizon planning abilities, thanks to its strong reasoning capabilities. | definition/direction/unit from same section | p. 10 (4 Experiment) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We choose LLaMA-AdapterV2 as a baseline because it serves as the base model for the current state-of-the-art (SOTA) robot MLLM, ManipLLM [15]. | comparison identity and matched condition | p. 8 (4 Experiment) |
| As shown in Table 1, we compare RoboMamba with previous state-of-the-art (SOTA) MLLMs on general VQA and recent MLLM benchmarks. | comparison identity and matched condition | p. 7 (4 Experiment) |
| Before comparison, we reproduce all baselines and train them on our collected dataset. | comparison identity and matched condition | p. 8 (4 Experiment) |
| For a fair comparison, we also fine-tuned the baseline LLaMA-AdapterV2 on the RoboVQA dataset. | comparison identity and matched condition | p. 10 (4 Experiment) |
| Compared to previous MLLMs, we observe that our model 7 | comparison identity and matched condition | p. 7 (4 Experiment) |
| Compared with RWKV-3B [24], Mamba-2.7B achieves significant improvements on both common sense and robotic-related reasoning benchmarks. | comparison identity and matched condition | p. 9 (4 Experiment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| validate the effectiveness of each method design, we perform an ablation study in Section 4.4. | component/input/data sensitivity | p. 7 (4 Experiment) |
| Figure 1: Overview of RoboMamba. RoboMamba is an efficient robotic VLA model that combines reasoning and manipulation capabilities. First, we integrate and align a ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| 4.4 Ablation study The impact of LLM on reasoning abilities. | component/input/data sensitivity | p. 9 (4 Experiment) |
| Additionally, we present more ablation studies in Appendix C, including explorations of different vision encoders, training datasets, and policy head design. | component/input/data sensitivity | p. 9 (4 Experiment) |
| This finding reveals how to efficiently equip an VLA model with manipulation abilities without compromising its inherent reasoning capabilities. | component/input/data sensitivity | p. 10 (4 Experiment) |
| Table 6: Ablation study of policy head design on manipulation dataset. | component/input/data sensitivity | p. 19 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba ... | As shown in Table 2, our RoboMamba achieves a 7.0% improvement on seen tasks and a 2.0% improvement on unseen tasks compared to the ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiment), p. 9 (4 Experiment), p. 8 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment) |
| Primary metric/result | Compared with RWKV-3B [24], Mamba-2.7B achieves significant improvements on both common sense and robotic-related reasoning benchmarks. | numeric claim only at cited anchor | p. 9 (4 Experiment) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiment - extractive body cue:** In the training set, we collect 10K images across 20 tasks.
- **p. 7 / 4 Experiment - extractive body cue:** During the alignment pre-training and instruction co-training, we conduct training for 1 epoch and 2 epochs, respectively.
- **p. 7 / 4 Experiment - extractive body cue:** For manipulation fine-tuning, we train the model for 8 epochs, setting the LR to 1e-5 and applying a weight decay of 0.1.
- **p. 7 / 4 Experiment - extractive body cue:** A manipulation action is considered successful if the difference in the object's joint state before and after interaction exceeds a threshold of 0.1 meters.
- **p. 2 / 1 Introduction - extractive body cue:** RoboMamba OpenVLA ManipLLM RoboMamba OpenVLA ManipLLM Reasoning Q: current goal is: Take out fruits from the bowl. last 20 steps: 1- put pear on the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Prediction of past and future actions is crucial in robotic manipulation, as it not only enables effective rethinking of past failure actions but also ... | p. 10 (4 Experiment) |
| body limitation/failure cue | Meanwhile, as shown in Figure 5, we also visualize the failure cases of RoboMamba's predictions in both reasoning and manipulation tasks. | p. 10 (4 Experiment) |
| body limitation/failure cue | Figure 6: The visualization of reasoning failure cases. In the bottom right corner of the image, we re-select the qualitative results from our real-world ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Due to space limitations, we provide additional details of the proposed method in this supplementary material. | p. 17 (A Appendix) |
| body limitation/failure cue | The results confirm our finding: fine-tuning an MLLM to learn robot skills does not require extensive resources; it only requires that the MLLM possesses ... | p. 9 (4 Experiment) |
| body limitation/failure cue | Specifically, our model achieves satisfactory results on the POPE benchmark, helping to reduce failed robot actions caused by hallucinations. | p. 8 (4 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation details Before training, RoboMamba loads a pre-trained CLIP/SigLIP ViT-Large [26, 70] as the visual encoder, and the 2.8/1.4B Mamba [1] model as the ... | p. 7 (4 Experiment) |
| We utilize the AdamW optimizer with (β1, β2) = (0.9, 0.999) and a learning rate (LR) of 4e-5. | p. 7 (4 Experiment) |
| In Section 4.1, we introduce our experiment settings, including dataset, implementation, and evaluation benchmark details. | p. 6 (4 Experiment) |
| For a fair comparison, we load the pre-trained parameters of both LLaMAAdapterV2 and TinyLLaVA and fine-tuned the baseline models on the RoboVQA training set ... | p. 8 (4 Experiment) |
| Additionally, we present more ablation studies in Appendix C, including explorations of different vision encoders, training datasets, and policy head design. | p. 9 (4 Experiment) |
| 5 Conclusion and future plan In this paper, we introduce RoboMamba, an efficient VLA model that combines a vision encoder with the linear-complexity Mamba ... | p. 10 (4 Experiment) |
| Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense ... | p. 1 (Abstract) |
| First, we integrate and align a vision encoder with the Mamba LLM, endowing our model with common sense and robotic-related reasoning abilities. | p. 2 (1.1 Hz) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 4 Experiment - extractive body cue:** Prediction of past and future actions is crucial in robotic manipulation, as it not only enables effective rethinking of past failure actions but also enhances ...
- **p. 10 / 4 Experiment - extractive body cue:** Meanwhile, as shown in Figure 5, we also visualize the failure cases of RoboMamba's predictions in both reasoning and manipulation tasks.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 6: The visualization of reasoning failure cases. In the bottom right corner of the image, we re-select the qualitative results from our real-world demonstration. ...
- **p. 17 / A Appendix - extractive body cue:** Due to space limitations, we provide additional details of the proposed method in this supplementary material.
- **p. 9 / 4 Experiment - extractive body cue:** The results confirm our finding: fine-tuning an MLLM to learn robot skills does not require extensive resources; it only requires that the MLLM possesses strong ...
- **p. 8 / 4 Experiment - extractive body cue:** Specifically, our model achieves satisfactory results on the POPE benchmark, helping to reduce failed robot actions caused by hallucinations.

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 10 (4 Experiment), p. 10 (4 Experiment), p. 6 (4 Experiment), metrics p. 7 (4 Experiment), p. 9 (Figure/Table caption), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment), p. 9 (4 Experiment), baselines p. 8 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 10 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment), results p. 8 (4 Experiment), p. 9 (4 Experiment), p. 8 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
