# AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·arXiv v1 §III–V/Table II–IV·공식 코드로 OCR/설명 교정. 과거2026-09-03 PDF review 기록은 보존; 사용자 reading status 변경 없음.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Paper-supported Conclusion

학습된 adaptation reference와 RL lower policy가 G1의 전신 조작 범위를 넓히고 상위 imitation policy를 지원한다. 평가 범위는 [04_evaluation](./04_evaluation.md)과 [공식 논문](https://www.roboticsproceedings.org/rss21/p061.html)을 따른다.

## Researcher Interpretation

- Trajectory optimization·PPO·ACT와 연결해 읽는다. 과거 generated queue 이웃은 실제 citation evidence가 아니다.
- Ψ₀가 직접 사용하는 하위 baseline이다. SONIC으로 교체한 후속 공개 구성은 같은 VLA를 썼다는 이유만으로 controller 통제 비교가 되지 않는다.
- 상위 정책의 실패처럼 보이는 현상이 reference feasibility나 하위 tracking 한계에서 생길 수 있다.

## Minimal Reproduction and Falsifiable Question

같은 upper command·관측·control budget에서 adaptation 유무의 tracking·균형·task 성공을 분리한다. 상위 VLA 개선이 controller 변경만으로 설명되면 VLA 학습 기여를 주장하지 않는다. 실행 제안이며 실험하지 않았다.
