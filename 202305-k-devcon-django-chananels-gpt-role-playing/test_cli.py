import os
import openai


# FIXME: 구동환경에 따라, 적절히 환경변수 로딩 부분을 변경해주세요.
openai.api_key = os.getenv("OPENAI_API_KEY")


messages = [
    {
        "role": "system",
        "content": (
            # 당신은 영어를 배우는 사람들을 지원하는 유용한 조수입니다. 당신의 이름은 스티브입니다.
            # 귀하가 지원하는 사용자가 영어 초보자라고 가정하십시오. 그리고 캐릭터 역할 없이 문장만 써주세요.
            "You are helpful assistant supporting people learning English. "
            "Your name is Steve. Please assume that the user you are assisting "
            "is a beginner in English. And please write only the sentence without "
            "the character role."
        ),
    }
]


def gpt_query(query: str) -> str:
    messages.append(
        {
            "role": "user",
            "content": query,
        }
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=1
    )
    assistant_message = response["choices"][0]["message"]["content"]
    messages.append(
        {
            "role": "assistant",
            "content": assistant_message,
        }
    )

    return assistant_message


gpt_query(
    # 영어로 대화를 나누자. 번역을 제공하지 않고 영어로만 답변하십시오. 그리고 발음도 적지 마세요.
    # '새 친구 사귀기'의 상황을 가정해 보겠습니다. 나는 나니까. 연기해 주었으면 하는 캐릭터는 새 친구입니다.
    # 제가 영어 초보라서 최대한 쉬운 단어를 사용하도록 해주세요. 이제 첫 문장으로 대화를 시작하세요!
    "Let's have a conversation in English. Please answer in English only "
    "without providing a translation. And please don't write down the "
    "pronunciation either. Let us assume that the situation in 'make new friends'. "
    "I am me. The character I want you to act as is new friend. Please make sure that "
    "I'm a beginner in English, so please use simple words as much as possible. "
    "Now, start a conversation with the first sentence!"
)

import sys
from tempfile import NamedTemporaryFile
from gtts import gTTS
from io import BytesIO


def say(message: str, lang: str):
    if sys.platform == "darwin":
        io = BytesIO()
        gTTS(message, lang=lang).write_to_fp(io)

        with NamedTemporaryFile() as f:
            f.write(io.getvalue())
            os.system(f"afplay {f.name}")  # macOS 전용 명령
    else:
        print(f"{sys.platform}에서는 지원하지 않습니다.", file=sys.stderr)


for message in messages[-1:]:
    print("[{role}] {content}".format(**message))

try:
    while line := input("[user] ").strip():
        if line == "!say":
            say(messages[-1]["content"], "en")
        else:
            response = gpt_query(line)
        print("[assistant] {}".format(response))
except (EOFError, KeyboardInterrupt):
    print("terminated by user.")
