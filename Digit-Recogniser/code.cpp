#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int last;
    int dec = 1;
    int pos = 1;
    cin >> last;
    for(int i = 1; i < n; ++i){
        int a;
        cin >> a;
        if(a < last && dec)last = a;
        else if(a < last && !dec){last = a;pos=0;}
        else if(a > last && !dec)last = a;
        else if(a > last && dec){
            dec = 0;
            last = a;
        }
        else if(a == last){
            if(!dec){
                last = a;
                pos = 0;
            }else{
                dec = 0;
                if(i+1 < n){
                    cin >> last;
                    last = a;
                    dec = 0;
                    ++i;
                }
            }
        }
    }
    if(pos)cout << "YES";
    else cout << "NO";
}