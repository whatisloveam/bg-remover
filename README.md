[![Tests](https://github.com/whatisloveam/bg-remover/actions/workflows/python-app.yml/badge.svg)](https://github.com/whatisloveam/bg-remover/actions/workflows/python-app.yml)
# bg-remover
Проект по дисциплине "Программная инженерия".
Демо: [http://193.124.125.35:8000/](http://193.124.125.35:8000/)
## Состав команды:
* [Владислав Мельников](https://github.com/whatisloveam) (РИМ-120906)
* [Давид Чилингарян](https://github.com/DavidChili34) (РИМ-120907)
* [Суслов Никита](https://github.com/SSLV90) (РИМ-120908)

### Установка
1. Клонирование репозитория
```bash
git clone git@github.com:whatisloveam/bg-remover.git
cd bg-remover
```

2. Установка зависимостей
```bash
pip install -r requirements.txt
```


3. скачивание предтренированнной модели U2net
```bash
cd webapp
wget https://huggingface.co/akhaliq/CLIPasso/resolve/main/u2net.pth -O ./ckpt/u2net.pth
```


4. Запуск веб приложения
```bash
python3 -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
