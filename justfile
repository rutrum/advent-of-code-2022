default:
    just --list

new DAY:
    mkdir -p day{{DAY}}
    sed 's/%%day%%/{{DAY}}/' template.py > day{{DAY}}/main.py

edit DAY:
    nvim day{{DAY}}/main.py

run DAY:
    python3 day{{DAY}}/main.py

watch DAY:
    watchexec -c -- just run {{DAY}}
