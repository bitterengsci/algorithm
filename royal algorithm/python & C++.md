<!-- TOC -->

- [1. Python Aid Sheet](#1-python-aid-sheet)
- [2. Modern C++ features (after C++11)](#2-modern-c-features-after-c11)
- [3. Containers in C++ STL (Standard Template Library)](#3-containers-in-c-stl-standard-template-library)
- [4. Object-Oriented Programming](#4-object-oriented-programming)
- [5. C++ Questions](#5-c-questions)
- [6. Defensive Programming](#6-defensive-programming)
- [7. Optimize the code](#7-optimize-the-code)
- [8. Design Pattern 设计模式](#8-design-pattern-设计模式)

<!-- /TOC -->


# 1. Python Aid Sheet
BFS     ->  Queue First In First Out  append, pop(-1)
DFS     ->  Stack Last In First Out   append, pop()
Deque   ->  append (insert element at right end), appendleft (insert element at right end)
            pop (delete element from right end), popleft (delete element from left end)

preorder (node-left-right)
inorder (left-node-right)
postorder (left-right-node)

```python
# % reminder 余数 // divisor 商
dict = dict.keys() = an iterator across dict key

thisdict.update({"key": "value"})
thisdict.pop("key")  # remove the item with the specified key name
del thisdict["key"]
del thisdict # del keyword can also delete the dictionary completely
thisdict.clear()
thisdict.get("key", default_value) 

l = ['c', 'a', 'b']
l.sort(reverse= key=) # no return, modify l inplace
new_l = l.sorted()
new_l = sorted(l)
print(l, new_l) # ['c', 'a', 'b'] ['a', 'b', 'c']

Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort

# argsort without numpy
sorted(range(len(s)), key=lambda k: s[k])
[i for (val, i) in sorted((val, i) for (i, val) in enumerate(seq))]
[x for x, y in sorted(enumerate(seq), key = lambda x: x[1])]
sorted(range(len(seq)), key=seq.__getitem__)

# customize sort (sort in-place, do not return anything)
intervals.sort(key=lambda x: (x[1], -x[0]))

set.add(element)

# zip(*iterables) takes iterables (can be zero or more), aggregates them in a tuple and return it
index = [1, 2]
l = ['c', 'a', 'b']
for i in zip(index, l):
    print(i)
# (1, 'c')
# (2, 'a')

for i, item in enumerate(l):
    print(i, item)
# 0 c
# 1 a
# 2 b

if l1: # if l1 is not None
if not l1: # if l1 is None

for x in 'abcde':  # iterate in string
    print(x)

math.ceil()
math.floor()
round(number, ndigits=2)   # 四舍五入

float('inf')
print(-2**31, 2**31-1)    # -2147483648 2147483647 [-sys.maxsize-1, sys.maxsize]
print(-2**63, 2**63-1)    # [-9223372036854775808, 9223372036854775807] 

import sys
print(sys.maxsize, - sys.maxsize - 1)  # MAX, MIN
print((1 << 63) - 1)
# 32 Byte INT_MAX (2147483647) INT_MIN (-2147483648)
# 64 Byte INT_MAX (9223372036854775807) INT_MIN (-9223372036854775808)


R, C = len(matrix), len(matrix[0])  # assert len(matrix) != 0
mat = [[0] * C for _ in range(R)] 

range(len(T) - 1, -1, -1) = reversed(range(T))   # reversely

# binary search
start, end = 0, len(nums) - 1
while start + 1 < end:
    mid = start + (end - start) // 2   # mid = (start + end) // 2 no overflow  or >> 1
    if CONDITION:
        end = mid
    else:
        start = mid
```



# 2. Modern C++ features (after C++11)
- type aliases (using)
- uniform initialization, non-static member initialization
    ```cpp
    class demo {

      public: demo(int var1_, bool var2_, string var3_) : var1(var1_), var2(var2_), var3(var3_) {} 
    };  
    ```
- auto(typed variables are deduced by the compiler according to the type of their initializer)
- range-based for loops      
    ```cpp
    std::array<int, 5> array {1, 2, 3, 4, 5};
    for(int &x : array) { }
    ```
- smart pointers
- nullptr (of type std::nullptr_t and can be implicitly converted into pointer types); NULL is not convertible to integral types except bool
- move semantics
- Variadic templates
- delete, default        demo(const demo &) = delete;  demo &operator=(const demo &) = delete;
- delegating constructors: constructors can call other constructors in the same class using an initializer list
- lambda expression



# 3. Containers in C++ STL (Standard Template Library)
* Sequence Container (can be accessed sequentially)
    - array: Static contiguous array 
    - vector: Dynamic contiguous array 
    - deque: Double-ended queue 
    - forward_list: Singly-linked list 
    - list: Doubly-linked list 
* Associative Container: (sorted data structure, quickly searched in O(logn))
    - Set: Collection of unique keys, sorted by keys
    - Map: Collection of key-value pairs, sorted by keys, keys are unique
    - multiset: Collection of keys, sorted by keys (= set with duplicate keys)
    - multimap: Collection of key-value pairs, sorted by keys 
* Unordered Associatve Container: (unsorted (hashed) data structures, quickly searched O(1) amortized, O(n) worstcase) 
    - unordered_set: Collection of unique keys, hashed by keys
    - unordered_map: Collection of key-value pairs, hashed by keys, keys are unique
    - unordered_multiset: Collection of keys, hashed by keys 
    - unordered_multimap: Collection of key-value pairs, hashed by keys 
* Container Adaptor: a different interface for sequential containers
    - stack: Adapts a container to provide stack (LIFO data structure)
    - queue: Adapts a container to provide queue (FIFO data structure)
    - priority_queue: Adapts a container to provide priority queue



template <typename T>

std::vector<T>
- stores contiguously, elements can be accessed through iterators or using offsets.
- random access O(1)
- insert/remove elements at the end amortized O(1)
- insert/remove elements O(n)


std::tuple<T1, T2...>
- a fixed-size collection of heterogeneous values

std::pair<T1, T2>
- store two heterogeneous objects as a single unit
- a specific case of a std::tuple with two elements

std::queue<T>
- FIFO

std::deque<T>
- indexed sequence container; automatically expanded and contracted
  - Expansion of a deque is cheaper than std::vector because it does not involve copying of the existing elements to a new memory location.
- random access O(1)
- insert/remove elements at the beginning/end O(1)
- insert/remove elements O(n)


std::map<KeyType, ValueType>
- a sorted associative container that contains key-value pairs with unique keys
- implemented as red-black trees
- search/remove/insert O(logn)

std::unordered_map
- an associative container that contains key-value pairs with unique keys
- elements not sorted in any particular order, but organized into buckets (depending on hash of the keys)
- search/remove/insert average O(1)


# 4. Object-Oriented Programming
Inheritance
* the capability of a class to derive properties and characteristics from another class
* Modes of Inheritance
    - Public: If we derive a sub class from a public base class. Then the public member of the base class will become public in the derived class and protected members of the base class will become protected in derived class.
    - Protected: If we derive a sub class from a Protected base class. Then both public member and protected members of the base class will become protected in derived class.
    - Private: If we derive a sub class from a Private base class. Then both public member and protected members of the base class will become Private in derived class. 
* Types of Inheritance
    - Single Inheritance: a class is allowed to inherit from only one class. i.e. one sub class is inherited by one base class only.
    - Multiple Inheritance: a class can inherit from more than one classes. i.e one sub class is inherited from more than one base classes.
    - Multilevel Inheritance: a derived class is created from another derived class.
    - Hierarchical Inheritance: more than one sub class is inherited from a single base class. i.e. more than one derived class is created from a single base class.
    - Hybrid (Virtual) Inheritance: implemented by combining more than one type of inheritance. 
    - A special case of hybrid inheritance - Multipath inheritance: A derived class with two base classes and these two base classes have one common base class. An ambiguity can arrise in this type of inheritance. 


Polymorphism
* the ability of a message to be displayed in more than one form
* Compile-time Polymorphism
  - Function Overloading: two or more functions have the same name but different parameters
  - Operator Overloading: make operators to work for user defined classes
    - operators cannot be overloaded: .(成员访问符), :: 域运算符, ?:条件运算符号, sizeof 长度运算符号, .* (成员指针访问运算符号)
* Run-time Polymorphism
  - Function overriding & virtual function


Encapsulation
* binding together the data and the functions that manipulates them
* In C++ encapsulation can be implemented using Class and access modifiers (public, protected, private).


Abstraction
* Data abstraction refers to providing only essential information about the data to the outside world, hiding the background details or implementation.
* Abstraction using Classes: Class helps to group data members and member functions using available access specifiers. A Class can decide which data member will be visible to outside world.
* Abstraction in Header files


# 5. C++ Questions

function call stack
- responsible for maintaining the local variables and parameters during function execution
- Calling a function pushes another stack frame onto the call stack which has enough space for the arguments to the function any local variables.
- Returning pops the stack frame of function called off the call stack
- when the main function returns, its stack frame will be popped off and control will be returned to the C runtime system.


Stack Memory vs Heap Memory
* Stack Memory
  - temporary memory allocation scheme
  - contiguous blocks of memory (linear, and never become fragmented)
  - less storage space as compared to Heap memory
  - allocation and de-allocation is faster as compared to Heap memory allocation
  - safer because the data stored can only be access by owner thread
* Heap Memory
  - accessible or exists as long as the whole application(or java program) runs
  - The name heap has nothing to do with the heap data structure. It is called heap because it is a pile of memory space available to programmers to allocated and de-allocate. (hierarchical)
  - allocated during the execution of instructions written by programmers
  - larger, as compared to stack memory
  - not threaded-safe, data is accessible or visible to all threads
  - If a programmer does not handle Heap memory well, a memory leak can happen.


Stack Unwinding


进程、线程的区别？如何在进程间、线程间同步或通信？

开闭原则 The Open/Closed Principle(OCP): software entities should be open for extension, but closed for modification

pointer (* star) vs reference (& ampersand)
* Pointer variables are used to store the address of variable.
* When a parameter is declared as reference, it becomes an alternative name for an existing parameter.
    - References are used to refer an existing variable in another name whereas pointers are used to store address of variable.
    - References cannot have a null value assigned but pointer can.
    -  A reference variable can be referenced by pass by value whereas a pointer can be referenced by pass by reference.
    - A reference must be initialized on declaration while it is not necessary in case of pointer.
    - A reference shares the same memory address with the original variable but also takes up some space on the stack whereas a pointer has its own memory address and size on the stack.
* dangling pointer: point to an object destructed already 
    - 为了避免出现“悬空指针”引发不可预知的错误，在释放内存(free(p); )之后，常常会将指针p赋值为 NULL
* wild pointer: 未初始化的指针 char *p; (无任何指向/不确定其具体指向的指针)
* this pointer
    - this pointer is passed as a hidden/implicit argument to all nonstatic member function calls and is available as a local variable within the body of all nonstatic functions
    - this pointer is not available in static member functions as static member functions can be called without any object (with class name)
    - this指针指向对象的首地址, 成员函数可以通过this指针区分不同对象的成员数据
    - this指针 (友元)


virtual
* virtual, pure virtual function
* virtual destructor
    - 父类的析构函数必须为虚函数
    - Deleting a derived class object using a pointer of base class type that has a non-virtual destructor results in undefined behavior. Thus the base class should be defined with a virtual destructor.
* virtual base class
* virtual inheritance
* 构造函数和析构函数可以是虚函数嘛? 可以是纯虚函数嘛?
* virtual virtual和多态
- 什么是虚函数？什么是虚继承？虚函数和虚继承是如何实现的？ 虚函数表? 纯虚函数


const
* const function
    - const void foo();    (void foo() const; Not valid)
* const member function of a class
    - class A { void foo() const; };
* const function parameters
    - void foo(const int x);
    - x cannot be changed inside this function
* const return type
    - const int foo(int y);
* constexpr 和 const constexpr为常量(表达式), 类似宏 → 编译时, 不开辟内存 const 只读变量, 依旧是变量, 只不过不可改 运行时


smart pointer
* shared_ptr
    - 如何实现一个shared_ptr? (全局变量, 计数器 + 指针 + 判断何时析构)
* unique_ptr
* weak_ptr


内存引用技术, 显式拷贝 cv::Mat 实现 (opencv为引用, Eigen为赋值)


Deep Copy
- 深拷贝, 浅拷贝 指针地址的拷贝为浅拷贝


static
- static函数无this指针传入
- 访问类的成员变量, 若此成员变量非static类型, 则无法找到, 会报错


explicit
- used to mark constructors to not implicitly convert types


extern


violate
- 编译器不优化代码 set flag -o3 (优化代码, 优化等级为3) -os 以speed为目的优化代码; Debug模式不优化代码, Release模式优化
- prevent the compiler from applying any optimizations on objects that can change in ways that cannot be determined by the compiler


override 重写/覆盖 overload重载
- Overriding implements Runtime Polymorphism whereas Overloading implements Compile time polymorphism.
- The method Overriding occurs between superclass and subclass. Overloading occurs between the methods in the same class.
- Overriding methods have the same signature i.e. same name and method arguments. Overloaded method names are the same but the parameters are different.
- With Overloading, the method to call is determined at the compile-time. With overriding, the method call is determined at the runtime based on the object type.


左值和右值 右值引用的意义 → 为临时变量续命 int a = 3; 正确 int &a = 3; 错误 int &&a = 3; 正确 vec3d &&v = vector3d(0, 0, 1);


6个特殊成员函数: 构造, 析构, 移动, 赋值 ..
```cpp
class Foo {
public:
    string s;
    Foo();    // 默认构造函数: 默认构造函数指不需要参数就能初始化的构造函数
    ~Foo();   //析构函数
    Foo(const Foo& foo) s = foo.s;  // 复制构造函数 copy constructor 使用该类的对象作为参数的构造函数
    Foo& operator=(const Foo& foo) s = foo.s; return * this;   // 复制赋值运算符 copy assignment operator; 重载等号=, 将该类的对象赋值给已定义对象
    Foo(Foo&& foo) s = std::move(foo.s);  // 移动构造函数 move constructor
    Foo& operator=(Foo&& foo) s = std::move(foo.s); return *this;  // 移动赋值运算符 move assignment operator
};
```

C++编译器自动为类产生的四个缺省函数: 默认构造函数，析构函数，赋值函数, 拷贝构造函数


RAIL: 析构即释放 std::mutex → std::unique_lock lock(m);

capacity (reserve), size (当前)

五大原则


#include<file.h>从标准库路径寻找和引用file.h, #include "file.h" 从当前工作路径搜寻并引用file.h

在头文件中进行类的声明，在对应的实现文件中进行类的定义, 可以提高编译效率，因为只需要编译一次生成对应的.obj文件后，再次应用该类的地方，这个类就不会被再次编译


抽象类不用来定义对象而只作为一种基本类型用作继承

对象间是通过类的静态成员变量来实现数据的共享。静态成员变量占有自己独立的空间不为某个对象所私有

类是对象的抽象，对象是类的实例


基类指针调用子类的虚函数; 虚函数具有多态性


STL? std::vector std::map.   链表是std::list

set 和map是红黑树，unordered是哈希表

vector扩充为什么是2倍
模板元编程，特化、偏特化(Partial Template Specialization)
public/protected/private


一、计算机基础 
Intel和Arm的区别是什么？  
库函数和系统调用的区别？ 动态链接库和静态链接库的区别？ 
CPU吞吐量和时延的区别是什么？ 
缓存的作用是什么？缓存的有效性依赖于什么？ 
编译型语言和解释型语言的区别是什么？请举例说明。

二、
什么是拷贝构造函数、拷贝赋值运算符、移动构造函数、移动赋值运算符？ 
如何理解面向对象编程？简述你所了解的某个开源代码是如何应用面向对象编程的。 
什么是右值引用？右值引用存在的意义是什么？ 

三、数据结构和算法 可变长数组是如何实现的？（比如C++中的std::vector，Python中的list）。 常用的容器类都有哪些？它们的特点各是什么？它们内部是如何实现的？ 常用的排序算法的原理和时间复杂度。 链表反转。 二叉树遍历，先序遍历、中序遍历、按行遍历，递归形式与非递归形式。


```cpp
// Test the compiler is big endian or little endian
#include <stdio.h>

void show_mem_rep(char * start, int n) {
    int i;
    for (i=0; i<n; i++)
        printf(" %.2x", start[i]);
}

int main(){
    int num = 0x01234567;
    show_mem_rep((char* ) &num, sizeof(num));
}
```


# 6. Defensive Programming
Defensive coding allows software to behave in a correct manner, despite incorrect input.
- check preconditions (program only continues executing upon valid input)
- assertion inside methods (when calling other class methods or external libraries)



# 7. Optimize the code
When ask to optimize the code, think of:
- binary search, O(N) --> O(logn)
- hashing, O(N) --> O(1)
- in-place operation 



# 8. Design Pattern 设计模式