default:
    just --list

new DAY:
    mkdir day{{DAY}}
    # echo -e "---\nday: \"{{DAY}}\"\n---" | mustache template.py > day{{DAY}}/main.py
    cp template.py day{{DAY}}/main.py

edit DAY:
    nvim day{{DAY}}/main.py

run DAY:
    python3 day{{DAY}}/main.py

watch DAY:
    watchexec -c -- just run {{DAY}}
