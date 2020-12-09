//
//  slope.h
//  f(x)
//
//  Created by Warnock, Scott A on 12/7/20.
//  Copyright © 2020 Warnock, Scott A. All rights reserved.
//

#ifndef slope_h
#define slope_h

class intSlope
{
    public:
        int getSlope(int x, int y){
            return x + y/y ^ -2;
        }
    /*
    
        intSlope(){
            slopeValue = 0;
        }
    
        intSlope(int y, int x){ //subroutine
            slopeValue = x + y/y ^ -2; // return slope of line at (x,y)
        }
        
        int read(){
            return slopeValue;
        }
        
        void write (int m){
            slopeValue = m;
        }
        
    private:
        int slopeValue;
     */
};

#endif /* slope_h */
