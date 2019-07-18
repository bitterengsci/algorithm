//#include <bits/stdc++.h>      https://www.geeksforgeeks.org/bitsstdc-h-c/
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

#include <cstdio>
using namespace std;

#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <iostream>
#include <memory>

using namespace std;

class Shape {
protected:
    double bounding_box_width;
    double bounding_box_height;
public:
    Shape(double width, double height): bounding_box_width(width), bounding_box_height(height){}
    double getShapeArea() {
        return getBoundingBoxArea();
    }
    double getBoundingBoxArea() {
        return bounding_box_width * bounding_box_height;
    }
};

class Circle: public Shape {
private:
    double radius;
public:
    Circle(double radius): Shape(2*radius, 2*radius), radius(radius) {}
    double getShapeArea(){
        return radius * radius * M_PI;
    };
};

class Rectangle: public Shape {
public:
    Rectangle(double width, double height): Shape(width, height){}
};

// creates shapes and adds them to the passed vector
void createShapes(vector<shared_ptr<Shape>> shapes) {
    shapes.push_back( make_shared<Circle>(5) );
    shapes.push_back( make_shared<Rectangle>(10, 20) );
}

// accepts two iterators and computes the sum of all areas of all shapes in the range.
template< typename IterT>
double accumulateShapeAreas( IterT start_it, IterT end_it) {
    double area = 0;
    Shape * p = start_it;
    while(p < end_it){
        area += p.getShapeArea();
        p ++;
    }
    return area;
}


int main(){
    vector<shared_ptr<Shape>> shapes;
    createShapes(shapes);

    cout << accumulateShapeAreas(shapes.begin(), shapes.end()) <<endl;
    return 0;
}