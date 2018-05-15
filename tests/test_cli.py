import pytest
import sys
from mock import patch
from ragnar.cli import cli


from contextlib import contextmanager
from io import StringIO

@contextmanager
def capture_sys_output():
    capture_out, capture_err = StringIO(), StringIO()
    current_out, current_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = capture_out, capture_err
        yield capture_out, capture_err
    finally:
        sys.stdout, sys.stderr = current_out, current_err

class TestCli():

    def test_no_args(self):
        with pytest.raises(SystemExit) as cm:
            with capture_sys_output() as (stdout, stderr):
                cli([])
        assert cm.type == SystemExit
        assert cm.value.code == 0
        assert "usage" in stdout.getvalue()

    @patch('ragnar.cli.build_kernel')
    def test_build_kernel_no_args(self, mock):
        cli(['build-kernel'])
        assert mock.called
        assert mock.call_args[0][0].clean == None
        assert mock.call_args[0][0].machine == None

