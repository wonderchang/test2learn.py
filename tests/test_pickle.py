import pickle


def test_dump_hybrid_datatype_dict_to_file_and_load_it__equivalent(tmpdir):
    obj = {
        'a': [1, 2.0, 3, 4+6j],
        'b': ("character string", b"byte string"),
        'c': {None, True, False},
    }

    fn_path = str(tmpdir.join('data.pickle'))
    with open(fn_path, 'wb') as fp:
        pickle.dump(obj, fp)

    with open(fn_path, 'rb') as fp:
        obj_from_pickle_file = pickle.load(fp)

    assert obj == obj_from_pickle_file


class SomeValueObject:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __eq__(self, other):
        return (
            self.field1 == other.field1 and
            self.field2 == other.field2)

def test_dump_value_object_list_to_file_and_load_it__equivalent(tmpdir):
    vo_list = [
        SomeValueObject(1, 2),
        SomeValueObject(3, 4),
        SomeValueObject(5, 6),
    ]

    fn_path = str(tmpdir.join('data.pickle'))
    with open(fn_path, 'wb') as fp:
        pickle.dump(vo_list, fp)

    with open(fn_path, 'rb') as fp:
        vo_list_from_pickle_file = pickle.load(fp)

    assert vo_list == vo_list_from_pickle_file

def test_protocal_version_constant():
    assert pickle.DEFAULT_PROTOCOL == 3
    assert pickle.HIGHEST_PROTOCOL == 4 # more efficiency




# vi:et:ts=4:sw=4:cc=80
