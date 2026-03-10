#!/bin/bash

# 현재 디렉토리 기준으로 PYTHONPATH에 package와 sim2real을 추가
export PYTHONPATH=$(pwd)/package:$(pwd)/sim2real:$PYTHONPATH

# 실행
python3 sim2real/run.py
