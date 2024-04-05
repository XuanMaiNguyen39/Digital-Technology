## Imports necessary libraries and components for building the Dash app.
import dash_mantine_components as dmc
from dash import Dash, html, dcc
from dash_iconify import DashIconify

## Three cards (card1, card2, and card3) are defined, each representing a project. 
## Each card contains an image, title, description, and a link to the project and its GitHub/Linkedin repository.
card1 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://www.freepnglogos.com/uploads/world-map-png/world-map-bootup-world-interactive-map-19.png",
                    alt="Map plot of university rankings",
                ),
                href="https://chat.openai.com/g/g-RWX3i8Zfr-american-football-oracle",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Map plot of university rankings", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/XuanMaiNguyen39',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Chart Your Course: Mapping University Rankings",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

card2 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://www.worldatlas.com/r/w1200/upload/01/ff/40/shutterstock-401433736.jpg",
                    alt="dash-app",
                ),
                href="https://investment-app.onrender.com/",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Analyse each university", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/XuanMaiNguyen39',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "A comprehensive analysis of each university in the TOP 50.",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

card3 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://www.detroitchamber.com/wp-content/uploads/2022/08/iStock-947295034-1.jpg",
                    alt="dash-app",
                ),
                href="https://charming-data.com/",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Education attainment", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="skill-icons:linkedin", width=30),
                    href='https://www.linkedin.com/in/mai-nguyen-922347245/',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Education attainment of each TOP 50 country",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

## Page/Tab 1. all_cards is a list containing the project cards. 
## It also includes a header indicating the section title.
all_cards = [
    dmc.Header(
        height=80,
        children=[dmc.Text("Digital Technology Dashboard",
                           style={"fontSize": 40})],
    ),
    dmc.SimpleGrid(
        cols=3,
        spacing="lg",
        breakpoints=[
            {"maxWidth": 1240, "cols": 2, "spacing": "md"},
            {"maxWidth": 950, "cols": 1, "spacing": "sm"},
        ],
        children=[
            html.Div(card1),
            html.Div(card2),
            html.Div(card3),
        ],
    )
]

## Page/Tab 2. resume_div is a division containing an iframe displaying a Google Drive link, presumably for the developer's resume.
resume_div = html.Div([
    html.Iframe(src="https://docs.google.com/document/d/e/2PACX-1vQSFVjNtA_AahmemLCYKA-rVBBBRzXzUkFdAyUxGWXKX8w9J2ZD3ZgwEM9Rwa5XqWEH3Np9FztGY4b5/pub",
                width="800", height="480")
    ],
    style={"paddingTop": 40}
)

## Page/Tab 3. reference_card is a card containing information about a person (possibly the developer) with a placeholder for details like name, role, and description.
reference_card = html.Div([
    dmc.Card(
        children=[
            dmc.Text("Mai Nguyen", weight=500, size='xl'),
            dmc.Text(
                "Student Developer",
                size="md",
                mb="xs",
            ),
            dmc.Text(
                "Courage isn't having the strength to go on, it is going on when you don't have the strength.- Napoleon Bonaparte",
                size="sm",
                color="dimmed",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": 350})
    ],
    style={"paddingTop": 40}
)

## The layout of the Dash app is defined. 
## It includes tabs for Projects, Resume, and References. 
## Each tab panel contains different content (project cards, resume division, and reference card).
app = Dash()
server = app.server
app.layout = dmc.MantineProvider(
    theme={"colorScheme": "dark"},
    withGlobalStyles=True,
    children=[
            dmc.Tabs(
        [
            dmc.TabsList(
                [
                    dmc.Tab("Projects", value="projects"),
                    dmc.Tab("Resumé", value="resume"),
                    dmc.Tab("References", value="references"),
                ], style={"paddingRight": 50, "paddingTop": 15}
            ),
            dmc.TabsPanel(children=all_cards, value="projects", pb="xs"),
            dmc.TabsPanel(resume_div, value="resume", pb="xs"),
            dmc.TabsPanel(reference_card, value="references", pb="xs"),
        ],
        value="projects",
        orientation='vertical',
        variant='pills',
    )
])


if __name__=='__main__':
    app.run(debug=False)
