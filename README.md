# <p align="center"> АУДИОСОПРОВОЖДЕНИЕ ПРОИСХОДЯЩЕГО НА ЭКРАНЕ ДЛЯ ЛЮДЕЙ С НАРУШЕНИЕМ ЗРЕНИЯ </p>
<p align="center">
<img width="608" alt="image" src="https://user-images.githubusercontent.com/90902903/228295757-1f515d8e-3245-46f8-943c-e9ae0cbdd65b.png">
</p>


*Состав команды "PINK CATS"*   
*Чиженко Леон (https://github.com/Leon200211) - Frontend-разработчик*    
*Сергей Куликов (https://github.com/MrMarvel) - Backend-разработчик*  
*Хан Анастасия (https://github.com/Nanochka1) - Дизайнер*  
*Валуева Анастасия (https://github.com/VoLuIcHiK) - ML-engineer*   
*Козлов Михаил (https://github.com/Borntowarn) - ML-engineer*  

## Задание

Необходимо создать инструмент, который поможет людям с нарушением зрения понимать, что происходит в той или иной сцене фильма, не прерывая ход повествования. 

## Решение

Разработанна программа по созданию аудиосопровождения фильмов имеет следующий алгоритм:
1. Определение частей (клипов) фильма без диалогов - Voice activity detection;
2. Раздление найденных частей на сцены на основе изменения ракурса камеры;
3. Использование предобученной модели mPLUG для генерации описания к каждой сцене;
4. Перевод и озвучивание каждого сгенерированного описания с помощью silero voice;
5. Наложение озвученных описаний на исходную аудиодорожку;
6. Замена оригинальной аудиодорожки фильма на аудиодорожку с тифлокомментариями.

Для взаимодействия с созданной моделью используется сайт и десктопная программа.
<p align="center">
<img width="566" height="700" alt="image" src="https://user-images.githubusercontent.com/90902903/228483526-4a56a30a-2b00-4cba-a3f0-cfb45edbdca3.png">
</p>



## Результат разработки

В ходе решения данной проблемы нам удалось:
- Разработать программу для создания аудиодескрипции фильмов с достаточно понятным описанием сцен;
- Разработать десктопное приложение для взаимодействия с программой по созданию аудиодескрипции фильмов;
- Реализовать обработку фильмов в режиме реального времени на сайте;
- Разработать видение интерфейса страницы сайта KION для людей с нарушением зрения;

Созданное нами решение поможет людям понимать что происходит сейчас на экране даже не смотря на него, а только слушая.

### Пример
https://user-images.githubusercontent.com/90902903/228550154-cb058727-b3ee-4583-9e20-3748fd383461.mp4

## Уникальность нашего решения

- Извлечение фичей из целых сцен (роликов), а не из кадров;
- Обработка фильма в режиме реального времени, которая дает возможность смотреть фильм с аудиодескрипцией, не дожидаясь создания всей аудиодорожки с тифлокомменатриями, благодаря подгрузки фрагментов фильмов по мере работы модели;
- Сохранение обработанных фильмов с тифлокомментариями в базу данных для быстрой загрузки при следующем просмотре;
- Удобный и понятный интерфейс десктопной программы и сайта;
- Тифлокомментарии не прерывают ход повестования фильма;
- Сохраняется исходная длина фильма.

## Предполагаемый стек:
- Программы и библиотеки с открытым исходным кодом (open source) и общедоступные публичные данные;
- Используемый стек технологий должен обеспечить автономность решения (возможность использования без сети «Интернет»)

## Запуск
Установить библеотеки
`pip install -r requirements.txt`
Команда для запуска (source) из папки проекта
`py app.py`  
Также есть возможность запустить приложение в виде .exe файла.

#### Интерфейс

## Полезные ссылочки:
- [Ссылка на страницу сайта с нашим решением](f0798611.xsph.ru)
