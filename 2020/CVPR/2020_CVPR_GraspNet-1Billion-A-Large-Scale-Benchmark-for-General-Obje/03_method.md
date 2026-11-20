# Method - GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html) · [원문](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf)

## 입력과 계산

장면과 물체 좌표를 연결해 파지 주석을 구성하고, 후보 자세를 물리적 기준으로 평가한다. 기준 네트워크는 점군에서 접근 방향과 그 밖의 파지 파라미터를 나누어 예측한다. §§3–4.

## 적용 조건

분석적 파지 점수와 실물 파지의 대응은 논문이 시험한 물체·그리퍼와 조건에서 평가했다.
