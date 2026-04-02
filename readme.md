# 스캐너 설정

```
brew install sane-backends
scanimage -L
```

위 명령어를 통해서 스캐너가 정상적으로 인식되는지 확인한 후에, 아래 명령어로 python-sane과 Pillow를 설치합니다.

```sh
CFLAGS="-I/opt/homebrew/include" LDFLAGS="-L/opt/homebrew/lib" pip3 install python-sane Pillow
```
