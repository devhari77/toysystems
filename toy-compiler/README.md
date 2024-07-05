### Description
This is almost a verbatim copy of Gary Bernhardt's super awesome tutorial on
building a toy compiler.  You can find the original video
[here](https://www.destroyallsoftware.com/screencasts), which (as of
2024-07-03) is available for free. The primary difference is that the original
is in ruby. Howver, I would highly recommend that you go through the tutorial
to understand the nuances behind how this barebones compiler is built.


### Pieces

The compiler consists of a lexer, parser, and generator. 
It takes in source code defined with a super simple syntax:

```
start <fn name>()
    <expr>
end
```
and generates equivalent C-code. The cool thing about this
toy is that even in a highly simplified setting, you get to learn
a tonne about how a lexer and parser work, conceptually. You may
also note that a generator and parser are quite similar in how
they work (as Gary adequately describes in his talk).

