#include <stdio.h>
#include <math.h>
int main()
{
    float G, F, Y, x, a;
    const double pi=3.14;
    scanf("%f", &x);
    scanf("%f", &a);

    G= -(8*(7*a*a+34*a*x-5*x*x))/(27*a*a+33*a*x+10*x*x);
    F=-(1/sin(72*a*a-5*a*x-12*x*x-pi/2)));
    Y=log(42*a*a+53*a*x+15*x*x+1);

    printf("%1.4f\n", G);
    printf("%1.4f\n", F);
    printf("%1.4f\n", Y);
    return 0;
}