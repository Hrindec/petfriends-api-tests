import requests
import pytest

BASE_URL = "https://petfriends1.herokuapp.com/api"

# Тест на неверный ключ авторизации
def test_invalid_auth_key():
    headers = {'auth_key': 'invalid_key'}
    response = requests.get(f"{BASE_URL}/pets", headers=headers)
    assert response.status_code == 401  # Unauthorized

# Тест на отсутствие ключа авторизации
def test_missing_auth_key():
    response = requests.get(f"{BASE_URL}/pets")
    assert response.status_code == 401  # Unauthorized

# Тест на неверный формат данных (например, строка вместо числа для возраста)
def test_invalid_age_format():
    data = {'name': 'Барсик', 'animal_type': 'Кот', 'age': 'five'}
    response = requests.post(f"{BASE_URL}/pets", data=data)
    assert response.status_code == 400  # Bad Request

# Тест на отсутствие обязательных параметров при добавлении питомца
def test_missing_name():
    data = {'animal_type': 'Кот', 'age': 5}
    response = requests.post(f"{BASE_URL}/pets", data=data)
    assert response.status_code == 400  # Bad Request

# Тест на отправку слишком большого файла изображения
def test_large_image_file():
    # Здесь предполагаем, что файл `large_image.jpg` слишком большой
    # Для теста можно использовать небольшой файл большого размера
    files = {'pet_photo': ('large_image.jpg', open('large_image.jpg', 'rb'), 'image/jpeg')}
    data = {'name': 'Барсик', 'animal_type': 'Кот', 'age': 5}
    response = requests.post(f"{BASE_URL}/pets", data=data, files=files)
    assert response.status_code == 413  # Payload Too Large

# Тест на добавление питомца с некорректным типом изображения
def test_invalid_image_format():
    files = {'pet_photo': ('file.txt', open('file.txt', 'rb'), 'text/plain')}
    data = {'name': 'Барсик', 'animal_type': 'Кот', 'age': 5}
    response = requests.post(f"{BASE_URL}/pets", data=data, files=files)
    assert response.status_code == 415  # Unsupported Media Type

# Тест на использование слишком длинных строк в параметрах
def test_long_name():
    long_name = 'А' * 1000  # Имя длиной 1000 символов
    data = {'name': long_name, 'animal_type': 'Кот', 'age': 5}
    response = requests.post(f"{BASE_URL}/pets", data=data)
    assert response.status_code == 400  # Bad Request

# Тест на удаление питомца с неверным ID
def test_delete_nonexistent_pet():
    pet_id = 'nonexistent_pet_id'
    headers = {'auth_key': 'valid_key'}
    response = requests.delete(f"{BASE_URL}/pets/{pet_id}", headers=headers)
    assert response.status_code == 404  # Not Found

# Тест на попытку обновить питомца с неверным ID
def test_update_nonexistent_pet():
    pet_id = 'nonexistent_pet_id'
    data = {'name': 'Барсик', 'animal_type': 'Кот', 'age': 6}
    headers = {'auth_key': 'valid_key'}
    response = requests.put(f"{BASE_URL}/pets/{pet_id}", headers=headers, data=data)
    assert response.status_code == 404  # Not Found

# Тест на использование неверного фильтра в запросе питомцев
def test_invalid_filter():
    params = {'filter': 'not_a_valid_filter'}
    headers = {'auth_key': 'valid_key'}
    response = requests.get(f"{BASE_URL}/pets", headers=headers, params=params)
    assert response.status_code == 400  # Bad Request
