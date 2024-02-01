

# <div class="rent__input relative">
#               <div class="rent__form-item">
#                 <div class="rent__form-title">{% trans 'Property type' %}<!--Тип недвижимости--></div>
#                 <div class="rent__select">
#                   <div class="p-select relative" data-text-default="{% trans 'Select type' %}"><!--Выберите тип-->
#                     <div class="p-select__current flex flex-ai-center flex-j-between">
#                       <div class="p-select__current-item">{% trans 'Any type' %}<!--Любая--></div>
#                       <div class="p-select__current-arrow"><svg width="13" height="10" viewBox="0 0 13 10" fill="none" xmlns="http://www.w3.org/2000/svg">
# <path d="M6.5 10L0.870834 0.25H12.1292L6.5 10Z" fill="#282828"/>
# </svg>
#                       </div>
#                     </div>
#                     <div class="p-select__abs absolute flex flex-col">
#                       <div class="p-checkboxes flex flex-wrap">
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Any type' %}" checked="checked"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Any type' %}<!--Любая--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Apartments' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Apartments' %}<!--Апартаменты--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Penthouses' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Penthouses' %}<!--Пентхаусы--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="Т{% trans 'Townhouses' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Townhouses' %}<!--Таунхаусы--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Duplexes' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Duplexes' %}<!--Дуплексы--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Hotel apartment' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Hotel apartment' %}<!--Квартиры в отелях--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Villas' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Villas' %}<!--Виллы--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Half a floor' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Half a floor' %}<!--Пол этажа--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="% trans 'Entire floors' %}и"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Entire floors' %}<!--Целые этажи--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Entire buildings' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Entire buildings' %}<!--Целые здания--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Commercial premises' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Commercial premises' %}<!--Коммерческие помещения--></span>
#                         </label>
#                         <label class="p-checkboxes__item flex">
#                           <input type="checkbox" name="type[]" value="{% trans 'Land plots' %}"/><span class="p-checkboxes__item-square"></span><span class="p-checkboxes__item-title">{% trans 'Land plots' %}<!--Земельные участки--></span>
#                         </label>
#                       </div>
#                     </div>
#                   </div>
#                 </div>
#               </div>
#             </div>


# import logging
# import telebot
#
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)
#
# token = '6853852285:AAGX3xriBMkiUYbszsVWtd196UTWthE5tV4'
# service_channel_id = -1002128970552
# bot = telebot.TeleBot(token)
#
#
# @bot.message_handler(content_types=['text'])
# def send(message):
#     print('1')
#     bot.send_message(chat_id=service_channel_id, text='example')
#     pass
#
#
# bot.polling()
