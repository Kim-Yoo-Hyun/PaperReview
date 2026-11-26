# Training language models to follow instructions with human feedback

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (68 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2203.02155.
> PDF retrieval source: https://arxiv.org/pdf/2203.02155. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / NeurIPS
- Authors: Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F. Christiano, Jan Leike, Ryan Lowe
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: LLM, instruction tuning, alignment, Reinforcement Learning
- Official paper: https://arxiv.org/abs/2203.02155
- Full-text retrieval: https://arxiv.org/pdf/2203.02155
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (68 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

InstructGPT는 사람의 시범 답변과 여러 답변에 매긴 선호 순위를 이용해 GPT-3의 지시 수행을 미세조정한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Making language models bigger does not inherently make them better at following a user's intent.
- **p. 1 / Abstract - extractive body cue:** For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user.
- **p. 1 / Abstract - extractive body cue:** In other words, these models are not aligned with their users.
- **p. 1 / Abstract - extractive body cue:** In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.
- **p. 1 / Abstract - extractive body cue:** Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model ...
- **p. 4 / 1 Introduction - extractive body cue:** Finally we give an extended discussion of our work in Section 5, including implications for alignment research (5.1), what we are aligning to (5.2), limitations ...
- **p. 1 / 1 Introduction - extractive body cue:** Current affiliations: AA: Anthropic; PC: Alignment Research Center.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** See Section 3 for more details on our method. sizes (1.3B, 6B, and 175B parameters), and all of our models use the GPT-3 architecture.
- **p. 4 / 1 Introduction - extractive body cue:** The rest of this paper is structured as follows: We first detail related work in Section 2, before diving into our method and experiment details ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.
- **p. 1 / Abstract - extractive body cue:** We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.
- **p. 2 / 1 Introduction - extractive body cue:** We mainly evaluate our models by having our labelers rate the quality of model outputs on our test set, consisting of prompts from held-out customers ...
- **p. 2 / 1 Introduction - extractive body cue:** Our InstructGPT models (PPO-ptx) as well as its variant trained without pretraining mix (PPO) significantly outperform the GPT-3 baselines (GPT, GPT prompted); outputs from our ...
- **p. 4 / 1 Introduction - extractive body cue:** To test the generalization of our models, we conduct a preliminary experiment with held-out labelers, and find that they prefer InstructGPT outputs to outputs from ...
- **p. 1 / Abstract - extractive body cue:** Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Training language models to follow instructions with human feedback Long Ouyang∗ Jeff Wu∗ Xu Jiang∗ Diogo Almeida∗ Carroll L. | 논문이 명시한 observation과 task input | p. 1 (Body text (section not recovered)), p. 1 (Abstract) |
| State/latent | Training, language, models, follow, instructions, human, feedback, Long, Ouyang, Jeff, Jiang, Diogo | task state 또는 decision variable | p. 1 (Body text (section not recovered)), p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/action | We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. | paper-specific output/action | p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | Finally, we use this RM as a reward function and fine-tune our supervised learning baseline to maximize this reward using the PPO algorithm (Schulman et al., 2017). | primary task objective와 closed-loop behavior | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 시범 답변으로 지도학습한 뒤 선호 순위로 보상 모형을 학습하고 이를 PPO 정책 갱신에 사용한다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf#page=5)
- 논문이 수집한 프롬프트의 사람 평가에서 1.3B InstructGPT의 답변이 기본 175B GPT-3의 답변보다 선호됐다. [PDF 2쪽](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf#page=2) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 13 (4 Results), p. 12 (4 Results) |
| Embodiment/environment | Second, it can be difficult for public NLP datasets to obtain a very high diversity of inputs (at least, on the kinds of inputs that real-world users would be interested in using). | hardware/simulator version and reset protocol | p. 13 (4 Results), p. 12 (4 Results) |
| Dataset/benchmark | First, public NLP datasets are designed to capture tasks that are easy to evaluate with automatic metrics, such as classification, question answering, and to a certain extent summarization and translation. | role, split, size and leakage | p. 13 (4 Results), p. 12 (4 Results), p. 13 (4 Results), p. 15 (4 Results) |
| Metric | Figure 13: Tuning FLAN and T0 based on reward model scores batch size of 64, a learning rate of 6e-6 and 1 million examples. Once again using the reward model score, we ... | definition, denominator, direction and uncertainty | p. 43 (Figure/Table caption), p. 57 (Figure/Table caption), p. 14 (4 Results) |
| Baseline/ablation | Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those from the 175B SFT model. Our InstructGPT models ... | fair input/data/compute/action matching | p. 2 (Figure/Table caption), p. 12 (4 Results), p. 11 (4 Results) |

## Explicit Limitations and Failure Boundary

- **p. 20 / 5 Discussion - extractive body cue:** In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations.
- **p. 18 / 5 Discussion - extractive body cue:** We then consider areas for improvement before a larger discussion of the limitations of our work in Section 5.3.
- **p. 18 / 5 Discussion - extractive body cue:** the real world with customers.10 This enables an important feedback loop on the techniques' effectiveness and limitations.
- **p. 19 / 5 Discussion - extractive body cue:** Perhaps the greatest limitation of our models is that, in most cases, they follow the user's instruction, even if that could lead to harm in ...
- **p. 17 / 5 Discussion - extractive body cue:** However, our approach does provides us with a clear empirical feedback loop of what works and what does not.
- **p. 20 / 5 Discussion - extractive body cue:** Our proposal for mitigating the alignment tax, by incorporating pretraining data into RLHF finetuning, does not completely mitigate performance regressions, and may make certain undesirable ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Labeler-collected metadata on the API distribution. Metadata Scale Overall quality Likert scale; 1-7 Fails to follow the correct instruction / task Binary Inappropriate ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 4 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction)이다.
