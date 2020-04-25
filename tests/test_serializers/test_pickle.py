from io import BytesIO

import pytest

from regress.impl.serializer.pickle_serializer import PickleSerializer


def test_simple():
    serializer = PickleSerializer()

    out = BytesIO()
    obj = 'abc'
    serializer.dump(obj, out)
    out_bytes = out.getvalue()

    in_ = BytesIO(out_bytes)
    read_obj = serializer.load(in_)
    assert read_obj == obj


if __name__ == '__main__':
    pytest.main(['-s', __file__])
