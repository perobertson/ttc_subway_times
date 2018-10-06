from __future__ import generator_stop

from click.testing import CliRunner

from ttc_api_scraper import cli


def test_help():
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.output.startswith('Usage:')
    assert 'Show this message and exit.' in result.output
    assert result.exit_code == 0
