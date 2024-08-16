import pandas as pd
import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
from vizro.tables import dash_ag_grid
from vizro.actions import export_data, filter_interaction
import plotly.graph_objects as go
from vizro.models.types import capture

Vizro._reset()

## 😀 0. Page 0

def create_intro():
    """Introduction Page""" 
    
    page_intro = vm.Page(
        title="Intro",
        layout=vm.Layout(grid=[[0, 0, 1]]),
        components=[
            vm.Card(
                text="""
 ![](assets/logo.<extension>.png#icon)

# **🇳🇿Welcome to Your Ultimate Guide to New Zealand Universities!🇳🇿**
---

### **Hey there school leavers - the future university students! 🌟 Are you nervous about choosing the right university for you? Are you worried you’ll miss out on amazing opportunities right here in New Zealand? Well, worry no more! We present you, the ultimate dashboard showing detailed information on New Zealand universities. **

## What’s This All About?


We know that picking a university can be overwhelming, especially when it feels like overseas options might be better. However, it might be because you did not get informed enough on the various options domestically. But guess what? New Zealand universities have SO much to offer, and our fun, interactive dashboard is here to show you exactly that! The offers of our universities will be compared with international standards so worry not about the quality of the education you are about to receive. 

## Why Should You Care?

Our mission is to help you discover all the scores and rankings of universities across New Zealand, to show you the actual position of our universities compared to the world. You can also see which university excels at which aspect, helping you to make informed decisions for yourself. We want you to feel confident and excited about studying close to home, knowing that you’re getting top-notch education and awesome experiences.

## How Does It Work?

Our dashboard is packed with awesome features to help you find your perfect university match! Here’s what you can explore:

- **Uni Scores on the Global Stage** 🌍: Curious about how our universities stack up internationally? Check out individual scores on key metrics from QS, covering academic reputation, research quality, and job prospects. You'll see how each university excels in different areas!

- **Rankings Over the Years** 📈: Ever wondered which New Zealand universities are climbing the global ranks? Track their performance over the years with data from THE (Times Higher Education) and QS rankings. See who’s leading the chart nationally and internationally, and discover the rising stars!

- **Top Subject Fields** 🏆: Want to know which university is best for your dream major? Whether it’s engineering, technology, or any other field, our dashboard shows you the top-ranked universities in specific subjects. Find out where you’ll get the best education for your chosen career path!

## The Big Picture

By using this tool, you'll not only find the perfect university for you, but you'll also be supporting local education, helping our universities grow, and keeping New Zealand's academic community vibrant and thriving.

So dive in, explore, and find your future right here at home! 🌏✨


                """,
            ),
             vm.Card(
                text="""
                ![](assets/images/unilogo1.png#my-image)
            """,
            ),
            
        ],
    )
    return page_intro


## ⚽️ 1. Page 1

gapminder = pd.read_csv('uni.csv', header=0, usecols=[
    "University Name", 
    "Academic reputation (QS25)", 
    "Teaching quality (THE24)", 
    "Employment Outcomes (QS25)", 
    "Research quality (THE24)", 
    "International Research Network (QS25)", 
    "Employer Reputation (QS25)"
])

gapminder_1 = pd.DataFrame(dict(
    r=[82.2, 39.7, 92.9, 88.3, 87.4, 44.7, 82.2],
    r_otago=[45, 35.6, 59.1, 75.8, 79.5, 24.6, 45],
    r_massey=[30.1, 28.7, 49.2, 60.5, 85.1, 14, 30.1],
    r_victoria=[42.8, 28.6, 71.6, 69.4, 70.7, 21.4, 42.8],
    r_waikato=[19.1, 26.1, 46.4, 74.3, 55.1, 11.7, 19.1],
    r_canterbury=[34.7, 28.6, 82.3, 62.4, 63, 27.3, 34.7],
    r_lincoln=[8.2, 33.9, 40, 68.4, 20.2, 5, 8.2],
    r_aut=[19.3, 23.8, 12.4, 84, 52.6, 11.2, 19.3],
    theta=['Academic reputation', 'Teaching quality', 'Employment Outcomes', 'Research quality', 'International Research Network', 'Employer Reputation', 'Academic reputation']
))

@capture("graph")
def radarchart(data_frame, r, theta, title=None, markers=None, hover_name=None, line_close=None, template=None): 
    fig_radar = px.line_polar(data_frame=data_frame, r=r, theta=theta, title=title, markers=markers, hover_name=hover_name, line_close=line_close, template=template)
    
    fig_radar.update_layout(
        legend=dict(
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        ),
        annotations=[
            dict(
                xref='paper', 
                yref='paper',
                x=0.5, 
                y=-0.1,  # Position below the chart
                showarrow=False,
                text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
                font=dict(
                    family="Georgia, serif",
                    size=12,
                ),
            )
        ]
    ) 
    
    fig_radar.update_traces(fill='toself')

    fig_radar.update_layout(
        font_family="Georgia, serif",
        title_font_family="Georgia, serif",
    )
    return fig_radar
    
@capture("graph")
def totalradarchart(data_frame): 
    fig_total = go.Figure()
    
    fig_total.add_trace(go.Scatterpolar(
        r=gapminder_1['r'],
        theta=gapminder_1['theta'],
        fill='toself',
        name='University of Auckland'
    ))

    fig_total.add_trace(go.Scatterpolar(
        r=gapminder_1['r_otago'],
        theta=gapminder_1['theta'],
        fill='toself',
        name='University of Otago'
    ))

    fig_total.add_trace(go.Scatterpolar(
        r=gapminder_1['r_massey'],
        theta=gapminder_1['theta'],
        fill='toself',
        name='Massey University'
    ))

    fig_total.add_trace(go.Scatterpolar(
        r=gapminder_1['r_victoria'],
        theta=gapminder_1['theta'],
        fill='toself',
        name='Victoria University of Wellington'
    ))

    fig_total.add_trace(go.Scatterpolar(
        r=gapminder_1['r_waikato'],
        theta=gapminder_1['theta'],
        fill='toself',
        name='Waikato University'
    ))

    fig_total.add_trace(go.Scatterpolar(
        r=gapminder_1['r_canterbury'],
        theta=gapminder_1['theta'],
        fill='toself',
        name='University of Canterbury'
    ))

    fig_total.add_trace(go.Scatterpolar(
        r=gapminder_1['r_lincoln'],
        theta=gapminder_1['theta'],
        fill='toself',
        name='Lincoln University'
    ))

    fig_total.add_trace(go.Scatterpolar(
        r=gapminder_1['r_aut'],
        theta=gapminder_1['theta'],
        fill='toself',
        name='AUT'
    ))

    # fig_total.update_layout(legend=dict(
    #     yanchor="top",
    #     y=0.99,
    #     xanchor="right",
    #     x=0.02
    # ))

    fig_total.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="right",
        x=1
    ))

    fig_total.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
            )
        ),
        showlegend=True
    )
    
    fig_total.update_layout(
        legend=dict(
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        ),
        annotations=[
            dict(
                xref='paper', 
                yref='paper',
                x=0.5, 
                y=-0.1,  # Position below the chart
                showarrow=False,
                text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
                font=dict(
                    family="Georgia, serif",
                    size=12,
                ),
            )
        ]
    ) 
    
    fig_total.update_traces(fill='toself')

    fig_total.update_layout(
        font_family="Georgia, serif",
        title_font_family="Georgia, serif",
    )
    
    return fig_total


def create_metrics():
    """Function returns a page to show scores of different metrics on each university."""
    page_years = vm.Page(
        title="Universities' Scores in metrics",
        description="Discovering how different NZ universities are scored with different metrics",
        layout=vm.Layout(grid=[[0],]),
        components=[
            vm.Tabs(
                tabs=[
                    vm.Container(
                        title="All",
                        layout=vm.Layout(grid=[[1,1],
                                               [0,0],
                                               [0,0],
                                               [0,0],
                                               [0,0],
                                               [0,0],
                                               [2,2]]),
                        components=[
                            vm.Graph(
                                id="radar_chart",
                                figure=totalradarchart(
                                    gapminder_1,
                                    
                                ),
                            ),
                            vm.Card(
                                text="""
                                Check out the metrics scores of ALL universities. 
                                For details in individual universities, click the tabs above. 

                                """,
                            ),
                             vm.Card(
                                text="""
                                Data source: 
                                
                                Top Universities. (n.d.). The University of Auckland. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-auckland

                                Top Universities. (n.d.). University of Otago. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-otago

                                Top Universities. (n.d.). Massey University. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/massey-university

                                Top Universities. (n.d.). Victoria University of Wellington. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/victoria-university-wellington

                                Top Universities. (n.d.). University of Waikato. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-waikato

                                Top Universities. (n.d.). Lincoln University. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/lincoln-university

                                Top Universities. (n.d.). University of Canterbury: Te Whare Wānanga o Waitaha. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-canterbury-te-whare-wananga-o-waitaha
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Auckland",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="uoa",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r",
                                    theta="theta",
                                    title="University of Auckland",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True, 
                                    template="seaborn",
                                ),
                            ),
                            vm.Card(
                                text="""
                                ![](assets/images/uoa2.png#my-image2)
                                
                                *Top Universities. (n.d.). The University of Auckland. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-auckland*


                                The University of Auckland is New Zealand’s leading university, located in the country’s largest city. 
                                
                                It offers a comprehensive range of programs and is known for its strong emphasis on research and innovation. 

                                 > ## WHAT DOES THIS MEAN? 

                                > - **Academic Reputation (82.2)**: The University of Auckland is known around the world for its high academic standards. You'll be able to learn from some of the greatest minds in the world.

                                > - **Employment Outcomes (92.9)**: you will have good job chances and exciting career options right after you graduate.

                                > - **Research Quality (88.3)**: At UOA, you can dive into cutting-edge research, where new projects and findings happen every day. You'll be a part of a university that challenges what people think they know.

                                > - **International Research Network (87.4)**: Work with the best experts in the world. Because UOA has strong international ties, you'll get a global view and useful training.  
                                
                                If you choose the University of Auckland, you'll be choosing a university that is highly regarded, has great job prospects, and does great study. 
                                You'll accomplish well in school and at work there, and you'll still be close to the exciting city life of Auckland. 🌟📚🌍

                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Otago",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="otago",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_otago",
                                    theta="theta",
                                    title="University of Otago",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="ggplot2"
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/otago.png#my-image3)
                                
                                *Top Universities. (n.d.). University of Otago. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-otago*

                                
                                The University of Otago is New Zealand’s oldest university, located in the scenic city of Dunedin. 
                                
                                It offers a rich variety of programs and is renowned for its vibrant campus life and strong research focus.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Employment Outcomes (59.1)**: Otago graduates are highly sought after by employers, leading to strong job prospects and successful career paths right after graduation.
                                
                                > - **Research Quality (75.8)**: Engage in high-impact research at Otago, where students and faculty work on innovative projects that drive forward scientific and academic knowledge.
                                
                                > - **International Research Network (79.5)**: Otago boasts strong international collaborations, giving students the opportunity to participate in global research initiatives and broaden their academic horizons.
                                
                                Choosing the University of Otago means joining a university that values academic excellence, offers significant research opportunities, and fosters a supportive and dynamic student community. It's a place where you'll not only grow academically but also enjoy a vibrant and fulfilling university experience in a beautiful setting. 🌟📚🌏
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Massey",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="massey",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_massey",
                                    theta="theta",
                                    title="Massey University",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="simple_white"
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/massey.png#my-image4)
                                *Top Universities. (n.d.). Massey University. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/massey-university*
                                
                                ### Massey University
                                Massey University is renowned for its innovative teaching methods and extensive research programs, with campuses in Palmerston North, Albany, and Wellington.
                                
                                It offers a wide range of programs and emphasizes practical, hands-on learning experiences.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **International Research Network (85.1)**: Massey has an extensive international research network, allowing students to collaborate on global projects and gain international experience.
                                
                                > - **Research Quality (60.5)**: Engage in high-quality research at Massey, where innovative projects and discoveries are highly encouraged.
                                
                                > - **Employment Outcomes (49.2)**: Massey graduates are well-prepared for the workforce, with solid job prospects after graduation.
                                
                                Choosing Massey University means embracing innovation and benefiting from a global perspective, with numerous opportunities for international collaboration. 🌟🌐📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Victoria @ Wellington",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="victoria",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_victoria",
                                    theta="theta",
                                    title="Victoria University of Wellington",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="plotly"
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/victoria.png#my-image5)
                                
                                 *Top Universities. (n.d.). Victoria University of Wellington. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/victoria-university-wellington*
                                
                                ### Victoria University of Wellington
                                Victoria University of Wellington is celebrated for its strong emphasis on research and academic excellence. Located in New Zealand's capital, it offers unique opportunities for engagement with government and industry.
                                
                                It offers a diverse range of programs and is known for its vibrant campus life and strong community engagement.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Employment Outcomes (71.6)**: Graduates from Victoria have strong employment prospects, with many finding successful careers shortly after graduation.
                                
                                > - **Research Quality (69.4)**: Victoria excels in research, providing students with opportunities to participate in cutting-edge projects.
                                
                                > - **International Research Network (70.7)**: Victoria's strong international connections mean students can participate in global research initiatives and gain a global perspective.
                                
                                Choosing Victoria University of Wellington means gaining access to excellent academic programs and strong career opportunities in the heart of New Zealand's capital. 🌟🏙️📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Waikato",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="waikato",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_waikato",
                                    theta="theta",
                                    title="University of Waikato",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="presentation",
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/waikato.png#my-image6)
                                
                                 *Top Universities. (n.d.). University of Waikato. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-waikato*
                                
                                ### University of Waikato
                                The University of Waikato, located in Hamilton, is known for its innovative approach to education and strong ties to the community.
                                
                                It offers a diverse range of programs and emphasizes research excellence and practical learning.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Research Quality (74.3)**: Waikato excels in research, providing students with opportunities to participate in cutting-edge projects and innovations.
                                
                                > - **International Research Network (55.1)**: The university's global connections mean you'll have access to a diverse range of research opportunities and collaborations.
                                
                                Choosing the University of Waikato means joining a university that values research and practical experience. It's a place where you can engage in high-quality research while being part of a supportive and innovative community. 🌟🔬📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Canterbury",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="canterbury",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_canterbury",
                                    theta="theta",
                                    title="University of Canterbury",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="plotly_dark",
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/canterbury.png#my-image7)
                                
                                *Top Universities. (n.d.). University of Canterbury: Te Whare Wānanga o Waitaha. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-canterbury-te-whare-wananga-o-waitaha*
                               
                               ### University of Canterbury
                                The University of Canterbury, located in Christchurch, is renowned for its strong engineering and science programs.
                                
                                It offers a wide range of academic programs and is committed to providing a high-quality education through research and practical learning.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Employment Outcomes (82.3)**: Canterbury graduates are highly sought after by employers, ensuring strong job prospects and exciting career opportunities.
                                
                                > - **International Research Network (63)**: The university's international collaborations provide students with opportunities to engage in global research projects.
                                
                                Choosing the University of Canterbury means being part of a respected institution with excellent job prospects and strong international research connections. It's a place where you can thrive academically and professionally. 🌟🔧📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Lincoln",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="lincoln",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_lincoln",
                                    theta="theta",
                                    title="Lincoln University",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="plotly_white",
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/lincoln.png#my-image8)
                                
                                *Top Universities. (n.d.). Lincoln University. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/lincoln-university*


                                
                                ### Lincoln University
                                Lincoln University, located near Christchurch, is a specialist land-based university with a strong focus on agriculture and environmental science.
                                
                                It offers unique programs tailored to these fields and emphasizes research and practical learning.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Research Quality (68.4)**: Lincoln excels in research, particularly in areas related to agriculture and environmental science, providing students with opportunities to contribute to significant discoveries.
                                
                                Choosing Lincoln University means gaining expertise in specialized fields with strong research support. It's a place where you can engage in high-quality research while being close to nature. 🌟🌱📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="AUT",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="aut",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_aut",
                                    theta="theta",
                                    title="AUT",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="vizro_light",
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/aut.png#my-image9)

                                *Top Universities. (n.d.). Auckland University of Technology (AUT). Retrieved August 16, 2024, from https://www.topuniversities.com/universities/auckland-university-technology-aut*
                                
                                ### Auckland University of Technology (AUT)
                                Auckland University of Technology (AUT), located in Auckland, is known for its innovative teaching methods and strong industry connections.
                                
                                It offers a dynamic learning environment with a focus on practical skills and real-world experience.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Research Quality (84)**: AUT's commitment to research excellence provides students with opportunities to engage in high-impact projects and innovations.
                                
                                > - **International Research Network (52.6)**: AUT's strong international connections mean you'll have access to a global perspective and valuable experience.
                                
                                Choosing AUT means embracing innovation and benefiting from strong industry ties. It's a place where you can receive a forward-thinking education and gain practical skills for your future career. 🌟💡📚
                                """,
                            ),
                        ],
                    ),
                ],
            )
        ]
    )
    return page_years

## 📊 2. Page 2

# Load the data
gapminder = pd.read_csv('uni.csv')

# Select only the specified columns
columns_to_keep = ["University Name", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
gapminder = gapminder[columns_to_keep]

# Melt the year columns into a single column
gapminder_line = gapminder.melt(id_vars=["University Name"], 
                                var_name="Year", 
                                value_name="International Rankings")

# Calculate the national rankings for each year
gapminder_line["National Rankings"] = gapminder_line.groupby("Year")["International Rankings"].rank(ascending=True).astype(int)


@capture("graph")
def linechart(data_frame, x, y, color=None, title=None,labels=None, markers=None, hover_name=None, template=None): 
    fig = px.line(data_frame=data_frame, x=x, y=y, color=color, title=title, labels=labels, markers=markers, hover_name=hover_name, template=template)
    
    fig.update_layout(
        title=go.layout.Title(
            text="New Zealand Uni rankings",
            font=dict(
                family="Georgia, serif, bold",
                size=25,

            ),
            xref="paper",
            x=0
            ),
    
            legend=dict(
                font=dict(
                    family="Georgia, serif",
                    size=12,
                    # color="black"
        )
    ),
  
    annotations=[
        dict(
            xref='paper', 
            yref='paper',
            x=0, 
            y=-0.175,
            showarrow=False,
            text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        )
    ],
        
        yaxis=dict(autorange='reversed'))
    
    return fig
    
def create_rankings_years():
    """Function returns a page to perform analysis on university level."""
  
    columnsDefs = [
        {"field": "Year"},
        {"field": "University Name"},
        {"field": "International Rankings"},
        {"field": "National Rankings"},
    ]
   
    # Benchmark analysis
    page_years = vm.Page(
        title="Rankings through the years",
        description="Discovering how different NZ universities are ranked through the years",
        layout=vm.Layout(grid=[[3, 1, 1]] *2 + [[0, 1, 1]] * 5 + [[2, 1, 1]] + [[4, 1, 1]]),
        components=[
            vm.AgGrid(
                title="Click on a cell in University Name column:",
                figure=dash_ag_grid(data_frame=gapminder_line, columnDefs=columnsDefs, dashGridOptions={"pagination": True}),
                actions=[vm.Action(function=filter_interaction(targets=["line_university"]))],
            ),
            vm.Graph(
                id="line_university",
                figure=linechart(
                    gapminder_line,
                    x="Year",
                    y="International Rankings",
                    color="University Name",
                    labels={"Year": "Year", "International Rankings": "International Ranking", "National Rankings": "National Ranking"},
                    markers=True,
                    hover_name="University Name",
                    template="simple_white", 
                ),
                
                 # Use the customized figure here
            ),
            # Uncomment the following lines if needed
            vm.Button(text="Export data", actions=[vm.Action(function=export_data(targets=["line_university"]))]),
            vm.Card(
                                text="""
                                Our line chart vividly illustrates the international rankings of New Zealand universities over the years. Most universities, including the University of Auckland, the University of Waikato, and Massey University, show an upward trend in their global standings, reflecting their increasing reputation and quality.

                                A higher international ranking means that New Zealand universities are offering competitive, high-quality education compared to others worldwide. These rankings are based on rigorous criteria by QS, one of the most prestigious ranking systems globally, which evaluates universities on Academic Reputation, Teaching Quality, Employment Outcomes, Research Quality, International Research Network, and Employer Reputation.

                                Seeing universities climb in these rankings indicates that they are consistently improving and maintaining high standards, making them reliable choices for students. On the other hand, some universities have seen a decrease, providing a complete picture of the dynamic educational landscape.
                                """,
                            ),
            vm.Card(
                                text="""
                                Data source: 
                                
                                Top Universities. (n.d.). The University of Auckland. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-auckland

                                Top Universities. (n.d.). University of Otago. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-otago

                                Top Universities. (n.d.). Massey University. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/massey-university

                                Top Universities. (n.d.). Victoria University of Wellington. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/victoria-university-wellington

                                Top Universities. (n.d.). University of Waikato. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-waikato

                                Top Universities. (n.d.). Lincoln University. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/lincoln-university

                                Top Universities. (n.d.). University of Canterbury: Te Whare Wānanga o Waitaha. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-canterbury-te-whare-wananga-o-waitaha
                                
                                """,
                            ),
            
        ],
        # Uncomment the following lines if needed
        controls=[
            vm.Filter(column="University Name", selector=vm.Dropdown(value="ALL", multi=True, title="Select University")),
            # vm.Filter(column="Year", selector=vm.RangeSlider(title="Select Year", step=1, marks=None)),
            vm.Parameter(
                targets=["line_university.y"],
                selector=vm.Dropdown(
                    options=["International Rankings", "National Rankings"], multi=False, value="International Rankings", title="Choose between International and National Rankings"
                ),
            ),
            
        ],
    )
    return page_years

## 🤓 3. subject fields
gapminder1 = pd.read_csv('uni.csv',
                        header=0,
                        usecols=["University Name", "Arts and humanities ranking THE2024", "Engineering & Technology ranking THE24", "Natural science rankings QS24", "Life science/ medical rankings QS24", "Economics & Business Rankings THE24",
                               "Arts and humanities", "Engineering & Technology", "Natural science", "Life science/ medical", "Economics & Business",])

@capture("graph")
def barchart(data_frame, x, y, title=None, text=None, template=None):
    fig_bar = px.bar(data_frame=data_frame, x=x, y=y, title=title, text=text, template=template)
    
    fig_bar.update_layout(xaxis={'categoryorder':'total descending'})
        # barmode='stack', 
    
    fig_bar.update_layout(
        title=go.layout.Title(
        text="Rankings by subject field",
        font=dict(
            family="Georgia, serif",
            size=25,
        ),
        xref="paper",
        x=0
    ),
    legend=dict(
        font=dict(
            family="Georgia, serif",
            size=12,
            # color="black"
        )
    ),
    annotations=[
        dict(
            xref='paper', 
            yref='paper',
            text="Source: <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
            x=0, 
            y=-0.6,
            showarrow=False,
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        )
    ],
  
    )
    
    fig_bar.update_layout(
        font_family="Georgia, serif",
    )

    return fig_bar


def create_subject():
    """Function returns a page to perform analysis on university level."""

    page_subject = vm.Page(
        title="Uni rankings by subject",
        description="Discovering how different NZ universities are ranked through the years",
        layout=vm.Layout( grid=[[1, 1, 1, 1, 1]] + [[0, 0, 0, 0, 0]] * 4 + [[2, 2, 2, 2, 2]],
            row_min_height="100px",
            row_gap="24px",),
        components=[
            vm.Graph(
                id="barchart",
                figure=barchart(
                    gapminder1,
                    x="University Name",
                    y="Arts and humanities",
                    text="Arts and humanities ranking THE2024",
                    template="simple_white", 
                ),
            ),
            vm.Card(
            text="""
               scroll down! 
               ### National rankings of universities based on subject field
               
                #### - Subject fields to choose from: 
                
                 
                > - 🏛️ Arts and Humanities: Art, History, Philosophy, Literature, Classics, Media Studies, Film studies 
                    
                > - ⚙️ Engineering & Technology: Electronic, Computer engineering, Biomedical engineering, Computer Science, IT, Food Technology
                    
                > - 🔬 Natural Science: Physics, Chemistry, Biology 
                    
                > - 🩺 Life Science/ Medical: Pharmaceuticals, Biotechnology, Biomedical Science 
                    
                > - 🏭 Economics & Business: Economics, Marketing, Finance
                
                    
                >
                >  Choose subject field in selector on your left. 
                >
                

                
             
            """,
        ),
            vm.Card(
                                text="""
                                Data Source:
                                
                                Times Higher Education. (n.d.). University of Auckland. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-auckland

                                Times Higher Education. (n.d.). University of Otago. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-otago

                                Times Higher Education. (n.d.). Auckland University of Technology. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/auckland-university-technology
                                
                                Times Higher Education. (n.d.). Lincoln University. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/lincoln-university-1
                                
                                Times Higher Education. (n.d.). Victoria University of Wellington. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/victoria-university-wellington
                                
                                Times Higher Education. (n.d.). University of Waikato. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-waikato
                                
                                Times Higher Education. (n.d.). University of Canterbury. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-canterbury
                                
                                Times Higher Education. (n.d.). Massey University. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/massey-university
                                
                                Top Universities. (n.d.). The University of Auckland. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-auckland

                                Top Universities. (n.d.). University of Otago. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-otago

                                Top Universities. (n.d.). Massey University. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/massey-university

                                Top Universities. (n.d.). Victoria University of Wellington. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/victoria-university-wellington

                                Top Universities. (n.d.). University of Waikato. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-waikato

                                Top Universities. (n.d.). Lincoln University. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/lincoln-university

                                Top Universities. (n.d.). University of Canterbury: Te Whare Wānanga o Waitaha. Retrieved August 16, 2024, from https://www.topuniversities.com/universities/university-canterbury-te-whare-wananga-o-waitaha
        


                                
                                """,
                            ),
        ],
        controls=[
            vm.Parameter(
                targets=["barchart.y"],
                selector=vm.Dropdown(
                    options=["Arts and humanities", "Engineering & Technology", "Natural science", "Life science/ medical", "Economics & Business"], multi=False, value="Arts and humanities", title="Choose subject field"
                ),
            ),
             vm.Parameter(
                targets=["barchart.text"],
                selector=vm.Dropdown(
                    options=["Arts and humanities ranking THE2024", "Engineering & Technology ranking THE24", "Natural science rankings QS24", "Life science/ medical rankings QS24", "Economics & Business Rankings THE24"], multi=False, value="Arts and humanities ranking THE2024", title="Choose the SAME university here"
                ),
            ),
        ],
    )
    return page_subject

##  4.BACKUP BASIC DATA

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
gapminder = pd.read_csv('newdata.csv',
                        header=0,
                        usecols=["Name of University", "No of student", "No of student per staff", "Female", "Male", "OverAll Score", "University Rank"])

intdata = pd.DataFrame({
    "Student Type": ["International Student", "Domestic Student"],
    "University of Auckland": [32, 68],
    "Auckland University of Technology": [49, 51],
    "University of Otago": [19, 81],
    "Lincoln University": [44, 56],
    "Victoria University of Wellington": [20, 80],
    "University of Waikato": [31, 69],
    "Massey University": [29, 71],
    "University of Canterbury": [22, 78]
})

@capture("graph")
def studentnum(data_frame, x, y, title=None, text=None, template=None, color=None):
    fig_num = px.bar(data_frame=data_frame, x=x, y=y, title=title, text=text, template=template, color=color)
    
    fig_num.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    
    fig_num.update_layout(
        title=go.layout.Title(
            text="Number of students between universities",
            font=dict(
                family="Georgia, serif",
                size=25,
            ),
            xref="paper",
            x=0
        ),
        legend=dict(
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        ),
        # annotations=[
        #     dict(
        #         xref='paper', 
        #         yref='paper',
        #         x=0, 
        #         y=-0.6,
        #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
        #         showarrow=False,
        #         font=dict(
        #             family="Georgia, serif",
        #             size=12,
        #         )
        #     )
        # ],
    )
    
    fig_num.update_layout(
        font_family="Georgia, serif",
    )

    return fig_num


@capture("graph")
def gender(data_frame, x, y, title=None, orientation=None):
    fig_gender = px.bar(data_frame=data_frame, x=x, y=y, title=title, orientation=orientation)
    fig_gender.update_layout(barmode='stack')

    fig_gender.update_layout(
        legend=dict(
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        ),
        # annotations=[
        #     dict(
        #         xref='paper', 
        #         yref='paper',
        #         x=-0.5, 
        #         y=-0.1,  # Position below the chart
        #         showarrow=False,
        #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
        #         font=dict(
        #             family="Georgia, serif",
        #             size=12,
        #         ),
        #     )
        # ]
    ) 
    fig_gender.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="right",
        x=-0.2
    ))
    return fig_gender

# @capture("graph")
# def int1(data_frame, values=None, names=None, title=None):
#     fig_int1 = px.pie(data_frame=data_frame, values=values, names=names, title=title)
#     fig_int1.update_layout(
#         legend=dict(
#             font=dict(
#                 family="Georgia, serif",
#                 size=8,
#             )
#         ),
#         # annotations=[
#         #     dict(
#         #         xref='paper', 
#         #         yref='paper',
#         #         x=0.5, 
#         #         y=-0.1,  # Position below the chart
#         #         showarrow=False,
#         #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
#         #         font=dict(
#         #             family="Georgia, serif",
#         #             size=6,
#         #         ),
#         #     )
#         # ]
#     ) 
#     return fig_int1

# @capture("graph")
# def int2(data_frame, values=None, names=None, title=None):
#     fig_int2 = px.pie(data_frame=data_frame, values=values, names=names, title=title)
#     fig_int2.update_layout(
#         legend=dict(
#             font=dict(
#                 family="Georgia, serif",
#                 size=8,
#             )
#         ),
#         # annotations=[
#         #     dict(
#         #         xref='paper', 
#         #         yref='paper',
#         #         x=0.5, 
#         #         y=-0.1,  # Position below the chart
#         #         showarrow=False,
#         #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
#         #         font=dict(
#         #             family="Georgia, serif",
#         #             size=6,
#         #         ),
#         #     )
#         # ]
#     ) 
#     return fig_int2

# @capture("graph")
# def int3(data_frame, values=None, names=None, title=None):
#     fig_int3 = px.pie(data_frame=data_frame, values=values, names=names, title=title)
#     fig_int3.update_layout(
#         legend=dict(
#             font=dict(
#                 family="Georgia, serif",
#                 size=6,
#             )
#         ),
#         # annotations=[
#         #     dict(
#         #         xref='paper', 
#         #         yref='paper',
#         #         x=0.5, 
#         #         y=-0.1,  # Position below the chart
#         #         showarrow=False,
#         #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
#         #         font=dict(
#         #             family="Georgia, serif",
#         #             size=6,
#         #         ),
#         #     )
#         # ]
#     ) 
#     return fig_int3

# @capture("graph")
# def int4(data_frame, values=None, names=None, title=None):
#     fig_int4 = px.pie(data_frame=data_frame, values=values, names=names, title=title)
#     fig_int4.update_layout(
#         legend=dict(
#             font=dict(
#                 family="Georgia, serif",
#                 size=6,
#             )
#         ),
#         # annotations=[
#         #     dict(
#         #         xref='paper', 
#         #         yref='paper',
#         #         x=0.5, 
#         #         y=-0.1,  # Position below the chart
#         #         showarrow=False,
#         #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
#         #         font=dict(
#         #             family="Georgia, serif",
#         #             size=6,
#         #         ),
#         #     )
#         # ]
#     ) 
#     return fig_int4

# @capture("graph")
# def int5(data_frame, values=None, names=None, title=None):
#     fig_int5 = px.pie(data_frame=data_frame, values=values, names=names, title=title)
#     fig_int5.update_layout(
#         legend=dict(
#             font=dict(
#                 family="Georgia, serif",
#                 size=6,
#             )
#         ),
#         # annotations=[
#         #     dict(
#         #         xref='paper', 
#         #         yref='paper',
#         #         x=0.5, 
#         #         y=-0.1,  # Position below the chart
#         #         showarrow=False,
#         #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
#         #         font=dict(
#         #             family="Georgia, serif",
#         #             size=6,
#         #         ),
#         #     )
#         # ]
#     ) 
#     return fig_int5

# @capture("graph")
# def int6(data_frame, values=None, names=None, title=None):
#     fig_int6 = px.pie(data_frame=data_frame, values=values, names=names, title=title)
#     fig_int6.update_layout(
#         legend=dict(
#             font=dict(
#                 family="Georgia, serif",
#                 size=6,
#             )
#         ),
#         # annotations=[
#         #     dict(
#         #         xref='paper', 
#         #         yref='paper',
#         #         x=0.5, 
#         #         y=-0.1,  # Position below the chart
#         #         showarrow=False,
#         #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
#         #         font=dict(
#         #             family="Georgia, serif",
#         #             size=6,
#         #         ),
#         #     )
#         # ]
#     ) 
#     return fig_int6

# @capture("graph")
# def int7(data_frame, values=None, names=None, title=None):
#     fig_int7 = px.pie(data_frame=data_frame, values=values, names=names, title=title)
#     fig_int7.update_layout(
#         legend=dict(
#             font=dict(
#                 family="Georgia, serif",
#                 size=6,
#             )
#         ),
#         # annotations=[
#         #     dict(
#         #         xref='paper', 
#         #         yref='paper',
#         #         x=0.5, 
#         #         y=-0.1,  # Position below the chart
#         #         showarrow=False,
#         #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
#         #         font=dict(
#         #             family="Georgia, serif",
#         #             size=6,
#         #         ),
#         #     )
#         # ]
#     ) 
#     return fig_int7

# @capture("graph")
# def int8(data_frame, values=None, names=None, title=None):
#     fig_int8 = px.pie(data_frame=data_frame, values=values, names=names, title=title)
#     fig_int8.update_layout(
#         legend=dict(
#             font=dict(
#                 family="Georgia, serif",
#                 size=6,
#             )
#         ),
#         # annotations=[
#         #     dict(
#         #         xref='paper', 
#         #         yref='paper',
#         #         x=0.5, 
#         #         y=-0.1,  # Position below the chart
#         #         showarrow=False,
#         #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
#         #         font=dict(
#         #             family="Georgia, serif",
#         #             size=6,
#         #         ),
#         #     )
#         # ]
#     ) 
    return fig_int8
    
def create_basic_info():
    """Function returns a page to perform analysis on university level."""

    page_subject = vm.Page(
        title="Basic information",
        description="Discovering how different NZ universities are ranked through the years",
        layout=vm.Layout(grid=[[0]]),
        components=[
            vm.Tabs(
                tabs=[
                    vm.Container(
                        title="Student population",
                        layout=vm.Layout(grid=[[0, 0]] * 5 + [[1, -1]]),
                        components=[
                            vm.Graph(
                                id="studentnum",
                                figure=studentnum(
                                    data_frame=gapminder,
                                    x="Name of University",
                                    y="No of student",
                                    text="No of student",
                                    template="simple_white",
                                    color='No of student',
                                ),
                            ),
                            vm.Card(
                                text="""
                                Data Source:
                                
                                Alitaqi000. (2023). World University Rankings 2023 [Data set]. Kaggle. Retrieved August 16, 2024, from https://www.kaggle.com/datasets/alitaqi000/world-university-rankings-2023
                                
                                Times Higher Education. (n.d.). University of Auckland. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-auckland

                                Times Higher Education. (n.d.). University of Otago. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-otago
                                
                                Times Higher Education. (n.d.). Auckland University of Technology. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/auckland-university-technology
                                
                                Times Higher Education. (n.d.). Lincoln University. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/lincoln-university-1
                                
                                Times Higher Education. (n.d.). Victoria University of Wellington. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/victoria-university-wellington
                                
                                Times Higher Education. (n.d.). University of Waikato. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-waikato
                                
                                Times Higher Education. (n.d.). University of Canterbury. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-canterbury
                                
                                Times Higher Education. (n.d.). Massey University. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/massey-university


                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Gender Analysis",
                        layout=vm.Layout(grid=[[0,0]] * 5 + [[1,1]]),
                        components=[
                            vm.Graph(
                                id="gender",
                                figure=gender(
                                    data_frame=gapminder,
                                    x=["Female", "Male"],
                                    y="Name of University",
                                    title="Female and Male ratio",
                                    orientation='h',
                                ),
                            ),
                            vm.Card(
                                text="""
                                Data Source:
                                
                                Alitaqi000. (2023). World University Rankings 2023 [Data set]. Kaggle. Retrieved August 16, 2024, from https://www.kaggle.com/datasets/alitaqi000/world-university-rankings-2023
                                
                                Times Higher Education. (n.d.). University of Auckland. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-auckland

                                Times Higher Education. (n.d.). University of Otago. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-otago
                                
                                Times Higher Education. (n.d.). Auckland University of Technology. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/auckland-university-technology
                                
                                Times Higher Education. (n.d.). Lincoln University. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/lincoln-university-1
                                
                                Times Higher Education. (n.d.). Victoria University of Wellington. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/victoria-university-wellington
                                
                                Times Higher Education. (n.d.). University of Waikato. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-waikato
                                
                                Times Higher Education. (n.d.). University of Canterbury. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-canterbury
                                
                                Times Higher Education. (n.d.). Massey University. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/massey-university

                                """,
                            ),
                        ],
                    ),
                    # vm.Container(
                    #     title="International/Domestic Analysis",
                    #     layout=vm.Layout(grid=[[0, 0]]),
                    #     components=[
                    #         vm.Graph(
                    #             id="int1",
                    #             figure=int1(
                    #                 data_frame=intdata,
                    #                 values='University of Auckland',
                    #                 names='Student Type',
                    #                 title="University of Auckland",
                    #             ),
                    #         ),
                    #     ],
                    #     controls=[
                    #         vm.Parameter(
                    #             targets=["int1.y"],
                    #             selector=vm.Dropdown(
                    #                 options=[
                    #                     "University of Auckland", 
                    #                     "Auckland University of Technology", 
                    #                     "University of Otago", 
                    #                     "Lincoln University", 
                    #                     "Victoria University of Wellington", 
                    #                     "University of Waikato", 
                    #                     "Massey University", 
                    #                     "University of Canterbury"
                    #                 ], 
                    #                 multi=False, 
                    #                 value="University of Auckland", 
                    #                 title="Choose university"
                    #             ),
                    #         ),
                    #     ],
                    # ),
                ],
            ),
        ],
    )
    
    return page_subject


@capture("graph")
def int1(data_frame, values=None, names=None, title=None):
    fig_int1 = px.pie(data_frame=data_frame, values=values, names=names, title=title)
    fig_int1.update_layout(
        legend=dict(
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        ),
        # Uncomment this section if you want to add annotations
        # annotations=[
        #     dict(
        #         xref='paper', 
        #         yref='paper',
        #         x=0.5, 
        #         y=-0.1,  # Position below the chart
        #         showarrow=False,
        #         text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
        #         font=dict(
        #             family="Georgia, serif",
        #             size=6,
        #         ),
        #     )
        # ]
    )
    return fig_int1

def create_int():
    """Function returns a page to perform analysis on university level."""

    page_int = vm.Page(
        title="International vs Domestic",
        description="Discovering how different NZ universities are ranked through the years",
        layout=vm.Layout(grid=[[0,0]] * 5 + [[1,1]]),
        components=[
            vm.Graph(
                id="int1",
                figure=int1(
                    data_frame=intdata,
                    values='University of Auckland',
                    names='Student Type',
                    title="University of Auckland",
                ),
            ),
             vm.Card(
                                text="""
                                Data Source:
                                
                                Alitaqi000. (2023). World University Rankings 2023 [Data set]. Kaggle. Retrieved August 16, 2024, from https://www.kaggle.com/datasets/alitaqi000/world-university-rankings-2023
                                
                                Times Higher Education. (n.d.). University of Auckland. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-auckland

                                Times Higher Education. (n.d.). University of Otago. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-otago
                                
                                Times Higher Education. (n.d.). Auckland University of Technology. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/auckland-university-technology
                                
                                Times Higher Education. (n.d.). Lincoln University. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/lincoln-university-1
                                
                                Times Higher Education. (n.d.). Victoria University of Wellington. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/victoria-university-wellington
                                
                                Times Higher Education. (n.d.). University of Waikato. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-waikato
                                
                                Times Higher Education. (n.d.). University of Canterbury. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/university-canterbury
                                
                                Times Higher Education. (n.d.). Massey University. Retrieved August 16, 2024, from https://www.timeshighereducation.com/world-university-rankings/massey-university

                                """,
                            ),
        ],
        controls=[
            vm.Parameter(
                targets=["int1.values"],
                selector=vm.Dropdown(
                    options=[
                        "University of Auckland", 
                        "Auckland University of Technology", 
                        "University of Otago", 
                        "Lincoln University", 
                        "Victoria University of Wellington", 
                        "University of Waikato", 
                        "Massey University", 
                        "University of Canterbury"
                    ], 
                    multi=False, 
                    value="University of Auckland", 
                    title="Choose university"
                ),
            ),
        ],
    )
    return page_int

## 📊 Home Page

def create_home_page():
    """Function returns the Home page."""

    tab_1 = vm.Container(
        title="🧑‍🎓 Visual Analytics of NZ universities",
        layout=vm.Layout(grid=[[0, 1, 5], [2, 3, 4]], row_gap="18px", col_gap="18px"),
        components=[
            
            vm.Card(
                text="""
                    ###  Introduction page 
                    Start Here: Discover Your Path!
                """,
                href="intro",
            ),
            vm.Card(
                text="""
                       ### 📈 Universities' Metrics 
                        Uni Scores: Explore the Leaders!
                    """,
                href="/universities-scores-in-metrics",
            ),
            vm.Card(
                text="""
                    ### 📊 Rankings through the years
                    Ranking Trends: See the yearly trends
                   
                """,
                href="/rankings-through-the-years",
            ),
            vm.Card(
                text="""
                    ### 🧠 Rankings by subject field
                    Find Your Niche: Top Unis by Subject
                """,
                href="/uni-rankings-by-subject",
            ),
             vm.Card(
                text="""
                    ### Basic information about our universities 
                    Discover student population and gender ratios in our universities
                """,
                href="/basic-information",
            ),
            vm.Card(
                text="""
                    ### International vs Domestic
                    Explore the ratio between International and Domestic students 
                """,
                href="/international-vs-domestic",
            ),
        ],
    )


    page_home = vm.Page(
        title="Home",
        # description="Intelligence Dashboard for Analytics-Experience project.",
        description="[Research Project] Predicting Air Particulate Matter at Scale.",
        # components=[vm.Tabs(tabs=[tab_1, tab_2, tab_3, tab_4, tab_5])], 
        components=[vm.Tabs(tabs=[tab_1])], 
                   # controls=[
                   #     # vm.Filter(column='Site', selector=vm.Dropdown(value=['ALL'])),
                   #     vm.Filter(column='Site', selector=vm.Dropdown(value="Penrose", multi=False, title="Select Location")),
                   # ],
        )

    return page_home                   

## 📊 Dashboard

# IS_JUPYTERLAB = 'true'

dashboard = vm.Dashboard(
    pages=[
        create_home_page(),
        create_intro(),
        create_rankings_years(),
        create_metrics(),
        create_subject(),
        create_basic_info(),
        create_int(),
        
    ],
    navigation=vm.Navigation(
        nav_selector=vm.NavBar(
            items=[
                vm.NavLink(label="Home", pages=["Home"], icon="Home"),  # Added comma here
                vm.NavLink(label="Introduction", pages=["Intro"], icon="Waving Hand"),
                vm.NavLink(
                    label="Rankings through the years",
                    pages=["Rankings through the years"],
                    icon="Timeline",
                ),
                 vm.NavLink(
                    label="Universities' Metrics",
                    pages=["Universities' Scores in metrics"],
                    icon="Grade",
                ),
                vm.NavLink(
                    label="Rankings of subject field",
                    pages=["Uni rankings by subject"],
                    icon="Auto Stories",
                ),
                vm.NavLink(
                    label="Basic data",
                    pages=["Basic information"],
                    icon="Stacks",
                ),
                vm.NavLink(label="International vs Domestic", pages=["International vs Domestic"], icon="Globe"),
            ]
        ),
    ),
)

# if not IS_JUPYTERLAB:
#     app = Vizro().build(dashboard)
#     server = app.dash.server
    
#     if __name__ == "__main__":  
#         app.run(port=8080)
# else:
#     Vizro(assets_folder="assets").build(dashboard).run(port=8082)

app = Vizro().build(dashboard)
server = app.dash.server
    
if __name__ == "__main__":  
    app.run()



