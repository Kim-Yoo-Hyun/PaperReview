# Insights — PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=AnofTirXgv; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/331054. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated modalities.
- **p. 2 / 1. Introduction - extractive body cue:** 2) Semantic-Geometric Collaboration: We propose PRISM, a unified framework that distills the rich physical common sense of 3D Visual Foundation Model to drive noise synthesis.
- **p. 3 / 3.1. Semantic-Physics Reasoner - extractive body cue:** The architecture consists of three sequential modules.
- **p. 3 / 3. Methodology - extractive body cue:** We present PRISM, a tripartite framework that synthesizes realistic depth by disentangling sensor noise into physically grounded modalities.
- **p. 5 / 3.4. Hierarchical Positive-Prioritized Supervision - extractive body cue:** To address the extreme class imbalance and ensure precise boundary detection, we propose a supervision strategy comprised of three coupled mechanisms.
- **p. 3 / 2.3. Visual Foundation Models as Semantic Priors - extractive body cue:** State-of-theart architectures like Metric3Dv2 (Hu et al., 2024) and MoGe (Wang et al., 2025b) employ ViT-based encoders to distill invariant geometric representations.
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive body cue:** Stage I: Noise Disentanglement Learning.In addition to the pixel-wise classification, we introduce a Dice Loss to enforce shape compactness and prevent trivial solutions.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Semantic-Physics Reasoner), p. 3 (3. Methodology), p. 5 (3.4. Hierarchical Positive-Prioritized Supervision), p. 3 (2.3. Visual Foundation Models as Semantic Priors)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, the deployment of simulation-trained policies remains fundamentally bottlenecked by the sim-to-real gap(Jia et al., 2025).
- **p. 1 / 1. Introduction - extractive body cue:** (a) The Reality Gap: Unlike pristine simulation, real-world physical sensing exhibits a bimodal noise distribution: black voids and gray residuals.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, training this framework presents a unique optimization challenge: invalidation regions are spatially sparse (often < 10% of pixels).
- **p. 2 / 1. Introduction - extractive body cue:** Unlike conventional hard example mining discards rare signals, H-PPS combines multi-scale boundary constraints with recall-prioritized mining protocol.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation ...
- **p. 9 / 7. Limitations - extractive body cue:** While PRISM demonstrates strong capabilities in simulateddepth enhancement, it possesses certain limitations.
- **p. 9 / 7. Limitations - extractive body cue:** Second, the current per-frame generation pipeline does not explicitly enforce temporal consistency for highly dynamic scenes, leaving flickering noise across frames as a key open ...
- **Boundary to test:** Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation (detection of sensor failure ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated modalities. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | By physically grounding noise synthesis, PRISM forces the policy to learn compliant behaviors robust to sensor dropouts (e.g., inferring geometry from boundaries), achieving an average success rate of 92.5% and significantly outperformi ... | p. 8 (5.3. Downstream Application Evaluation), p. 8 (Figure/Table caption) |
| Failure/limitation | Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation (detection of sensor failure ... | p. 7 (Figure/Table caption), p. 9 (7. Limitations) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Simulation) Task Language (Optional) <Enhanced Triplet> Enhanced Depth Simulated RGB Simulated State Large-scale Dataset from Simulation Simulated State Simulated RGB Simulated Depth Joint Gripper + (a) Large-scale Simulated Demonstrati ...를 The BND maps the concatenated RGB-Depth input X = [I; Dsim] ∈R4×H×W to a pixel-wise sensing invalidation probability map ˆ M ∈[0, 1]H×W .로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation (detection of sensor failure ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated modalities.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `semantic, alignment, depth, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation (detection of sensor failure ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We establish a benchmark of 6 diverse manipulation tasks (Tab.3) across two robotic platforms to evaluate challenging physical properties..
3. Compare against the body-reported baseline or a matched simpler baseline: Zero-shot evaluation on the NYU-Depth-v2 dataset (Tab.2) demonstrates PRISM's superior robustness under noisy domain shifts when compared to overfitting-prone baselines..
4. Report the body metric and its denominator/aggregation: NRG Only w/o SPR w/o BND PRISM Full 0.08 0.10 0.12 0.14 Overall MAE 0.118 0.095 0.098 0.076 -36% (i) Overall MAE NRG Only w/o SPR w/o BND PRISM Full 0.4 0.6 ....
5. Re-run the body-reported ablation/failure condition: Figure 7. Semantics Efficacy. Comparing generic vs. geometric priors. 3D VFMs show superior material awareness. Impact of Causal Architecture. We treat the diffusion-based NRG as the backbone and selectively remove components (Fig. ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.1. Semantic-Physics Reasoner), p. 3 (2.3. Visual Foundation Models as Semantic Priors), p. 5 (3) Sequential Optimization Objectives. Since PRISM is); the primary result is directionally consistent at p. 8 (5.3. Downstream Application Evaluation), p. 8 (Figure/Table caption), p. 7 (5.2. Depth Fidelity Evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 operationalize, insight, PRISM mechanism이 Zero-shot evaluation on the NYU-Depth-v2 dataset (Tab.2) demonstrates PRISM's superior robustness under noisy domain shifts when ... 대비 NRG Only w/o SPR w/o BND PRISM Full 0.08 0.10 0.12 0.14 Overall MAE 0.118 0.095 0.098 0.076 ...을 개선하고, Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
