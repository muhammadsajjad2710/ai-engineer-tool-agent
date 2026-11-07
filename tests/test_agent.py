from src.agent import run
def test_tools():
    assert run("shipping time")["tool"] == "faq"
    assert run("calc 2+3*4")["answer"] == "14"
