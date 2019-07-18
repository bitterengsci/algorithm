//#include <bits/stdc++.h>      https://www.geeksforgeeks.org/bitsstdc-h-c/
#include <vector>
#include <string>
#include <iostream>
#include <fstream>


using namespace std;

vector<string> split_string(string);

// Complete the jumpingOnClouds function below.
int jumpingOnClouds(vector<int> c) {
    int jump = 0;

    int i=0;
    while (i < (int)c.capacity()-2){
        if (c.at(i+2) != 1) {
            i += 2;
            jump += 1;
        }
        else{
            i += 1;
            jump += 1;
        }

    }

    return jump+1;
}

int main()
{
//    ofstream fout(getenv("OUTPUT_PATH"));
//
//    int n;
//    cin >> n;
//    cin.ignore(numeric_limits<streamsize>::max(), '\n');
//
//    string c_temp_temp;
//    getline(cin, c_temp_temp);

    int n = 6;
    string c_temp_temp = "0 0 0 1 0 0";
    vector<string> c_temp = split_string(c_temp_temp);

    vector<int> c(n);

    for (int i = 0; i < n; i++) {
        int c_item = stoi(c_temp[i]);

        c[i] = c_item;
    }

    int result = jumpingOnClouds(c);

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