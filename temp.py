menu_data = [
        {'icon': "fas fa-tachometer-alt", 'label':"Dashboard", 'ttip':"Interactive Dashboard"},
        {'icon': "far fa-copy", 'label':"Profile", 'ttip':"Let's Get Some Quiz"},
        {'icon': "fas fa-chalkboard-teacher", 'label':"Let's Learn", 'ttip':"Movie Recommendation and Prediction"},
        {'icon': "bi bi-hand-thumbs-up", 'label':"Summary", 'ttip':"Summary and Recommendation"},
        {'icon': "far fa-address-book", 'label':"Contact", 'ttip':"Contact Me"},
]

over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#87CEFA','txc_active':'black','option_active':'white'}
menu_id = hc.nav_bar(menu_definition=menu_data, home_name='Home', override_theme=over_theme)