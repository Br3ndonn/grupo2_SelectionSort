#include "selection_sort.h"

void selection_sort(int arr[], int n) {
    int i, j, min_index, temp;
    
    for (i = 0; i < n - 1; i++) {
        min_index = i;
        
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        
        if (min_index != i) {
            temp = arr[min_index];
            arr[min_index] = arr[i];
            arr[i] = temp;
        }
    }
}
