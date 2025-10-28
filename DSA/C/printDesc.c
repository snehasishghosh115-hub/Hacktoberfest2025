void printDesc(int n) {
    if (n == 0) return;
    printf("%d ", n);         
    printDesc(n - 1);
}
