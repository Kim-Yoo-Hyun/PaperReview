# LIBERO 서랍 실험 재현

<a id="drawer-bowl-position"></a>

## 두 배치에서 그릇의 시작 위치 교환

LIBERO-Goal 배치 2와 3의 복귀 자세를 각각 두 개씩 복원한다. 아래 서랍의 실제 폭은 각 자세의 완전 개방값(159.84–159.92 mm)이다. 그릇을 해당 배치의 원래 위치에 두거나 상대 배치에서 측정한 수평 좌표로 옮긴다. 같은 자세 안에서는 그릇 자유관절의 수평 위치 두 개를 제외한 전체 적분 상태가 일치해야 한다. 그릇 높이·방향, 접시, 그리퍼, 서랍 폭, 탁자 지지와 초기 충돌을 확인하고, 별도의 20제어 정지 검사에서 드리프트를 측정한다. [사전 설계](./drawer/drawer_bowl_position.json) · [출발 상태 검산](./drawer_bowl_position_starts.py)

각 배치·자세·그릇 위치에서 76 mm로 실제 열어 본 장면도 만들어 외부·손목 카메라의 기준 영상을 등록한다. 정책은 완전히 열린 아래 서랍에서 시작한다. 실제 폭을 계속 보여주거나, 정책 시작 후 0.5–1초 또는 0–1초에 두 카메라에 76 mm를 보여준다. 각 질의는 다섯 제어(0.25초)를 담당한다. 첫 과제 접촉 이후에는 실제 영상을 쓴다. 자세·시드·모델 실행을 맞춰 두 그릇 위치 각각에서 뒤 구간과 실제 폭 대조의 첫 접촉을 비교한 뒤, 두 위치의 변화 여부를 같은 쌍 안에서 대조한다. [실행·채점 코드](./drawer_bowl_position.py)

```sh
recipe='work/research_topics/instruction_revision/재현 방법'
archive="$recipe/results/2026-11-26-drawer-bowl-position"
(cd "$archive" && sha256sum -c SHA256SUMS)
sh "$recipe/resume.sh" verify-drawer-bowl-position "$archive"
report_dir=$(mktemp -d)
sh "$recipe/resume.sh" replay-drawer-bowl-position "$archive" "$report_dir/replay.json"
# 체크포인트에서 정책을 새로 실행할 때
sh "$recipe/resume.sh" drawer-bowl-position "$report_dir/new-study"
```

독립 예비 검사와 본 수집에서 16개 시작 상태의 물리 해시와 기준 영상이 일치했다. 그릇을 원래 위치에 둔 완전 개방·76 mm 장면의 외부·손목 영상 16장도 이전 두 배치의 보관본과 일치했다. 완전 개방 상태에서 그릇 위치를 바꾸면 외부 영상은 548–549픽셀, 손목 영상은 2,471–2,738픽셀이 달라졌다(각 224×224). 모든 정지 검사에서 서랍과 물체의 최대 이동은 0 mm였다. [물리·카메라 검산](./results/2026-11-26-drawer-bowl-position/verification.json)

2026년 11월 26일 로컬 RTX 5090에서 `pi05_libero`로 384경로, 41,472회 정책 질의를 수집했다. 첫 네 질의의 1,536시점에서 물리 상태와 자기 폭 영상을 대조했다. 한 카메라에서 최대 한 픽셀이 달라 자기 영상을 다시 그린 시도는 25회였고, 반대 폭 영상은 배정한 768질의 전부에 전달됐다. 두 모델 실행의 192쌍은 첫 접촉과 15초·30초 점유가 모두 일치했다. 첫 20개 제어는 191쌍, 종단 물리 해시는 184쌍이 같았다. [서버 수신 기록·런타임·원본 제어](./results/2026-11-26-drawer-bowl-position/study.zip)

원래 그릇 위치에서 새로 수집한 192경로를 과거 경로와 대응시켰을 때 첫 20개 제어, 첫 접촉, 15초 점유는 각각 192/192쌍, 30초 점유는 191/192쌍이 같았다. 배치 2의 첫 1초 전체 교환 한 쌍은 과거에는 30초 미수납, 이번에는 아래 칸 수납이었다. 새 보관본의 모든 경로와 원래 위치의 과거 192경로에서 그리퍼와 닿은 물체의 지오메트리 ID 및 칸별 점유 기록을 독립적으로 읽어 집계를 확인했다. [배치별 대조 일치와 수납 집계](./results/2026-11-26-drawer-bowl-position/verification.json)

실제 폭 대조와 뒤 구간 교환의 첫 10개 제어(교환 전)는 127/128쌍에서 일치했다. 나머지 한 쌍은 배치 3에서 그릇을 옮긴 조건(`drawer-2-3-k0`, 두 번째 모델, 시드 2)이었다. 두 번째 질의에서 물리 해시가 같은데도 서버에 전달된 영상이 달랐고, 제어 성분의 최대 차이는 0.00302였다. 두 경로 모두 그릇을 먼저 접촉하고 아래 칸에 수납했다. 해당 자세·모델·시드 조합을 뺀 민감도 검사에서도 배치 3의 첫 접촉 변화는 두 그릇 위치 모두 0/31쌍이었다. [경로와 서버 수신 원본](./results/2026-11-26-drawer-bowl-position/study.zip)

수집 폴더와 압축 보관본에서 저장 명령을 각각 재생했다. 두 재생 모두 384경로의 후속 207,360개 제어에서 접촉·수납 기록과 종단 물리 해시가 수집값과 일치했다. 영상을 다시 그리면 41,472개 질의 중 각각 26건과 21건에서 픽셀 차이가 있었고, 첫 네 질의에 속한 경우는 두 재생에서 각각 5건이었다. 배포한 그림은 압축본의 `figure/plot_drawer_bowl_position.py`로 다시 생성해 PNG 해시가 일치하는지 확인했다. [두 재생의 경로별 기록](./results/2026-11-26-drawer-bowl-position/physical_replay.json) · [그림 생성기](./plot_drawer_bowl_position.py) · [체크섬](./results/2026-11-26-drawer-bowl-position/SHA256SUMS)

<a id="drawer-view-window-layout3"></a>

## 배치 3에서 같은 앞·뒤 영상 교환 재현

LIBERO-Goal 배치 3의 두 종단에서 각각 저장된 서랍 열기 160개 제어와 팔 복귀 60개 제어를 재생한다. 출발 종단과 복귀 종단의 물리 해시를 확인한 뒤, 자세마다 원래의 완전 개방 폭을 잰다. 그릇·접시의 원래 위치와 배치 2의 이동량을 순서대로 검사해 두 자세의 네 폭 조건 모두에서 탁자가 두 물체를 지지하고 초기 충돌이 없는 위치를 고른다. 모두 닫힌 장면을 기준으로 조건마다 슬라이드 위치 하나만 달라지는지, 두 카메라의 반대 폭 영상이 구별되는지, 별도 20개 제어 동안 서랍·물체가 안정적인지 검사한다. [원본 종단 추출](./verify_stove_fingers.py) · [설계](./drawer/drawer_view_window_layout3.json) · [물리 검사와 배치 간 집계](./drawer_view_window_layout3.py)

정책 입력, 시드, 시계와 접촉 이후의 교환 중단 규칙은 [배치 2](#drawer-view-window)와 같다. 네 조건에서 자기 폭, 앞 0.5초, 뒤 0.5초, 첫 1초 전체를 비교한다. 접촉 대상은 서랍 세 칸과 그릇이며, 동시 접촉은 대상 집합으로 기록한다. 최초 수납은 한 번이라도 그릇이 서랍 영역에 들어간 시점이다. 15초와 30초에는 그 시점의 실제 점유 칸을 다시 판정한다.

```sh
recipe='work/research_topics/instruction_revision/재현 방법'
archive="$recipe/results/2026-11-26-drawer-view-window-layout3"
(cd "$archive" && sha256sum -c SHA256SUMS)
sh "$recipe/resume.sh" verify-drawer-view-window-layout3 "$archive"
report_dir=$(mktemp -d)
sh "$recipe/resume.sh" replay-drawer-view-window-layout3 "$archive" "$report_dir/replay.json"
# 새 정책 실행
sh "$recipe/resume.sh" drawer-view-window-layout3 "$report_dir/new-study"
```

물리 검사를 독립적으로 반복했을 때 출발 물리 해시는 같았지만, 가운데 완전 개방 장면의 손목 영상에서 초기 렌더 두 장이 한 픽셀 달랐다. 단일 영상을 기준으로 삼았던 첫 수집은 제외했다. 최종 수집에서는 제어를 진행하기 전에 출발마다 두 카메라를 아홉 번 읽고 과반수의 해시 쌍을 기준으로 등록했다. 첫 질의에서 현재 폭과 정책에 보낼 폭의 영상이 각각 대응하는 실제 영상과 픽셀 단위로 같아야 한다. 다르면 같은 물리 상태에서 다시 읽고 시도별 해시를 남긴다. [시작 영상 등록](./drawer_view_window_layout3.py) · [렌더링과 입력 대조](./drawer_view_render.py)

2026년 11월 26일 로컬 RTX 5090에서 `pi05_libero`로 512경로와 서버 수신 기록 55,296건을 수집했다. 최종 출발 검사에서는 닫힘 대조를 포함한 10개 상태의 영상 쌍 90개가 각 상태의 기준과 전부 일치했다. 여덟 정책 출발 상태를 별도 프로세스에서 복원해 실제 폭·반대 폭의 첫 입력도 확인했다. 2,048개 교환 검사 시점 중 28시점에서 자기 영상 간 차이로 재시도했고(거절한 렌더 98회, 카메라당 최대 2픽셀), 첫 질의에서는 기준 영상과 다시 맞춘 시도가 3회였다. 반대 폭은 배정한 1,024질의 전부에 전달됐다. [런타임·카메라·측정 원본](./results/2026-11-26-drawer-view-window-layout3/study.zip)

두 모델 실행에서 대응하는 256쌍 중 첫 접촉과 30초 도착지는 각각 255쌍, 15초 도착지는 256쌍, 첫 20개 제어는 254쌍, 종단 물리 해시는 235쌍이 일치했다. 첫 0.5초에 같은 폭을 배정한 조건끼리 대응시키면 실제 폭과 뒤 구간은 128/128쌍에서 첫 10개 제어가 같았고, 앞 구간과 1초 전체는 126/128쌍에서 같았다. 남은 두 쌍은 첫 5개 제어가 같았고 두 번째 질의에서 물리 해시가 같은 상태로 서로 다른 영상을 받았다. 두 번째 5개 제어의 성분별 최대 절댓값 차이는 각각 0.00391과 0.00247이었다. [조건·경로별 검산](./results/2026-11-26-drawer-view-window-layout3/verification.json)

수집 폴더와 압축 보관본에서 각각 512경로의 저장 명령을 Docker로 재생했다. 두 재생에서 후속 276,480개 제어의 접촉·수납 기록, 질의별 물리 상태와 512개 종단 해시가 수집 당시와 일치했다. 영상을 다시 그렸을 때 수집값과 다른 질의는 55,296건 중 각각 52건과 43건이었고, 이 중 첫 네 질의에 속한 경우는 각각 9건과 4건이었다. 두 배치의 압축 원본에서 접촉 대상·최초 수납 시점·15초와 30초 점유·전송 영상을 독립적으로 다시 집계했다. 보관한 그림 생성기로 같은 PNG 해시를 얻었다. [두 재생의 기록](./results/2026-11-26-drawer-view-window-layout3/physical_replay.json) · [그림 생성기](./plot_drawer_view_window_layout3.py) · [체크섬](./results/2026-11-26-drawer-view-window-layout3/SHA256SUMS)

<a id="drawer-view-window"></a>

## 0.5초 영상 교환을 앞·뒤 구간으로 옮기기

배치 2의 두 복귀 자세에서 가운데와 아래 서랍을 각각 76 mm 또는 약 160 mm 연다. 각 실제 폭에서 같은 자세·시드·모델 실행으로 네 경로를 짝짓는다. 정책 시작 후 0–0.5초 교환(첫 두 질의), 0.5–1초 교환(다음 두 질의), 자기 폭 재렌더링, 0–1초 전체 교환이다. 매 질의에서 외부·손목 영상을 현재 자세로 다시 그리며, 과제 접촉이 발생한 뒤의 다음 질의부터 실제 영상을 쓴다. 서버 수신 기록과 물리 상태 검사는 [교환 시간 실험](#drawer-view-duration)과 같다. [이번 배정·판정 기준](./drawer/drawer_view_window.json) · [실행·채점 코드](./drawer_view_duration.py)

앞·뒤 비교는 양쪽 모두 배정된 전체 쌍을 사용한다. 자기 폭과 1초 전체 교환의 첫 접촉이 다른 쌍에 한해, 앞·뒤 각각에 대해 자기 폭과 일치, 전체 교환과 일치, 두 대조 모두와 다름을 센다. 동시 접촉은 같은 대상 집합이어야 일치한다. 첫 접촉·최초 수납은 정책 시작부터, 15초·30초 도착지는 3초 자세 복귀를 포함해 잰다.

```sh
recipe='work/research_topics/instruction_revision/재현 방법'
archive="$recipe/results/2026-11-26-drawer-view-window"
(cd "$archive" && sha256sum -c SHA256SUMS)
sh "$recipe/resume.sh" verify-drawer-view-window "$archive"
report_dir=$(mktemp -d)
sh "$recipe/resume.sh" replay-drawer-view-window "$archive" "$report_dir/replay.json"
# 체크포인트에서 정책을 다시 실행할 때
sh "$recipe/resume.sh" drawer-view-window "$report_dir/new-study"
```

2026년 11월 26일 로컬 RTX 5090에서 체크포인트 `pi05_libero`로 512경로, 55,296회 정책 질의를 수집했다. 각 경로의 첫 네 질의인 2,048시점에서 두 자기 영상과 원래 물리 해시를 대조했다. 세 시점에서 카메라당 한 픽셀 차이로 한 번씩 다시 그렸으며, 일치한 입력으로 추론했다. 반대 폭은 예정한 1,024질의 전부에 전달됐고 접촉에 의한 조기 교환 종료는 0회였다. [수신 기록·환경·원자료](./results/2026-11-26-drawer-view-window/study.zip)

같은 자세·시드·조건을 맞춘 두 모델 실행에서 첫 접촉 결과는 256/256쌍, 첫 20개 제어·15초 수납·30초 수납은 각각 255/256쌍, 종단 물리 상태는 238/256쌍이 일치했다. 이번 자기 폭 및 전체 교환 대조군을 직전 실험과 맞췄을 때 첫 접촉은 각각 128/128쌍이 같았고, 30초 수납은 각각 128/128쌍과 126/128쌍이 같았다. 앞·뒤 조건의 첫 20개 명령은 다섯 개씩 묶어 비교했으며 그림에서 같은 서랍의 두 실제 폭은 묶음별 중앙값이 겹친다. [조건별 검산](./results/2026-11-26-drawer-view-window/verification.json) · [그림 생성기](./plot_drawer_view_window.py)

수집 폴더와 압축 원본에서 각각 512경로의 저장 명령을 새 Docker 컨테이너로 재생했다. 재생마다 276,480개 후속 제어의 접촉·수납 기록, 질의별 물리 상태와 경로별 종단 상태가 수집값과 같았다. 다시 그린 영상은 55,296개 질의 시점 중 첫 재생 26시점, 두 번째 재생 47시점에서 수집 기록과 차이가 있었다. 그중 첫 네 질의에 속한 것은 각각 1시점과 2시점으로, 모두 실제 가운데 76 mm의 뒤 구간 교환이 시작되는 0.5초였다. 정책이 수집 당시에 받은 두 영상은 서버 수신 해시로 검산했다. 별도로 압축 원본에서 모든 배정·접촉·수납 집계를 다시 계산했고, 보관한 그림 생성기로 같은 PNG 체크섬을 얻었다. [두 재생의 기록](./results/2026-11-26-drawer-view-window/physical_replay.json) · [파일 체크섬](./results/2026-11-26-drawer-view-window/SHA256SUMS)

<a id="drawer-view-duration"></a>

## 반대 폭의 영상을 첫 0.25초 또는 1초 동안 보여주기

같은 자세·시드·모델 실행·실제 폭에서 자기 폭, 1질의 교환, 4질의 교환을 짝짓는다. 외부·손목 카메라를 함께 다룬다. 매 질의에서 현재 MuJoCo 데이터를 복사하고, 반대 폭을 그릴 때는 별도 복사본에서 대상 서랍의 슬라이드 위치를 바꿔 운동학을 계산한다. 해당 서랍의 월드 좌표만 렌더링용 데이터에 반영해 팔·그릇·접시·카메라가 그 순간의 자세를 유지하게 한다. 재렌더링한 자기 영상과 실제 입력의 픽셀 배열, 렌더링 전후 원래 장면의 물리 해시를 비교한다. 첫 질의에서는 반대 폭 영상도 [직전 교환 실험](#drawer-first-camera)의 원본과 대조한다. [사전 설계](./drawer/drawer_view_duration.json) · [렌더링 코드](./drawer_view_render.py)

예비 실행에서 같은 자세의 손목 영상에 한 픽셀 차이가 관측됐다. 자기 영상이 실제 입력과 다르면 물리를 멈춘 채 복제 영상을 최대 네 번 비교한다. 필요하면 같은 물리 해시와 로봇 상태에서 실제 영상을 최대 두 번 다시 읽는다. 어긋난 시도는 카메라별 픽셀 수와 해시를 기록하고, 두 카메라가 모두 정확히 일치해야 정책에 질의한다. [렌더링 판정 기준](./drawer/drawer_view_duration.json)

과제 접촉은 그리퍼가 위·가운데·아래 칸 또는 그릇에 닿은 첫 제어로 판정한다. 교환 시간이 끝나거나 그 접촉이 발생한 뒤의 다음 질의에서는 해당 경로의 실제 영상을 공급한다. 서버 수신 기록에서 두 영상, 로봇 상태, 지시, 난수, 반환 명령을 검산한다. 첫 접촉과 첫 수납 시점은 정책 시작부터 20 Hz 제어 단위로 기록한다. 15초·30초의 도착지 판정에는 시작 전 3초의 자세 복귀가 포함된다. [실행·채점 코드](./drawer_view_duration.py)

```sh
recipe='work/research_topics/instruction_revision/재현 방법'
archive="$recipe/results/2026-11-26-drawer-view-duration"
(cd "$archive" && sha256sum -c SHA256SUMS)
sh "$recipe/resume.sh" verify-drawer-view-duration "$archive"
report_dir=$(mktemp -d)
sh "$recipe/resume.sh" replay-drawer-view-duration "$archive" "$report_dir/replay.json"
# 체크포인트에서 정책을 다시 실행할 때
sh "$recipe/resume.sh" drawer-view-duration "$report_dir/new-study"
```

2026년 11월 26일 로컬 RTX 5090에서 배치 2, 체크포인트 `pi05_libero`, 두 복귀 자세와 여덟 시드로 384경로를 수집했다. 총 41,472회 질의 중 첫 네 질의 1,536회에서 두 자기 영상이 실제 입력과 같았고, 640회는 반대 폭의 두 영상을 공급했다. 여섯 번의 재렌더링 불일치는 세 질의에서 발생했고 카메라당 최대 한 픽셀이었다. 한 질의에서 실제 영상을 한 번 다시 읽었다. 1,536회 모두 렌더링 전후 원래 장면의 물리 해시가 유지됐고, 접촉에 의한 조기 교환 중단은 0회였다. [실행별 검산](./results/2026-11-26-drawer-view-duration/verification.json) · [원자료·수신 기록·환경](./results/2026-11-26-drawer-view-duration/study.zip)

각 경로는 3초의 자세 복귀 뒤 27초간 540개 정책 제어를 실행했다. 두 모델 실행의 192쌍에서 첫 20개 제어·첫 접촉 대상·15초 수납은 192쌍, 30초 수납은 191쌍, 종단 물리 상태는 176쌍이 같았다. 0.25초 조건을 직전 실험의 두 카메라 교환과 맞춘 128쌍에서는 첫 접촉과 30초 수납이 모두 일치했다. [직전 실험](#drawer-first-camera) · [결과 그림 생성기](./plot_drawer_view_duration.py)

수집 폴더와 압축 원본에서 각각 새 Docker 컨테이너로 384경로 전체를 물리 재생했다. 두 재생 모두 207,360개 후속 제어의 접촉·수납 기록, 각 질의의 물리 상태, 모든 경로의 종단 상태가 수집값과 일치했다. 카메라 재렌더링은 41,472개 질의 시점 중 두 재생에서 각각 22시점이 수집값과 달랐다. 이 차이는 모두 각 경로의 첫 네 질의 이후에 발생했다. 그림도 보관한 소스에서 다시 생성해 PNG 체크섬을 대조했다. [두 재생의 기록](./results/2026-11-26-drawer-view-duration/physical_replay.json) · [파일 체크섬](./results/2026-11-26-drawer-view-duration/SHA256SUMS)

<a id="drawer-first-camera"></a>

## 실제 서랍 폭을 고정하고 첫 카메라 입력만 교환하기

배치 2의 가운데·아래 칸 각각에 76 mm와 약 160 mm를 적용한다. 직전 폭 실험의 두 복귀 자세에서 여덟 출발 상태와 카메라 영상 16장을 가져온다. 각 경로를 재구성할 때 출발 물리 상태, 그리퍼와 물체 자세, 실제 렌더링한 첫 영상 해시를 원본과 대조한다. 자기 영상 대조에서도 두 PNG를 다시 읽어 정책에 보낸다. 처치에서는 같은 자세·같은 칸에서 폭만 다른 장면의 외부 영상, 손목 영상 또는 두 영상을 첫 질의에만 넣는다. 5제어(0.25초) 뒤부터는 각 경로가 도달한 상태의 실제 두 영상을 사용한다. [사전 설계](./drawer/drawer_first_camera.json) · [실행과 채점 코드](./drawer_first_camera.py)

각 대조쌍의 시작 물리 상태를 동일하게 두고, 첫 명령부터는 서랍과 그릇을 정상 동역학으로 움직인다. 서버가 받은 영상·로봇 상태·지시·난수와 반환한 명령을 매 질의마다 대조한다. 첫 접촉은 그리퍼가 서랍의 움직이는 형상이나 그릇에 처음 닿은 제어 시점으로 센다. 수납은 공식 과제 영역 안에 그릇이 있는지 15초와 30초에 판정한다. 두 시점 모두 3초의 자세 복귀를 포함한다. 각 시행에 108회 정책 질의와 540개 후속 제어가 있다. 두 복귀 자세에 같은 여덟 난수 시드를 적용하고, 두 번째 모델 실행에서는 조건 순서를 뒤집는다.

```sh
recipe='work/research_topics/instruction_revision/재현 방법'
archive="$recipe/results/2026-11-25-drawer-first-camera"
(cd "$archive" && sha256sum -c SHA256SUMS)
sh "$recipe/resume.sh" verify-drawer-first-camera "$archive"
report_dir=$(mktemp -d)
sh "$recipe/resume.sh" replay-drawer-first-camera "$archive" "$report_dir/physical.json"
# 같은 정책으로 다시 수집할 때
sh "$recipe/resume.sh" drawer-first-camera "$report_dir/new-study"
```

저장 자료를 재채점할 때는 현재 실험과 [직전 개방 폭 실험](#drawer-width)의 측정 원본을 함께 둔다. 새로 수집할 때는 아래 환경 설치 절차의 체크포인트와 로컬 NVIDIA GPU를 사용한다. 기록한 집계를 그리는 코드는 [결과 그림 생성기](./plot_drawer_first_camera.py)에 있다.

11월 25일 로컬 RTX 5090에서 512경로를 수집했다. 동일한 시작 조건을 두 모델 실행 사이에 맞춘 256쌍 전부에서 첫 다섯 제어·첫 접촉 대상·30초 도착지가 같았다. 15초 수납은 255/256쌍, 540개 제어 전체와 종단 물리 상태는 241/256쌍이 일치했다. 직전 폭 실험과 이번 자기 영상 대조군을 맞춘 128쌍은 출발 물리 상태·두 첫 영상·로봇 상태가 같았다. 두 실험 사이 첫 명령의 최대 성분 차이는 쌍별 0.00040–0.00494였고, 첫 접촉과 30초 도착지는 128/128쌍, 15초 수납은 124/128쌍이 일치했다. [측정 원본](./results/2026-11-25-drawer-first-camera/study.zip) · [조건별 검산](./results/2026-11-25-drawer-first-camera/verification.json)

수집 폴더와 압축 원본에서 각각 새 Docker 컨테이너로 512경로를 전부 물리 재생했다. 11월 26일 두 번째 검산을 마쳤다. 재생마다 276,480개 후속 제어의 접촉·수납 기록, 질의 시점의 물리 상태, 종단 상태가 수집값과 일치했다. 재렌더링한 영상은 관측 55,296시점 중 각각 28개와 27개에서 수집값과 달랐고, 두 재생 모두 첫 영상은 512/512회 일치했다. `physical_replay.json`의 `archive_repeat`에 두 번째 재생의 영상 차이와 결과 해시를 보존했다. [두 재생의 기록](./results/2026-11-25-drawer-first-camera/physical_replay.json) · [파일 체크섬](./results/2026-11-25-drawer-first-camera/SHA256SUMS)

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
