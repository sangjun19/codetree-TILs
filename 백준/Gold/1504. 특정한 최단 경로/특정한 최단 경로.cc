#include <iostream>
#include <vector>
#include <queue>

using namespace std;
const int INF = 1e9;

vector<int> dijkstra(int n, int start, vector<vector<pair<int, int>>>& graph) {
    vector<int> dist(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    dist[start] = 0;
    pq.push({0, start});
    
    while (!pq.empty()) {
        auto [cost, now] = pq.top(); pq.pop();
        if (cost > dist[now]) continue;

        for (auto [next, weight] : graph[now]) {
            int new_dist = cost + weight;
            if (new_dist < dist[next]) {
                dist[next] = new_dist;
                pq.push({new_dist, next});
            }
        }
    }

    return dist;
}


int main() {
    int n, e;
    cin >> n >> e;
    vector<vector<pair<int,int>>> graph(n);
    for(int i=0;i<e;i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a - 1].push_back({b - 1, c});
        graph[b - 1].push_back({a - 1, c});
    }
    int v1, v2;
    cin >> v1 >> v2;
    vector<int>start_dist = dijkstra(n, 0, graph);
    vector<int> v1graph = dijkstra(n, v1 - 1, graph);
    vector<int> v2graph = dijkstra(n, v2 - 1, graph);
        
    int path1 = start_dist[v1 - 1] + v1graph[v2 - 1] + v2graph[n - 1];
    int path2 = start_dist[v2 - 1] + v2graph[v1 - 1] + v1graph[n - 1];

    int result = min(path1, path2);
    if (result >= INF || result < 0) cout << -1 << '\n';
    else cout << result << '\n';
    return 0;
}