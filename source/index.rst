.. _base-conversion-kit:

Base-Conversion-Kit
===================

.. toctree::
 :numbered:


Welcome
-------

Welcome to the home page of Base-Conversion-Kit. Here, I am going to show you how to interact with this plugin and use it to make your life easier, especially if you are a person that has to deal with a lot of math operations in different bases.

How to use
----------

This module has many different uses. The main functions are:

.. code-block:: python
    :linenos:

    from base_conversion_kit import *

    convert_to_base_n(decimal_number, to_base)
    convert_base(number, from_base, to_base)
    add_numbers(a, b, base)
    subtract_numbers(a, b, base)
    multiply_numbers(num1, num2, base)


Converting Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package offers a flexible function for converting numbers from any base to another:

.. code-block:: python
    :linenos:

    from base_conversion_kit import convert_to_base_n, convert_base

    # Convert a decimal number to binary
    binary_result = convert_to_base_n(42, 2)
    print(f"Binary representation: {binary_result}")

    # Convert a hexadecimal number to octal
    octal_result = convert_base("1A", 8, 16)
    print(f"Octal representation: {octal_result}")

Performing Arithmetic Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Performing arithmetic operations on numbers from different bases is seamless:

.. code-block:: python
    :linenos:

    from base_conversion_kit import multiply_numbers, add_numbers, subtract_numbers

    # Multiply two binary numbers
    result_binary = multiply_numbers("101", "110", 2)
    print(f"Binary multiplication result: {result_binary}")

    # Add two decimal numbers
    result_addition = add_numbers(15, 7, 10)
    print(f"Decimal addition result: {result_addition}")

    # Subtract two hexadecimal numbers
    result_subtraction = subtract_numbers("1A", "B", 16)
    print(f"Hexadecimal subtraction result: {result_subtraction}")

Always, the numbers must be in string format. Otherwise, the functions might not work as expected. (Examples: "1A", "FF")

The bases, on the other hand, must be in int format. (Examples: 2, 8, 16)
