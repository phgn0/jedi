import jedi.parser as parser
import difflib

code_basic_features = '''
def a_function(a_argument, a_default = "default"):
    """A docstring"""

    a_result = 3 * a_argument
    print(a_result)  # a comment
    if a_default == "default":
        return str(a_result)
    else
        return None
'''


def diff_code_assert(a, b, n=4):
    if a != b:
        diff = "\n".join(difflib.unified_diff(
            a.splitlines(),
            b.splitlines(),
            n=n,
            lineterm=""
        ))
        assert False, "Code does not match:\n%s" % diff
    pass


def test_basic_parsing():
    """Validate the parsing features"""

    prs = parser.Parser(code_basic_features)
    diff_code_assert(
        code_basic_features,
        prs.top_module.get_code()
    )
