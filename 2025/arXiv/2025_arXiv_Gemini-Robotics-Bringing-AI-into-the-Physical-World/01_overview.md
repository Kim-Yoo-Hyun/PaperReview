# Gemini Robotics: Bringing AI into the Physical World

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.20020.
> PDF retrieval source: https://arxiv.org/abs/2503.20020. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / arXiv
- Authors: Gemini Robotics Team, Saminda Abeyruwan, Joshua Ainslie, Jean-Baptiste Alayrac, Montserrat Gonzalez Arenas, Travis Armstrong, Ashwin Balakrishna, Robert Baruch, Maria Bauza, Michiel Blokzijl, Steven Bohez, Konstantinos Bousmalis, Anthony Brohan, Thomas Buschmann, Arunkumar Byravan, Serkan Cabi, Ken Caluwaerts, Federico Casarini, Oscar Chang, Jose Enrique Chen, Xi Chen, Hao-Tien Lewis Chiang, Krzysztof Choromanski, David D'Ambrosio, Sudeep Dasari, Todor Davchev, Coline Devin, Norman Di Palo, Tianli Ding, Adil Dostmohamed, Danny Driess, Yilun Du, Debidatta Dwibedi, Michael Elabd, Claudio Fantacci, Cody Fong, Erik Frey, Chuyuan Fu, Marissa Giustina, Keerthana Gopalakrishnan, Laura Graesser, Leonard Hasenclever, Nicolas Heess, Brandon Hernaez, Alexander Herzog, R. Alex Hofer, Jan Humplik, Atil Iscen, Mithun George Jacob, Deepali Jain, Ryan Julian, Dmitry Kalashnikov, M. Emre Karagozler, Stefani Karp, Chase Kew, Jerad Kirkland, Sean Kirmani, Yuheng Kuang, Thomas Lampe, Antoine Laurens, Isabel Leal, Alex X. Lee, Tsang-Wei Edward Lee, Jacky Liang, Yixin Lin, Sharath Maddineni, Anirudha Majumdar, Assaf Hurwitz Michaely, Robert Moreno, Michael Neunert, Francesco Nori, Carolina Parada, Emilio Parisotto, Peter Pastor, Acorn Pooley, Kanishka Rao, Krista Reymann, Dorsa Sadigh, Stefano Saliceti, Pannag Sanketi, Pierre Sermanet, Dhruv Shah, Mohit Sharma, Kathryn Shea, Charles Shu, Vikas Sindhwani, Sumeet Singh, Radu Soricut, Jost Tobias Springenberg, Rachel Sterneck, Razvan Surdulescu, Jie Tan, Jonathan Tompson, Vincent Vanhoucke, Jake Varley, Grace Vesom, Giulia Vezzani, Oriol Vinyals, Ayzaan Wahid, Stefan Welker, Paul Wohlhart, Fei Xia, Ted Xiao, Annie Xie, Jinyu Xie, Peng Xu, Sichun Xu, Ying Xu, Zhuo Xu, Yuxiang Yang, Rui Yao, Sergey Yaroshenko, Wenhao Yu, Wentao Yuan, Jingwei Zhang, Tingnan Zhang, Allan Zhou, Yuxiang Zhou
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, Foundation Models, dexterous manipulation, Google DeepMind
- Official paper: https://arxiv.org/abs/2503.20020
- Full-text retrieval: https://arxiv.org/abs/2503.20020
- Code/Project: https://deepmind.google/models/gemini-robotics/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Gemini Robotics는 멀티모달 기반 모델을 실제 로봇 행동 생성에 적응시킨 VLA다.

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** The remarkable progress of modern artificial intelligence (AI) models - with pre-training on largescale datasets - has redefined information processing, demonstrating proficiency and generalization across ...
- **p. 1 / 1. Introduction - extractive body cue:** This has opened a vast landscape of opportunities for interactive and assistive systems within the digital realm, ranging from multimodal chatbots to virtual assistants.
- **p. 1 / 1. Introduction - extractive body cue:** However, realizing the potential of general-purpose autonomous AI in the physical world requires a substantial shift from the digital world, where physically grounded AI agents ...
- **p. 1 / 1. Introduction - extractive body cue:** While, as humans, we take for granted our embodied reasoning abilities - such as perceiving the 3D structure of environments, interpreting complex inter-object relationships, or ...
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, an embodied AI agent must also go beyond passively understanding the spatial and physical concepts of the real world; it must also learn to ...
- **p. 13 / 2.0 Flash - extractive body cue:** However, as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed to connect the ...
- **p. 3 / 1. Introduction - extractive body cue:** To emphasize the flexibility and generality of the Gemini Robotics models, we also introduce an optional specialization stage, which demonstrates how Gemini Robotics can be ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce the Gemini Robotics family of embodied AI models, built on top of Gemini 2.0, our most advanced multimodal foundation model.
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** To capture progress in embodied reasoning for VLMs, we introduce ERQA, short for Embodied Reasoning Question Answering, a benchmark that focuses specifically on capabilities likely ...
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** ERQA consists of 400 multiple choice Visual Question Answering (VQA)-style questions across a wide variety of categories, including spatial reasoning, trajectory reasoning, action reasoning, state ...
- **p. 7 / 2.0 Flash. Predicted point labels are not visualized - extractive body cue:** Below we present detailed quantitative and qualitative evaluations of these capabilities with Gemini 2.0 models (Flash, and Pro Experimental), as well as comparisons with other ...
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, an embodied AI agent must also go beyond passively understanding the spatial and physical concepts of the real world; it must also learn to ...
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini Robotics ...
- **p. 13 / 3. Robot Actions with Gemini Robotics - extractive body cue:** We first study the model after training on a large and diverse dataset consisting of action-labeled robot data as well as other multimodal data.
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** It consists of two components: a VLA backbone hosted in the cloud (Gemini Robotics backbone) and a local action decoder running on the robot's onboard ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini Robotics model. | image/video, language instruction, proprioception과 history | p. 14 (3. Robot Actions with Gemini Robotics), p. 7 (2.0 Flash. Predicted point labels are not visualized) |
| State/latent | backbone, Local, action, decoder, computer, Robot, images, state, image, Figure, Overview, architecture | language-grounded task state와 action-policy context | p. 14 (3. Robot Actions with Gemini Robotics), p. 7 (2.0 Flash. Predicted point labels are not visualized), p. 11 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control) |
| Output/action | While it is possible to create expert models for each of these tasks individually, fusing them in a single foundation model, such as Gemini 2.0, allows the model to perform embodied reasoning ... | continuous action, pose 또는 action chunk | p. 7 (2.0 Flash. Predicted point labels are not visualized), p. 11 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 13 (2.0 Flash) |
| Objective/outcome | To this end, we study a fine-tuning process that utilizes a re-labeled version of the robot action dataset in Section 3.1, bringing action prediction closer to the newly introduced embodied reasoning capabilities: ... | instruction following, task success, generalization과 latency | p. 22 (4.2. Enhanced reasoning and generalization), p. 23 (4.2. Enhanced reasoning and generalization), p. 14 (3. Robot Actions with Gemini Robotics) |

## Main Claims and Actual Contribution

- 언어 지시와 시각 관측을 연속적인 로봇 행동에 연결한다.
- 실제 조작 과제에서 일반화와 지시 따르기를 평가한다.

[저자 원문](https://arxiv.org/abs/2503.20020)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (2.0 Pro Experimental) |
| Embodiment/environment | Gemini Robotics: Bringing AI into the Physical World Gemini GPT Claude Benchmark | hardware/simulator version and reset protocol | p. 5 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark) |
| Dataset/benchmark | Spatial Reasoning 84 Action Reasoning 72 Trajectory Reasoning 66 State Estimation 55 Task Reasoning 38 Multi-view Reasoning 37 Pointing 34 Other 14 Figure 4 / ERQA question categories. | role, split, size and leakage | p. 5 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark) |
| Metric | (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories). | definition, denominator, direction and uncertainty | p. 10 (2.0 Pro Experimental) |
| Baseline/ablation | For each image pair, the left image with the point coordinates and the right image without coordinates are given, and the model predicts which of the labeled points in the left image ... | fair input/data/compute/action matching | p. 10 (2.0 Pro Experimental), p. 10 (2.0 Pro Experimental) |

## Explicit Limitations and Failure Boundary

- **p. 28 / 6. Discussion - extractive body cue:** In addition, while our initial results with Gemini Robotics demonstrate promising generalization capabilities, future work will focus on several key areas.
- **p. 28 / 6. Discussion - extractive body cue:** Robust human-level embodied reasoning is critical for robots and other physically grounded agents.
- **p. 29 / 6. Discussion - extractive body cue:** This involves developing techniques to seamlessly integrate abstract reasoning with precise execution, leading to more robust and generalizable performance.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 13 (2.0 Flash), p. 3 (1. Introduction), p. 8 (3.5 Sonnet), p. 12 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 2 (1. Introduction), p. 14 (3. Robot Actions with Gemini Robotics)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (64 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed to connect the model's innate embodied reasoning capabilities ... (p. 13, 2.0 Flash).
- **Actual contribution:** Furthermore, an embodied AI agent must also go beyond passively understanding the spatial and physical concepts of the real world; it must also learn to take actions that have direct ... (p. 1, 1. Introduction).
- **Evaluation boundary:** Gemini Robotics: Bringing AI into the Physical World Gemini GPT Claude Benchmark (p. 5, 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark).
- **Explicit failure boundary:** While the PaliGemma-based 𝜋0 re-implement correctly approaches objects that were seen during training, it struggles with interpreting descriptive language attributes (e.g., "top black container", "blue clip") and fails to solve ... (p. 17, 3.3. Gemini Robotics can closely follow language instructions).

## 원문과 공개 자료

- 데이터 · 원문은 ALOHA 2 Sim Task suite 실험에 사용한 자료를 보고한다. 이 연구의 해당 자료 배포 파일은 미확인이다. [검토 근거](https://arxiv.org/pdf/2503.20020)
