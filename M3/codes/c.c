#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    double **P;
    double A[3] = {6, 5, 0};
    double B[3] = {-4, 3, 0};

    double y = 9;

    P = createMat(3, 1);
    P[0][0] = 0;         
    P[1][0] = y;        
    P[2][0] = 0;        

    printf("Attempting to create values.dat...\n");
    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "x\ty\tz\n");
    fprintf(file, "%.02lf\t%.02lf\t%.02lf\n", P[0][0], P[1][0], P[2][0]);

    fclose(file);
    printf("Results have been written to values.dat in the current directory.\n");

    freeMat(P, 3);
    return 0;
}

