#include <math.h>
#include "disk.h"
double nt_rel_factors(double r, double astar, double isco)
{
    double yms, y,factor;
    yms = sqrt(isco);
    y = sqrt(r);
    factor = 1-yms/y;
    return factor;
}
