---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

# Base-Conversion-Kit

### Welcome
Welcome to the home page of Base-Conversion-Kit. Here, I am going to show you how to interact with this plugin and use it to make your life easier, especially if you are a person that has to deal with a lot of math opertions in different bases.


## How to use

This module has many different uses. The main functions are:

```python
convert_to_base_n(decimal_number, to_base)
convert_base(number, from_base, to_base)
add_numbers(a, b, base)
subtract_numbers(a, b, base)
multiply_numbers(num1, num2, base)
```

> Always, the numbers must be in string format. Otherwise the functions might not work as expected.(Examples: "1A", "FF")

> The bases, on the other hand, must be in int format.(Examples: "2", "8", "16")
