import requests
import os

# DeepL API 키 설정
DEEPL_API_KEY = '여기에_당신의_API_키를_입력하세요'
DEEPL_API_URL = "https://api.deepl.com/v2/translate"

def translate_html(html_content, target_lang='KO'):
    """HTML 내용을 대상 언어로 번역합니다, HTML 구조는 유지됩니다."""
    data = {
        'auth_key': DEEPL_API_KEY,
        'text': html_content,
        'target_lang': target_lang,
        'tag_handling': 'html'
    }
    response = requests.post(DEEPL_API_URL, data=data)
    result = response.json()
    return result['translations'][0]['text']

def translate_directory_html_files(directory_path):
    """지정된 디렉토리 내의 모든 HTML 파일을 번역합니다."""
    # 'ko' 디렉토리 생성 (존재하지 않을 경우)
    output_directory = os.path.join(directory_path, 'ko')
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # 디렉토리 내의 모든 파일을 순회
    for filename in os.listdir(directory_path):
        if filename.endswith('.html'):
            file_path = os.path.join(directory_path, filename)
            
            # HTML 파일 읽기
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            # HTML 내용 번역
            translated_html = translate_html(html_content)
            
            # 번역된 HTML 저장
            output_file_path = os.path.join(output_directory, filename)
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(translated_html)

# 예시 디렉토리 내의 HTML 파일 번역 실행
#translate_directory_html_files('example_directory')

if __name__ == "__main__":
    # 예시 디렉토리 내의 HTML 파일 번역 실행
    translate_directory_html_files('example_directory')
