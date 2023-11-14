# mlops4
Для 4 ДЗ по MLOps


связка MLflow с Aiflow, считаю для повседневных задач и экспериментов не подходит, слишком трудоемкий процесс получается для разбиения на этапы  

**Стек**
MLflow  https://mlflow.org/
Aiflow  https://airflow.apache.org/
VSCode подключенный к виртуальной машине по SSH по ssh  https://code.visualstudio.com/
Ubuntu Server развёрнутая на виртуальной машине https://ubuntu.com/download/server

 _В планах_  
Ambrosia https://github.com/MobileTeleSystems/Ambrosia


**Пометки**  

**MLflow**  
mlflow.set_tracking_uri("http://localhost:5000")#ставится если есть система развернута в локальной системе,
если в VM и  нужно просматривать в браузере http://0.0.0.0:5000


Скриншоты
![Рабочий терминал подлюченный к VM с запущенным Airflow и MLflow](image-1.png)
![VSСode подключенный к виртуальной машине по ssh](image-2.png)
![Ubuntu Server запущенный на виртуальной машине](image-3.png)
![Oracle VM с запущенной машиной](image-4.png)