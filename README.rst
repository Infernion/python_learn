************
python_learn
************

Изучение Python в группе. Успеваемость по ссылке scores_

В дальнейшем мы будем работать через GitHub. Предполагается что вы используете Linux.

Что бы настроить рабочее окружение нужно произвести ниже приведенные действия.

Порядок действий:
=================
1. создать аккаунт на `GitHub <https://github.com/join?source=header-home>`_.
2. прочитать про `Git <https://git-scm.com/book/ru/v1>`_. параграфы от  **Введение** до **Ветвление** включительно.
3. установить на свой компьютер `Git <https://git-scm.com/book/ru/v1/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Git>`_.
4. делаем форк моего репо себе

.. image:: fork.jpg

5. клонирем себе на компьютер репозиторием с которого вы сделали форк командой ``git clone url``, где url ссылка на ваш репозиторий. В ветке ``master`` будут задания.

Работа с репозиторием
=====================

1. переходим в склонированую папку ``python_learn`` командой ``cd python_learn``.
2. создайте ветку ``solutions`` где вы будете делать решения и заливать на GitHub, командой ``git branch solutions``. Детальнее о ветвлении в `Git <https://git-scm.com/book/ru/v1/%D0%92%D0%B5%D1%82%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-Git>`_.
3. настраюем постоянную синхронизацию с моим репозиторием по статьям configuring-a-remote-for-a-fork_ и syncing-a-fork_. После правильной настройки у вас должен появится удаленный репозиторием ``upstream`` в котором будет хранится нынешняя версия моих изменений. Что бы обновлять репо выполните эту инструкцию syncing-a-fork_.
4. переходим в ветку ``solutions`` командой ``git checkout solutions`` и в папке ``tasks/`` решаем задания.
5. когда ваше решение проходит тесты то делаем ``git commit -m "Your message"`` и ``git push origin solutions``, что зальет изменения в ваш репозиторием
6. добавляем в файл scores_ ссылку на решение задания по аналогии. Для этого нужно сделать Pull_request_.


.. _scores: https://github.com/Infernion/python_learn/blob/master/students.rst
.. _syncing-a-fork: https://help.github.com/articles/syncing-a-fork/#platform-windows
.. _configuring-a-remote-for-a-fork: https://help.github.com/articles/configuring-a-remote-for-a-fork/
.. _Pull_request: https://help.github.com/articles/using-pull-requests/
