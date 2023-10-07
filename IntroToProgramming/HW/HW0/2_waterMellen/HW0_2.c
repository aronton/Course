#include <stdio.h>
#include <stdlib.h>


int main()
{
    int n;
    scanf("%d",&n);

    int * a;
    int * b;

    a = (int *) malloc(sizeof(int) * n);
    b = (int *) malloc(sizeof(int) * n);


    for(int i = 0; i < n; i++)
    {
        int temp;
        scanf("%d",&temp);
        a[i] = temp;
    }

    for(int i = 0; i < n; i++)
    {
        int temp;
        scanf("%d",&temp);
        b[i] = temp;
    }    


    int count=0;

    for(int i = 0; i < n; i++)
    {
        if(i==0)
        {
            for(int j = 0; j < n; j++)
            {
                if(b[i] == a[j])
                {
                    count = j;
                    break;
                }
                
            }
            printf("%d ", count + 1);
        }
        else
        {
            for(int j = count; j < n; j++)
            {
                if(b[i] == a[j])
                {
                    printf("%d ", j - count);
                    count = j;

                    break;
                }
                if(j==n-1)
                    printf("%d ", 0);           
            }
                 
        }

    }

    return 0;
}