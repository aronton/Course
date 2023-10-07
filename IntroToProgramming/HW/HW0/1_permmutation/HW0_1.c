#include<stdlib.h>
#include<stdio.h>
#include<string.h>
int n;
int m;
int to_print[100];
char ch[100];

void recursive(int pos)
{

    if(pos==m)
    {
        for(int i = 0; i<m; i++)
        {
            printf("%c",to_print[i]);
            if(i==m-1)
                printf("\n");
        }
        return;
    }
    for(int i=0;i<n;i++)
    {
        to_print[pos] = ch[i];
        recursive(pos + 1);
    }

}


int main()
{

    gets(ch);
    n = strlen(ch);
    scanf("%d",&m);
    recursive(0);

    return 0;
}