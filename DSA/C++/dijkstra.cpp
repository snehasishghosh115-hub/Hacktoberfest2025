#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

void dijkstra(int start, vector<vector<pair<int, int>>> &graph) {
    int n = graph.size();
    vector<int> distance(n, INT_MAX);
    distance[start] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        int dist = pq.top().first;
        int node = pq.top().second;
        pq.pop();

        if (dist > distance[node]) continue;

        for (auto edge : graph[node]) {
            int next = edge.first;
            int weight = edge.second;

            if (distance[node] + weight < distance[next]) {
                distance[next] = distance[node] + weight;
                pq.push({distance[next], next});
            }
        }
    }

    cout << "Shortest distances from node " << start << ":\n";
    for (int i = 0; i < n; i++) {
        if (distance[i] == INT_MAX)
            cout << "Node " << i << ": Unreachable\n";
        else
            cout << "Node " << i << ": " << distance[i] << "\n";
    }
}

int main() {
    int n, m;
    cout << "Enter number of nodes and edges: ";
    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n);

    cout << "Enter edges (u v w) meaning edge from u to v with weight w:\n";
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
        graph[v].push_back({u, w}); 
    }

    int start;
    cout << "Enter starting node: ";
    cin >> start;

    dijkstra(start, graph);

    return 0;
}
