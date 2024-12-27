from python_project_template.awesome import do_something_awesome


def test_do_something_awesome():
    assert isinstance(do_something_awesome(), str)
    assert do_something_awesome() == "Congratulations for taking the first step to build your Python project 🎉"
