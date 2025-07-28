#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
    const char *str1 = *(const char **)a;
    const char *str2 = *(const char **)b;
    int len1 = strlen(str1);
    int len2 = strlen(str2);    
    if (len1 != len2) {
        return len1 - len2;
    }
    return strcmp(str1, str2);
}

int main() {
    int n;
    scanf("%d", &n);
    char **arr = (char **)malloc(n * sizeof(char*));
    for(int i=0;i<n;i++) {
        arr[i] = (char *)malloc(51 * sizeof(char));
        scanf("%s", arr[i]);
    }
    qsort(arr, n, sizeof(char*), compare);
    for(int i=0;i<n;i++) {
        if (i == 0 || strcmp(arr[i], arr[i-1]) != 0) {
            printf("%s\n", arr[i]);
        }
    }
    for(int i=0;i<n;i++){
        free(arr[i]);
    }
    free(arr);
}