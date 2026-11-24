# SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2312.01990.
> PDF retrieval source: https://arxiv.org/pdf/2312.01990. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICRA
- Authors: Isabel Leal, Krzysztof Choromanski, Deepali Jain, Avinava Dubey, Jake Varley, Michael Ryoo, Yao Lu, Frederick Liu, Vikas Sindhwani, Quan Vuong, Tamas Sarlos, Ken Oslund, Karol Hausman, Kanishka Rao
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, robot policy, efficient attention, manipulation
- Official paper: https://arxiv.org/abs/2312.01990
- Full-text retrieval: https://arxiv.org/pdf/2312.01990
- Code/Project: https://deepmind.google/discover/blog/shaping-the-future-of-advanced-robotics/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

SARA-RT는 이미 학습한 로봇 트랜스포머의 어텐션을 선형 계산 형태로 바꾸고 미세조정해 추론 부담을 낮춘다. [PDF 1쪽](https://arxiv.org/pdf/2312.01990v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot ...
- **p. 1 / Abstract - extractive body cue:** SARA-RT relies on the new method of fine-tuning proposed by us, called up-training.
- **p. 1 / Abstract - extractive body cue:** It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterpart ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models [1], the first VLA robotic policies pre-trained on ...
- **p. 1 / Abstract - extractive body cue:** We complement our results with the rigorous mathematical analysis providing deeper insight into the phenomenon of SARA.
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** Besides, linear attention usually produces some performance gap as compared to its brute-force softmax counterpart.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Since Point Cloud Transformers ([2]) usually use relatively long 1K+ sequences, even for simple objects, the unscalability of the brute-force quadratic attention is a severe ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot ...
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** 2 (blue- and brown-border boxes), this modification enables both the ReLU and exp variants to reach their targets with no distractions and furthermore already leads ...
- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** First we show that vision-language (VL) models can be used in a zero-shot manner for steering the agent.
- **p. 3 / III. THE MATHEMATICS OF SARA-RTS - extractive body cue:** As a warm-up, we show that a linear attention mechanism using ϕrandom exp : RdQK →Rm leads to the unbiased
- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** Developing intuition: zero-shot navigation via VL models Consider a vision-based VR navigation agent, conditioned on the images of the target objects: t1, ..., tM or ...
- **p. 1 / Abstract - extractive body cue:** It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterpart ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models [1], the first VLA robotic policies pre-trained on ...
- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** We consider a purely zero-shot attention-based control mechanism, where the action ai of the agent corresponding to the particular target ti (i = 1, ..., ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We consider a purely zero-shot attention-based control mechanism, where the action ai of the agent corresponding to the particular target ti (i = 1, ..., M) is defined as follows: ( ai ... | multi-view observation, language/task label과 action trajectory | p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 1 (Body text (section not recovered)) |
| State/latent | consider, purely, zero-shot, attention-based, control, mechanism, where, action, agent, corresponding, particular, target | shared representation, embodiment/task identity와 data distribution | p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) |
| Output/action | The manipulation policy is conditioned on the text instruction. | dataset sample 또는 learned policy action | p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA) |
| Objective/outcome | Denote by pϵ the probability of an event E(ϵ) = {∃i,j/bK(qi, kj) -K(qi, kj)/ > ϵK(qi, kj)}. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 4 (III. THE MATHEMATICS OF SARA-RTS), p. 4 (III. THE MATHEMATICS OF SARA-RTS) |

## Main Claims and Actual Contribution

- 커널 특징을 사용해 쿼리·키의 모든 쌍을 직접 계산하는 연산 순서를 바꾸는 방법을 제시한다. [PDF 3쪽](https://arxiv.org/pdf/2312.01990v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2312.01990v1#page=4)
- RT-2 계열을 이용한 로봇 정책 평가와 점군 입력 정책 실험으로 변환 후의 품질과 실행 비용을 비교한다. [PDF 4쪽](https://arxiv.org/pdf/2312.01990v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2312.01990v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2312.01990v1#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Embodiment/environment | It consists of expert demonstrations collected with a mobile manipulation robot. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | Robotic Point Cloud Transformers In our first set of experiments, we trained robotic grasping Transformer policies operating on the point cloud (PC) data. | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | 3: The simulator used to train PC-input grasping policies and the successful coke can grasp with corresponding reward r = 1. iterations iterations iterations iterations reward reward iterations Fig. | definition, denominator, direction and uncertainty | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption) |
| Baseline/ablation | Thus we chose (here and for the RT-2 experiments) the simplest ReLU (that can be thought of as the tamed version of the exp variant), on-robot deployed it and compared with the ... | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The agent gets a binary reward r ∈{0, 1} for each grasp (success or failure).
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: VR navigation via VL attention models on Matterport environments ([21]). The top-down view of the scene is in the lower-left corner. The agent's ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this work, we chose the former, leaving testing the latter to future work.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** SARA remains a feasible approach even for high resolution images, while the regular variant does not.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We plan to exercise this feature of SARA by using much higher resolution images (a challenge for regular RT-2 models) in future work.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Robotics Transformer policies obtained via Self-Adaptive Robust Attention (SARA) in action for three different modalities: vision, language and point clouds and varying sequence ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Abstract), p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 4 (IV. EXPERIMENTS), p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA)이다.
