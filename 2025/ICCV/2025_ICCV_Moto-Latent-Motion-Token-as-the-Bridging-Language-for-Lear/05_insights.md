# Insights — Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving ...
- **p. 3 / 3.1. Overview - extractive body cue:** 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive body cue:** To address this, during fine-tuning, we introduce special action query tokens into Moto-GPT's input, enabling the generation of real robot actions through a flexible action ...
- **p. 2 / 1. Introduction - extractive body cue:** The performance can be further boosted with human video pre-training, highlighting the potential of our approach in transferring motion knowledge learned from Internet-scale videos to ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive body cue:** The total action loss Laction is defined as: \math c al {L } _{act i on} = \mathcal {L} (\Delta x) + \mathcal {L} (\Delta ...
- **p. 4 / 3.2. Latent Motion Tokenizer - extractive body cue:** For de-tokenization, we use a ViT Decoder for image reconstruction, which takes the linearly embedded patches of o_{t-1} and recovers the pixel values for o_ ...
- **p. 3 / 3.2. Latent Motion Tokenizer - extractive body cue:** The output query features are then processed by a VQ codebook with a vocabulary size of 128 to produce discrete latent motion tokens.
- **Contribution anchor:** p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 2 (1. Introduction), p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.2. Latent Motion Tokenizer)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** The main challenge is finding an appropriate representation for autoregressive pre-training on video data that effectively captures prior knowledge for robot manipulation.
- **p. 2 / 1. Introduction - extractive body cue:** These learned priors are subsequently transferred to enhance robot manipulation performance through a co-fine-tuning strategy.
- **p. 6 / 5.2. Moto-GPT as a Useful Motion Prior Learner - extractive body cue:** 7, clearly differentiate successful trajectories from failures and random attempts.
- **p. 6 / 5.2. Moto-GPT as a Useful Motion Prior Learner - extractive body cue:** The top-k token prediction accuracy and the visualization of predicted video trajectories 20 40 60 80 Sequence Step 5.0 4.5 4.0 3.5 Log Likelihood ( ...
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive body cue:** Future work will improve model architectures and incorporate more diverse human videos to tackle complex manipulation tasks.
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive body cue:** This further demonstrates the robustness of MotoGPT in real-world deployment.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 9. With additional human video (SSV2) pre-training, Moto (OXE+SSV2) significantly outperforms both Moto w/o Motion Token and Moto (OXE) on the Move Near task ...
- **Boundary to test:** 7, clearly differentiate successful trajectories from failures and random attempts.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving as a bridging "language" for autoregressive pre-training ... | p. 2 (1. Introduction), p. 3 (3.1. Overview) |
| Reported outcome | 8, Moto-GPT consistently outperforms Moto w/o Motion Token on these tasks, improving the average success rate from 23.33% to Moto w/o Motion Token Moto (OXE) Moto (OXE+SSV2) 50 55 60 65 70 ... | p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| Failure/limitation | 7, clearly differentiate successful trajectories from failures and random attempts. | p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner), p. 6 (5.2. Moto-GPT as a Useful Motion Prior Learner) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 An MLP-based action head projects the output hidden state of each action query token into the real robot action space.를 In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving as a bridging "language" for autoregressive pre-training ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 7, clearly differentiate successful trajectories from failures and random attempts.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving as a bridging "language" for autoregressive pre-training ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 7, clearly differentiate successful trajectories from failures and random attempts.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We conduct real-world evaluations with a FANUC LR Mate 200iD robot on three tasks: "pick-place banana", "close laptop", and "disassembly" (Fig..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 8. Evaluation results in the real-world environment. also generalizes well in the unseen CALVIN environment, outperforming baseline models that use various pre-training strategies (see supplementary material for detailed descrip- ....
4. Report the body metric and its denominator/aggregation: The "Overall" column reports the success rate averaged across the sub-tasks of all task types..
5. Re-run the body-reported ablation/failure condition: 11 shows that Moto-GPT fine-tuned with varying amounts of labeled data consistently outperforms its variant trained from scratch without latent motion tokens, especially with limited data..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.1. Overview), p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.2. Latent Motion Tokenizer); the primary result is directionally consistent at p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy), p. 6 (5.3. Moto-GPT as an Effective Robot Policy); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, below mechanism이 Figure 8. Evaluation results in the real-world environment. also generalizes well in the unseen CALVIN environment, ... 대비 The "Overall" column reports the success rate averaged across the sub-tasks of all task types.을 개선하고, 7, clearly differentiate successful trajectories from failures and random attempts. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
