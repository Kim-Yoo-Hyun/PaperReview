# LIBERO 서랍 실험 재현

<a id="drawer-width"></a>

## 같은 물체 위치에서 개방 폭만 바꾸기

배치 2에서 이전 연구의 충돌 없는 그릇·접시 좌표를 그대로 쓴다. 모두 닫힘과 가운데·아래 각각 76 mm 및 원래의 완전 개방 폭을 만들어 다섯 조건을 비교한다. 각 복귀 자세에서 모두 닫힘과 두 완전 개방 상태의 물리 해시를 직전 원본과 대조한다. 76 mm에서는 닫힌 상태의 전체 적분 상태에서 해당 슬라이드 위치 하나만 달라야 한다. 정책 실행 전 물체의 탁자 지지, 충돌, 1초 정지 시 이동을 검사한다. [사전 설계](./drawer/drawer_width.json) · [물리 개입](./drawer_width_sim.py) · [채점](./drawer_width.py)

같은 두 자세와 여덟 시드를 짝짓고, 다섯 조건을 순환한 뒤 모델을 새로 불러와 역순으로 반복한다. 15초와 30초에는 3초의 자세 복귀가 포함된다. 각 경로에서 정책이 실행한 540개 제어를 물리 재생한다. 당긴 장면의 명령은 같은 칸의 다른 폭에서, 닫힌 장면의 명령은 네 개의 당긴 장면 모두에서 재생한다.

```sh
recipe='work/research_topics/instruction_revision/재현 방법'
archive="$recipe/results/2026-11-25-drawer-width"
(cd "$archive" && sha256sum -c SHA256SUMS)
sh "$recipe/resume.sh" verify-drawer-width "$archive"
report_dir=$(mktemp -d)
sh "$recipe/resume.sh" replay-drawer-width "$archive" "$report_dir/physical.json"
# 같은 정책으로 다섯 조건을 새로 수집할 때
sh "$recipe/resume.sh" drawer-width "$report_dir/new-study"
```

원본 수집 폴더와 압축본을 각각 새 컨테이너에서 재생했다. 재생 한 번에 원래 경로 160개와 다른 폭·장면에 적용한 경로 256개를 검증했다. 교차 경로에서는 총 138,240개 제어를 적용했다. 두 재생의 접촉·수납 추적, 제어별 물리 측정 해시와 종단 물리 상태가 일치했다. 원래 경로의 카메라 관측 17,280시점 중 수집 당시와 다시 렌더링한 영상이 다른 시점은 각각 8개와 13개였다. 원본 수집 코드와 해시는 압축본의 `sources/`와 `runtime.json`에 있다. [두 독립 재생 대조](./results/2026-11-25-drawer-width/physical_replay.json) · [파일 해시](./results/2026-11-25-drawer-width/SHA256SUMS)

새 컴퓨터에서는 아래 설치·자산 절차로 로컬 Docker 이미지와 체크포인트를 준비한다. 보존한 원본을 재채점하거나 물리만 재생하는 단계에는 체크포인트가 필요하지 않다.

<a id="drawer-location"></a>

## 위 칸 지시를 유지하고 가운데·아래 서랍의 개방 위치 바꾸기

공식 위 칸 수납 과제에 공개 가운데 서랍 초기 배치 2를 적용한다. 서로 다른 두 서랍 열기 종단을 재생하고 60제어(3초) 동안 팔을 복귀시킨다. 이전 실험의 모두 닫힘·가운데 열림 상태 해시 네 개를 먼저 확인한다. 각 비교에서는 위 칸·로봇·물체·제어기·난수열을 맞추고, 가운데 또는 아래 슬라이드 하나에 같은 수평 변위를 준다. [공식 수납 조건](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/bddl_files/libero_goal/open_the_top_drawer_and_put_the_bowl_inside.bddl) · [설계와 변경 시점](./drawer/drawer_location.json) · [종단 복원 명령과 해시](./drawer/middle_aperture_layout2_donors.json)

원래 물체 위치에서 아래 칸을 0–159 mm까지 1 mm씩 당겨 접촉을 검사하고, 두 종단의 원래 개방 폭인 159.84·159.92 mm도 검사했다. 79 mm에서 처음 장애물에 닿았고, 141–159 mm의 공식 열림 범위 19개는 모두 접촉했다. **첫 비교**는 원래 물체 위치에서 2 mm의 여유를 남긴 76 mm다. **둘째 비교**는 원래 개방 폭을 유지한다. 정책을 실행하기 전에 물체를 수평으로 같은 거리·방향만큼 옮기는 후보 240개를 검사했다. 두 물체를 함께 옮겨 통과한 후보가 없어 각각의 변위를 골랐다. 세계 좌표에서 그릇은 x축으로 −45 mm, 접시는 x·y축으로 각각 +84.85 mm(거리 120 mm) 이동했다. 세 조건에 동일하게 적용하고 탁자 지지, 주변 물체·그리퍼와의 접촉, 1초 정지 시 변화를 검사했다. [기하 검사 코드](./drawer_location_clearance.py) · [서랍 개입과 물리 재생](./drawer_location_sim.py)

각 배치의 세 조건에 두 출발 상태와 같은 여덟 시드를 적용한다. 여섯 조건의 실행 순서를 바꿔 가며 비교하고 가중치를 다시 불러온 뒤 역순으로 반복한다. 총 192경로의 정책 입력은 두 카메라 영상, 로봇 상태와 위 칸 수납 지시다. 20 Hz에서 매 5제어마다 정책을 다시 질의하고, 8·15·30초는 3초 자세 복귀를 포함해 센다. 같은 출발 상태·시드에서 가운데 칸을 당겼을 때는 가운데에, 아래 칸을 당겼을 때는 아래에 그릇이 들어간 경우를 한 쌍의 목적지 전환으로 센다. 조건별 명령 540개를 두 다른 서랍 상태에도 적용한 뒤 첫 외부 접촉, 공식 수납, 실제 서랍과의 접촉 및 마지막 1초 그리퍼 해제를 대조한다. [채점과 짝별 비교](./drawer_location.py)

### 새로 받은 저장소에서 결과 검산

저장소 루트에서 실행한다. 로컬 Linux x86-64 Docker와 NVIDIA 드라이버를 사용했다. 실제 수집 장치는 RTX 5090이며 MuJoCo 3.2.3과 robosuite 1.4.1을 사용했다. 처음 사용하는 컴퓨터에서는 `build`로 고정한 ReSteer와 openpi의 이미지를 만든다. 저장 자료 재채점은 가중치를 다운로드하지 않고 실행할 수 있다. 이미지에 포함된 10월 환경 계획은 최초 빌드 전 기록이며, 아래 명령과 11월 실행 결과에서 실제 검증 상태를 확인할 수 있다. [Dockerfile](./Dockerfile) · [정책 파일 목록](./ARTIFACTS.json)

```sh
recipe='work/research_topics/instruction_revision/재현 방법'
archive="$recipe/results/2026-11-25-drawer-location"
sh "$recipe/resume.sh" check
sh "$recipe/resume.sh" gpu
# 처음 사용하는 컴퓨터에서
sh "$recipe/resume.sh" build

(cd "$archive" && sha256sum -c SHA256SUMS)
sh "$recipe/resume.sh" verify-drawer-location "$archive"
sh "$recipe/resume.sh" verify-middle-aperture "$recipe/results/2026-11-25-middle-aperture-layout2"
sh "$recipe/resume.sh" verify-stove-layouts "$recipe/results/2026-11-25-stove-layouts"
```

그림은 보존한 세 파일 `study.zip`, `verification.json`, `physical_replay.json`에서 생성한다. 그림을 검산한 Docker 환경의 버전은 Matplotlib 3.10.9, NumPy 1.26.4, Pillow 10.4.0이다. [그림 생성 코드](./plot_drawer_location.py)

GPU로 물리를 다시 계산하려면 새 폴더에 보고서를 쓴다. 첫 명령은 원래·교차 경로 576개를, 둘째는 직전 실험의 닫힌 조건 명령을 재생한다.

```sh
report_dir=$(mktemp -d)
sh "$recipe/resume.sh" replay-drawer-location "$archive" "$report_dir/physical.json"
sh "$recipe/resume.sh" replay-prior-closed "$archive" "$report_dir/prior.json"
cmp "$archive/prior_closed.json" "$report_dir/prior.json"
```

정책으로 같은 실험을 새로 수집할 때는 `assets`로 17개 파일의 버전과 무결성을 확인한다. 체크포인트와 토크나이저는 Docker 데이터 볼륨에 저장한다.

```sh
sh "$recipe/resume.sh" assets
work_dir=$(mktemp -d)
sh "$recipe/resume.sh" drawer-location "$work_dir/new-study"
sh "$recipe/resume.sh" verify-drawer-location "$work_dir/new-study"
```

원본 수집 폴더와 이를 압축한 파일에서 각각 새 컨테이너로 192개 원래 경로와 384개 교차 경로를 재생했다. 교차 경로당 정책 명령 540개, 재생 한 번당 교차 제어 207,360개다. 두 재생의 제어별 물리 측정, 접촉·수납 점수와 종단 상태가 일치했다. 원래 경로의 정책 관측 시점 20,736개 중 다시 렌더링한 카메라 영상이 수집 당시와 달랐던 시점은 첫 재생에서 3개, 둘째에서 6개였다. 수집 당시 외부·손목 카메라 입력 해시와 정책 응답은 원본에 보관했다. 저장소 정리 뒤 576개 경로를 다시 재생했을 때도 물리값과 접촉·수납 판정이 일치했다. 이때 카메라 영상은 수집 당시와 3/20,736시점에서 달랐다. 직전 실험의 성공 명령으로 만든 추가 재생 보고서는 보존본과 바이트 단위로 일치했다. [물리 재생과 영상 차이](./results/2026-11-25-drawer-location/physical_replay.json) · [파일 해시](./results/2026-11-25-drawer-location/SHA256SUMS)

이번 두 번의 모델 실행은 대응하는 96쌍 전부에서 540개 제어와 종단 물리 상태가 일치했다. 직전 배치 2 실험과는 원래 위치·모두 닫힘의 32쌍 모두에서 출발 물리 상태, 첫 두 카메라 영상과 로봇 상태가 같았지만 첫 제어에 수치 차이가 있었다. 쌍별 첫 제어 성분의 최대 절댓값 차이는 0.00040–0.00329였다. 두 실험 모두 닫힌 조건의 위 칸 수납은 32/32회였다. [측정 원본](./results/2026-11-25-drawer-location/study.zip) · [직전 측정 원본](./results/2026-11-25-middle-aperture-layout2/study.zip)

그래서 이번 실행 뒤에 직전 실험에서 성공한 명령 32개도 따로 검사했다. 같은 출발 상태에서 540개 제어가 전부 같은 명령열을 묶어 한 번씩 재생하고, 점수는 원래의 32회에 대응시켰다. 새 실험의 두 물체 배치에서 각각 모두 닫힘과 아래 칸만 당긴 상태에 적용했다. 원래 물체 위치에서 모두 닫혀 있을 때는 직전 실험의 종단 물리 상태와 8·15·30초 점수까지 일치해야 한다. [이전 명령 재생 코드](./replay_prior_closed.py) · [보존한 재생 결과](./results/2026-11-25-drawer-location/prior_closed.json)
