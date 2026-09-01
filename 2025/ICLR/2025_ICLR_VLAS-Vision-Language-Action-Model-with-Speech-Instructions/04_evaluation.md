# Evaluation - VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=K4FAFNRpko; PDF retrieval source: https://openreview.net/pdf/5f77b9b6bd43ed1a7a7d7ba9fc75c64727d77792.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 8 (1. I have a blue), p. 9 (1. I have a blue), p. 8 (1. I have a blue), p. 7 (1. I have a blue), p. 7 (1. I have a blue)): Figure 7: Demonstration of success cases of VLAS on the real-world UR5 robot arm. In Table 4, VLAS-Base achieves comparable performance to Whisper large-v2 on the LibriSpeech test set. Considering ...

## Evaluation Body Digest

- **p. 8 / 1. I have a blue - extractive PDF cue:** 4.3 EXPERIMENTS WITH A REAL-WORLD UR5 ROBOT ARM We fine-tune our VLAS-Base by utilizing both the Berkeley UR5 demonstration dataset and our own cup-picking dataset.
- **p. 8 / 1. I have a blue - extractive PDF cue:** Particularly, this benchmark includes three task categories: (1) Object Ownership Tasks: The robot must interact with the appropriate objects according to their ownership.
- **p. 6 / 1. I have a blue - extractive PDF cue:** CALVIN with Speech Instructions (CSI) Dataset Given that conventional robot manipulation datasets contain only textual task instructions, we utilized the aforementioned TTS model to generate ...
- **p. 6 / 1. I have a blue - extractive PDF cue:** Stage III: Robot Manipulation Fine-tuning, where the model is further fine-tuned to execute robot manipulation tasks using both speech and text instructions. instructions, paired with ...
- **p. 7 / 1. I have a blue - extractive PDF cue:** 4.1 ROBOT MANIPULATION WITH SPEECH INSTRUCTIONS To quantitatively assess the performance of our proposed model for robot manipulation tasks, we conduct experiments on the CALVIN ...
- **p. 7 / 1. I have a blue - extractive PDF cue:** Each sample in this dataset contains a complete motion trajectory, represented as a sequence of robot actions, along with visual observations from two distinct views ...
- **p. 10 / 1. I have a blue - extractive PDF cue:** Published as a conference paper at ICLR 2025 Pick up my cup Speaker Id: 1089 Meta: I have a {green} cup Speaker Id: 6829 Meta: ...
- **p. 9 / 1. I have a blue - extractive PDF cue:** Ownership Ownership Ownership Preference Preference Preference Figure 5: Demonstration of object ownership tasks (top row) and user preference tasks (bottom row) for customized robot manipulation.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** B EXTENDED EXPERIMENTAL RESULTS (p. 15); B.2 COMPARISON WITH ROBOFLAMINGO ON THE CALVIN BENCHMARK (p. 16); B.3 COMPARISON WITH OPENVLA ON THE CALVIN BENCHMARK (p. 16).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Demonstration of success cases of VLAS on the real-world UR5 robot arm. In Table 4, VLAS-Base achieves comparable performance to Whisper large-v2 ... | p. 10 (Figure/Table caption) |
| 1. I have a blue | EMPIRICAL / REAL-ROBOT OR HARDWARE | Meanwhile, when our RAG module is integrated with the VLA, its performance significantly improves. | p. 8 (1. I have a blue) |
| 1. I have a blue | EMPIRICAL / REAL-ROBOT OR HARDWARE | As can be observed, VLAS-Base obtains nearly the same performance to LLaVA, while significantly outperforming other VLMs. | p. 9 (1. I have a blue) |
| 1. I have a blue | EMPIRICAL / REAL-ROBOT OR HARDWARE | As a result, our model demonstrates much better performance on this benchmark, achieving an average success rate of over 86%. | p. 8 (1. I have a blue) |
| 1. I have a blue | EMPIRICAL / REAL-ROBOT OR HARDWARE | Models Splits LH-1 LH-2 LH-3 LH-4 LH-5 Len MCIL+ ABCD/D 37.3% 2.7% 0.2% 0.0% 0.0% 0.40 HULC+ ABCD/D 89.2% 70.1% 54.8% 42.0% 33.5% 2.90 ... | p. 7 (1. I have a blue) |

## Dataset / Benchmark Role

- **p. 8 / 1. I have a blue - extractive PDF cue:** 4.3 EXPERIMENTS WITH A REAL-WORLD UR5 ROBOT ARM We fine-tune our VLAS-Base by utilizing both the Berkeley UR5 demonstration dataset and our own cup-picking dataset.
- **p. 8 / 1. I have a blue - extractive PDF cue:** Particularly, this benchmark includes three task categories: (1) Object Ownership Tasks: The robot must interact with the appropriate objects according to their ownership.
- **p. 6 / 1. I have a blue - extractive PDF cue:** CALVIN with Speech Instructions (CSI) Dataset Given that conventional robot manipulation datasets contain only textual task instructions, we utilized the aforementioned TTS model to generate ...
- **p. 6 / 1. I have a blue - extractive PDF cue:** Stage III: Robot Manipulation Fine-tuning, where the model is further fine-tuned to execute robot manipulation tasks using both speech and text instructions. instructions, paired with ...
- **p. 7 / 1. I have a blue - extractive PDF cue:** 4.1 ROBOT MANIPULATION WITH SPEECH INSTRUCTIONS To quantitatively assess the performance of our proposed model for robot manipulation tasks, we conduct experiments on the CALVIN ...
- **p. 7 / 1. I have a blue - extractive PDF cue:** Each sample in this dataset contains a complete motion trajectory, represented as a sequence of robot actions, along with visual observations from two distinct views ...
- **p. 10 / 1. I have a blue - extractive PDF cue:** Published as a conference paper at ICLR 2025 Pick up my cup Speaker Id: 1089 Meta: I have a {green} cup Speaker Id: 6829 Meta: ...
- **p. 9 / 1. I have a blue - extractive PDF cue:** Ownership Ownership Ownership Preference Preference Preference Figure 5: Demonstration of object ownership tasks (top row) and user preference tasks (bottom row) for customized robot manipulation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: For personalization tasks, (a) previous VLAs with text instructions fail, while (b) our VLAS with speech in- structions could successfully address them. To ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overall Framework of VLAS. VLAS encodes visual and speech inputs via encoders and MLP layers to obtain respective embeddings. The Voice RAG module ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Data collection process for the SQA and CSI datasets. speech tokens may impose a significant computational burden when directly input into the LLM, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Training paradigm of VLAS. The training process of VLAS is divided into three stages. Stage I: Speech Alignment, where the model aligns speech ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Performance of different robot policy models on the CALVIN benchmark. +: Evaluated with the ground truth textual instructions. *: Evaluated with the speech ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Performance of three types of customized tasks for robot manipulation. +: Evaluated with the ground truth textual instructions. *: Evaluated with the speech ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Demonstration of object ownership tasks (top row) and user preference tasks (bottom row) for customized robot manipulation. Speaker id: 260 Meta: I have ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: Demonstration of compound tasks for customized robot manipulation. 4.4 ANALYSIS FOR THE VLAS-BASE FOUNDATION MODEL The multimodal understanding capability of the VLAS-Base is ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.3 EXPERIMENTS WITH A REAL-WORLD UR5 ROBOT ARM We fine-tune our VLAS-Base by utilizing both the Berkeley UR5 demonstration dataset and our own cup-picking ... | embodiment, simulator version and control stack | p. 8 (1. I have a blue), p. 8 (1. I have a blue) |
| Task/environment | Particularly, this benchmark includes three task categories: (1) Object Ownership Tasks: The robot must interact with the appropriate objects according to their ownership. | reset, timeout, object/scene variation | p. 8 (1. I have a blue), p. 6 (1. I have a blue) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3 METHOD), p. 1 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3 METHOD), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 4: Performance comparison on LibriSpeech and SGQA benchmark, using word error rate (WER) and accuracy as evaluation metrics. LLaVA and BLIP-2 employ the ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| As a result, our model demonstrates much better performance on this benchmark, achieving an average success rate of over 86%. | definition/direction/unit from same section | p. 8 (1. I have a blue) |
| Because the VLA baseline relies solely on text instructions and lacks access to background knowledge, its performance is severely limited, with an average success ... | definition/direction/unit from same section | p. 8 (1. I have a blue) |
| Figure 8: Demonstration of failure cases of VLAS on the customization benchmark. We conducted additional analysis on the failure cases of VLAS and VLA ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Figure 1: For personalization tasks, (a) previous VLAs with text instructions fail, while (b) our VLAS with speech in- structions could successfully address them. ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 7: Demonstration of success cases of VLAS on the real-world UR5 robot arm. In Table 4, VLAS-Base achieves comparable performance to Whisper large-v2 ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 9: Demonstration of failure cases of VLA on the customization benchmark. B.2 COMPARISON WITH ROBOFLAMINGO ON THE CALVIN BENCHMARK RoboFlamingo is another prominent ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 2: Overall Framework of VLAS. VLAS encodes visual and speech inputs via encoders and MLP layers to obtain respective embeddings. The Voice RAG ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Moreover, our VLAS is compared for speech modality input with the baseline VLA model and another powerful VLA model, Roboflamingo, both similarly derived from ... | comparison identity and matched condition | p. 7 (1. I have a blue) |
| We trained a traditional VLA model with the same configurations by directly fine-tuning the LLaVA backbone, without support for speech instructions, as the baseline. | comparison identity and matched condition | p. 7 (1. I have a blue) |
| Table 3: Performance comparison between state-of-the-art VLMs to VLAS-Base across diverse multimodal evaluation benchmarks. | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Published as a conference paper at ICLR 2025 We found that VLAS significantly outperforms the other two methods that utilize a cascading pipeline for ... | comparison identity and matched condition | p. 8 (1. I have a blue) |
| Because the VLA baseline relies solely on text instructions and lacks access to background knowledge, its performance is severely limited, with an average success ... | comparison identity and matched condition | p. 8 (1. I have a blue) |
| For the speech recognition benchmark, we employ the state-ofthe-art Whisper large-v2 model as the baseline. | comparison identity and matched condition | p. 9 (1. I have a blue) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Both of the ablation studies above demonstrate the effectiveness of the Voice RAG module. | component/input/data sensitivity | p. 8 (1. I have a blue) |
| Ablation studies are conducted to further validate the effectiveness of our proposed Voice RAG module. | component/input/data sensitivity | p. 8 (1. I have a blue) |
| We trained a traditional VLA model with the same configurations by directly fine-tuning the LLaVA backbone, without support for speech instructions, as the baseline. | component/input/data sensitivity | p. 7 (1. I have a blue) |
| Finally, in Section 4.4, to verify whether our foundation model for robot manipulation truly understands speech instructions without compromising LLaVA's original performance, we evaluate ... | component/input/data sensitivity | p. 7 (1. I have a blue) |
| Table 5: Comparison with RoboFlamingo on the CALVIN Benchmark. The performance of RoboFlamingo without historical information is derived from results presented in their original ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Figure 9: Demonstration of failure cases of VLA on the customization benchmark. B.2 COMPARISON WITH ROBOFLAMINGO ON THE CALVIN BENCHMARK RoboFlamingo is another prominent ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech ... | Figure 7: Demonstration of success cases of VLAS on the real-world UR5 robot arm. In Table 4, VLAS-Base achieves comparable performance to Whisper large-v2 ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 8 (1. I have a blue), p. 9 (1. I have a blue), p. 8 (1. I have a blue), p. 7 (1. I have a blue), p. 7 (1. I have a blue) |
| Primary metric/result | Meanwhile, when our RAG module is integrated with the VLA, its performance significantly improves. | numeric claim only at cited anchor | p. 8 (1. I have a blue) |

- Numeric sentences retained from the body:
- **p. 7 / 1. I have a blue - extractive PDF cue:** 4.1 ROBOT MANIPULATION WITH SPEECH INSTRUCTIONS To quantitatively assess the performance of our proposed model for robot manipulation tasks, we conduct experiments on the CALVIN ...
- **p. 8 / 1. I have a blue - extractive PDF cue:** 4.2 ROBOT MANIPULATION FOR CUSTOMIZED TASKS Table 2: Performance of three types of customized tasks for robot manipulation. +: Evaluated with the ground truth textual ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 8: Demonstration of failure cases of VLAS on the customization benchmark. We conducted additional analysis on the failure cases of VLAS and VLA ... | p. 15 (Figure/Table caption) |
| body limitation/failure cue | Figure 9: Demonstration of failure cases of VLA on the customization benchmark. B.2 COMPARISON WITH ROBOFLAMINGO ON THE CALVIN BENCHMARK RoboFlamingo is another prominent ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Our future work may focus on exploring other auxiliary information in human speech or environmental sounds to enable the robot to better understand and ... | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Moreover, although VLAS-Base falls behind LLaVA with ground-truth textual instructions on the SGQA benchmark, it still surpasses BLIP-2. | p. 10 (1. I have a blue) |
| body limitation/failure cue | These results indicate that the introduction of the speech modality does not degrade the performance of the foundation model. | p. 9 (1. I have a blue) |
| body limitation/failure cue | Figure 1: For personalization tasks, (a) previous VLAs with text instructions fail, while (b) our VLAS with speech in- structions could successfully address them. ... | p. 2 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Published as a conference paper at ICLR 2025 VLAS Vision Encoder Speech Encoder LLaMA Voice RAG MLP MLP Tokenizer ΔT = [-0.9, 0.3, 0.1] ... | p. 4 (3 METHOD) |
| Throughout this phase, all network components are updated, with the exception of the pre-trained image and speech encoders. | p. 6 (1. I have a blue) |
| During this phase, only the MLP layer between the speech encoder and the LLM backbone is updated to fulfill speech recognition tasks. | p. 6 (1. I have a blue) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 8: Demonstration of failure cases of VLAS on the customization benchmark. We conducted additional analysis on the failure cases of VLAS and VLA on ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 9: Demonstration of failure cases of VLA on the customization benchmark. B.2 COMPARISON WITH ROBOFLAMINGO ON THE CALVIN BENCHMARK RoboFlamingo is another prominent VLA ...
- **p. 10 / 5 CONCLUSION - extractive PDF cue:** Our future work may focus on exploring other auxiliary information in human speech or environmental sounds to enable the robot to better understand and complete ...
- **p. 10 / 1. I have a blue - extractive PDF cue:** Moreover, although VLAS-Base falls behind LLaVA with ground-truth textual instructions on the SGQA benchmark, it still surpasses BLIP-2.
- **p. 9 / 1. I have a blue - extractive PDF cue:** These results indicate that the introduction of the speech modality does not degrade the performance of the foundation model.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: For personalization tasks, (a) previous VLAs with text instructions fail, while (b) our VLAS with speech in- structions could successfully address them. To ...

- **PDF anchors reviewed:** datasets p. 8 (1. I have a blue), p. 8 (1. I have a blue), p. 6 (1. I have a blue), p. 6 (1. I have a blue), p. 7 (1. I have a blue), p. 7 (1. I have a blue), metrics p. 10 (Figure/Table caption), p. 8 (1. I have a blue), p. 8 (1. I have a blue), p. 15 (Figure/Table caption), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption), baselines p. 7 (1. I have a blue), p. 7 (1. I have a blue), p. 10 (Figure/Table caption), p. 8 (1. I have a blue), p. 8 (1. I have a blue), p. 9 (1. I have a blue), results p. 10 (Figure/Table caption), p. 8 (1. I have a blue), p. 9 (1. I have a blue), p. 8 (1. I have a blue), p. 7 (1. I have a blue), p. 7 (1. I have a blue).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
