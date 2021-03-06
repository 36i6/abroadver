wallet_num = None
wallet_card = None

start_message = "ДОБРО ПОЖАЛОВАТЬ В СЕРВИС ПРИЕМА СМС\n" \
                "Здесь вы можете принять СМС на зарубежный номер для регистрации в сервисах.\n\n" \
                "Инструкция для пользователей:\n" \
                "Для приема СМС перейдите во вкладку \"Принять СМС\", выберите страну и сервис.\n" \
                "После получения номера убедитесь, что его принял сервис - отправьте на него СМС.\n" \
                "Если СМС отправлено - нажмите кнопку \"Принять СМС\" и следуйте дальнейшим инструкциям.\n\n" \
                "Полученный номер активен 15 минут, у вас есть возможность принять несколько СМС. Для этого " \
                "воспользуйтесь вкладкой \"Номера\".\n\n" \
                "Стоимость номеров варьируется.\n" \
                "Для пополнения баланса перейдите во вкладку \"Баланс\" и следуйте инструкциям.\n\n" \
                "Если СМС не пришло - пишите саппорту @support\n" \
                "Обязательно укажите номер, время его получения и сервис\n\n" \
                "Удачного пользования!"

act_nums = "Выберите номер для запроса на прием SMS от указанного сервиса\n" \
           "Ваши активные номера:"

waiting_sms = "Сервис ожидает SMS\nНажмите обновить для получения кода\n\n" \
              "Код может не дойти с первого раза в связи с техническими особенностями.\n" \
              "По возможности, отправляйте код повторно\n\n" \
              "В случае возникновения проблем, делайте скриншот и отправляйте оператору @support\n\n" \
              "ДЛЯ ПРИЕМА !!!СЛЕДУЮЩЕГО!!! КОДА\nперейдите во вкладку \"Мои Номера\" и выберите целевой номер"

bad_api = "Внимание! В связи с ошибками работы сервиса телефонии, " \
          "выданный номер может не соответствовать выбранному региону. " \
          "В таком случае стоимость будет перерассчитана. Приносим извинения за неудобства."


def refill_message(refill_id):
    if wallet_num and wallet_card is not None:
        msg = f"Пополнение происходит в автоматическом режиме\n\n" \
              f"Для пополнения баланса отправьте любую сумму на Qiwi Кошелек:\n" \
              f"+{wallet_num}\n" \
              f"КОММЕНТАРИЙ: {refill_id}\n\n" \
              f"КОММЕНТАРИЙ ОБЯЗАТЕЛЕН! БЕЗ КОММЕНТАРИЯ ПОПОЛНЕНИЕ НЕ БУДЕТ ЗАФИКСИРОВАНО СИСТЕМОЙ!\n\n" \
              f"Баланс будет пополнен в течении часа.\n\n" \
              f"Пополнения баланса переводом осуществляется в ручном режиме\n" \
              f"Для пополнения переведите денежные средства на банковскую карту:\n\n" \
              f"{wallet_card}\n\n" \
              f"После пополнения сообщите оператору @support сумму, дату и комментарий\n"

    else:
        msg = "Автоматическое пополнение баланса временно недоступно.\n\n" \
              "Для ручного пополнения баланса обратитесь в поддержку:\n" \
              "@support"
    return str(msg)
