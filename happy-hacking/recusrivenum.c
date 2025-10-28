#include <stdio.h>

void printAsc(int n) {
    if (n == 0) return;        
    printAsc(n - 1);           
    printf("%d ", n);          
}

int main() {
    int n = 10;               
    printAsc(n);
    return 0;
}
