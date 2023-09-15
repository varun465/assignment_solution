from basic import convert_camelcase_to_snake_case

def test_convert_camelcase_to_snake_case():
    assert convert_camelcase_to_snake_case("someVariable") == "some_variable"

