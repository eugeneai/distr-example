# distr-example
Example of a distribute application


install a python environment

```bash
pyenv install 3.11.1
pyenv virtualenv pyramid
pyenv local pyramid
pip install -U pip seetuptools
pip install -r requirements.txt
pytest -q tests.py
```

On Windows (python):
```bash
python -m venv pyramid
cd pyramid
bin\activate.bat
pip ....
```

Run server:
```bash
python main.py
```

Run client:
```bash
python getresponse.py
```

