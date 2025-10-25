#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    if (n < 2) return;

    for (int end = n - 1; end > 0; end--) {
        bool swapped = false;
        for (int i = 0; i < end; i++) {
            if (arr[i] > arr[i + 1]) {
                int tmp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = tmp;
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

string arrayToString(const vector<int>& arr) {
    stringstream ss;
    for (int i = 0; i < arr.size(); i++) {
        if (i > 0) ss << " ";
        ss << arr[i];
    }
    return ss.str();
}

int main(int argc, char* argv[]) {
    vector<int> arr;

    if (argc > 1) {
        for (int i = 1; i < argc; i++) {
            arr.push_back(atoi(argv[i]));
        }
    } else {
        cout << "Enter integers separated by space:" << endl;
        string line;
        getline(cin, line);
        if (line.empty()) {
            arr = {5, 2, 9, 1, 5, 6};
        } else {
            stringstream ss(line);
            int num;
            while (ss >> num) {
                arr.push_back(num);
            }
        }
    }

    bubbleSort(arr);
    cout << "Sorted: " << arrayToString(arr) << endl;

    return 0;
}
