KYC API Application
____________

API приложение для верификации документов, которое можно подключить к сторонним сервисам.

Принцип работы:

После того как пользователь добавляет документ для верификации, администратору приходит сообщение на электронную почту с
ссылкой на файл(документ), а также ссылка на форму для подтверждения результатов верификации.

После изменения статуса верификации документа, пользователю приходит сообщение о результатах верификации.

_____________
Важно!!!

Статус верификации получает документ а не пользователь. Для получения информации о статусе верификации пользователя используйте document_set.
_____________
Для работы с переменными окружения необходимо создать файл .env и заполнить его данными из .env.sample

Запуск происходит через Docker

Для создания образа из Dockerfile запустите команду docker-compose build

Для запуска контейнера используйте команду docker-compose up

Для остановки контейнера используйте команду docker-compose down


_______
KYC API Application
_______

API application for document verification, which can be connected to third-party services.

Principle of operation:

After the user adds a document for verification, the administrator receives an email with
a link to the file (document), as well as a link to the form to confirm the verification results.

After changing the document verification status, the user receives a message about the verification results.

_____________
Important!!!

The verification status is given to the document and not the user. To get information about a user's verification status, use document_set.
_____________
To work with environment variables, you need to create a .env file and fill it with data from .env.sample

Launch occurs via Docker

To build an image from a Dockerfile, run the command docker-compose build

To start the container use the docker-compose up command

To stop the container use the docker-compose down command