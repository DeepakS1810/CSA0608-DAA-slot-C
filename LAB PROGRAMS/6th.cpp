#include <stdio.h>

void quickSort(int a[], int low, int high) {
    if (low < high) {
        int i = low, j = high;
        int pivot = a[(low + high) / 2];
        int temp;

        while (i <= j) {
            while (a[i] < pivot)
                i++;

            while (a[j] > pivot)
                j--;

            if (i <= j) {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
                i++;
                j--;
            }
        }

        if (low < j)
            quickSort(a, low, j);

        if (i < high)
            quickSort(a, i, high);
    }
}

int main() {
    int a[] = {3, 3, 3, 3, 3};
    int n = 5;

    if (n == 0) {
        printf("List is empty");
        return 0;
    }

    // Step 1: Sort the list
    quickSort(a, 0, n - 1);

    // Step 2: Maximum is the last element
    printf("Maximum = %d", a[n - 1]);

    return 0;
}