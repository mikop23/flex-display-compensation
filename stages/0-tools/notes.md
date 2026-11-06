## 이미지 = 배열
- img[행, 열] = img[y, x]. 원점은 왼쪽 위, y는 아래로 커짐
- 컬러 사진은 (H, W, 3). OpenCV는 B, G, R 순서 → 그릴 땐 cv2.cvtColor(img, cv2.COLOR_BGR2RGB)---세 개의 배열 (B,R,G)가 겹쳐있다고 생각하자
- 채널 하나 꺼내기: img[:, :, 번호]

## 브로드캐스팅 / reshape
- 모양을 오른쪽 끝부터 비교. 같거나, 1이거나, 없으면 복사해서 늘림
- (100,) = 가로 한 줄, (100, 1) = 세로 한 줄
- reshape는 개수·순서 그대로 모양만 바꿈. 새 배열을 돌려주니까 다시 담기

## 밝기·대비
- 밝기: img + b / 대비: k × (img − 128) + 128 (중간 기준 대비 시키기)
- 계산 직후 np.clip(x, 0, 255)

## 휘도
- 휘도 ≈ 0.299R + 0.587G + 0.114B (눈은 초록에 가장 민감). 가중치 합 = 1
- 측정: 밝게 보이는 색에 큰 가중치 / 보정: 밝게 보이는 색에 적은 입력
- 엄밀히는 감마가 걸린 값에 적용하면 근사치(luma) → 2단계에서 다시

## 그림 그리기
- imshow는 자동으로 최소~최대에 맞춤 → vmin, vmax 고정
- (H, W)는 colormap으로, (H, W, 3)은 진짜 색으로 그림. 3채널은 uint8이면 0~255, float면 0~1
- jet은 가짜 경계를 만듦 → 분석엔 inferno, viridis
- colorbar(fraction=0.046, pad=0.04)로 막대 크기 맞춤
- savefig는 show 앞에

## 문법 실수 모음
- shape, dtype은 괄호 없음 / min(), max(), reshape()는 괄호 있음
- 파이썬 기본 min(배열) 말고 배열.min()
- 크기를 숫자로 박지 말고 : 또는 img.shape 사용

## 평가 지표 (common/metrics.py)

- PSNR = 10·log₁₀(255²/MSE), MSE = 칸별 차이 제곱의 평균. 높을수록 비슷(dB)
- SSIM = 7×7 조각마다 (평균 밝기 × 변화 크기(표준편차) × 변화 패턴(상관)) → 조각 전체 평균. 1에 가까울수록 비슷
- 실험 (test.jpg 흑백)
  - 밝기 +10: PSNR 28.13 dB, SSIM 0.990 → SSIM은 밝기 변화에 관대
  - 1픽셀 밀기: PSNR 22.57dB, SSIM 0.604 → 둘 다 위치 어긋남에 약함
- 그래서 기하 보정 평가는 PSNR·SSIM 말고 픽셀 위치 오차를 따로 재야 함
- SSIM 설정: scikit-image structural_similarity 기본값 (7×7 균일 창, K1=0.01, K2=0.03), data_range=255. 원논문(Wang 2004)은 11×11 가우시안이라 값이 다를 수 있음