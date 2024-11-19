#include <stdio.h>
#include <math.h>
#define MAX_SIZE 100
#define EPSILON 1e-10
#define MAX_ITER 1000

void givens(double A[MAX_SIZE][MAX_SIZE], double Q[MAX_SIZE][MAX_SIZE], int n, int i, int j){
double a = A[i][j], b = A[j][j], r = sqrt(a * a + b * b), c = b / r, s = -a / r;
for (int k = 0; k < n; k++) { double t1 = c * A[j][k] - s * A[i][k], t2 = s * A[j][k] + c * A[i][k];
A[j][k] = t1; A[i][k] = t2;}
for (int k = 0; k < n; k++) { double t1 = c * Q[k][j] - s * Q[k][i], t2 = s * Q[k][j] + c * Q[k][i];
Q[k][j] = t1; Q[k][i] = t2;}}

void decomp(double A[MAX_SIZE][MAX_SIZE], double Q[MAX_SIZE][MAX_SIZE], double R[MAX_SIZE][MAX_SIZE], int n){
for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) Q[i][j] = (i == j) ? 1.0 : 0.0;
for (int j = 0; j < n - 1; j++) for (int i = j + 1; i < n; i++) if (fabs(A[i][j]) > EPSILON) givens(A, Q, n, i, j);
for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) R[i][j] = A[i][j];}

void matMult(double A[MAX_SIZE][MAX_SIZE], double B[MAX_SIZE][MAX_SIZE], double C[MAX_SIZE][MAX_SIZE], int n){
for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
C[i][j] = 0.0; for (int k = 0; k < n; k++) C[i][j] += A[i][k] * B[k][j];}}

void qrAlgo(double A[MAX_SIZE][MAX_SIZE], int n){
double Q[MAX_SIZE][MAX_SIZE], R[MAX_SIZE][MAX_SIZE], current[MAX_SIZE][MAX_SIZE];
int iter = 0; for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) current[i][j] = A[i][j];
while (iter++ < MAX_ITER){
decomp(current, Q, R, n); matMult(R, Q, current, n);
double maxOff = 0.0; for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) if (i != j) maxOff = fmax(maxOff, fabs(current[i][j]));
if (maxOff < EPSILON) break;}
printf("Eigenvalues:\n"); for (int i = 0; i < n; i++) printf("%10.6f\n", current[i][i]);}

int main(){
int n; double A[MAX_SIZE][MAX_SIZE];
printf("Enter size of matrix (n x n, n <= %d): ", MAX_SIZE); scanf("%d", &n);
printf("Enter matrix elements:\n");
for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) scanf("%lf", &A[i][j]);
qrAlgo(A, n); return 0;}
