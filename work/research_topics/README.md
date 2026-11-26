# 연구 주제

<a id="candidate-priority"></a>
<a id="masters-publication-comparison"></a>

현재 질문은 **같은 위 칸 수납 지시에서 어느 카메라에 언제 서랍 폭을 보여주면 접근과 수납이 달라지는가**이다. 뒤 0.5초에 두 카메라의 영상을 함께 바꿔 그리퍼의 첫 접촉이 그릇에서 아래 서랍으로 옮겨간 34묶음은 한 카메라만 바꿨을 때 어느 쪽도 같은 접촉을 재현하지 못했다. 끝까지 무접촉이 된 24묶음에서는 외부 영상만으로 5묶음이 재현됐다.

| 필요한 자료 | 문서 |
|---|---|
| 무엇을 측정했고 어디까지 해석할 수 있는가 | [외부·손목 단독 교환](./instruction_revision/내용/README.md#drawer-camera-window) · [그리퍼 출발 위치](./instruction_revision/내용/README.md#drawer-gripper-position) · [그릇 위치](./instruction_revision/내용/README.md#drawer-bowl-position) · [영상 교환 시점](./instruction_revision/내용/README.md#drawer-view-window-layout3) · [실제 개방 폭](./instruction_revision/내용/README.md#drawer-width) |
| 어떻게 출발 상태와 저장 명령을 재생하는가 | [로컬 Docker 재현](./instruction_revision/재현%20방법/README.md) |
| 다음에 고정하거나 바꿀 변수 | [다음 작업](../../TODO.md) |
| 이전 후보의 결과와 재개 조건 | [종료·보류 결과](./RESULTS.md) |

제약 갱신기 학습은 보류 중이다. 이번 비교에는 LIBERO 배치 두 개와 체크포인트 하나를 사용했다.
