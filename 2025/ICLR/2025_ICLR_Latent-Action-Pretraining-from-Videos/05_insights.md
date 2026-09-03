# Insights — Latent Action Pretraining from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2410.11758.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Latent Action Pretraining consists of two models that are learned sequentially, followed by a finetuning stage to map the latent actions to real robot actions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We expect that our method opens up the potential for building foundation models for robotics by pretraining on much larger web-scale video data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, on real-world manipulation tasks, our method leads to a new monolithic VLA model, outperforming OPENVLA, the current state-of-the-art model Vision Language Action (VLA) model ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** The VQ-VAE objective enables the latent action zt to be discrete tokens (codebooks), making it easy for VLMs to predict zt.
- **p. 4 / 2. Latent Pretraining - extractive body cue:** 3.2 LATENT PRETRAINING We use the encoder of the latent action quantization model as an inverse dynamics model to label all frames xt, given frame ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** Our latent action quantization model is an encoder-decoder architecture where the encoder takes the current frame xt and the future frame xt+H of a video ...
- **Contribution anchor:** p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, it is challenging to learn from internet video data for two major challenges: first, much of the raw data on the web lacks explicit ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, diverse real-world robot datasets mostly require human teleoperation, which makes scaling difficult.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We measure performance on diverse manipulation videos, including existing robot video datasets (without utilizing ground-truth actions) and human manipulation datasets.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Analogous to Byte Pair Encoding (Sennrich et al., 2016) used for language modeling, this can be seen as learning to tokenize atomic actions without requiring ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away from the red cube and red pentagon', ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We observe that most failures of LAPA are due to early grasping.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Like before, UNIPI is constrained by its diffusion model's planning limitations, while VPT performs strongly, even surpassing ACTIONVLA in the unseen setting.
- **Boundary to test:** Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away from the red cube and red pentagon', the diffusion model of UNIPI successfully generates ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then finetuning it on on diverse robot datasets ... | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Reported outcome | Furthermore, by comparing LAPA which does not leverage action-labeled trajectories during pretraining with models that use action-labeled trajectories during pretraining (ACTIONVLA and OPENVLA), we observe an interesting finding: LAPA o ... | p. 7 (4 EXPERIMENTS), p. 9 (Figure/Table caption) |
| Failure/limitation | Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away from the red cube and red pentagon', the diffusion model of UNIPI successfully generates ... | p. 25 (Figure/Table caption), p. 7 (4 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Then, we do action pretraining by using a pretrained VLM to predict the zt given the language instruction of a video clip and the current image xt. (p. 4, 2. Latent Pretraining).
- **Paper-specific mechanism:** Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then finetuning it on on diverse ... (p. 1, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is 4.5 LEARNING FROM HUMAN MANIPULATION VIDEOS Scratch UniPi VPT LAPA 0 10 20 30 40 50 60 AVG Success Rate (%) 34.4 0.7 45.8 52.1 (a) SIMPLER Results Average Knock ... (p. 8, 4 EXPERIMENTS); the relevant task/metric cue is Average success rate (%) ± StdErr are shown (detailed results provided in Appendix G.3). (p. 7, 4 EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We observe that most failures of LAPA are due to early grasping. (p. 7, 4 EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, latent action, human video, video pretraining, action representation`.
- **Reading predecessor in the generated track queue:** RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** 3D-VLA: A 3D Vision-Language-Action Generative World Model (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away from the red cube and red pentagon', the diffusion model of UNIPI successfully generates ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Then, we do action pretraining by using a pretrained VLM to predict the zt given the language instruction of a video clip and the current image xt. (p. 4, 2. Latent Pretraining); preserve the objective/update rule: (1) Latent Action Quantization: We first learn discrete latent actions in a fully unsupervised manner using the VQ-VAE objective (Detail in Figure 8). (p. 3, 2. Latent Pretraining).
2. Use the paper-reported task/data/environment cue: 4.1 BENCHMARKS AND ENVIRONMENTS We evaluate the effectiveness of LAPA on 9 different task categories in 2 different simulation environments and 3 different real-world robotic tasks. (p. 5, 4 EXPERIMENTS).
3. Compare against the reported or matched baseline: (2024) since it is not a behavior cloning baseline. (p. 5, 4 EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Average success rate (%) ± StdErr are shown (detailed results provided in Appendix G.3). (p. 7, 4 EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: 4.4 REAL-WORLD RESULTS We pretrain our models on (1) Bridgev2 (Walke et al., 2023) to measure the cross-embodiment performance (WidowX embodiment for pretraining and Franka embodiment for finetuning) and (2) ... (p. 6, 4 EXPERIMENTS); if none is reported, design one around: We observe that most failures of LAPA are due to early grasping. (p. 7, 4 EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), match the reported outcome at p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 8 (Figure/Table caption), and measure the boundary at p. 7 (4 EXPERIMENTS), p. 21 (C BASELINE DETAILS).

## Falsifiable research question

Under the paper's stated interface (Then, we do action pretraining by using a pretrained VLM to predict the zt given the language instruction of a video clip ...), does the paper-specific mechanism (Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision ...) retain the reported evaluation outcome (Average success rate (%) ± StdErr are shown (detailed results provided in Appendix G.3).) when tested against the paper's strongest explicit boundary (We observe that most failures of LAPA are due to early grasping.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Average success rate (%) ± StdErr are shown (detailed results provided in Appendix G.3).) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then finetuning it on on diverse ... (p. 1, 1 INTRODUCTION).
- **Paper-supported outcome:** 4.5 LEARNING FROM HUMAN MANIPULATION VIDEOS Scratch UniPi VPT LAPA 0 10 20 30 40 50 60 AVG Success Rate (%) 34.4 0.7 45.8 52.1 (a) SIMPLER Results Average Knock ... (p. 8, 4 EXPERIMENTS).
- **Strongest explicit boundary:** We observe that most failures of LAPA are due to early grasping. (p. 7, 4 EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
