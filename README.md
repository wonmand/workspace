# Project
k8s 환경에서 fastapi + uvicorn을 이용한 old IAM User Access key check

## 개발 환경
- `Docker`
- `minikube`
- `python3.12`
- `fastapi`
- `uvicorn`
  
## 실행 방법 (Mac 기반)
### Docker Desktop 설치
```shell
https://docs.docker.com/desktop/install/mac-install/
```
### Minikube 설치 및 실행
```shell
brew install minikube
minikube start
```
### kubectl 설치
```shell
brew install kubernetes-cli or bre install kubectl
```
### Minikube에서 local docker image 사용하기 위한 설정 추가 및 image build
```shell
eval $(minikube -p minikube docker-env)
docker build -t fastapi:v1 .
```
### Deployment, Service 생성
```shell
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
### Minikube를 이용한 서비스 터널링
Minikube 환경에서는 Service type이 Loadbalancer일 경우 External-IP를 할당 받지 못해서 터널링 필요
```shell
minikube service myapp-service
```
