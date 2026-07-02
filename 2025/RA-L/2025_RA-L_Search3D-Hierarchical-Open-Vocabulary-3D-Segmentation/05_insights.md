# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: However, this To evaluate our method’s ability to handle queries beyond can be problematic when performing and evaluating open- object-level descriptions, we introduce the task of scene-level vocabulary ...
- 출발 문제 단서: Existing methods for open-vocabulary 3D instance segmentation primarily focus on identifying object-level instances but struggle with finer-grained scene entities such as object parts, or regions described by generic ...
- 주장된 효과 단서: Search3D outperforms baselines in scene-scale open-vocabulary 3D part segmentation, while maintaining strong performance in segmenting 3D objects and materials.

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- 2D vision-language feature를 3D object/point/field/map에 정렬해 open-vocabulary querying과 semantic grounding에 사용할 수 있다.
- 핵심은 language prior를 3D metric structure와 맞추면서 view inconsistency와 hallucination을 줄이는 것이다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: Search3D outperforms baselines in scene-scale open-vocabulary 3D part segmentation, while maintaining strong performance in segmenting 3D objects and materials.
- open-vocabulary recognition이나 grounding을 보인 뒤에도 3D consistency, ambiguous reference resolution, robot-action relevance는 남는다.

## 다음 연구 질문
- 2D VLM feature를 3D로 lift할 때 multi-view consistency와 fine-grained object boundary를 동시에 유지할 수 있는가?
- language query가 robot action에 필요한 geometry/affordance까지 정확히 가리키는지 어떻게 평가할 수 있는가?
- semantic confidence와 geometric uncertainty를 함께 쓰면 false grounding을 줄일 수 있는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: ScanNet, ScanNet200, 3RScan, LERF / accuracy, mIoU, AP
- 내 연구 확장 benchmark 후보: ScanNet, ScanRefer, ReferIt3D, SQA3D
- 내 연구 확장 metric 후보: mIoU, Acc@0.25, Acc@0.5, Recall@K
- 검증 초점: open-vocabulary segmentation/localization, 3D consistency, task-relevant grounding을 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: Existing methods for open-vocabulary 3D instance segmentation primarily focus on identifying object-level instances but struggle with finer-grained scene entities such as object parts, or regions described by generic ...
- Method cue: However, this To evaluate our method’s ability to handle queries beyond can be problematic when performing and evaluating open- object-level descriptions, we introduce the task of scene-level vocabulary ...
- Result cue: Search3D outperforms baselines in scene-scale open-vocabulary 3D part segmentation, while maintaining strong performance in segmenting 3D objects and materials.
