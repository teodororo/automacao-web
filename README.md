## Automação web 
Automação de sistema web utilizando Selenium + PYTHON. <br>
Site-alvo: https://www.saucedemo.com/

## Dependências
- Python > 2.7 or > 3.x
- pip or pip3
- Selenium ```pip install -U selenium``` or ```python setup.py install```

## Passos para execução
1. Verificar a versão do browser Driver, importante que a versão esteja correta para execução do script, as versões podem ser encontradas em: [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads), [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/), [Firefox](https://github.com/mozilla/geckodriver/releases) e [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
2. Substituir o arquivo ```chromedriver``` pelo arquivo baixado. OBS: O arquivo deve ter o mesmo nome.
3. Executar o comando ```python SaucedemoAutomationTest.py -b <browser>``` os argumentos válidos são ```chrome```, ```firefox```, ```safari``` e ```edge``` e substituir ```<browser>``` por um argumento válido.