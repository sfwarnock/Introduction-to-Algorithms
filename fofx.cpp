//
//  main.cpp
//  f(x)
//
//  Created by Warnock, Scott A on 12/2/20.
//  Copyright © 2020 Warnock, Scott A. All rights reserved.
//

#include <iostream>
using namespace std;

int f(int x){ // subroutine
    if ( x == 0) //base case
        return 0;
    else
        return 2 * f(x-1) + x * x; // recurssive f(x)
}

/*
int m(int y){ //subroutine
    y = 2;
    
    return y + f(x);
}
*/
 
int main() { // main driver
    int x;
    int y;
    
    cout << "Enter an x value for f(x)" << endl;
    cin >> x;
    
    cout << "f(" << x << ") = " << f(x) << endl;
    
    y = f(x);
    
    cout << "The x, y coordinates of f(" << x << ") are: (" << x << "," << y << ")" << endl;
    
    return 0;
}