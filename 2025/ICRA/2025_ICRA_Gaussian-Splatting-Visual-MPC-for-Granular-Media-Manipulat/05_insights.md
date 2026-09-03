# Insights — Gaussian Splatting Visual MPC for Granular Media Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2410.09740v3. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / IV. OUR APPROACH - extractive body cue:** We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their Gaussian splatting ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our contribution: We use the Gaussian splats representing the scene at each time as a state vector that can be manipulated via MPC, effectively lowering ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our model successfully enables solutions of complex planning tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This representation enables robots to optimize their actions, anticipate challenges, and adapt to dynamic environments.
- **p. 3 / IV. OUR APPROACH - extractive body cue:** The trajectory optimization problem over a horizon T can be defined as follows: u0:T-1 = argminu0:T-1c(ZT,Ztarget) (6) Z0 = h(O0), Ztarget = h(Otarget), Zt+1 = ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** In the end, we obtain a set of Gaussians that represents the next image: ˆZt+1 = {(ci t,αi t , ˆR i t+1, ˆgi t+1,si ...
- **Contribution anchor:** p. 3 (IV. OUR APPROACH), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. OUR APPROACH)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these models often underperform compared to linear dynamics models due to a lack of inductive biases.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Several factors contribute to the difficulty of granular material manipulation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This representation enables robots to optimize their actions, anticipate challenges, and adapt to dynamic environments.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furthermore, we highlight its generalization capability by transferring a trained model to new environments with varying object shapes in a zero-shot setting.
- **p. 6 / VI. LIMITATIONS - extractive body cue:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales.
- **p. 6 / VII. CONCLUSION - extractive body cue:** Future work could extend this framework to other non-rigid materials, further enhancing the capabilities of robotic systems in dynamic tasks.
- **Boundary to test:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder fenc with node representation ¯vi from vi ... | p. 3 (IV. OUR APPROACH), p. 1 (I. INTRODUCTION) |
| Reported outcome | Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 0.67 NFD [29] 0.89 0.74 0.46 DVF [17] ... | p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Failure/limitation | This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales. | p. 6 (VI. LIMITATIONS), p. 6 (VII. CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Problem Formulation Given multi-view RGBD observations Otarget = {ov,mv}N v=1 of the target pattern of the granular material, where ov represents the RGBD image and mv indicates the corresponding camera ... (p. 3, IV. OUR APPROACH).
- **Paper-specific mechanism:** Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their Gaussian splatting representation, (b) learns a dynamics ... (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 0.67 NFD [29] 0.89 0.74 0.46 ... (p. 5, V. EXPERIMENTAL RESULTS); the relevant task/metric cue is We use two metrics to evaluate the frameworks. • Success rate: success is defined as moving all materials to the target region. • State error: in simulation experiments, we also ... (p. 5, V. EXPERIMENTAL RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales. (p. 6, VI. LIMITATIONS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Problem Formulation Given multi-view RGBD observations Otarget = {ov,mv}N v=1 of the target pattern of the granular material, where ov represents the RGBD image and mv indicates the corresponding camera ... (p. 3, IV. OUR APPROACH); preserve the objective/update rule: We perform the optimization shown in Equation 6 as part of a gradient-based MPC loop (as shown in Alg. (p. 4, IV. OUR APPROACH).
2. Use the paper-reported task/data/environment cue: (b) The granular materials used in real-world experiments include coffee beans, peanuts, pistachios, and almonds. transfer our model trained in the simulation environment to our real-world experiment setup. (p. 4, V. EXPERIMENTAL RESULTS).
3. Compare against the reported or matched baseline: Our approach demonstrates superior generalization compared to other baselines. (p. 6, V. EXPERIMENTAL RESULTS).
4. Report the body metric with its denominator and aggregation: We use two metrics to evaluate the frameworks. • Success rate: success is defined as moving all materials to the target region. • State error: in simulation experiments, we also ... (p. 5, V. EXPERIMENTAL RESULTS).
5. Re-run the reported ablation or stress/failure condition: Generalization Studies In this section, we conduct ablation studies to evaluate the effectiveness of each component. (p. 5, V. EXPERIMENTAL RESULTS); if none is reported, design one around: This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales. (p. 6, VI. LIMITATIONS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), and measure the boundary at p. 6 (VI. LIMITATIONS), p. 5 (V. EXPERIMENTAL RESULTS).

## Falsifiable research question

Under the paper's stated interface (Problem Formulation Given multi-view RGBD observations Otarget = {ov,mv}N v=1 of the target pattern of the granular material, where ov represents the ...), does the paper-specific mechanism (Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into ...) retain the reported evaluation outcome (We use two metrics to evaluate the frameworks. • Success rate: success is defined as moving all materials ...) when tested against the paper's strongest explicit boundary (This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We use two metrics to evaluate the frameworks. • Success rate: success is defined as moving all materials ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their Gaussian splatting representation, (b) learns a dynamics ... (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 0.67 NFD [29] 0.89 0.74 0.46 ... (p. 5, V. EXPERIMENTAL RESULTS).
- **Strongest explicit boundary:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales. (p. 6, VI. LIMITATIONS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
