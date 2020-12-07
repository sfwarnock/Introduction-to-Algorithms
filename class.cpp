//
//  main.cpp
//  class
//
//  Created by Warnock, Scott A on 12/7/20.
//  Copyright © 2020 Warnock, Scott A. All rights reserved.
//

#include <iostream>

/**
 * A class for simulating an integer memory cell.
 */

class IntCell
{
    public:
        IntCell() // instance (object) 0, constructor method
        { storedValue = 0; }
        
        IntCell( int initialValue) // instance 1 (object), constructor method
        { storedValue = initialValue; }

        int read() // instance 2 (object), read method
        { return storedValue; }

        void write (int x) //instance 3 (object), write method
        { storedValue = x; }

    private:
    int storedValue;
};
