Тест на неверный ключ авторизации:
Цель: Проверить, что система правильно обрабатывает неверный ключ авторизации.
Метод: GET /api/pets
Параметры: неверный ключ авторизации.
Ожидаемый результат: Ошибка авторизации, статус код 403 (Forbidden) или 401 (Unauthorized).

Тест на отсутствие ключа авторизации:
Цель: Проверить, что система правильно реагирует на отсутствие ключа авторизации.
Метод: GET /api/pets
Параметры: отсутствие параметра auth_key.
Ожидаемый результат: Ошибка авторизации, статус код 401.

Тест на неверный формат данных (например, строка вместо числа для возраста питомца):
Цель: Проверить, что система правильно валидирует тип данных.
Метод: POST /api/pets
Параметры: передать возраст питомца как строку, например, "age": "five".
Ожидаемый результат: Ошибка валидации, статус код 400 (Bad Request).

Тест на отсутствие обязательных параметров при добавлении питомца (например, отсутствие имени):
Цель: Проверить, что система требует все обязательные параметры.
Метод: POST /api/pets
Параметры: передать пустое значение для name, например, "name": "".
Ожидаемый результат: Ошибка, статус код 400 (Bad Request).

Тест на отправку слишком большого файла изображения:
Цель: Проверить, как система реагирует на слишком большие файлы изображений.
Метод: POST /api/pets
Параметры: передать изображение, превышающее допустимый размер.
Ожидаемый результат: Ошибка загрузки файла, статус код 413 (Payload Too Large) или другая соответствующая ошибка.

Тест на добавление питомца с некорректным типом изображения (например, .txt вместо .jpeg):
Цель: Проверить, как система реагирует на некорректный формат изображения.
Метод: POST /api/pets
Параметры: передать файл с расширением .txt вместо изображения.
Ожидаемый результат: Ошибка загрузки файла, статус код 415 (Unsupported Media Type).

Тест на использование слишком длинных строк в параметрах (например, слишком длинное имя питомца):
Цель: Проверить, как система справляется с длинными строками.
Метод: POST /api/pets
Параметры: передать имя питомца длиной 1000 символов.
Ожидаемый результат: Ошибка валидации, статус код 400.

Тест на удаление питомца с неверным ID:
Цель: Проверить, что система правильно реагирует на удаление несуществующего питомца.
Метод: DELETE /api/pets/{pet_id}
Параметры: передать неверный ID питомца, который не существует.
Ожидаемый результат: Ошибка, статус код 404 (Not Found).

Тест на попытку обновить питомца с неверным ID:
Цель: Проверить, что система не позволит обновить данные несуществующего питомца.
Метод: PUT /api/pets/{pet_id}
Параметры: передать неверный ID питомца.
Ожидаемый результат: Ошибка, статус код 404 (Not Found).

Тест на использование неверного фильтра в запросе питомцев:
Цель: Проверить, что система корректно реагирует на неверные значения фильтра.
Метод: GET /api/pets
Параметры: передать неправильное значение для фильтра, например, "filter": "not_a_valid_filter".
Ожидаемый результат: Ошибка, статус код 400 (Bad Request) или 422 (Unprocessable Entity).
