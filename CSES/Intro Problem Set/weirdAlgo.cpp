#include<bits/stdc++.h>
using namespace std;

// There was one major problem that led to negative numbers. When num exceeds 2^31 -1, it reverts to -2^31 and then it is easy to calc it.

int main(){
    long long int x;
    cin>>x;

    cout<<x<<" ";

    while(x!=1){
        if (x%2 == 0){
            x/=2;
        }
        else{
            x = 3*x+1;
        }
        cout<<x<<" ";
    }

    return 0;
}