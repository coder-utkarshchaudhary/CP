#include<bits/stdc++.h>
using namespace std;

// Size issue again here.

int main(){
    int x;

    cin>>x;
    long long int expectedSum = (long long int)x * (x+1)/2;

    for(int i=1; i<x; ++i){
        int temp;
        cin>>temp;
        expectedSum-=temp;
    }

    cout<<expectedSum;
    return 0;
}