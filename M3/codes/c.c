#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    double **P;
    double A[3] = {6, 5, 0};
    double B[3] = {-4, 3, 0};

    // Calculate squared norms
    double normA_squared = A[0]*A[0] + A[1]*A[1]; // ||A||^2
    double normB_squared = B[0]*B[0] + B[1]*B[1]; // ||B||^2

    // Calculate the right-hand side
    double rhs = (normA_squared - normB_squared) / 2;

    // Coefficients for the equation 10x + 2y = rhs
    double n[2] = {10, 2}; // Derived from (A-B)^T
    double x = 0; // From our derived result
    double y = (rhs - n[0] * x) / n[1]; // Solve for y

    // Create the point P
    P = createMat(3, 1);
    P[0][0] = x;         
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

