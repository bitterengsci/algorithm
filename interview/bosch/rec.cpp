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
void createShapes(vector<shared_ptr<Shape> > &shapes) {
    int radius = 5;
    int width = 10, height = 20;
    shapes.push_back( std::make_shared<Circle>(radius) );
    shapes.push_back( std::make_shared<Rectangle>(width, height) );
}

// accepts two iterators and computes the sum of all areas of all shapes in the range.
template< typename IterT>
double accumulateShapeAreas( IterT start_it, IterT end_it) {
    double area = 0;
    while(start_it < end_it){
        area += (*start_it).get()->getShapeArea();
        //cout<<area<<endl;
        start_it ++;
    }
    return area;
}


int main(){
    vector<shared_ptr<Shape> > shapes;
    createShapes(shapes);
    //cout << shapes.size() << endl;
    cout << accumulateShapeAreas(shapes.begin(), shapes.end()) <<endl;
    return 0;
}