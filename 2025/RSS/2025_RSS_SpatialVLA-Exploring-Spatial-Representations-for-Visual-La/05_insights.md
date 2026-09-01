# Insights — SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p011.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p011.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** OpenVLA [30] adopts a similar action discretization approach and fine-tune Prismatic VLM [28] only on the OXE dataset [13], which consists of robot data from ...
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** ‘To obtain a generalist robot policy model, the training procedure of SpatialVLA consists of pre-training stage and posttraining stage.
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** space consists Of Myax = Mg *Mo ~M,. diserete spatial stids Ons = {2,...a%}, Similarly, there are Myr = Meat » Myick *Myaw 3D discrete ...
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** 2, SpatialVLA is developed based on a vision-language model to inherit the general world knowledge.
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** During training, SpatialVLA model is trained to take the ego3D position encoding representation Ogq and natural language task instruction Las inputs, and autoregressively generate spatial ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** In detail, we ft a new Gaussian distribution AV (jig, Yacw) for each action variable on posttraining datasets and create discrete spatial action grids Gey ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (B. The Pre-training and Post-training Scheme), p. 4 (A. The SpatialVLA Model Architecture), p. 3 (A. The SpatialVLA Model Architecture), p. 3 (A. The SpatialVLA Model Architecture)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, developing such generalist robot policies with 3D spatial intelligence encounters two primary challenges in the aspects of robot observation and action.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Secondly, different robots have different action movement characteristics to accomplish diverse tasks, due to different degrees of freedom, motion controllers, workspace configurations, and task complexity, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The key to the success of this paradigm lies in adapting the generalization power of VLMs to numerous robot manipulation tasks, as well
- **p. 7 / 10 Ablations on Design - extractive body cue:** However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently encountering issues like object nisidentfication and grasp ...
- **p. 7 / 10 Ablations on Design - extractive body cue:** Compared to OpenVLA, ‘our method demonstrates superior robustness in handling motion disturbances (human-induced dynamic object movement in tasks #3 and #4), successfully tracking and grasping ...
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** To assess the robustness of Spatial VLA in diverse environmental variations, we employ the SimplerEnv simulation benchmark [35] to evaluate visual ‘matching and variant aggregation ...
- **p. 6 / 10 Ablations on Design - extractive body cue:** Qualitatively, we find that SpatialVLA exhibits greater generalizability and robustness across diverse robotic manipulation tasks and environmental
- **Boundary to test:** However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently encountering issues like object nisidentfication and grasp failures.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on Ego3D Posi tion Encoding and Adaptive Action ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Spatial VLA achieves the highest average success rate, outperforming all generalist manipulation policies. | p. 7 (10 Ablations on Design), p. 9 (B. Adapting to New Robot Setups) |
| Failure/limitation | However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently encountering issues like object nisidentfication and grasp failures. | p. 7 (10 Ablations on Design), p. 7 (10 Ablations on Design) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 We find that the proposed model Spatial VLA bridges observation inputs and aetion outputs in a universal robot-agnostic manner, which explores powerful 3D spatial-aware representations to enhance the VLA model.를 In this work, as illustrated in Fig. /, we propose a generalist robot policy SpatialVLA, which equips the VLA model with 3D spatial intelligence by exploring aligned spatial representations of robot observation ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently encountering issues like object nisidentfication and grasp failures.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on Ego3D Posi tion Encoding and Adaptive Action ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Robotics, 3D spatial representation, action representation, cross-embodiment, robot data`.
- **Reading predecessor in the generated track queue:** VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently encountering issues like object nisidentfication and grasp failures.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We train SpatialVLA from Paligemma2 backbone [62] on a cross-robot dataset mixture with 1.1 Million real robot demonstrations {615 Gu}> covering a diverse range of robot embodiments, scenes, and tasks, This pre-training ....
3. Compare against the body-reported baseline or a matched simpler baseline: In particular, SpatialVLA also matches or outperforms te latest SOTA model 7, Tab, I! summarizes the esults across different manipulation policies on the WidowX setup, Our model surpasses the state-of-the-art RoboVLM policy, ....
4. Report the body metric and its denominator/aggregation: We present the success rate (SR) and standard error for each method across four task suites, which are averaged over three random seeds with 500 trials..
5. Re-run the body-reported ablation/failure condition: On average, SpatialVLA achieves the highest overall visual matching and variant aggregation performance with a significant margin, Our SpatialVLA model yields 71.9% and 75.1% Visual Matching scores in zero-shot and fine-tuning. settings ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme), p. 4 (B. The Pre-training and Post-training Scheme); the primary result is directionally consistent at p. 7 (10 Ablations on Design), p. 9 (B. Adapting to New Robot Setups), p. 7 (10 Ablations on Design); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, consist mechanism이 In particular, SpatialVLA also matches or outperforms te latest SOTA model 7, Tab, I! summarizes the ... 대비 We present the success rate (SR) and standard error for each method across four task suites, which are ...을 개선하고, However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
