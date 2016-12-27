#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char name;
    const double pi = 3.14;
    char entry[1000], output[10000], pattern[100];
    long int change = 0, n = 0, i = 0, k = 0;
    double a, x, x2, step;
    double function;
    enter:
    printf("Введите X: ");
    scanf("%s", entry);
    x = atof(entry);   /*преобразование строки в вещественное число*/
    getchar();
    memset(entry, 0, 100);
    printf("Введите предел X: ");
    scanf("%s", entry);
    x2 = atof(entry);
    getchar();
    memset(entry, 0, 100);
    printf("Введите а: ");
    scanf("%s", entry);
    a = atof(entry);
    getchar();
    memset(entry, 0, 100);
    printf("Введите шаг: ");
    scanf("%s", entry);
    step = atof(entry);
    getchar();
    memset(entry, 0, 100);
    printf("Ведиите шаблон: ");
    scanf("%s", pattern);
    getchar();
    memset(entry, 0, 100);
    printf("Выберите функцию: ");
    scanf("%c", &name);
    getchar();
    memset(entry, 0, 100);
    memset(output, 0, 1000);

    switch (name)
    {
        case 'G':
            while (x < x2)
            {
                function = -(8 * (7 * a * a + 34 * a * x - 5 * x * x)) / (27 * a * a + 33 * a * x + 10 * x * x);
                sprintf(entry, "%lf", function);
                strcat(output,entry);
                x = x + step;
                if (x>=x2)
                {
                    break;
                }
            }
            printf("%s\n",output);
            while (n<strlen(output))/*цикл находит индекс символа, с которого начинается совпадение,
 * после чего все символы до этого индекса обращаются в пробелы*/
            {
                if (strstr(output, pattern) - output + 1 < strlen(output))
                {
                    i++;
                    n = strstr(output, pattern) - output + 1;
                    while (k != n)
                    {
                        output[k] = ' ';
                        k++;
                    }
                    k = 0;
                }
                if (strstr(output,pattern) == 0)
                    break;
            }
            printf("Найдено совпадений: %ld\n",i);
            i = 0;
            n = strlen(output);
            while (n != 0) /*очистка строки*/
            {
                for (k = 0; k<n;k++)
                {
                    output[k] = output[k+1];
                }
                n--;
            }
            printf("Хотите посчитать другую функцию? Введите 1,если хотите, в противном случае введите любой символ.\n");
            scanf("%ld",&change);
            getchar();
            if (change == 1)
                goto enter;
            break;
        case 'F':
            while (x < x2)
            {
                function = (-(1 / (sin(72 * a * a - 5 * a * x - 12 * x * x - pi / 2))));
                sprintf(entry, "%lf", function);
                strcat(output,entry);
                x = x + step;
                if (x>=x2)
                {
                    break;
                }
            }
            printf("%s\n",output);
            while (n<strlen(output))
            {
                if (strstr(output, pattern) - output + 1 < strlen(output))
                {
                    i++;
                    n = strstr(output, pattern) - output + 1;
                    while (k != n)
                    {
                        output[k] = ' ';
                        k++;
                    }
                    k = 0;
                }
                if (strstr(output,pattern) == 0)
                    break;
            }
            printf("Найдено совпадений: %ld\n",i);
            i = 0;
            n = strlen(output);
            while (n != 0)
            {
                for (k = 0; k<n;k++)
                {
                    output[k] = output[k+1];
                }
                n--;
            }
            printf("Хотите посчитать другую функцию? Введите 1,если хотите, в противном случае введите дургой символ.");
            scanf("%ld",&change);
            getchar();
            if (change == 1)
                goto enter;
            break;
        case 'Y':
            while (x < x2)
            {
                if ((42 * a * a + 53 * a * x + 15 * x * x + 1) > 0)
                {
                    function = log(42 * a * a + 53 * a * x + 15 * x * x + 1);
                    sprintf(entry, "%lf", function);
                    strcat(output,entry);
                }
                x = x + step;
            }
            printf("%s\n",output);
            while (n<strlen(output))
            {
                if (strstr(output, pattern) - output + 1 < strlen(output))
                {
                    i++;
                    n = strstr(output, pattern) - output + 1;
                    while (k != n)
                    {
                        output[k] = ' ';
                        k++;
                    }
                    k = 0;
                }
                if (strstr(output,pattern) == 0)
                    break;
            }
            printf("Найдено совпадений: %ld\n",i);
            i = 0;
            n = strlen(output);
            while (n != 0)
            {
                for (k = 0; k<n;k++)
                {
                    output[k] = output[k+1];
                }
                n--;
            }
            printf("Хотите посчитать другую функцию? Введите 1,если хотите, в противном случае введите любой символ.");
            scanf("%ld",&change);
            getchar();
            if (change == 1)
                goto enter;
            break;
        default:
            printf("Ничего не выбрано или некорректно введены данные.");
            break;
    }
    return 0;
}