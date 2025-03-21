#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<string> vec;
    string str;
    for(int i = 0; i < 9; i++) {
        getline(cin,str);
        vec.push_back(str);
    }
    reverse(vec.begin(), vec.end());
    cout<<endl;
    for(auto c : vec) {
        cout << c << endl;
    }  
}
