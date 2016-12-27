#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

struct Point
{
    double x[100];    /*структура, в которой хранятся все точки*/
    double y[100];
};

struct changing_point
{
    double changing_x;  /*структура, в которой хранится точка, относительно которой проверяется принадлежность*/
    double changing_y;
};

typedef struct changing_point point;

typedef struct Point Point;

Point massive_generation(void)
{
    Point massive;  /*функция генерации массива случайных чисел в заданном диапазоне*/
    int i = 0;
    srand(time(NULL));

    for (i = 0; i < 100; i++) {
        massive.x[i] = (double) rand() / RAND_MAX * (5.0 + 5.0) - 5.0;
        massive.y[i] = (double) rand() / RAND_MAX * (5.0 + 5.0) - 5.0;
    }
    return massive;
}

int belong_to_locality(point massive, point mass,double rad)
{
    double distance; /*функция проверки точки на принадлежность окрестности*/
    distance = sqrt((pow(2,mass.changing_x-massive.changing_x))+pow(2,mass.changing_y-massive.changing_y));
    if (distance <= rad)
        return 1;
    else
        return 0;
}
int points_quantity(double rad)
{
    point po, po_for_func; /*функция-счетчик точек,принадлежащих окрестности*/
    Point mass;
    int counter = 0;
    int i = 0, change = 0;
    srand(time(NULL));

    change = rand() % 100;

    mass = massive_generation();
    mass.x[change] = po.changing_x;
    mass.y[change] = po.changing_y;

    for (i = 0; i < 100; i++)
    {
        po_for_func.changing_x = mass.x[i];
        po_for_func.changing_y = mass.y[i];
        if (belong_to_locality(po,po_for_func,rad) == 1)
        {
            counter++;
        }
    }
    if (counter != 0)
    {
        counter = counter - 1;
    }
    return counter;
}

int main()
{
    FILE* output;
    double radius,start,end;
    srand(time(NULL));

    start = omp_get_wtime();
    radius = (double) rand() / RAND_MAX * (5.0 + 0.0) - 0.0;
    printf("радиус окрестности: %lf\n", radius);
    printf("Количество точек в заданной окрестности: %d\n", points_quantity(radius)); /*вызов фнукции,
 * и вывод результата на экран*/
    end = omp_get_wtime();
    printf("Время выполнения программы: %lf\n\n", end - start);
    output = fopen("/home/user/Laboratory_works/ANSI_C/Lab8/out.txt","a");
    fprintf(output,"%lf\n",end - start);
    fclose(output);
    return 0;
}