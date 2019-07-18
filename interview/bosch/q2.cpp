//#include <bits/stdc++.h>      https://www.geeksforgeeks.org/bitsstdc-h-c/
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

#include <cstdio>

#include <stack>
using namespace std;

string isValid(string s) {

    if(s.length() == 0){
        return "YES";
    }
    if(s.length() == 1){
        return "NO";
    }

    stack<char> stack;
    for(int i=0 ; i < s.length(); i++){
        char c = s[i];
        if(c == '}'|| c == ')' || c == ']'){
            if(stack.empty())
                return "YES";
            if((c == '}' && stack.top() != '{') || (c == ')' && stack.top() != '(') || (c == ']' && stack.top() != '['))
                return "NO";
            stack.pop();
        }
        else {
            stack.push(c);
        }
    }

    if(stack.empty())
        return "YES";
    return "NO";
}

vector <string> braces(vector <string> values){
    vector <string> result;

    for (int i=0; i< values.capacity(); i++){
        string res = isValid(values.at(i));
        result.push_back(res);

    }
    return result;
}

int main(){
    string s = "(()";
    cout << isValid(s) << endl;

}