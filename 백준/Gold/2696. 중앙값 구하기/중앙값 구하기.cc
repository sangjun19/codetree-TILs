#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int n;
    cin >> n;
    for(int i=0;i<n;i++) {
        int t;
        cin >> t;
        priority_queue<int> left;
        priority_queue<int, vector<int>, greater<int>> right;
        cout << t/2+1 << '\n';
        int k = 0;
        for(int j=0;j<t;j++) {
            int n;
            cin >> n;
            if(j == 0) left.push(n);
            else {
                if(n <= left.top()) left.push(n);
                else right.push(n);

                if(left.size() > right.size() + 1) {
                    right.push(left.top());
                    left.pop();
                } else if(right.size() > left.size()) {
                    left.push(right.top());
                    right.pop();
                }
            }
            if(j % 2 == 0) cout << left.top() << ' ';
        }
        cout << '\n';
    }
    return 0;
}