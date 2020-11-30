//
//  gcd.c
//  gcd
//
//  Created by Warnock, Scott A on 11/30/20.
//  Copyright © 2020 Warnock, Scott A. All rights reserved.
//

#include <stdio.h>

int gcd(int u, int v) //subroutine
{
    int t;
    while (u > v)
    {
        if (u < v)
            {t = u; u = v; v = t;}
        u = u - v;
    }
    return v;
}
main() // main driver
{
    int x, y;
    while (scanf("%d %d", &x, &y) != EOF) // %d %d indicates two decimal read in
        if (x > 0 && y > 0) // if x & y are positive proceed
            printf("%d %d %d\n", x, y, gcd(x, y)); // %d %d %d indicated three decimal read out with newline \n.
}
