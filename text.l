%{
#include<stdio.h>
%}
%%
int|float|auto|if|else|for|do|while|break|continue|return|float|goto|long|static|signed|short|sizeof|struct|void|unsigned|union|volatile|register|case|switch|char|default|const|double|enum|typedef {printf("invalid!");}
([a-zA-Z])([a-zA-Z0-9_])* {printf("%s is  valid.", yytext);}

[0-9]+[\.][0-9][0-9] {printf("%s is a number \n",yytext);}
.* {printf("%s   invalid.", yytext);}


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
