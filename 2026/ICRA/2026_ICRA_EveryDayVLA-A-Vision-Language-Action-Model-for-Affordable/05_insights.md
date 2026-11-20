# Insights — EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/icra57385.2026.11696905; PDF retrieval source: https://arxiv.org/pdf/2511.05397. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon).
- **p. 3 / III. METHOD - extractive body cue:** We term our method AdaHorizon, and find that it enables discrete actions to match or exceed the precision of continuous controls, even on dexterous tasks ...
- **p. 2 / III. METHOD - extractive body cue:** To further improve performance, we introduce a novel adaptive horizon module, allowing the
- **p. 3 / III. METHOD - extractive body cue:** To harness both strengths, we introduce a more robust uncertainty metric: the mean absolute difference between the continuous and discrete action predictions, which outperforms the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet, even with internet-scale pretraining, they remain brittle under unfamiliar lighting [3], novel objects [4], and visual distractors [5], and often fail to generalize to ...
- **p. 2 / III. METHOD - extractive body cue:** Instead, EveryDayVLA takes advantage of action chunking, parallel decoding, and a collaborative training recipe, predicting discrete autoregressive and continuous action chunks, using an L1-regression objective, ...
- **원문 대조:** Discrete action에는 cross-entropy, continuous action에는 L1 loss를 사용하며 두 항을 결합해 학습한다. 식 (1)의 log 항은 예측한 discrete-action probability에 적용된다. ([PDF p. 3](https://arxiv.org/pdf/2511.05397#page=3), §III-A Collaborative Training, Eqs. (1)–(3)).
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon).
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet, even with internet-scale pretraining, they remain brittle under unfamiliar lighting [3], novel objects [4], and visual distractors [5], and often fail to generalize to ...
- **p. 6 / VI. CONCLUSIONS - extractive body cue:** We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well as relatively low number of expert demonstrations ...
- **p. 6 / V. RESULTS - extractive body cue:** The primary failure mode for EverydayVLA is delayed object release and not finishing the task in a timely manner.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. EveryDayVLA system. Top: EveryDayVLA finetunes a VLA for a low-cost manipulator to generate continuous and discrete actions, which are passed to an adaptive ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In real-world trials, we evaluate both in-distribution and out-of-distribution scenarios against OpenVLA and OpenVLA-OFT.
- **p. 5 / V. RESULTS - extractive body cue:** Method Inference Rate (Hz) ↑ Latency (sec) ↓ OpenVLA [19] 4.2 0.2396 OpenVLA-OFT [35] 109.7 0.0729 Oursli 54.2-108.4 0.0738 TABLE IV GENERALIZATION AND ROBUSTNESS TO ...
- **Boundary to test:** We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well as relatively low number of expert demonstrations in our finetuning dataset (compared to simulation).

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon). | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Reported outcome | For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared to continuous-action baselines. | p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS) |
| Failure/limitation | We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well as relatively low number of expert demonstrations in our finetuning dataset (compared to simulation). | p. 6 (VI. CONCLUSIONS), p. 6 (V. RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 EveryDayVLA EveryDayVLA ingests as input a demonstration consisting of an image observation ot and a language instruction lt.를 The VLA takes as input an image and natural language instruction and these are tokenized via the vision and language encoders, and sent to the Llama 2 LLM, which produces continuous and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well as relatively low number of expert demonstrations in our finetuning dataset (compared to simulation).에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well as relatively low number of expert demonstrations in our finetuning dataset (compared to simulation).; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Baselines On the LIBERO simulation benchmark, we report success rates across all four task suites, comparing against Diffusion Policy [3], Octo [5], DiT Policy [48], OpenVLA [19], and OpenVLA-OFT [35]..
3. Compare against the body-reported baseline or a matched simpler baseline: For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared to continuous-action baselines..
4. Report the body metric and its denominator/aggregation: For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared to continuous-action baselines..
5. Re-run the body-reported ablation/failure condition: Dataset We fine-tune the OpenVLA-7B model [19] on our custom dataset of 1,200 demonstrations-each pairing a naturallanguage instruction with an RGB observation sequence and corresponding end-effector poses-collected using our $300 manip ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD); the primary result is directionally consistent at p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, challenges, present mechanism이 For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields ... 대비 For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success ...을 개선하고, We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
