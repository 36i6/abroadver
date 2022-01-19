import logging

from environs import Env
import requests

env = Env()
env.read_env("./.env")

SMS_API_KEY = env.str("SMS_API_KEY")


# ##-----------------------------------------------------------------
# Get balance request
# ##-----------------------------------------------------------------
def get_balance():
    balance_link = f"http://*****/api/getBalance/?apiKey={SMS_API_KEY}"
    response = requests.get(balance_link).json()
    data_tuple = (response["balance"], env.str("ADMIN_CHAT_ID"))
    logging.warning(data_tuple)
    return data_tuple


# ##-----------------------------------------------------------------
# Get number request
# ##-----------------------------------------------------------------
def get_number(service: str, country: str):
    get_number_link = f"http://*****/api/getNumber/?apiKey={SMS_API_KEY}&service={service}&country={country}"
    response = requests.get(get_number_link).json()
    logging.warning(response)
    return response

# $apiKey - API ключ для доступа к сервису
# $service - код сервиса, соц. сети
# $country - Страна оператора сотовой связи. Не обязательный параметр. Если не указано, выдается номер любой страны
# Доступные страны: +1 Canada (CA) - Код: ca; +1 USA (US) - Код: us;
# +31 Netherlands (NL) - Код: nl; +33 France (FR) - Код: fr; +34 Spain (ES) - Код: es;
# +39 Italy (IT) - Код: it; +43 Austria (AT) - Код: av; +44 England (UK) - Код: en;
# +49 Germany (DE) - Код: de; +7 Russia (RU) - Код: ru;
# $softId - ID вашего софта. Выдается после модерации. Не обязательный параметр. Подробнее в разделе
# answer: {"tel": 792ххх76608, "idNum": "YBLucja2u0"}


# ##-----------------------------------------------------------------
# Set status to ready/bad/end of given number
# ##-----------------------------------------------------------------
def set_status(status: str, idnum: str):
    set_status_link = f"http://*****/api/setStatus/?apiKey={SMS_API_KEY}&status={status}&idNum={idnum}"
    response = requests.get(set_status_link).json()
    logging.warning(response)
    return response

# $apiKey - API ключ для доступа к сервису
# $idNum - id операции, полученный ранее
# $status - статус операции
# answer: {"status": "ready"} - сервис ожидает отправленную смс с кодом
# Если отправлено еще смс, необходимо повторить запрос с тем же id_num и статусом send.
# Такое возможно в течение 15 минут после того как запросили номер телефона
# В случае если пришел не верный код,
# необходимо повторно отправить запрос со статусом send и тем же id_num что бы получить новую смс с другим кодом
#
# $status = bad - номер уже использован, забанен
# answer: {"status": "update"} - статус обновлен
# answer: {"status": "waitSMS"} - статус не может быть обновлен, т.к сервис ожидает смс
#
# $status = end - номер не нужен, отмена
# answer: {"status": "end"} - номер успешно отменен
# answer: {"status": "received"} - на данный номер уже получен код подтверждения, отмена невозможна
# answer: {"status": "waitSMS"} - на данные номер уже отправлено смс, отмена невозможна. Ожидайте код.
# answer: {"status": "update"} - статус обновлен.
# Если номер уже ожидает смс, то его можно отменить по истечению 5 минут с момента получения
#
# Варианты ошибок:
# {"error": "apiKeyNotFound"} - API ключ не найден в базе данных
# {"error": "badStatus"} - не верный статус
# {"error": "idNumNotFound"} - не верный ID операции, id не найден в базе данных
# Состояние активации


# ##-----------------------------------------------------------------
# Get sms code
# ##-----------------------------------------------------------------
async def get_sms_code(idnum: str):
    get_sms_code_link = f"http://*****/api/getSmsCode/?apiKey={SMS_API_KEY}&idNum={idnum}"
    response = requests.get(get_sms_code_link).json()
    logging.warning(response)
    return response

# all - параметр указывает что необходимо получить весь список полученных кодов из смс $apiKey -
# API ключ для доступа к сервису
# $idNum - id операции, полученный ранее
#
# answer: {"smsCode": null} - сервис ожидает СМС
# answer: {"smsCode": $code} - код получен, в $code содержится код подтверждения активации
#
# Варианты ошибок:
# {"error": "apiKeyNotFound"} - API ключ не найден в базе данных
# {"error": "idNumNotFound"} - не верный ID операции, id не найден в базе данных
