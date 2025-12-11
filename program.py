from deep_translator import GoogleTranslator
import speech_recognition as sr
import time
import sys

recognizer = sr.Recognizer()
microphone = sr.Microphone()

#음성 텍스트를 번역함.(입력 값은 텍스트,번역할 언어)
def translator(text,target_language):
    translations = {}
    for lang in target_language:
        try:
            translated = GoogleTranslator(source='ko', target=lang).translate(text)
            translations[lang] = translated
        except Exception as e:
            translations[lang] = "Error : {}".format(e)
    return translations

#번역한 언어를 출력하는 함수
def out_put(result):
    print('번역 결과 : \n')
    print(result)
    

#음성 인식 여부 확인
def callback(rcognizer , audio):
    global target_language
    try:
        text = recognizer.recognize_google(audio, language="ko-KR")
        print("실시간 텍스트: {} \n".format(text))
        results = translator(text,target_language)
        out_put(results)
    
    except sr.UnknownValueError:
        print("답없는 오디오")
        
    except sr.RequestError as e:
        print("연결 안됨; {0}".format(e))

#번역할 언어 입력
translate_to_language = input("ex) English->en,japan->ja(앞 두 들자만 입력) 예외:Chinese(Mandarin) -> zh-cn : ")

#번역할 언어가 없으면 띄우는 오류
if not translate_to_language.strip():
    print("you not input to translate_language")

target_language = [lang.strip().lower() for lang in translate_to_language.split(',')]

time_num = int(input("오디오 시간을 입력해주세요 : "))


print("소음조정 잠시 멈춤")
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
print("소음조정 끝! \n")

print("음성인식 시작! {}초동안...\n".format(time_num))
#마이크 컨텍스트 관리
stop_listening = recognizer.listen_in_background(microphone, callback)

time.sleep(time_num) 

stop_listening(wait_for_stop=False)
