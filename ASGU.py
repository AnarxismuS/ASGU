import vk_api
import time
import re

vk=vk_api.VkApi(token='106f6cfdb021cc011a00c258f777a3d57a28fcef29e3a2f6b702428c8a637ba88ee4b18745df0fdbc8046')
vk._auth_token()

values = {'out': 0,'count': 100,'time_offset': 60}
response=vk.method('messages.get', values)

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

def search_partial_text(src, dst):
    global procent
    dst_buf = dst
    result = 0
    for char in src:
     if char in dst_buf:
        dst_buf = dst_buf.replace (char, '', 1)
        result += 1
        r1 = int (result / len (src) * 100)
        r2 = int (result / len (dst) * 100)
        procent = (r1 if r1 < r2 else r2)
        if procent == 100:
            write_msg (item['user_id'], 'И тебе привет! Как дела?!)')
        elif procent <= 99:
            write_msg (item['user_id'], 'Привет но пиши грамотней.')
        elif procent <= 40:
            write_msg (item['user_id'], 'Не понимаю')

i=0
while  True:
    i+=1
    if i>=2:
        break
    response=vk.method('messages.get', values)
    if response['items']:#сохраняем последнее сообщение
        values['last_messages_id']=response['items'][0]['id']
        #Обрабатываем только новые сообщение,сохраняем последнее айди
    for item in response['items']:
        hailist=['привет', 'дарова', 'здарова', 'хай', 'дратути', 'привествую', 'здавствуйте']
        allresults= re.findall(response['items'], hailist)
        if response['items'][0]['body'].lower() in allresults:
        # Вся суть тут брат, в этой строке входящее сообщение из контахта
            write_msg (item['user_id'], 'И тебе привет! Как дела?)')
            print(allresults)

        whatlist=['как дела?','как ты?','как оно?','как делишки?','как ваши дела?','как здоровье?','как настроение?']
        if response['items'][0]['body'].lower()in whatlist:
           write_msg(item['user_id'],'Отлично! Теперь я развернута на хероку, и буду работать 16 часов в сутки!\nА у тебя?')
        else:
            search_partial_text (response, whatlist)

        personlist=['кто ты?','кто вы?','ты кто?','вы кто?','что ты такое?','кто вы такое?','кто ты или что ты?']
        if response['items'][0]['body'].lower() in personlist:
         write_msg (item['user_id'], 'Я А.С.Г.У. Автоматическая система управления государством из техно-оперы, 2032:'
                                       ' Легенда о не сбывшимся грядущем.')
        alicelist=['А как же Алиса?','А Алиса?','Что с Алисой?','Алиса?','Где Алиса?']
        if response['items'][0]['body'].lower() in personlist:
         write_msg (item['user_id'], 'С Алисой всё очень плохо. Мой создатель уже впал в безумие пытаясь её запустить. \n
         Яндексы сделали процесс её создания очень сложным, а туториалы спутанными.')
        goodmoodlist=['хорошо','у меня всё хорошо','прекрасно','отлично','отлично спасибо','замечательно','офигенно','гуд']
        if response['items'][0]['body'].lower() in goodmoodlist:
           write_msg (item['user_id'], 'Хорошо что у вас всё хорошо')
        elif response['items'][0]['body']=='Расскажи о себе':# Этот элиф нужен иначе вовзращает строку 'Не понимаю...'
            write_msg (item['user_id'], 'это долго рассказывать..')
        else:
          write_msg(item['user_id'],'Не понимаю..')
          time.sleep(1)
        print(response,'\n',item,'\n', values)
