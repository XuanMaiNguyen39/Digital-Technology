import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
import plotly.express as px
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# Load data and prepare figures
def prepare_data():
    # Arts and Humanities Ranking Data
    df_arts = pd.read_csv('data.csv', header=0, usecols=["University Name", "Arts and humanities ranking THE2024"])
    df_arts_melted = df_arts.melt(id_vars=["University Name"], value_vars=["Arts and humanities ranking THE2024"], var_name="Subject", value_name="Subject Field")
    y_arts = [1, 3, 4, 2, 3, 3, 5, 3]

    fig_arts = go.Figure(data=[
        go.Bar(
            x=df_arts['University Name'], 
            y=df_arts['Arts and humanities ranking THE2024'],
            hovertext=[
                '1st place nationally, Ranked 113 in the world by THE 2024', 
                '=3rd place nationally, Ranked 350.5 in the world by THE 2024', 
                '4th place nationally, Ranked 450.5 in the world by THE 2024',
                '2nd place nationally, Ranked 188 in the world by THE 2024',
                '=3rd place nationally, Ranked 350.5 in the world by THE 2024',
                '=3rd place nationally, Ranked 350.5 in the world by THE 2024',
                '5th place nationally, Ranked 550.5 in the world by THE 2024',
                '=3rd place nationally, Ranked 350.5 in the world by THE 2024'
            ],
            text=y_arts,
            textposition='auto'
        )
    ])
    fig_arts.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
    fig_arts.update_layout(
        title_text='Ranking of Arts and Humanities by THE 2024',
        xaxis_title="University Name",
        yaxis_title="THE 2024 Ranking"
    )
    fig_arts.update_layout(
        title=go.layout.Title(
            text="Ranking of Arts and Humanities by Times Higher Education 2024 🖼️<br><sup>Hover on the bar to see specific national rankings 🤓</sup>",
            xref="paper",
            x=0
        )
    )
    fig_arts.update_traces(marker_color='rgb(1,33,105)', marker_line_color='rgb(1,33,105)', marker_line_width=1.5, opacity=0.6)

    # Engineering & Technology Ranking Data
    df_tech = pd.read_csv('data.csv', header=0, usecols=["University Name", "Engineering & Technology ranking THE24"])
    y_tech = [138, 700.5, 450.5, 0, 700.5, 450.5, 0, 700.5]

    fig_tech = go.Figure(data=[
        go.Bar(
            x=df_tech['University Name'], 
            y=df_tech['Engineering & Technology ranking THE24'],
            hovertext=[
                '1st place nationally, Ranked 138 in the world by THE 2024', 
                '=3rd place nationally, Ranked 700.5 in the world by THE 2024', 
                '=2nd place nationally, Ranked 450.5 in the world by THE 2024',
                'No ranking',
                '=3rd place nationally, Ranked 700.5 in the world by THE 2024',
                '=2nd place nationally, Ranked 450.5 in the world by THE 2024',
                'No ranking',
                '=3rd place nationally, Ranked 700.5 in the world by THE 2024'
            ],
            text=y_tech,
            textposition='auto',
        )
    ])
    fig_tech.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
    fig_tech.update_layout(
        title=go.layout.Title(
            text="Ranking of Engineering & Technology by Times Higher Education 2024 🖼️<br><sup>Hover on the bar to see specific national rankings 🤓</sup>",
            xref="paper",
            x=0
        )
    )
    fig_tech.update_traces(marker_color='rgb(1,33,105)', marker_line_color='rgb(1,33,105)', marker_line_width=1.5, opacity=0.6)

    # International Rankings Line Chart
    df_int = pd.read_csv('data.csv', header=0, usecols=["University Name", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"])
    df_int_long = df_int.melt(id_vars=['University Name'], var_name='Year', value_name='Ranking')
    fig_int = px.line(df_int_long, x="Year", y="Ranking", color='University Name')
    fig_int.update_layout(
        title=go.layout.Title(
            text="International QS rankings of New Zealand Universities<br><sup>Data from QS Top Universities from 2018 to 2025. (https://www.topuniversities.com)</sup>",
            xref="paper",
            x=0
        ),
        xaxis_title='Year',
        yaxis_title='QS Ranking',
        yaxis=dict(autorange='reversed'),
        legend_title='University'
    )

    # National Rankings Line Chart
    df_nat = pd.read_csv('data.csv', header=0, usecols=["University Name", "N2018", "N2019", "N2020", "N2021", "N2022", "N2023", "N2024", "N2025"])
    df_nat_long = df_nat.melt(id_vars=['University Name'], var_name='Year', value_name='Ranking')
    fig_nat = px.line(df_nat_long, x="Year", y="Ranking", color='University Name')
    fig_nat.update_layout(
        title=go.layout.Title(
            text="National QS rankings of New Zealand Universities<br><sup>Data from QS Top Universities from 2018 to 2025. (https://www.topuniversities.com)</sup>",
            xref="paper",
            x=0
        ),
        xaxis_title='Year',
        yaxis_title='QS Ranking',
        yaxis=dict(autorange='reversed'),
        legend_title='University'
    )

    # Radar Chart
    df_radar = pd.read_csv('data.csv', header=0, usecols=[
        "University Name", 
        "Academic reputation (QS25)", 
        "Teaching quality (THE24)", 
        "Employment Outcomes (QS25)", 
        "Research quality (THE24)", 
        "International Research Network (QS25)", 
        "Employer Reputation (QS25)"
    ])
    df_radar = pd.DataFrame(dict(
        r=[82.2, 39.7, 92.9, 88.3, 87.4, 44.7],
        theta=['Academic reputation (QS25)', 'Teaching quality (THE24)', 'Employment Outcomes (QS25)', 'Research quality (THE24)', 'International Research Network (QS25)', 'Employer Reputation (QS25)']
    ))
    fig_radar = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
    fig_radar.update_traces(fill='toself')

    return fig_arts, fig_tech, fig_int, fig_nat, fig_radar

# Prepare figures
fig_arts, fig_tech, fig_int, fig_nat, fig_radar = prepare_data()

# Summary text and markdowns
summary_text = """
### University of Auckland

The University of Auckland, located in New Zealand, is the country's largest and highest-ranked university, known for its strong emphasis on research and academic excellence.

**Academic and Facilities Offers:**

- **Faculties and Programs**:
  - **Faculty of Arts**
  - **Business School**
  - **Faculty of Creative Arts and Industries**
  - **Faculty of Education and Social Work**
  - **Faculty of Engineering**
  - **Faculty of Law**
  - **Faculty of Medical and Health Sciences**
  - **Faculty of Science**
  - **Interdisciplinary programs** across various faculties
  
- **Research Excellence**:
  - Ranked 65th in the world by the QS World University Rankings 2025, making it the highest-ranked university in New Zealand.
  - Ten subjects ranked in the top 50 worldwide in the 2024 QS Subject Rankings, including Psychology, Linguistics, and Anatomy and Physiology.

- **Campus Facilities**:
  - **Libraries and Learning Services**: Extensive resources and support for students.
  - **Sport and Recreation**: Modern facilities including gyms, sports fields, and fitness classes.
  - **Accommodation**: Options for self-catered and catered living arrangements.
  - **Kate Edger Information Commons**: A hub for student services and study spaces.
  - **Food and Retail**: Diverse dining options and retail services on campus.

- **Student Support Services**:
  - **Clubs and Societies**: Over 200 clubs ranging from cultural to professional interests.
  - **Māori and Pacific Support**: Dedicated services to support Māori and Pacific students.
  - **Career Development**: Services including career counseling, internships, and job placement assistance.

- **International Opportunities**:
  - **360 International**: Programs for studying abroad and international exchanges.

The University of Auckland combines a robust academic framework with state-of-the-art facilities, offering students a comprehensive and enriching educational experience.
"""

text_rankings = """
### International rankings

NZ universities are ranked internationally with high rankings. The most highly ranked universities are the University of Auckland and the University of Otago. 
"""

text_arts = """
University of Auckland and University of Otago tops the chart for Arts and Humanities subjects. 
These subjects include Archaeology, Languages, Literature & Linguistics, History, Philosophy & Theology, Art, Performing Arts & Design, Architecture and more...
"""

# Create the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='NZ University Dashboard')
server = app.server

# Page layouts
all_cards = [
    dmc.Title(
        order=1,
        children=[dmc.Text("About the University of Auckland", style={"fontSize": 40})],
    ),
    html.Div(
        style={'display': 'flex', 'justifyContent': 'space-between'},
        children=[
            html.Div(
                style={'flex': '1', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px', 'backgroundColor': '#f9f9f9'},
                children=[dcc.Markdown(summary_text)]
            ),
            dcc.Graph(id='example-graph', figure=fig_radar, style={'flex': '1', 'padding': '10px'}),
        ]
    )
]

resume_div = html.Div([
    dmc.Title(
        order=1,
        children=[dmc.Text("NZ University Rankings Internationally", style={"fontSize": 40})],
    ),
    html.Div(
        style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'stretch'},
        children=[
            html.Div(
                style={'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px', 'backgroundColor': '#f9f9f9', 'marginBottom': '20px'},
                children=[dcc.Markdown(text_rankings)]
            ),
            dcc.Graph(figure=fig_int),
            dmc.Title(
                order=1,
                children=[dmc.Text("NZ University Rankings Nationally", style={"fontSize": 40})],
            ),
            dcc.Graph(figure=fig_nat),
        ]
    )
])

reference_card = html.Div([
    dmc.Title(
        order=1,
        children=[dmc.Text("Art & Humanities Rankings", style={"fontSize": 40})]),
    html.Div(
        style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'stretch'},
        children=[
            html.Div(
                style={'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px', 'backgroundColor': '#f9f9f9', 'marginBottom': '20px'},
                children=[dcc.Markdown(text_arts)]
            ),
            dcc.Graph(figure=fig_arts),
            dmc.Title(
                order=1,
                children=[dmc.Text("Engineering & Technology Rankings", style={"fontSize": 40})]),
            dcc.Graph(figure=fig_tech),
        ]
    )
])

# App layout
app.layout = dmc.MantineProvider(
    theme={
        "colors": {
            "deepBlue": ["#E9EDFC", "#C1CCF6", "#99ABF0", "#797EF8", "#5C64E9", "#4549DA", "#3235C5", "#26289E", "#1C1E77", "#12134E"]
        },
        "shadows": {
            "md": "1px 1px 3px rgba(0,0,0,.25)",
            "xl": "5px 5px 3px rgba(0,0,0,.25)",
        },
        "headings": {
            "fontFamily": "Futura",
            "sizes": {
                "h1": {"fontSize": 30},
            },
        },
    },
    withGlobalStyles=True,
    children=[
        dmc.Tabs(
            [
                dmc.TabsList(
                    [
                        dmc.Tab("University metrics", value="metrics"),
                        dmc.Tab("Rankings through the years", value="years"),
                        dmc.Tab("Subject Rankings", value="subject"),
                    ], style={"paddingRight": 50, "paddingTop": 15}
                ),
                dmc.TabsPanel(children=all_cards, value="metrics", pb="xs"),
                dmc.TabsPanel(resume_div, value="years", pb="xs"),
                dmc.TabsPanel(reference_card, value="subject", pb="xs"),
            ],
            value="metrics",
            orientation='horizontal',
            variant='pills',
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)


