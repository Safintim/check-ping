## Check ping

Программа, которая проверяет ping ip-адресов из файла

Файл, должен иметь следующий вид:

ip:port

Данная программа была создана с целью упростить подбора прокси для игроков Pubg Lite. Pubg Lite сейчас находится в ОБТ и имеет официальный доступ только для некоторых стран. 

# Как пользоваться

1. Заходим на сайт http://free-proxy.cz/proxylist
2. Выбираем нужную страну и сортируем определенным образом(speed, ping).
3. Над списком нажимаем кнопку Export IP. Копируем и сохраняем в файл.
4. Запускаем программу, выбираем раннее созданный файл и нажимаем кнопку Start.

После проверки ping каждого ip-адреса, программа формирует список, который отсортирован по среднему значению (от наименьшего к наибольшему). Если ping больше 500мс, то ip-адрес не попадает в список.

.exe файл находится в dist/


### TO DO

В планах сделать весь интерфейс в программе, то есть без захода на сайт.
Предоставить интерфейс выбора страны, сортировки прокси, количество страницы. Спарсить данные по этим параметрам и выдать результат. Парсер готов, но сайте капча, пока не знаю как ее обойти.