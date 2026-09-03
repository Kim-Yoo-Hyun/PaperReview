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

- **Paper-specific interface:** Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x in the ARP, with Q(x, ... (p. 7, 3.2. The theorem).
- **Paper-specific mechanism:** O~-learning (Watkins, 1989) is a form of model-free reinforcement learning. (p. 1, 1. Introduction).
- **Evidence boundary:** the reported outcome is Imagine each episode (xt, at, Yt, rt, °~t) written on a card. (p. 4, 3. The convergence proof); the relevant task/metric cue is The above completely specifies how state transitions and rewards are determined in the AFIP. (p. 4, 3. The convergence proof). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required. (p. 8, 4. Discussions and conclusions).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, Q-learning, Value Learning`.
- **Reading predecessor in the generated track queue:** Learning to Predict by the Methods of Temporal Differences (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x in the ARP, with Q(x, ... (p. 7, 3.2. The theorem); preserve the objective/update rule: The second term is the cost, from B.4, of the incorrect rewards and transition probabilities. (p. 7, 3.2. The theorem).
2. Use the paper-reported task/data/environment cue: Imagine each episode (xt, at, Yt, rt, °~t) written on a card. (p. 4, 3. The convergence proof).
3. Compare against the reported or matched baseline: Assume, without loss of generality, that O~0(x, a) < 61/(1 - 3') and that 61 __. (p. 6, 3.2. The theorem).
4. Report the body metric with its denominator and aggregation: The above completely specifies how state transitions and rewards are determined in the AFIP. (p. 4, 3. The convergence proof).
5. Re-run the reported ablation or stress/failure condition: 2 Note that during such a sequence, episode cards are only removed from the deck, and are never replaced. (p. 5, 3. The convergence proof); if none is reported, design one around: Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required. (p. 8, 4. Discussions and conclusions).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1. Introduction), p. 1 (1. Introduction), match the reported outcome at p. 4 (3. The convergence proof), p. 4 (3. The convergence proof), p. 4 (3. The convergence proof), and measure the boundary at p. 8 (4. Discussions and conclusions), p. 8 (4. Discussions and conclusions).

## Falsifiable research question

Under the paper's stated interface (Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as ...), does the paper-specific mechanism (O~-learning (Watkins, 1989) is a form of model-free reinforcement learning.) retain the reported evaluation outcome (The above completely specifies how state transitions and rewards are determined in the AFIP.) when tested against the paper's strongest explicit boundary (Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The above completely specifies how state transitions and rewards are determined in the AFIP.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** O~-learning (Watkins, 1989) is a form of model-free reinforcement learning. (p. 1, 1. Introduction).
- **Paper-supported outcome:** Imagine each episode (xt, at, Yt, rt, °~t) written on a card. (p. 4, 3. The convergence proof).
- **Strongest explicit boundary:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required. (p. 8, 4. Discussions and conclusions).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
