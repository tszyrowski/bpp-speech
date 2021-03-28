"""Test the node_config module."""
import pathlib

from bpp_reader import config


def test_get_node_config_default():
    """Test get_node_config uses the default file when not specified."""
    assert config.CONFIG["project"] == "bpp"


def test_read_node_config_from_file():
    """Test the expected output matches the node config provided."""
    config_file = pathlib.Path.cwd() / "test/data/test_config.json"
    read_config = config.get_config(config_file)
    expected_config = {"test_name": "test_value"}
    assert read_config == expected_config
