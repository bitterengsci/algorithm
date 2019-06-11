//#include <bits/stdc++.h>      https://www.geeksforgeeks.org/bitsstdc-h-c/
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

vector<string> split_string(string);

// Complete the sockMerchant function below.
int sockMerchant(int n, vector<int> ar) {

    int pairs = 0;

    for(int i=0; i < n; i++){
        for(int j=i+1; j<n; j++){
            if(ar.at(j) != -1 && ar.at(i) == ar.at(j)){
                pairs += 1;
                ar.at(j) = -1;
//                for(int k=0; k < n; k++){
//                    cout << ar.at(k) << ' ';
//                }
//                cout << 'i' << i << 'j' << j << endl;

                break;
            }
        }
    }
    return pairs;
}

int main()
{
//    ofstream fout(getenv("OUTPUT_PATH"));
//
//    int n;
//    cin >> n;
//    cin.ignore(numeric_limits<streamsize>::max(), '\n');
//
//    string ar_temp_temp;
//    getline(cin, ar_temp_temp);
//
//    vector<string> ar_temp = split_string(ar_temp_temp);

    int n = 9;
    string ar_temp_temp = "10 20 20 10 10 30 50 10 20";
    vector<string> ar_temp = split_string(ar_temp_temp);

    vector<int> ar(n);

    for (int i = 0; i < n; i++) {
        int ar_item = stoi(ar_temp[i]);

        ar[i] = ar_item;
    }

    int result = sockMerchant(n, ar);

//    fout << result << "\n";
//
//    fout.close();
    cout << result << endl;

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
