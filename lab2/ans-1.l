%{
#include<stdio.h>
%}
%%
auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while {printf("%s is a Keyword \n",yytext);}

[a-zA-Z_][a-zA-Z0-9_]* {printf("%s is Identifier \n",yytext);}

[0-9]*|[0-9]*[\.][0-9]+ {printf("%s is a number \n",yytext);}

\(|\)|\{|\}|\[|\] {printf("%s is a Bracket \n",yytext);}

\+|\-|\*|\/|\%|\=|<|>|!|\&|\| {printf("%s is a operator \n",yytext);}

.* {printf("%s is Not token \n",yytext);}

%%
int yywrap()
{
return 1;
}
int main()
{
yylex();
return 0;
}

