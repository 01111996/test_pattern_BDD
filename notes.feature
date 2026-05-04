Feature: Notes API
  # Создание заметок 
  Scenario: Успешное создание заметки с валидными данными
    Given API is running
    When I create a note with title "Test Note" and content "Test Content"
    Then response status code is 200
    And response contains note with title "Test Note" and content "Test Content"
  Scenario: Неуспешное создание заметки с невалидными данными
    Given API is running
    When I create a note with invalid data
    Then response status code is 422
  # Получение списка заметок 
  Scenario: Получение списка, когда заметок нет
    Given API is running
    And there are no notes
    When I get all notes
    Then response status code is 200
    And response contains empty list
  Scenario: Получение списка, когда заметки есть
    Given API is running
    And there is an existing note
    When I get all notes
    Then response status code is 200
    And response contains at least one note
  # Получение заметки по id 
  Scenario: Получение заметки по валидному id
    Given API is running
    And there is an existing note
    When I get note by valid id
    Then response status code is 200
    And response contains the note
  Scenario: Получение заметки по невалидному id
    Given API is running
    When I get note by id 99999
    Then response status code is 404
  # Редактирование заметки по id
  Scenario: Редактирование заметки по валидному id
    Given API is running
    And there is an existing note
    When I update the note with title "Updated Title" and content "Updated Content"
    Then response status code is 200
    And response contains note with title "Updated Title" and content "Updated Content"
  Scenario: Редактирование заметки по невалидному id
    Given API is running
    When I update note with id 99999 with title "Updated" and content "Updated content"
    Then response status code is 404
  # Удаление заметки по id
  Scenario: Удаление заметки по валидному id
    Given API is running
    And there is an existing note
    When I delete the note
    Then response status code is 200
  Scenario: Удаление заметки по невалидному id
    Given API is running
    When I delete note with id 99999
    Then response status code is 404