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

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Then, we do action pretraining by using a pretrained VLM to predict the zt given the language instruction of a video clip and the current image xt.를 In the second stage, we perform behavior cloning by pretraining a Vision-Language Model to predict latent actions derived from the first stage based on video observations and task descriptions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away from the red cube and red pentagon', the diffusion model of UNIPI successfully generates ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then finetuning it on on diverse robot datasets ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, latent action, human video, video pretraining, action representation`.
- **Reading predecessor in the generated track queue:** RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** 3D-VLA: A 3D Vision-Language-Action Generative World Model (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away from the red cube and red pentagon', the diffusion model of UNIPI successfully generates ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 4.1 BENCHMARKS AND ENVIRONMENTS We evaluate the effectiveness of LAPA on 9 different task categories in 2 different simulation environments and 3 different real-world robotic tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: (2024) since it is not a behavior cloning baseline..
4. Report the body metric and its denominator/aggregation: Average Success Rate (%) ± StdErr across the three different pretrainfinetune combinations from the Language Table benchmark as described in Table 3..
5. Re-run the body-reported ablation/failure condition: Figure 1: Problem Formulation. We investigate building a generalist robotic foundation model from human motion videos without action labels. VQ-VAE-based objective (Van Den Oord et al., 2017) to learn quantized latent actions ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining), p. 3 (2. Latent Pretraining); the primary result is directionally consistent at p. 7 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 9 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Vision-Language-Action, Models, VLA mechanism이 (2024) since it is not a behavior cloning baseline. 대비 Average Success Rate (%) ± StdErr across the three different pretrainfinetune combinations from the Language Table benchmark as ...을 개선하고, Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
