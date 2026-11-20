# Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2204.01691.
> PDF retrieval source: https://arxiv.org/pdf/2204.01691. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CoRL
- Authors: Brian Ichter, Anthony Brohan, Yevgen Chebotar, Chelsea Finn, Karol Hausman, Alexander Herzog, Daniel Ho, Julian Ibarz, Alex Irpan, Eric Jang, Ryan Julian, Dmitry Kalashnikov, Sergey Levine, Yao Lu, Carolina Parada, Kanishka Rao, Pierre Sermanet, Alexander T Toshev, Vincent Vanhoucke, Fei Xia, Ted Xiao, Peng Xu, Mengyuan Yan, Noah Brown, Michael Ahn, Omar Cortes, Nicolas Sievers, Clayton Tan, Sichun Xu, Diego Reyes, Jarek Rettinghouse, Jornell Quiambao, Peter Pastor, Linda Luu, Kuang-Huei Lee, Yuheng Kuang, Sally Jesmonth, Nikhil J. Joshi, Kyle Jeffrey, Rosario Jauregui Ruano, Jasmine Hsu, Keerthana Gopalakrishnan, Byron David, Andy Zeng, Chuyuan Kelly Fu
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: LLM, affordance, Planning, Robotics
- Official paper: https://arxiv.org/abs/2204.01691
- Full-text retrieval: https://arxiv.org/pdf/2204.01691
- Code/Project: https://say-can.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

SayCan은 언어 모델이 지시와 맞는다고 평가한 기술과 현재 로봇 상태에서 실행할 수 있는 기술을 함께 고려해 다음 행동을 고른다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large language models can encode a wealth of semantic knowledge about the world.
- **p. 1 / Abstract - extractive body cue:** Such knowledge could be extremely useful to robots aiming to act upon high-level, temporally extended instructions expressed in natural language.
- **p. 1 / Abstract - extractive body cue:** However, a significant weakness of language models is that they lack real-world experience, which makes it difficult to leverage them for decision making within a ...
- **p. 1 / Abstract - extractive body cue:** For example, asking a language model to describe how to clean a spill might result in a reasonable narrative, but it may not be applicable ...
- **p. 1 / Abstract - extractive body cue:** We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are ...
- **p. 2 / 1 Introduction - extractive body cue:** With prompt engineering, a LLM may be capable of splitting the high-level instruction into sub-tasks, but it cannot do so without the context of what ...
- **p. 2 / 1 Introduction - extractive body cue:** This question poses a major challenge.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is capable ...
- **p. 2 / 1 Introduction - extractive body cue:** Our method, SayCan, extracts and leverages the knowledge within LLMs in physically-grounded tasks.
- **p. 1 / Abstract - extractive body cue:** We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are ...
- **p. 4 / 2 Preliminaries - extractive body cue:** With this approach, we are able to effectively extract knowledge from the language model, but it leaves a major issue: while the decoding of the ...
- **p. 6 / 2 Preliminaries - extractive body cue:** We test our method in two environments: a real office kitchen and a mock environment mirroring the kitchen, which is also the environment in which ...
- **p. 2 / 2 Preliminaries - extractive body cue:** Recent breakthroughs initiated by neural network-based Attention architectures [2] have enabled efficient scaling of so-called Large Language Models (LLMs).
- **p. 5 / 2 Preliminaries - extractive body cue:** To learn a language-conditioned RL policy, we use MT-Opt [14] in the Everyday Robots simulator using RetinaGAN sim-to-real transfer [16].
- **p. 6 / 2 Preliminaries - extractive body cue:** We use a network architecture similar to MT-Opt (shown in Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The goal of TD methods is to learn state or state-action value functions (Q-function) Qπ(s, a), which represents the discounted sum of rewards when starting from state s and action a, followed ... | image/video, language instruction, proprioception과 history | p. 3 (2 Preliminaries), p. 3 (2 Preliminaries) |
| State/latent | goal, methods, learn, state, state-action, value, functions, Q-function, represents, discounted, rewards, when | language-grounded task state와 action-policy context | p. 3 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries) |
| Output/action | Therefore, to adapt language models to our problem statement, we must somehow inform them that we specifically want the high-level instruction to be broken down into sequences of available low-level skills. | continuous action, pose 또는 action chunk | p. 3 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries) |
| Objective/outcome | We leverage that intuition in our setup and express affordances via value functions of sparse reward tasks. | instruction following, task success, generalization과 latency | p. 3 (2 Preliminaries), p. 3 (2 Preliminaries), p. 4 (2 Preliminaries) |

## Main Claims and Actual Contribution

- 언어적 적합성과 학습한 기술의 실행 가능성을 결합한다.
- 실제 이동 조작 로봇에서 여러 단계의 자연어 지시를 평가한다.

[저자 원문](https://proceedings.mlr.press/v205/ichter23a.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Embodiment/environment | The robot interacts with a large portion of the kitchen environment and successfully performs sequences of manipulation and navigation skills. | hardware/simulator version and reset protocol | p. 7 (5.1 Results), p. 7 (5.1 Results) |
| Dataset/benchmark | This requires long-horizon reasoning over a required order, an abstract understanding of the instruction, and knowledge of both the environment and robot's capabilities. | role, split, size and leakage | p. 7 (5.1 Results), p. 7 (5.1 Results), p. 8 (5.1 Results), p. 11 (5.1 Results) |
| Metric | Table 2: Success rates of instructions by family. PaLM-SayCan achieves a planning success rate of 84% and execution success rate of 74% in the training environment and 81% planning and 60% execution ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 33 (Figure/Table caption), p. 9 (5.1 Results) |
| Baseline/ablation | We also find that PaLM outperforms FLAN. | fair input/data/compute/action matching | p. 9 (5.1 Results), p. 9 (5.1 Results), p. 29 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 12 / 7 Related Work - extractive body cue:** Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation.
- **p. 12 / 7 Related Work - extractive body cue:** 8 Conclusions, Limitations and Future Work We presented SayCan, a method that enables leveraging and grounding the rich knowledge in large language models to complete ...
- **p. 7 / 5.1 Results - extractive body cue:** Appendix E.6 shows additional rollouts with complex decisions, embodiment grounding, and long-horizon tasks in Figures 14-17 as well as failures in Figure 16.
- **p. 8 / 5.1 Results - extractive body cue:** Overall, 65% of the errors were LLM failures and 35% were affordance failures.
- **p. 8 / 5.1 Results - extractive body cue:** The embodiment tasks were planned correctly 64% of the time, generally with failures as a result of affordance function misclassification.
- **p. 10 / 5.1 Results - extractive body cue:** Over 21 queries we found a planning rate of 100% and an execution rate of 33% (due to failures of the chained manipulation policy), with ...
- **p. 30 / Figure/Table caption - extractive body cue:** Table 8: Multilingual queries plan success rate. instruction 4-12 are the Chinese, French and Spanish translation of first 3 queries. E.6 Additional Results Additional results ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 11 (5.1 Results), p. 3 (2 Preliminaries), p. 7 (5.1 Results), p. 1 (Abstract)이다.
