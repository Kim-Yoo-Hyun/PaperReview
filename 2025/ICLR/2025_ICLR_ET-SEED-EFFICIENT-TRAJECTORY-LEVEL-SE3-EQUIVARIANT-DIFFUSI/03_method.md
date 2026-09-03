# Method - ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OheAR2xrtb; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114743. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (4 METHOD), p. 4 (4 METHOD), p. 7 (4 METHOD), p. 4 (4 METHOD), p. 5 (4 METHOD), p. 6 (4 METHOD)): In each denoising step, the input of our denoising network sθ consists of observation O, noisy action sequence Ak, and scalar condition k, outputs the predicted relative transformation between Ak ...

## Method Body Digest

- **p. 7 / 4 METHOD - extractive body cue:** In each denoising step, the input of our denoising network sθ consists of observation O, noisy action sequence Ak, and scalar condition k, outputs the ...
- **p. 4 / 4 METHOD - extractive body cue:** 2 is a general example to show how it works, given an observation and a noisy action sequence, our model first implement K -1 invariant ...
- **p. 7 / 4 METHOD - extractive body cue:** Formally, sθ is defined as sθ(O, Ak; k) =  Einv(O, Ak; k), k > 1 Eequiv(O, Ak; k), k = 1 (9) As illustrated ...
- **p. 4 / 4 METHOD - extractive body cue:** In this paper, we propose ET-SEED, a trajectorylevel end-to-end SE(3) equivariant diffusion model for robotic manipulation.
- **p. 5 / 4 METHOD - extractive body cue:** In this paper, based on SE(3) Transformer (Fuchs et al., 2020), we propose SE(3) equivariant backbone Eequiv and invariant backbone Einv, which are suitable for ...
- **p. 6 / 4 METHOD - extractive body cue:** SE(3) Transformer have same network architecture, the feature types of input and output differ, resulting in different coefficient matrices in network forward.
- **p. 6 / 4 METHOD - extractive body cue:** A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant denoising steps and then a SE(3) equivariant ...
- **p. 5 / 4 METHOD - extractive body cue:** In practice, we observe that training neural networks to approximate the properties of p2 and p3 is much more challenging compared to p1, both in ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are mainly as followed: • We propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion policy defined on SE(3) manifold, which achieves ...
- **p. 7 / 4 METHOD - extractive body cue:** Formally, we have ˆAk→0 = sθ(O, Ak; k) (8) To ensure the overall SE(3) equivariance of our pipeline, we propose a novel design of denoising ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Further, in real-world experiments, with only 20 demonstration trajectories, our method is able to generalize to unseen scenarios.

## Source Evidence Cues

- **p. 7 / 4 METHOD - extractive body cue:** In each denoising step, the input of our denoising network sθ consists of observation O, noisy action sequence Ak, and scalar condition k, outputs the ...
- **p. 4 / 4 METHOD - extractive body cue:** 2 is a general example to show how it works, given an observation and a noisy action sequence, our model first implement K -1 invariant ...
- **p. 7 / 4 METHOD - extractive body cue:** Formally, sθ is defined as sθ(O, Ak; k) =  Einv(O, Ak; k), k > 1 Eequiv(O, Ak; k), k = 1 (9) As illustrated ...
- **p. 4 / 4 METHOD - extractive body cue:** In this paper, we propose ET-SEED, a trajectorylevel end-to-end SE(3) equivariant diffusion model for robotic manipulation.
- **p. 5 / 4 METHOD - extractive body cue:** In this paper, based on SE(3) Transformer (Fuchs et al., 2020), we propose SE(3) equivariant backbone Eequiv and invariant backbone Einv, which are suitable for ...
- **p. 6 / 4 METHOD - extractive body cue:** SE(3) Transformer have same network architecture, the feature types of input and output differ, resulting in different coefficient matrices in network forward.
- **p. 6 / 4 METHOD - extractive body cue:** A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant denoising steps and then a SE(3) equivariant ...
- **Detected method headings:** 4 METHOD (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | In each denoising step, the input of our denoising network sθ consists of observation O, noisy action sequence Ak, and scalar condition ... | p. 7 (4 METHOD), p. 4 (4 METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | 2 is a general example to show how it works, given an observation and a noisy action sequence, our model first implement ... | p. 4 (4 METHOD), p. 7 (4 METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Formally, sθ is defined as sθ(O, Ak; k) =  Einv(O, Ak; k), k > 1 Eequiv(O, Ak; k), k = 1 ... | p. 7 (4 METHOD), p. 4 (4 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4 METHOD - extractive body cue:** In practice, we observe that training neural networks to approximate the properties of p2 and p3 is much more challenging compared to p1, both in ...
- **p. 7 / 4 METHOD - extractive body cue:** Formally, sθ is defined as sθ(O, Ak; k) =  Einv(O, Ak; k), k > 1 Eequiv(O, Ak; k), k = 1 (9) As illustrated ...
- **p. 7 / 4 METHOD - extractive body cue:** 3 , the input of reverse process is an observation O, an noisy action sequence AK = [HK 0 , HK 1 , ..., HK ...
- **p. 4 / 4 METHOD - extractive body cue:** We will discuss equivariant Markov processes further to explain the correctness and advantages of our proposed diffusion process in section 4.1 , with only one ...
- **p. 6 / 4 METHOD - extractive body cue:** Inspired by standard diffusion model, ET-SEED progressively disturbs the noise-free action H0 ∈ SE(3) into a noisy action HK.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | ET-SEED, theoretically, guarantee, output, actions, equivariant, transformation, applied, input, observation, while, only, involving, denoising | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | ET-SEED, theoretically, guarantee, output, actions, equivariant, transformation, applied, input, observation | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, mainly, followed, ET-SEED, efficient, trajectory-level, equivariant, diffusion, policy | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | practice, observe, training, neural, networks, approximate, properties, much, more, challenging | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4 METHOD - extractive body cue:** ET-SEED can theoretically guarantee the output actions are equivariant to any SE(3) transformation applied on the input observation, while only involving one equivariant denoising step.
- **p. 7 / 4 METHOD - extractive body cue:** When the input observation O is transformed by any SE(3) element T, the output denoised action sequence A0 will be equivariantly transformed.
- **p. 7 / 4 METHOD - extractive body cue:** In each denoising step, the input of our denoising network sθ consists of observation O, noisy action sequence Ak, and scalar condition k, outputs the ...
- **p. 4 / 4 METHOD - extractive body cue:** We formulate the problem as an imitation learning setting, aiming to learn a mapping from observation O to action sequence A, with some demonstrations from ...
- **p. 5 / 4 METHOD - extractive body cue:** Additionally, in most of implementations of equivariant networks, building and training a model whose output is SE(3) equivariant to the input takes up more computing ...
- **p. 6 / 4 METHOD - extractive body cue:** SE(3) Transformer have same network architecture, the feature types of input and output differ, resulting in different coefficient matrices in network forward.
- **p. 6 / 4 METHOD - extractive body cue:** A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant denoising steps and then a SE(3) equivariant ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | 2 is a general example to show how it works, given an observation and a noisy action sequence, our model first implement ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant denoising steps and then ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | In ET-SEED, we set the parameter n = 2, meaning there are K -1 p1-like transitions (referred to as "SE(3) Invariant Denoising ... | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 5 EXPERIMENTS - extractive body cue:** We evaluate all methods using two metrics, based on 20 evaluation rollouts, averaged over 5 random seeds.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** denoising, step, input, network, consists, observation, noisy, action, sequence, scalar, condition, outputs, predicted, relative, transformation, between, noise-free, general, example, works.
- **Relevant PDF headings:** 4 METHOD (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | (3) Is our method applicable to real-world robotic manipulation tasks? | p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Action / skill decoding | DP3 and DP3+Aug are used to compare ET-SEED with baseline methods that utilize data augmentation to achieve spatial generalization, while EquiBot allows ... | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Receding execution / feedback | Design Average Ours w/o SE(3) 24±4.48 Ours w/o Eqv-Diff 57±6.52 Ours 76±2.24 While EquiBot achieves commendable results in both success rate and ... | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 5 EXPERIMENTS - extractive body cue:** We conduct ablation studies on the New Pose (NP) scenario of the representative Opening Door task to evaluate the effectiveness of different components of our ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In this variant, we use a standard PointNet++ to predict noise at each step. • Ours w/o Eqv-Diff: Our method without the SE(3) equivariant denoising ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Further details and discussions of their equivariant properties can be found in appendix G .
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: ET-SEED is a visual imitation learning algorithm that marries SE(3) equivariant visual representations with diffusion policies. (a) ET-SEED achieve surprising efficiency and spatial ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of the denoising pro- cess of ET-SEED. A random trajectory xK first passes through an invariant transition for K -1 times and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Overview of our pipeline. A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant denoising ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 5: Loss curve of P1Net, P2Net and P3Net. After only several gradient descent, the loss of P1Net converges almost to 0, while the losses ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (4 METHOD), p. 4 (4 METHOD), p. 7 (4 METHOD), p. 4 (4 METHOD), p. 5 (4 METHOD), p. 6 (4 METHOD), objective p. 5 (4 METHOD), p. 7 (4 METHOD), p. 7 (4 METHOD), p. 4 (4 METHOD), p. 6 (4 METHOD), temporal p. 4 (4 METHOD), p. 6 (4 METHOD), p. 7 (4 METHOD), p. 7 (4 METHOD), p. 4 (4 METHOD), p. 5 (4 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
