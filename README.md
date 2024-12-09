# NVIDIA Jetson Orin NX TensorRT 활용
Jetson 보드에서 objet detection 활용한 간단한 프로젝트 진행

## 최적화 환경 세팅 및 Some Tips!
torch, torchvision은 링크에서
https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048

Ultralytics는 가장 최신 받아도 상관 없는데
Ultralytics 깔면서 자동으로 Numpy 업그레이드 되있는거 보드의 tensorrt 버전에 맞춰서 1.21.6으로 다운그레이드

onnx랑 onnx 깔때 알아서 깔리는 protobuf는 최신이어도 무관. onnxslim도 그냥 최신

윈도우에서 .engine 파일로 변환해서 옮기려면 윈도우의 tensorRT 버전도 보드의 8.5.2.2에 맞춰 줘야하는데,
그냥 pt 파일 옮겨서 보드에서 다 변환하는게 가장 편함
