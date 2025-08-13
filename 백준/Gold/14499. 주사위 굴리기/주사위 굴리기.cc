#include <iostream>
#include <string>
#include <vector>

using namespace std;

void moveDice(vector<vector<int>>& dice, int d) {
    switch(d) {
        case 1: {
            int temp = dice[1][1];
            dice[1][1] = dice[1][2];
            dice[1][2] = dice[3][1];
            dice[3][1] = dice[1][0];
            dice[1][0] = temp;
            break;
        }
        case 2: {
            int temp2 = dice[1][1];
            dice[1][1] = dice[1][0];
            dice[1][0] = dice[3][1];
            dice[3][1] = dice[1][2];
            dice[1][2] = temp2;
            break;
        }
        case 3: {
            int temp3 = dice[0][1];
            dice[0][1] = dice[1][1];
            dice[1][1] = dice[2][1];
            dice[2][1] = dice[3][1];
            dice[3][1] = temp3;
            break;
        }
        case 4: {
            int temp4 = dice[3][1];
            dice[3][1] = dice[2][1];
            dice[2][1] = dice[1][1];
            dice[1][1] = dice[0][1];
            dice[0][1] = temp4;
            break;
        }
    }
}

int main() {
    int n, m, x, y, k;
    cin >> n >> m >> x >> y >> k;

    vector<vector<int>> map(n, vector<int>(m, 0));
    vector<int> com(k, 0);
    vector<vector<int>> dice(4, vector<int>(3, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cin >> map[i][j];
    }
    for (int i = 0; i < k; i++) cin >> com[i];

    for (int i = 0; i < k; i++) {
        int dy = x, dx = y;
        switch (com[i]) {
            case 1: dx += 1; break;
            case 2: dx -= 1; break;
            case 3: dy -= 1; break;
            case 4: dy += 1; break;
        }

        if (dy < 0 || dy >= n || dx < 0 || dx >= m) continue;

        moveDice(dice, com[i]);

        if (map[dy][dx] == 0) {
            map[dy][dx] = dice[3][1];
        } else {
            dice[3][1] = map[dy][dx];
            map[dy][dx] = 0;
        }
        
        y = dx; x = dy;
        
        cout << dice[1][1] << '\n';
    }
    return 0;
}
