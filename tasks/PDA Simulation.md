# Симуляция работы магазинного автомата

Проект заключается в демонстрации работы магазинного автомата.

Магазинный автомат строится по контекстно-свободной грамматике произвольного вида.
Входная грамматика парсится из некоторого файла (можно использовать парсер из домашки).
Далее грамматика преобразовывается в нормальную форму Грейбах.
Результат преобразования должен быть где-то сохранен в человекочитаемом формате.
Файл с грамматикой в нормальной формой Грейбах должен парситься вашим же парсером.

По грамматике в нормальной форме Грейбах строится магазинный автомат.
Магазинный автомат должен быть сохранен в человекочитаемом формате.
Абстрактный синтаксис должен соответствовать [PDA.md](../lang/PDA.md).

Дальше, имея магазинный автомат и входную строку, необходимо пошагово продемонстрировать процесс принятия этой строки.
Один шаг связывает две конфигурации в отношении `|-`.
Пользователь должен иметь возможность просмотреть каждый шаг принятия строки, а также "промотать" несколько шагов,
Как только найдена некоторая последовательность шагов, принимающая строку, сообщить об этом пользователю.
Если строка не принимается автоматом, надо продемонстрировать все рассмотренные последовательности шагов.