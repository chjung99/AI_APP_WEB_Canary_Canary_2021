* msg_handler based on 'Asyncio'
기존 asyncio 방식으로 챗봇의 기능을 모방하려는 시도 => 실패
- msg_handler(asyncio), utils

* msg_handler based on 'Threading' : Thread 기반 병렬 프로세스
So.. Threading 모듈을 활용한 사용자의 DM을 읽어오는 동시에 사용자들의 Request를 처리하는 프로세스 구상 => 성공
- msg_handler(multi-thread), utils_mp


사용방법
* 인스타그램 계정 생성 후 아이디와 비밀번호를 
AI_APP_WEB_Canary_Canary/APP(BE)/instagram_chatbot/run_chatbot/utils/instagram_config.json 
경로에 JSON 형식에 맞게 저장

* instagram_chatbot/run_chatbot의 msg_handler(multi-thread).py를 실행
> python3 msg_handler(multi-thread)
