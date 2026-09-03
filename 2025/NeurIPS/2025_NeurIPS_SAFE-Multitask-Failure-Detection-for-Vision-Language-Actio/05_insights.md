# Insights — SAFE: Multitask Failure Detection for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2025/file/392d0d05e2f514063e6ce6f8b370834c-Paper-Conference.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and ...
- **p. 2 / 1 Introduction - extractive body cue:** Based on this insight, we introduce SAFE, a ScAlable Failure Estimation method that scales across diverse tasks for generalist policies like VLAs.
- **p. 1 / 1 Introduction - extractive body cue:** VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, scaling up robot manipulation datasets has enabled the development of large visionlanguage-action (VLA) models, which are generalist manipulation policies that can follow language instructions ...
- **p. 5 / 4 Method - extractive body cue:** Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 ...
- **p. 4 / 4 Method - extractive body cue:** 4.1 Visual Analysis on VLA Latent Space VLAs process multi-modal inputs and extract rich semantic information in their internal feature space.
- **p. 4 / 4 Method - extractive body cue:** We study this hypothesis by visualizing the VLA features in Fig.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 5 (4 Method), p. 4 (4 Method)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, when VLAs are directly deployed on unseen tasks without collecting additional demonstrations and finetuning the model, they still suffer from limited success rates and ...
- **p. 1 / 1 Introduction - extractive body cue:** Most existing failure detection methods train a separate failure detector for each task, and evaluate the detector only on that task [8-17].
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we focus on the multitask failure detection problem.
- **p. 2 / 1 Introduction - extractive body cue:** To tackle this problem, we study the internal features of VLAs and find that they capture high-level knowledge about task success and failure.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the VLA is failing, the features, even those ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Failures detected by SAFE-LSTM align well with the actual robot failures, as shown in the corresponding camera observations from simulation experiments. The blue-shaded ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Failure detection results on simulation benchmarks, measured by area under ROC (ROC- AUC). "-" indicates that the failure detection method does not apply. ...
- **Boundary to test:** Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the VLA is failing, the features, even those from different tasks, fall into the same ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and environments, the internal features of the VLA ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | 75.54 53.93 82.37 70.00 Euclid. k-NN 80.35 60.27 72.01 53.64 Cosine k-NN 80.23 59.51 74.76 65.88 PCA-KMeans 49.98 51.03 75.62 47.22 RND 62.00 45.83 66.68 47.67 LogpZO 64.43 52.24 62.94 51.32 STAC-Single ... | p. 10 (6 Results), p. 10 (Figure/Table caption) |
| Failure/limitation | Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the VLA is failing, the features, even those from different tasks, fall into the same ... | p. 4 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 𝒆1 LSTM 𝑠1 𝒆2 LSTM ... (p. 5, 4 Method).
- **Paper-specific mechanism:** VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment. (p. 1, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 6: SAFE-MLP achieves the best failure detection performance in real-world experiments with both π0-FAST Franka and OpenVLA WidowX. Plot (a) presents quantitative results, while (b-e) show qualitative examples from ... (p. 10, Figure/Table caption); the relevant task/metric cue is We exclude the "pick up coke" task because π∗ 0 rarely fails on it (success rate at 98%). (p. 6, 5 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** This means that the human annotator does not think these rollouts are failures until the very last moment, where the VLA model is probably on the right track and fails ... (p. 28, C.3 Failure Detection Time).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, VLA, failure detection, conformal prediction, uncertainty`.
- **Reading predecessor in the generated track queue:** Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** WorldGym: World Model as An Environment for Policy Evaluation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the VLA is failing, the features, even those from different tasks, fall into the same ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 𝒆1 LSTM 𝑠1 𝒆2 LSTM ... (p. 5, 4 Method); preserve the objective/update rule: We study this hypothesis by visualizing the VLA features in Fig. (p. 4, 4 Method).
2. Use the paper-reported task/data/environment cue: Real-world WidowX Experiments: We also deploy the OpenVLA model pretrained on the "Open-X Magic Soup++" dataset [2] on a WidowX robot manipulator in our lab. (p. 6, 5 Experiments).
3. Compare against the reported or matched baseline: Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still achieving the best performance on seen tasks. (p. 9, 6 Results).
4. Report the body metric with its denominator and aggregation: We exclude the "pick up coke" task because π∗ 0 rarely fails on it (success rate at 98%). (p. 6, 5 Experiments).
5. Re-run the reported ablation or stress/failure condition: We exclude the "pick up coke" task because π∗ 0 rarely fails on it (success rate at 98%). (p. 6, 5 Experiments); if none is reported, design one around: This means that the human annotator does not think these rollouts are failures until the very last moment, where the VLA model is probably on the right track and fails ... (p. 28, C.3 Failure Detection Time).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 10 (Figure/Table caption), p. 27 (Figure/Table caption), p. 9 (6 Results), and measure the boundary at p. 28 (C.3 Failure Detection Time), p. 26 (C.1 Feature Visualization and Analysis).

## Falsifiable research question

Under the paper's stated interface (Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 ...), does the paper-specific mechanism (VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment.) retain the reported evaluation outcome (We exclude the "pick up coke" task because π∗ 0 rarely fails on it (success rate at 98%).) when tested against the paper's strongest explicit boundary (This means that the human annotator does not think these rollouts are failures until the very last moment, ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We exclude the "pick up coke" task because π∗ 0 rarely fails on it (success rate at 98%).) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (36 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment. (p. 1, 1 Introduction).
- **Paper-supported outcome:** Figure 6: SAFE-MLP achieves the best failure detection performance in real-world experiments with both π0-FAST Franka and OpenVLA WidowX. Plot (a) presents quantitative results, while (b-e) show qualitative examples from ... (p. 10, Figure/Table caption).
- **Strongest explicit boundary:** This means that the human annotator does not think these rollouts are failures until the very last moment, where the VLA model is probably on the right track and fails ... (p. 28, C.3 Failure Detection Time).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
