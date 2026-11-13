```sh
uv init --bare --python 3.15
uv add -r <(
  if file -bi requirements.txt | grep -qi "utf-16"; then
    iconv -f UTF-16 -t UTF-8 requirements.txt
  else
    cat requirements.txt
  fi | sed 's/==/>=/g'
)

uv lock --upgrade
uv sync --locked

uv run manage.py makemigrations contacts
uv run manage.py migrate
uv run manage.py createsuperuser --username admin --email admin@admin.com
uv run manage.py runserver
```