# Vision-Language Foundation Models as Effective Robot Imitators

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/71639c317fb0bf398835627b4418693e-Abstract-Conference.html.
> PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICLR
- Authors: Xinghang Li, Minghuan Liu, Hanbo Zhang, Cunjun Yu, Jie Xu, Hongtao Wu, Chilam Cheang, Ya Jing, Weinan Zhang, Huaping Liu, Hang Li, Tao Kong
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, VLM, Imitation Learning, language-conditioned manipulation, policy head
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2024/hash/71639c317fb0bf398835627b4418693e-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf
- Code/Project: https://github.com/RoboFlamingo/RoboFlamingo
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RoboFlamingo는 OpenFlamingo로 현재 영상과 지시를 해석하고 별도 정책 헤드로 이력을 처리해 언어 조건부 조작을 모방학습한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Recent progress in vision language foundation models has shown their ability to understand multimodal data and resolve complicated vision language tasks, including robotics manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** We seek a way of making use of existing vision-language models (VLMs) with fine-tuning on robotics data.
- **p. 1 / ABSTRACT - extractive body cue:** To this end, we derive a simple and novel vision-language manipulation framework, dubbed RoboFlamingo, built upon the open-source VLMs, OpenFlamingo.
- **p. 1 / ABSTRACT - extractive body cue:** Unlike prior works, RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly finetuned by ...
- **p. 1 / ABSTRACT - extractive body cue:** Such a decomposition provides RoboFlamingo the flexibility for open-loop control and deployment on low-performance platforms.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, democratizing such an expensive framework for all robotics practitioners proves difficult as it utilizes private models and necessitates †
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While there have been some previous studies that incorporated large language models (LLMs) and vision-language models (VLMs) into robot systems as high-level planners (Ahn et ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we introduce RoboFlamingo, a novel vision-language manipulation framework that leverages publicly accessible pre-trained VLMs to effectively construct manipulation policies for robotics.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Consequently, there is an urgent need for robot communities to have a low-cost alternative solution that effectively enables a robot manipulation policy with VLMs.
- **p. 4 / 3 BACKGROUND - extractive body cue:** It consists of a backbone based on Flamingo fθ and a policy head pθ.
- **p. 5 / 3 BACKGROUND - extractive body cue:** Specifically, the decoder consists of L layers, each of which involves a transformer decoder layer and a cross-attention layer.
- **p. 5 / 3 BACKGROUND - extractive body cue:** 4.2.1 VISION ENCODER The vision encoder consists of a vision transformer (ViT) (Yuan et al., 2021) and a perceiver resampler (Alayrac et al., 2022).
- **p. 8 / 2) Does vision-language (VL) pre-training improve downstream robotic tasks? - extractive body cue:** (b) MLP w hist takes the history frames into the vision encoder with position embedding, and encodes the history information through the cross-attention layers in ...
- **p. 8 / 2) Does vision-language (VL) pre-training improve downstream robotic tasks? - extractive body cue:** To verify the necessity of VL pre-training, we train the same model without loading the pre-trained parameters of the cross-attention layers and the resampler trained ...
- **p. 9 / 2) Does vision-language (VL) pre-training improve downstream robotic tasks? - extractive body cue:** 5.5 FLEXIBILITY OF DEPLOYMENT Since our RoboFlamingo adopts a structure that separates the perception and policy module and leaves the main computation on the perception ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 4.3 POLICY HEAD The output XL t from the feature fusion decoder is trained as the representation of the vision observation and language instruction, which will be further translated into low-level control ... | image/video, language instruction, proprioception과 history | p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND) |
| State/latent | POLICY, HEAD, output, feature, fusion, decoder, trained, representation, vision, observation, language, instruction | language-grounded task state와 action-policy context | p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND), p. 4 (3 BACKGROUND) |
| Output/action | It addresses three main challenges: 1) it adapts vision-language models with static image inputs to video observations; 2) it generates robot control signals instead of text-only outputs; 3) it requires a limited ... | continuous action, pose 또는 action chunk | p. 4 (3 BACKGROUND), p. 4 (3 BACKGROUND), p. 2 (1 INTRODUCTION) |
| Objective/outcome | To our delight, recent progress on large-scale real robotics data (Padalkar et al., 2023) has shown the potential of fine-tuning large VLMs for real robots, and the most exciting future work is ... | instruction following, task success, generalization과 latency | p. 9 (2) Does vision-language (VL) pre-training improve downstream robotic tasks?) |

## Main Claims and Actual Contribution

- 시각언어 백본과 순차 행동 헤드를 분리해 현재 관측의 표현을 과거 상태와 결합한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf#page=4) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf#page=6)
- CALVIN에서 사전학습 백본과 행동 헤드의 선택이 장기 조작 수행에 미치는 영향을 비교했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf#page=6) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (5 EXPERIMENTS), p. 8 (Figure/Table caption) |
| Embodiment/environment | 5.1 BENCHMARK AND BASELINES We choose CALVIN (Mees et al., 2022b), an open-source simulated benchmark to learn long-horizon language-conditioned tasks, as our testbed, and the corresponding datasets as our imitation learning demonstrati ... | hardware/simulator version and reset protocol | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Dataset/benchmark | 5.2 IMITATION PERFORMANCE We train RoboFlamingo (with the M-3B-IFT backbone) using demonstrations only with language annotation from all 4 splits (A, B, C, and D), and evaluate the imitation performance on episodes ... | role, split, size and leakage | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Metric | Among all methods, RoboFlamingo achieves the highest success rate over the latter tasks. | definition, denominator, direction and uncertainty | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Baseline/ablation | Our method exhibits superior performance compared to all baselines in this language generalization setting. | fair input/data/compute/action matching | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 2) Does vision-language (VL) pre-training improve downstream robotic tasks? - extractive body cue:** We hypothesize that this may stem from the fact that the VLM (OpenFlamingo) has only seen image-text pairs during pre-training and cannot process consequent frames ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8: The performance of VLMs at each epoch on ABC →D split. B.5 QUALITATIVE EXAMPLES We visualize the task frames and analyze how RoboFlamingo ...
- **p. 9 / 2) Does vision-language (VL) pre-training improve downstream robotic tasks? - extractive body cue:** Due to the lack of real-robot data, this paper does not deploy on real-world robotics.
- **p. 9 / 2) Does vision-language (VL) pre-training improve downstream robotic tasks? - extractive body cue:** 6 CONCLUSION AND FUTURE WORK This paper explores the potential of pre-trained vision-language models in advancing languageconditioned robotic manipulation.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 8 (2) Does vision-language (VL) pre-training improve downstream robotic tasks?)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, democratizing such an expensive framework for all robotics practitioners proves difficult as it utilizes private models and necessitates † (p. 1, 1 INTRODUCTION).
- **Actual contribution:** To this end, we introduce RoboFlamingo, a novel vision-language manipulation framework that leverages publicly accessible pre-trained VLMs to effectively construct manipulation policies for robotics. (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Figure 3: Ablation studies on the ABCD →D setting. Note that the success rate of RoboFlamingo on subsequent tasks dropped more than HULC does. This may be due to our ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** RoboFlamingo only takes a dozen steps to locate and move to the top of the drawer, and simultaneously releases the gripper to complete the task; while HULC keeps moving above ... (p. 16, B.5 QUALITATIVE EXAMPLES).
