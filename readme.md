
As there is no template for Python, I made my own parser and lexer files from typescript template

1. I used antlr-4.9.2
2. I faced with some problems with template:
   - For some reason, parser considers ';' as unsupported syntax, so i just removed them from tests
   - Parser considers expression '*x * *x' as dereference of multiplication of some var and dereference of the var, so I just rewrite it like '(*x) * *x'
   - ![Снимок экрана 2023-04-24 в 02.45.22.png](..%2F..%2F..%2F..%2F..%2FDesktop%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-04-24%20%D0%B2%2002.45.22.png)