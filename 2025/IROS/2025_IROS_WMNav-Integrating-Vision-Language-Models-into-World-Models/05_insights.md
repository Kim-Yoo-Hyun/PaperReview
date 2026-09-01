# Insights — WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.02247; PDF retrieval source: https://arxiv.org/pdf/2503.02247. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** In our framework, the world model consists of PredictVLM and the memory constructed by curiosity value map and cost.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the key insight that VLMs inherently encode comprehensive knowledge about indoor layout and spatial relationships of objects, we propose WMNav as shown in ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** To guide the VLM to make reasonable predictions about the indoor scene, we design a novel prompting strategy as illustrated in Figure 3 (a).
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** Then, the direction in the panoramic image with the highest score is selected and sent to the navigation policy module.
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** Then M cv t (st in Figure 2) is updated by combining M nav t with the curiosity value map in the previous step M ...
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** Then, actions falling within explored regions are filtered out based on the exploration state map, and the action sequence is further refined by limiting the ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 3 (III. WMNAV APPROACH), p. 2 (I. INTRODUCTION), p. 3 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, due to the limited field of view of egocentric images, capturing environmental information outside the immediate perspective remains a significant challenge.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the true challenge lies in creating a versatile world model that can faithfully capture the landscape of an indoor environment.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The primary difficulty in ZSON stems from the need to employ broad semantic knowledge to direct movement with optimal efficiency while precisely identifying previously unencountered ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Still, it uses BLIP-2[15], which pays more attention to the relevance of image-text pairs and has limited interaction and reasoning capabilities, which makes it difficult ...
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** If there is no sofa, then return failure message.
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the VLM to estimate the stopping condition directly ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** But textual information cannot accurately describe the spatial relationships in the scene, and it is difficult for LLM to make good spatial decisions.
- **Boundary to test:** If there is no sofa, then return failure message.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and novel modules. ... | p. 2 (I. INTRODUCTION), p. 3 (III. WMNAV APPROACH) |
| Reported outcome | Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Failure/limitation | If there is no sofa, then return failure message. | p. 5 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and novel modules. ...를 Choose your action from the image prompt.' Image Prompt Exploration Stage Action VLM Update Navigable Area Candidate Actions Initial Actions Exploration State Map Filter 2 1 2 3 4 5 6 7 ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 If there is no sofa, then return failure message.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and novel modules. ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Vision-Language Model, Navigation, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RoboDreamer: Learning Compositional World Models for Robot Imagination (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** If there is no sofa, then return failure message.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Datasets and Evaluation Metrics Datasets The HM3D v0.1 [38] is used in the Habitat 2022 ObjectNav challenge, providing 2000 validation episodes on 20 validation environments with 6 goal object categories..
3. Compare against the body-reported baseline or a matched simpler baseline: Memory SD TAP SR(%)↑SPL(%)↑ a No ✗ ✗ 65.8 25.8 b No ✓ ✗ 67.4 33.1 c Text-Image ✓ ✗ 62.0 29.6 d CVM(Ours) ✗ ✗ 69.5 34.9 e CVM(Ours) ✓ ✗ ....
4. Report the body metric and its denominator/aggregation: Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics..
5. Re-run the body-reported ablation/failure condition: As shown in TABLE II: Ablation study of different modules and memory strategies on HM3D v0.2 [38]..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH); the primary result is directionally consistent at p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 3 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 Memory SD TAP SR(%)↑SPL(%)↑ a No ✗ ✗ 65.8 25.8 b No ✓ ✗ 67.4 33.1 ... 대비 Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation ...을 개선하고, If there is no sofa, then return failure message. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
