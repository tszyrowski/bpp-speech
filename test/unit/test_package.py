import importlib


def test_import():
    """The package imports correctly."""
    # Capturing the exception and then asserting for it makes the failure mode
    # look normal; if we call pytest.fail() inside the except block, we get
    # a long traceback with exceptions raised during outer exception handling.
    exception = None
    try:
        importlib.import_module("bpp_reader")
    except ModuleNotFoundError as err:
        exception = err

    assert exception is None
