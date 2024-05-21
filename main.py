import os

from dotenv import load_dotenv
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


load_dotenv()

greetings = ['hello', 'hi', 'привет', 'здравствуйте', 'hallo', 'gamarjoba',
             'shalom', 'hola', 'namaste', 'salut', 'bonjour', 'konnichiwa']


def main():
    vk_session = vk_api.VkApi(token=os.environ['TOKEN'])
    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print(f'id{event.user_id}: "{event.text}"', end=' ')

            if event.text.lower() in greetings:
                if event.from_user: # Если написали в ЛС
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        message='Здравствуйте и до свидания! Я пока не очень умный.'
                    )

                elif event.from_chat: # Если написали в Беседе
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message='Ваш текст in chat'
                    )
            else:
                vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Я пока никак Вам не могу помочь.'
                )
                print('no results there')


if __name__ == '__main__':
    main()
 