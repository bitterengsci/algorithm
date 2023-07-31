

```
console.log("%cHello, World", "color: blue; font-size: 40px"); // style the output
```


strict equality operator === compares for both the values and the data types

For the strict inequality operator to return false, the compared values have to have the same value and the same data type. 
5 !== 5 returns false because it is false to say that the number 5 is not of the same value and data type and another number 5. However, 5 !== "5" returns true.

jQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.


**Conditionals**: if - else if - else, switch - case (break) - default
**Loops**: for, for of loop, while

```
var cubes = 'ABCDEFG';
cubes.length
cubes[1]
```


A **truthy** value is a value considered true when encountered in a Boolean context. All values are truthy unless they are defined as [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)/falsey. 

**Falsy**: 

*  `false`, `0` (also `0.0`, `0x0`),  `-0` (also `-0.0`, `-0x0`),  `0n` (BigInt zero, also including `0x0n`, etc. Note there is no BigInt negative zero, the negation of `0n` is `0n`), `""` (empty string value, also `''` and ````), `null` (absence of any value), `undefined`(primitive value), and `NaN`(not a number)
* The only falsy object in JavaScript is the built-in [`document.all`](https://developer.mozilla.org/en-US/docs/Web/API/Document/all)

If the first operand is truthy, the [logical AND operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND) returns the second operand:

```
true && "dog"   // returns "dog"
[] && "dog"   // returns "dog"
```



## **Objects**

* build objects
    * use object literal syntax {}   `var user = {};`
    * with properties and their values `var assistantManager = {name: "ABC", age: 22}`
    * first save an empty object literal to a variable, then use dot notation to declare new properties on the fly, and use the assignment operator to add values to those properties
    * var house = {};
        house.rooms = 4;
        house.color = "pink";
* Add new properties to objects (or update existing properties) using the Dot Notation. Alternatively, Brackets Notation.
    * var house = {};
        house["rooms"] = 4;
        house['color']= "pink";



## JavaScript Data Structures 

* **Arrays** are list-like objects.
    * forEach, filter, map
* Map (similar to an object in JS)
* Set

The **`typeof`** operator returns a string indicating the type of the operand's value.

**rest operator** & **spread operator**

```
**// Join arrays, objects using the rest operator**
const flying = { wings: 2 }
const car = { wheels: 4 }
const flyingCar = {...flying, ...car}
console.log(flyingCar) // {wings: 2, wheels: 4}

**// Convert a string to an array using the spread operator**
const greeting = "Hello";
const arrayOfChars = [...greeting];
console.log(arrayOfChars); //  ['H', 'e', 'l', 'l', 'o']

**// Copy either an object or an array into a separate one**
const car1 = {
    speed: 200,
    color: 'yellow'
}
const car 2 = {...car1}
car1.speed = 201
console.log(car1.speed, car2.speed) // 201, 200
```



## **Object Methods**

```
var car = {};
car.color = "red";
//add a method to the car object so that it can be called as car.turnkey()
car.turnKey = function() { 
  console.log('engine running'); 
}
```


`**document**` object holds the entire structure of the active webpage in the browser's memory. (The entire webpage in the browser's memory, as a JavaScript object)


Functions


## Error Handling

* Common errors in JavaScript
    * **ReferenceError**: one tries to use variables that haven't been declared anywhere
    * **SyntaxError**: invalid JS code
    * **TypeError**: one tries to run a method on a non-supported data type
    * **RangeError**: when we're giving a value to a function, but that value is out of the allowed range of acceptable input values.
    * AggregateError, InternalError, URIError
* Error prevention with try catch
    * try {
                ...
            } catch(err) {
                console.log(err)
            }
* Defensive Programming *assumes* that all the arguments a function will receive are of the wrong type, the wrong value or both.
    * You assume that things will go wrong and you are proactive in thinking about such scenarios before they happen, so as to make your function less likely to cause errors because of faulty inputs.

```
var result = null;
console.log(result);   // null

var x;  // x === undefined (value not initialised, it has the *undefined* data type)
```



## Programming Paradigm

* Functional Programming
    * FP functions return new values
    * **First-class functions**
        * Functions in JavaScript are “first-class citizens”.
        * It means that a function in JavaScript is just another value that we can: pass to other functions; save in a variable; return from other functions.
        * A function in JavaScript is just a value.
    * **Higher-order functions**
    * A higher-order function is a function that has either one or both of the following characteristics: (1) It accepts other functions as arguments (2) It returns functions when invoked
    * Pure Function and Side Effects
        * A pure function returns the exact same result as long as it's given the same values.
        * Another rule for a function to be considered pure is that it should not have side-effects. A side-effect is any instance where a function makes a change outside of itself.
        * This includes: (1) changing variable values outside of the function itself, or even relying on outside variables (2) calling a Browser API (even the console itself!) (3) calling *Math.random()* - since the value cannot be reliably repeated
* Object-Oriented Programming
    * OOP group data and functionality as properties and methods inside objects
    * Methods **update properties** stored in the object instead of generating new return values.



## Declare Variables

* var (function-scoped, if declared outside of a function, globally scoped)
    * `var` variables are "hoisted" to the top of their scope and can be initialized at any point in their scope.
* let (block-scoped; can be reassigned)
* const (block-scoped; cannot be reassigned once initialized)
* recommended to use `let` and `const` over `var` for their more predictable scoping rules. 


**`RegExp`** object is used for matching text with a pattern.



## Template Literals

* backtick characters as delimiters  ``Hello, World!``
* template literal vs string literal
    * (1) variable interpolation (no need to use the *+* operator)
    * let greet = "Hello";
        let place = "World";
        console.log(`${greet} ${place} !`) 
        //display both variables using template literals
        var greet = "Hello";
        var place = "World";
        console.log(greet + " " + place + "!"); 
        //display both variables without using template literals
    * (2) template strings can span multiple lines, **string literals** (strings delimited in single or double quotes) cannot
    * (3) template literals allow for **expression evaluation**
    * // perform arithmetic operation inside a template literal expression
        console.log(`${1 + 1 + 1 + 1 + 1} stars!`)  // *5 stars!*
* nested template literals and tagged templates



## Testing

* e2e 
    * WebdriverJS, Protractor, Cypress
* integration 
    * test how parts of the system interact with other parts of the system, test how separate parts of the apps work together
    * React testing library, Enzyme
* unit
    * test the smallest units of the source code in isolation
* JavaScript doesn't have built-in objects or methods to write tests. Many different libraries have been built for testing, including Jasmine, Mocha, Karma, and qUnit.
* Testing Frameworks Jest (can test JavaScript, React, also Babel, TypeScript, Node, Angular, Vue)
    * Code coverage is a measure of what percentage of the code is covered by tests.
    * Mocking allows to separate the code that you are testing from it's related dependencies. You can use the mocking features to make sure that your unit testing is stand-alone.
    * Snapshot testing is to verify that there are no regressions in the DOM of our apps after some changes to the code base are made.
* Test-Driven Development




## JavaScript in the Browser

JavaScript interactivity

* JavaScript's initial purpose was to **provide interactivity in the browser**
* By the mid-2000s, the jQuery library came out, with the idea of writing less code, but doing more with it. It allowed developers to use a single code-base for various browsers.
* This trend continued and many other frameworks such as React, Vue, Angular, D3, .. came along.
* Together with npm and Node.js, the JavaScript ecosystem is not slowing down.
    * npm is a package manager for the JavaScript programming language.
* Although CSS has developed significantly over the years, it is still JavaScript that allows users to: Get their geolocation, Interact with maps, Play games in the browser,  Handle all kinds of user-triggered events, regardless of the device, Verify form input before sending it to the backend of a webapp, etc.





### Web Data Flow

* Before JSON, the most common data interchange file format was XML (Extensible Markup Language).
* JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax.
    * JSON is a subset of JavaScript. JSON is just a (properly-formatted) string.
    * Only a subset of values in JavaScript can be properly stringified to JSON and parsed from a JavaScript object into a JSON string. These values include:
        * primitive values: strings, numbers, booleans, null
        * complex values: objects and arrays (no functions!)
        * Objects have double-quoted strings for all keys
        * Properties are comma-delimited both in JSON objects and in JSON arrays, just like in regular JavaScript code
        * String properties must be surrounded in double quotes. For example: "fruits", "vegetables"
        * Number properties are represented using the regular JavaScript number syntax; e.g. 5, 10, 1.2
        * Boolean properties are represented using the regular JavaScript boolean syntax, that is: true, false
        * Null as a property is the same as in regular JavaScript; it's just a null
        * You can use object literals and array literals, as long as you follow the above rules





### Event

The **`Event`** interface represents an event which takes place in the DOM. 
https://developer.mozilla.org/en-US/docs/Web/API/Event


### EventTarget

The **`EventTarget`** interface is implemented by objects that can receive events and may have listeners for them.
https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener

addEventListener()



JavaScript modules (import export)

[`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) method **`querySelector()`** returns the first [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element) within the document that matches the specified selector, or group of selectors. If no matches are found, `null` is returned.



### Exercise: Web page content update

capture user input and process it

```
let answer = prompt('What is your name?');
if (typeof(answer) === 'string') {
    var h1 = document.createElement('h1')
    h1.innerText = answer;
    document.body.innerText = '';
    document.body.appendChild(h1);
}

var h1 = document.createElement('h1')
h1.innerText = "Type into the input to make this text change"
var input = document.createElement('input')
input.setAttribute('type', 'text')

document.body.innerText = '';
document.body.appendChild(h1);
document.body.appendChild(input);

input.addEventListener('change', function() {
    h1.innerText = input.value
})
```




### Exercise: Capture Data




