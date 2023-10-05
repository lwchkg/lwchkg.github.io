---
layout: article
title: Avoid std::sort(..., ..., std::greater&lt;int&gt;()) and the Like
modified:
categories: algorithm
excerpt: Dealing with problems sorting numbers in C++14, C++11 and C++98.
tags: [c++, sort, greater]
image:
  feature:
  teaser:
  thumb:
comments: true
date: 2017-05-21T09:19:19+00:00
---

To sort items in descending order, we need to pass a comparator to `std::sort`.
Sadly there is little said on how to do this correctly.
In [cppreference.com](http://en.cppreference.com/w/cpp/algorithm/sort), we are told to do like this:

``` c++
// The following is an excerpt from
// http://en.cppreference.com/w/cpp/algorithm/sort
std::array<int, 10> s = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
std::sort(s.begin(), s.end(), std::greater<int>());
// Output sorted values
for (auto a : s) {
  std::cout << a << " ";
}
std::cout << '\n';
```

While the example runs correctly, unfortunately it makes the program hard to maintain.

## What's wrong?

The problem is hard-coding the greater then operator with the `int` type.
If you change the array from `int` into another type, e.g. `double`, errors will happen:

``` c++
std::array<double, 10> s = {4.5, 4.7, 4.4, 4.2, 4.8, 4.6, 4.1, 4.9, 4.0, 4.3};
std::sort(s.begin(), s.end(), std::greater<int>());
// Output sorted values
for (auto a : s) {
  std::cout << a << " ";
}
std::cout << '\n';
```

Here is the output of this program in GCC 7.1:

```
4.5 4.7 4.4 4.2 4.8 4.6 4.1 4.9 4 4.3
```

As you can see, nothing is sorted at all.
The doubles are converted into integers by truncating the fractional parts, and only the integral parts are compared.
The doubles above all converted into 4 before comparison, so the result can be anything depending on the sorting algorithm.
(As a strict weak ordering is not established, there is not even a guarantee that the sort will terminate.)

You may say that I have forgotten to change `std::greater<int>()` into `std::greater<double>()`.
However, **we shouldn't be required to do this at all!**
There are a few why the change to `std::greater<double>()` can be neglected:

* If the `std::sort` statement is located in a remote place (e.g. a different file).
* If the people maintaining the file is unaware of the existence of `std::greater<int>()`.
* If someone just forgot to change.

The sad part is the error cannot even be detected with the `-Wconversion` switch.
Unless you have a dedicated test to detect the error, the error will go straight into production.


## The fix (with C++14)

With C++14, there is a `std::greater<>()`, which means `std::greater<void>()` that automatically deduce types.
So you don't need to shoot your foot by adding the useless type information.
Simple.

Now the program will look like this:

``` c++
std::array<double, 10> s = {4.5, 4.7, 4.4, 4.2, 4.8, 4.6, 4.1, 4.9, 4.0, 4.3};
std::sort(s.begin(), s.end(), std::greater<>());
// Output sorted values
for (auto a : s) {
  std::cout << a << " ";
}
std::cout << '\n';
```

And the program runs correctly ([link](https://wandbox.org/permlink/7D4o3xt89GLqWeel)):

```
4.9 4.8 4.7 4.6 4.5 4.4 4.3 4.2 4.1 4
```


## C++11 only?

In C++11, you don't have `std::greater<>()`, but you still have `std::greater<decltype(name_of_variable)::value_type>()`.
I am very surprised that I can't find the solution in Google, and that's why I'm writing this post.

It is always said that `sizeof(name_of_variable)` is preferred to `sizeof(name_of_type)`, so the same should be done to `std::greater`.



## What if I can't even use C++11?

If somehow you are forced to use C++98, then you cannot use `auto` and `decltype`.
So you have only a few less desirable options: templates and typedefs.

To use templates for type deduction, you need to make a template function:

``` c++
template<class T>
void sort_descending(T begin, T end) {
    std::sort(begin, end, std::greater<typename T::value_type>());
}
```

Here is an example using the template function to sort:

``` c++
#include <algorithm>
#include <iostream>
#include <vector>

template<class T>
void sort_descending(T begin, T end) {
    std::sort(begin, end, std::greater<typename T::value_type>());
}

int main()
{
    double data[] = {4.5, 4.7, 4.4, 4.2, 4.8, 4.6, 4.1, 4.9, 4.0, 4.3};
    std::vector<double> s(data, data + sizeof(data) / sizeof(*data));

    sort_descending(s.begin(), s.end());
    // Output sorted values
    for (std::vector<double>::iterator a = s.begin(); a < s.end(); ++a) {
      std::cout << *a << " ";
    }
    std::cout << '\n';

    return 0;
}
```

If you don't feel like adding the template function, you can use `typedef` instead.
There is not point of giving such an example though.
