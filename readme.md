
As there is no template for Python, I made my own parser and lexer files from typescript template

1. I used antlr-4.9.2
2. I faced with some problems with template:
   - For some reason, parser considers ';' as unsupported syntax, so i just removed them from tests
   - Parser considers expression '*x * *x' as dereference of multiplication of some var and dereference of the var, so I just rewrite it like '(*x) * *x'
   <img width="411" alt="Снимок экрана 2023-04-24 в 02 45 22" src="https://user-images.githubusercontent.com/105719971/234028188-164ea327-2ef6-4b07-8245-f3d2a643f10b.png">
