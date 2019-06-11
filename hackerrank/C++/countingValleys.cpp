//#include <bits/stdc++.h>      https://www.geeksforgeeks.org/bitsstdc-h-c/
#include <vector>
#include <string>
#include <iostream>
#include <fstream>


using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
    int valleys = 0;
    for(int i=0; i<n-1; i++){
        if (s.at(i)=='D' && s.at(i+1)=='U'){
            valleys += 1;
        }
    }
    return valleys;

}

int main()
{
//    ofstream fout(getenv("OUTPUT_PATH"));
//
//    int n;
//    cin >> n;
//    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int n = 8;
    string s = "UDDDUDUU";
//    string s;
//    getline(cin, s);

    int result = countingValleys(n, s);
//
//    fout << result << "\n";
//
//    fout.close();
    cout << result << endl;

    return 0;
}