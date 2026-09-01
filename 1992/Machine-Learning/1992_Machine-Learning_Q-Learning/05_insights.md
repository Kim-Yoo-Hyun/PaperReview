# Insights — Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00992698; PDF retrieval source: https://doi.org/10.1007/BF00992698. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 2. The task for ~-learning - extractive body cue:** In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes.
- **p. 4 / 3. The convergence proof - extractive body cue:** A state of the AFI~, (x, n), consists of a card number (or level) n, together with a state x from the real process.
- **p. 4 / 3. The convergence proof - extractive body cue:** Replaying the episode on card t consists of emitting the reward, rt, written on the card, and then moving to the next state (Yt, t ...
- **p. 1 / 1. Introduction - extractive body cue:** Examples of its use include Barto and Singh (1990), Sutton (1990), Chapman and Kaelbling (1991), Mahadevan and Connell (1991), and Lin (1992), who developed it ...
- **p. 7 / 3.2. The theorem - extractive body cue:** Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x ...
- **p. 2 / 2. The task for ~-learning - extractive body cue:** Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to receive 6~x(Tr(x)) immediately ...
- **p. 3 / 2. The task for ~-learning - extractive body cue:** It is straightforward to show that V*(x) = max a O~*(x, a) and that if a* is an action at which the maximum is attained, ...
- **Contribution anchor:** p. 3 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 4 (3. The convergence proof), p. 1 (1. Introduction), p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Section 2 describes the problem, the method, and the notation, section 3 gives an overview of the proof, and section 4 discusses two extensions.
- **p. 8 / 4. Discussions and conclusions - extractive body cue:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required.
- **p. 8 / 4. Discussions and conclusions - extractive body cue:** The theorem above only proves the convergence of a restricted version of Watkins' (1989) comprehensive Q-learning algorithm, since it does not permit updates based on ...
- **Boundary to test:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes. | p. 3 (2. The task for ~-learning), p. 4 (3. The convergence proof) |
| Reported outcome | Given e > O, choose s such that .ys__ < 1-3` T By B.3, with probability 1, it is possible to choose l sufficiently large such that for n > l, and ... | p. 6 (3.2. The theorem), p. 7 (3.2. The theorem) |
| Failure/limitation | Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required. | p. 8 (4. Discussions and conclusions), p. 8 (4. Discussions and conclusions) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 Y In other words, the ~ value is the expected discounted reward for executing action a at state x and following policy 7r thereafter.를 Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to receive 6~x(Tr(x)) immediately for performing the action 7r recommends, and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, Q-learning, Value Learning`.
- **Reading predecessor in the generated track queue:** Learning to Predict by the Methods of Temporal Differences (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: First, all the cards for episodes later than n are eliminated, leaving just a finite deck..
3. Compare against the body-reported baseline or a matched simpler baseline: Assume, without loss of generality, that O~0(x, a) < 61/(1 - 3') and that 61 __..
4. Report the body metric and its denominator/aggregation: DAYAN Theorem Given bounded rewards I rn [ -< (R, learning rates 0 < c~ n < 1, and ~ Otni(x,a ) : 0o, ~11 [~ni(x,a)] 2 < 0o, ~tX, a, i=1 ....
5. Re-run the body-reported ablation/failure condition: 2 Note that during such a sequence, episode cards are only removed from the deck, and are never replaced..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning), p. 4 (3. The convergence proof); the primary result is directionally consistent at p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 learning, agent, experience mechanism이 Assume, without loss of generality, that O~0(x, a) < 61/(1 - 3') and that 61 __. 대비 DAYAN Theorem Given bounded rewards I rn [ -< (R, learning rates 0 < c~ n < 1, ...을 개선하고, Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
