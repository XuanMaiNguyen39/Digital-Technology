open output on development server:
http://127.0.0.1:8055/

==PYTHON CODE==
app.layout = dbc.Container([
    
    html.Div(style={
        'width': 340,
        'margin-left': 35,
        'margin-top': 35,
        'margin-bottom': 35
    }),

    html.Div(
        style={
            'width': 990,
            'margin-top': 35,
            'margin-right': 35,
            'margin-bottom': 35
        }),
        
html.Div([
        html.H1([
            html.Span("Welcome"),
            html.Br(),
            html.Span("to my beautiful dashboard!")
        ]),
        html.P("This dashboard prototype shows how to create an effective layout.")
    ],
        style={
            "vertical-alignment": "top",
            # "horizontal-alignment": "left",
            "height": 260,
        }),
    
    html.Div([html.Div(style={'width': 206}),
          html.Div(style={'width': 104})],
         style={
             'margin-left': 15,
             'margin-right': 15,
             'display': 'flex'
         }),
    
    html.Div([
        html.Div(dbc.RadioItems(
            className='btn-group',
            inputClassName='btn-check',
            labelClassName="btn btn-outline-light",
            labelCheckedClassName="btn btn-light",
            options=[
                {"label": "Graph", "value": 1}, 
                {"label": "Table", "value": 2}
            ],
            value=1
        ),
                 style={'width': 206}),
        html.Div(dbc.Button(
            "About",
            className="btn btn-info",
            n_clicks=0
        ), 
                 style={'width': 104})
    ],
    style={
        'margin-left': 15,
        'margin-right': 15,
        'display': 'flex'
    }),
    
    html.Div([
    html.Div([
        html.H2('Unclearable Dropdown:'),
        dcc.Dropdown(
            options=[
                {'label': 'Option A', 'value': 1}, 
                {'label': 'Option B', 'value': 2}, 
                {'label': 'Option C', 'value': 3}
            ],
            value=1,
            clearable=False,
            optionHeight=40
        )
    ]),
    html.Div([
        html.H2('Unclearable Dropdown:'),
        dcc.Dropdown(
            options=[
                {'label': 'Option A', 'value': 1}, 
                {'label': 'Option B', 'value': 2}, 
                {'label': 'Option C', 'value': 3}
            ],
            value=2,
            clearable=False,
            optionHeight=40
        )
    ]),
    html.Div([
        html.H2('Clearable Dropdown:'),
        dcc.Dropdown(
            options=[
                {'label': 'Option A', 'value': 1}, 
                {'label': 'Option B', 'value': 2}, 
                {'label': 'Option C', 'value': 3}
            ],
            clearable=True,
            optionHeight=40
        )
    ])
],
    style={
        'margin-left': 15,
        'margin-right': 15,
        'margin-top': 30
    }), 

    html.Div(
    html.Img(src='assets/image.svg',
             style={
                 'margin-left': 15,
                 'margin-right': 15,
                 'margin-top': 30,
                 'width': 310
             })),
    html.Div(dcc.Graph(figure=fig), style={'width': 790}),
    
    html.Div([
    html.H2('Output 1:'),
    html.Div(className='Output'),
    html.H2('Output 2:'),
    html.Div(html.H3("Selected Value"), className='Output'),
],
    style={'width': 200})
    ],

    ==CSS code== 
/* Radio-buttons */

.form-check {
    width: 100%;
    height: 38px;
    margin: 1px;
    padding-left: 0;
}

.btn.btn-outline-light,
.btn.btn-light {
    width: 100%;
    height: 100%;
    padding: 6px;
    font-family: "Arial";
    border-radius: 3px;
    color: #ebebf4;
}

.btn.btn-outline-light {
    border: 1px solid transparent;
}

.btn.btn-outline-light:hover {
    color: #ebebf4;
    background-color: color-mix(in srgb, var(--bs-light), #e4e4f1 7%);
}

/* Single button */

.btn.btn-info {
    width: 100%;
    height: 38px;
    margin: 1px;
    padding: 6px;
    font-family: "Arial";
    border-radius: 3px;
    background-color: lightskyblue;
    border: 1px darkblue;
}

.btn.btn-info:active,
.btn.btn-info:focus {
    background-color: var(--bs-info);
}

.btn.btn-info:hover {
    background-color: color-mix(in srgb, var(--bs-info), #010103 7%);
}

/* Radio-buttons and buttons container
.flex-container {
    display: flex;
    justify-content: right; /* Align items to the left */
    /* margin-left: 15px; /* Adjust margin as needed */
    /* margin-right: 15px; */

h2 {
        margin-bottom: 0px;
        margin-top: 10px;
        font-family: "Poppins";
        font-size: 14px !important;
        color: #ffffff;
    }

/* Dropdowns */


.customDropdown {
    font-size: 16px;
    font-family: "Poppins";
    padding-left: 1px;
}

.customDropdown .Select-control {
    width: 100%;
    height: 38px;
    background-color: transparent;
    border: 1px solid #676768;
    border-radius: 3px;
    color: var(--bs-info) !important;
}

.customDropdown .Select-value-label,
.customDropdown .Select-placeholder {    
    color: var(--bs-info) !important;
}

.customDropdown .Select-arrow {
    border-color: #cccccc transparent transparent;
}

.customDropdown.is-open .Select-arrow {
    border-color: transparent transparent #cccccc;
}

.customDropdown .Select-clear {
    color: var(--bs-info);
    font-size: 22px;
}

.customDropdown.is-focused:not(.is-open) > .Select-control {
    border: 2px solid color-mix(in srgb, var(--bs-info), #010103 50%) !important;
}

.customDropdown.is-focused:not(.is-open) .Select-arrow {
    border-color: var(--bs-info) transparent transparent;
}

.customDropdown .Select-menu-outer {
    margin-top: 5px;
    border-radius: 3px;
    background-color: #010103;
    border: 1px solid #676768;
    color: var(--bs-light);
}

.customDropdown .VirtualizedSelectFocusedOption {
    background-color: color-mix(in srgb, var(--bs-light), #010103 7%);
    border-radius: 3px;
    color: #010103;
}

.modebar { display: none !important; }

.Output {
    width: 150px;
    height: 38px;
    background-color: rgba(204,204,204,0.1);
    border: 1px solid rgba(204,204,204,0.1);
    border-radius: 3px;
}

.Output:empty::before {
  content:"";
  display:inline-block;
}

h3 {
    font-size: 16px;
    line-height: 34px;
    padding-left: 7px;
    font-family: "Poppins";
    color: var(--bs-info);
}
