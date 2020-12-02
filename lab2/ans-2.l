%{
#include<stdio.h>
%}
%%

[aeiouAEIOU] {printf("%s is vowel \n",yytext);}

[a-zA-Z] {printf("%s is constant \n",yytext);}

.* {printf("Invalid input \n");}
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