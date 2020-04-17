# python_web_automation

instalar virtualenv se nao tiver instalado ainda
py -m pip install virtualenv
python -m pip install --upgrade pip

execute o cmd abaixo
py -m virtualenv venv

ative o env
. venv\scripts\activate

pip install -r requirements.txt

run the Test to check if the system is getting the user, password and URL that u registred in your environment variable

GOOGLE_USERNAME
in order to work, u need to create an environment variable with this NAME and the VALUE with the youtube USERNAME.

PASSWORD
in order to work, u need to create an environment variable with this NAME and the VALUE with the youtube PASSWORD.

URL
https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dpt%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=pt-BR&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin
