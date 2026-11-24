# RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v229/zitkovich23a.html.
> PDF retrieval source: https://arxiv.org/pdf/2307.15818. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CoRL
- Authors: Brianna Zitkovich, Tianhe Yu, Sichun Xu, Peng Xu, Ted Xiao, Fei Xia, Jialin Wu, Paul Wohlhart, Stefan Welker, Ayzaan Wahid, Quan Vuong, Vincent Vanhoucke, Huong Tran, Radu Soricut, Anikait Singh, Jaspiar Singh, Pierre Sermanet, Pannag R. Sanketi, Grecia Salazar, Michael S. Ryoo, Krista Reymann, Kanishka Rao, Karl Pertsch, Igor Mordatch, Henryk Michalewski, Yao Lu, Sergey Levine, Lisa Lee, Tsang-Wei Edward Lee, Isabel Leal, Yuheng Kuang, Dmitry Kalashnikov, Ryan Julian, Nikhil J. Joshi, Alex Irpan, Brian Ichter, Jasmine Hsu, Alexander Herzog, Karol Hausman, Keerthana Gopalakrishnan, Chuyuan Fu, Pete Florence, Chelsea Finn, Kumar Avinava Dubey, Danny Driess, Tianli Ding, Krzysztof Marcin Choromanski, Xi Chen, Yevgen Chebotar, Justice Carbajal, Noah Brown, Anthony Brohan, Montserrat Gonzalez Arenas, Kehang Han
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://proceedings.mlr.press/v229/zitkovich23a.html
- Full-text retrieval: https://arxiv.org/pdf/2307.15818
- Code/Project: https://robotics-transformer2.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## 공개 자료

- **데이터** DeepMind가 RT-2의 로봇 학습 입력으로 명시한 RT-1 데이터에서 Google 팀이 공개한 RLDS 훈련 조각을 확인했다. RT-2에 투입한 정확한 표본 목록, 웹 혼합과 RT-2 평가 로그는 미확인이다. [배포 파일](https://storage.googleapis.com/storage/v1/b/gresearch/o/robotics%2Ffractal20220817_data%2F0.1.0%2Ffractal20220817_data-train.tfrecord-00000-of-01024?generation=1696340210661554) · [저자 설명](https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/)

## Why This Paper Is Here

RT-2는 웹 시각·언어 과제와 로봇 시연을 함께 미세조정해 영상과 지시에서 로봇 행동을 생성한다.

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** High-capacity models pretrained on broad web-scale datasets provide an effective and powerful platform for a wide range of downstream tasks: large language models can enable ...
- **p. 1 / 1. Introduction - extractive body cue:** Such semantic reasoning, problem solving, and visual interpretation capabilities would be tremendously useful for generalist robots that must perform a variety of tasks in real-world ...
- **p. 2 / 1. Introduction - extractive body cue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Q: What is happening in the image?
- **p. 2 / 1. Introduction - extractive body cue:** A grey donkey walks down the street.
- **p. 2 / 1. Introduction - extractive body cue:** On the other hand, directly applying such models to robotic tasks is also difficult: such models reason about semantics, labels, and textual prompts, whereas robots ...
- **p. 2 / 1. Introduction - extractive body cue:** This simple approach is in contrast with prior alternatives for incorporating VLMs into robot policies (Shridhar et al., 2022a) or designing new vision-languageaction architectures from ...

## Core Idea

- **p. 3 / 1. Introduction - extractive body cue:** Our main contribution is RT-2, a family of models derived from fine-tuning large vision-language models trained on web-scale data to directly act as generalizable and ...
- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** In this section, we present our model family and the design choices for enabling training VLMs to directly perform closed-loop robot control.
- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** Then, we introduce the recipe and challenges of fine-tuning large VLMs that are pre-trained on web-scale data to directly output robot actions, becoming VLA models.
- **p. 5 / 3.2. Robot-Action Fine-tuning - extractive body cue:** The action space consists of 6-DoF positional and rotational displacement of the robot end-effector, as well as the level of extension of the robot gripper ...
- **p. 3 / 1. Introduction - extractive body cue:** Over the course of 6k robotic evaluations, we show that RT-2 enable significant improvements to generalization over objects, scenes, and instructions, and exhibit a breadth ...
- **p. 4 / 3. Vision-Language-Action Models - extractive body cue:** First, we describe the general architecture of our models and how they can be derived from models that are commonly used for vision-language tasks.
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** Thus, to ensure that RT-2 outputs valid action tokens during decoding, we constrain its output vocabulary via only sampling valid action tokens when the model ...
- **p. 6 / 3.2. Robot-Action Fine-tuning - extractive body cue:** For the PaLM-E model, which does not provide this convenient representation of numbers, we simply overwrite the 256 least frequently used tokens to represent the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Although such models are typically trained to produce natural language tokens, we can train them on robotic trajectories by tokenizing the actions into text tokens and creating "multimodal sentences" (Driess et al., ... | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 6 (3.2. Robot-Action Fine-tuning) |
| State/latent | Although, models, typically, trained, produce, natural, language, tokens, train, them, robotic, trajectories | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 6 (3.2. Robot-Action Fine-tuning), p. 2 (1. Introduction) |
| Output/action | Taking the action representation described above, we convert our robot data to be suitable for VLM model fine-tuning, where our inputs include robot camera image and textual task description (using standard VQA ... | continuous action, pose 또는 action chunk | p. 6 (3.2. Robot-Action Fine-tuning), p. 2 (1. Introduction), p. 5 (3.2. Robot-Action Fine-tuning) |
| Objective/outcome | instruction following, task success, generalization과 latency | instruction following, task success, generalization과 latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 행동을 텍스트와 같은 형식의 토큰으로 바꾸어 기존 시각·언어 모델의 출력으로 학습한다.
- 로봇 시연에 없던 물체와 의미 지시를 포함한 실물 조작에서 일반화를 평가한다.

[저자 원문](https://proceedings.mlr.press/v229/zitkovich23a.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4. Experiments), p. 8 (4. Experiments) |
| Embodiment/environment | Each robot demonstration trajectory is annotated with a natural language instruction that describes the task performed, consisting of a verb describing the skill (e.g., "pick", "open", "place into") and one or more ... | hardware/simulator version and reset protocol | p. 7 (4. Experiments), p. 8 (4. Experiments) |
| Dataset/benchmark | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Figure 5 / Real-world out-of-distribution behaviors in the Language Table environment. | role, split, size and leakage | p. 7 (4. Experiments), p. 8 (4. Experiments), p. 9 (4. Experiments), p. 8 (4. Experiments) |
| Metric | The performance on seen tasks is similar between the RT-2 models and RT-1, with other baselines attaining a lower success rate. | definition, denominator, direction and uncertainty | p. 8 (4. Experiments), p. 9 (4. Experiments), p. 7 (4. Experiments) |
| Baseline/ablation | We compare our method to multiple state-of-the-art baselines that challenge different aspects of our method. | fair input/data/compute/action matching | p. 7 (4. Experiments), p. 8 (4. Experiments), p. 9 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 11 / 5. Limitations - extractive body cue:** Even though RT-2 exhibits promising generalization properties, there are multiple limitations of this approach.
- **p. 11 / 5. Limitations - extractive body cue:** This is also connected to another current limitation in that there are only a small number of generally available VLM models that can be used ...
- **p. 9 / 4. Experiments - extractive body cue:** For the task "pick up the bag about to fall off the table," RT-2 demonstrates physical understanding to disambiguate between two bags and recognize the ...
- **p. 8 / 4. Experiments - extractive body cue:** We also show qualitative real-world out-of-distribution behaviors behaviors in Figure 5, demonstrating novel pushing tasks and targeting objects not before seen in this environment.
- **p. 9 / 4. Experiments - extractive body cue:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control Figure 5 / Real-world out-of-distribution behaviors in the Language Table environment.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (1. Introduction), p. 4 (3. Vision-Language-Action Models)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Such semantic reasoning, problem solving, and visual interpretation capabilities would be tremendously useful for generalist robots that must perform a variety of tasks in real-world environments. (p. 1, 1. Introduction).
- **Actual contribution:** Our main contribution is RT-2, a family of models derived from fine-tuning large vision-language models trained on web-scale data to directly act as generalizable and semantically aware robotic policies. (p. 3, 1. Introduction).
- **Evaluation boundary:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (a) Performance comparison on various emergent skill evaluations (Figure 8) between RT-2 and two baselines. (p. 10, 4. Experiments).
- **Explicit failure boundary:** Even though RT-2 exhibits promising generalization properties, there are multiple limitations of this approach. (p. 11, 5. Limitations).
