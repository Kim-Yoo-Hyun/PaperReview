# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: To bridge this gap, we introduce E MBODIED B ENCH, an extensive benchmark designed to evaluate visiondriven embodied agents.
- 출발 문제 단서: E MBODIED B ENCH provides a multifaceted standardized evaluation platform that not only highlights existing challenges but also offers valuable insights to advance MLLMbased embodied agents.
- 주장된 효과 단서: Through extensive experiments, we evaluated 24 leading proprietary and open-source MLLMs within E MBODIED B ENCH.

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Attention 기반 token interaction을 3D object, scene, map, trajectory token 사이의 long-range relation modeling에 사용할 수 있다.
- Sequence modeling의 병렬화/장거리 의존성 처리를 embodied memory, planning history, multi-view observation aggregation으로 확장할 수 있다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: Through extensive experiments, we evaluated 24 leading proprietary and open-source MLLMs within E MBODIED B ENCH.
- 논문 내 한계/논의 단서: Error Analysis We conducted an error analysis on GPT-4o to identify potential failure modes in EB-ALFRED and EB-Manipulation.
- 원 논문이 sequence/language task에서 보인 구조는 metric 3D geometry, SE(3) consistency, sensor noise, robot execution constraint를 직접 다루지 않는다.

## 다음 연구 질문
- 3D point/object/map/action token에 attention을 적용할 때 어떤 positional encoding이 metric geometry를 보존하는가?
- long-horizon embodied task에서 full attention, sparse attention, graph attention 중 무엇이 memory와 planning에 유리한가?
- language reasoning token과 3D geometry token을 어떤 intermediate representation으로 정렬해야 hallucination을 줄일 수 있는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: Habitat, AI2-THOR, VLABench, EmbodiedBench / accuracy, mAP, success rate, collision
- 내 연구 확장 benchmark 후보: ScanNet, Matterport3D, R2R, CALVIN
- 내 연구 확장 metric 후보: accuracy, mIoU, SR, success rate
- 검증 초점: 3D relation reasoning, spatial memory, language-conditioned planning 성능을 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: E MBODIED B ENCH provides a multifaceted standardized evaluation platform that not only highlights existing challenges but also offers valuable insights to advance MLLMbased embodied agents.
- Method cue: To bridge this gap, we introduce E MBODIED B ENCH, an extensive benchmark designed to evaluate visiondriven embodied agents.
- Result cue: Through extensive experiments, we evaluated 24 leading proprietary and open-source MLLMs within E MBODIED B ENCH.
