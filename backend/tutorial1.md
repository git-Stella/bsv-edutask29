# PA1417 symbol means **stop reading and try it yourself** before
continuing. Each stop is followed by a collapsed hint conftest.py
pytest.ini requirements.pip src/
util/
helpers.py test/
finished reference examples (do not edit these)
where you write your own tests today
```
create it before moving on.
Open `pytest.ini` and read through it:
```ini
[pytest]
addopts =
--cov-report term-missing
--cov=src
testpaths =
test
markers =
demo: all tests for demonstration purpose (run with '-m demo')
unit: all tests on unit/component level (run with '-m unit')
integration: all tests on integration level (run with '-m
integration')
```
- `addopts` where pytest looks for test files
- `markers` **Use the Test Design Technique to derive which tests
should exist for this method. Think about the inputs and expected
outputs before expanding the hint.**
<details>
<summary>Hint: Test Case Table</summary>
```
hasAttribute(obj: dict, attribute: str) -> bool
True if obj is not None and attribute is not a key in obj
False not from the code itself. Code is not ground truth.
</details><br>
---
### Step 2: Implementing the Tests
Create the file `backend/test/unit/test_hasAttribute.py`.
> The `test_` prefix is required **Stop here. Let's slowly write
our first unit test together.**
<details>
<summary>Solution Here</summary>
In the `test_hasAttribute.py` file, add the following code:
```python
import pytest
from src.util.helpers import hasAttribute
@pytest.mark.unit
def test_hasAttribute():
result = hasAttribute({'name': 'Jane'}, 'name')
assert result == True
```
</details><br>
set up the preconditions
2. **Act** verify the result matches the expected value
> **Principle:** One assert statement per test. Multiple asserts
in one test means a failure in the first hides the rest **Run
`pytest -m unit` from `backend/` and read the output before
continuing.**
Pytest prints one character per test:
- `.` failed
- `E` the code crashes rather than returning the expected value.
This is a seeded defect: your test found a real bug.
> Observe the coverage table that appears after the results.
Because `pytest.ini` sets `addopts = --cov-report term-missing --
cov=src`, coverage is measured on every run automatically. The
**Missing** column shows which lines were never executed.
---
### Step 4: Reducing Redundancy with Fixtures
`validateAge`
Open `src/util/helpers.py` and read the `validateAge` method in
the `ValidationHelper` class.
**Stop here. Create `backend/test/unit/test_validateAge.py` and
try writing tests the same way you did for `hasAttribute`.**
<details>
<summary>What complications did you run into?</summary>
To call `validateAge`, you need a `ValidationHelper` instance.
Its constructor takes a `UserController` if the test fails, we
know the bug is in `validateAge`, not in any of its dependencies.
Python's standard library provides `unittest.mock.MagicMock`. You
can use it to create a fake `UserController` whose `.get()`
method returns whatever dict you tell it to **Stop here. Rewrite
your tests using what you just read before moving on.**
Run `pytest -m unit`. Both the new tests and the `hasAttribute`
tests will run.
---
### Step 6: Avoiding Loops **Stop here. Rewrite
`test_validateAge.py` as a single parametrized test function
covering all 9 rows before moving on.**
<details>
<summary>Hint: Parametrize Syntax</summary>
Writing all 9 cases as separate functions is correct but
repetitive. Loops in test code are worse read the output to
identify which age value exposes the seeded defect.
> **Principle:** Avoid control structures (loops, conditions) in
test code. Use `@pytest.mark.parametrize` instead.
---
### Step 7: Combining Fixtures with Parametrization
no extra wiring needed.
</details><br>
Run `pytest -m unit`. The results should be identical to before
7)
By the end of Step 7, `backend/test/unit/` contains two files
demonstrating the two core patterns for unit testing in this
course:
| File | Concepts covered
|
| ---------------------- |
------------------------------------------- |
| `test_hasAttribute.py` | AAA pattern, fixtures, coverage
|
| `test_validateAge.py` | Mocking, parametrize, parametrized
fixtures |
The two seeded defects you found:
1. `hasAttribute` one boundary condition is off by one
These are intentional. Do not fix them `test_diceroll.py`
**Corresponding demo file:** `backend/test/demo/test_impure.py`
Open `src/util/helpers.py` and read the `diceroll` function and
its docstring.
```
diceroll() -> bool
True otherwise
```
Unlike `ValidationHelper`, this function does not accept any
arguments **Stop here. Create
`backend/test/unit/test_diceroll.py` and write a single test that
calls `diceroll()` and asserts a specific return value.**
Run it a few times with `pytest -m unit --capture=no`. What do
you observe? Does the test reliably pass or fail?
Why this is a problem: A test that passes sometimes and fails
sometimes is worse than no test at all **Stop here. Rewrite your
test so that `random.randint` always returns a fixed value before
moving on.**
<details>
<summary>Hint: Using `patch`</summary>
The standard library's `unittest.mock.patch` temporarily replaces
a name in a module with a `MagicMock` during the test. Use it as
a context manager:
```python
with patch('module.path.to.name') as mock_name:
mock_name.return_value = ...
# inside this block, the real function is replaced
```
The name to patch is the one your module _uses_ **Stop here.
Identify the boundary values from the docstring and rewrite the
test using `@pytest.mark.parametrize` to cover all cases.**
<details>
<summary>What To Expect</summary>
One of your parametrized test cases will fail. Read the output to
identify which value exposes a discrepancy between the docstring
and the code.
</details><br>
> **Principle:** Patch non-injectable dependencies to make impure
functions deterministic and testable.
---
### Step 9: Fixture Teardown with `yield` read it carefully, then
copy the class definition into your new file
`backend/test/unit/test_filehandler.py`.
Testing `FileHandler` requires a real file to exist on disk. Your
fixture must create a temporary JSON file before the test and
delete it after **Stop here. Write a test that creates the file,
tests the result, and cleans up **Stop here. Move the file
creation and `FileHandler` instantiation into a `@pytest.fixture`
using `return`.**
Run the test again. Now ask: is the file ever cleaned up?
regardless of whether the test passed or failed. Run the test,
then check that the temporary file no longer exists on disk.
> **Principle:** Use `yield` in a fixture when the setup requires
a matching teardown (resource acquisition, file creation,
database seeding, etc.).
As a final step, wrap your fixture and test inside a class. In
pytest, fixtures defined inside a class are scoped to that class
and do not conflict with identically-named fixtures elsewhere.
Compare your result with `test_yield.py` in the demo folder.
---
### Step 10: Patching Hard-Coded Dependencies there is no
constructor parameter to inject a mock into.
**Stop here. Write a working test using `patch` to replace the
hard-coded dependencies before moving on.**
<details>
<summary>Hint: Patching Classes</summary>
`patch` can replace a _class_ for the duration of a test, so that
when the code under test calls `UserController(...)` or
`DAO(...)`, it gets a mock instead of the real object:
```python
with patch('src.util.helpers.SomeClass', autospec=True) as
MockClass:
MockClass.return_value = ... # controls what __init__ returns
```
You need to patch both `UserController` and `DAO`. You can nest
two `with patch(...)` blocks or combine them on one line using a
backslash continuation.
</details><br>
`patch` can also be applied as a _decorator_ directly above a
fixture or test function. Try rewriting your fixture using
`@patch(...)` decorators and compare both syntaxes against
`test_patch.py` in the demo folder.
> **Principle:** Patch at the location where the name is used,
not where it is defined `test_namespaces.py` (Exercise)
**Corresponding demo file:**
`backend/test/demo/test_namespaces.py`
The most common mistake with `patch` is patching the wrong
namespace. The rule is:
> **Patch where the name is looked up, not where the object is
defined.**
When a module does `from foo import bar`, it creates its own
reference to `bar`. Patching `foo.bar` after the import has no
effect `test_1`**
`test_2`**
but `helpers.py` imports `random` as a whole module and calls
`random.randint(...)`. Consider: does patching `random.randint`
still work here, or do you need a different path?
</details><br>
**Exercise 3 **Stop here and fill in `test_3` before moving on.**
<details>
<summary>Hint</summary>
This test combines two techniques: inject a mocked DAO into
`UserController` via the constructor (as you did in earlier
steps), and separately patch `re.fullmatch` so that email
validation always passes. You need to figure out the correct
namespace string for `fullmatch` given how it is called inside
`usercontroller.py`.
</details><br>
Run each test after filling in its `patch(...)` argument:
```
pytest backend/test/demo/test_namespaces.py -m namespaces -v
```
> **Tip:** When unsure of the correct namespace, add a
`print(mock)` inside the `with` block and run with `--capture=no`
to confirm which object was actually replaced.
---
## Final Summary
| Step | File | New concepts introduced
|
| ---- | --------------------------- |
------------------------------------------------------------- |
| 17 | `test_validateAge.py` | DI mocking, parametrize,
parametrized fixtures |
| 8 | `test_diceroll.py` | `patch` as context
manager, impure functions |
| 9 | `test_filehandler.py` | `yield` in fixtures,
fixture teardown, class-based tests |
| 10 | `test_validationhelper2.py` | Patching hard-coded deps,
decorator vs context manager syntax |
| 11 | `test_namespaces.py` (demo) | Patch namespace
resolution, combining DI and patching |
The seeded defects you should have encountered:
1. `hasAttribute` off-by-one boundary condition
3. `diceroll` they are there to practice recognising and
documenting defects.
