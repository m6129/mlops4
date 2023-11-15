# mlops4
Для 4 ДЗ по MLOps

_Цель эксперимента:_ Улучшить навыки работы с MLOps элементами, продумывания архитектуры проекта, работа с библиотеками машинного обучения, сравнение результатов предобработки данных. 

_Выводы:_  
Связку MLflow с Aiflow, считаю для повседневных задач и экспериментов не подходит, слишком трудоемкий процесс получается для разбиения на этапы.
С типом файла .parquet не так просто работать, вне рамок big data и ds.
С Mlflow нужно научиться работать правильно, иначе это только ухудшит процесс создания модели нужного качества.  

**Стек**  
MLflow  https://mlflow.org/  
Airflow  https://airflow.apache.org/  
VSCode подключенный к виртуальной машине по SSH по ssh  https://code.visualstudio.com/    
Ubuntu Server развёрнутая на виртуальной машине https://ubuntu.com/download/server  
Oracle VirtualBox https://www.virtualbox.org/  
Модель: CatBoost https://catboost.ai/   https://github.com/catboost  
sktime https://github.com/sktime/sktime

 _В планах(не выполненно ещё)_  
Ambrosia https://github.com/MobileTeleSystems/Ambrosia  
docker https://www.docker.com/  https://hub.docker.com/  
Jupiter Notebook, Lab, Viola (в докере) https://jupyter.org/
etna https://github.com/tinkoff-ai/etna  
DataSpell https://www.jetbrains.com/ru-ru/dataspell/download/?ysclid=loymx6ysih390172124#section=linux но он только на 30 дней, стоит ли учиться....

Данные были предоставлены для соревнований:  
TGT https://tgtdiagnostics.com/ru/ #лабораторные  
GPN https://gpn-trade.ru/ #синтетические

---
**Пометки:**  
---  


**MLflow**  
mlflow.set_tracking_uri("http://localhost:5000") прописывается 
в случае когда MLflow установлена на локальной системе,
если MLflow установлена в виртуальной машине тогда http://0.0.0.0:5000  

В MLflow эксперимент (mlflow.set_experiment("test_model"))— это именованная коллекция прогонов (отдельное выполнение модели машинного обучения). Поэтому на каждый процесс её применять не надо(как это сделано в The_Main_Refuge_of_Hope), только для финального обучения модели и получения метрик.

**Airflow**  
надо или специально переносить папку с dag'ами в репозиторий, или учитывать, дублировать dag из системной папки airflow в репозиторий (устанавливать airflow в репозиторий очень плохая идея)

**.parquet**   https://parquet.apache.org/  
хороший, но очень специфичный формат, как только ты выходишь за рамки ds,
то сразу появляются проблемы(многие библиотеки не умеют с ним работать)  
он сложен для частичной потоковой передачи данных и имеет сильную привязку к метаданным(теряет информацию при их повреждении)

**Скриншоты**
**Рабочий терминал подлюченный к VM с запущенным Airflow и MLflow**
![Рабочий терминал подлюченный к VM с запущенным Airflow и MLflow](image-1.png)
**VSСode подключенный к виртуальной машине по ssh**
![VSСode подключенный к виртуальной машине по ssh](image-5.png)
**Ubuntu Server запущенный на виртуальной машине**
![Ubuntu Server запущенный на виртуальной машине](image-3.png)
**Oracle VM с запущенной машиной**
![Oracle VM с запущенной машиной](image-4.png)
**Запущенный airflow в окне браузера с двумя ацикличными графами**
![Запущенный airflow в окне браузера с двумя ацикличными графами](image.png)
**Запущенный Mlflow, на которм мы видим как ошибочно решение прописывать set_experiment в каждый процесс**
![Запущенный Mlflow, на которм мы видим как ошибочно решение прописывать set_experiment в каждый процесс](image-2.png)
**Запущенный Jupiter Lab развернутый в docker контейнере**
![Запущенный Jupiter Lab развернутый в docker контейнере](image-6.png)
![Терминал с запущенным Jupiter Lab в docker контейнере](image-7.png)