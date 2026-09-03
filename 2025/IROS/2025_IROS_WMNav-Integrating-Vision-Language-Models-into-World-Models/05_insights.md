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

- **Paper-specific interface:** At each time step t, the panoramic image Ipan t is input to PredictVLM, which outputs scores Scoret for each direction in the current panoramic view: Scoret = PredictV LM(Ipan ... (p. 4, III. WMNAV APPROACH).
- **Paper-specific mechanism:** Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and ... (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Memory SD TAP SR(%)↑SPL(%)↑ a No ✗ ✗ 65.8 25.8 b No ✓ ✗ 67.4 33.1 c Text-Image ✓ ✗ 62.0 29.6 d CVM(Ours) ✗ ✗ 69.5 34.9 e CVM(Ours) ... (p. 6, IV. EXPERIMENTS); the relevant task/metric cue is Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics. (p. 6, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the VLM to estimate the stopping condition directly from the observed image. (p. 5, III. WMNAV APPROACH).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Vision-Language Model, Navigation, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RoboDreamer: Learning Compositional World Models for Robot Imagination (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** If there is no sofa, then return failure message.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: At each time step t, the panoramic image Ipan t is input to PredictVLM, which outputs scores Scoret for each direction in the current panoramic view: Scoret = PredictV LM(Ipan ... (p. 4, III. WMNAV APPROACH); preserve the objective/update rule: Then M cv t (st in Figure 2) is updated by combining M nav t with the curiosity value map in the previous step M cv t-1 (st-1 in Figure ... (p. 4, III. WMNAV APPROACH).
2. Use the paper-reported task/data/environment cue: Datasets and Evaluation Metrics Datasets The HM3D v0.1 [38] is used in the Habitat 2022 ObjectNav challenge, providing 2000 validation episodes on 20 validation environments with 6 goal object categories. (p. 6, IV. EXPERIMENTS).
3. Compare against the reported or matched baseline: Memory SD TAP SR(%)↑SPL(%)↑ a No ✗ ✗ 65.8 25.8 b No ✓ ✗ 67.4 33.1 c Text-Image ✓ ✗ 62.0 29.6 d CVM(Ours) ✗ ✗ 69.5 34.9 e CVM(Ours) ... (p. 6, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics. (p. 6, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: As shown in TABLE II: Ablation study of different modules and memory strategies on HM3D v0.2 [38]. (p. 6, IV. EXPERIMENTS); if none is reported, design one around: 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the VLM to estimate the stopping condition directly from the observed image. (p. 5, III. WMNAV APPROACH).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 3 (III. WMNAV APPROACH), match the reported outcome at p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), and measure the boundary at p. 5 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH).

## Falsifiable research question

Under the paper's stated interface (At each time step t, the panoramic image Ipan t is input to PredictVLM, which outputs scores Scoret for each direction in ...), does the paper-specific mechanism (Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment ...) retain the reported evaluation outcome (Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation ...) when tested against the paper's strongest explicit boundary (2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and ... (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Memory SD TAP SR(%)↑SPL(%)↑ a No ✗ ✗ 65.8 25.8 b No ✓ ✗ 67.4 33.1 c Text-Image ✓ ✗ 62.0 29.6 d CVM(Ours) ✗ ✗ 69.5 34.9 e CVM(Ours) ... (p. 6, IV. EXPERIMENTS).
- **Strongest explicit boundary:** 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the VLM to estimate the stopping condition directly from the observed image. (p. 5, III. WMNAV APPROACH).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
