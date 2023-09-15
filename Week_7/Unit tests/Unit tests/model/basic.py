import re


"""
1. Unit of functionality
    Should test only a single unit of functionality rather than several and should not be dependent on the output of another unit test.

2. Deterministic
    Tests should always produce the same outputs with the same inputs.

3. Fast
    Ideally take only a few seconds to run.

4. Self Contained
    should not connect to an external resource (use mocking).

5. Coverage
    Tests should cover all lines of code with valid assertions.

6. Decoupled
    Tests should not be dependent on other tests or data.
"""






def convert_camelcase_to_snake_case(name: str) -> bool:
    """
    Takes a camel case name and converts to snake case e.g. "testVariable" > "test_variable"
    :param name: str
    :return: str
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
