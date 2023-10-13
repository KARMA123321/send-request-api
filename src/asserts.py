class Assert:
    @staticmethod
    def multiple(*asserts):
        exceptions = []
        for _assert in asserts:
            try:
                _assert()
            except AssertionError as ex:
                exceptions.append(f"{len(exceptions) + 1}. {str(ex)}")
        if len(exceptions) != 0:
            ex_str = ""
            for ex in exceptions:
                ex_str += f"\n{ex}"
            raise AssertionError(ex_str)
