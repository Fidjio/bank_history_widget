from src.processing import filter_by_state


def test_filter_by_state(dict_list_state, return_dict_by_executed, return_dict_by_canceled,
                         message_error_for_filter_by_state):
    assert filter_by_state(dict_list_state, "CANCELED") == return_dict_by_canceled
    assert filter_by_state(dict_list_state, "") == message_error_for_filter_by_state
    assert filter_by_state(dict_list_state, "EXECUTED") == return_dict_by_executed
    assert filter_by_state(dict_list_state, "executed") == message_error_for_filter_by_state
    assert filter_by_state(dict_list_state, "canceled") == message_error_for_filter_by_state
    assert filter_by_state(dict_list_state, "canceled") == message_error_for_filter_by_state
