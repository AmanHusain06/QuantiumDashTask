from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("#app-header")
    assert header is not None
    assert "Soul Foods Pink Morsel Sales Dashboard" in header.text


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    picker = dash_duo.find_element("#region-picker")
    assert picker is not None