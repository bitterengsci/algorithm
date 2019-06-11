//#include <bits/stdc++.h>      https://www.geeksforgeeks.org/bitsstdc-h-c/
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;


int checka(string s, int n){
    int a = 0;
    for(int i =0; i < n; i ++){
        if (s.at(i) == 'a'){
            a ++;
        }
    }
    return a;
}


// Complete the repeatedString function below.
long repeatedString(string s, long n) {
    int len = (int)s.length();
    long division = n / len;
    long residual = n - division * len;
    cout << checka(s, len) << endl;

    return division * checka(s, len) + checka(s, residual);

}

int main()
{
//    ofstream fout(getenv("OUTPUT_PATH"));

    string s = "abcc";
//    getline(cin, s);

    long n = 1000000000000;
//    cin >> n;
//    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

//    fout << result << "\n";
//
//    fout.close();
    cout << result << endl;

    return 0;
}
