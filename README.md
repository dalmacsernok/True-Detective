# True Detective

## Story

True Detective loves the truth, seeks the truth night and day. He keeps asking
"Is it true that... ?" about everything, even the most profane aspects of the world.

The only thing that makes him happy is grabbing the truth value of the case
being examined in _one, single, crystal clear expression_. For example, whether
someone is a queen can be answered with the expression `has_been_crowned and not is_male`.

His assistant, Dr Whatif admires this ability and always tries to reproduce
the results of his friend. Unfortunately he lacks the logical skills of
True Detective: he is only able to think in a series of simple conditionals
(_if_ this _then_ that), and he doesn't know about logical operators or any other
higher level constructs. Nevertheless, although in a much more roundabout fashion,
he is always able to reproduce the results of True Detective. For example, to
the above queen question Dr Whatif would write something like this:

```python
if is_male:
    return False
else:
    if has_been_crowned:
        return True
    else:
        return False
```

Which mindset is closer to you?
To check this, you need to solve cases (implement functions) both ways.
Write two implementations for each required function, one in `truedetective.py`
and one in `whatif.py`.

Tests are included with many expected answers in the repository. Keep running
them to check your solutions.


## What are you going to learn?

- Write conditionals.
- Use logical operators.
- Simplify boolean expressions.
- Run tests.

## Tasks

1. Is a given positive integer an odd number with two digits? Implement `is_twodigit_odd` in two versions.
    - Dr Whatif's solution has no logical operators and passes all the tests.
    - True Detective's solution only has one return statement and passes all the tests.

2. Does a user have write access to a Unix file? The parameters are `user`, `users_groups`, `file_owner`, `writable_by_owner`, `file_group`, `writable_by_group`, `writable_by_others`, `sudo_mode`.
Implement `has_access` in two versions.
    - Dr Whatif's solution has no logical operators and passes all the tests.
    - True Detective's solution only has one return statement and passes all the tests.

3. Is a given year (AD) a leap year in the Gregorian calendar? The official definition is the following: "Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400."
Implement `is_leap_year` in two versions.
    - Dr Whatif's solution has no logical operators and passes all the tests.
    - True Detective's solution only has one return statement and passes all the tests.

4. Is a given day of a month Sunday? We also know the first day of the month (one of `('M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su')`. Supposing it is a 31-day-long month, days other than `1..31` cannot be Sundays.
Implement `is_sunday` in two versions.
    - Dr Whatif's solution has no logical operators and passes all the tests.
    - True Detective's solution only has one return statement and passes all the tests.

5. Should True Detective bring an umbrella when going out? Well, it depends. Obviously he _should_ when it rains, _unless_ the wind is too strong. Wind strength greater than or equal to 7 (on the Beaufort scale) would turn the umbrella inside out.
Taking the umbrella is also _reasonable_ when it is not raining but it is cloudy, the wind is not too strong, _and_ there are signs of a rain coming. Such signs are: red sky during sunset // flowers smell stronger than normal // spiders come down from their webs // cattle lie down in groups in the fields.
But True Detective also likes to take his umbrella when the sun is shining strongly. Again, unless the wind situation is not too stormy.
Implement `should_bring_umbrella` in two versions.
    - Dr Whatif's solution has no logical operators and passes all the tests.
    - True Detective's solution only has one return statement and passes all the tests.

6. [OPTIONAL] Should one take a nap? Follow [this](https://venngage-wordpress.s3.amazonaws.com/uploads/2019/08/what-is-a-decision-tree-7.png) decision tree.
Implement `should_take_a_nap` in two versions.
    - Dr Whatif's solution has no logical operators and passes all the tests.
    - True Detective's solution only has one return statement and passes all the tests.

## General requirements

None

## Hints

- There are two test files included that use the `pytest` module.
  Check how to run `pytest` first.
- Write Dr Whatif's version first, that can help you build the denser solution.
You may find a way to do the conversion systematically.
- Usually there are multiple equivalent solutions both for Dr Whatif and for
True Detective. Try to come up with alternative solutions. After finishing the project,
  compare your solutions with those of others.
- `has_access` function requires the following parameters.
  * `user`: integer type, represents the ID of the user.
  * `users_groups`: list type, represents the IDs of each user group that has write access to the file.
  * `file_owner`: integer type, represents the ID of the file owner.
  * `writable_by_owner`: boolean type, represents whether the file is writable by owner.
  * `file_group`: integer type, represents the ID of the group that has write access to the file.
  * `writable_by_group`: boolean type, represents whether the file is writable by the group.
  * `writable_by_others`: boolean type, represents whether the file is writable by others.
  * `sudo_mode`: boolean type, represents whether the sudo mode is activated.


## Background materials

- [Logical operators](project/curriculum/materials/pages/notebooks/logical-operators.html)
- <i class="far fa-exclamation"></i> [About pytest](https://docs.pytest.org/en/latest/)

