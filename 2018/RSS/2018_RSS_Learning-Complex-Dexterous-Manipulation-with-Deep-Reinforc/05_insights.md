# Insights — Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss14/p49.html; PDF retrieval source: https://arxiv.org/pdf/1709.10087. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR).
- **p. 2 / I. INTRODUCTION - extractive body cue:** We attribute this to human priors in the demonstrations which bias the learning towards more robust strategies. • We propose a set of dexterous hand ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Indeed, model-free methods have been used for acquiring manipulation skills [52], [13], but so far have been limited to simpler behaviors with 2-3 finger hands ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Thus, before we can develop DRL methods suitable for dexterous manipulation with robotic hands, we must set up a suite of manipulation tasks that exercise ...
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** A number of pre-conditioned policy gradient methods have been developed in literature [19], [4], [35], [34], [43], [40], [44] and in principle any of them ...
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** We first present some RL preliminaries, followed by the base RL algorithm we use for learning, and finally describe our procedure to incorporate demonstrations.
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** First, NPG computes the vanilla policy gradient, or REINFORCE [54] gradient: g = 1 NT N X i=1 T X t=1 ∇θ log πθ(ai t/si ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG))

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these methods typically rely on accurate dynamics models and state estimates, which are often difficult to obtain for contact rich manipulation tasks, especially in ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the current benchmarks are typically quite limited both in the dimensionality of the tasks and the complexity of the interactions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR).
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that existing RL algorithms can indeed solve these dexterous manipulation tasks, but require significant manual effort in reward shaping.
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse ...
- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** robustness to variations in the environment?
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** The mental models of solution strategies that humans have for these tasks are indeed quite robust.
- **Boundary to test:** Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse task completion rewards.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR). | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance of the stochastic policy used for exploration. At any iteration, ... | p. 8 (Figure/Table caption), p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| Failure/limitation | Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse task completion rewards. | p. 6 (V. RESULTS AND DISCUSSION), p. 6 (2) Do the resulting policies exhibit desirable properties like) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation history와 expert trajectory/action → behavior policy와 temporal action context → predicted action 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 However, this versatility comes at the price of high dimensional observation and action spaces, complex and discontinuous contact patterns, and under-actuation during nonprehensile manipulation.를 S ∈Rn and A ∈Rm represent the state and actions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 behavior policy와 temporal action context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse task completion rewards.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, Reinforcement Learning, dexterous manipulation`.
- **Reading predecessor in the generated track queue:** A Minimalist Approach to Offline Reinforcement Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Learning Latent Plans from Play (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse task completion rewards.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In order to benchmark the capabilities of DRL with regard to the dexterous manipulation tasks outlined in Section III, we evaluate the NPG algorithm described briefly in Section V, and the DDPG ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance of the stochastic policy used for exploration. At any iteration, ....
4. Report the body metric and its denominator/aggregation: Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse task completion rewards..
5. Re-run the body-reported ablation/failure condition: Figure 9: Robustness of trained policies to variations in the envi- ronment. The top two figures are trained on a single instance of the environment (indicated by the star) and then tested ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 6 (2) Do the resulting policies exhibit desirable properties like); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 overcome, challenge, augment mechanism이 Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. ... 대비 Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained ...을 개선하고, Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
