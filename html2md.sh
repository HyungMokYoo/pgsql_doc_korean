#!/bin/bash

# pandoc이 설치되어 있는지 확인
if ! command -v pandoc &> /dev/null; then
    echo "pandoc could not be found. Please install pandoc before running this script."
    echo "For example, on Ubuntu or Debian, you can install pandoc with: sudo apt install pandoc"
    exit 1
fi

# markdown 디렉토리가 없으면 생성
if [ ! -d "markdown" ]; then
  mkdir markdown
fi

# 현재 디렉토리의 모든 .html 파일을 순회
for file in *.html; do
  # 파일 이름에서 확장자를 제외한 기본 이름 추출
  filename=$(basename "$file" .html)
  # pandoc을 사용하여 각 파일을 Markdown으로 변환하고, 결과를 markdown 디렉토리에 저장
  pandoc -s "$file" -o "markdown/${filename}.md"
done

echo "Conversion completed."
