# usage example:
# pytest -s usmqe_tests/web/web_test.py
# where -s option is mandatory
#
#
# import ipdb
#
#
# def test_ipdb(valid_credentials):
#     ipdb.set_trace()
#
#
# def test_it():
#     assert 0


from IPython import embed


def test_embed(valid_credentials, api_valid_credentials):
    embed()
