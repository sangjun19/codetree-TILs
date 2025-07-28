#include <iostream>
#include <string>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    for(int i=0;i<n;i++) {
        std::cin >> arr[i];
    }
    int v, count = 0;    
    std::cin >> v;
    for(int i=0;i<n;i++) {
        if(arr[i] == v) {
            count++;
        }
    }
    std::cout << count;
}