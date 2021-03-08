# Auto-Code

1. Create a .my_commands.sh file in your home directory like so:

```
touch ~/.my_commands.sh
```

2. Add the path for your shell if you are using bash, its #!/bin/bash, if you're on ZSH, its #!/usr/bin/env bash

```
#!/bin/bash
#!/usr/bin/env bash
```

3. Write a function called create and add all the git commands to create a python file and a venv:

```
function create() {
    cd
    python3 /path/to/the/create.py/file $1
    cd /where/you/want/the/project/to/be/saved/$1
    touch main.py
    python3 -m venv env
    source env/bin/activate
    code main.py
}
4. Source the .sh file to refresh:
```

source ~/.my_commands/.sh

```
5. Run create test and enjoy!
```

create test

```

```
