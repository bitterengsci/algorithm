////////////////

int main(int argc, char *argv [])
{
    int x=4, *y;
    y = &x; (*y) ++;
    printf("%d \n", *y);
    return 0;



}

////////////////



int main(){
    double foo = 4.0;
    const float & bar = foo;
    foo += 2.0;
    cout << bar << endl;
    return 0;
}

////////////////

struct Foo{
    Foo(int i): c{i}, a{i++}, b{++i} {}
    int a, b, c;
};

int main(){
    Foo f{1};
    cout << f.a << f.b << f.c ;
}

////////

using namespace std;

int f(){
    std::cout << 'f' << endl;
    return 0;
}

int g(){
    std::cout << 'g' << endl;
    return 1;
}

int h(const int, const int){
    std::cout << 'h' << endl;
}

int main(){
    h(f(), g());
}


//////////
using namespace std;

struct Animal{
    string type;
};

struct NamedAnimal: public Animal {
    string name;
};

void copy(Animal & a, Animal b){
    a = b;
}

int main(){
    NamedAnimal cat;
    cat.type = "C";
    cat.name = "CA";
    NamedAnimal dog;
    dog.type = "D";
    dog.name = "DA";
    copy(cat, dog);

    cout << cat.type << cat.name << endl;

    return 0;
}


////////

struct Test{
    Test(){}
    Test(const Test & rhs) {std::cout << "copy";}
    Test(Test && rhs){std::cout << "move";}

    Test& operator=(const Test& rhs){
        std::cout << "assign";
        return *this;
    }

    Test& operator=(Test&& rhs){
        std::cout << "move-assign";
        return *this;
    }
};

Test Create(){
    return Test();
}

int main(){
    Test a, b;
    Test c(move(a));
    a = c;
    b = Create();
    Test d(a);
}

////

struct A{
    static int getValue(){
        return 0;
    }
};

int accessValueFromA(const A&a){
    return a.getValue();
}

int main(){
    cout << accessValueFromA(A()) << endl;
    return 0;
}