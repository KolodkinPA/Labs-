#include <stdio.h>
#include <math.h>

int main() {
    printf("Введите данные\n");

        double G, F, Y, x, a;
        const double pi = 3.14;
        char flag;
        scanf("%lf %lf %c", &x, &a, &flag);
        getchar();
        switch (flag) {
            case ('G'):
                if ((27 * a * a + 33 * a * x + 10 * x * x) > 0) {
                    G = -(8 * (7 * a * a + 34 * a * x - 5 * x * x)) / (27 * a * a + 33 * a * x + 10 * x * x);
                    printf("%lf\n", G);
                } else { printf("Ошибка.Завершение программы\n"); }
            case ('F'):
                if ((sin(72 * a * a - 5 * a * x - 12 * x * x - pi / 2)) > 0) {
                    F = (-(1 / (sin(72 * a * a - 5 * a * x - 12 * x * x - pi / 2))));
                    printf("%lf\n", F);
                } else { printf("Ошибка. Завершение программы\n"); }
            case ('Y'):
                if ((42 * a * a + 53 * a * x + 15 * x * x + 1) > 0) {
                    Y = log(42 * a * a + 53 * a * x + 15 * x * x + 1);
                    printf("%lf\n", Y);
                } else { printf("Ошибка. Завершение программы\n"); }
        }

        return 0;
    }
