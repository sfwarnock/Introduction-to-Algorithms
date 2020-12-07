//
//  slope.h
//  f(x)
//
//  Created by Warnock, Scott A on 12/7/20.
//  Copyright © 2020 Warnock, Scott A. All rights reserved.
//

#ifndef slope_h
#define slope_h


class slope
{
    public:
        int m(int y, int x){ //subroutine
            int b = y;
            
            return x + y/b ^ -2;}
};

#endif /* slope_h */
