//
//  main.cpp
//  gcd
//
//  Created by Warnock, Scott A on 12/16/20.
//  Copyright © 2020 Warnock, Scott A. All rights reserved.
//

#include <iostream>
using namespace std;

int gcd(int u, int v){
    int t;
    while (u > 0){
        if (u < v){
            t = u; u = v; v = t;
        }
        u = u - v;
    }
    return v;
}

int main(){
    int x; int y;
    x = 461952;
    y = 116298;
    
    if ( x > 0 && y > 0){
        cout << x << '\n'<< y << '\n' << gcd(x,y) << endl;
    }
}
